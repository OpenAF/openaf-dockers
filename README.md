# OpenAF dockers

Main OpenAF docker builds.

## OpenAF

The main base container for OpenAF.

### Running

````bash
docker pull openaf/openaf
````

There are two tags available:

| Tag     | Description              |
|---------|--------------------------|
| latest  | The lastest stable build |
| nightly | The nightly build        |

The environment variables available:

| Variable   | Description | Example |
|------------|-------------|---------|
| OPACKS     | A comma separated list of oPacks to install during the first execution from central repositories. | OPACKS=APIs,Docker,Mongo |
| OPACKS_DIR | A container based folder with .opack files or folders to be installed during the first execution. | OPACKS_DIR=/opacks |
| OPACKS_DB  | A comma separated list of  | OPACKS_DB=http://main.server/opack.db |
| OPENAF     | A container based script to be executed. | /myscripts/script.js |
| OJOB       | A container based ojob to be executed. | /myojobs/job.yaml |

#### Examples

````bash
docker run -ti -e OPACKS=APIs openaf/openaf -e 'load("apis.js");print(apis.ChuckNorrisJokes.get())'
````

### Building

_tbc_

## OpenAF Console

### Running

````bash
docker pull openaf/openaf-console
````

There are two tags available:

| Tag     | Description              |
|---------|--------------------------|
| latest  | The lastest stable build |
| nightly | The nightly build        |

_tbc_

### Building

_tbc_

## oJob

### Running

````bash
docker pull openaf/openaf-ojob
````

There are two tags available:

| Tag     | Description              |
|---------|--------------------------|
| latest  | The lastest stable build |
| nightly | The nightly build        |

_tbc_

### Building

_tbc_

## oJobC

### Running

````bash
docker pull openaf/openaf-ojobc
````

There are two tags available:

| Tag     | Description              |
|---------|--------------------------|
| latest  | The lastest stable build |
| nightly | The nightly build        |

_tbc_

### Building

_tbc_