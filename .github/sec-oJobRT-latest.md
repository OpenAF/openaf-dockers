````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:26245f364b6f5d223003dc344ec1eb5eb8439052bfecb31d79aeba0c74344b3a
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-10-21T07:10:49Z	INFO	[vulndb] Need to update DB
│           2024-10-21T07:10:49Z	INFO	[vulndb] Downloading vulnerability DB...
│           2024-10-21T07:10:49Z	INFO	[vulndb] Downloading artifact...	repo="ghcr.io/aquasecurity/trivy-db:2"
│           54.37 MiB / 54.37 MiB [----------------------------------------------------------->] 100.00% ? p/s
│           ?54.37 MiB / 54.37 MiB [----------------------------------------------------------->] 100.00% ? p/s
│            ?54.37 MiB / 54.37 MiB [----------------------------------------------------------->] 100.00% ?
│           p/s ?54.37 MiB / 54.37 MiB [----------------------------------------------------------->] 100.00% ?
│            p/s ?54.37 MiB / 54.37 MiB [----------------------------------------------------------->] 100.00%
│           ? p/s ?54.37 MiB / 54.37 MiB [----------------------------------------------------------->] 100.00%
│            ? p/s ?54.37 MiB / 54.37 MiB [----------------------------------------------------------->]
│           100.00% ? p/s ?54.37 MiB / 54.37 MiB [----------------------------------------------------------->]
│            100.00% ? p/s ?54.37 MiB / 54.37 MiB
│           [----------------------------------------------------------->] 100.00% ? p/s ?54.37 MiB / 54.37 MiB
│            [-------------------------------------------------] 100.00% 30.88 MiB p/s
│           2.0s2024-10-21T07:10:52Z	INFO	[vulndb] Artifact successfully
│           downloaded	repo="ghcr.io/aquasecurity/trivy-db:2"
│           2024-10-21T07:10:52Z	INFO	[vuln] Vulnerability scanning is enabled
│           2024-10-21T07:10:52Z	INFO	[secret] Secret scanning is enabled
│           2024-10-21T07:10:52Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2024-10-21T07:10:52Z	INFO	[secret] Please see also
│           https://aquasecurity.github.io/trivy/v0.56/docs/scanner/secret#recommendation for faster secret
│           detection
│           2024-10-21T07:10:53Z	INFO	[javadb] Downloading Java DB...
│           2024-10-21T07:10:53Z	INFO	[javadb] Downloading
│           artifact...	repo="ghcr.io/aquasecurity/trivy-java-db:1"
│           2024-10-21T07:10:54Z	ERROR	[javadb] Failed to download
│           artifact	repo="ghcr.io/aquasecurity/trivy-java-db:1" err="oci download error: failed to fetch the
│           layer: GET
│           https://ghcr.io/v2/aquasecurity/trivy-java-db/blobs/sha256:20cb5539a08cda4a3821bc3963d458522703f8ea
│           e4e65d3341689e335adef4cb: TOOMANYREQUESTS: retry-after: 213.146µs, allowed: 44000/minute"
│           2024-10-21T07:10:54Z	FATAL	Fatal error	image scan error: scan error: scan failed: failed analysis:
│           analyze error: pipeline error: failed to analyze layer
│           (sha256:bfa73751de9766a462867814ddb9e2f2654d016001be55d5fc388b00d0acc82e): post analysis error:
│           post analysis error: Unable to initialize the Java DB: Java DB update failed: OCI artifact error:
│           failed to download Java DB: failed to download artifact from any source 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/ojobrt:latest 
````
