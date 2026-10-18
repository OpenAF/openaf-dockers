set -eu
fail() { printf 'openaf-docker: %s\n' "$*" >&2; exit 1; }
PATH=/openaf:$PATH
export PATH
for tool in openaf ojob oafp; do
    [ -x "/openaf/$tool" ] || fail "image lacks /openaf/$tool"
done
# Register unknown numeric users only in the disposable container, using the
# image's existing group-writable passwd policy. Java obtains user.home here.
uid=$(id -u)
gid=$(id -g)
home=$(awk -F: -v uid="$uid" '$3 == uid { print $6; exit }' /etc/passwd)
if [ -z "$home" ]; then
    [ -w /etc/passwd ] || fail 'unknown UID and /etc/passwd is not writable; use OPENAF_DOCKER_USER=image or a compatible image'
    home=$(mktemp -d /tmp/openaf-cli.XXXXXX) || fail 'cannot create private home'
    printf 'openaf-cli-%s:x:%s:%s:OpenAF CLI:%s:/bin/sh\n' "$uid" "$uid" "$gid" "$home" >> /etc/passwd
fi
[ -d "$home" ] && [ -w "$home" ] || fail 'image user home is not writable; choose a compatible UID/image'
HOME=$home
export HOME
[ -w /openaf ] || fail '/openaf is not writable for this identity; use a compatible image or user setting'
if [ -n "${OPACKS:-}" ] || [ -n "${OPACKS_DIR:-}" ] || [ -n "${OPACKS_DB:-}" ] || [ "${OAF_ORIG+x}" = x ]; then
    [ -r /openaf/.docker/installOPacks.js ] || fail 'image lacks the oPack installation helper'
    [ ! -e /openaf/.opack.db ] || [ -w /openaf/.opack.db ] || fail 'image oPack database is not writable'
    (
        # Empty values retain their application semantics, but must not become
        # empty installation requests in the helper subprocess.
        [ -n "${OPACKS:-}" ] || unset OPACKS
        [ -n "${OPACKS_DIR:-}" ] || unset OPACKS_DIR
        [ -n "${OPACKS_DB:-}" ] || unset OPACKS_DB
        /openaf/openaf -c "$OPENAF_CLI_BOOTSTRAP_JS"
    ) </dev/null >&2 || exit $?
fi
# addOPackRemoteDB affects only the bootstrap JVM. Carry requested repositories
# into the application using OpenAF's native environment interface.
if [ -n "${OPACKS_DB:-}" ]; then
    OAF_OPACKS=${OAF_OPACKS:+$OAF_OPACKS,}$OPACKS_DB
    export OAF_OPACKS
fi
unset OPENAF_CLI_BOOTSTRAP_JS
case "$1" in openaf|ojob|oafp) command=$1; shift ;; *) fail 'invalid internal selector' ;; esac
exec "/openaf/$command" "$@"
