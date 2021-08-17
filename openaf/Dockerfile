ARG DIST
ARG OPENAFDIST

#FROM openjdk:8-jre-alpine
FROM alpine
ARG DIST
ARG OPENAFDIST

# Upgrade alpine
#RUN apk upgrade\
# && apk upgrade openjdk8-jre

# Copy auxiliary scripts
COPY entrypoint.sh installOPacks.js /openaf/.docker/
COPY getOpenAFOrigJar.js /openaf/

# Install java, Update SSL certificates and clean up + Auxiliary settings
RUN echo 'PATH=$PATH:/openaf' > /etc/profile.d/openaf.sh\
 && mv /etc/profile.d/color_prompt.sh.disabled /etc/profile.d/color_prompt.sh\
 && apk update\
 && apk --no-cache add openjdk8-jre ca-certificates curl openssl sudo\
 && update-ca-certificates\
 && rm -rf /usr/lib/jvm/java-1.8-openjdk/jre/lib/ext/nashorn.jar\
 && rm -rf /usr/lib/jvm/java-1.8-openjdk/jre/man\
 && rm -rf /usr/lib/jvm/java-1.8-openjdk/jre/lib/images\
 && adduser -Ds /bin/sh openaf\
 && chown -R openaf: /openaf\
 && chown -R openaf: /openaf/.docker\
 && echo "openaf ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/openaf

USER openaf

# Install openaf and prepare everthing
RUN cd /openaf\
 && curl -o openaf.jar https://openaf.io/$OPENAFDIST/openaf.jar.repacked -s\
 && java -jar openaf.jar --install\
 && chmod u+x /openaf/.docker/entrypoint.sh\
 && chmod u+x,g-rw,o-rw /openaf/getOpenAFOrigJar.js

WORKDIR /openaf
ENTRYPOINT ["/openaf/.docker/entrypoint.sh"]
