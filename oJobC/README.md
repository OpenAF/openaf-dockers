# oJobC

## Building

````sh
docker build -t openaf/openaf-ojobc --build-arg DIST="latest" https://github.com/OpenAF/openaf-dockers.git#:oJobC
````

| Build argument | Description |
|----------------|-------------|
| DIST           | The docker containter distribution/tag (e.g. latest, nightly) |
| OPENAFDIST     | The OpenAF build to use (e.g. "" (stable), "nightly") |
