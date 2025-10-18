# oLB

## Overview

`openaf.io/oLB` provides a lightweight HAProxy-based load balancer managed by an OpenAF oJob. It watches Docker containers on the local host (via the Docker socket), filters them according to your criteria, and rewrites the HAProxy backend list whenever containers start or stop.

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `FILTER_PATH` | — | Container property used for filtering (e.g., `Names`, `Labels.com.example.role`). |
| `FILTER_VALUE` | — | Regular expression applied to `FILTER_PATH` to decide which containers become backends. |
| `BACKEND_PORT` | `80` | TCP port exposed by the backend containers. |
| `PORT` | `80` | Front-end port exposed by HAProxy. |
| `HOST` | `*` | Address where HAProxy listens. |
| `BALANCE` | `roundrobin` | Load-balancing algorithm passed to HAProxy. |

## Usage

```yaml
services:
  lb-elastic:
    build: https://github.com/OpenAF/openaf-dockers.git#:openaf.io/oLB
    ports:
      - "9200:80"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    environment:
      BACKEND_PORT: 9200
      FILTER_PATH: Names
      FILTER_VALUE: /elastic/
      BALANCE: roundrobin
```

> The container requires read-only access to the Docker socket so it can enumerate running containers.
