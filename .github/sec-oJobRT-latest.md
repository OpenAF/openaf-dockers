````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:addfb8fd6b9e520c25b22c61d8aa5d58ecd7879177aa959f952bf4734f4e3f60
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-09-26T07:09:29Z	INFO	[db] Need to update DB
│           2024-09-26T07:09:29Z	INFO	[db] Downloading DB...	repository="ghcr.io/aquasecurity/trivy-db:2"
│           53.80 MiB / 53.80 MiB [----------------------------------------------------------->] 100.00% ? p/s
│           ?53.80 MiB / 53.80 MiB [----------------------------------------------------------->] 100.00% ? p/s
│            ?53.80 MiB / 53.80 MiB [----------------------------------------------------------->] 100.00% ?
│           p/s ?53.80 MiB / 53.80 MiB [----------------------------------------------------------->] 100.00% ?
│            p/s ?53.80 MiB / 53.80 MiB [----------------------------------------------------------->] 100.00%
│           ? p/s ?53.80 MiB / 53.80 MiB [----------------------------------------------------------->] 100.00%
│            ? p/s ?53.80 MiB / 53.80 MiB [----------------------------------------------------------->]
│           100.00% ? p/s ?53.80 MiB / 53.80 MiB [----------------------------------------------------------->]
│            100.00% ? p/s ?53.80 MiB / 53.80 MiB [-------------------------------------------------] 100.00%
│           35.18 MiB p/s 1.7s2024-09-26T07:09:31Z	INFO	[vuln] Vulnerability scanning is enabled
│           2024-09-26T07:09:31Z	INFO	[secret] Secret scanning is enabled
│           2024-09-26T07:09:31Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2024-09-26T07:09:31Z	INFO	[secret] Please see also
│           https://aquasecurity.github.io/trivy/v0.55/docs/scanner/secret#recommendation for faster secret
│           detection
│           2024-09-26T07:09:33Z	INFO	Java DB Repository	repository=ghcr.io/aquasecurity/trivy-java-db:1
│           2024-09-26T07:09:33Z	INFO	Downloading the Java DB...
│           2024-09-26T07:09:33Z	FATAL	Fatal error	image scan error: scan error: scan failed: failed analysis:
│           analyze error: pipeline error: failed to analyze layer
│           (sha256:6f576c9eca0f8458e264e86a3a31395e22a545453dcb5e1dbbef910a56d7bea9): post analysis error:
│           post analysis error: Unable to initialize the Java DB: Java DB update failed: DB download error:
│           oci download error: failed to fetch the layer: GET
│           https://ghcr.io/v2/aquasecurity/trivy-java-db/blobs/sha256:d8b1857b4f65873ecf84d2c6ebae1004b475b480
│           e98425ef97121340c357f113: TOOMANYREQUESTS: retry-after: 324.159µs, allowed: 44000/minute 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/ojobrt:latest 
````
