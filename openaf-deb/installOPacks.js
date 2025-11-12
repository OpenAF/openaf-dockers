var OPACKS     = getEnv("OPACKS")
var OPACKS_DIR = getEnv("OPACKS_DIR")
var OPACKS_DB  = getEnv("OPACKS_DB")
var OAF_ORIG   = getEnv("OAF_ORIG")

if (isDef(OPACKS_DB) && OPACKS_DB != null) {
  var packsdb = String(OPACKS_DB).split(/,/)
  if (isArray(packsdb)) packsdb.forEach((v) => { addOPackRemoteDB(v); })
}

if (isDef(OPACKS) && OPACKS != null) {
  var packs = String(OPACKS).split(/,/)
  if (isArray(packs)) oPack("install " + packs.join(" "))
}

if (isDef(OPACKS_DIR) && OPACKS_DIR != null) {
  var files = io.listFiles(String(OPACKS_DIR)).files
  if (isArray(files)) {
     files.forEach((v) => {
        if (v.isFile && v.filename.endsWith(".opack")) oPack("install " + v.canonicalPath)
        if (v.isFolder) oPack("install " + v.canonicalPath)
     });
  }
}

if (isDef(OAF_ORIG)) {
  $rest().get2File("/openaf/openaf.jar.orig", "https://openaf.io/" + getDistribution() + "/openaf-" + getVersion() + ".jar")
}