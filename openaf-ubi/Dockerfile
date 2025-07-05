ARG DIST
ARG OPENAFDIST

FROM registry.access.redhat.com/ubi9/ubi-minimal as main
ARG DIST
ARG OPENAFDIST

# Copy auxiliary scripts
COPY entrypoint.sh installOPacks.js /openaf/.docker/
COPY getOpenAFOrigJar.js /openaf/

# Install java + auxiliary settings
RUN microdnf upgrade -y\
 && rm -rf /var/cache/yum\
 && microdnf install -y --nodocs java-21-openjdk-headless tar sudo shadow-utils bash-completion\
 && echo 'PATH=$PATH:/openaf' > /etc/profile.d/openaf.sh\
 && adduser openaf -g 0 -u 1000\
 && chown -R openaf: /openaf\
 && echo "openaf ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/openaf\
 && microdnf remove -y shadow-utils\
 && microdnf clean all\
 && echo "source ~/.openaf_completion_bash.sh > /dev/null 2>&1" >> /etc/bashrc\
 && chmod -R a+rx /openaf/.docker\
 && chmod g+w /etc/passwd\
 && cp ~/.bash_profile /.bash_profile\
 && cp ~/.bashrc /.bashrc

USER 1000:0

# Install openaf and prepare everything
RUN cd /openaf\
 && curl -o openaf.jar https://openaf.io/${OPENAFDIST:+$OPENAFDIST/}openaf.jar.repacked -s\
 && java -jar openaf.jar --install -e 'args=$JAVA_ARGS'\
 && sudo chmod -R u+rwx,g+rwx,o+rx,o-w /openaf/*\
 && sudo chmod a+rwx /openaf\
 && sudo chown -R openaf:0 /openaf\
 && sudo chown openaf:0 /openaf/.opack.db || true\
 && sudo chmod g+w /openaf/.opack.db || true\
 && /openaf/oaf --bashcompletion all > ~/.openaf_completion_bash.sh

USER root
RUN /openaf/oaf --bashcompletion all > ~/.openaf_completion_bash.sh
USER 1000:0

# -------------------
FROM scratch as final

COPY --from=main / /

ENV OAF_HOME=/openaf
USER 1000:0

WORKDIR /openaf
ENTRYPOINT ["/openaf/.docker/entrypoint.sh"]
