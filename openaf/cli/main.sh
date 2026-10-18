# Generated standalone OpenAF Docker CLI. Source: openaf/cli/. Do not edit.
# OPENAF_DOCKER_MANAGED_SCRIPT_V1
# POSIX syntax deliberately shared by Bash 3.2+ and Zsh.
set -eu
fail() { printf 'openaf-docker: %s\n' "$*" >&2; exit 2; }
usage() {
    cat <<'HELP'
Usage: openaf-docker {oafp|ojob|openaf|oaf} [application arguments...]
       openaf-docker --install|--update [--aliases] [--replace-aliases]
                     [--bin-dir DIR] [--rc-file FILE]

Install/update from this local script; aliases are opt-in. No downloads or image pulls.
Configuration (exported variables):

  OPENAF_DOCKER_IMAGE     openaf/openaf:latest (tag or digest)
  OPENAF_DOCKER_READONLY  false | true (workspace mount only)
  OPENAF_DOCKER_TTY       auto | never | always
  OPENAF_DOCKER_USER      host | image | numeric UID:GID
  OPENAF_DOCKER_ENV       comma-separated additional exported names

Forwarded by default: OAF_JARGS, OPACKS, OPACKS_DB; OPACKS_DIR maps a host directory.
Only the physical current directory is mounted at /work. Create output directories first.
Native-named aliases pass all options, including --help, to their selected application.
HELP
}
# Determine the invoked source without readlink -f (installation may use a link).
cli_self=$0
case "$cli_self" in */*) ;; *) cli_self=$(command -v "$cli_self") ;; esac
cli_basename=${0##*/}
case "$cli_basename" in
    oafp|ojob|openaf|oaf) cli_selector=$cli_basename ;;
    *)
        case "${1:-}" in
            --help|-h) usage; exit 0 ;;
            --install|--update) cli_install "$@"; exit 0 ;;
            oafp|ojob|openaf|oaf) cli_selector=$1; shift ;;
            *) fail 'expected oafp, ojob, openaf, or oaf; see --help' ;;
        esac ;;
esac
# oaf is the native short name for the same OpenAF launcher.
case "$cli_selector" in oaf) cli_selector=openaf ;; esac
command -v docker >/dev/null 2>&1 || fail 'docker executable not found in PATH'
case "$(command -v docker)" in *.exe) fail 'use the Linux docker CLI inside WSL2; docker.exe is unsupported' ;; esac
cli_image=${OPENAF_DOCKER_IMAGE-openaf/openaf:latest}
case "$cli_image" in ''|-*|*[[:space:]]*) fail 'OPENAF_DOCKER_IMAGE must be a nonempty image reference without whitespace' ;; esac
cli_readonly=${OPENAF_DOCKER_READONLY-false}
case "$cli_readonly" in true|false) ;; *) fail 'OPENAF_DOCKER_READONLY must be true or false' ;; esac
cli_tty=${OPENAF_DOCKER_TTY-auto}
case "$cli_tty" in auto|never|always) ;; *) fail 'OPENAF_DOCKER_TTY must be auto, never, or always' ;; esac
cli_user=${OPENAF_DOCKER_USER-host}
case "$cli_user" in
    host|image) ;;
    *:*) cli_uid=${cli_user%%:*}; cli_gid=${cli_user#*:}
         case "$cli_uid" in ''|*[!0-9]*) fail 'OPENAF_DOCKER_USER must be host, image, or numeric UID:GID' ;; esac
         case "$cli_gid" in ''|*[!0-9]*) fail 'OPENAF_DOCKER_USER must be host, image, or numeric UID:GID' ;; esac ;;
    *) fail 'OPENAF_DOCKER_USER must be host, image, or numeric UID:GID' ;;
esac
cli_work=$(pwd -P && printf .) || fail 'cannot resolve current directory'
cli_work=${cli_work%.}
cli_work=${cli_work%?}
[ "$cli_work" != / ] || fail 'refusing to mount the host filesystem root'
# Docker --mount uses CSV parsing. Reject delimiters rather than silently bind
# another source. Spaces, apostrophes, colons, dollars and globs are supported.
cli_cr=$(printf '\r')
cli_mount_path() {
    case "$1" in *','*|*'"'*|*'
'*|*"$cli_cr"*) fail 'mount source contains unsupported comma, double quote, CR, or newline' ;; esac
    [ -d "$1" ] || fail "mount source is not a directory: $1"
}
cli_mount_path "$cli_work"
cli_opacks_dir=
if printenv OPACKS_DIR >/dev/null 2>&1 && [ -n "${OPACKS_DIR:-}" ]; then
    cli_opacks_dir=$(CDPATH='' cd -- "$OPACKS_DIR" && pwd -P && printf .) || fail 'OPACKS_DIR must name an existing host directory'
    cli_opacks_dir=${cli_opacks_dir%.}
    cli_opacks_dir=${cli_opacks_dir%?}
    cli_mount_path "$cli_opacks_dir"
fi
# Build Docker's argv around the original application argv. No string execution.
set -- "$cli_selector" "$@"
set -- "$cli_image" -c "$cli_bootstrap" openaf-cli "$@"
set -- --entrypoint /bin/sh "$@"
if [ "$cli_readonly" = true ]; then cli_mount="type=bind,src=$cli_work,dst=/work,readonly"; else cli_mount="type=bind,src=$cli_work,dst=/work"; fi
set -- --mount "$cli_mount" --workdir /work "$@"
if [ -n "$cli_opacks_dir" ]; then
    set -- --mount "type=bind,src=$cli_opacks_dir,dst=/_openaf_cli/opacks,readonly" --env OPACKS_DIR=/_openaf_cli/opacks "$@"
elif printenv OPACKS_DIR >/dev/null 2>&1; then
    set -- --env OPACKS_DIR "$@"
fi
case "$cli_user" in
    host) set -- --user "$(id -u):$(id -g)" --group-add 0 "$@" ;;
    image) ;;
    *) set -- --user "$cli_user" --group-add 0 "$@" ;;
esac
if [ "$cli_tty" = always ]; then
    [ -t 0 ] || fail 'OPENAF_DOCKER_TTY=always requires terminal stdin'
    set -- --tty "$@"
elif [ "$cli_tty" = auto ] && [ -t 0 ] && [ -t 1 ] && [ -t 2 ]; then
    set -- --tty "$@"
fi
# Check presence one name at a time; never parse values or the full environment.
cli_names=OAF_JARGS,OPACKS,OPACKS_DB,TERM
if [ -n "${OPENAF_DOCKER_ENV:-}" ]; then cli_names=$cli_names,$OPENAF_DOCKER_ENV; fi
cli_seen=,
while :; do
    cli_name=${cli_names%%,*}
    case "$cli_name" in ''|[!a-zA-Z_]*|*[!a-zA-Z0-9_]*) fail 'OPENAF_DOCKER_ENV contains an invalid or empty name' ;; esac
    case "$cli_name" in
        OPENAF_DOCKER_*|OPENAF_CLI_*|cli_*|PATH|HOME|PWD|OLDPWD|CDPATH|IFS|ENV|BASH_ENV|SHELLOPTS|BASHOPTS|ZDOTDIR|OAF_HOME|OAF_DIR|OAF_OPACKS|JAVA_HOME|OPENAF|OJOB|OAFP|OPACK_EXEC|OPACKS_DIR|TINI_*) fail "reserved environment name: $cli_name" ;;
    esac
    case "$cli_seen" in *",$cli_name,"*) ;;
        *) cli_seen=$cli_seen$cli_name,
           if printenv "$cli_name" >/dev/null 2>&1; then set -- --env "$cli_name" "$@"; fi ;;
    esac
    case "$cli_names" in *,*) cli_names=${cli_names#*,} ;; *) break ;; esac
 done
# Docker's init forwards signals to the launcher's process group, including Java.
exec docker run --rm --interactive --init --env TINI_KILL_PROCESS_GROUP=1 "$@"
