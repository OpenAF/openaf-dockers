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
COPY installOPacks.js /openaf/.docker/installOPacks.js
COPY getOpenAFOrigJar.js /openaf/getOpenAFOrigJar.js
COPY entrypoint.sh /openaf/.docker/entrypoint.sh

# Auxiliary settings
RUN echo 'PATH=$PATH:/openaf' > /etc/profile.d/openaf.sh \
 && mv /etc/profile.d/color_prompt.sh.disabled /etc/profile.d/color_prompt.sh

# Install java, Update SSL certificates and clean up
RUN apk update\
 && apk add openjdk11-jre\
 && apk add ca-certificates wget\
 && update-ca-certificates\
 && apk --no-cache add openssl

# Install openaf and prepare everthing
RUN cd /openaf\
 && wget -O openaf.jar https://openaf.io/$OPENAFDIST/openaf.jar.repacked -q\
 && java -jar openaf.jar --install\
 && chmod u+x /openaf/.docker/entrypoint.sh\
 && chmod u+x /openaf/getOpenAFOrigJar.js

WORKDIR /openaf
ENTRYPOINT ["/openaf/.docker/entrypoint.sh"]
