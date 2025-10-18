# oJobRT

## Overview

`openaf/ojobrt` is a generic OpenAF oJob runtime. It knows how to fetch an oJob definition at startup (from the filesystem, HTTP/S, or S3-compatible object storage), unpacks it when needed, and then executes the requested job. This makes it a good fit for GitOps-style deployments where the job definition lives outside of the container image.

## Available tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest stable build published to Docker Hub. |
| `nightly` | Nightly build from the most recent OpenAF sources. |
| `edge` | Builds aligned with the bleeding-edge OpenAF distribution. |

## Build from source

```bash
docker build \
  -t openaf/ojobrt:local \
  --build-arg DIST=latest \
  https://github.com/OpenAF/openaf-dockers.git#:oJobRT
```

| Build argument | Description |
|----------------|-------------|
| `DIST`         | Docker distribution tag to bake into the image (`latest`, `nightly`, `edge`, ...). |

## Runtime configuration

| Variable     | Required? | Purpose |
|--------------|-----------|---------|
| `OJOB_METHOD`| No        | Selects how the oJob definition is retrieved. Supported values: `none` (default), `local`, `http`, `s3`. |
| `OJOB_CONFIG`| Yes       | Path, URL, or object key that points to the main oJob file (or ZIP package) for the chosen method. Defaults to `/ojob/main.yaml` when `OJOB_METHOD=none`. |
| `OJOB_JSONLOG` | No      | When set to `true`, emits entrypoint logs in JSON (does not affect the oJob own logging). |

The image also accepts the standard OpenAF variables (`OPACKS`, `OPACKS_DIR`, `OPACKS_DB`, `OPENAF`, `OPACK_EXEC`, `OAFP`) inherited from the base runtime.

### Method: none

Mount or bake the oJob directly inside the image and rely on the default path:

```bash
docker run --rm -ti \
  -v "$PWD/examples":/ojob \
  openaf/ojobrt:latest
```

Override the default path with `OJOB_CONFIG` if the file lives elsewhere:

```bash
docker run --rm -ti \
  -v "$PWD/examples":/payload \
  -e OJOB_METHOD=none \
  -e OJOB_CONFIG=/payload/main.yaml \
  openaf/ojobrt:latest
```

### Method: local

Point to a file or ZIP already available inside the container (typically through a bind mount):

```bash
docker run --rm -ti \
  -v "$PWD/jobs":/jobs \
  -e OJOB_METHOD=local \
  -e OJOB_CONFIG=/jobs/main.yaml \
  openaf/ojobrt:nightly
```

### Method: http

Download the job from an HTTP/S endpoint. Optional `login` and `pass` environment variables enable basic authentication.

```bash
docker run --rm -ti \
  -e OJOB_METHOD=http \
  -e OJOB_CONFIG=https://example.local/jobs/package.zip \
  openaf/ojobrt:latest
```

### Method: s3

Fetch an oJob (file or ZIP) from an S3-compatible object store. Secrets can be provided either through the OpenAF secrets bucket mechanism or via environment variables.

| Variable | Purpose |
|----------|---------|
| `secBucket`, `secKey`, `secFile` | Point to credentials stored in an OpenAF secrets bucket (defaults: bucket `ojob`, key `s3_config`, file `/secrets/secrets.yaml`). |
| `url`, `bucket`, `accessKey`, `secret`, `sessionToken` | Provide S3 credentials directly as environment variables. |

```bash
docker run --rm -ti \
  -e OJOB_METHOD=s3 \
  -e OJOB_CONFIG=jobs/pipeline.zip \
  -e bucket=my-bucket \
  -e url=https://minio.local:9000 \
  -e accessKey=minioadmin \
  -e secret=minioadmin \
  openaf/ojobrt:edge
```

### Working with ZIP packages

When `OJOB_CONFIG` points to a ZIP file, the archive is unpacked and `main.yaml` is executed. You can optionally include a `secrets.yaml` alongside the job definition for testing purposes.

| File path     | Description |
|---------------|-------------|
| `/main.yaml`  | Required oJob entry point executed by the runtime. |
| `/secrets.yaml` | Optional OpenAF `$sec` secrets file that is loaded before execution. |
