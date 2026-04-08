ARG DIST
FROM openaf/oaf:${DIST}
ARG DIST

USER root
RUN case "${DIST}" in \
    deb*) apt-get -y update && apt-get -y install --no-install-recommends bubblewrap && apt-get clean && rm -rf /var/lib/apt/lists/* ;; \
    ubi*) if microdnf repoquery bubblewrap | grep -q '^bubblewrap-'; then microdnf install -y bubblewrap; else echo "bubblewrap is not available in the enabled UBI repositories; continuing without it" >&2; fi && microdnf clean all ;; \
    *) apk update && apk --no-cache add bubblewrap && rm -rf /var/cache/apk/* ;; \
  esac

USER openaf
RUN /openaf/opack install mini-a AWS Mermaid S3 oJob-common Jsoup APIs ghcopilot

ENV OPACK_EXEC=mini-a
ENV OAF_MINI_A_LIBS="@AWS/aws.js,@ghcopilot/ghcopilot.js"
