# nAttrMon

## Overview

This image packages [nAttrMon](https://github.com/OpenAF/nAttrMon) on top of the OpenAF runtime. It can bootstrap its configuration from multiple backends (local files, HTTP/S, or S3-compatible object storage) and exposes knobs to run with JSON logging, integrity checks, and different secret sources.

## Build from source

```bash
docker build -t nattrmon:$(date +%Y%m%d) https://github.com/OpenAF/openaf-dockers.git#:nAttrMon
```

## Runtime configuration

| Variable    | Required? | Description |
|-------------|-----------|-------------|
| `NAM_METHOD`| No        | Retrieval method for `NAM_CONFIG`. Supported values: `none` (default), `local`, `http`, `s3`. |
| `NAM_CONFIG`| Yes*      | Path, URL, or object key holding the nAttrMon configuration (ZIP or `main.yaml`). Required unless `NAM_METHOD=none` and you ship your own `/nattrmon/main.yaml`. |
| `NAM_JSONLOG` | No      | Set to `true` to emit container logs in JSON. |
| `NAM_HASH`  | No        | SHA-1 checksum used to verify the downloaded package (applies to ZIP or `main.yaml`). |

### Local configuration (`NAM_METHOD=local`)

```bash
docker run --rm -ti \
  -v "$PWD/examples":/config \
  -e NAM_METHOD=local \
  -e NAM_CONFIG=/config/main.zip \
  nattrmon:20240202
```

### HTTP/S configuration (`NAM_METHOD=http`)

```bash
docker run --rm -ti \
  -e NAM_METHOD=http \
  -e NAM_CONFIG=https://example.local/nattrmon/config.zip \
  nattrmon:20240202
```

Set `login` and `pass` environment variables for basic-auth endpoints.

### S3 configuration (`NAM_METHOD=s3`)

You can rely on OpenAF secrets buckets or provide credentials directly as environment variables.

| Variable | Purpose |
|----------|---------|
| `secBucket`, `secKey`, `secFile` | Configure OpenAF secrets bucket lookup (defaults: bucket `nattrmon`, key `s3_config`, file `/secrets/secrets.yaml`). |
| `url`, `bucket`, `accessKey`, `secret`, `sessionToken` | Supply credentials directly to reach an S3-compatible endpoint. |

```bash
docker run --rm -ti \
  -e NAM_METHOD=s3 \
  -e NAM_CONFIG=configs/main.zip \
  -e bucket=my-bucket \
  -e url=https://minio.local:9000 \
  -e accessKey=minioadmin \
  -e secret=minioadmin \
  nattrmon:20240202
```

### ZIP package layout

When `NAM_CONFIG` points to a ZIP file, nAttrMon expects a structure similar to:

| Path          | Description |
|---------------|-------------|
| `/main.yaml`  | Entry point executed at startup. |
| `/secrets.yaml` | Optional OpenAF `$sec` secrets file (handy for local testing). |
