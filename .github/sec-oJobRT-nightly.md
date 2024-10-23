````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:26245f364b6f5d223003dc344ec1eb5eb8439052bfecb31d79aeba0c74344b3a
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-10-23T02:36:23Z	INFO	[vulndb] Need to update DB
│           2024-10-23T02:36:23Z	INFO	[vulndb] Downloading vulnerability DB...
│           2024-10-23T02:36:23Z	INFO	[vulndb] Downloading artifact...	repo="ghcr.io/aquasecurity/trivy-db:2"
│           54.61 MiB / 54.61 MiB [----------------------------------------------------------->] 100.00% ? p/s
│           ?54.61 MiB / 54.61 MiB [----------------------------------------------------------->] 100.00% ? p/s
│            ?54.61 MiB / 54.61 MiB [----------------------------------------------------------->] 100.00% ?
│           p/s ?54.61 MiB / 54.61 MiB [----------------------------------------------------------->] 100.00% ?
│            p/s ?54.61 MiB / 54.61 MiB [----------------------------------------------------------->] 100.00%
│           ? p/s ?54.61 MiB / 54.61 MiB [----------------------------------------------------------->] 100.00%
│            ? p/s ?54.61 MiB / 54.61 MiB [----------------------------------------------------------->]
│           100.00% ? p/s ?54.61 MiB / 54.61 MiB [----------------------------------------------------------->]
│            100.00% ? p/s ?54.61 MiB / 54.61 MiB
│           [----------------------------------------------------------->] 100.00% ? p/s ?54.61 MiB / 54.61 MiB
│            [-------------------------------------------------] 100.00% 30.84 MiB p/s
│           2.0s2024-10-23T02:36:25Z	INFO	[vulndb] Artifact successfully
│           downloaded	repo="ghcr.io/aquasecurity/trivy-db:2"
│           2024-10-23T02:36:25Z	INFO	[vuln] Vulnerability scanning is enabled
│           2024-10-23T02:36:25Z	INFO	[secret] Secret scanning is enabled
│           2024-10-23T02:36:25Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2024-10-23T02:36:25Z	INFO	[secret] Please see also
│           https://aquasecurity.github.io/trivy/v0.56/docs/scanner/secret#recommendation for faster secret
│           detection
│           2024-10-23T02:36:26Z	FATAL	Fatal error	image scan error: scan error: scan failed: failed analysis:
│           analyze error: pipeline error: failed to analyze layer
│           (sha256:249f61e2f18db1438402cb3f0d0f5e6aadb6a9629ad0c41f5f9f941c4ccc8465): walk error: failed to
│           process the file: failed to analyze file: failed to analyze openaf/S3/bcprov-jdk18on-1.78.jar:
│           unable to open openaf/S3/bcprov-jdk18on-1.78.jar: failed to open: unable to read the file: stream
│           error: stream ID 7; INTERNAL_ERROR; received from peer 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/ojobrt:nightly 
````
