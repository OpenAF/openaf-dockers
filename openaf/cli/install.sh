cli_quote() { printf "'"; printf '%s' "$1" | sed "s/'/'\\\\''/g"; printf "'"; }
cli_managed_script() {
    [ -f "$1" ] && [ ! -L "$1" ] && head -n 5 "$1" | grep -q '^# OPENAF_DOCKER_MANAGED_SCRIPT_V1$'
}
cli_install() {
    cli_action=$1; shift
    cli_aliases=false
    cli_replace=false
    cli_bin=${HOME:?HOME must be set}/.local/bin
    if [ "$cli_shell" = zsh ]; then cli_rc=${ZDOTDIR:-$HOME}/.zshrc; else cli_rc=$HOME/.bashrc; fi
    while [ $# -gt 0 ]; do
        case "$1" in
            --aliases) cli_aliases=true; shift ;;
            --replace-aliases) cli_replace=true; shift ;;
            --bin-dir|--rc-file)
                [ $# -ge 2 ] && [ -n "$2" ] || fail "$1 requires a path"
                case "$1" in --bin-dir) cli_bin=$2 ;; *) cli_rc=$2 ;; esac
                shift 2 ;;
            *) fail "unknown installation option: $1" ;;
        esac
    done
    # Normalize without readlink -f; no startup file is sourced or executed.
    case "$cli_bin" in /*) ;; *) cli_bin=$PWD/$cli_bin ;; esac
    case "$cli_rc" in /*) ;; *) cli_rc=$PWD/$cli_rc ;; esac
    cli_target=$cli_bin/openaf-docker.$cli_shell
    if [ -e "$cli_target" ] || [ -L "$cli_target" ]; then
        cli_managed_script "$cli_target" || fail "refusing to replace unrelated installation: $cli_target"
    elif [ "$cli_action" = --update ]; then
        fail 'no managed installation to update; use --install first'
    fi
    cli_link=$cli_bin/openaf-docker
    if [ -e "$cli_link" ] || [ -L "$cli_link" ]; then
        [ -L "$cli_link" ] || fail "refusing to replace unrelated file: $cli_link"
        cli_link_target=$(readlink "$cli_link")
        case "$cli_link_target" in /*) ;; *) cli_link_target=$cli_bin/$cli_link_target ;; esac
        case "$cli_link_target" in "$cli_bin/openaf-docker.bash"|"$cli_bin/openaf-docker.zsh") ;; *) fail "unmanaged symlink: $cli_link" ;; esac
        cli_managed_script "$cli_link_target" || fail "unmanaged symlink target: $cli_link"
    fi
    cli_begin='# >>> openaf-docker managed aliases >>>'
    cli_end='# <<< openaf-docker managed aliases <<<'
    cli_had_block=false
    if [ -f "$cli_rc" ] && grep -q -F "$cli_begin" "$cli_rc"; then cli_had_block=true; fi
    if [ "$cli_action" = --update ] && [ "$cli_had_block" = true ]; then cli_aliases=true; fi
    cli_tmp=
    cli_copy=
    cli_newlink=
    cli_mode=
    trap 'rm -f -- "${cli_tmp:-}" "${cli_copy:-}" "${cli_newlink:-}" "${cli_mode:-}"' EXIT
    if [ "$cli_aliases" = true ]; then
        [ ! -L "$cli_rc" ] || fail 'startup file is a symlink; pass its actual target with --rc-file'
        [ ! -e "$cli_rc" ] || [ -f "$cli_rc" ] || fail 'startup file must be a regular file'
        [ -d "${cli_rc%/*}" ] || fail 'startup directory does not exist; use --rc-file'
        cli_tmp=$(mktemp "${cli_rc}.openaf-docker.XXXXXX") || fail 'cannot prepare startup update'
        if [ -f "$cli_rc" ]; then
            awk -v begin="$cli_begin" -v end="$cli_end" '
                $0 == begin { if (inside || seen++) exit 3; inside=1; next }
                $0 == end { if (!inside) exit 3; inside=0; next }
                !inside { print }
                END { if (inside) exit 3 }
            ' "$cli_rc" > "$cli_tmp" || fail 'malformed or duplicate managed alias block; repair it before installing'
        fi
        if [ "$cli_replace" != true ]; then
            if grep -E '(^|[;[:space:]])alias[[:space:]]+(openaf-docker|oafp|ojob|openaf|oaf)=|^[[:space:]]*(function[[:space:]]+)?(openaf-docker|oafp|ojob|openaf|oaf)[[:space:]]*\(' "$cli_tmp" >/dev/null; then
                fail 'unmanaged aliases/functions exist; use --replace-aliases to intentionally shadow them'
            fi
            for cli_native in openaf-docker oafp ojob openaf oaf; do
                # Existing aliases were already opted into. Newly added names
                # still need collision checks when updating an older block.
                if [ "$cli_had_block" = true ] && grep -q "^alias $cli_native=" "$cli_rc"; then continue; fi
                cli_found=$(command -v "$cli_native" 2>/dev/null || :)
                case "$cli_found" in ''|"$cli_link"|"$cli_target") ;; *) fail "$cli_native already exists ($cli_found); use --replace-aliases to intentionally shadow it" ;; esac
            done
        fi
        {
            printf '%s\n' "$cli_begin"
            printf '# Installed locally; configuration is read at invocation time.\n'
            for cli_native in openaf-docker oafp ojob openaf oaf; do
                cli_value=$(cli_quote "$cli_target")
                [ "$cli_native" = openaf-docker ] || cli_value="$cli_value $cli_native"
                printf 'alias %s=' "$cli_native"
                cli_quote "$cli_value"
                printf '\n'
            done
            printf '%s\n' "$cli_end"
        } >> "$cli_tmp"
    fi
    mkdir -p -- "$cli_bin"
    cli_copy=$(mktemp "$cli_bin/.openaf-docker.XXXXXX") || fail 'cannot prepare installed script'
    cp -- "$cli_self" "$cli_copy"
    chmod 755 "$cli_copy"
    if [ ! -f "$cli_target" ] || ! cmp -s "$cli_copy" "$cli_target"; then mv -f -- "$cli_copy" "$cli_target"; fi
    cli_newlink=$cli_bin/.openaf-docker-link.$$
    ln -s "openaf-docker.$cli_shell" "$cli_newlink"
    mv -f -- "$cli_newlink" "$cli_link"
    if [ "$cli_aliases" = true ]; then
        if [ ! -f "$cli_rc" ] || ! cmp -s "$cli_tmp" "$cli_rc"; then
            if [ -f "$cli_rc" ]; then
                cli_backup=$(mktemp "${cli_rc}.openaf-docker.backup.XXXXXX")
                cp -p -- "$cli_rc" "$cli_backup"
                # Preserve the existing startup file's permissions.
                cli_mode=$(mktemp "${cli_rc}.openaf-docker.XXXXXX")
                cp -p -- "$cli_rc" "$cli_mode"
                cat "$cli_tmp" > "$cli_mode"
                mv -f -- "$cli_mode" "$cli_rc"
                printf 'Backup: %s\n' "$cli_backup"
            else
                mv -- "$cli_tmp" "$cli_rc"
            fi
        fi
        printf 'Activate in a new shell, or run: source '
        cli_quote "$cli_rc"
        printf '\n'
    fi
    printf 'Installed: %s\nAdd its directory to PATH if needed. Image updates remain explicit: docker pull openaf/openaf:latest\n' "$cli_target"
    rm -f -- "${cli_tmp:-}" "${cli_copy:-}" "${cli_newlink:-}" "${cli_mode:-}"
    trap - EXIT
}
