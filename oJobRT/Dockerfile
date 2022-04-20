ARG DIST

FROM openaf/openaf:${DIST}

COPY --chown=openaf entrypoint.yaml /openaf/entrypoint.yaml

USER root 
RUN mkdir /ojob\
 && chown -R openaf: /ojob

USER openaf
RUN /openaf/opack install ojob-common\
 && /openaf/opack install S3

WORKDIR /ojob
ENV OJOB=/openaf/entrypoint.yaml