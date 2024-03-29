ARG url=openaf/oaf
FROM $url

USER root
RUN mkdir /config\
 && chown -R openaf: /config\
 && chmod -R g+rwx /config

USER openaf
RUN /openaf/opack install oJob-common -deps\
 && /openaf/opack install nAttrMon -deps\
 && /openaf/opack install Kube -deps\
 && /openaf/opack install S3 -deps\
 && /openaf/opack install Notifications -deps\
 && /openaf/opack install DockerRegistry -deps\
 && /openaf/opack install ElasticSearch -deps\
 && chmod a+rw /openaf/.opack.db

COPY --chown=openaf: main.yaml /openaf/main.yaml

ENV CONFIG=/config\
    COREOBJECTS=/openaf/nAttrMon/config/objects,/config/objects\
    BUFFERCHANNELS=true\
    BUFFERBYNUMBER=100\
    BUFFERBYTIME=1000\
    COREOBJECTS_LAZYLOADING=true\
    MAXPLUGEXECUTE_TIME=10\
    NEED_CH_PERSISTENCE=false\
    LOGCONSOLE=true

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3\
    CMD [ "curl", "http://127.0.0.1:8090/healthz" ]

EXPOSE 8090
ENV OJOB=/openaf/main.yaml
