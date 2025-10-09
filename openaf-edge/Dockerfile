ARG DIST
ARG OPENAFDIST

FROM alpine:edge as main
ARG DIST
ARG OPENAFDIST

# Copy auxiliary scripts
COPY entrypoint.sh installOPacks.js /openaf/.docker/
COPY getOpenAFOrigJar.js /openaf/

# Install java, Update SSL certificates and clean up + Auxiliary settings
RUN echo 'PATH=$PATH:/openaf' > /etc/profile.d/openaf.sh\
 && mv /etc/profile.d/color_prompt.sh.disabled /etc/profile.d/color_prompt.sh\
 && apk update\
 && apk --no-cache add ca-certificates curl openssl sudo bash mimalloc2\
 && update-ca-certificates\
 && adduser -g 0 -u 1000 -Ds /bin/sh openaf\
 && echo "openaf ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/openaf\
 && chmod g+w /etc/passwd\
 && cd /openaf\
 && curl https://openaf.io/getJava.sh | VERSION=25 bash\
 && tar xzf jre.tgz\
 && rm jre.tgz\
 && mv jdk* jre\
 && apk del bash\
 && rm -rf /var/cache/apk/*

# Install openaf and prepare everthing
RUN cd /openaf\
 && curl -o openaf.jar https://openaf.io/${OPENAFDIST:+$OPENAFDIST/}openaf.jar.repacked -s\
 && jre/bin/java --enable-native-access=ALL-UNNAMED -jar openaf.jar --install\
 && chown -R openaf:0 /openaf\
 && chown openaf:0 /openaf/.opack.db || true\
 && chown openaf:0 /openaf/.shared.oaf || true\
 && chmod -R u+rwx,g+rwx,o+rx,o-w /openaf/*\
 && chmod a+rwx /openaf\
 && chmod -R a+rx /openaf/.docker\
 && chmod g+w /openaf/.opack.db || true\
 && chmod g+w /openaf/.shared.oaf || true

# if distribution equals t8
#RUN OPENAFDIST=${OPENAFDIST:-t8} && \
#  if [ "$OPENAFDIST" = "t8" ]; then \
#    cd /openaf && \
#    /openaf/ojob ojob.io/oaf/j23SharedAOC && \
#    chown openaf:0 /openaf/.shared.oaf && \
#    chmod a+r /openaf/.shared.oaf; && \
#    chown -R openaf:0 /openaf && \
#    chown openaf:0 /openaf/.opack.db || true\
#  else \
#    echo "Skipping AOC..."; \
#  fi

# -------------------
FROM scratch as final

COPY --from=main / /

ENV OAF_HOME=/openaf
ENV LD_PRELOAD=/usr/lib/libmimalloc.so.2
USER openaf:0

WORKDIR /openaf
ENTRYPOINT ["/bin/sh", "/openaf/.docker/entrypoint.sh"]
