# OpenAF Console

## Overview

`openaf/openaf-console` extends the base OpenAF image so it launches the interactive OpenAF console (`openaf-console`) immediately after container start. It is ideal for troubleshooting and exploratory automation because it keeps all of the base image functionality (oPack installation, custom scripts, oJobs) while dropping you straight into the console.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest stable console image. |
| `nightly` | Nightly build of the console image. |
| `t8` | Developer build aligned with the `t8` OpenAF distribution. |

## Usage

Launch the console with an ephemeral container:

```sh
docker run --rm -ti openaf/openaf-console:latest
```

Install additional oPacks before the console starts:

```sh
docker run --rm -ti \
  -e OPACKS=APIs,Docker \
  openaf/openaf-console:nightly
```

Run the console with a custom startup script (executed via `OPENAF`) and keep the console session alive:

```sh
docker run --rm -ti \
  -v "$PWD/startup":/startup \
  -e OPENAF=/startup/init.js \
  openaf/openaf-console:latest
```

## Configuration

The image reuses the same entrypoint as `openaf/openaf`, which means you can set `OPACKS`, `OPACKS_DIR`, `OPACKS_DB`, `OPENAF`, `OJOB`, and `OPACK_EXEC` exactly the same way. After those optional steps run, the container execs into `openaf-console`.

## Build from source

```sh
docker build \
  -t openaf/openaf-console:local \
  --build-arg DIST=latest \
  https://github.com/OpenAF/openaf-dockers.git#:openaf-console
```
