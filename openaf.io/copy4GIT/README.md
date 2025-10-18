# copy4GIT

## Overview

`openaf.io/copy4GIT` produces an image that clones a Git repository branch, strips all Git metadata, and leaves the working tree in a target directory. It is handy for copying code into restricted environments or preparing build contexts without exposing repository history.

## Usage

The container runs the `main.yaml` oJob on startup. Configure it via environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `CLONEGIT_GITURL` | **Required.** Git repository URL to clone. | — |
| `CLONEGIT_TARGET` | Destination folder for the sanitized copy. | `/data` |
| `CLONEGIT_BRANCH` | Branch or tag to checkout. | Repository default |
| `CLONEGIT_TEMP` | Temporary directory used during cloning. | `<target>.tmp` |
| `CLONEGIT_USER` / `CLONEGIT_PASS` | Credentials for HTTP(S) remotes when needed. | — |

Example (after building the image as `copy4git:latest`, see below):

```sh
docker run --rm \
  -v "$PWD/output":/data \
  -e CLONEGIT_GITURL=https://github.com/OpenAF/openaf.git \
  -e CLONEGIT_BRANCH=main \
  copy4git:latest
```

## Build from source

```sh
docker build -t copy4git:latest https://github.com/OpenAF/openaf-dockers.git#:openaf.io/copy4GIT
```
