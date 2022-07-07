#!/usr/bin/env /openaf/oaf-sb

$rest().get2File("/openaf/openaf.jar.orig", "https://openaf.io/" + getDistribution() + "/openaf-" + getVersion() + ".jar");