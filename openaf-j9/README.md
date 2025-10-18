# OpenAF (OpenJ9)

## Overview

`openaf/openaf-j9` runs OpenAF on top of Eclipse OpenJ9 (via the AdoptOpenJDK Alpine base image). It enables class data sharing and container-friendly tuning options so you can benchmark OpenAF under OpenJ9’s AOT/JIT strategy.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest stable build with OpenJ9. |
| `nightly` | Nightly refresh of the OpenJ9 variant. |

## Usage

```sh
docker run --rm -ti openaf/openaf-j9:latest
```

Reuse the standard OpenAF environment variables (`OPACKS`, `OPENAF`, `OJOB`, `OPACK_EXEC`, `OAFP`) to install oPacks or launch scripts automatically.

## Build from source

```sh
docker build \
  -t openaf/openaf-j9:local \
  --build-arg DIST=latest \
  --build-arg OPENAFDIST= \
  https://github.com/OpenAF/openaf-dockers.git#:openaf-j9
```

| Build arg    | Description |
|--------------|-------------|
| `DIST`       | Docker tag to apply to the resulting image (`latest`, `nightly`, ...). |
| `OPENAFDIST` | OpenAF distribution to embed (empty for stable, `nightly`, etc.). |
