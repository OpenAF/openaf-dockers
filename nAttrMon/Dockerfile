FROM openaf/openaf:nightly

RUN /openaf/opack install nAttrMon\
 && mkdir /config\
 && mkdir /snapshots\
 && apk update\
 && apk add curl\
 && ln -s /openaf/nAttrMon/config/inputs /config/inputs\
 && ln -s /openaf/nAttrMon/config/outputs /config/outputs\
 && ln -s /openaf/nAttrMon/config/validations /config/validations\
 && ln -s /openaf/nAttrMon/config/objects.assets /config/objects.assets\
 && ln -s /openaf/nAttrMon/config/outputs.disabled/yaml/00.httphealthz.yaml /config/outputs/01.httphealthz.yaml\
 && ln -s /openaf/nAttrMon/config/outputs.disabled/yaml/02.httpjson.yaml /config/outputs/02.httpjson.yaml\
 && ln -s /openaf/nAttrMon/config/outputs.disabled/yaml/03.http.yaml /config/outputs/03.http.yaml\
 && ln -s /openaf/nAttrMon/config/outputs.disabled/yaml/04.httpmetrics.yaml /config/outputs/04.httpmetrics.yaml\
 && ln -s /openaf/nAttrMon/config/outputs.disabled/yaml/09.channels.yaml /config/outputs/09.channels.yaml

COPY main.js /openaf/nAttrMon/main.js
VOLUME [ "/snapshots", "/config" ]

EXPOSE 8090
WORKDIR /openaf/nAttrMon
ENTRYPOINT [ "/openaf/oaf", "-f", "main.js" ]
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl", "http://127.0.0.1:8090/healthz" ]

ENV CH_PERSISTENCE_PATH=/snapshots
ENV CONFIG=/config
ENV LOGCONSOLE=true