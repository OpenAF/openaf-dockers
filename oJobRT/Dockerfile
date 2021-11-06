ARG DIST

FROM openaf/openaf:${DIST}

COPY --chown=openaf entrypoint.yaml /openaf/entrypoint.yaml

RUN /openaf/opack install ojob-common\
 && /openaf/opack install S3

ENTRYPOINT [ "/openaf/ojob", "/openaf/entrypoint.yaml" ]