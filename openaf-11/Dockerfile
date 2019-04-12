ARG DIST
ARG OPENAFDIST

FROM adoptopenjdk/openjdk11:alpine
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
 && wget https://openaf.io/$OPENAFDIST/openaf.jar -q\
 && java -jar openaf.jar --repack\
 && java -jar openaf.jar --install\
 && chmod u+x /openaf/.docker/entrypoint.sh

RUN cd /openaf\
 && export JAVA_TOOL_OPTIONS=" -XX:+IgnoreUnrecognizedVMOptions -XX:+UseContainerSupport -XX:+IdleTuningCompactOnIdle -XX:+IdleTuningGcOnIdle"\
 && unzip openaf.jar.orig js.jar\
 && mkdir tmp\
 && cd tmp\
 && unzip ../js.jar\
 && rm ../js.jar\
 && unzip ../openaf.jar openaf_js.class\
 && unzip ../openaf.jar openafsigil_js.class\
 && cd ..\
 && jaotc --output openaf-js.so --directory tmp\
 && rm -rf tmp\
 && java -jar openaf.jar --install -e args="-XX:AOTLibrary=/openaf/openaf-js.so -XX:+IgnoreUnrecognizedVMOptions -XX:+UseContainerSupport -XX:+IdleTuningCompactOnIdle -XX:+IdleTuningGcOnIdle"

WORKDIR /openaf
ENTRYPOINT ["/openaf/.docker/entrypoint.sh"]