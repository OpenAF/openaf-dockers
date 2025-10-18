# opackServer

## Overview

`openaf.io/opackServer` delivers a simple, self-hosted oPack repository. Mount a directory containing `.opack` files or unpacked oPack folders and the container serves both a REST API (port 8090) and a static file endpoint (port 8100) for your clients.

## Usage

```sh
docker run --rm \
  -p 8090:8090 \
  -p 8100:8100 \
  -v "$PWD/opacks":/data \
  -e OPACKSERVER_PATH=/data \
  -e OPACKSERVER_URL=http://localhost:8090 \
  opackserver:latest
```

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `OPACKSERVER_PATH` | Location of the `opack.db` database and the oPack files/folders inside the container. | `/data` |
| `OPACKSERVER_URL` | Base URL advertised in metadata for clients to download packages. | `http://127.0.0.1:8090` |
| `OPACKSERVER_INITRELOAD` | Set to `false` to skip rebuilding `opack.db` on startup. | `true` |

If you prefer to run the logic directly with OpenAF, execute `ojob main.yaml` and provide the same environment variables.

## Build from source

```sh
docker build -t opackserver:latest https://github.com/OpenAF/openaf-dockers.git#:openaf.io/opackServer
```
