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
