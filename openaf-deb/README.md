# OpenAF (Debian/Ubuntu)

## Overview

`openaf/openaf-deb` packages OpenAF on top of Ubuntu rolling. It downloads a slim Java 21 runtime, installs bash-completion for the `oaf` CLI, and runs as the non-root `openaf` user (UID 1000, GID 0). Choose this variant if you want a glibc-based environment or need Debian tooling inside the container.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest stable Debian-based build. |
| `nightly` | Nightly refresh from the newest OpenAF sources. |

## Usage

```sh
docker run --rm -ti openaf/openaf-deb:latest
```

All standard OpenAF environment variables (`OPACKS`, `OPACKS_DIR`, `OPACKS_DB`, `OPENAF`, `OJOB`, `OPACK_EXEC`, `OAFP`) are supported. Bash completion for `oaf` is pre-configured for both the `openaf` user and root.

## Build from source

```sh
docker build \
  -t openaf/openaf-deb:local \
  --build-arg DIST=latest \
  --build-arg OPENAFDIST= \
  https://github.com/OpenAF/openaf-dockers.git#:openaf-deb
```

| Build arg    | Description |
|--------------|-------------|
| `DIST`       | Docker tag assigned to the resulting image (`latest`, `nightly`, ...). |
| `OPENAFDIST` | OpenAF distribution to embed (empty for stable, `nightly`, etc.). |
