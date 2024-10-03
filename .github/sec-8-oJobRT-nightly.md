````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:e682a9f8db9db6f09731fe2f63e4234d240ec67a811d90974b5af3d40497f843
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-10-03T07:11:34Z	INFO	[vulndb] Need to update DB
│           2024-10-03T07:11:34Z	INFO	[vulndb] Downloading vulnerability DB...
│           2024-10-03T07:11:34Z	INFO	[vulndb] Downloading artifact...	repo="ghcr.io/aquasecurity/trivy-db:2"
│           53.95 MiB / 53.95 MiB [----------------------------------------------------------->] 100.00% ? p/s
│           ?53.95 MiB / 53.95 MiB [----------------------------------------------------------->] 100.00% ? p/s
│            ?53.95 MiB / 53.95 MiB [----------------------------------------------------------->] 100.00% ?
│           p/s ?53.95 MiB / 53.95 MiB [----------------------------------------------------------->] 100.00% ?
│            p/s ?53.95 MiB / 53.95 MiB [----------------------------------------------------------->] 100.00%
│           ? p/s ?53.95 MiB / 53.95 MiB [----------------------------------------------------------->] 100.00%
│            ? p/s ?53.95 MiB / 53.95 MiB [----------------------------------------------------------->]
│           100.00% ? p/s ?53.95 MiB / 53.95 MiB [----------------------------------------------------------->]
│            100.00% ? p/s ?53.95 MiB / 53.95 MiB [-------------------------------------------------] 100.00%
│           34.85 MiB p/s 1.7s2024-10-03T07:11:36Z	INFO	[vulndb] Artifact successfully
│           downloaded	repo="ghcr.io/aquasecurity/trivy-db:2"
│           2024-10-03T07:11:36Z	INFO	[vuln] Vulnerability scanning is enabled
│           2024-10-03T07:11:36Z	INFO	[secret] Secret scanning is enabled
│           2024-10-03T07:11:36Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2024-10-03T07:11:36Z	INFO	[secret] Please see also
│           https://aquasecurity.github.io/trivy/v0.56/docs/scanner/secret#recommendation for faster secret
│           detection
│           2024-10-03T07:11:37Z	INFO	[javadb] Downloading Java DB...
│           2024-10-03T07:11:37Z	INFO	[javadb] Downloading
│           artifact...	repo="ghcr.io/aquasecurity/trivy-java-db:1"
│           2024-10-03T07:11:37Z	ERROR	[javadb] Failed to download
│           artifact	repo="ghcr.io/aquasecurity/trivy-java-db:1" err="oci download error: failed to fetch the
│           layer: GET
│           https://ghcr.io/v2/aquasecurity/trivy-java-db/blobs/sha256:74e4dae8423bd915af4934cc666a29e1dc2ff87f
│           6f23deb50c3a5c6c987d883a: TOOMANYREQUESTS: retry-after: 516.98µs, allowed: 44000/minute"
│           2024-10-03T07:11:37Z	FATAL	Fatal error	image scan error: scan error: scan failed: failed analysis:
│           analyze error: pipeline error: failed to analyze layer
│           (sha256:244c6278a9ab2dbb4be86e60bcc4157033a73faaeffa6a2a7da0c046899889ac): post analysis error:
│           post analysis error: Unable to initialize the Java DB: Java DB update failed: OCI artifact error:
│           failed to download vulnerability DB: failed to download artifact from any source 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/ojobrt:8-nightly 
````
