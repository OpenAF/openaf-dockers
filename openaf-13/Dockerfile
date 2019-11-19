ARG DIST
ARG OPENAFDIST

FROM openjdk:13-alpine
ARG DIST
ARG OPENAFDIST

# Copy auxiliary scripts
COPY installOPacks.js /openaf/.docker/installOPacks.js
COPY entrypoint.sh /openaf/.docker/entrypoint.sh

# Update SSL certificates
RUN apk update\
 && apk add gcc\
 && apk add ca-certificates wget\
 && update-ca-certificates\
 && apk --no-cache add openssl wget

# Auxiliary settings
RUN echo 'PATH=$PATH:/openaf' > /etc/profile.d/openaf.sh \
 && echo 'unset JAVA_TOOL_OPTIONS' >> /etc/profile.d/openaf.sh\
 && mv /etc/profile.d/color_prompt /etc/profile.d/color_prompt.sh

# Install openaf and prepare everthing
RUN cd /openaf\
 && wget https://openaf.io/$OPENAFDIST/openaf.jar -O openaf.jar.orig -q\
 && wget https://openaf.io/$OPENAFDIST/openaf.jar.repacked -O openaf.jar -q\
 && java -jar openaf.jar --install -e args="-Xshare:off -XX:+IgnoreUnrecognizedVMOptions -XX:+UseContainerSupport -XX:MaxRAMPercentage=90.0 -XX:+IdleTuningCompactOnIdle -XX:+IdleTuningGcOnIdle"\
 && chmod u+x /openaf/.docker/entrypoint.sh

WORKDIR /openaf
ENTRYPOINT ["/openaf/.docker/entrypoint.sh"]