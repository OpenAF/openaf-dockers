ARG DIST
FROM openaf/oaf:${DIST}

RUN /openaf/opack install mini-a AWS Mermaid S3 oJob-common Jsoup APIs

ENV OPACK_EXEC=mini-a
ENV OAF_MINI_A_LIBS="@AWS/aws.js"
