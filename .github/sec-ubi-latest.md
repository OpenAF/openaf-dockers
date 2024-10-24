````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:26245f364b6f5d223003dc344ec1eb5eb8439052bfecb31d79aeba0c74344b3a
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-10-24T07:08:56Z	INFO	[vulndb] Need to update DB
│           2024-10-24T07:08:56Z	INFO	[vulndb] Downloading vulnerability DB...
│           2024-10-24T07:08:56Z	INFO	[vulndb] Downloading artifact...	repo="ghcr.io/aquasecurity/trivy-db:2"
│           54.79 MiB / 54.79 MiB [----------------------------------------------------------->] 100.00% ? p/s
│           ?54.79 MiB / 54.79 MiB [----------------------------------------------------------->] 100.00% ? p/s
│            ?54.79 MiB / 54.79 MiB [----------------------------------------------------------->] 100.00% ?
│           p/s ?54.79 MiB / 54.79 MiB [----------------------------------------------------------->] 100.00% ?
│            p/s ?54.79 MiB / 54.79 MiB [----------------------------------------------------------->] 100.00%
│           ? p/s ?54.79 MiB / 54.79 MiB [----------------------------------------------------------->] 100.00%
│            ? p/s ?54.79 MiB / 54.79 MiB [----------------------------------------------------------->]
│           100.00% ? p/s ?54.79 MiB / 54.79 MiB [----------------------------------------------------------->]
│            100.00% ? p/s ?54.79 MiB / 54.79 MiB
│           [----------------------------------------------------------->] 100.00% ? p/s ?54.79 MiB / 54.79 MiB
│            [-------------------------------------------------] 100.00% 31.19 MiB p/s
│           2.0s2024-10-24T07:08:58Z	INFO	[vulndb] Artifact successfully
│           downloaded	repo="ghcr.io/aquasecurity/trivy-db:2"
│           2024-10-24T07:08:58Z	INFO	[vuln] Vulnerability scanning is enabled
│           2024-10-24T07:08:58Z	INFO	[secret] Secret scanning is enabled
│           2024-10-24T07:08:58Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2024-10-24T07:08:58Z	INFO	[secret] Please see also
│           https://aquasecurity.github.io/trivy/v0.56/docs/scanner/secret#recommendation for faster secret
│           detection
│           2024-10-24T07:09:08Z	INFO	[javadb] Downloading Java DB...
│           2024-10-24T07:09:08Z	INFO	[javadb] Downloading
│           artifact...	repo="ghcr.io/aquasecurity/trivy-java-db:1"
│           2024-10-24T07:09:08Z	ERROR	[javadb] Failed to download
│           artifact	repo="ghcr.io/aquasecurity/trivy-java-db:1" err="oci download error: failed to fetch the
│           layer: GET
│           https://ghcr.io/v2/aquasecurity/trivy-java-db/blobs/sha256:e95d468624ace95dd39ad3ddb9227a6156512265
│           5cdf5ebd076dfae7a40470dc: TOOMANYREQUESTS: retry-after: 1.232564ms, allowed: 44000/minute"
│           2024-10-24T07:09:08Z	FATAL	Fatal error	image scan error: scan error: scan failed: failed analysis:
│           analyze error: pipeline error: failed to analyze layer
│           (sha256:42c3e4a2bba4bdad5a878431c820546b0181ce80b9e796d5e3af8ebeb611349c): post analysis error:
│           post analysis error: Unable to initialize the Java DB: Java DB update failed: OCI artifact error:
│           failed to download Java DB: failed to download artifact from any source 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/oaf:ubi 
````
