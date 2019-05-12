# oPackServer

opackServer is a simple private opack server that will serve opacks from a provided folder. These opacks can be in the form of opack files or folders.

## Install it as a docker container

### Build the container

To build the container:

````bash
docker build -t opackserver .
````

To run the container:

````bash
docker run -ti -p 8090:8090 -p 8100:8100 -v /my/opacks/folder:/data opackserver
````

Uncomment and change, if needed, the following environment variables:

````dockerfile
# Where the opack.db and opacks folder is located in the container
ENV OPACKSERVER_PATH /data
# The external endpoint on which the opack content will be available
ENV OPACKSERVER_URL http://127.0.0.1:8090
# Don't reload opack.db on startup
ENV OPACKSERVER_INITRELOAD false
````

## Install it as a oJob

_tbc_