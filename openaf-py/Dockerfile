ARG url=openaf/oaf
FROM $url

USER root
RUN apk update\
 && apk --no-cache add python3 py3-pip\
 && apk cache --purge\
 && rm -rf /var/cache/apk/*

USER openaf
ENV OAF_PYTHON=python3\
    OAF_PYTHON_VER=3
