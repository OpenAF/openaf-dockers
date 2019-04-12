# OpenAF-11

Experimental openaf container with JDK11, AOT OpenAF optimization and JDK container optimizations.

## Building

````sh
docker build -t openaf/openaf --build-arg DIST="latest" --build-arg OPENAFDIST="" https://github.com/OpenAF/openaf-dockers.git#:openaf-11
````

| Build argument | Description |
|----------------|-------------|
| DIST           | The docker containter distribution/tag (e.g. latest, nightly) |
| OPENAFDIST     | The OpenAF build to use (e.g. "" (stable), "nightly") |
