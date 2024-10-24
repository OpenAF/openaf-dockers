````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:26245f364b6f5d223003dc344ec1eb5eb8439052bfecb31d79aeba0c74344b3a
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-10-24T07:09:58Z	INFO	[vulndb] Need to update DB
│           2024-10-24T07:09:58Z	INFO	[vulndb] Downloading vulnerability DB...
│           2024-10-24T07:09:58Z	INFO	[vulndb] Downloading artifact...	repo="ghcr.io/aquasecurity/trivy-db:2"
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
│            [-------------------------------------------------] 100.00% 31.16 MiB p/s
│           2.0s2024-10-24T07:10:00Z	INFO	[vulndb] Artifact successfully
│           downloaded	repo="ghcr.io/aquasecurity/trivy-db:2"
│           2024-10-24T07:10:00Z	INFO	[vuln] Vulnerability scanning is enabled
│           2024-10-24T07:10:00Z	INFO	[secret] Secret scanning is enabled
│           2024-10-24T07:10:00Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2024-10-24T07:10:00Z	INFO	[secret] Please see also
│           https://aquasecurity.github.io/trivy/v0.56/docs/scanner/secret#recommendation for faster secret
│           detection
│           2024-10-24T07:10:04Z	INFO	[javadb] Downloading Java DB...
│           2024-10-24T07:10:04Z	INFO	[javadb] Downloading
│           artifact...	repo="ghcr.io/aquasecurity/trivy-java-db:1"
│           2024-10-24T07:10:04Z	ERROR	[javadb] Failed to download
│           artifact	repo="ghcr.io/aquasecurity/trivy-java-db:1" err="OCI repository error: 1 error
│           occurred:\n\t* GET https://ghcr.io/v2/aquasecurity/trivy-java-db/manifests/1: TOOMANYREQUESTS:
│           retry-after: 1.200705ms, allowed: 44000/minute\n\n"
│           2024-10-24T07:10:04Z	FATAL	Fatal error	image scan error: scan error: scan failed: failed analysis:
│           analyze error: pipeline error: failed to analyze layer
│           (sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed28ea1250ef005595c5f9): post analysis error:
│           post analysis error: Unable to initialize the Java DB: Java DB update failed: OCI artifact error:
│           failed to download Java DB: failed to download artifact from any source 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/oaf:8-latest 
````
