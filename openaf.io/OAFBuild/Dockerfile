FROM openaf/openaf-ojobc

RUN apk update\
 && apk add openjdk8

COPY main.yaml /openaf/main.yaml

COPY stable.json /openaf/stable.json
COPY nightly.json /openaf/nightly.json

#ENV OPACKS ojob-common
#ENV OJOB /openaf/main.yaml