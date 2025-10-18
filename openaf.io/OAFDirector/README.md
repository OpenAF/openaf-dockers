# OAFDirector

## Overview

`openaf.io/OAFDirector` is an OpenAF oJob that exposes a REST API to orchestrate OpenAF builds and oPack packaging tasks. It works alongside the other `openaf.io` services (`OAFBuild`, `copy4GIT`, etc.) and is typically started via `ojob oafdirector.yaml` or through the provided Docker Compose definition.

## Usage

Start the service directly with OpenAF:

```sh
ojob oafdirector.yaml
```

By default it listens on port `8099` and registers endpoints such as:

- `POST /build` – Trigger an OpenAF build using the configured `OAFBuild` image.
- `POST /opacks` – Rebuild or publish oPacks using the configured copy image.

The Docker Compose file under `openaf.io/docker-compose.yml` wires the director together with its helper services.

## Configuration anchors

Important settings live under the `init:` section of `oafdirector.yaml` and can be overridden through environment variables when launching the oJob:

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | REST API port. | `8099` |
| `IMAGE_BUILD` | Container image used to build OpenAF releases. | `openafio_oafbuild:latest` |
| `IMAGE_COPYOPACKS` | Image used to copy oPacks into the distribution folder. | `openafio_copy-main-opacks:latest` |
| `OPACKS_FOLDER` | Host path where rebuilt oPacks are stored. | `/tmp/data/opacks` |
| `OAF_FOLDER` | Host path where built OpenAF artifacts are stored. | `/tmp/data/oaf` |
| `OAF_NETWORK` / `OPACKS_NETWORK` | Docker networks the helper containers should join. | `openafio_openafio` |

Adjust these values to point at your own infrastructure before deploying the service.
