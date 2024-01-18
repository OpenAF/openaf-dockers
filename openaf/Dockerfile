ARG DIST
ARG OPENAFDIST

#FROM openjdk:8-jre-alpine
FROM alpine as main
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
 && apk --no-cache add openjdk21-jre ca-certificates curl openssl sudo\
 && update-ca-certificates\
 && adduser -Ds /bin/sh openaf\
 && echo "openaf ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/openaf

# Install openaf and prepare everthing
RUN cd /openaf\
 && curl -o openaf.jar https://openaf.io/$OPENAFDIST/openaf.jar.repacked -s\
 && java -jar openaf.jar --install\
 && chown -R openaf:0 /openaf\
 && chmod -R a+rwx /openaf\
 && chmod -R a+rx /openaf/.docker

# -------------------
FROM scratch as final

COPY --from=main / /

ENV OAF_HOME=/openaf
USER openaf

WORKDIR /openaf
ENTRYPOINT ["/bin/sh", "/openaf/.docker/entrypoint.sh"]
