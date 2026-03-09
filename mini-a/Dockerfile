ARG DIST
FROM openaf/oaf:${DIST}

USER root
RUN apk update\
 && apk --no-cache add bubblewrap\
 && rm -rf /var/cache/apk/*

USER openaf
RUN /openaf/opack install mini-a AWS Mermaid S3 oJob-common Jsoup APIs

ENV OPACK_EXEC=mini-a
ENV OAF_MINI_A_LIBS="@AWS/aws.js"
