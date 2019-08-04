FROM openaf/openaf-ojobc

RUN apk add haproxy\
 && /openaf/opack install docker

COPY main.yaml /openaf/main.yaml
COPY haproxy.cfg.hbs /openaf/haproxy.cfg.hbs
