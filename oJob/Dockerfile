ARG DIST
ARG OPENAFDIST

FROM openaf/openaf:${DIST}

COPY --chown=openaf main.yaml /openaf/main.yaml
ENV OJOB=/openaf/main.yaml
#COPY --chown=openaf entrypoint.sh /openaf/.docker/entrypoint.sh

#RUN chmod u+x /openaf/.docker/entrypoint.sh