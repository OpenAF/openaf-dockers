ARG DIST
ARG OPENAFDIST

FROM openaf/openaf:${DIST}

RUN /openaf/opack install ojob-common

COPY main.yaml /openaf/main.yaml
COPY entrypoint.sh /openaf/.docker/entrypoint.sh
RUN chmod u+x /openaf/.docker/entrypoint.sh
