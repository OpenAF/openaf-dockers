# OpenAF (UBI)

## Overview

`openaf/openaf-ubi` is the Red Hat UBI 9 minimal variant of the OpenAF runtime. It bundles OpenJDK 21 from the UBI repositories, adds bash, sudo, and OpenAF bash-completion scripts, and runs as the non-root user `openaf` (UID 1000, GID 0). This image is a good fit for OpenShift clusters or environments that require Red Hat certified base images.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest stable UBI build. |
| `nightly` | Nightly refresh with the newest OpenAF runtime. |

## Usage

Run the image with Podman or Docker:

```sh
podman run --rm -ti openaf/openaf-ubi:latest
```

All standard OpenAF environment variables (`OPACKS`, `OPACKS_DIR`, `OPACKS_DB`, `OPENAF`, `OJOB`, `OPACK_EXEC`, `OAFP`) are supported. UBI-specific helpers `JVM_MEMMXPERC` and `JVM_MEMMSPERC` let you tune the JVM memory percentage flags that the entrypoint exports as `JAVA_ARGS`.

## Build from source

```sh
docker build \
  -t openaf/openaf-ubi:local \
  --build-arg DIST=latest \
  --build-arg OPENAFDIST= \
  https://github.com/OpenAF/openaf-dockers.git#:openaf-ubi
```

| Build arg    | Description |
|--------------|-------------|
| `DIST`       | Docker tag to apply to the resulting image (`latest`, `nightly`, ...). |
| `OPENAFDIST` | OpenAF distribution to embed (empty for stable, `nightly`, etc.). |
