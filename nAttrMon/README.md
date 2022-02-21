# nAttrMon docker

## Building

To build the container execute (changing the date to the current date):

````bash
$ docker build -t nattrmon:20220202 .
````

## Running

When running the following are the main environment variables considered:

| Env variable | Mandatory? | Description |
|--------------|------------|-------------|
| NAM_METHOD   | No | Method to retrieve NAM_CONFIG (e.g. S3, HTTP, LOCAL, NONE) |
| NAM_CONFIG   | Yes | ZIP file or URL to a zip file (if NAM_METHOD=HTTP) with the nAttrMon configuration |
| NAM_JSONLOG  | No | Turns the log output to json |
| NAM_HASH     | No | Ensure the NAM_CONFIG zip file or main.yaml as the provided hash (SHA-1) |

### Local nAttrMon configuration

To run a local provided nAttrMon ZIP file use the following environment variables:

| Env variable | Example value |
|--------------|---------------|
| NAM_METHOD  | local         |
| ONAM_CONFIG  | /local/path/config.zip |

**Example:**

````bash
$ docker run --rm -ti -v "$(pwd)"/examples:/test -e NAM_METHOD=local -e NAM_CONFIG=/test/main.zip nattrmon:20220202
````

### S3 based nAttrMon

To retrieve a nAttrMonh ZIP package from a S3 based bucket set the following environment variables:

| Env variable | Example value |
|--------------|-------|
| NAM_METHOD  | s3    |
| NAM_CONFIG  | /some/path/myPackage.zip |

**Example using default secrets:**

By default, the secrets.yaml is expected to be in /secrets/secrets.yaml. 
If no secBucket environment variable is provided it will default for searching the main key *"nattrmon"*.
If no secKey environment variable is provided it will default for searching the key *"s3_config"* in the OpenAF secBucket.

````bash
docker run --rm -ti -e NAM_METHOD=s3 -e NAM_CONFIG=test.zip -v "$(pwd)"/secrets:/secrets --net nattrmon nattrmon:20220202
````

**Example using a different secBucket and/or secKey:**

````bash
$ docker run --rm -ti -e NAM_METHOD=s3 -e NAM_CONFIG=test/test.zip -e secBucket=mySBucket -e secKey=myS3 -v "$(pwd)"/secrets:/secrets --net nattrmon nattrmon:20220202 
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
$ docker run --rm -ti -e NAM_METHOD=s3 -e NAM_CONFIG=test.zip -e bucket=test -e url=http://minio:9000 -e accessKey=minioadmin -e secret=minioadmin --net nattrmon nattrmon:20220202
````

### HTTP based nAttrMon config

To retrieve a nAttrMon ZIP configuration from a HTTP url set the following environment variables:

| Env variable | Example value |
|--------------|-------|
| NAM_METHOD  | http  |
| NAM_CONFIG  | http://some.server:12345/path/config.zip |

**Example:**

````bash
docker run --rm -ti -v "$(pwd)"/examples:/test -e NAM_METHOD=http -e NAM_CONFIG=http://minio:9000/test/config.zip -v "$(pwd)"/secrets:/secrets --net nattrmon nattrmon:20220202
````

> It's possible also to provide a "login" and a "pass" enviroment variable for HTTP(s) basic authentication.

### nAttrMon ZIP config

The ZIP file can have all the necessary files for the nAttrMon configuration. For __TESTING PROPOSES__ optionally a **secrets.yaml** can be provided also.
