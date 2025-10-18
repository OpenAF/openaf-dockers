# oJob

## Overview

`openaf/openaf-ojob` is a convenience image that bootstraps the OpenAF runtime to execute an oJob when the container starts. It inherits from `openaf/openaf` and ships a default `/openaf/main.yaml` so you can drop an oJob into the container (or mount one from the host) and have it executed automatically.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest stable oJob runtime. |
| `nightly` | Nightly build aligned with the nightly OpenAF distribution. |
| `t8` | Developer build aligned with the `t8` OpenAF distribution. |

## Usage

Run the default oJob (`/openaf/main.yaml`):

```sh
docker run --rm -ti openaf/openaf-ojob:latest
```

Execute a custom oJob mounted from the host:

```sh
docker run --rm -ti \
  -v "$PWD/jobs":/ojobs \
  -e OJOB=/ojobs/pipeline.yaml \
  -e OPACKS=APIs,Prometheus \
  openaf/openaf-ojob:nightly
```

Override the default oJob arguments:

```sh
docker run --rm \
  -e OJOB=/openaf/main.yaml \
  openaf/openaf-ojob:latest --var project=demo
```

## Configuration

All of the base image options (`OPACKS`, `OPACKS_DIR`, `OPACKS_DB`, `OPENAF`, `OPACK_EXEC`, `OAFP`) are available. This image sets `OJOB=/openaf/main.yaml` by default; if you define your own `OJOB` the entrypoint will execute that file (or ZIP) instead.

To persist state (config, secrets, custom oPacks) mount a volume into `/openaf` or bind mount the directories your oJob expects.

## Build from source

```sh
docker build \
  -t openaf/openaf-ojob:local \
  --build-arg DIST=latest \
  https://github.com/OpenAF/openaf-dockers.git#:oJob
```
