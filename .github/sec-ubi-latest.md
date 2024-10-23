````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:26245f364b6f5d223003dc344ec1eb5eb8439052bfecb31d79aeba0c74344b3a
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-10-21T07:10:38Z	INFO	[vulndb] Need to update DB
│           2024-10-21T07:10:38Z	INFO	[vulndb] Downloading vulnerability DB...
│           2024-10-21T07:10:38Z	INFO	[vulndb] Downloading artifact...	repo="ghcr.io/aquasecurity/trivy-db:2"
│           2024-10-21T07:10:39Z	ERROR	[vulndb] Failed to download
│           artifact	repo="ghcr.io/aquasecurity/trivy-db:2" err="oci download error: failed to fetch the layer:
│            GET
│           https://ghcr.io/v2/aquasecurity/trivy-db/blobs/sha256:c510109649e886ad7244015fa12b358ce3e53d1295596
│           e930f3ef946c57b53ea: TOOMANYREQUESTS: retry-after: 1.170158ms, allowed: 44000/minute"
│           2024-10-21T07:10:39Z	FATAL	Fatal error	init error: DB error: failed to download vulnerability DB:
│           OCI artifact error: failed to download vulnerability DB: failed to download artifact from any
│           source 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/oaf:ubi 
````
