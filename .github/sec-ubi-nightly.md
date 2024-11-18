````yaml
╭ stdout   
├ stderr  : latest: Pulling from aquasec/trivy
│           Digest: sha256:cad5cc4c273b98de4e84d19b481399fae19cd2ba09914239e9d0597fa227a8e4
│           Status: Image is up to date for aquasec/trivy:latest
│           2024-11-18T07:09:47Z	INFO	[vuln] Vulnerability scanning is enabled
│           2024-11-18T07:09:47Z	INFO	[secret] Secret scanning is enabled
│           2024-11-18T07:09:47Z	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to
│           disable secret scanning
│           2024-11-18T07:09:47Z	INFO	[secret] Please see also
│           https://aquasecurity.github.io/trivy/v0.57/docs/scanner/secret#recommendation for faster secret
│           detection
│           2024-11-18T07:09:57Z	INFO	Detected OS	family="redhat" version="9.5"
│           2024-11-18T07:09:57Z	INFO	[redhat] Detecting RHEL/CentOS vulnerabilities...	os_version="9"
│           pkg_num=145
│           2024-11-18T07:09:57Z	FATAL	Fatal error	image scan error: scan error: scan failed: scan failed:
│           failed to detect vulnerabilities: unable to scan OS packages: failed vulnerability detection of OS
│           packages: failed detection: redhat vulnerability detection error: failed to get Red Hat advisories:
│            unable to find CPE indices. See https://github.com/aquasecurity/trivy-db/issues/435 for details 
├ exitcode: 1 
╰ cmd     : docker run --pull always --rm -v trivy-db:/root/.cache/trivy aquasec/trivy -f json  image
            openaf/oaf:ubi-nightly 
````
