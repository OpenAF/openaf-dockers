````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:addfb8fd6b9e520c25b22c61d8aa5d58ecd7879177aa959f952bf4734f4e3f60
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-09-18T13:11:19Z	INFO	[db] Need to update DB
│           2024-09-18T13:11:19Z	INFO	[db] Downloading DB...	repository="ghcr.io/aquasecurity/trivy-db:2"
│           53.31 MiB / 53.31 MiB [----------------------------------------------------------->] 100.00% ? p/s
│           ?53.31 MiB / 53.31 MiB [----------------------------------------------------------->] 100.00% ? p/s
│            ?53.31 MiB / 53.31 MiB [----------------------------------------------------------->] 100.00% ?
│           p/s ?53.31 MiB / 53.31 MiB [----------------------------------------------------------->] 100.00% ?
│            p/s ?53.31 MiB / 53.31 MiB [----------------------------------------------------------->] 100.00%
│           ? p/s ?53.31 MiB / 53.31 MiB [----------------------------------------------------------->] 100.00%
│            ? p/s ?53.31 MiB / 53.31 MiB [----------------------------------------------------------->]
│           100.00% ? p/s ?53.31 MiB / 53.31 MiB [----------------------------------------------------------->]
│            100.00% ? p/s ?53.31 MiB / 53.31 MiB [-------------------------------------------------] 100.00%
│           34.98 MiB p/s 1.7s2024-09-18T13:11:21Z	INFO	[vuln] Vulnerability scanning is enabled
│           2024-09-18T13:11:21Z	INFO	[secret] Secret scanning is enabled
│           2024-09-18T13:11:21Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2024-09-18T13:11:21Z	INFO	[secret] Please see also
│           https://aquasecurity.github.io/trivy/v0.55/docs/scanner/secret#recommendation for faster secret
│           detection
│           2024-09-18T13:11:24Z	INFO	Java DB Repository	repository=ghcr.io/aquasecurity/trivy-java-db:1
│           2024-09-18T13:11:24Z	INFO	Downloading the Java DB...
│           2024-09-18T13:11:24Z	FATAL	Fatal error	image scan error: scan error: scan failed: failed analysis:
│           analyze error: pipeline error: failed to analyze layer
│           (sha256:200fe82c90d26374909c4f29f5388f33b0480e17f7953689bc34cfb0b5061ed4): post analysis error:
│           post analysis error: Unable to initialize the Java DB: Java DB update failed: DB download error:
│           oci download error: failed to fetch the layer: GET
│           https://ghcr.io/v2/aquasecurity/trivy-java-db/blobs/sha256:c92eadafdf3b8ed7fa646e41ba43dcd5f25b340b
│           d4d33907cdcdfbe116ca2a72: TOOMANYREQUESTS: retry-after: 638.693µs, allowed: 44000/minute 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/oaf:8-nightly 
````
