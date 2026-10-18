# Implementation checklist

- `cli/main.sh`, `cli/install.sh`, `cli/bootstrap.sh`, `cli/bootstrap.js`: shared dispatch, installation, Docker execution and fixed bootstrap; reuse the image helper and its logging API to detect reported errors.
- `cli/generate.sh`, `bin/openaf-docker.{bash,zsh}`: deterministic standalone outputs with shell-specific shebangs; Bash 3.2-compatible shared source.
- `tests/`: offline argv/environment/install tests and explicit real-container fixtures, terminal and signal checks.
- `.github/workflows/openaf-cli.yml`: Linux/macOS offline checks and generated-file freshness.
- `openaf/README.md`, root `README.md`, `.package.yaml`: usage, limitations, packaging and evidence.

Preserve the service entrypoint and unrelated `.mini-a`. No push or image publication.

Implemented the checklist. Evidence and platform gaps are recorded in `../tests/VALIDATION.md`. Database-only configuration is bridged into the application through native `OAF_OPACKS`, since helper registration is JVM-local. The only image-helper correction is accepting `isDirectory` as well as `isFolder`; a bootstrap-local adapter supports the already-published helper.

`oaf` is accepted as a selector and executable basename, normalized to `openaf`, and included in alias installation/update and conflict checks.
