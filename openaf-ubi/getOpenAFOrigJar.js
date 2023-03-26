#!/usr/bin/env /openaf/oaf-sb

var dist = getDistribution()
$rest().get2File("/openaf/openaf.jar.orig", "https://openaf.io" + (dist == "stable" ? "" : "/" + dist) + "/openaf-" + getVersion() + ".jar")