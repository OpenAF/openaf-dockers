````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:addfb8fd6b9e520c25b22c61d8aa5d58ecd7879177aa959f952bf4734f4e3f60
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-09-24T07:12:31Z	INFO	[db] Need to update DB
│           2024-09-24T07:12:31Z	INFO	[db] Downloading DB...	repository="ghcr.io/aquasecurity/trivy-db:2"
│           53.58 MiB / 53.58 MiB [----------------------------------------------------------->] 100.00% ? p/s
│           ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->] 100.00% ? p/s
│            ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->] 100.00% ?
│           p/s ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->] 100.00% ?
│            p/s ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->] 100.00%
│           ? p/s ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->] 100.00%
│            ? p/s ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->]
│           100.00% ? p/s ?53.58 MiB / 53.58 MiB [----------------------------------------------------------->]
│            100.00% ? p/s ?53.58 MiB / 53.58 MiB [-------------------------------------------------] 100.00%
│           34.52 MiB p/s 1.8s2024-09-24T07:12:33Z	INFO	[vuln] Vulnerability scanning is enabled
│           2024-09-24T07:12:33Z	INFO	[secret] Secret scanning is enabled
│           2024-09-24T07:12:33Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2024-09-24T07:12:33Z	INFO	[secret] Please see also
│           https://aquasecurity.github.io/trivy/v0.55/docs/scanner/secret#recommendation for faster secret
│           detection
│           2024-09-24T07:12:35Z	INFO	Java DB Repository	repository=ghcr.io/aquasecurity/trivy-java-db:1
│           2024-09-24T07:12:35Z	INFO	Downloading the Java DB...
│           2024-09-24T07:12:35Z	FATAL	Fatal error	image scan error: scan error: scan failed: failed analysis:
│           analyze error: pipeline error: failed to analyze layer
│           (sha256:33619e618e28ac56dd850b8bffe80d888f7f58633dabbd761e670726bd609e7e): post analysis error:
│           post analysis error: Unable to initialize the Java DB: Java DB update failed: DB download error:
│           oci download error: failed to fetch the layer: GET
│           https://ghcr.io/v2/aquasecurity/trivy-java-db/blobs/sha256:9db93b26e3cf8e1145331700e688ae806815ad19
│           5271dfdf171f89e633d349a4: TOOMANYREQUESTS: retry-after: 457.167µs, allowed: 44000/minute 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/ojobrt:8-nightly 
````
