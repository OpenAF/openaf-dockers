````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:addfb8fd6b9e520c25b22c61d8aa5d58ecd7879177aa959f952bf4734f4e3f60
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-09-24T07:10:15Z	INFO	[db] Need to update DB
│           2024-09-24T07:10:15Z	INFO	[db] Downloading DB...	repository="ghcr.io/aquasecurity/trivy-db:2"
│           53.58 MiB / 53.58 MiB [----------------------------------------------------------->] 100.00% ? p/s
│           ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->] 100.00% ? p/s
│            ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->] 100.00% ?
│           p/s ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->] 100.00% ?
│            p/s ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->] 100.00%
│           ? p/s ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->] 100.00%
│            ? p/s ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->]
│           100.00% ? p/s ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->]
│            100.00% ? p/s ?53.58 MiB / 53.58 MiB [-------------------------------------------------] 100.00%
│           34.54 MiB p/s 1.8s2024-09-24T07:10:17Z	INFO	[vuln] Vulnerability scanning is enabled
│           2024-09-24T07:10:17Z	INFO	[secret] Secret scanning is enabled
│           2024-09-24T07:10:17Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2024-09-24T07:10:17Z	INFO	[secret] Please see also
│           https://aquasecurity.github.io/trivy/v0.55/docs/scanner/secret#recommendation for faster secret
│           detection
│           2024-09-24T07:10:20Z	INFO	Java DB Repository	repository=ghcr.io/aquasecurity/trivy-java-db:1
│           2024-09-24T07:10:20Z	INFO	Downloading the Java DB...
│           2024-09-24T07:10:21Z	FATAL	Fatal error	image scan error: scan error: scan failed: failed analysis:
│           analyze error: pipeline error: failed to analyze layer
│           (sha256:5e9a5d0961a2b45ae6c236e4f8ac9ebd620ade276443a394ef86cdd561fc26f7): post analysis error:
│           post analysis error: Unable to initialize the Java DB: Java DB update failed: DB download error:
│           OCI repository error: 1 error occurred:
│           	* GET https://ghcr.io/v2/aquasecurity/trivy-java-db/manifests/1: TOOMANYREQUESTS: retry-after:
│           697.225µs, allowed: 44000/minute
│            
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/oaf:8-latest 
````
