ARG DIST
ARG OPENAFDIST

FROM openjdk:8-jdk-alpine
ARG DIST
ARG OPENAFDIST

# Copy auxiliary scripts
COPY installOPacks.js /openaf/.docker/installOPacks.js
COPY entrypoint.sh /openaf/.docker/entrypoint.sh

# Auxiliary settings
RUN echo 'PATH=$PATH:/openaf' > /etc/profile.d/openaf.sh \
 && mv /etc/profile.d/color_prompt /etc/profile.d/color_prompt.sh

# Update SSL certificates
RUN apk update\
 && apk add ca-certificates wget\
 && update-ca-certificates\
 && apk --no-cache add openssl wget

# Install openaf and prepare everthing
RUN cd /openaf\
 && wget https://openaf.io/$OPENAFDIST/openaf.jar -q\
 && java -jar openaf.jar --repack\
 && sleep 2\
 && java -jar openaf.jar --install\
 && chmod u+x /openaf/.docker/entrypoint.sh

WORKDIR /openaf
ENTRYPOINT ["/openaf/.docker/entrypoint.sh"]
