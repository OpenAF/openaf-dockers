````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:cad5cc4c273b98de4e84d19b481399fae19cd2ba09914239e9d0597fa227a8e4
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-11-08T07:08:32Z	INFO	[vulndb] Need to update DB
│           2024-11-08T07:08:32Z	INFO	[vulndb] Downloading vulnerability DB...
│           2024-11-08T07:08:32Z	INFO	[vulndb] Downloading artifact...	repo="ghcr.io/aquasecurity/trivy-db:2"
│           2024-11-08T07:08:32Z	ERROR	[vulndb] Failed to download
│           artifact	repo="ghcr.io/aquasecurity/trivy-db:2" err="oci download error: failed to fetch the layer:
│            GET
│           https://ghcr.io/v2/aquasecurity/trivy-db/blobs/sha256:8b8d60b85983c2c89042ac1c243d82c2e0b432f8331ff
│           7fd6c7b8f71315907ad: TOOMANYREQUESTS: retry-after: 430.822µs, allowed: 44000/minute"
│           2024-11-08T07:08:32Z	FATAL	Fatal error	init error: DB error: failed to download vulnerability DB:
│           OCI artifact error: failed to download vulnerability DB: failed to download artifact from any
│           source: 1 error occurred:
│           	* oci download error: failed to fetch the layer: GET
│           7fd6c7b8f71315907ad: TOOMANYREQUESTS: retry-after: 430.822µs, allowed: 44000/minute
│            
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm -v trivy-db:/root/.cache/trivy aquasec/trivy -f json  image
            openaf/oaf:ubi 
````
