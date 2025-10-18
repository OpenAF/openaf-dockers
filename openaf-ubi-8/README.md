# OpenAF (UBI + Java 8)

## Overview

`openaf/openaf-ubi-8` is the Red Hat UBI-based OpenAF runtime that stays on OpenJDK 8. It installs shell helpers from ojob.io for auto-completion, runs as user `openaf` (UID 1000, GID 0), and keeps the standard OpenAF entrypoint logic.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest stable UBI + Java 8 build. |
| `nightly` | Nightly refresh from the latest OpenAF sources. |

## Usage

```sh
docker run --rm -ti openaf/openaf-ubi-8:latest
```

Mount a directory with your oJobs and run them directly:

```sh
docker run --rm -ti \
  -v "$PWD/jobs":/ojobs \
  -e OJOB=/ojobs/main.yaml \
  openaf/openaf-ubi-8:latest
```

The image supports all usual OpenAF configuration variables (`OPACKS`, `OPACKS_DIR`, `OPACKS_DB`, `OPENAF`, `OJOB`, `OPACK_EXEC`, `OAFP`) and honours `JVM_MEMMXPERC` / `JVM_MEMMSPERC` to tune the JVM memory percentages exposed via `JAVA_ARGS`.

## Build from source

```sh
docker build \
  -t openaf/openaf-ubi-8:local \
  --build-arg DIST=latest \
  --build-arg OPENAFDIST= \
  https://github.com/OpenAF/openaf-dockers.git#:openaf-ubi-8
```

| Build arg    | Description |
|--------------|-------------|
| `DIST`       | Docker tag to assign to the resulting image (`latest`, `nightly`, ...). |
| `OPENAFDIST` | OpenAF distribution to embed (empty for stable, `nightly`, etc.). |
