# nAttrMon dockerfile

_tbc_

````sh
docker build -t openaf/nattrmon https://github.com/OpenAF/openaf-dockers.git#:nAttrMon
````

## Initializing config folder

````sh
docker run -v /my/local/config:/config --rm openaf/nattrmon -e op=init
````

## Starting

````sh
docker volume create nattrmon_snapshots
docker run -v /my/local/config:/config -v nattrmon_snapshots:/snapshots -p 8090:8090 openaf/nattrmon
````