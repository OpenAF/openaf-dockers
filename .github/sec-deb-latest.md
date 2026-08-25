```yaml
╭ [0] ╭ Target         : openaf/oaf:deb (ubuntu 26.04) 
│     ├ Class          : os-pkgs 
│     ├ Type           : ubuntu 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : bsdutils@1:2.41.3-3ubuntu2 
│                       │      ├ PkgName         : bsdutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/bsdutils@2.41.3-3ubuntu2?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : fce02d7573b26c2e 
│                       │      ├ InstalledVersion: 1:2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:14e1aaca3f148e92eb9c4b6a7dcb791e37af38ce80e5e4f421fdc
│                       │      │                   19047c895e9 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-59 
│                       │      │                  CWE-269
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-27456 
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-27456        
│                       │      │                  https://github.com/bottlerocket-os/bottlerocket-core-kit/blob
│                       │      │                  /develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.toml            
│                       │      │                  https://github.com/util-linux/util-linux/commit/5e390467b26a3
│                       │      │                  cf3fecc04e1a0d482dff3162fc4                                  
│                       │      │                  https://github.com/util-linux/util-linux/releases/tag/v2.41.4
│                       │      │                                                                               
│                       │      │                  https://github.com/util-linux/util-linux/security/advisories/
│                       │      │                  GHSA-qq4x-vfq4-9h9g                                          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-07-24T22:10:00.14Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : bsdutils@1:2.41.3-3ubuntu2 
│                       │      ├ PkgName         : bsdutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/bsdutils@2.41.3-3ubuntu2?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : fce02d7573b26c2e 
│                       │      ├ InstalledVersion: 1:2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ae4858bafead5b5311c1a6e9ee3e5369353acf6117f4c948c1132
│                       │      │                   facb1d5b001 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-289
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                           
│                       │      │                  ────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:7180     
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-3184
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-3184      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-3184      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-08-21T13:17:47.457Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-11856 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.3 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.3?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2c5a5f1d985455f6 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.3 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.4 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-11856 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c7cb06810752a6f4f62f74262fe89c48419e2aaa9114325993f3b
│                       │      │                   5e52529d041 
│                       │      ├ Title           : curl: curl: Information disclosure via incorrect Digest
│                       │      │                   authentication header reuse 
│                       │      ├ Description     : Successfully using libcurl to do a transfer to a specific
│                       │      │                   HTTP origin
│                       │      │                   (`hostA`) with **Digest** authentication and then changing
│                       │      │                   the origin to a
│                       │      │                   different one (`hostB`) for a second transfer, reusing the
│                       │      │                   same handle, makes
│                       │      │                   libcurl wrongly pass on the  `Authorization:` header field
│                       │      │                   meant for `hostA`,
│                       │      │                   to `hostB`. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-294
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 4 
│                       │      │                  ├ photon: 4 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 9.8 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-11856
│                       │      │                  https://curl.se/L7HzKXisfJ/CVE-2026-11856.md         
│                       │      │                  https://curl.se/docs/CVE-2026-11856.html             
│                       │      │                  https://curl.se/docs/CVE-2026-11856.json             
│                       │      │                  https://github.com/advisories/GHSA-9crq-qh8v-6xmm    
│                       │      │                  https://hackerone.com/reports/3793260                
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-11856      
│                       │      │                  https://ubuntu.com/security/notices/USN-8651-1       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-11856      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-03T07:16:23.973Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T19:43:55.6Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-54371 
│                       │      ├ PkgID           : libattr1@1:2.5.2-4 
│                       │      ├ PkgName         : libattr1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libattr1@2.5.2-4?arch=amd64&distro=ubu
│                       │      │                  │       ntu-26.04&epoch=1 
│                       │      │                  ╰ UID : 7316bbc1a7f10b3f 
│                       │      ├ InstalledVersion: 1:2.5.2-4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54371 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:253c8d8fa28dc1b342869e7b81c84d4bc2482c442fb2b48dc7033
│                       │      │                   6719661d1e9 
│                       │      ├ Title           : attr: attr: Symlink Traversal Privilege Escalation via
│                       │      │                   getfattr and setfattr 
│                       │      ├ Description     : attr before version 2.6.0 contains a symlink traversal
│                       │      │                   vulnerability in the getfattr and setfattr utilities that
│                       │      │                   allows local attackers to escalate privileges by replacing a
│                       │      │                    pathname component with a symbolic link during directory
│                       │      │                   hierarchy traversal. Attackers who control a pathname
│                       │      │                   component can redirect getfattr and setfattr operations to
│                       │      │                   arbitrary files by substituting a symlink, leading to local
│                       │      │                   privilege escalation when getfattr or setfattr is invoked by
│                       │      │                    a privileged process over an attacker-controlled path. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                 
│                       │      │                  ──────
│                       │      │                  CWE-59
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.3 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:34889             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:56133             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-54371        
│                       │      │                  https://bugzilla.redhat.com/2490283                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2490283          
│                       │      │                  https://cgit.git.savannah.nongnu.org/cgit/attr.git/commit/?id
│                       │      │                  =49f79e947270f06940b9100fa638f85dddc4aa7f                    
│                       │      │                  https://cgit.git.savannah.nongnu.org/cgit/attr.git/commit/?id
│                       │      │                  =c440855d6b33446edf4b5eb1a2d892281f15a99b                    
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-54371
│                       │      │                                                                               
│                       │      │                  https://errata.almalinux.org/8/ALSA-2026-56133.html          
│                       │      │                                                                               
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:56133                
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-54371.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-56133.html         
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-54371              
│                       │      │                                                                               
│                       │      │                  https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-
│                       │      │                  2026-54371.json                                              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-54371              
│                       │      │                                                                               
│                       │      │                  https://www.openwall.com/lists/oss-security/2026/06/29/1     
│                       │      │                                                                               
│                       │      │                  https://www.vulncheck.com/advisories/attr-symlink-traversal-p
│                       │      │                  rivilege-escalation-via-getfattr-setfattr                    
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-29T14:16:57.823Z 
│                       │      ╰ LastModifiedDate: 2026-08-24T13:19:12.583Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : libblkid1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libblkid1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libblkid1@2.41.3-3ubuntu2?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : cfada1ce2d53117c 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:8e36832dd6a7375bfb5ce05ee0825787fadfd33fcb5c4b420324f
│                       │      │                   026aefad037 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-59 
│                       │      │                  CWE-269
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-27456 
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-27456        
│                       │      │                  https://github.com/bottlerocket-os/bottlerocket-core-kit/blob
│                       │      │                  /develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.toml            
│                       │      │                  https://github.com/util-linux/util-linux/commit/5e390467b26a3
│                       │      │                  cf3fecc04e1a0d482dff3162fc4                                  
│                       │      │                  https://github.com/util-linux/util-linux/releases/tag/v2.41.4
│                       │      │                                                                               
│                       │      │                  https://github.com/util-linux/util-linux/security/advisories/
│                       │      │                  GHSA-qq4x-vfq4-9h9g                                          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-07-24T22:10:00.14Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : libblkid1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libblkid1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libblkid1@2.41.3-3ubuntu2?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : cfada1ce2d53117c 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:bb672f05866ab3ecea100fa8e8e27c4874c2374e16dda8cfd0130
│                       │      │                   bb3b7ea3270 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-289
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                           
│                       │      │                  ────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:7180     
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-3184
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-3184      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-3184      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-08-21T13:17:47.457Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-11856 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.3 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : cb8d80bd61f0ce19 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.3 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.4 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-11856 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:50f7cc07bed6e5d24007afc95d0282d8175399aabcfee67525e52
│                       │      │                   f0798bc00b1 
│                       │      ├ Title           : curl: curl: Information disclosure via incorrect Digest
│                       │      │                   authentication header reuse 
│                       │      ├ Description     : Successfully using libcurl to do a transfer to a specific
│                       │      │                   HTTP origin
│                       │      │                   (`hostA`) with **Digest** authentication and then changing
│                       │      │                   the origin to a
│                       │      │                   different one (`hostB`) for a second transfer, reusing the
│                       │      │                   same handle, makes
│                       │      │                   libcurl wrongly pass on the  `Authorization:` header field
│                       │      │                   meant for `hostA`,
│                       │      │                   to `hostB`. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-294
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 4 
│                       │      │                  ├ photon: 4 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 9.8 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-11856
│                       │      │                  https://curl.se/L7HzKXisfJ/CVE-2026-11856.md         
│                       │      │                  https://curl.se/docs/CVE-2026-11856.html             
│                       │      │                  https://curl.se/docs/CVE-2026-11856.json             
│                       │      │                  https://github.com/advisories/GHSA-9crq-qh8v-6xmm    
│                       │      │                  https://hackerone.com/reports/3793260                
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-11856      
│                       │      │                  https://ubuntu.com/security/notices/USN-8651-1       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-11856      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-03T07:16:23.973Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T19:43:55.6Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2025-66382 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-66382 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:34e5fa945792bb42ea58ff66aa8e8c9bfe2243dfa2cf56de0717a
│                       │      │                   9952ed754e3 
│                       │      ├ Title           : libexpat: libexpat: Denial of service via crafted file
│                       │      │                   processing 
│                       │      ├ Description     : In libexpat through 2.7.3, a crafted file with an
│                       │      │                   approximate size of 2 MiB can lead to dozens of seconds of
│                       │      │                   processing time. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-407
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 2.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2025/12/02/1      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2025-66382        
│                       │      │                  https://cert-portal.siemens.com/productcert/html/ssa-082556.h
│                       │      │                  tml                                                          
│                       │      │                  https://cert-portal.siemens.com/productcert/html/ssa-253495.h
│                       │      │                  tml                                                          
│                       │      │                  https://github.com/libexpat/libexpat/issues/1076             
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2025-66382              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2025-66382              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2025-11-28T07:15:57.9Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T09:56:45.24Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2024-2236 
│                       │      ├ PkgID           : libgcrypt20@1.12.0-2ubuntu1 
│                       │      ├ PkgName         : libgcrypt20 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgcrypt20@1.12.0-2ubuntu1?arch=amd64
│                       │      │                  │       &distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 45e5e1ad6adb0acd 
│                       │      ├ InstalledVersion: 1.12.0-2ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-2236 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:51faa51d54ad93a0b60aa0d60cc12ff0a82fb56add44f48fa2f55
│                       │      │                   d5c91b86666 
│                       │      ├ Title           : libgcrypt: vulnerable to Marvin Attack 
│                       │      ├ Description     : A timing-based side-channel flaw was found in libgcrypt's
│                       │      │                   RSA implementation. This issue may allow a remote attacker
│                       │      │                   to initiate a Bleichenbacher-style attack, which can lead to
│                       │      │                    the decryption of RSA ciphertexts. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-385
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2024:9404              
│                       │      │                  https://access.redhat.com/errata/RHSA-2025:3530              
│                       │      │                  https://access.redhat.com/errata/RHSA-2025:3534              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2024-2236         
│                       │      │                  https://bugzilla.redhat.com/2245218                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2245218          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2268268          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2236 
│                       │      │                  https://dev.gnupg.org/T7136                                  
│                       │      │                  https://errata.almalinux.org/9/ALSA-2024-9404.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2024:9404                 
│                       │      │                  https://github.com/tomato42/marvin-toolkit/tree/master/exampl
│                       │      │                  e/libgcrypt                                                  
│                       │      │                  https://gitlab.com/redhat-crypto/libgcrypt/libgcrypt-mirror/-
│                       │      │                  /merge_requests/17                                           
│                       │      │                  https://linux.oracle.com/cve/CVE-2024-2236.html              
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2024-9404.html          
│                       │      │                                                                               
│                       │      │                  https://lists.gnupg.org/pipermail/gcrypt-devel/2024-March/005
│                       │      │                  607.html                                                     
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2024-2236               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2024-2236               
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2024-03-06T22:15:57.977Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T07:24:06.083Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : libmount1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libmount1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libmount1@2.41.3-3ubuntu2?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : ec572950b070797 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:caf0578aea1fba081b81bb0618f68d56b9e07fac185621627a130
│                       │      │                   ab2e5c38342 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-59 
│                       │      │                  CWE-269
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-27456 
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-27456        
│                       │      │                  https://github.com/bottlerocket-os/bottlerocket-core-kit/blob
│                       │      │                  /develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.toml            
│                       │      │                  https://github.com/util-linux/util-linux/commit/5e390467b26a3
│                       │      │                  cf3fecc04e1a0d482dff3162fc4                                  
│                       │      │                  https://github.com/util-linux/util-linux/releases/tag/v2.41.4
│                       │      │                                                                               
│                       │      │                  https://github.com/util-linux/util-linux/security/advisories/
│                       │      │                  GHSA-qq4x-vfq4-9h9g                                          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-07-24T22:10:00.14Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : libmount1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libmount1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libmount1@2.41.3-3ubuntu2?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : ec572950b070797 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:1dd021fb0a8d2901dbf394be622f7347c67d76f44101b017d9256
│                       │      │                   3653c1f46e7 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-289
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                           
│                       │      │                  ────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:7180     
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-3184
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-3184      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-3184      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-08-21T13:17:47.457Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-13757 
│                       │      ├ PkgID           : libp11-kit0@0.26.2-2 
│                       │      ├ PkgName         : libp11-kit0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libp11-kit0@0.26.2-2?arch=amd64&distro
│                       │      │                  │       =ubuntu-26.04 
│                       │      │                  ╰ UID : 38d0559292d79a63 
│                       │      ├ InstalledVersion: 0.26.2-2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13757 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e16c6767ef4720ca50942c5efc0a71049419555dfe27a74b7c040
│                       │      │                   ccf6e24d2c3 
│                       │      ├ Title           : p11-kit: Stack exhaustion via unbounded recursion in RPC
│                       │      │                   attribute parsing 
│                       │      ├ Description     : A flaw was found in p11-kit. The RPC message attribute
│                       │      │                   parsing functions p11_rpc_message_get_attribute() and
│                       │      │                   p11_rpc_message_get_attribute_array_value() form a
│                       │      │                   mutually-recursive call chain with no recursion depth limit
│                       │      │                   when processing nested CKA_WRAP_TEMPLATE,
│                       │      │                   CKA_UNWRAP_TEMPLATE, and CKA_DERIVE_TEMPLATE attributes. An
│                       │      │                   unauthenticated attacker with local access to the p11-kit
│                       │      │                   RPC Unix domain socket can send a specially crafted request
│                       │      │                   with deeply nested template attributes, causing stack
│                       │      │                   exhaustion and crashing the p11-kit server process and its
│                       │      │                   dependent services. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-674
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:37469             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:38342             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:49667             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:49668             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:53371             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:54387             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:54760             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-13757        
│                       │      │                  https://bugzilla.redhat.com/2494556                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2494556          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-13757
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-49667.html          
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:49667                
│                       │      │                  https://github.com/advisories/GHSA-p2wm-69qx-x25w            
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-13757.html             
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-49668.html         
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-13757              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-13757              
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-29T19:16:40.907Z 
│                       │      ╰ LastModifiedDate: 2026-08-21T13:16:51.2Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : libsmartcols1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libsmartcols1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsmartcols1@2.41.3-3ubuntu2?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : eb8f24163bcc7b6b 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ce8133e4cfe1175dea8a773b57c8e4e595e0420b8d35ea30017dd
│                       │      │                   8d700ab400d 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-59 
│                       │      │                  CWE-269
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-27456 
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-27456        
│                       │      │                  https://github.com/bottlerocket-os/bottlerocket-core-kit/blob
│                       │      │                  /develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.toml            
│                       │      │                  https://github.com/util-linux/util-linux/commit/5e390467b26a3
│                       │      │                  cf3fecc04e1a0d482dff3162fc4                                  
│                       │      │                  https://github.com/util-linux/util-linux/releases/tag/v2.41.4
│                       │      │                                                                               
│                       │      │                  https://github.com/util-linux/util-linux/security/advisories/
│                       │      │                  GHSA-qq4x-vfq4-9h9g                                          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-07-24T22:10:00.14Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : libsmartcols1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libsmartcols1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsmartcols1@2.41.3-3ubuntu2?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : eb8f24163bcc7b6b 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:54f5d2cbbd8c033649ae8dffe386576ddf569c6414589615b4e79
│                       │      │                   c3c5d0e9cf9 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-289
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                           
│                       │      │                  ────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:7180     
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-3184
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-3184      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-3184      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-08-21T13:17:47.457Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-15059 
│                       │      ├ PkgID           : libsystemd0@259.5-0ubuntu3 
│                       │      ├ PkgName         : libsystemd0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsystemd0@259.5-0ubuntu3?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c2c6a8cc93da771f 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3 
│                       │      ├ FixedVersion    : 259.5-0ubuntu3.4 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-15059 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:478fe4adf5ace9b6c11c2aea238ba4bf366674d194147f0cc444e
│                       │      │                   1ac85945adb 
│                       │      ├ Title           : Local unprivileged users can terminate arbitrary local
│                       │      │                   processes via a ... 
│                       │      ├ Description     : Local unprivileged users can terminate arbitrary local
│                       │      │                   processes via a systemd-oomd IPC API due to a missing path
│                       │      │                   traversal validation. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                 
│                       │      │                  ──────
│                       │      │                  CWE-22
│                       │      │                  CWE-59
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/systemd/systemd/security/advisories/GHSA-6
│                       │      │                  52q-wxr6-h5j6                                                
│                       │      │                  https://ubuntu.com/security/notices/USN-8626-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-15059              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-10T14:17:20.76Z 
│                       │      ╰ LastModifiedDate: 2026-08-10T18:17:40.983Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-15060 
│                       │      ├ PkgID           : libsystemd0@259.5-0ubuntu3 
│                       │      ├ PkgName         : libsystemd0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsystemd0@259.5-0ubuntu3?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c2c6a8cc93da771f 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3 
│                       │      ├ FixedVersion    : 259.5-0ubuntu3.4 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-15060 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:58130818daa39ea2e1496af90e537cadc236abcc80cfa4c7ab7d1
│                       │      │                   fb6f59293c7 
│                       │      ├ Title           : When systemd-machined >= v259 (or v258 with a custom
│                       │      │                   `polkit` policy t ... 
│                       │      ├ Description     : When systemd-machined >= v259 (or v258 with a custom
│                       │      │                   `polkit` policy that allows `register-machine` access) is
│                       │      │                   running on a desktop system, an unprivileged user logged in
│                       │      │                   a desktop graphical session can kill arbitrary processes,
│                       │      │                   even privileged ones.
│                       │      │                   
│                       │      │                   - versions older than v259 are not affected, unless
│                       │      │                   unprivileged access is granted for the `register-machine`
│                       │      │                   polkit action via a local, custom policy config file
│                       │      │                   - versions older than v258 are not affected
│                       │      │                   - unrelated to the systemd service manager (pid 1 or user
│                       │      │                   session managers)
│                       │      │                   - systemd-machined is not typically installed by default,
│                       │      │                   and is typically in an optional, separate package (e.g.:
│                       │      │                   systemd-container)
│                       │      │                   - terminal-only or remote sessions (e.g.: ssh) are not
│                       │      │                   affected 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                                                           
│                       │      │                  ────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:33155
│                       │      │                  CWE-862                                         
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/systemd/systemd/security/advisories/GHSA-q
│                       │      │                  wv4-3gwc-w5g8                                                
│                       │      │                  https://ubuntu.com/security/notices/USN-8626-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-15060              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-10T14:17:21.13Z 
│                       │      ╰ LastModifiedDate: 2026-08-10T18:17:41.087Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-16742 
│                       │      ├ PkgID           : libsystemd0@259.5-0ubuntu3 
│                       │      ├ PkgName         : libsystemd0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsystemd0@259.5-0ubuntu3?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c2c6a8cc93da771f 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3 
│                       │      ├ FixedVersion    : 259.5-0ubuntu3.4 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-16742 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:84441b21e2e68316e49981e5386b6ae3dbeb174474f0f5bf2c59d
│                       │      │                   63ee310bfd1 
│                       │      ├ Title           : systemd-homed contains a local privilege escalation bug via
│                       │      │                   arbitrary  ... 
│                       │      ├ Description     : systemd-homed contains a local privilege escalation bug via
│                       │      │                   arbitrary system group addition to a local, logged in,
│                       │      │                   homed-managed user 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-269
│                       │      │                  CWE-347
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/systemd/systemd/security/advisories/GHSA-j
│                       │      │                  m29-p7hh-vjhv                                                
│                       │      │                  https://ubuntu.com/security/notices/USN-8626-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-16742              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-10T14:17:21.277Z 
│                       │      ╰ LastModifiedDate: 2026-08-10T16:19:29.157Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libsystemd0@259.5-0ubuntu3 
│                       │      ├ PkgName         : libsystemd0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsystemd0@259.5-0ubuntu3?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c2c6a8cc93da771f 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:23e0f887cb500ec01b882a6a6d8d0d0cd19ef64987f44c4d4a276
│                       │      │                   56e136d98cd 
│                       │      ├ Title           : systemd: systemd-journald: Unintended output to user
│                       │      │                   terminals via logger command 
│                       │      ├ Description     : In systemd 259, systemd-journald can send ANSI escape
│                       │      │                   sequences to the terminals of arbitrary users when a "logger
│                       │      │                    -p emerg" command is executed, if ForwardToWall=yes is
│                       │      │                   set. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-669
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ nvd   : 1 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 3.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 2.9 
│                       │      ├ References                                                               
│                       │      │                  ────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/05/05/1 
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-40228   
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-40228         
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-40228         
│                       │      │                  https://www.openwall.com/lists/oss-security/2026/04/08/1
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-10T16:16:33.753Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:44:53.31Z 
│                       ├ [18] ╭ VulnerabilityID : CVE-2026-15059 
│                       │      ├ PkgID           : libudev1@259.5-0ubuntu3 
│                       │      ├ PkgName         : libudev1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libudev1@259.5-0ubuntu3?arch=amd64&dis
│                       │      │                  │       tro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2ce94cee56148901 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3 
│                       │      ├ FixedVersion    : 259.5-0ubuntu3.4 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-15059 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a4b1d243d5d18fb9980edd7c26c5d00431ba3102ce55864746eb1
│                       │      │                   2a19478731a 
│                       │      ├ Title           : Local unprivileged users can terminate arbitrary local
│                       │      │                   processes via a ... 
│                       │      ├ Description     : Local unprivileged users can terminate arbitrary local
│                       │      │                   processes via a systemd-oomd IPC API due to a missing path
│                       │      │                   traversal validation. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                 
│                       │      │                  ──────
│                       │      │                  CWE-22
│                       │      │                  CWE-59
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/systemd/systemd/security/advisories/GHSA-6
│                       │      │                  52q-wxr6-h5j6                                                
│                       │      │                  https://ubuntu.com/security/notices/USN-8626-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-15059              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-10T14:17:20.76Z 
│                       │      ╰ LastModifiedDate: 2026-08-10T18:17:40.983Z 
│                       ├ [19] ╭ VulnerabilityID : CVE-2026-15060 
│                       │      ├ PkgID           : libudev1@259.5-0ubuntu3 
│                       │      ├ PkgName         : libudev1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libudev1@259.5-0ubuntu3?arch=amd64&dis
│                       │      │                  │       tro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2ce94cee56148901 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3 
│                       │      ├ FixedVersion    : 259.5-0ubuntu3.4 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-15060 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:bc00bd90e66e0a4e4a957544a9349b259dbf6db15239446b2863c
│                       │      │                   087e605a334 
│                       │      ├ Title           : When systemd-machined >= v259 (or v258 with a custom
│                       │      │                   `polkit` policy t ... 
│                       │      ├ Description     : When systemd-machined >= v259 (or v258 with a custom
│                       │      │                   `polkit` policy that allows `register-machine` access) is
│                       │      │                   running on a desktop system, an unprivileged user logged in
│                       │      │                   a desktop graphical session can kill arbitrary processes,
│                       │      │                   even privileged ones.
│                       │      │                   
│                       │      │                   - versions older than v259 are not affected, unless
│                       │      │                   unprivileged access is granted for the `register-machine`
│                       │      │                   polkit action via a local, custom policy config file
│                       │      │                   - versions older than v258 are not affected
│                       │      │                   - unrelated to the systemd service manager (pid 1 or user
│                       │      │                   session managers)
│                       │      │                   - systemd-machined is not typically installed by default,
│                       │      │                   and is typically in an optional, separate package (e.g.:
│                       │      │                   systemd-container)
│                       │      │                   - terminal-only or remote sessions (e.g.: ssh) are not
│                       │      │                   affected 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  CWE-862
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/systemd/systemd/security/advisories/GHSA-q
│                       │      │                  wv4-3gwc-w5g8                                                
│                       │      │                  https://ubuntu.com/security/notices/USN-8626-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-15060              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-10T14:17:21.13Z 
│                       │      ╰ LastModifiedDate: 2026-08-10T18:17:41.087Z 
│                       ├ [20] ╭ VulnerabilityID : CVE-2026-16742 
│                       │      ├ PkgID           : libudev1@259.5-0ubuntu3 
│                       │      ├ PkgName         : libudev1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libudev1@259.5-0ubuntu3?arch=amd64&dis
│                       │      │                  │       tro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2ce94cee56148901 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3 
│                       │      ├ FixedVersion    : 259.5-0ubuntu3.4 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-16742 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e8c56b2511e4197784990f802c9c722c993298c26b3b3dab4a14f
│                       │      │                   a96cbbad5a7 
│                       │      ├ Title           : systemd-homed contains a local privilege escalation bug via
│                       │      │                   arbitrary  ... 
│                       │      ├ Description     : systemd-homed contains a local privilege escalation bug via
│                       │      │                   arbitrary system group addition to a local, logged in,
│                       │      │                   homed-managed user 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-269
│                       │      │                  CWE-347
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/systemd/systemd/security/advisories/GHSA-j
│                       │      │                  m29-p7hh-vjhv                                                
│                       │      │                  https://ubuntu.com/security/notices/USN-8626-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-16742              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-10T14:17:21.277Z 
│                       │      ╰ LastModifiedDate: 2026-08-10T16:19:29.157Z 
│                       ├ [21] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libudev1@259.5-0ubuntu3 
│                       │      ├ PkgName         : libudev1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libudev1@259.5-0ubuntu3?arch=amd64&dis
│                       │      │                  │       tro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2ce94cee56148901 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:15925e442d2be0fd3cf60ae8bd575ec7d4286cb7eff85a27748a6
│                       │      │                   47d452eb2dc 
│                       │      ├ Title           : systemd: systemd-journald: Unintended output to user
│                       │      │                   terminals via logger command 
│                       │      ├ Description     : In systemd 259, systemd-journald can send ANSI escape
│                       │      │                   sequences to the terminals of arbitrary users when a "logger
│                       │      │                    -p emerg" command is executed, if ForwardToWall=yes is
│                       │      │                   set. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-669
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ nvd   : 1 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 3.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 2.9 
│                       │      ├ References                                                               
│                       │      │                  ────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/05/05/1 
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-40228   
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-40228         
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-40228         
│                       │      │                  https://www.openwall.com/lists/oss-security/2026/04/08/1
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-10T16:16:33.753Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:44:53.31Z 
│                       ├ [22] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : libuuid1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libuuid1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libuuid1@2.41.3-3ubuntu2?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04 
│                       │      │                  ╰ UID : 927585f152fe989a 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:83babd88096d8c0c188dcc920b525829a5391a744435d460ef49e
│                       │      │                   b21688d9d2f 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-59 
│                       │      │                  CWE-269
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-27456 
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-27456        
│                       │      │                  https://github.com/bottlerocket-os/bottlerocket-core-kit/blob
│                       │      │                  /develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.toml            
│                       │      │                  https://github.com/util-linux/util-linux/commit/5e390467b26a3
│                       │      │                  cf3fecc04e1a0d482dff3162fc4                                  
│                       │      │                  https://github.com/util-linux/util-linux/releases/tag/v2.41.4
│                       │      │                                                                               
│                       │      │                  https://github.com/util-linux/util-linux/security/advisories/
│                       │      │                  GHSA-qq4x-vfq4-9h9g                                          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-07-24T22:10:00.14Z 
│                       ├ [23] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : libuuid1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libuuid1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libuuid1@2.41.3-3ubuntu2?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04 
│                       │      │                  ╰ UID : 927585f152fe989a 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d8cd7b428bab2e1e911f070072b0ad0963e924e22ca62756b62ba
│                       │      │                   334361c7da2 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-289
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                           
│                       │      │                  ────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:7180     
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-3184
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-3184      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-3184      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-08-21T13:17:47.457Z 
│                       ├ [24] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : login@1:4.16.0-2+really2.41.3-3ubuntu2 
│                       │      ├ PkgName         : login 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login@4.16.0-2%2Breally2.41.3-3ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : 591feb53ee99f4f9 
│                       │      ├ InstalledVersion: 1:4.16.0-2+really2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:68156348a08097837077bb32fd8e0a03d1601e7ba7b213fa1a8da
│                       │      │                   4e261178968 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-59 
│                       │      │                  CWE-269
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-27456 
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-27456        
│                       │      │                  https://github.com/bottlerocket-os/bottlerocket-core-kit/blob
│                       │      │                  /develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.toml            
│                       │      │                  https://github.com/util-linux/util-linux/commit/5e390467b26a3
│                       │      │                  cf3fecc04e1a0d482dff3162fc4                                  
│                       │      │                  https://github.com/util-linux/util-linux/releases/tag/v2.41.4
│                       │      │                                                                               
│                       │      │                  https://github.com/util-linux/util-linux/security/advisories/
│                       │      │                  GHSA-qq4x-vfq4-9h9g                                          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-07-24T22:10:00.14Z 
│                       ├ [25] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : login@1:4.16.0-2+really2.41.3-3ubuntu2 
│                       │      ├ PkgName         : login 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login@4.16.0-2%2Breally2.41.3-3ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : 591feb53ee99f4f9 
│                       │      ├ InstalledVersion: 1:4.16.0-2+really2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6166b88d91bab99ebd2db415245651060dee5dea488a0f2b9bf55
│                       │      │                   47303f55c20 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-289
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                           
│                       │      │                  ────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:7180     
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-3184
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-3184      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-3184      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-08-21T13:17:47.457Z 
│                       ├ [26] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : login.defs@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : login.defs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login.defs@4.17.4-2ubuntu3?arch=all&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : eaf648d5e4e975f7 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:dc4569d85e64c0afef2f42a773cbf846444db01ebdee1fb4fdc6c
│                       │      │                   cf5c9a13740 
│                       │      ├ Title           : shadow-utils: Default subordinate ID configuration in
│                       │      │                   /etc/login.defs could lead to compromise 
│                       │      ├ Description     : shadow-utils (aka shadow) 4.4 through 4.17.0 establishes a
│                       │      │                   default /etc/subuid behavior (e.g., uid 100000 through
│                       │      │                   165535 for the first user account) that can realistically
│                       │      │                   conflict with the uids of users defined on locally
│                       │      │                   administered networks, potentially leading to account
│                       │      │                   takeover, e.g., by leveraging newuidmap for access to an NFS
│                       │      │                    home directory (or same-host resources in the case of
│                       │      │                   remote logins by these local network users). NOTE: it may
│                       │      │                   also be argued that system administrators should not have
│                       │      │                   assigned uids, within local networks, that are within the
│                       │      │                   range that can occur in /etc/subuid. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                   
│                       │      │                  ────────
│                       │      │                  CWE-1188
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 1 
│                       │      │                  ├ azure      : 1 
│                       │      │                  ├ oracle-oval: 1 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.6 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2025:20559             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2024-56433        
│                       │      │                  https://bugzilla.redhat.com/2334165                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2334165          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-56433
│                       │      │                  https://errata.almalinux.org/9/ALSA-2025-20559.html          
│                       │      │                  https://errata.rockylinux.org/RLSA-2025:20559                
│                       │      │                  https://github.com/shadow-maint/shadow/blob/e2512d5741d4a44bd
│                       │      │                  d81a8c2d0029b6222728cf0/etc/login.defs#L238-L241             
│                       │      │                  https://github.com/shadow-maint/shadow/issues/1157           
│                       │      │                                                                               
│                       │      │                  https://github.com/shadow-maint/shadow/releases/tag/4.4      
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/cve/CVE-2024-56433.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2025-20559-0.html       
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2024-56433              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2024-56433              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2024-12-26T09:15:07.267Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T08:12:10.903Z 
│                       ├ [27] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : mount@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : mount 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/mount@2.41.3-3ubuntu2?arch=amd64&distr
│                       │      │                  │       o=ubuntu-26.04 
│                       │      │                  ╰ UID : 98c6a5d7e9e110eb 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:dc30d3a1bae850c53029bfebb43390810bd71bda0f537c3a9b01a
│                       │      │                   701959498a1 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-59 
│                       │      │                  CWE-269
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-27456 
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-27456        
│                       │      │                  https://github.com/bottlerocket-os/bottlerocket-core-kit/blob
│                       │      │                  /develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.toml            
│                       │      │                  https://github.com/util-linux/util-linux/commit/5e390467b26a3
│                       │      │                  cf3fecc04e1a0d482dff3162fc4                                  
│                       │      │                  https://github.com/util-linux/util-linux/releases/tag/v2.41.4
│                       │      │                                                                               
│                       │      │                  https://github.com/util-linux/util-linux/security/advisories/
│                       │      │                  GHSA-qq4x-vfq4-9h9g                                          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-07-24T22:10:00.14Z 
│                       ├ [28] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : mount@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : mount 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/mount@2.41.3-3ubuntu2?arch=amd64&distr
│                       │      │                  │       o=ubuntu-26.04 
│                       │      │                  ╰ UID : 98c6a5d7e9e110eb 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b1458d635c48e10421543adaefa7cfcd2e071b7e8349bc9345c0b
│                       │      │                   026cc7ac74b 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-289
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                           
│                       │      │                  ────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:7180     
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-3184
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-3184      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-3184      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-08-21T13:17:47.457Z 
│                       ├ [29] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : passwd@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : passwd 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/passwd@4.17.4-2ubuntu3?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : 6f8f43a2d44eb6a2 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e2f8b2dff9e87cfb1d9b8a92ee0bfad400e2a55f61be36389a13b
│                       │      │                   2682a06eb9c 
│                       │      ├ Title           : shadow-utils: Default subordinate ID configuration in
│                       │      │                   /etc/login.defs could lead to compromise 
│                       │      ├ Description     : shadow-utils (aka shadow) 4.4 through 4.17.0 establishes a
│                       │      │                   default /etc/subuid behavior (e.g., uid 100000 through
│                       │      │                   165535 for the first user account) that can realistically
│                       │      │                   conflict with the uids of users defined on locally
│                       │      │                   administered networks, potentially leading to account
│                       │      │                   takeover, e.g., by leveraging newuidmap for access to an NFS
│                       │      │                    home directory (or same-host resources in the case of
│                       │      │                   remote logins by these local network users). NOTE: it may
│                       │      │                   also be argued that system administrators should not have
│                       │      │                   assigned uids, within local networks, that are within the
│                       │      │                   range that can occur in /etc/subuid. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                   
│                       │      │                  ────────
│                       │      │                  CWE-1188
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 1 
│                       │      │                  ├ azure      : 1 
│                       │      │                  ├ oracle-oval: 1 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.6 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2025:20559             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2024-56433        
│                       │      │                  https://bugzilla.redhat.com/2334165                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2334165          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-56433
│                       │      │                  https://errata.almalinux.org/9/ALSA-2025-20559.html          
│                       │      │                  https://errata.rockylinux.org/RLSA-2025:20559                
│                       │      │                  https://github.com/shadow-maint/shadow/blob/e2512d5741d4a44bd
│                       │      │                  d81a8c2d0029b6222728cf0/etc/login.defs#L238-L241             
│                       │      │                  https://github.com/shadow-maint/shadow/issues/1157           
│                       │      │                                                                               
│                       │      │                  https://github.com/shadow-maint/shadow/releases/tag/4.4      
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/cve/CVE-2024-56433.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2025-20559-0.html       
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2024-56433              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2024-56433              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2024-12-26T09:15:07.267Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T08:12:10.903Z 
│                       ├ [30] ╭ VulnerabilityID : CVE-2026-35341 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35341 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:8e56cf096e3d7d83ad34105ab8802a3fc545da150dcdbec10dbf8
│                       │      │                   a12fe5adf87 
│                       │      ├ Title           : A vulnerability in uutils coreutils mkfifo allows for the
│                       │      │                   unauthorized ... 
│                       │      ├ Description     : A vulnerability in uutils coreutils mkfifo allows for the
│                       │      │                   unauthorized modification of permissions on existing files.
│                       │      │                   When mkfifo fails to create a FIFO because a file already
│                       │      │                   exists at the target path, it fails to terminate the
│                       │      │                   operation for that path and continues to execute a follow-up
│                       │      │                    set_permissions call. This results in the existing file's
│                       │      │                   permissions being changed to the default mode (often 644
│                       │      │                   after umask), potentially exposing sensitive files such as
│                       │      │                   SSH private keys to other users on the system. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-732
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N 
│                       │      │                         ╰ V3Score : 7.1 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils                          
│                       │      │                  https://github.com/uutils/coreutils/issues/10020             
│                       │      │                  https://github.com/uutils/coreutils/pull/10376               
│                       │      │                  https://github.com/uutils/coreutils/security/advisories/GHSA-
│                       │      │                  pmf6-rcx4-v53v                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35341              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35341              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:36.06Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:25.5Z 
│                       ├ [31] ╭ VulnerabilityID : CVE-2026-35344 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35344 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:10f55c96e76562264bdb2fae0d77a6d5ddeb4738bec07244b5b3c
│                       │      │                   02e13a30277 
│                       │      ├ Title           : The dd utility in uutils coreutils suppresses errors during
│                       │      │                   file trunc ... 
│                       │      ├ Description     : The dd utility in uutils coreutils suppresses errors during
│                       │      │                   file truncation operations by unconditionally calling
│                       │      │                   Result::ok() on truncation attempts. While intended to mimic
│                       │      │                    GNU behavior for special files like /dev/null, the uutils
│                       │      │                   implementation also hides failures on regular files and
│                       │      │                   directories caused by full disks or read-only file systems.
│                       │      │                   This can lead to silent data corruption in backup or
│                       │      │                   migration scripts, as the utility may report a successful
│                       │      │                   operation even when the destination file contains old or
│                       │      │                   garbage data. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-252
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N 
│                       │      │                         ╰ V3Score : 3.3 
│                       │      ├ References                                                      
│                       │      │                  ───────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils            
│                       │      │                  https://github.com/uutils/coreutils/issues/9745
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35344
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35344
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:36.49Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:25.833Z 
│                       ├ [32] ╭ VulnerabilityID : CVE-2026-35345 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35345 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:1909d312c5cb6cc6b5253a09b80c94e9edea9b824d4789bbe709b
│                       │      │                   ac887ea06ba 
│                       │      ├ Title           : A vulnerability in the tail utility of uutils coreutils
│                       │      │                   allows for the ... 
│                       │      ├ Description     : A vulnerability in the tail utility of uutils coreutils
│                       │      │                   allows for the exfiltration of sensitive file contents when
│                       │      │                   using the --follow=name option. Unlike GNU tail, the uutils
│                       │      │                   implementation continues to monitor a path after it has been
│                       │      │                    replaced by a symbolic link, subsequently outputting the
│                       │      │                   contents of the link's target. In environments where a
│                       │      │                   privileged user (e.g., root) monitors a log directory, a
│                       │      │                   local attacker with write access to that directory can
│                       │      │                   replace a log file with a symlink to a sensitive system file
│                       │      │                    (such as /etc/shadow), causing tail to disclose the
│                       │      │                   contents of the sensitive file. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-59 
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:L/A:N 
│                       │      │                         ╰ V3Score : 5.3 
│                       │      ├ References                                                       
│                       │      │                  ────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils             
│                       │      │                  https://github.com/uutils/coreutils/issues/10328
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35345 
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35345 
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:36.627Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:25.943Z 
│                       ├ [33] ╭ VulnerabilityID : CVE-2026-35348 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35348 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6427105e5fb71cdefceb710ae41ca4da65ae28d5fce8ebb263a65
│                       │      │                   070bae346c7 
│                       │      ├ Title           : The sort utility in uutils coreutils is vulnerable to a
│                       │      │                   process panic  ... 
│                       │      ├ Description     : The sort utility in uutils coreutils is vulnerable to a
│                       │      │                   process panic when using the --files0-from option with
│                       │      │                   inputs containing non-UTF-8 filenames. The implementation
│                       │      │                   enforces UTF-8 encoding and utilizes expect(), causing an
│                       │      │                   immediate crash when encountering valid but non-UTF-8 paths.
│                       │      │                    This diverges from GNU sort, which treats filenames as raw
│                       │      │                   bytes. A local attacker can exploit this to crash the
│                       │      │                   utility and disrupt automated pipelines. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-248
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H 
│                       │      │                         ╰ V3Score : 5.5 
│                       │      ├ References                                                      
│                       │      │                  ───────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils            
│                       │      │                  https://github.com/uutils/coreutils/issues/9696
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35348
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35348
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.04Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.27Z 
│                       ├ [34] ╭ VulnerabilityID : CVE-2026-35350 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35350 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3d3bcda3aed7b6513ec69f6eccad44674a00208de5b36bcd540da
│                       │      │                   82d196f505e 
│                       │      ├ Title           : The cp utility in uutils coreutils fails to properly handle
│                       │      │                   setuid and ... 
│                       │      ├ Description     : The cp utility in uutils coreutils fails to properly handle
│                       │      │                   setuid and setgid bits when ownership preservation fails.
│                       │      │                   When copying with the -p (preserve) flag, the utility
│                       │      │                   applies the source mode bits even if the chown operation is
│                       │      │                   unsuccessful. This can result in a user-owned copy retaining
│                       │      │                    original privileged bits, creating unexpected privileged
│                       │      │                   executables that violate local security policies. This
│                       │      │                   differs from GNU cp, which clears these bits when ownership
│                       │      │                   cannot be preserved. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-281
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:H/A:L 
│                       │      │                         ╰ V3Score : 6.6 
│                       │      ├ References                                                      
│                       │      │                  ───────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils            
│                       │      │                  https://github.com/uutils/coreutils/issues/9750
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35350
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35350
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.327Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.48Z 
│                       ├ [35] ╭ VulnerabilityID : CVE-2026-35351 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35351 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d7213c86c2e2fe79fb846ad9fc50e796cd3b54f4b6c3fca7cdc2a
│                       │      │                   c0001d17ab9 
│                       │      ├ Title           : The mv utility in uutils coreutils fails to preserve file
│                       │      │                   ownership du ... 
│                       │      ├ Description     : The mv utility in uutils coreutils fails to preserve file
│                       │      │                   ownership during moves across different filesystem
│                       │      │                   boundaries. The utility falls back to a copy-and-delete
│                       │      │                   routine that creates the destination file using the caller's
│                       │      │                    UID/GID rather than the source's metadata. This flaw breaks
│                       │      │                    backups and migrations, causing files moved by a privileged
│                       │      │                    user (e.g., root) to become root-owned unexpectedly, which
│                       │      │                   can lead to information disclosure or restricted access for
│                       │      │                   the intended owners. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-281
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L 
│                       │      │                         ╰ V3Score : 4.2 
│                       │      ├ References                                                      
│                       │      │                  ───────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils            
│                       │      │                  https://github.com/uutils/coreutils/issues/9714
│                       │      │                  https://github.com/uutils/coreutils/pull/11706 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35351
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35351
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.457Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.587Z 
│                       ├ [36] ╭ VulnerabilityID : CVE-2026-35352 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35352 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:cf9db0cb3b12c5890de14dae85e28bf038093bc200a2ee8d3679c
│                       │      │                   5c908a28ef4 
│                       │      ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) race condition
│                       │      │                   exists in the m ... 
│                       │      ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) race condition
│                       │      │                   exists in the mkfifo utility of uutils coreutils. The
│                       │      │                   utility creates a FIFO and then performs a path-based chmod
│                       │      │                   to set permissions. A local attacker with write access to
│                       │      │                   the parent directory can swap the newly created FIFO for a
│                       │      │                   symbolic link between these two operations. This redirects
│                       │      │                   the chmod call to an arbitrary file, potentially enabling
│                       │      │                   privilege escalation if the utility is run with elevated
│                       │      │                   privileges. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H 
│                       │      │                         ╰ V3Score : 7 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/05/04/4
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/05/04/5
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/05/04/6
│                       │      │                  https://github.com/uutils/coreutils                    
│                       │      │                  https://github.com/uutils/coreutils/issues/10020       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35352        
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35352        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.597Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.69Z 
│                       ├ [37] ╭ VulnerabilityID : CVE-2026-35354 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35354 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:73a9d2e9cc95c491c1bd5fa382ecc7c46d5c4aaf5dd20cd9d7802
│                       │      │                   ae169fe30c7 
│                       │      ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability exists
│                       │      │                    in the mv ... 
│                       │      ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability exists
│                       │      │                    in the mv utility of uutils coreutils during cross-device
│                       │      │                   moves. The extended attribute (xattr) preservation logic
│                       │      │                   uses multiple path-based system calls that perform fresh
│                       │      │                   path-to-inode lookups for each operation. A local attacker
│                       │      │                   with write access to the directory can exploit this race to
│                       │      │                   swap files between calls, causing the destination file to
│                       │      │                   receive an inconsistent mix of security xattrs, such as
│                       │      │                   SELinux labels or file capabilities. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/A:N 
│                       │      │                         ╰ V3Score : 4.7 
│                       │      ├ References                                                       
│                       │      │                  ────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils             
│                       │      │                  https://github.com/uutils/coreutils/issues/10014
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35354 
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35354 
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.867Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.907Z 
│                       ├ [38] ╭ VulnerabilityID : CVE-2026-35357 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35357 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d4d53fbd5b47be6e361045a21571623f28fd359f7e02d357a7a2f
│                       │      │                   9720f68859b 
│                       │      ├ Title           : The cp utility in uutils coreutils is vulnerable to an
│                       │      │                   information dis ... 
│                       │      ├ Description     : The cp utility in uutils coreutils is vulnerable to an
│                       │      │                   information disclosure race condition. Destination files are
│                       │      │                    initially created with umask-derived permissions (e.g.,
│                       │      │                   0644) before being restricted to their final mode (e.g.,
│                       │      │                   0600) later in the process. A local attacker can race to
│                       │      │                   open the file during this window; once obtained, the file
│                       │      │                   descriptor remains valid and readable even after the
│                       │      │                   permissions are tightened, exposing sensitive or private
│                       │      │                   file contents. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N 
│                       │      │                         ╰ V3Score : 4.7 
│                       │      ├ References                                                       
│                       │      │                  ────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils             
│                       │      │                  https://github.com/uutils/coreutils/issues/10011
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35357 
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35357 
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:38.267Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.223Z 
│                       ├ [39] ╭ VulnerabilityID : CVE-2026-35359 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35359 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:84c1c122fca3291707a8b75daaed3b5ef88952c71e6276d8b8cb7
│                       │      │                   54a1be9717c 
│                       │      ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability in the
│                       │      │                    cp utilit ... 
│                       │      ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability in the
│                       │      │                    cp utility of uutils coreutils allows an attacker to bypass
│                       │      │                    no-dereference intent. The utility checks if a source path
│                       │      │                   is a symbolic link using path-based metadata but
│                       │      │                   subsequently opens it without the O_NOFOLLOW flag. An
│                       │      │                   attacker with concurrent write access can swap a regular
│                       │      │                   file for a symbolic link during this window, causing a
│                       │      │                   privileged cp process to copy the contents of arbitrary
│                       │      │                   sensitive files into a destination controlled by the
│                       │      │                   attacker. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-59 
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N 
│                       │      │                         ╰ V3Score : 4.7 
│                       │      ├ References                                                       
│                       │      │                  ────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils             
│                       │      │                  https://github.com/uutils/coreutils/issues/10017
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35359 
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35359 
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:38.537Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.437Z 
│                       ├ [40] ╭ VulnerabilityID : CVE-2026-35360 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35360 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6900335c5a94dcae5ea775a37a5e3e14e2fde66dffa1a319bd15f
│                       │      │                   912115bcf6a 
│                       │      ├ Title           : The touch utility in uutils coreutils is vulnerable to a
│                       │      │                   Time-of-Check ... 
│                       │      ├ Description     : The touch utility in uutils coreutils is vulnerable to a
│                       │      │                   Time-of-Check to Time-of-Use (TOCTOU) race condition during
│                       │      │                   file creation. When the utility identifies a missing path,
│                       │      │                   it later attempts creation using File::create(), which
│                       │      │                   internally uses O_TRUNC. An attacker can exploit this window
│                       │      │                    to create a file or swap a symlink at the target path,
│                       │      │                   causing touch to truncate an existing file and leading to
│                       │      │                   permanent data loss. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/A:H 
│                       │      │                         ╰ V3Score : 6.3 
│                       │      ├ References                                                       
│                       │      │                  ────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils             
│                       │      │                  https://github.com/uutils/coreutils/issues/10019
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35360 
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35360 
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:38.673Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.543Z 
│                       ├ [41] ╭ VulnerabilityID : CVE-2026-35363 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35363 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d20f0a924e25c254ca555052b98f6d1d6a5e8c5f136f3ac33dc0b
│                       │      │                   b8678f704da 
│                       │      ├ Title           : A vulnerability in the rm utility of uutils coreutils allows
│                       │      │                    the bypas ... 
│                       │      ├ Description     : A vulnerability in the rm utility of uutils coreutils allows
│                       │      │                    the bypass of safeguard mechanisms intended to protect the
│                       │      │                   current directory. While the utility correctly refuses to
│                       │      │                   delete . or .., it fails to recognize equivalent paths with
│                       │      │                   trailing slashes, such as ./ or .///. An accidental or
│                       │      │                   malicious execution of rm -rf ./ results in the silent
│                       │      │                   recursive deletion of all contents within the current
│                       │      │                   directory. The command further obscures the data loss by
│                       │      │                   reporting a misleading 'Invalid input' error, which may
│                       │      │                   cause users to miss the critical window for data recovery.[
│                       │      │                   m 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                 
│                       │      │                  ──────
│                       │      │                  CWE-22
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:N/I:H/A:L 
│                       │      │                         ╰ V3Score : 5.6 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils                          
│                       │      │                  https://github.com/uutils/coreutils/issues/9749              
│                       │      │                  https://github.com/uutils/coreutils/security/advisories/GHSA-
│                       │      │                  89p7-7cq3-hhr2                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35363              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35363              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:39.12Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.867Z 
│                       ├ [42] ╭ VulnerabilityID : CVE-2026-35364 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35364 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0bb41b68db2e4326ca7ca217e915e8e5d4e670c479bcb23cae78c
│                       │      │                   7ff732c7f0e 
│                       │      ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) race condition
│                       │      │                   exists in the m ... 
│                       │      ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) race condition
│                       │      │                   exists in the mv utility of uutils coreutils during
│                       │      │                   cross-device operations. The utility removes the destination
│                       │      │                    path before recreating it through a copy operation. A local
│                       │      │                    attacker with write access to the destination directory can
│                       │      │                    exploit this window to replace the destination with a
│                       │      │                   symbolic link. The subsequent privileged move operation will
│                       │      │                    follow the symlink, allowing the attacker to redirect the
│                       │      │                   write and overwrite an arbitrary target file with contents
│                       │      │                   from the source. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/A:H 
│                       │      │                         ╰ V3Score : 6.3 
│                       │      ├ References                                                       
│                       │      │                  ────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils             
│                       │      │                  https://github.com/uutils/coreutils/issues/10015
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35364 
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35364 
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:39.737Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.97Z 
│                       ├ [43] ╭ VulnerabilityID : CVE-2026-35367 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35367 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:9d77c553a1859f9c15501226c88bc30b45ad7a678c43789473ef2
│                       │      │                   4f0eb718ce3 
│                       │      ├ Title           : The nohup utility in uutils coreutils creates its default
│                       │      │                   output file, ... 
│                       │      ├ Description     : The nohup utility in uutils coreutils creates its default
│                       │      │                   output file, nohup.out, without specifying explicit
│                       │      │                   restricted permissions. This causes the file to inherit
│                       │      │                   umask-based permissions, typically resulting in a
│                       │      │                   world-readable file (0644). In multi-user environments, this
│                       │      │                    allows any user on the system to read the captured
│                       │      │                   stdout/stderr output of a command, potentially exposing
│                       │      │                   sensitive information. This behavior diverges from GNU
│                       │      │                   coreutils, which creates nohup.out with owner-only (0600)
│                       │      │                   permissions. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-732
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N 
│                       │      │                         ╰ V3Score : 3.3 
│                       │      ├ References                                                       
│                       │      │                  ────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils             
│                       │      │                  https://github.com/uutils/coreutils/issues/10021
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35367 
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35367 
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.423Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.297Z 
│                       ├ [44] ╭ VulnerabilityID : CVE-2026-35368 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35368 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:9461d7c9e863cf748fa5c119864a7b4aa395edbc54d5bb8794a64
│                       │      │                   b72fce2e7ad 
│                       │      ├ Title           : A vulnerability exists in the chroot utility of uutils
│                       │      │                   coreutils when  ... 
│                       │      ├ Description     : A vulnerability exists in the chroot utility of uutils
│                       │      │                   coreutils when using the --userspec option. The utility
│                       │      │                   resolves the user specification via getpwnam() after
│                       │      │                   entering the chroot but before dropping root privileges. On
│                       │      │                   glibc-based systems, this can trigger the Name Service
│                       │      │                   Switch (NSS) to load shared libraries (e.g., libnss_*.so.2)
│                       │      │                   from the new root directory. If the NEWROOT is writable by
│                       │      │                   an attacker, they can inject a malicious NSS module to
│                       │      │                   execute arbitrary code as root, facilitating a full
│                       │      │                   container escape or privilege escalation. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-426
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H 
│                       │      │                         ╰ V3Score : 7.9 
│                       │      ├ References                                                       
│                       │      │                  ────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils             
│                       │      │                  https://github.com/uutils/coreutils/issues/10327
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35368 
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35368 
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.56Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.4Z 
│                       ├ [45] ╭ VulnerabilityID : CVE-2026-35370 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35370 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:8062e228398d958c1f5253a5f4c94e96ee5f2df6044a37bea9c7f
│                       │      │                   13db8640977 
│                       │      ├ Title           : The id utility in uutils coreutils miscalculates the groups=
│                       │      │                    section o ... 
│                       │      ├ Description     : The id utility in uutils coreutils miscalculates the groups=
│                       │      │                    section of its output. The implementation uses a user's
│                       │      │                   real GID instead of their effective GID to compute the group
│                       │      │                    list, leading to potentially divergent output compared to
│                       │      │                   GNU coreutils. Because many scripts and automated processes
│                       │      │                   rely on the output of id to make security-critical
│                       │      │                   access-control or permission decisions, this discrepancy can
│                       │      │                    lead to unauthorized access or security
│                       │      │                   misconfigurations. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-863
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N 
│                       │      │                         ╰ V3Score : 4.4 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils                          
│                       │      │                  https://github.com/uutils/coreutils/issues/10006             
│                       │      │                  https://github.com/uutils/coreutils/security/advisories/GHSA-
│                       │      │                  47c7-qrm7-mqw7                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35370              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35370              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.833Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.613Z 
│                       ├ [46] ╭ VulnerabilityID : CVE-2026-35371 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35371 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:4cc201516153c51b48f3f61062e74d33075970896a88284612ad4
│                       │      │                   c8315b62d3a 
│                       │      ├ Title           : The id utility in uutils coreutils exhibits incorrect
│                       │      │                   behavior in its  ... 
│                       │      ├ Description     : The id utility in uutils coreutils exhibits incorrect
│                       │      │                   behavior in its "pretty print" output when the real UID and
│                       │      │                   effective UID differ. The implementation incorrectly uses
│                       │      │                   the effective GID instead of the effective UID when
│                       │      │                   performing a name lookup for the effective user. This
│                       │      │                   results in misleading diagnostic output that can cause
│                       │      │                   automated scripts or system administrators to make incorrect
│                       │      │                    decisions regarding file permissions or access control. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-451
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N 
│                       │      │                         ╰ V3Score : 3.3 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils                          
│                       │      │                  https://github.com/uutils/coreutils/issues/10006             
│                       │      │                  https://github.com/uutils/coreutils/security/advisories/GHSA-
│                       │      │                  xv5w-cw7x-72gj                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35371              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35371              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.987Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.723Z 
│                       ├ [47] ╭ VulnerabilityID : CVE-2026-35373 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35373 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:39330d39fa4e0cc6ac436563cafb9f3ca059af03f97b888953729
│                       │      │                   7720f3e1c67 
│                       │      ├ Title           : A logic error in the ln utility of uutils coreutils causes
│                       │      │                   the program ... 
│                       │      ├ Description     : A logic error in the ln utility of uutils coreutils causes
│                       │      │                   the program to reject source paths containing non-UTF-8
│                       │      │                   filename bytes when using target-directory forms (e.g., ln
│                       │      │                   SOURCE... DIRECTORY). While GNU ln treats filenames as raw
│                       │      │                   bytes and creates the links correctly, the uutils
│                       │      │                   implementation enforces UTF-8 encoding, resulting in a
│                       │      │                   failure to stat the file and a non-zero exit code. In
│                       │      │                   environments where automated scripts or system tasks process
│                       │      │                    valid but non-UTF-8 filenames common on Unix filesystems,
│                       │      │                   this divergence causes the utility to fail, leading to a
│                       │      │                   local denial of service for those specific operations. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-176
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L 
│                       │      │                  │      ╰ V3Score : 3.3 
│                       │      │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H 
│                       │      │                         ╰ V3Score : 5.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils                          
│                       │      │                  https://github.com/uutils/coreutils/pull/11403               
│                       │      │                  https://github.com/uutils/coreutils/security/advisories/GHSA-
│                       │      │                  jcjr-rh8q-7xqf                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35373              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35373              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:41.997Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.933Z 
│                       ├ [48] ╭ VulnerabilityID : CVE-2026-35374 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:736e63936a2a1ae1318f8f405cfbb8d4f574850247ec07cec74f5
│                       │      │                   c49943ebb84 
│                       │      ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability exists
│                       │      │                    in the sp ... 
│                       │      ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability exists
│                       │      │                    in the split utility of uutils coreutils. The program
│                       │      │                   attempts to prevent data loss by checking for identity
│                       │      │                   between input and output files using their file paths before
│                       │      │                    initiating the split operation. However, the utility
│                       │      │                   subsequently opens the output file with truncation after
│                       │      │                   this path-based validation is complete. A local attacker
│                       │      │                   with write access to the directory can exploit this race
│                       │      │                   window by manipulating mutable path components (e.g.,
│                       │      │                   swapping a path with a symbolic link). This can cause split
│                       │      │                   to truncate and write to an unintended target file,
│                       │      │                   potentially including the input file itself or other
│                       │      │                   sensitive files accessible to the process, leading to
│                       │      │                   permanent data loss. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/A:H 
│                       │      │                         ╰ V3Score : 6.3 
│                       │      ├ References                                                      
│                       │      │                  ───────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils            
│                       │      │                  https://github.com/uutils/coreutils/pull/11401 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35374
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35374
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:42.127Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:29.04Z 
│                       ├ [49] ╭ VulnerabilityID : CVE-2026-35377 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35377 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:9d5e7ee65174d47b7db8b4f7a334af885997b342f063cf7cfd28c
│                       │      │                   3b11400772d 
│                       │      ├ Title           : A logic error in the env utility of uutils coreutils causes
│                       │      │                   a failure  ... 
│                       │      ├ Description     : A logic error in the env utility of uutils coreutils causes
│                       │      │                   a failure to correctly parse command-line arguments when
│                       │      │                   utilizing the -S (split-string) option. In GNU env,
│                       │      │                   backslashes within single quotes are treated literally (with
│                       │      │                    the exceptions of \\ and \'). However, the uutils
│                       │      │                   implementation incorrectly attempts to validate these
│                       │      │                   sequences, resulting in an "invalid sequence" error and an
│                       │      │                   immediate process termination with an exit status of 125
│                       │      │                   when encountering valid but unrecognized sequences like \a
│                       │      │                   or \x. This divergence from GNU behavior breaks
│                       │      │                   compatibility for automated scripts and administrative
│                       │      │                   workflows that rely on standard split-string semantics,
│                       │      │                   leading to a local denial of service for those operations.[
│                       │      │                   m 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                 
│                       │      │                  ──────
│                       │      │                  CWE-20
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ ghsa  : 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L 
│                       │      │                         ╰ V3Score : 3.3 
│                       │      ├ References                                                      
│                       │      │                  ───────────────────────────────────────────────
│                       │      │                  https://github.com/uutils/coreutils            
│                       │      │                  https://github.com/uutils/coreutils/pull/11512 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-35377
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-35377
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-22T17:16:42.577Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:29.357Z 
│                       ├ [50] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : util-linux@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : util-linux 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/util-linux@2.41.3-3ubuntu2?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 34e9503915630576 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ca0e9f99aab3119c61912d3e01d0aaad7d491ebe533ceccb785b0
│                       │      │                   8cd2b0afa88 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-59 
│                       │      │                  CWE-269
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-27456 
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-27456        
│                       │      │                  https://github.com/bottlerocket-os/bottlerocket-core-kit/blob
│                       │      │                  /develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.toml            
│                       │      │                  https://github.com/util-linux/util-linux/commit/5e390467b26a3
│                       │      │                  cf3fecc04e1a0d482dff3162fc4                                  
│                       │      │                  https://github.com/util-linux/util-linux/releases/tag/v2.41.4
│                       │      │                                                                               
│                       │      │                  https://github.com/util-linux/util-linux/security/advisories/
│                       │      │                  GHSA-qq4x-vfq4-9h9g                                          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-27456              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-07-24T22:10:00.14Z 
│                       ├ [51] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : util-linux@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : util-linux 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/util-linux@2.41.3-3ubuntu2?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 34e9503915630576 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                       │      │                  │         3cff84dcfa0a255f209e 
│                       │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                       │      │                            9e194f8c4780e1e1a63d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6120751ed74565ab67ec988b56540e6d98e947b0690eb7efa8de4
│                       │      │                   c05b2922a5e 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-289
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                           
│                       │      │                  ────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:7180     
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-3184
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-3184      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-3184      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-08-21T13:17:47.457Z 
│                       ╰ [52] ╭ VulnerabilityID : CVE-2026-27171 
│                              ├ PkgID           : zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu3 
│                              ├ PkgName         : zlib1g 
│                              ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/zlib1g@1.3.dfsg%2Breally1.3.1-1ubuntu3
│                              │                  │       ?arch=amd64&distro=ubuntu-26.04&epoch=1 
│                              │                  ╰ UID : e6f2cecd2b667912 
│                              ├ InstalledVersion: 1:1.3.dfsg+really1.3.1-1ubuntu3 
│                              ├ Status          : affected 
│                              ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
│                              │                  │         3cff84dcfa0a255f209e 
│                              │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
│                              │                            9e194f8c4780e1e1a63d 
│                              ├ SeveritySource  : ubuntu 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27171 
│                              ├ DataSource       ╭ ID  : ubuntu 
│                              │                  ├ Name: Ubuntu CVE Tracker 
│                              │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                              ├ Fingerprint     : sha256:808173db1728d9b2054098e20dea034e589a44d3dbb4d02972610
│                              │                   77aec03aef8 
│                              ├ Title           : zlib: zlib: Denial of Service via infinite loop in CRC32
│                              │                   combine functions 
│                              ├ Description     : zlib before 1.3.2 allows CPU consumption via crc32_combine64
│                              │                    and crc32_combine_gen64 because x2nmodp can do right shifts
│                              │                    within a loop that has no termination condition. 
│                              ├ Severity        : LOW 
│                              ├ CweIDs                   
│                              │                  ────────
│                              │                  CWE-1284
│                              │                  
│                              ├ VendorSeverity   ╭ amazon     : 1 
│                              │                  ├ azure      : 1 
│                              │                  ├ cbl-mariner: 1 
│                              │                  ├ julia      : 2 
│                              │                  ├ nvd        : 2 
│                              │                  ├ photon     : 2 
│                              │                  ├ redhat     : 1 
│                              │                  ╰ ubuntu     : 1 
│                              ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                              │                  │        │           /A:H 
│                              │                  │        ╰ V3Score : 5.5 
│                              │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                              │                  │        │           /A:H 
│                              │                  │        ╰ V3Score : 5.5 
│                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                              │                           │           /A:L 
│                              │                           ╰ V3Score : 3.3 
│                              ├ References                                                                   
│                              │                  ────────────────────────────────────────────────────────────
│                              │                  https://7asecurity.com/blog/2026/02/zlib-7asecurity-audit   
│                              │                  https://7asecurity.com/blog/2026/02/zlib-7asecurity-audit/  
│                              │                  https://7asecurity.com/reports/pentest-report-zlib-RC1.1.pdf
│                              │                  https://access.redhat.com/security/cve/CVE-2026-27171       
│                              │                  https://github.com/advisories/GHSA-h858-mf2m-8jf4           
│                              │                  https://github.com/madler/zlib/issues/904                   
│                              │                  https://github.com/madler/zlib/releases/tag/v1.3.2          
│                              │                  https://nvd.nist.gov/vuln/detail/CVE-2026-27171             
│                              │                  https://ostif.org/zlib-audit-complete                       
│                              │                  https://ostif.org/zlib-audit-complete/                      
│                              │                  https://www.cve.org/CVERecord?id=CVE-2026-27171             
│                              │                  
│                              ├ PublishedDate   : 2026-02-18T04:16:01.263Z 
│                              ╰ LastModifiedDate: 2026-06-17T10:26:47.357Z 
├ [1] ╭ Target  : Java 
│     ├ Class   : lang-pkgs 
│     ├ Type    : jar 
│     ╰ Packages 
╰ [2] ╭ Target         : usr/bin/pebble 
      ├ Class          : lang-pkgs 
      ├ Type           : gobinary 
      ├ Packages        
      ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : GHSA-w67g-5rqw-f597 
                        │      ├ PkgID           : github.com/gorilla/websocket@v1.5.1 
                        │      ├ PkgName         : github.com/gorilla/websocket 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/github.com/gorilla/websocket@v1.5.1 
                        │      │                  ╰ UID : 13db0ba03ae70421 
                        │      ├ InstalledVersion: v1.5.1 
                        │      ├ FixedVersion    : 1.5.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ SeveritySource  : ghsa 
                        │      ├ PrimaryURL      : https://github.com/advisories/GHSA-w67g-5rqw-f597 
                        │      ├ DataSource       ╭ ID  : ghsa 
                        │      │                  ├ Name: GitHub Security Advisory Go 
                        │      │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+e
                        │      │                          cosystem%3Ago 
                        │      ├ Fingerprint     : sha256:1c840dc1873ff2e460039c99d6e032ec9239fe7cfed34f5206bf1
                        │      │                   dcfe7d39089 
                        │      ├ Title           : Gorilla WebSocket Uses Cryptographically Weak PRNG for
                        │      │                   WebSocket Mask Key 
                        │      ├ Description     : gorilla/websocket used `math/rand` (cryptographically weak
                        │      │                   pseudo-random number generator) to generate WebSocket frame
                        │      │                   mask keys prior to commit d67f4185. WebSocket masking keys
                        │      │                   MUST be unpredictable to prevent frame content injection
                        │      │                   attacks. math/rand produces deterministic output when seeded
                        │      │                    with a known value, enabling an attacker to predict or
                        │      │                   recover mask keys and inject content into WebSocket
                        │      │                   connections.
                        │      │                   
                        │      │                   **Type:** Use of Cryptographically Weak Pseudo-Random Number
                        │      │                    Generator
                        │      │                   **Fix:** Replaced math/rand with crypto/rand (commit
                        │      │                   d67f4185, released in v1.5.3)
                        │      │                   **Credit:** bounty-hunter v6.0 silent-fix detection 
                        │      ├ Severity        : MEDIUM 
                        │      ├ VendorSeverity   ─ ghsa: 2 
                        │      ├ CVSS             ─ ghsa ╭ V40Vector: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI
                        │      │                         │            :L/VA:N/SC:N/SI:N/SA:N 
                        │      │                         ╰ V40Score : 6.9 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://github.com/canolgun-commits/websocket                
                        │      │                  https://github.com/canolgun-commits/websocket/security/adviso
                        │      │                  ries/GHSA-w67g-5rqw-f597                                     
                        │      │                  https://github.com/gorilla/websocket/commit/d67f41855da42d7bc
                        │      │                  cd9ef050c49f7e54e783b95                                      
                        │      │                  https://github.com/gorilla/websocket/releases/tag/v1.5.3     
                        │      │                                                                               
                        │      │                  
                        │      ├ PublishedDate   : 2026-08-24T21:00:54Z 
                        │      ╰ LastModifiedDate: 2026-08-24T21:00:54Z 
                        ├ [1]  ╭ VulnerabilityID : CVE-2026-25681 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-5029
                        │      │                  
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.55.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-25681 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:33cd00ab359f6d2cc791849baced936ea52b36cd2c3d7e38b8deb
                        │      │                   0d9da67d5b4 
                        │      ├ Title           : golang.org/x/net/html: golang.org/x/net/html: Arbitrary code
                        │      │                    execution via Cross-Site Scripting 
                        │      ├ Description     : Parsing arbitrary HTML which is then rendered using Render
                        │      │                   can result in an unexpected HTML tree. This can be leveraged
                        │      │                    to execute XSS attacks in applications that attempt to
                        │      │                   sanitize input HTML before rendering. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                   
                        │      │                  ────────
                        │      │                  CWE-1021
                        │      │                  
                        │      ├ VendorSeverity   ╭ alma       : 3 
                        │      │                  ├ amazon     : 3 
                        │      │                  ├ azure      : 2 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ redhat     : 3 
                        │      │                  ╰ rocky      : 3 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 8.1 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:37123             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-25681        
                        │      │                  https://bugzilla.redhat.com/2480680                          
                        │      │                  https://bugzilla.redhat.com/2480681                          
                        │      │                  https://bugzilla.redhat.com/2480685                          
                        │      │                  https://bugzilla.redhat.com/2480688                          
                        │      │                  https://bugzilla.redhat.com/2480757                          
                        │      │                  https://bugzilla.redhat.com/2480761                          
                        │      │                  https://bugzilla.redhat.com/2493620                          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480680          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480681          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480685          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480688          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480757          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480761          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2493620          
                        │      │                  https://creativecommons.org/licenses/by/4.0/                 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-25681
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-27136
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39829
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39832
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39835
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42508
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-57231
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-37123.html          
                        │      │                  https://errata.rockylinux.org/RLSA-2026:37123                
                        │      │                  https://go.dev/cl/781703                                     
                        │      │                  https://go.dev/issue/79574                                   
                        │      │                  https://groups.google.com/g/golang-announce/c/iI-mYSI0lu8    
                        │      │                  https://linux.oracle.com/cve/CVE-2026-25681.html             
                        │      │                  https://linux.oracle.com/errata/ELSA-2026-37123.html         
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-25681              
                        │      │                  https://pkg.go.dev/vuln/GO-2026-5029                         
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-25681              
                        │      │                  
                        │      ├ PublishedDate   : 2026-05-22T16:16:19.863Z 
                        │      ╰ LastModifiedDate: 2026-07-23T16:10:00.137Z 
                        ├ [2]  ╭ VulnerabilityID : CVE-2026-27136 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-5030
                        │      │                  
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.55.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27136 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:e3424a3f8a16fa949d552eafd264f495d1ccf1330f1cc3a478d2f
                        │      │                   b7493558470 
                        │      ├ Title           : golang.org/x/net/html: golang: golang.org/x/net/html:
                        │      │                   Cross-Site Scripting via HTML parsing bypass 
                        │      ├ Description     : Parsing arbitrary HTML which is then rendered using Render
                        │      │                   can result in an unexpected HTML tree. This can be leveraged
                        │      │                    to execute XSS attacks in applications that attempt to
                        │      │                   sanitize input HTML before rendering. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                   
                        │      │                  ────────
                        │      │                  CWE-1021
                        │      │                  
                        │      ├ VendorSeverity   ╭ alma       : 3 
                        │      │                  ├ amazon     : 3 
                        │      │                  ├ azure      : 2 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ redhat     : 3 
                        │      │                  ╰ rocky      : 3 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 8.1 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:37123             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-27136        
                        │      │                  https://bugzilla.redhat.com/2480680                          
                        │      │                  https://bugzilla.redhat.com/2480681                          
                        │      │                  https://bugzilla.redhat.com/2480685                          
                        │      │                  https://bugzilla.redhat.com/2480688                          
                        │      │                  https://bugzilla.redhat.com/2480757                          
                        │      │                  https://bugzilla.redhat.com/2480761                          
                        │      │                  https://bugzilla.redhat.com/2493620                          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480680          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480681          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480685          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480688          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480757          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480761          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2493620          
                        │      │                  https://creativecommons.org/licenses/by/4.0/                 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-25681
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-27136
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39829
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39832
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39835
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42508
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-57231
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-37123.html          
                        │      │                  https://errata.rockylinux.org/RLSA-2026:37123                
                        │      │                  https://go.dev/cl/781685                                     
                        │      │                  https://go.dev/issue/79575                                   
                        │      │                  https://groups.google.com/g/golang-announce/c/iI-mYSI0lu8    
                        │      │                  https://linux.oracle.com/cve/CVE-2026-27136.html             
                        │      │                  https://linux.oracle.com/errata/ELSA-2026-37123.html         
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-27136              
                        │      │                  https://pkg.go.dev/vuln/GO-2026-5030                         
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-27136              
                        │      │                  
                        │      ├ PublishedDate   : 2026-05-22T16:16:20.087Z 
                        │      ╰ LastModifiedDate: 2026-07-23T16:10:00.137Z 
                        ├ [3]  ╭ VulnerabilityID : CVE-2026-33814 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-4918
                        │      │                  
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.53.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ SeveritySource  : nvd 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-33814 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:df61f8fbb964c8ad046dd2a21cb3bd10eb2a7ebb43da2d86c5a47
                        │      │                   4e8ada9a5d0 
                        │      ├ Title           : net/http/internal/http2: golang: golang.org/x/net: Go
                        │      │                   HTTP/2: Denial of Service via malformed
                        │      │                   SETTINGS_MAX_FRAME_SIZE frame 
                        │      ├ Description     : When processing HTTP/2 SETTINGS frames, transport will enter
                        │      │                    an infinite loop of writing CONTINUATION frames if it
                        │      │                   receives a SETTINGS_MAX_FRAME_SIZE with a value of 0. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-835
                        │      │                  CWE-606
                        │      │                  
                        │      ├ VendorSeverity   ╭ amazon     : 3 
                        │      │                  ├ azure      : 2 
                        │      │                  ├ bitnami    : 3 
                        │      │                  ├ nvd        : 3 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ photon     : 3 
                        │      │                  ├ redhat     : 3 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ├ nvd     ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:23262             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:23264             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33120             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33123             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33142             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33150             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:34342             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:37387             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42644             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:43692             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:50205             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54274             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54283             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54284             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54285             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54286             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54287             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57191             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57194             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-33814        
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467815          
                        │      │                  https://github.com/golang/go/issues/78476                    
                        │      │                  https://go-review.googlesource.com/c/go/+/761581             
                        │      │                  https://go-review.googlesource.com/c/net/+/761640            
                        │      │                  https://go.dev/cl/761581                                     
                        │      │                  https://go.dev/cl/761640                                     
                        │      │                  https://go.dev/issue/78476                                   
                        │      │                  https://groups.google.com/g/golang-announce/c/qcCIEXso47M    
                        │      │                  https://linux.oracle.com/cve/CVE-2026-33814.html             
                        │      │                  https://linux.oracle.com/errata/ELSA-2026-22121.html         
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-33814              
                        │      │                  https://pkg.go.dev/vuln/GO-2026-4918                         
                        │      │                  https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-
                        │      │                  2026-33814.json                                              
                        │      │                  https://ubuntu.com/security/notices/USN-8430-1               
                        │      │                                                                               
                        │      │                  https://ubuntu.com/security/notices/USN-8471-1               
                        │      │                                                                               
                        │      │                  https://ubuntu.com/security/notices/USN-8472-1               
                        │      │                                                                               
                        │      │                  https://ubuntu.com/security/notices/USN-8473-1               
                        │      │                                                                               
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-33814              
                        │      │                                                                               
                        │      │                  
                        │      ├ PublishedDate   : 2026-05-07T20:16:42.88Z 
                        │      ╰ LastModifiedDate: 2026-08-24T13:18:13.207Z 
                        ├ [4]  ╭ VulnerabilityID : CVE-2026-39821 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-5026
                        │      │                  
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.55.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-39821 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:2e8944ebe5340c5d76e2f0480794b5332cb85c71b6fd61abd591b
                        │      │                   04e746322eb 
                        │      ├ Title           : golang.org/x/net/idna: golang: net/http:
                        │      │                   golang.org/x/net/idna: Privilege escalation via incorrect
                        │      │                   Punycode label processing 
                        │      ├ Description     : The ToASCII and ToUnicode functions incorrectly accept
                        │      │                   Punycode-encoded labels that decode to an ASCII-only label.
                        │      │                   For example, ToUnicode("xn--example-.com") incorrectly
                        │      │                   returns the name "example.com" rather than an error. This
                        │      │                   behavior can lead to privilege escalation in programs using
                        │      │                   the idna package. For example, a program which performs
                        │      │                   privilege checks on the ASCII hostname may reject
                        │      │                   "example.com" but permit "xn--example-.com". If that program
                        │      │                    subsequently converts the ASCII hostname to Unicode, it
                        │      │                   will inadvertently permits access to the Unicode name
                        │      │                   "example.com". 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                   
                        │      │                  ────────
                        │      │                  CWE-1289
                        │      │                  
                        │      ├ VendorSeverity   ╭ alma       : 3 
                        │      │                  ├ amazon     : 3 
                        │      │                  ├ azure      : 4 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ redhat     : 3 
                        │      │                  ├ rocky      : 3 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 8.2 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:23262             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:23264             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:26546             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:26547             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:30650             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:30651             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:30853             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:30854             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:30855             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33155             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33160             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33163             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33173             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33183             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33524             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33531             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:34342             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:34357             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:34359             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:34364             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:34789             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35826             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35827             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35828             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35829             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35830             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35831             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35993             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35994             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36105             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36167             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36207             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36648             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36651             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36796             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36797             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36808             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36820             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36883             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:37387             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:37435             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:37436             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:38995             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:39005             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:39573             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:39879             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:40118             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:40262             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:40945             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41019             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41030             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41031             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41036             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41055             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41066             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41928             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41930             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42043             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42047             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42048             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42049             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42050             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42051             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42078             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42079             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42080             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42082             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42132             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42142             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42146             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42150             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42151             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42240             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42644             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42796             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42852             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:43038             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:43052             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:43692             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:44622             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:44624             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:46395             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:47149             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:47735             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:47737             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:47952             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:50300             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:50843             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:51033             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:51112             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:51187             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:51194             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:51341             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:52826             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:53374             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:53412             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:53413             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:53415             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:53530             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54191             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54274             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54283             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54284             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54285             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54286             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54287             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54395             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54401             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54435             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54441             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54531             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54580             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54757             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:56143             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:56223             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:56340             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:56431             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57194             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57541             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-39821        
                        │      │                  https://bugzilla.redhat.com/2480756                          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480756          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2498152          
                        │      │                  https://creativecommons.org/licenses/by/4.0/                 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39821
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39822
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-37435.html          
                        │      │                  https://errata.rockylinux.org/RLSA-2026:37435                
                        │      │                  https://github.com/golang/go/issues/78760                    
                        │      │                  https://go.dev/cl/767220                                     
                        │      │                  https://go.dev/issue/78760                                   
                        │      │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                        │      │                  https://groups.google.com/g/golang-announce/c/iI-mYSI0lu8    
                        │      │                  https://linux.oracle.com/cve/CVE-2026-39821.html             
                        │      │                  https://linux.oracle.com/errata/ELSA-2026-46395.html         
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-39821              
                        │      │                  https://pkg.go.dev/vuln/GO-2026-5026                         
                        │      │                  https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-
                        │      │                  2026-39821.json                                              
                        │      │                  https://ubuntu.com/security/notices/USN-8416-1               
                        │      │                                                                               
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-39821              
                        │      │                                                                               
                        │      │                  
                        │      ├ PublishedDate   : 2026-05-22T16:16:20.41Z 
                        │      ╰ LastModifiedDate: 2026-08-24T13:18:22.547Z 
                        ├ [5]  ╭ VulnerabilityID : CVE-2026-46600 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-5942
                        │      │                  
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.56.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46600 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:694acd8ff1f0f494d0a20de2eb8111b9f3fd27afe985b76b200d2
                        │      │                   dac091379b4 
                        │      ├ Title           : golang.org/x/net/dns/dnsmessage:
                        │      │                   golang.org/x/net/dns/dnsmessage: Denial of Service via
                        │      │                   invalid DNS record parsing 
                        │      ├ Description     : Parsing an invalid SVCB or HTTPS RR can panic when the size
                        │      │                   of a parameter value overflows the message buffer. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-125
                        │      │                  
                        │      ├ VendorSeverity   ╭ azure  : 2 
                        │      │                  ├ bitnami: 3 
                        │      │                  ╰ redhat : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-46600    
                        │      │                  https://go.dev/cl/786345                                 
                        │      │                  https://go.dev/issue/79795                               
                        │      │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-46600          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-5942                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-46600          
                        │      │                  
                        │      ├ PublishedDate   : 2026-07-21T20:17:01.213Z 
                        │      ╰ LastModifiedDate: 2026-08-14T16:16:55.673Z 
                        ├ [6]  ╭ VulnerabilityID : CVE-2025-47911 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-4440
                        │      │                  
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.45.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ SeveritySource  : nvd 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-47911 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:c82251dd54b9e88d73251e01fd89ebde5367a171603fd7922e6c3
                        │      │                   b5f8fa856a2 
                        │      ├ Title           : golang.org/x/net/html: Quadratic parsing complexity in
                        │      │                   golang.org/x/net/html 
                        │      ├ Description     : The html.Parse function in golang.org/x/net/html has
                        │      │                   quadratic parsing complexity when processing certain inputs,
                        │      │                    which can lead to denial of service (DoS) if an attacker
                        │      │                   provides specially crafted HTML content. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ VendorSeverity   ╭ amazon     : 2 
                        │      │                  ├ azure      : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                  │        │           /A:L 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                           │           /A:L 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2025-47911    
                        │      │                  https://github.com/golang/go/issues/75682                
                        │      │                  https://github.com/golang/vulndb/issues/4440             
                        │      │                  https://go.dev/cl/709876                                 
                        │      │                  https://groups.google.com/g/golang-announce/c/jnQcOYpiR2c
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2025-47911          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-4440                     
                        │      │                  https://ubuntu.com/security/notices/USN-8089-1           
                        │      │                  https://ubuntu.com/security/notices/USN-8089-2           
                        │      │                  https://ubuntu.com/security/notices/USN-8089-3           
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2025-47911          
                        │      │                  
                        │      ├ PublishedDate   : 2026-02-05T18:16:09.893Z 
                        │      ╰ LastModifiedDate: 2026-06-17T09:28:50.07Z 
                        ├ [7]  ╭ VulnerabilityID : CVE-2025-58190 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-4441
                        │      │                  
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.45.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ SeveritySource  : nvd 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-58190 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:2f88ca6b605197bb832b9d41fdb3d14cca5139104ec49569a04d9
                        │      │                   412faeaa69f 
                        │      ├ Title           : golang.org/x/net/html: Infinite parsing loop in
                        │      │                   golang.org/x/net 
                        │      ├ Description     : The html.Parse function in golang.org/x/net/html has an
                        │      │                   infinite parsing loop when processing certain inputs, which
                        │      │                   can lead to denial of service (DoS) if an attacker provides
                        │      │                   specially crafted HTML content. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-835
                        │      │                  
                        │      ├ VendorSeverity   ╭ amazon     : 2 
                        │      │                  ├ azure      : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                  │        │           /A:L 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N
                        │      │                           │           /A:L 
                        │      │                           ╰ V3Score : 4.3 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2025-58190    
                        │      │                  https://github.com/golang/go/issues/70179                
                        │      │                  https://github.com/golang/vulndb/issues/4441             
                        │      │                  https://go.dev/cl/709875                                 
                        │      │                  https://groups.google.com/g/golang-announce/c/jnQcOYpiR2c
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2025-58190          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-4441                     
                        │      │                  https://ubuntu.com/security/notices/USN-8089-1           
                        │      │                  https://ubuntu.com/security/notices/USN-8089-2           
                        │      │                  https://ubuntu.com/security/notices/USN-8089-3           
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2025-58190          
                        │      │                  
                        │      ├ PublishedDate   : 2026-02-05T18:16:10.027Z 
                        │      ╰ LastModifiedDate: 2026-06-17T09:44:02.557Z 
                        ├ [8]  ╭ VulnerabilityID : CVE-2026-25680 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-5028
                        │      │                  
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.55.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-25680 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:d73d9a34e983617ce137c5d6d23bf85b529e8620d38fd0355736c
                        │      │                   987fedf5511 
                        │      ├ Title           : golang.org/x/net/html: golang.org/x/net/html: Denial of
                        │      │                   Service due to excessive HTML parsing 
                        │      ├ Description     : Parsing arbitrary HTML can consume excessive CPU time,
                        │      │                   possibly leading to denial of service. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-400
                        │      │                  
                        │      ├ VendorSeverity   ╭ amazon: 3 
                        │      │                  ├ azure : 2 
                        │      │                  ╰ redhat: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N
                        │      │                           │           /A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-25680    
                        │      │                  https://go.dev/cl/781702                                 
                        │      │                  https://go.dev/issue/79573                               
                        │      │                  https://groups.google.com/g/golang-announce/c/iI-mYSI0lu8
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-25680          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-5028                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-25680          
                        │      │                  
                        │      ├ PublishedDate   : 2026-05-22T16:16:19.753Z 
                        │      ╰ LastModifiedDate: 2026-07-23T16:10:00.137Z 
                        ├ [9]  ╭ VulnerabilityID : CVE-2026-42502 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-5027
                        │      │                  
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.55.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42502 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:6fef51aff124aa34bcc5971409560614e03ca4b1a6fa99c19254f
                        │      │                   42f84dd73d4 
                        │      ├ Title           : golang.org/x/net/html: golang: golang.org/x/net/html:
                        │      │                   Cross-Site Scripting via unexpected HTML tree rendering 
                        │      ├ Description     : Parsing arbitrary HTML which is then rendered using Render
                        │      │                   can result in an unexpected HTML tree. This can be leveraged
                        │      │                    to execute XSS attacks in applications that attempt to
                        │      │                   sanitize input HTML before rendering. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                   
                        │      │                  ────────
                        │      │                  CWE-1021
                        │      │                  
                        │      ├ VendorSeverity   ╭ amazon: 3 
                        │      │                  ├ azure : 2 
                        │      │                  ╰ redhat: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 6.1 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-42502    
                        │      │                  https://go.dev/cl/781701                                 
                        │      │                  https://go.dev/issue/79572                               
                        │      │                  https://groups.google.com/g/golang-announce/c/iI-mYSI0lu8
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-42502          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-5027                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-42502          
                        │      │                  
                        │      ├ PublishedDate   : 2026-05-22T16:16:20.587Z 
                        │      ╰ LastModifiedDate: 2026-07-23T16:10:00.137Z 
                        ├ [10] ╭ VulnerabilityID : CVE-2026-42506 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-5025
                        │      │                  
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.55.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42506 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:478e9b7319530bb9d3408f2660ec0f81cb0c334be8c310ec9bec0
                        │      │                   889a9687fdc 
                        │      ├ Title           : golang.org/x/net/html: golang.org/x/net/html: Cross-Site
                        │      │                   Scripting (XSS) via arbitrary HTML parsing 
                        │      ├ Description     : Parsing arbitrary HTML which is then rendered using Render
                        │      │                   can result in an unexpected HTML tree. This can be leveraged
                        │      │                    to execute XSS attacks in applications that attempt to
                        │      │                   sanitize input HTML before rendering. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                 
                        │      │                  ──────
                        │      │                  CWE-79
                        │      │                  
                        │      ├ VendorSeverity   ╭ amazon: 3 
                        │      │                  ├ azure : 2 
                        │      │                  ╰ redhat: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 5.4 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-42506    
                        │      │                  https://go.dev/cl/781700                                 
                        │      │                  https://go.dev/issue/79571                               
                        │      │                  https://groups.google.com/g/golang-announce/c/iI-mYSI0lu8
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-42506          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-5025                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-42506          
                        │      │                  
                        │      ├ PublishedDate   : 2026-05-22T16:16:20.803Z 
                        │      ╰ LastModifiedDate: 2026-07-23T16:10:00.137Z 
                        ├ [11] ╭ VulnerabilityID : CVE-2026-39824 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-5024
                        │      │                  
                        │      ├ PkgID           : golang.org/x/sys@v0.33.0 
                        │      ├ PkgName         : golang.org/x/sys 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/sys@v0.33.0 
                        │      │                  ╰ UID : a350d4cc028089d4 
                        │      ├ InstalledVersion: v0.33.0 
                        │      ├ FixedVersion    : 0.44.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-39824 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:33e5e58d75dee191d3dbafc6c71df18b1adeff62a46f7e3dace6f
                        │      │                   ac06fc9648d 
                        │      ├ Title           : Invoking integer overflow in NewNTUnicodeString in
                        │      │                   golang.org/x/sys/windows 
                        │      ├ Description     : NewNTUnicodeString does not check for string length
                        │      │                   overflow. When provided with a string that overflows the
                        │      │                   maximum size of a NTUnicodeString (a 16-bit number of
                        │      │                   bytes), it returns a truncated string rather than an
                        │      │                   error. 
                        │      ├ Severity        : UNKNOWN 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-190
                        │      │                  
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://go.dev/cl/770080                                 
                        │      │                  https://go.dev/issue/78916                               
                        │      │                  https://groups.google.com/g/golang-announce/c/6MMI8Lj-Atg
                        │      │                  https://pkg.go.dev/vuln/GO-2026-5024                     
                        │      │                  
                        │      ├ PublishedDate   : 2026-05-22T20:16:33.057Z 
                        │      ╰ LastModifiedDate: 2026-07-23T16:10:00.137Z 
                        ├ [12] ╭ VulnerabilityID : CVE-2026-33818 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-5972
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.4 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.4 
                        │      │                  ╰ UID : 364846ec8fe81bdc 
                        │      ├ InstalledVersion: v1.26.4 
                        │      ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-33818 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:57a5300dc506023770d06381e75889acabc9ad26580459105513b
                        │      │                   4e61af8fc14 
                        │      ├ Title           : encoding/asn1: golang: Go encoding/asn1: Denial of Service
                        │      │                   via excessive recursion in Unmarshal 
                        │      ├ Description     : Enforce a recursion limit in Unmarshal to prevent stack
                        │      │                   exhaustion when parsing deeply-nested, recursive
                        │      │                   structures. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-400
                        │      │                  
                        │      ├ VendorSeverity   ╭ bitnami: 3 
                        │      │                  ╰ redhat : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-33818    
                        │      │                  https://go.dev/cl/814980                                 
                        │      │                  https://go.dev/issue/80405                               
                        │      │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-33818          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-5972                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-33818          
                        │      │                  
                        │      ├ PublishedDate   : 2026-08-13T22:17:19.84Z 
                        │      ╰ LastModifiedDate: 2026-08-14T16:16:55.317Z 
                        ├ [13] ╭ VulnerabilityID : CVE-2026-39821 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-5026
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.4 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.4 
                        │      │                  ╰ UID : 364846ec8fe81bdc 
                        │      ├ InstalledVersion: v1.26.4 
                        │      ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-39821 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:e7eebe0766abc46c7268a518856231ba379b50d6ac6e68aeade57
                        │      │                   0271e5fabd9 
                        │      ├ Title           : golang.org/x/net/idna: golang: net/http:
                        │      │                   golang.org/x/net/idna: Privilege escalation via incorrect
                        │      │                   Punycode label processing 
                        │      ├ Description     : The ToASCII and ToUnicode functions incorrectly accept
                        │      │                   Punycode-encoded labels that decode to an ASCII-only label.
                        │      │                   For example, ToUnicode("xn--example-.com") incorrectly
                        │      │                   returns the name "example.com" rather than an error. This
                        │      │                   behavior can lead to privilege escalation in programs using
                        │      │                   the idna package. For example, a program which performs
                        │      │                   privilege checks on the ASCII hostname may reject
                        │      │                   "example.com" but permit "xn--example-.com". If that program
                        │      │                    subsequently converts the ASCII hostname to Unicode, it
                        │      │                   will inadvertently permits access to the Unicode name
                        │      │                   "example.com". 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                   
                        │      │                  ────────
                        │      │                  CWE-1289
                        │      │                  
                        │      ├ VendorSeverity   ╭ alma       : 3 
                        │      │                  ├ amazon     : 3 
                        │      │                  ├ azure      : 4 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ redhat     : 3 
                        │      │                  ├ rocky      : 3 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 8.2 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:23262             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:23264             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:26546             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:26547             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:30650             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:30651             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:30853             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:30854             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:30855             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33155             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33160             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33163             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33173             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33183             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33524             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:33531             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:34342             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:34357             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:34359             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:34364             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:34789             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35826             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35827             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35828             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35829             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35830             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35831             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35993             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:35994             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36105             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36167             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36207             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36648             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36651             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36796             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36797             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36808             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36820             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:36883             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:37387             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:37435             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:37436             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:38995             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:39005             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:39573             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:39879             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:40118             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:40262             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:40945             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41019             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41030             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41031             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41036             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41055             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41066             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41928             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:41930             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42043             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42047             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42048             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42049             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42050             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42051             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42078             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42079             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42080             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42082             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42132             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42142             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42146             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42150             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42151             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42240             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42644             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42796             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:42852             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:43038             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:43052             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:43692             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:44622             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:44624             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:46395             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:47149             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:47735             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:47737             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:47952             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:50300             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:50843             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:51033             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:51112             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:51187             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:51194             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:51341             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:52826             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:53374             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:53412             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:53413             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:53415             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:53530             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54191             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54274             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54283             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54284             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54285             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54286             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54287             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54395             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54401             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54435             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54441             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54531             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54580             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54757             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:56143             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:56223             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:56340             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:56431             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57194             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57541             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-39821        
                        │      │                  https://bugzilla.redhat.com/2480756                          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480756          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2498152          
                        │      │                  https://creativecommons.org/licenses/by/4.0/                 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39821
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39822
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-37435.html          
                        │      │                  https://errata.rockylinux.org/RLSA-2026:37435                
                        │      │                  https://github.com/golang/go/issues/78760                    
                        │      │                  https://go.dev/cl/767220                                     
                        │      │                  https://go.dev/issue/78760                                   
                        │      │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                        │      │                  https://groups.google.com/g/golang-announce/c/iI-mYSI0lu8    
                        │      │                  https://linux.oracle.com/cve/CVE-2026-39821.html             
                        │      │                  https://linux.oracle.com/errata/ELSA-2026-46395.html         
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-39821              
                        │      │                  https://pkg.go.dev/vuln/GO-2026-5026                         
                        │      │                  https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-
                        │      │                  2026-39821.json                                              
                        │      │                  https://ubuntu.com/security/notices/USN-8416-1               
                        │      │                                                                               
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-39821              
                        │      │                                                                               
                        │      │                  
                        │      ├ PublishedDate   : 2026-05-22T16:16:20.41Z 
                        │      ╰ LastModifiedDate: 2026-08-24T13:18:22.547Z 
                        ├ [14] ╭ VulnerabilityID : CVE-2026-39822 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-4970
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.4 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.4 
                        │      │                  ╰ UID : 364846ec8fe81bdc 
                        │      ├ InstalledVersion: v1.26.4 
                        │      ├ FixedVersion    : 1.25.12, 1.26.5, 1.27.0-rc.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-39822 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:b950101fb2df766a35f37c23f79539feca4c0f5bed5fb6ec35736
                        │      │                   5cba131f31d 
                        │      ├ Title           : golang: Go os.Root: Symlink following vulnerability allows
                        │      │                   directory traversal 
                        │      ├ Description     : On Unix systems, opening a file in an os.Root improperly
                        │      │                   follows symlinks to locations outside of the Root when the
                        │      │                   final path component of the a path is a symbolic link and
                        │      │                   the path ends in /. For example, 'root.Open("symlink/")'
                        │      │                   will open "symlink" even when "symlink" is a symbolic link
                        │      │                   pointing outside of the root. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                 
                        │      │                  ──────
                        │      │                  CWE-61
                        │      │                  
                        │      ├ VendorSeverity   ╭ alma       : 3 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ azure      : 3 
                        │      │                  ├ bitnami    : 3 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ photon     : 3 
                        │      │                  ├ redhat     : 3 
                        │      │                  ╰ rocky      : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:
                        │      │                  │         │           H/A:H 
                        │      │                  │         ╰ V3Score : 7.8 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:
                        │      │                            │           H/A:H 
                        │      │                            ╰ V3Score : 7.8 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:38878             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-39822        
                        │      │                  https://bugzilla.redhat.com/2498152                          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2498152          
                        │      │                  https://creativecommons.org/licenses/by/4.0/                 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39822
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-38878.html          
                        │      │                  https://errata.rockylinux.org/RLSA-2026:38878                
                        │      │                  https://go.dev/cl/797880                                     
                        │      │                  https://go.dev/issue/79005                                   
                        │      │                  https://groups.google.com/g/golang-announce/c/OrmQE_Yp5Sc    
                        │      │                  https://linux.oracle.com/cve/CVE-2026-39822.html             
                        │      │                  https://linux.oracle.com/errata/ELSA-2026-38995.html         
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-39822              
                        │      │                  https://pkg.go.dev/vuln/GO-2026-4970                         
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-39822              
                        │      │                  
                        │      ├ PublishedDate   : 2026-07-08T17:17:21.31Z 
                        │      ╰ LastModifiedDate: 2026-07-13T14:54:26.317Z 
                        ├ [15] ╭ VulnerabilityID : CVE-2026-46600 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-5942
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.4 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.4 
                        │      │                  ╰ UID : 364846ec8fe81bdc 
                        │      ├ InstalledVersion: v1.26.4 
                        │      ├ FixedVersion    : 1.26.6, 1.27.0-rc.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46600 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:15b00906fb9b8599ae791f7aa007546bf383bbbfc46870c3bf8d8
                        │      │                   c06b015764d 
                        │      ├ Title           : golang.org/x/net/dns/dnsmessage:
                        │      │                   golang.org/x/net/dns/dnsmessage: Denial of Service via
                        │      │                   invalid DNS record parsing 
                        │      ├ Description     : Parsing an invalid SVCB or HTTPS RR can panic when the size
                        │      │                   of a parameter value overflows the message buffer. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-125
                        │      │                  
                        │      ├ VendorSeverity   ╭ azure  : 2 
                        │      │                  ├ bitnami: 3 
                        │      │                  ╰ redhat : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-46600    
                        │      │                  https://go.dev/cl/786345                                 
                        │      │                  https://go.dev/issue/79795                               
                        │      │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-46600          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-5942                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-46600          
                        │      │                  
                        │      ├ PublishedDate   : 2026-07-21T20:17:01.213Z 
                        │      ╰ LastModifiedDate: 2026-08-14T16:16:55.673Z 
                        ├ [16] ╭ VulnerabilityID : CVE-2026-56853 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6089
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.4 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.4 
                        │      │                  ╰ UID : 364846ec8fe81bdc 
                        │      ├ InstalledVersion: v1.26.4 
                        │      ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56853 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:61d8a76f04e290a66edf6484dcad2c5f16a7ebf8dc783982ab54f
                        │      │                   5059e872017 
                        │      ├ Title           : net/http: golang: Go net/http: Unencrypted HTTP/2
                        │      │                   connections vulnerable to Denial of Service 
                        │      ├ Description     : When a server is configured to support unencrypted HTTP/2,
                        │      │                   it reads a few bytes from each new connection to see if they
                        │      │                    contain the HTTP/2 client preface. ReadHeaderTimeout is
                        │      │                   unexpectedly not being applied when doing this. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-770
                        │      │                  
                        │      ├ VendorSeverity   ╭ bitnami: 3 
                        │      │                  ╰ redhat : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56853    
                        │      │                  https://go.dev/cl/795540                                 
                        │      │                  https://go.dev/issue/80205                               
                        │      │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56853          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6089                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56853          
                        │      │                  
                        │      ├ PublishedDate   : 2026-08-13T22:17:22.093Z 
                        │      ╰ LastModifiedDate: 2026-08-14T16:16:57.21Z 
                        ├ [17] ╭ VulnerabilityID : CVE-2026-56858 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6091
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.4 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.4 
                        │      │                  ╰ UID : 364846ec8fe81bdc 
                        │      ├ InstalledVersion: v1.26.4 
                        │      ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56858 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:0ce2a4f805c2f42a225a5b970154918a22d1aafa5bd54514f6b58
                        │      │                   4e5d8519aed 
                        │      ├ Title           : html/template: golang: Go html/template: Cross-Site
                        │      │                   Scripting via pathological input 
                        │      ├ Description     : Previously, pathological inputs could close an unescaped '/'
                        │      │                    early, allowing for attack-controlled data to inject
                        │      │                   arbitrary content, potentially leading to XSS. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                 
                        │      │                  ──────
                        │      │                  CWE-79
                        │      │                  
                        │      ├ VendorSeverity   ╭ bitnami: 2 
                        │      │                  ╰ redhat : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:
                        │      │                  │         │           L/A:N 
                        │      │                  │         ╰ V3Score : 6.1 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:
                        │      │                            │           H/A:N 
                        │      │                            ╰ V3Score : 8.1 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56858    
                        │      │                  https://go.dev/cl/807100                                 
                        │      │                  https://go.dev/issue/80435                               
                        │      │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56858          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6091                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56858          
                        │      │                  
                        │      ├ PublishedDate   : 2026-08-13T22:17:22.207Z 
                        │      ╰ LastModifiedDate: 2026-08-14T16:16:57.367Z 
                        ├ [18] ╭ VulnerabilityID : CVE-2026-56859 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6088
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.4 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.4 
                        │      │                  ╰ UID : 364846ec8fe81bdc 
                        │      ├ InstalledVersion: v1.26.4 
                        │      ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56859 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:cfe2c3f7d2dc7f54867c665f85636a48cf96e4c06ef2e43dd2c42
                        │      │                   2f0825e7603 
                        │      ├ Title           : encoding/xml: golang: Go: Denial of Service via XML decoding
                        │      │                    recursion depth issue 
                        │      ├ Description     : Previously, DecodeElement would reset the depth counter
                        │      │                   causing it to never fire; this could lead to stack
                        │      │                   exhaustion. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-770
                        │      │                  
                        │      ├ VendorSeverity   ╭ bitnami: 3 
                        │      │                  ╰ redhat : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56859    
                        │      │                  https://go.dev/cl/803320                                 
                        │      │                  https://go.dev/issue/80481                               
                        │      │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56859          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6088                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56859          
                        │      │                  
                        │      ├ PublishedDate   : 2026-08-13T22:17:22.32Z 
                        │      ╰ LastModifiedDate: 2026-08-14T16:16:57.523Z 
                        ├ [19] ╭ VulnerabilityID : CVE-2026-56860 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6218
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.4 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.4 
                        │      │                  ╰ UID : 364846ec8fe81bdc 
                        │      ├ InstalledVersion: v1.26.4 
                        │      ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56860 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:1c1e628dbeb088327d9cda04c7b806db9c6da5c8a2d7d9c38059c
                        │      │                   e4f52e473e0 
                        │      ├ Title           : net/url: golang: golang net/url: Denial of Service from
                        │      │                   quadratic complexity in path resolution 
                        │      ├ Description     : Previously, resolving relative paths containing parent
                        │      │                   directory ('..') segments performed string conversions and
                        │      │                   buffer rewrites on each step, resulting in quadratic time
                        │      │                   complexity and high memory allocation overhead. Now, path
                        │      │                   resolution operates on a byte buffer using index-based
                        │      │                   backtracking for '..' segments, eliminating the quadratic
                        │      │                   time complexity and significantly reducing memory
                        │      │                   allocations. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-407
                        │      │                  
                        │      ├ VendorSeverity   ╭ bitnami: 2 
                        │      │                  ╰ redhat : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 5.9 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56860    
                        │      │                  https://go.dev/cl/803681                                 
                        │      │                  https://go.dev/issue/80494                               
                        │      │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56860          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6218                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56860          
                        │      │                  
                        │      ├ PublishedDate   : 2026-08-13T22:17:22.44Z 
                        │      ╰ LastModifiedDate: 2026-08-14T17:19:13.91Z 
                        ├ [20] ╭ VulnerabilityID : CVE-2026-56862 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6090
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.4 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.4 
                        │      │                  ╰ UID : 364846ec8fe81bdc 
                        │      ├ InstalledVersion: v1.26.4 
                        │      ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                        │      │                  │         3cff84dcfa0a255f209e 
                        │      │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                        │      │                            9e194f8c4780e1e1a63d 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56862 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:0c7507f419d2ff05252dd8bf07f0a50336ab1700bf238c9a6de7b
                        │      │                   b8a4c701c02 
                        │      ├ Title           : crypto/tls: golang: Golang crypto/tls: Denial of Service via
                        │      │                    indefinite KeyUpdate messages 
                        │      ├ Description     : Handshake messages, such as KeyUpdate, are always considered
                        │      │                    as state-advancing, regardless of whether a handshake has
                        │      │                   been completed or not. As a result, a malicious client can
                        │      │                   keep sending KeyUpdate messages to force the server to keep
                        │      │                   performing key derivation operations indefinitely. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-770
                        │      │                  
                        │      ├ VendorSeverity   ╭ bitnami: 3 
                        │      │                  ╰ redhat : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56862    
                        │      │                  https://go.dev/cl/804261                                 
                        │      │                  https://go.dev/issue/80528                               
                        │      │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56862          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6090                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56862          
                        │      │                  
                        │      ├ PublishedDate   : 2026-08-13T22:17:22.55Z 
                        │      ╰ LastModifiedDate: 2026-08-14T16:16:57.717Z 
                        ╰ [21] ╭ VulnerabilityID : CVE-2026-42505 
                               ├ VendorIDs                    
                               │                  ────────────
                               │                  GO-2026-5856
                               │                  
                               ├ PkgID           : stdlib@v1.26.4 
                               ├ PkgName         : stdlib 
                               ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.4 
                               │                  ╰ UID : 364846ec8fe81bdc 
                               ├ InstalledVersion: v1.26.4 
                               ├ FixedVersion    : 1.25.12, 1.26.5, 1.27.0-rc.2 
                               ├ Status          : fixed 
                               ├ Layer            ╭ Digest: sha256:26448373a8d4fbcc063b054f5ec837804b73411e93a1
                               │                  │         3cff84dcfa0a255f209e 
                               │                  ╰ DiffID: sha256:b88975a5f247334b2c31281a6b73fda4105784701f25
                               │                            9e194f8c4780e1e1a63d 
                               ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42505 
                               ├ DataSource       ╭ ID  : govulndb 
                               │                  ├ Name: The Go Vulnerability Database 
                               │                  ╰ URL : https://pkg.go.dev/vuln/ 
                               ├ Fingerprint     : sha256:016e203b19f9492e91dd1cfa1880191142261454bbc0f2b0d2cf6
                               │                   b05d807f70c 
                               ├ Title           : crypto/tls: golang: Go crypto/tls: Information disclosure in
                               │                    Encrypted Client Hello 
                               ├ Description     : Handshakes which used Encrypted Client Hello could be
                               │                   de-anonymized by a passive network observer due to a
                               │                   disclosure of pre-shared key identities in the unencrypted
                               │                   client hello. 
                               ├ Severity        : MEDIUM 
                               ├ CweIDs                  
                               │                  ───────
                               │                  CWE-201
                               │                  
                               ├ VendorSeverity   ╭ alma   : 3 
                               │                  ├ amazon : 2 
                               │                  ├ azure  : 2 
                               │                  ├ bitnami: 2 
                               │                  ├ photon : 2 
                               │                  ╰ redhat : 2 
                               ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
                               │                  │         │           N/A:N 
                               │                  │         ╰ V3Score : 5.3 
                               │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
                               │                            │           N/A:N 
                               │                            ╰ V3Score : 5.3 
                               ├ References                                                                
                               │                  ─────────────────────────────────────────────────────────
                               │                  https://access.redhat.com/errata/RHSA-2026:37435         
                               │                  https://access.redhat.com/security/cve/CVE-2026-42505    
                               │                  https://bugzilla.redhat.com/2480756                      
                               │                  https://errata.almalinux.org/9/ALSA-2026-37435.html      
                               │                  https://go.dev/cl/775960                                 
                               │                  https://go.dev/issue/79282                               
                               │                  https://groups.google.com/g/golang-announce/c/OrmQE_Yp5Sc
                               │                  https://nvd.nist.gov/vuln/detail/CVE-2026-42505          
                               │                  https://pkg.go.dev/vuln/GO-2026-5856                     
                               │                  https://www.cve.org/CVERecord?id=CVE-2026-42505          
                               │                  
                               ├ PublishedDate   : 2026-07-08T17:17:21.497Z 
                               ╰ LastModifiedDate: 2026-07-13T17:05:36.303Z 
```
