# OpenAF Console

Based on the main openaf container facilitates the use of the openaf-console.

## Building

````sh
docker build -t openaf/openaf-console --build-arg DIST="latest" https://github.com/OpenAF/openaf-dockers.git#:openaf-console
````

| Build argument | Description |
|----------------|-------------|
| DIST           | The docker containter distribution/tag (e.g. latest, nightly) |
| OPENAFDIST     | The OpenAF build to use (e.g. "" (stable), "nightly") |