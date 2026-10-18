// Run the existing image helper, but treat reported oPack errors as failures.
// startLog/dumpLog are public OpenAF APIs. No package-resolution logic lives here.
try {
    startLog(undefined, -1);
    // Published helpers test isFolder; current io.listFiles returns isDirectory.
    // Adapt only the explicitly selected input directory, in this subprocess.
    var listFiles = io.listFiles;
    io.listFiles = function(path) {
        var result = listFiles(path);
        if (String(path) === String(getEnv('OPACKS_DIR'))) {
            result.files.forEach(function(entry) {
                if (entry.isDirectory) entry.isFolder = true;
            });
        }
        return result;
    };
    try {
        load('/openaf/.docker/installOPacks.js');
    } finally {
        io.listFiles = listFiles;
    }
    var failed = dumpLog().some(function(entry) { return entry.t === 'ERROR'; });
    stopLog();
    if (failed) {
        printErr('openaf-docker: oPack bootstrap reported errors; application not started');
        exit(1);
    }
} catch (error) {
    printErr('openaf-docker: bootstrap failed: ' + error);
    exit(1);
}
