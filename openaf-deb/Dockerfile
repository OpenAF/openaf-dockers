ARG DIST
ARG OPENAFDIST

#FROM openjdk:8-jre-alpine
FROM ubuntu:rolling as main
ARG DIST
ARG OPENAFDIST

# Upgrade alpine
RUN apt-get -y update\
 && apt-get -y upgrade\
 && apt-get -y install curl sudo gzip\
 && apt-get purge -y --auto-remove\
 && apt-get clean\
 && rm -rf /var/lib/apt/lists/*\
 && update-ca-certificates

# Copy auxiliary scripts
COPY entrypoint.sh installOPacks.js /openaf/.docker/
COPY getOpenAFOrigJar.js /openaf/

# Install java, Update SSL certificates and clean up + Auxiliary settings
RUN echo 'PATH=$PATH:/openaf:/openaf/jre/bin' > /etc/profile.d/openaf.sh\
 && userdel -r ubuntu\
 && useradd --gid 0 --uid 1000 -m --shell /bin/bash openaf\
 && echo "openaf ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/openaf\
 && chmod g+w /etc/passwd

# Install openaf and prepare everthing
RUN cd /openaf\
 && curl -o openaf.jar https://openaf.io/$OPENAFDIST/openaf.jar.repacked -s\
 && curl -o jre.tgz "https://openaf.io/java/java21_$(if [ "$(uname -m)" = "x86_64" ]; then echo ''; else echo 'A'; fi)64.tgz" -s\
 && tar xzf jre.tgz\
 && mv jdk* jre\
 && rm jre.tgz\
 && jre/bin/java -jar openaf.jar --install\
 && chown -R openaf:0 /openaf\
 && chown openaf:0 /openaf/.opack.db || true\
 && chmod -R u+rwx,g+rwx,o+rx,o-w /openaf/*\
 && chmod a+rwx /openaf\
 && chmod -R a+rx /openaf/.docker\
 && chmod g+w /openaf/.opack.db || true

# -------------------
FROM scratch as final

COPY --from=main / /

ENV OAF_HOME=/openaf
ENV PATH=$PATH:/openaf:/openaf/jre/bin
USER openaf:0

WORKDIR /openaf
ENTRYPOINT ["/bin/bash", "/openaf/.docker/entrypoint.sh"]
