# openaf.io utilities

The `openaf.io` folder contains auxiliary container images that complement the main OpenAF runtimes. They focus on build automation, temporary tooling, and helper services.

| Component | Description | Documentation |
|-----------|-------------|---------------|
| `copy4GIT` | Clones a Git repository branch, strips metadata, and ships the working tree (handy for air-gapped transfers). | `copy4GIT/README.md` |
| `fbrowser` | Disposable web file browser for quickly inspecting mounted volumes. | `fbrowser/README.md` |
| `OAFBuild` | Automated pipeline to clone, build, test, and package OpenAF releases. | `OAFBuild/README.md` |
| `OAFDirector` | REST API service that orchestrates OpenAF builds and oPack creation. | `OAFDirector/README.md` |
| `oLB` | Local HAProxy-based load-balancer whose backend list is managed by an OpenAF oJob. | `oLB/README.md` |
| `opackServer` | Lightweight private oPack server backed by a mounted directory of `.opack` files or folders. | `opackServer/README.md` |

Use the individual READMEs for build/run details.
