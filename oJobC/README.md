# oJobC

## Overview

`openaf/openaf-ojobc` packages the OpenAF runtime together with the `ojob-common` oPack so that common helpers are immediately available to your jobs. Like `openaf/openaf-ojob`, it runs an oJob as soon as the container starts and defaults to the bundled `/openaf/main.yaml`.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest stable build with `ojob-common` pre-installed. |
| `nightly` | Nightly variant built from the latest OpenAF sources. |
| `t8` | Developer build aligned with the `t8` OpenAF distribution. |

## Usage

Execute the default oJob (which assumes `ojob-common` is present):

```sh
docker run --rm -ti openaf/openaf-ojobc:latest
```

Run a custom oJob that relies on `ojob-common`:

```sh
docker run --rm -ti \
  -v "$PWD/jobs":/ojobs \
  -e OJOB=/ojobs/main.yaml \
  openaf/openaf-ojobc:nightly
```

Install additional oPacks before the job runs:

```sh
docker run --rm -ti \
  -e OPACKS=Mongo,Prometheus \
  openaf/openaf-ojobc:latest
```

## Configuration

All environment variables supported by `openaf/openaf` are available (`OPACKS`, `OPACKS_DIR`, `OPACKS_DB`, `OPENAF`, `OPACK_EXEC`, `OAFP`). This image sets `OJOB=/openaf/main.yaml` by default, and it installs `ojob-common` during the build stage so the corresponding commands are ready to use when the container starts.

Persistent state or additional configuration can be mounted into `/openaf` or whichever paths your jobs require.

## Build from source

```sh
docker build \
  -t openaf/openaf-ojobc:local \
  --build-arg DIST=latest \
  https://github.com/OpenAF/openaf-dockers.git#:oJobC
```
