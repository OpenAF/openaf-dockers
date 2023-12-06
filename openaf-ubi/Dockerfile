ARG DIST
ARG OPENAFDIST

FROM registry.access.redhat.com/ubi9/ubi-minimal 
ARG DIST
ARG OPENAFDIST

# Copy auxiliary scripts
COPY entrypoint.sh installOPacks.js /openaf/.docker/
COPY getOpenAFOrigJar.js /openaf/

# Install java + auxiliary settings
RUN microdnf upgrade -y\
 && rm -rf /var/cache/yum\
 && microdnf install -y --nodocs java-1.8.0-openjdk-headless sudo shadow-utils\
 && rm -rf /usr/lib/jvm/java-1.8.0-openjdk-*/jre/lib/ext/nashorn.jar\
 && rm -rf /usr/lib/jvm/java-1.8.0-openjdk-*/jre/lib/images/jre/man\
 && rm -rf /usr/lib/jvm/java-1.8.0-openjdk-*/jre/lib/images\
 && echo 'PATH=$PATH:/openaf' > /etc/profile.d/openaf.sh\
 && adduser openaf\
 && chown -R openaf: /openaf\
 && echo "openaf ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/openaf\
 && microdnf remove -y shadow-utils\
 && microdnf clean all\
 && echo 'if [ ! -e ~/.openaf-ojobio-complete ] || [ $(find ~/.openaf-ojobio-complete -mtime +1) ]; then curl --max-time 2 -s https://ojob.io/autoComplete.sh > ~/.openaf-ojobio-complete; fi' >> /etc/bashrc\
 && echo "source ~/.openaf-ojobio-complete" >> /etc/bashrc

USER openaf

# Install openaf and prepare everything
RUN cd /openaf\
 && curl -o openaf.jar https://openaf.io/$OPENAFDIST/openaf.jar.repacked -s\
 && java -jar openaf.jar --install -e 'args=$JAVA_ARGS'\
 && chmod u+x /openaf/.docker/entrypoint.sh\
 && chmod u+x /openaf/getOpenAFOrigJar.js\
 && curl -s https://ojob.io/autoComplete.sh > ~/.openaf-ojobio-complete

WORKDIR /openaf
ENTRYPOINT ["/openaf/.docker/entrypoint.sh"]
