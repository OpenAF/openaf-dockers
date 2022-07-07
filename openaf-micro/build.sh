microcontainer=$(buildah from registry.access.redhat.com/ubi8/ubi-micro)
micromount=$(buildah mount $microcontainer)
cd $micromount
mkdir openaf
echo 'PATH=$PATH:/openaf' > etc/profile.d/openaf.sh
curl -o openaf/openaf.jar https://openaf.io/openaf.jar.repacked -s
mkdir openaf/.docker
cp /openaf-micro/entrypoint.sh openaf/.docker/.
cp /openaf-micro/getOpenAFOrigJar.js openaf/.
chmod u+x openaf/.docker/entrypoint.sh
chmod u+x openaf/getOpenAFOrigJar.js
cd openaf
ojob ojob.io/java/download
tar xzf jre.tgz
rm jre.tgz
rm jre/lib/ext/nashorn.jar
rm -rf jre/lib/images/jre/man
rm -rf jre/lib/images
jre/bin/java -jar openaf.jar --install
rm openaf.jar.orig
buildah umount $microcontainer
buildah commit $microcontainer 
