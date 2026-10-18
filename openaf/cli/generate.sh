#!/bin/sh
# Generate both standalone scripts. --check leaves the checkout untouched.
set -eu
base=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd -P)
task_tmp=$(mktemp -d)
trap 'rm -rf "$task_tmp"' EXIT HUP INT TERM
for shell in bash zsh; do
    output=$task_tmp/openaf-docker.$shell
    {
        printf '#!/usr/bin/env %s\n' "$shell"
        printf '# Generated standalone OpenAF Docker CLI. Do not edit.\n'
        printf '# OPENAF_DOCKER_MANAGED_SCRIPT_V1\n'
        printf 'cli_shell=%s\n' "$shell"
        # Zsh's default lack of sh-style splitting is fine: all argv are quoted.
        cat "$base/install.sh"
        {
            printf "OPENAF_CLI_BOOTSTRAP_JS='"
            sed "s/'/'\\\\''/g" "$base/bootstrap.js"
            printf "'\n"
            cat "$base/bootstrap.sh"
        } > "$task_tmp/bootstrap"
        printf '# shellcheck disable=SC1003,SC2016\n'
        printf "cli_bootstrap='"
        sed "s/'/'\\\\''/g" "$task_tmp/bootstrap"
        printf "'\n"
        cat "$base/main.sh"
    } > "$output"
    if [ "${1:-}" = --check ]; then
        cmp "$output" "$base/../bin/openaf-docker.$shell"
    else
        cp "$output" "$base/../bin/openaf-docker.$shell"
        chmod 755 "$base/../bin/openaf-docker.$shell"
    fi
done
