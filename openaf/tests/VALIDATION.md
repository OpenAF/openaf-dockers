# OpenAF host CLI validation

Validated on 2026-10-18. No image was built or published for this feature.

## Image and host

- Host: macOS arm64, Bash 3.2.57 and Zsh 5.9, Docker Desktop Linux containers.
- Published image: `openaf/openaf:latest`, OpenAF `20261015`, Linux arm64.
- Repository digest: `openaf/openaf@sha256:d208e1cd69826c669a81734831334b88a76aac10421366f3d2181387cfb8ff9d`.
- Local image ID: `sha256:b7fc5315536e15a8f1ace13a60856d136c31be9f870a07bb919b15e0c8c482fc`.

## Executed

- Offline contract suite with Bash and Zsh on macOS; also on Alpine Linux in an ephemeral container with Bash, Zsh and Python installed. Exact argv, exported/unset/empty/multiline environment, mounts, invalid settings, binary streams, status propagation, installation/update, alias activation and collision handling, and a real PTY matrix.
- Generated-file freshness; Bash, Zsh, macOS `/bin/sh` and Alpine `/bin/sh` syntax checks.
- ShellCheck using `koalaman/shellcheck:stable` in a disposable container. Generated literal-bootstrap quoting has scoped SC1003/SC2016 suppressions; shared variable references use SC2034/SC2154 exclusions.
- Bash and Zsh real-image integration: JSON/CSV, nested outputs, host redirection, OpenAF and oJob file fixtures, `OAF_JARGS`, writable private home and Java `user.home` with a non-image UID, local directory/archive oPacks, a local repository lookup after database-only bootstrap, empty variables, bootstrap failure, clean stdout, pipelines, exit status, and workspace read-only behavior.
- A deliberately missing remote package request failed and prevented application execution (Bash integration with `--network`).
- Real SIGINT and SIGTERM during bootstrap and application execution, with container removal verified by unique test labels.

## Source-backed deviations

The published helper checks `isFolder`, but `io.listFiles` returns `isDirectory`.
The wrapper adapts only the explicit OPACKS_DIR listing in the bootstrap process;
the repository helper accepts either field. This keeps published-image support
independent of releasing a corrected image. Package resolution remains in the
image helper. OpenAF's public log collection makes reported helper errors fatal,
including verification errors that otherwise coexist with an “installed” result.

The helper registers repositories only in its own JVM. The wrapper therefore
bridges OPACKS_DB into OpenAF's native OAF_OPACKS environment setting for the
application, with that name reserved from host forwarding. A local zipped
repository lookup verifies the application actually sees the added database.

The native oafp/ojob launchers serialize arguments, and launch Java without `exec`.
Wrapper argv preservation is tested independently of that native parser. Docker
init process-group forwarding was verified with real interruptions rather than
assuming the launchers forward signals themselves.

## Remaining limits

- WSL2 and `/mnt/c` have no available live test host. Their documented support boundary uses Linux Docker tooling; neither ownership behavior nor Windows-mounted filesystem semantics is claimed verified.
- Ordinary Linux host output ownership, rootless Docker, user-namespace remapping, other image families, and amd64 runtime execution were not validated on this macOS host. Linux offline tests do not establish those runtime properties.
- Real forced-TTY interactive OpenAF session parity was not established; the TTY selection matrix is verified with a mock Docker and PTYs.
- `OAF_ORIG` downloading is opt-in and was not executed. No automatic image builds, pulls per invocation, package cache, or persistent containers were introduced.
- Generated scripts are tested as executables; sourcing the entire script into a user's shell is unsupported. Only the managed alias block is sourced.

## oaf alias extension

Offline coverage includes `oaf` selector/basename dispatch to `openaf`, native help
forwarding, managed alias activation, upgrading older alias blocks, and refusal
to shadow an existing native `oaf` without explicit opt-in.

The extended offline suite passed for Bash and Zsh on macOS. Both standalone
scripts also passed a real-container `oaf -c` smoke test against the image above.
