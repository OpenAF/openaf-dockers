````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:cad5cc4c273b98de4e84d19b481399fae19cd2ba09914239e9d0597fa227a8e4
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-11-07T00:32:56Z	INFO	[vulndb] Need to update DB
│           2024-11-07T00:32:56Z	INFO	[vulndb] Downloading vulnerability DB...
│           2024-11-07T00:32:56Z	INFO	[vulndb] Downloading artifact...	repo="ghcr.io/aquasecurity/trivy-db:2"
│           2024-11-07T00:32:56Z	ERROR	[vulndb] Failed to download
│           artifact	repo="ghcr.io/aquasecurity/trivy-db:2" err="oci download error: failed to fetch the layer:
│            GET
│           https://ghcr.io/v2/aquasecurity/trivy-db/blobs/sha256:57a4273faac0d5c4f135926583a11b3613106dc524b10
│           870e5725b5226edbce2: TOOMANYREQUESTS: retry-after: 1.138806ms, allowed: 44000/minute"
│           2024-11-07T00:32:56Z	FATAL	Fatal error	init error: DB error: failed to download vulnerability DB:
│           OCI artifact error: failed to download vulnerability DB: failed to download artifact from any
│           source: 1 error occurred:
│           	* oci download error: failed to fetch the layer: GET
│           870e5725b5226edbce2: TOOMANYREQUESTS: retry-after: 1.138806ms, allowed: 44000/minute
│            
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm -v trivy-db:/root/.cache/trivy aquasec/trivy -f json  image
            openaf/ojobrt:latest 
````
