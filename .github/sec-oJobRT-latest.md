````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:cad5cc4c273b98de4e84d19b481399fae19cd2ba09914239e9d0597fa227a8e4
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-11-15T03:11:42Z	INFO	[vulndb] Need to update DB
│           2024-11-15T03:11:42Z	INFO	[vulndb] Downloading vulnerability DB...
│           2024-11-15T03:11:42Z	INFO	[vulndb] Downloading artifact...	repo="ghcr.io/aquasecurity/trivy-db:2"
│           53.80 MiB / 55.50 MiB [----------------------------------------------------------->_] 96.93% ? p/s
│           ?55.50 MiB / 55.50 MiB [----------------------------------------------------------->] 100.00% ? p/s
│            ?55.50 MiB / 55.50 MiB [----------------------------------------------------------->] 100.00% ?
│           p/s ?55.50 MiB / 55.50 MiB [----------------------------------------------->] 100.00% 2.84 MiB p/s
│           ETA 0s55.50 MiB / 55.50 MiB [----------------------------------------------->] 100.00% 2.84 MiB p/s
│            ETA 0s55.50 MiB / 55.50 MiB [----------------------------------------------->] 100.00% 2.84 MiB
│           p/s ETA 0s55.50 MiB / 55.50 MiB [----------------------------------------------->] 100.00% 2.65 MiB
│            p/s ETA 0s55.50 MiB / 55.50 MiB [----------------------------------------------->] 100.00% 2.65
│           MiB p/s ETA 0s55.50 MiB / 55.50 MiB [----------------------------------------------->] 100.00% 2.65
│            MiB p/s ETA 0s55.50 MiB / 55.50 MiB [----------------------------------------------->] 100.00%
│           2.48 MiB p/s ETA 0s55.50 MiB / 55.50 MiB [-------------------------------------------------]
│           100.00% 28.95 MiB p/s 2.1s2024-11-15T03:11:45Z	INFO	[vulndb] Artifact successfully
│           downloaded	repo="ghcr.io/aquasecurity/trivy-db:2"
│           2024-11-15T03:11:45Z	INFO	[vuln] Vulnerability scanning is enabled
│           2024-11-15T03:11:45Z	INFO	[secret] Secret scanning is enabled
│           2024-11-15T03:11:45Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2024-11-15T03:11:45Z	INFO	[secret] Please see also
│           https://aquasecurity.github.io/trivy/v0.57/docs/scanner/secret#recommendation for faster secret
│           detection
│           2024-11-15T03:11:46Z	INFO	[javadb] Downloading Java DB...
│           2024-11-15T03:11:46Z	INFO	[javadb] Downloading
│           artifact...	repo="ghcr.io/aquasecurity/trivy-java-db:1"
│           2024-11-15T03:11:46Z	ERROR	[javadb] Failed to download
│           artifact	repo="ghcr.io/aquasecurity/trivy-java-db:1" err="oci download error: failed to fetch the
│           layer: GET
│           https://ghcr.io/v2/aquasecurity/trivy-java-db/blobs/sha256:23bb77a4dc57525c1ec7eaadc67eb09483e19b6d
│           4025075410cc876ab68954b3: TOOMANYREQUESTS: retry-after: 587.046µs, allowed: 44000/minute"
│           2024-11-15T03:11:46Z	FATAL	Fatal error	image scan error: scan error: scan failed: failed analysis:
│           analyze error: pipeline error: failed to analyze layer
│           (sha256:4b9767b3f4d165c26954b69d03df40a009bb74ac2b3e0da7da39f7f843d0eb76): post analysis error:
│           post analysis error: Unable to initialize the Java DB: Java DB update failed: OCI artifact error:
│           failed to download Java DB: failed to download artifact from any source: 1 error occurred:
│           	* oci download error: failed to fetch the layer: GET
│           4025075410cc876ab68954b3: TOOMANYREQUESTS: retry-after: 587.046µs, allowed: 44000/minute
│            
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm -v trivy-db:/root/.cache/trivy aquasec/trivy -f json  image
            openaf/ojobrt:latest 
````
