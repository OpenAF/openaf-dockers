# OpenAF (Java 11)

## Overview

`openaf/openaf-11` is an experimental build of OpenAF powered by OpenJDK 11. It enables container-aware JVM tuning flags and repacks the OpenAF runtime to take advantage of class data sharing. Use it if you need a Java 11 environment or want to benchmark how OpenAF behaves on that JVM generation.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest stable Java 11 build. |
| `nightly` | Nightly Java 11 build refreshed from the latest sources. |

## Usage

```sh
docker run --rm -ti openaf/openaf-11:latest
```

The entrypoint matches the base `openaf/openaf` image, so you can use `OPACKS`, `OPENAF`, `OJOB`, and friends exactly the same way.

## Build from source

```sh
docker build \
  -t openaf/openaf-11:local \
  --build-arg DIST=latest \
  --build-arg OPENAFDIST= \
  https://github.com/OpenAF/openaf-dockers.git#:openaf-11
```

| Build arg    | Description |
|--------------|-------------|
| `DIST`       | Docker tag to give the resulting image (`latest`, `nightly`, ...). |
| `OPENAFDIST` | OpenAF distribution to download (leave empty for stable, use `nightly`, etc.). |
