ARG DIST

FROM openaf/openaf:${DIST}

COPY --chown=openaf entrypoint.yaml /openaf/entrypoint.yaml

USER root 
RUN mkdir /ojob\
 && mkdir /secrets\
 && chown -R openaf: /ojob\
 && chown -R openaf: /secrets\
 && chmod -R a+rwx /ojob\
 && chmod -R a+rwx /secrets

USER openaf
RUN /openaf/opack install ojob-common\
 && /openaf/opack install S3\
 && chmod a+rw /openaf/.opack.db

WORKDIR /ojob
ENV OJOB=/openaf/entrypoint.yaml
