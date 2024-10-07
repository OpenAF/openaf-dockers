````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           43c4264eed91: Already exists
│           958beee14847: Pulling fs layer
│           adc406921242: Pulling fs layer
│           e1d9543056a1: Pulling fs layer
│           e1d9543056a1: Verifying Checksum
│           e1d9543056a1: Download complete
│           958beee14847: Download complete
│           adc406921242: Verifying Checksum
│           adc406921242: Download complete
│           958beee14847: Pull complete
│           adc406921242: Pull complete
│           e1d9543056a1: Pull complete
│           Digest: sha256:c42bb3221509b0a9fa2291cd79a3a818b30a172ab87e9aac8a43997a5b56f293
│           Status: Downloaded newer image for aquasec/trivy:latest
│           2024-10-07T07:08:04Z	INFO	[vulndb] Need to update DB
│           2024-10-07T07:08:04Z	INFO	[vulndb] Downloading vulnerability DB...
│           2024-10-07T07:08:04Z	INFO	[vulndb] Downloading artifact...	repo="ghcr.io/aquasecurity/trivy-db:2"
│           54.04 MiB / 54.04 MiB [----------------------------------------------------------->] 100.00% ? p/s
│           ?54.04 MiB / 54.04 MiB [----------------------------------------------------------->] 100.00% ? p/s
│            ?54.04 MiB / 54.04 MiB [----------------------------------------------------------->] 100.00% ?
│           p/s ?54.04 MiB / 54.04 MiB [----------------------------------------------------------->] 100.00% ?
│            p/s ?54.04 MiB / 54.04 MiB [----------------------------------------------------------->] 100.00%
│           ? p/s ?54.04 MiB / 54.04 MiB [----------------------------------------------------------->] 100.00%
│            ? p/s ?54.04 MiB / 54.04 MiB [----------------------------------------------------------->]
│           100.00% ? p/s ?54.04 MiB / 54.04 MiB [----------------------------------------------------------->]
│            100.00% ? p/s ?54.04 MiB / 54.04 MiB [-------------------------------------------------] 100.00%
│           34.94 MiB p/s 1.7s2024-10-07T07:08:05Z	INFO	[vulndb] Artifact successfully
│           downloaded	repo="ghcr.io/aquasecurity/trivy-db:2"
│           2024-10-07T07:08:05Z	INFO	[vuln] Vulnerability scanning is enabled
│           2024-10-07T07:08:05Z	INFO	[secret] Secret scanning is enabled
│           2024-10-07T07:08:05Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2024-10-07T07:08:05Z	INFO	[secret] Please see also
│           https://aquasecurity.github.io/trivy/v0.56/docs/scanner/secret#recommendation for faster secret
│           detection
│           2024-10-07T07:08:09Z	INFO	[javadb] Downloading Java DB...
│           2024-10-07T07:08:09Z	INFO	[javadb] Downloading
│           artifact...	repo="ghcr.io/aquasecurity/trivy-java-db:1"
│           2024-10-07T07:08:09Z	ERROR	[javadb] Failed to download
│           artifact	repo="ghcr.io/aquasecurity/trivy-java-db:1" err="OCI repository error: 1 error
│           occurred:\n\t* GET https://ghcr.io/v2/aquasecurity/trivy-java-db/manifests/1: TOOMANYREQUESTS:
│           retry-after: 261.634µs, allowed: 44000/minute\n\n"
│           2024-10-07T07:08:09Z	FATAL	Fatal error	image scan error: scan error: scan failed: failed analysis:
│           analyze error: pipeline error: failed to analyze layer
│           (sha256:b770c899a9946be2dc865e80e3595740e2ffcd95079c7c60572df942c02002a8): post analysis error:
│           post analysis error: Unable to initialize the Java DB: Java DB update failed: OCI artifact error:
│           failed to download Java DB: failed to download artifact from any source 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm  aquasec/trivy -f json  image openaf/oaf:latest 
````
