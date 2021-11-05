# oJobRT

## Building

````sh
docker build -t openaf/ojobrt --build-arg DIST="latest" https://github.com/OpenAF/openaf-dockers.git#:oJobRT
````

| Build argument | Description |
|----------------|-------------|
| DIST           | The docker containter distribution/tag (e.g. latest, nightly) |
| OPENAFDIST     | The OpenAF build to use (e.g. "" (stable), "nightly") |

## Possible options

````sh
docker run --rm -ti -v `pwd`/test:/test -e OJOB_METHOD=local -e OJOB_CONFIG=/test/main.yaml openaf/ojobrt 

docker run --rm -ti -v `pwd`/test:/test -e OJOB_METHOD=s3 -e OJOB_CONFIG=test.zip -e bucket=test -e url=http://minio:9000 -e accessKey=minioadmin -e secret=minioadmin --net test openaf/ojobrt

docker run --rm -ti -v `pwd`/test:/test -e OJOB_METHOD=s3 -e OJOB_CONFIG=test.zip -v `pwd`/secrets:/secrets --net test openaf/ojobrt

docker run --rm -ti -v `pwd`/test:/test -e OJOB_METHOD=http -e OJOB_CONFIG=http://minio:9000/test/test.zip -v `pwd`/secrets:/secrets --net test openaf/ojobrt
````