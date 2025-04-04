# OpenAF dockers

Main OpenAF docker builds.

Security scans:

[![sec-latest](.github/sec-latest.svg)](.github/sec-latest.md)<br>
[![sec-nightly](.github/sec-nightly.svg)](.github/sec-nightly.md)<br>
[![sec-edge](.github/sec-edge.svg)](.github/sec-edge.md)<br>
[![sec-ubi-latest](.github/sec-ubi-latest.svg)](.github/sec-ubi-latest.md)<br>
[![sec-ubi-nightly](.github/sec-ubi-nightly.svg)](.github/sec-ubi-nightly.md)<br>
[![sec-deb-latest](.github/sec-deb-latest.svg)](.github/sec-deb-latest.md)<br>
[![sec-deb-nightly](.github/sec-deb-nightly.svg)](.github/sec-deb-nightly.md)<br>
[![sec-oJobRT-latest](.github/sec-oJobRT-latest.svg)](.github/sec-oJobRT-latest.md)<br>
[![sec-oJobRT-nightly](.github/sec-oJobRT-nightly.svg)](.github/sec-oJobRT-nightly.md)<br>
[![sec-oJobRT-edge](.github/sec-oJobRT-edge.svg)](.github/sec-oJobRT-edge.md)<br>
[![sec-pyOAF-nightly](.github/sec-pyOAF-nightly.svg)](.github/sec-pyOAF-nightly.md)<br>
[![sec-pyOAF-edge](.github/sec-pyOAF-edge.svg)](.github/sec-pyOAF-edge.md)<br>

## OpenAF

The main base container for OpenAF.

### Running

````sh
docker pull openaf/openaf
````

There are two tags available:

| Tag     | Description              |
|---------|--------------------------|
| latest  | The lastest stable build |
| nightly | The nightly build        |
| t8      | The developer version    |

The environment variables available:

| Variable   | Description | Example |
|------------|-------------|---------|
| OPACKS     | A comma separated list of oPacks to install during the first execution from central repositories. | OPACKS=APIs,Docker,Mongo |
| OPACKS_DIR | A container based folder with .opack files or folders to be installed during the first execution. | OPACKS_DIR=/opacks |
| OPACKS_DB  | A comma separated list of  | OPACKS_DB=http://main.server/opack.db |
| OPENAF     | A container based script to be executed. | /myscripts/script.js |
| OJOB       | A container based ojob to be executed. | /myojobs/job.yaml |
| OAFP       | If defined will rever to running oafp. | -h |

#### Examples

Running commands directly:
````sh
docker run -ti -e OPACKS=APIs openaf/openaf -e 'load("apis.js");print(apis.ChuckNorrisJokes.get())'
````
Running a script:
````sh
docker run -ti -e OPACKS=APIs -e OPENAF=/scripts/myScript.js -v /myscripts:/scripts openaf/openaf
````
Running an oJob:
````sh
docker run -ti -e OPACKS=APIs -e OJOB=/ojobs/myJob.yaml -v /myojobs:/ojobs openaf/openaf
````
Invoking the console with a private opack:
````sh
docker run -ti -e OPACKS=https://user:pass@my.server/myOPack.opack openaf/openaf --console
````

[Building openaf](openaf)

## OpenAF Console

Based on the main openaf container facilitates the use of the openaf-console.

### Running

````sh
docker pull openaf/openaf-console
````

There are two tags available:

| Tag     | Description              |
|---------|--------------------------|
| latest  | The lastest stable build |
| nightly | The nightly build        |
| t8      | The developer version    |

#### Example

````sh
docker run -ti openaf/openaf-console
````

[Building openaf-console](openaf-console)

## oJob

Based on the main openaf container facilitates the execution of an oJob executing /openaf/main.yaml be default.

### Running

````sh
docker pull openaf/openaf-ojob
````

There are two tags available:

| Tag     | Description              |
|---------|--------------------------|
| latest  | The lastest stable build |
| nightly | The nightly build        |
| t8      | The developer version    |

[Building oJob](oJob)

## oJobC

Based on the main openaf container facilitates the execution of an oJob, with ojob-common opack pre-installed, executing /openaf/main.yaml be default.

### Running

````sh
docker pull openaf/openaf-ojobc
````

There are two tags available:

| Tag     | Description              |
|---------|--------------------------|
| latest  | The lastest stable build |
| nightly | The nightly build        |
| t8      | The developer version    |

[Building oJobC](oJobC)
