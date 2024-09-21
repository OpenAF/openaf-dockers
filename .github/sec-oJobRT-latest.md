````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:addfb8fd6b9e520c25b22c61d8aa5d58ecd7879177aa959f952bf4734f4e3f60
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-09-18T13:10:19Z	INFO	[db] Need to update DB
│           2024-09-18T13:10:19Z	INFO	[db] Downloading DB...	repository="ghcr.io/aquasecurity/trivy-db:2"
│           2024-09-18T13:10:19Z	FATAL	Fatal error	init error: DB error: failed to download vulnerability DB:
│           database download error: oci download error: failed to fetch the layer: GET
│           https://ghcr.io/v2/aquasecurity/trivy-db/blobs/sha256:4104f3122c25da34b44ccedf9aa5f82ec44d3d5d0433b
│           9fcf54cadc062052e8a: TOOMANYREQUESTS: retry-after: 284.343µs, allowed: 44000/minute 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/ojobrt:latest 
````
