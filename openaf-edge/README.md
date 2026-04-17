# OpenAF Edge

## Overview

`openaf/openaf-edge` tracks the bleeding-edge OpenAF runtime on top of Alpine Linux `edge`. It bundles a slim Java 25 runtime fetched via `getJava.sh`, enables mimalloc (`LD_PRELOAD=/usr/lib/libmimalloc.so.2`), and keeps the same entrypoint experience as the standard image. Use it to validate upcoming changes before they land in the stable `openaf/openaf` builds.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest OpenAF Edge build based on Alpine edge. |
| `nightly` | Nightly Edge build refreshed every day. |
| `t8` | Developer build aligned with the `t8` distribution. |

## Usage

Launch an interactive shell:

```sh
docker run --rm -ti openaf/openaf-edge:latest
```

Run a script against the bleeding-edge runtime:

```sh
docker run --rm -ti \
  -v "$PWD/scripts":/scripts \
  -e OPENAF=/scripts/preview.js \
  openaf/openaf-edge:nightly
```

Install custom oPacks before dropping into the shell:

```sh
docker run --rm -ti \
  -e OPACKS=APIs \
  openaf/openaf-edge:t8
```

All standard OpenAF entrypoint variables are supported: `OPACKS`, `OPACKS_DIR`, `OPACKS_DB`, `OPENAF`, `OJOB`, `OPACK_EXEC`, and `OAFP`. In addition, `SHELL=1` enables shell-form command passthrough.

Run a shell-form command through the entrypoint with `SHELL=1`. This is useful when Docker passes split arguments to `sh -c`, including commands that contain spaces or shell operators:

```sh
docker run --rm -ti \
  -e SHELL=1 \
  openaf/openaf-edge:latest \
  'echo "OpenAF Edge"' '&&' 'oaf -c "1 + 1"'
```

## Build from source

```sh
docker build \
  -t openaf/openaf-edge:local \
  --build-arg DIST=latest \
  --build-arg OPENAFDIST=edge \
  https://github.com/OpenAF/openaf-dockers.git#:openaf-edge
```

| Build arg    | Description |
|--------------|-------------|
| `DIST`       | Docker tag to apply to the resulting image (`latest`, `nightly`, `t8`, ...). |
| `OPENAFDIST` | Which OpenAF distribution to download (default matches the chosen tag). |
