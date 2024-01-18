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
 && microdnf install -y --nodocs java-21-openjdk-headless tar sudo shadow-utils\
 && echo 'PATH=$PATH:/openaf' > /etc/profile.d/openaf.sh\
 && adduser openaf -u 1000\
 && chown -R openaf: /openaf\
 && echo "openaf ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/openaf\
 && microdnf remove -y shadow-utils\
 && microdnf clean all\
 && echo 'if [ ! -e ~/.openaf-ojobio-complete ] || [ $(find ~/.openaf-ojobio-complete -mtime +1) ]; then curl --max-time 2 -s https://ojob.io/autoComplete.sh > ~/.openaf-ojobio-complete; fi' >> /etc/bashrc\
 && echo "source ~/.openaf-ojobio-complete" >> /etc/bashrc

USER 1000

# Install openaf and prepare everything
RUN cd /openaf\
 && curl -o openaf.jar https://openaf.io/$OPENAFDIST/openaf.jar.repacked -s\
 && java -jar openaf.jar --install -e 'args=$JAVA_ARGS'\
 && chown -R openaf:0 /openaf\
 && chmod -R a+rwx /openaf\
 && chmod -R u+rwx,g+rwx,o+rx /openaf/*\
 && chmod -R a+rx /openaf/.docker\
 && curl -s https://ojob.io/autoComplete.sh > ~/.openaf-ojobio-complete

# -------------------
FROM scratch as final

COPY --from=main / /

ENV OAF_HOME=/openaf
USER 1000

WORKDIR /openaf
ENTRYPOINT ["/openaf/.docker/entrypoint.sh"]
