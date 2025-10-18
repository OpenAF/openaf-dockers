# fbrowser

## Overview

`openaf.io/fbrowser` launches a temporary, read-only web file browser backed by an OpenAF oJob. Mount any folder into `/output` and the container serves a simple UI on port 8888 for quick inspection.

## Usage

```sh
docker run --rm \
  -p 8888:80 \
  -v "$PWD":/output:ro \
  fbrowser:latest
```

Then open `http://localhost:8888` in your browser.

## Build from source

```sh
docker build -t fbrowser:latest https://github.com/OpenAF/openaf-dockers.git#:openaf.io/fbrowser
```
