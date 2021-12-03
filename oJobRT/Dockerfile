ARG DIST

FROM openaf/openaf:${DIST}

COPY --chown=openaf entrypoint.yaml /openaf/entrypoint.yaml

USER root 

RUN /openaf/opack install ojob-common\
 && /openaf/opack install S3\
 && mkdir /ojob\
 && chown -R openaf: /ojob

USER openaf

WORKDIR /ojob
ENTRYPOINT [ "/openaf/ojob", "/openaf/entrypoint.yaml" ]