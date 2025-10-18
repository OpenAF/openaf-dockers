# OpenAF (Java 8)

## Overview

`openaf/openaf-8` is the legacy OpenAF runtime built on Alpine Linux with OpenJDK 8. It keeps the same entrypoint as the main image but stays on Java 8 for workloads that cannot yet upgrade to modern JDKs.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest stable build with OpenJDK 8. |
| `nightly` | Nightly build refreshed from the latest sources. |
| `t8` | Developer build aligned with the `t8` OpenAF distribution. |

## Usage

```sh
docker run --rm -ti openaf/openaf-8:latest
```

Because the entrypoint is identical to `openaf/openaf`, you can rely on the same environment variables (`OPACKS`, `OPENAF`, `OJOB`, etc.) to customise behaviour.

## Build from source

```sh
docker build \
  -t openaf/openaf-8:local \
  --build-arg DIST=latest \
  --build-arg OPENAFDIST= \
  https://github.com/OpenAF/openaf-dockers.git#:openaf-8
```

| Build arg    | Description |
|--------------|-------------|
| `DIST`       | Docker tag to assign to the resulting image (`latest`, `nightly`, `t8`, ...). |
| `OPENAFDIST` | Which OpenAF distribution to download (empty string for stable, `nightly`, etc.). |
