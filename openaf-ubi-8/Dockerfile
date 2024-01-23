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
 && microdnf install -y --nodocs java-1.8.0-openjdk-headless tar sudo shadow-utils\
 && rm -rf /usr/lib/jvm/java-1.8.0-openjdk-*/jre/lib/ext/nashorn.jar\
 && rm -rf /usr/lib/jvm/java-1.8.0-openjdk-*/jre/lib/images/jre/man\
 && rm -rf /usr/lib/jvm/java-1.8.0-openjdk-*/jre/lib/images\
 && echo 'PATH=$PATH:/openaf' > /etc/profile.d/openaf.sh\
 && adduser openaf -g 0 -u 1000\
 && chown -R openaf: /openaf\
 && echo "openaf ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/openaf\
 && microdnf remove -y shadow-utils\
 && microdnf clean all\
 && echo 'if [ ! -e /tmp/.openaf-ojobio-complete ] || [ $(find /tmp/.openaf-ojobio-complete -mtime +1) ]; then curl --max-time 2 -s https://ojob.io/autoComplete.sh > /tmp/.openaf-ojobio-complete; fi' >> /etc/bashrc\
 && echo "source /tmp/.openaf-ojobio-complete" >> /etc/bashrc\
 && chmod -R a+rx /openaf/.docker\
 && chmod g+w /etc/passwd\
 && cp ~/.bash_profile /.bash_profile\
 && cp ~/.bashrc /.bashrc

USER 1000:0

# Install openaf and prepare everything
RUN cd /openaf\
 && curl -o openaf.jar https://openaf.io/$OPENAFDIST/openaf.jar.repacked -s\
 && java -jar openaf.jar --install -e 'args=$JAVA_ARGS'\
 && sudo chmod -R u+rwx,g+rwx,o+rx,o-w /openaf/*\
 && sudo chmod a+rwx /openaf\
 && sudo chown -R openaf:0 /openaf\
 && sudo chown openaf:0 /openaf/.opack.db\
 && sudo chmod g+w /openaf/.opack.db\
 && curl -s https://ojob.io/autoComplete.sh > /tmp/.openaf-ojobio-complete\
 && chmod a+rw /tmp/.openaf-ojobio-complete 

# -------------------
FROM scratch as final

COPY --from=main / /

ENV OAF_HOME=/openaf
USER 1000:0

WORKDIR /openaf
ENTRYPOINT ["/openaf/.docker/entrypoint.sh"]
