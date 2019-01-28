ARG DIST
ARG OPENAFDIST

FROM openaf/openaf:${DIST}

COPY main.yaml /openaf/main.yaml
COPY entrypoint.sh /openaf/.docker/entrypoint.sh
RUN chmod u+x /openaf/.docker/entrypoint.sh
