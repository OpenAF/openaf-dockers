# oJobRT

This container image is aimed to be a generic oJob runtime allowing different methods to retrieve the oJob to run upon startup. 

## Building

To build it from the source:

````bash
$ docker build -t openaf/ojobrt --build-arg DIST="latest" https://github.com/OpenAF/openaf-dockers.git#:oJobRT
````

| Build argument | Description |
|----------------|-------------|
| DIST           | The docker containter distribution/tag (e.g. latest, nightly) |

## Running

When running the following are the main environment variables considered:

| Env variable | Mandatory? | Description |
|--------------|------------|-------------|
| OJOB_METHOD  | No         | Selects the method to retrive the corresponding oJob definition (defaults to 'NONE') |
| OJOB_CONFIG  | Yes        | Depending on the OJOB_METHOD choosen points to the source object or filepath where the oJob definition (individual file or zip package) can be found |
| OJOB_JSONLOG | No         | If OJOB_JSONLOG=true the entrypoint log will be output in JSON format |

> OJOB_JSONLOG doesn't set how logs from the corresponding oJob are output. This should be defined on the oJob itself.

### None oJob

To run a directly mapped file(s) (to the folder /ojob) you don't need to provide any environment variables (optionally you can use OJOB_CONFIG for a different value than the default /ojob/main.yaml)

**Example:**
````bash
$ docker run --rm -ti -v "$(pwd)"/examples:/test -e OJOB_CONFIG=/ojob/main.yaml openaf/ojobrt
````

### Local oJob

To run a local provided oJob file or zip package use the following environment variables:

| Env variable | Example value |
|--------------|---------------|
| OJOB_METHOD  | local         |
| OJOB_CONFIG  | /local/path/main.yaml |

**Example:**

````bash
$ docker run --rm -ti -v "$(pwd)"/examples:/test -e OJOB_METHOD=local -e OJOB_CONFIG=/test/main.yaml openaf/ojobrt 
````

### S3 based oJob

To retrieve a oJob ZIP package from a S3 based bucket set the following environment variables:

| Env variable | Example value |
|--------------|-------|
| OJOB_METHOD  | s3    |
| OJOB_CONFIG  | /some/path/myPackage.zip |

**Example using default secrets:**

By default, the secrets.yaml is expected to be in /secrets/secrets.yaml. 
If no secBucket environment variable is provided it will default for searching the main key *"ojob"*.
If no secKey environment variable is provided it will default for searching the key *"s3_config"* in the OpenAF secBucket.

````bash
docker run --rm -ti -e OJOB_METHOD=s3 -e OJOB_CONFIG=test.zip -v "$(pwd)"/secrets:/secrets --net test openaf/ojobrt
````

**Example using a different secBucket and/or secKey:**

````bash
$ docker run --rm -ti -e OJOB_METHOD=s3 -e OJOB_CONFIG=test/test.zip -e secBucket=mySBucket -e secKey=myS3 -v "$(pwd)"/secrets:/secrets --net test openaf/ojobrt 
````

> To use a different secrets file the environment variable **secFile** can be provided

**Example using all secrets in environment variables:**

To provide the secrets directly, without using the OpenAF SBucket functionality, as enviroment variables use the following extra enviroment variables:

| Env variable | Example value |
|--------------|---------------|
| url          | https://minio:9000 |
| bucket       | mybucket      |
| accessKey    | minioadmin    |
| secret       | minioadmin    | 

````sh
$ docker run --rm -ti -e OJOB_METHOD=s3 -e OJOB_CONFIG=test.zip -e bucket=test -e url=http://minio:9000 -e accessKey=minioadmin -e secret=minioadmin --net test openaf/ojobrt
````

### HTTP based oJob

To retrieve a oJob ZIP package from a HTTP url set the following environment variables:

| Env variable | Example value |
|--------------|-------|
| OJOB_METHOD  | http  |
| OJOB_CONFIG  | http://some.server:12345/path/package.zip |

**Example:**

````bash
docker run --rm -ti -v "$(pwd)"/examples:/test -e OJOB_METHOD=http -e OJOB_CONFIG=http://minio:9000/test/test.zip -v "$(pwd)"/secrets:/secrets --net test openaf/ojobrt
````

> It's possible also to provide a "login" and a "pass" enviroment variable for HTTP(s) basic authentication.

### oJob ZIP package

For some retrieval methods (OJOB_METHOD) it's possible to point to a ZIP file instead of a single file. The ZIP file can have all the necessary files to run the corresponding oJob but the main execution requires a **"main.yaml"** file. Optionally a **secrets.yaml** can be provided for testing proposed.

Structure of the oJob ZIP package:

| Filepath | Description |
|----------|-------------|
| /main.yaml | The main execution oJob |
| /secrets.yaml | An optional secrets.yaml file (OpenAF $sec based) |

