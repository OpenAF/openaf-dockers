# OpenAF

## Building

````sh
docker build -t openaf/openaf --build-arg DIST="latest" --build-arg OPENAFDIST="" https://github.com/OpenAF/openaf-dockers.git#:openaf-ubi
````

| Build argument | Description |
|----------------|-------------|
| DIST           | The docker containter distribution/tag (e.g. latest, nightly) |
| OPENAFDIST     | The OpenAF build to use (e.g. "" (stable), "nightly") |
