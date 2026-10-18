# OpenAF

## Overview

`openaf/openaf` is the reference container image for running OpenAF scripts, oJobs, and oPack tooling. It is built on Alpine Linux and bundles OpenJDK 21 together with the OpenAF runtime, entrypoint helpers, and a non-root `openaf` user (UID 1000, GID 0) so it works well in Kubernetes and Podman environments.

## Available tags

| Tag     | Description |
|---------|-------------|
| `latest` | Latest stable build published to Docker Hub. |
| `nightly` | Nightly build produced from the most recent OpenAF sources. |
| `t8` | Developer build aligned with the `t8` OpenAF distribution. |

## Usage

Start an interactive shell with OpenAF on the `PATH`:

```sh
docker run --rm -ti openaf/openaf:latest
```

Run a script that is mounted from the host:

```sh
docker run --rm -ti \
  -v "$PWD/scripts":/scripts \
  -e OPENAF=/scripts/cleanup.js \
  openaf/openaf:latest
```

Execute an oJob definition:

```sh
docker run --rm -ti \
  -v "$PWD/jobs":/ojobs \
  -e OPACKS=APIs \
  -e OJOB=/ojobs/main.yaml \
  openaf/openaf:nightly
```

## Configuration

The entrypoint reacts to the following environment variables:

| Variable     | Description |
|--------------|-------------|
| `OPACKS`     | Comma-separated list of oPacks to install on first run (fetched from configured repositories). |
| `OPACKS_DIR` | Directory containing `.opack` files or unpacked oPack folders to install on first run. |
| `OPACKS_DB`  | Comma-separated list of remote oPack database URLs to add before installing oPacks. |
| `OPENAF`     | Path to a script inside the container that will be executed with `openaf`. |
| `OJOB`       | Path to an oJob file or ZIP that will be executed with `ojob`. |
| `OPACK_EXEC` | Name of an oPack executable to run with `opack exec` (extra arguments are passed through). |
| `OAFP`       | When present, runs `oafp` instead of the default entrypoint logic. |

Installation of requested oPacks happens only on the first container start and is tracked via `/openaf/.installed`. Without any of the variables above the container drops into `/bin/sh` with all OpenAF tools available on the `PATH`.

For persistent state (such as custom oPacks or logs) mount host storage into `/openaf`.

## Build from source

```sh
docker build \
  -t openaf/openaf:local \
  --build-arg DIST=latest \
  --build-arg OPENAFDIST=nightly \
  https://github.com/OpenAF/openaf-dockers.git#:openaf
```

| Build arg    | Description |
|--------------|-------------|
| `DIST`       | Selects the Docker distribution tag produced by the build (`latest`, `nightly`, `t8`, etc.). |
| `OPENAFDIST` | Chooses which OpenAF build to embed (empty string for stable, `nightly`, `edge`, ...). |

## Host CLI: Bash and Zsh

Run OpenAF tools with Docker and standard host shell utilities, without host Java
or OpenAF. Two standalone scripts are generated from one maintained implementation:
`bin/openaf-docker.bash` (Bash 3.2+) and `bin/openaf-docker.zsh` (Zsh). Choose the
script matching your shell. Execute scripts rather than sourcing them.

From a repository checkout, install either version:

```sh
bash openaf/bin/openaf-docker.bash --install
# Or:
zsh openaf/bin/openaf-docker.zsh --install

# Ensure the installation directory is on PATH (persist manually if needed):
export PATH="$HOME/.local/bin:$PATH"
openaf-docker --help
```

Installation copies the standalone script to `~/.local/bin/openaf-docker.bash`
or `.zsh`, and creates an `openaf-docker` symlink to it. Installing the other
version explicitly switches that managed symlink; both shell-specific scripts
can coexist. No companion source files are needed at runtime. Unrelated files or
symlinks at these destinations are never overwritten.

### Optional aliases and updates

Alias installation is explicit and persists one marked block in `~/.bashrc` or
`${ZDOTDIR:-$HOME}/.zshrc`:

```sh
bash openaf/bin/openaf-docker.bash --install --aliases
# Or:
zsh openaf/bin/openaf-docker.zsh --install --aliases
```

The block defines `openaf-docker`, `oafp`, `ojob`, `openaf`, and `oaf`, referring to the
absolute installed script. Configuration values are read on each invocation.
Existing native commands and recognizable unmanaged alias/function definitions
cause installation to stop. Use `--replace-aliases` only when you intend to shadow
them; native programs and unrelated startup content remain present. Dynamic
aliases created elsewhere cannot always be discovered. A definition later in your
startup sequence can override the managed aliases.

The installer never executes startup files. It prints a safely quoted `source`
command for activation; alternatively open a new shell. Bash login profiles must
source `.bashrc` for those aliases to load in a login shell. The installer does
not alter login profiles or PATH. Use `--bin-dir DIR` and `--rc-file FILE` for
custom destinations. For a symlinked startup file, pass its actual target with
`--rc-file`. Changed startup files receive unique `.openaf-docker.backup.*`
backups. Repeated installation/update replaces the marked block without duplicates
or redundant backups; malformed blocks are rejected.

After updating your checkout, refresh the installed script and any existing
managed aliases:

```sh
bash openaf/bin/openaf-docker.bash --update
# Or:
zsh openaf/bin/openaf-docker.zsh --update
```

Use the same destination overrides as installation. Update reads the local script;
it performs no downloads, image updates, or implicit alias opt-in. To remove the
integration, delete its marked startup block, its installed shell-specific file,
and the managed symlink if no longer needed.

### Files, scripts, and pipelines

```sh
mkdir -p outputs
openaf-docker oafp file=inputs/data.csv in=csv out=json
openaf-docker ojob jobs/process.yaml
openaf-docker openaf -f scripts/process.js

# With optional aliases:
oafp file=inputs/data.json out=yaml outfile=outputs/data.yaml
oafp file=inputs/data.json out=json > outputs/data.json
cat inputs/data.json | oafp in=json out=yaml 2>outputs/errors.log
openaf -f scripts/process.js
oaf -f scripts/process.js  # Short alias for openaf
ojob jobs/process.yaml
```

Each invocation starts one foreground container with `--rm`, `--interactive`, and
`--init`. The physical current directory is mounted read-write at `/work`, which
is the working directory for every tool. Changing host directories changes the
next invocation's mount. Script paths do not change the working directory.
Create output directories yourself. Files appear immediately in both directions;
they are not uploaded or copied into the container.

Host absolute paths are not translated. Use paths relative to the mounted tree,
or explicit container paths. Relative symlinks within that tree work; absolute
symlinks and references outside it may fail. No host home, parent directory,
credentials, or Docker socket is mounted automatically. Invocation from `/` is
rejected. Spaces, apostrophes, colons, dollar signs and wildcard characters in
mount paths are supported; commas, double quotes, CR and newline are rejected
because Docker mount specifications have separate delimiter rules.

The wrapper passes original argument boundaries to each native launcher, including
empty arguments and literal metacharacters. Quote arguments normally in your host
shell. The image's `oafp` and `ojob` launchers subsequently serialize arguments
into OpenAF's native expression format; this can impose parsing limits beyond the
wrapper. The verified image also modifies terminal settings in its native
launchers. No parser or terminal restoration replacement is supplied here.
`openaf-docker --help` describes the wrapper; after a selector, help/options go
to the application. Native aliases always select their application first.

### Configuration and environment

Export settings, or use inline assignments:

| Variable | Default | Allowed values / purpose |
| --- | --- | --- |
| `OPENAF_DOCKER_IMAGE` | `openaf/openaf:latest` | Image tag or digest reference. |
| `OPENAF_DOCKER_READONLY` | `false` | `true` or `false`; workspace bind only. |
| `OPENAF_DOCKER_TTY` | `auto` | `auto`, `never`, `always`. |
| `OPENAF_DOCKER_USER` | `host` | `host`, `image`, numeric `UID:GID`. |
| `OPENAF_DOCKER_ENV` | empty | Comma-separated additional exported names. |

```sh
OAF_JARGS="-Xmx2g" openaf -f scripts/process.js
OPACKS="Tika,APIs" ojob jobs/process.yaml
OPACKS_DIR="./local opacks" ojob jobs/process.yaml
OPENAF_DOCKER_ENV=OAF_MODEL,OAF_LC_MODEL,OAF_DECIDE_MODEL,HTTPS_PROXY,NO_PROXY \
  openaf -f scripts/process.js
OPENAF_DOCKER_READONLY=true oafp file=inputs/data.json out=json > outputs/result.json
```

`OAF_JARGS`, `OPACKS`, `OPACKS_DB`, and `TERM` are forwarded when exported;
`OPACKS_DIR` has special path handling. Unset variables remain unset; exported
empty values remain empty for the application. Empty package requests are removed
only in the bootstrap subprocess. Unexported parent-shell variables are unavailable.
Values, including multiline values, are forwarded by name without printing them.
The extra-name list validates and deduplicates identifiers; it does not forward
all variables or infer prefixes. Model/proxy examples enable forwarding only.

Host `PATH`, `HOME`, `PWD`, OpenAF/Java installation paths, shell startup controls,
entrypoint selectors (`OPENAF`, `OJOB`, `OAFP`, `OPACK_EXEC`), mapped `OPACKS_DIR`,
and wrapper/init controls are reserved. `JAVA_ARGS` and other JVM variables may
be explicitly forwarded, but consumption depends on the selected launcher.
`JAVA_ARGS` is never translated into `OAF_JARGS`. Host paths embedded in arbitrary
values are never rewritten: JVM/configuration file references need container paths.
Explicitly allowlisting exported `OAF_ORIG` enables the image helper's original-JAR
download, including its presence semantics for an empty value; this needs network
access. It is never enabled by default.

### oPacks and image updates

Nonempty `OPACKS`, `OPACKS_DB` or `OPACKS_DIR` requests run the image's
`/openaf/.docker/installOPacks.js` before the application. Database-only requests
are supported. Because helper registration is local to its JVM, the wrapper also
maps nonempty `OPACKS_DB` into the application's native `OAF_OPACKS` repository
setting. `OPACKS_DB` itself stays unchanged; `OAF_OPACKS` is reserved for this
bridge, preserving and extending any value already supplied by the selected image. Package and repository syntax is the existing helper syntax.
`OPACKS_DIR` identifies a host directory, resolved from the caller's current
directory and mounted read-only at `/_openaf_cli/opacks`. It may be outside the
workspace because it is explicitly selected. This read-only view does not make
those files inaccessible through an overlapping writable workspace mount.

Bootstrap receives `/dev/null` as stdin and sends all output to stderr. The
wrapper uses OpenAF's public `startLog`/`dumpLog` APIs to make reported package
errors fatal, even when the helper returns normally. It also adapts directory
metadata for the published helper's `isFolder`/`isDirectory` mismatch, only during
bootstrap. The repository helper now accepts both fields. No package resolution
or download implementation is duplicated, and `/openaf/.installed` does not skip
explicit requests.

Every container has private runtime state: no persistent `/openaf` volume or shared
package cache. Repeated requests repeat bootstrap work. For frequent use, prepare
an image deliberately and remove runtime installation requests when unnecessary:

```sh
export OPENAF_DOCKER_IMAGE=my-prepared-openaf:version
openaf-docker ojob jobs/process.yaml
# Deliberately refresh the default image when wanted:
docker pull openaf/openaf:latest
```

Normal execution uses Docker's pull-if-missing policy, without a registry/daemon
preflight, automatic pull, OpenAF update, image build, or package upgrade.

### Permissions, terminals, and supported environments

The default identity is the caller's UID and primary GID, plus supplementary group
0 for this image family's writable runtime. It does not substitute primary GID 0
or fall back to root. Unknown UIDs receive a private home and an entry in the
already-writable container passwd file. Existing UIDs use their image home.
`HOME` and Java `user.home` were checked with a non-image UID. Incompatible home,
runtime or database permissions fail with a clear error. The wrapper does not
chmod/chown host files or mount the host home. Use `OPENAF_DOCKER_USER=image` or an
explicit numeric identity when intentionally choosing another policy.

Linux Docker, Docker Desktop, rootless Docker and user-namespace remapping can
produce different ownership behavior. Docker Desktop file sharing does not prove
ordinary Linux UID ownership equivalence. WSL scope is WSL2 with Linux `docker`
and Docker Desktop integration or an in-distro daemon. WSL1, Windows `docker.exe`,
PowerShell, Git Bash and other container engines are outside this implementation.
Test `/mnt/c` separately from the WSL Linux filesystem; Windows-mounted permission
semantics differ. See [validation evidence](tests/VALIDATION.md) for tested hosts
and remaining gaps.

TTY `auto` requires stdin, stdout **and** stderr to be terminals. Redirecting even
stderr disables it. `never` preserves separate streams; `always` requires terminal
stdin and merges terminal streams through Docker. Native tools using `/dev/tty`
may still behave differently when streams are redirected. Host shell redirection
is a host operation: a read-only workspace mount cannot prevent `> output.json`.
Private home/runtime/bootstrap writes remain permitted in read-only workspace mode.

Host-to-Docker and bootstrap-to-launcher handoffs use `exec`. Docker init forwards
signals to the launcher process group, including Java. Ordinary SIGINT/SIGTERM
interrupts and container removal are tested during bootstrap and application
execution. This does not guarantee cleanup after crashes, daemon failure or
untrappable signals. Docker/application failures retain their exit status.

Remote Docker binds refer to the **daemon host**, not the client's filesystem;
this wrapper does not transfer the current directory. Shell commands/dependencies
used by scripts must exist inside the image. Container `localhost` refers to the
container, not host services. Each call incurs container/JVM startup overhead.
A read-write workspace allows container code and installed oPacks to modify its
contents; run images and packages you trust.

### Development and tests

```sh
sh openaf/cli/generate.sh
sh openaf/cli/generate.sh --check
python3 openaf/tests/test_cli.py
bash -n openaf/bin/openaf-docker.bash
zsh -n openaf/bin/openaf-docker.zsh
# Requires a local image and daemon; no implicit integration-test pulls:
python3 openaf/tests/integration.py --image openaf/openaf:latest --shell bash
python3 openaf/tests/integration.py --image openaf/openaf:latest --shell zsh
# Optional remote missing-package failure test:
python3 openaf/tests/integration.py --image openaf/openaf:latest --network
```

Offline tests use Python's standard library, mock Docker argv/environment capture,
a real pseudo-terminal matrix, and fake bootstrap launchers. CI runs them with
Bash/Zsh on Linux/macOS and checks generated-file freshness and ShellCheck. They
prove wrapper contracts, not image behavior. Integration fixtures use local data
and oPacks; network-dependent checks are separate. Edit `cli/` sources and regenerate
both standalone outputs; never maintain separate Docker invocation logic.
