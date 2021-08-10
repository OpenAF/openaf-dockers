ARG DIST
ARG OPENAFDIST

FROM registry.access.redhat.com/ubi8/ubi-minimal 
ARG DIST
ARG OPENAFDIST

# Upgrade alpine
RUN microdnf upgrade\
 && microdnf install -y java-1.8.0-openjdk-headless\
 && microdnf clean all

# Copy auxiliary scripts
COPY installOPacks.js /openaf/.docker/installOPacks.js
COPY getOpenAFOrigJar.js /openaf/getOpenAFOrigJar.js
COPY entrypoint.sh /openaf/.docker/entrypoint.sh

# Auxiliary settings
RUN echo 'PATH=$PATH:/openaf' > /etc/profile.d/openaf.sh 

# Cleanups to get slimer version
RUN rm -rf /usr/lib/jvm/java-1.8.0-openjdk-*/jre/lib/ext/nashorn.jar\
 && rm -rf /usr/lib/jvm/java-1.8.0-openjdk-*/jre/lib/images/jre/man\
 && rm -rf /usr/lib/jvm/java-1.8.0-openjdk-*/jre/lib/images

# Install openaf and prepare everthing
RUN cd /openaf\
 # && wget -O openaf.jar.orig https://openaf.io/$OPENAFDIST/openaf.jar -q\
 && curl -o openaf.jar https://openaf.io/$OPENAFDIST/openaf.jar.repacked -q\
 && java -jar openaf.jar --install\
 && chmod u+x /openaf/.docker/entrypoint.sh\
 && chmod u+x /openaf/getOpenAFOrigJar.js

WORKDIR /openaf
ENTRYPOINT ["/openaf/.docker/entrypoint.sh"]
