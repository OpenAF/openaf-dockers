````yaml
╭ stdout   
├ stderr  : [vuln] Vulnerability scanning is enabled
│           2025-10-20T07:25:40Z	INFO	[secret] Secret scanning is enabled
│           2025-10-20T07:25:40Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2025-10-20T07:25:40Z	INFO	[secret] Please see
│           https://trivy.dev/v0.67/docs/scanner/secret#recommendation for faster secret detection
│           2025-10-20T07:27:11Z	FATAL	Fatal error	run error: image scan error: scan error: unable to
│           initialize a scan service: unable to initialize artifact: unable to initialize container image:
│           unable to find the specified image "openaf/pyoaf:nightly" in ["docker" "containerd" "podman"
│           "remote"] 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm -v trivy-db:/root/.cache/trivy aquasec/trivy -f json  image
            openaf/pyoaf:nightly 
````
