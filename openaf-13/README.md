# OpenAF (Java 13)

## Overview

`openaf/openaf-13` targets OpenJDK 13 and enables JVM settings tuned for container workloads (`-XX:+UseContainerSupport`, idle GC tuning, etc.). It is primarily useful for regression testing and benchmarking OpenAF against this JVM release.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest OpenAF build on top of OpenJDK 13. |
| `nightly` | Nightly refresh of the Java 13 variant. |

## Usage

```sh
docker run --rm -ti openaf/openaf-13:latest
```

Use the standard OpenAF entrypoint variables (`OPACKS`, `OPENAF`, `OJOB`, `OPACK_EXEC`, `OAFP`) to tailor the container to your workloads.

## Build from source

```sh
docker build \
  -t openaf/openaf-13:local \
  --build-arg DIST=latest \
  --build-arg OPENAFDIST= \
  https://github.com/OpenAF/openaf-dockers.git#:openaf-13
```

| Build arg    | Description |
|--------------|-------------|
| `DIST`       | Docker tag to assign to the resulting image (`latest`, `nightly`, ...). |
| `OPENAFDIST` | OpenAF distribution to download (empty for stable, `nightly`, etc.). |
