````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:addfb8fd6b9e520c25b22c61d8aa5d58ecd7879177aa959f952bf4734f4e3f60
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-10-01T07:11:28Z	INFO	[db] Need to update DB
│           2024-10-01T07:11:28Z	INFO	[db] Downloading DB...	repository="ghcr.io/aquasecurity/trivy-db:2"
│           2024-10-01T07:11:28Z	FATAL	Fatal error	init error: DB error: failed to download vulnerability DB:
│           database download error: oci download error: failed to fetch the layer: GET
│           https://ghcr.io/v2/aquasecurity/trivy-db/blobs/sha256:23d1b901e7534020d5ac5f238b090ad66dcb78afef730
│           1ed7d8ebe6b974ab5f1: TOOMANYREQUESTS: retry-after: 702.679µs, allowed: 44000/minute 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/oaf:8-ubi-nightly 
````
