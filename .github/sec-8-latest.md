````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:e682a9f8db9db6f09731fe2f63e4234d240ec67a811d90974b5af3d40497f843
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-10-03T07:10:11Z	INFO	[vulndb] Need to update DB
│           2024-10-03T07:10:11Z	INFO	[vulndb] Downloading vulnerability DB...
│           2024-10-03T07:10:11Z	INFO	[vulndb] Downloading artifact...	repo="ghcr.io/aquasecurity/trivy-db:2"
│           2024-10-03T07:10:11Z	ERROR	[vulndb] Failed to download
│           artifact	repo="ghcr.io/aquasecurity/trivy-db:2" err="OCI repository error: 1 error occurred:\n\t*
│           GET https://ghcr.io/v2/aquasecurity/trivy-db/manifests/2: TOOMANYREQUESTS: retry-after: 317.692µs,
│           allowed: 44000/minute\n\n"
│           2024-10-03T07:10:11Z	FATAL	Fatal error	init error: DB error: failed to download vulnerability DB:
│           OCI artifact error: failed to download vulnerability DB: failed to download artifact from any
│           source 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/oaf:8-latest 
````
