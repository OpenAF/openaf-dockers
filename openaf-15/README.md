# OpenAF (Java 15)

## Overview

`openaf/openaf-15` is an experimental build that packages OpenAF with OpenJDK 15 on Alpine Linux. It follows the same entrypoint conventions as the main image and is best suited for validating compatibility with Java 15.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest OpenAF build targeting OpenJDK 15. |
| `nightly` | Nightly refresh of the Java 15 variant. |

## Usage

```sh
docker run --rm -ti openaf/openaf-15:latest
```

All standard OpenAF environment variables (`OPACKS`, `OPENAF`, `OJOB`, `OPACK_EXEC`, `OAFP`) remain available for customising behaviour.

## Build from source

```sh
docker build \
  -t openaf/openaf-15:local \
  --build-arg DIST=latest \
  --build-arg OPENAFDIST= \
  https://github.com/OpenAF/openaf-dockers.git#:openaf-15
```

| Build arg    | Description |
|--------------|-------------|
| `DIST`       | Docker tag to give the resulting image (`latest`, `nightly`, ...). |
| `OPENAFDIST` | OpenAF distribution to embed (empty for stable, `nightly`, etc.). |
