var params = processExpr(" ");

if (isString(params.op)) {
    switch (params.op) {
    case "init":
        log("Initializing init folder...");
        $sh("cp -R /openaf/nAttrMon/config/. /config/.").prefix("init").get();

        log("Copy initial files...");
        [
            { f: "/openaf/nAttrMon/config/outputs.disabled/yaml/00.httphealthz.yaml", t: "/config/outputs/01.httphealthz.yaml" },
            { f: "/openaf/nAttrMon/config/outputs.disabled/yaml/02.httpjson.yaml", t: "/config/outputs/02.httpjson.yaml" },
            { f: "/openaf/nAttrMon/config/outputs.disabled/yaml/03.http.yaml", t: "/config/outputs/03.http.yaml" },
            { f: "/openaf/nAttrMon/config/outputs.disabled/yaml/04.httpmetrics.yaml", t: "/config/outputs/04.httpmetrics.yaml" },
            { f: "/openaf/nAttrMon/config/outputs.disabled/yaml/09.channels.yaml", t: "/config/outputs/09.channels.yaml" }
        ].forEach(m => {
            log("Creating " + m.t + "...");
            io.cp(m.f, m.t);
        });
        log("Done.");
        exit(0);
        break;
    default:
        loadLIb("nattrmon.js");
    }
} else {
    loadLib("nattrmon.js");
}