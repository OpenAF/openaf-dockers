# OpenAF-FBrowser

Quick, simple, temporary file browser for a quick hack. 

## Using it

1. Build the container

````bash
docker build -t fbrowser https://github.com/OpenAF/openaf-dockers.git#:openaf-fbrowser
````

2. Run the container

````bash
docker run --rm -ti -v [the folder you want to expose]:/output -p 8888:80 fbrowser
````

3. Point your browser to the docker host address on port 8888 (e.g. http://127.0.0.1:8888)
