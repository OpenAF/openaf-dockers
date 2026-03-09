ARG DIST
FROM openaf/oaf:${DIST}
ARG DIST

USER root
RUN case "${DIST}" in \
    deb*) apt-get -y update && apt-get -y install --no-install-recommends bubblewrap && apt-get clean && rm -rf /var/lib/apt/lists/* ;; \
    ubi*) microdnf install -y bubblewrap && microdnf clean all ;; \
    *) apk update && apk --no-cache add bubblewrap && rm -rf /var/cache/apk/* ;; \
  esac

USER openaf
RUN /openaf/opack install mini-a AWS Mermaid S3 oJob-common Jsoup APIs

ENV OPACK_EXEC=mini-a
ENV OAF_MINI_A_LIBS="@AWS/aws.js"
