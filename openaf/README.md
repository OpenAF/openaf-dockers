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
