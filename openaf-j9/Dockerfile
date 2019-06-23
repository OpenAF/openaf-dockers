FROM adoptopenjdk/openjdk8-openj9:alpine
ARG DIST
ARG OPENAFDIST

# Copy auxiliary scripts
COPY installOPacks.js /openaf/.docker/installOPacks.js
COPY entrypoint.sh /openaf/.docker/entrypoint.sh

# Update SSL certificates
RUN apk update\
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
 && java -Xtune:virtualized -Xshareclasses:persistent -Xshareclasses:name=openaf -Xshareclasses:cacheDir=/openaf -jar openaf.jar --repack\
 && sleep 2\
 && java -Xtune:virtualized -Xshareclasses:persistent -Xshareclasses:name=openaf -Xshareclasses:cacheDir=/openaf -jar openaf.jar --install args="-Xquickstart -Xtune:virtualized -Xshareclasses:persistent -Xshareclasses:name=openaf -Xshareclasses:cacheDir=/openaf"\
 && chmod u+x /openaf/.docker/entrypoint.sh

WORKDIR /openaf
ENTRYPOINT ["/openaf/.docker/entrypoint.sh"]
