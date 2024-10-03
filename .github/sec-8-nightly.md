````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:e682a9f8db9db6f09731fe2f63e4234d240ec67a811d90974b5af3d40497f843
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-10-03T07:10:20Z	INFO	[vulndb] Need to update DB
│           2024-10-03T07:10:20Z	INFO	[vulndb] Downloading vulnerability DB...
│           2024-10-03T07:10:20Z	INFO	[vulndb] Downloading artifact...	repo="ghcr.io/aquasecurity/trivy-db:2"
│           2024-10-03T07:10:20Z	ERROR	[vulndb] Failed to download
│           artifact	repo="ghcr.io/aquasecurity/trivy-db:2" err="oci download error: failed to fetch the layer:
│            GET
│           https://ghcr.io/v2/aquasecurity/trivy-db/blobs/sha256:77a50f405854d311fdf062f2d7edf3c04c63e2f5d2187
│           51a29125431376757a1: TOOMANYREQUESTS: retry-after: 934.183µs, allowed: 44000/minute"
│           2024-10-03T07:10:20Z	FATAL	Fatal error	init error: DB error: failed to download vulnerability DB:
│           OCI artifact error: failed to download vulnerability DB: failed to download artifact from any
│           source 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/oaf:8-nightly 
````
