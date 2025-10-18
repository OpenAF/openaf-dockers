# OAFBuild

## Overview

`openaf.io/OAFBuild` automates cloning, building, testing, and packaging an OpenAF release. It runs the `main.yaml` oJob, which accepts several environment variables to describe the target repository, desired distribution, and output location.

## Usage

```sh
docker run --rm \
  -v "$PWD/output":/output \
  -e OAFCOMPILE_GITURL=https://github.com/OpenAF/openaf.git \
  -e OAFCOMPILE_BRANCH=main \
  -e OAFCOMPILE_VERSION=20250101 \
  -e OAFCOMPILE_DIST=nightly \
  -e OAFCOMPILE_JSON=nightly.json \
  oafbuild:latest
```

The container writes build artifacts and test reports to `/output`.

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `OAFCOMPILE_GITURL` | Repository to clone. | `https://github.com/openaf/openaf` |
| `OAFCOMPILE_BRANCH` | Branch or tag to checkout. | `master` |
| `OAFCOMPILE_TARGET` | Output directory where the final build is stored. | `/output` |
| `OAFCOMPILE_FOLDER` | Working directory for the build stages. | `/openaf/tmp` |
| `OAFCOMPILE_VERSION` | Version string injected into the build. | — |
| `OAFCOMPILE_DIST` | Distribution label (`stable`, `nightly`, etc.). | `nightly` |
| `OAFCOMPILE_JSON` | JSON descriptor to use (e.g., `stable.json`, `nightly.json`). | `nightly.json` |
| `OAFCOMPILE_TEST` | Set to `yes` to run automated tests after compiling. | `yes` |
| `OAFCOMPILE_USER` / `OAFCOMPILE_PASS` | Credentials for private repositories when needed. | — |

## Build from source

```sh
docker build -t oafbuild:latest https://github.com/OpenAF/openaf-dockers.git#:openaf.io/OAFBuild
```
