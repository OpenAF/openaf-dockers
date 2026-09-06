```yaml
╭ [0] ╭ Target         : openaf/pyoaf:edge (alpine 3.24.1) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-13608 
│                       │      ├ PkgID           : curl@8.21.0-r0 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.21.0-r0?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : eec4901c65f38f5a 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13608 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:3ac5d8a97116c14a2df1554c5e1a299eb440768ee900c4bba05e3
│                       │      │                   468c667d568 
│                       │      ├ Title           : [Unknown description] 
│                       │      ├ Description     : [Unknown description] 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-18924 
│                       │      ├ PkgID           : curl@8.21.0-r0 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.21.0-r0?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : eec4901c65f38f5a 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18924 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e35b0af4da2d1c6abe7ac79808f74bbef7d81d661c3b80df74c62
│                       │      │                   ce22bc62891 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : Description Not Available 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-19931 
│                       │      ├ PkgID           : curl@8.21.0-r0 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.21.0-r0?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : eec4901c65f38f5a 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-19931 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:31d42cadaa7be04452cdf7f59b1cc0cf64655895897f670eca18b
│                       │      │                   7ae7d9abf27 
│                       │      ├ Title           : CVE-2026-19931 
│                       │      ├ Description     : A flaw in libcurl makes it wrongly reuse an HTTP connection
│                       │      │                   setup for a given hostname using Negotiate authentication,
│                       │      │                   when the initial request is done using empty credentials.
│                       │      │                   This can make user B's request get sent over user A's
│                       │      │                   previously authenticated connection. 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-80229 
│                       │      ├ PkgID           : curl@8.21.0-r0 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.21.0-r0?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : eec4901c65f38f5a 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80229 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:831dfe781fe51febf04e30a7c49aaed2de948f2b33447be2c780e
│                       │      │                   c7de9b766bc 
│                       │      ├ Title           : [Unknown description] 
│                       │      ├ Description     : [Unknown description] 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-80230 
│                       │      ├ PkgID           : curl@8.21.0-r0 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.21.0-r0?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : eec4901c65f38f5a 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80230 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:b1891073267c530b6ce907bb77a8e1671b18656f48aafba92ecb4
│                       │      │                   c60715c0950 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : Description Not Available 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-80231 
│                       │      ├ PkgID           : curl@8.21.0-r0 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.21.0-r0?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : eec4901c65f38f5a 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80231 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:a9a26d18115e955b7337f77a5e037903caf1af04de570bddda932
│                       │      │                   b9f637b5188 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : Description Not Available 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-80255 
│                       │      ├ PkgID           : curl@8.21.0-r0 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.21.0-r0?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : eec4901c65f38f5a 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80255 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:6dcfa50fb91b710f9caa07bd44d67e61db33589d85c86fc9a0675
│                       │      │                   a157c707138 
│                       │      ├ Title           : [Unknown description] 
│                       │      ├ Description     : [Unknown description] 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-80256 
│                       │      ├ PkgID           : curl@8.21.0-r0 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.21.0-r0?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : eec4901c65f38f5a 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:79e84e061598409d5fd3c6f1c7f07387b4e37937fb0b6206050c3
│                       │      │                   f735c16c94f 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-82208 
│                       │      ├ PkgID           : curl@8.21.0-r0 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.21.0-r0?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : eec4901c65f38f5a 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-82208 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:1aa5bdcadb1cfa9a648f077311df6e45858bd191bb395cbe9f2ce
│                       │      │                   e610dfd0a0b 
│                       │      ├ Title           : [Unknown description] 
│                       │      ├ Description     : [Unknown description] 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-82209 
│                       │      ├ PkgID           : curl@8.21.0-r0 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.21.0-r0?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : eec4901c65f38f5a 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-82209 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:b9c42d599faaed4530ee7085e7c8774c8f1b4bf54563a1566b56a
│                       │      │                   958895add3a 
│                       │      ├ Title           : domain-scoped PSL domain cookie 
│                       │      ├ Description     : When libpsl support is enabled, libcurl fails to enforce the
│                       │      │                    Public Suffix List boundary check when processing a
│                       │      │                   `Set-Cookie` header where the `Domain` attribute explicitly
│                       │      │                   matches an origin host that is itself a public suffix (e.g.,
│                       │      │                    `Domain=co.uk` set by `co.uk`). Instead of coercing it into
│                       │      │                    a strict host-only cookie, libcurl saves the cookie with
│                       │      │                   wildcard domain scope (`.co.uk`). Consequently, the cookie
│                       │      │                   is inappropriately included in subsequent outbound requests
│                       │      │                   or HTTP redirects to arbitrary sibling subdomains under the
│                       │      │                   same public suffix (e.g., `attacker.co.uk`). 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-26740 
│                       │      ├ PkgID           : giflib@5.2.2-r1 
│                       │      ├ PkgName         : giflib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/giflib@5.2.2-r1?arch=x86_64&distro=3.2
│                       │      │                  │       4.1 
│                       │      │                  ╰ UID : 82fb7ad92099da32 
│                       │      ├ InstalledVersion: 5.2.2-r1 
│                       │      ├ FixedVersion    : 5.2.2-r2 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-26740 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:6015ff1dcefbd96b641137d26a2a9d6f56fb846d91200db72db74
│                       │      │                   93e36c7facc 
│                       │      ├ Title           : giflib: giflib: Denial of Service via buffer overflow in
│                       │      │                   EGifGCBToExtension 
│                       │      ├ Description     : Buffer Overflow vulnerability in giflib v.5.2.2 allows a
│                       │      │                   remote attacker to cause a denial of service via the
│                       │      │                   EGifGCBToExtension overwriting an existing Graphic Control
│                       │      │                   Extension block without validating its allocated size. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-787
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ julia      : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 8.2 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:33447             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:33450             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:33451             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:33452             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:33455             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:33456             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:33501             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:33502             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:33503             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:33509             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:36004             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:36005             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:36006             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:9683              
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:9686              
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:9689              
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:9693              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-26740        
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2448747          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-26740
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-9693.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:33501                
│                       │      │                  https://github.com/zakkanijia/POC/blob/main/giflib/giftool/gi
│                       │      │                  flib_giftool_gce_len_heap_oobwrite_disclosure.md             
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-26740.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-9693.html          
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-26740              
│                       │      │                                                                               
│                       │      │                  https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-
│                       │      │                  2026-26740.json                                              
│                       │      │                  https://ubuntu.com/security/notices/USN-8583-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-26740              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-03-18T18:16:26.22Z 
│                       │      ╰ LastModifiedDate: 2026-07-23T12:17:15.66Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-14456 
│                       │      ├ PkgID           : libcrypto3@3.5.7-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.7-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.1 
│                       │      │                  ╰ UID : 9ce2cdb3f0bf014b 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-14456 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:9eaa577ddd61dc0758780cfafae66a29ff191b47fbd58c61309ef
│                       │      │                   ccb91448d62 
│                       │      ├ Title           : openssl: OpenSSL: Denial of Service via unbounded memory
│                       │      │                   growth in QUIC server 
│                       │      ├ Description     : Issue summary: When an OpenSSL QUIC server (Listener SSL
│                       │      │                   object) processes
│                       │      │                   valid QUIC Initial packets for unknown destination
│                       │      │                   connection IDs, it
│                       │      │                   can allocate and queue new incoming channels without
│                       │      │                   enforcing any limit.
│                       │      │                   
│                       │      │                   Impact summary: A remote peer that can make many Initial
│                       │      │                   packets reach the
│                       │      │                   server listener faster than the application accepts
│                       │      │                   connections, can cause the
│                       │      │                   memory allocated to store the per-channel state to grow
│                       │      │                   without any limits,
│                       │      │                   potentially making the QUIC listener unavailable and causing
│                       │      │                    Denial of Service.
│                       │      │                   CWE: CWE-770: Allocation of Resources Without Limits or
│                       │      │                   Throttling
│                       │      │                   Description: The function that handles inbound QUIC packets
│                       │      │                   uses
│                       │      │                   Connection-Id from the packet header to find an existing
│                       │      │                   connection
│                       │      │                   (QUIC channel). If no existing connection is found and the
│                       │      │                   packet
│                       │      │                   type is INITIAL, the function treats the packet as a new
│                       │      │                   connection. It
│                       │      │                   allocates a new channel object and inserts it into a queue
│                       │      │                   where it
│                       │      │                   waits to be accepted by the local application with
│                       │      │                   SSL_accept(3ossl).
│                       │      │                   The memory occupied by these initial channel objects may
│                       │      │                   grow
│                       │      │                   without bounds if the application is not able to call
│                       │      │                   SSL_accept()
│                       │      │                   frequently enough to serve these inbound connection
│                       │      │                   requests.
│                       │      │                   The issue is present since OpenSSL 3.5 when the QUIC server
│                       │      │                   implementation
│                       │      │                   was added.
│                       │      │                   The fix introduces a limit for pending connections. The
│                       │      │                   default limit is set
│                       │      │                   to 256 pending connections (waiting to be accepted by the
│                       │      │                   local application).
│                       │      │                   Applications may change the default by calling
│                       │      │                   SSL_set_value_uint(3ossl).
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS module is not affected as the QUIC implementation
│                       │      │                   is outside of
│                       │      │                   the OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-770
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ photon: 3 
│                       │      │                  ├ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/08/13/4      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-14456        
│                       │      │                  https://github.com/openssl/openssl/commit/08e7756c3900bcfd77a
│                       │      │                  720e7b74e27d6e4ed01a9                                        
│                       │      │                  https://github.com/openssl/openssl/commit/4084152e040329ca019
│                       │      │                  4c4c1750b9b46d00a5b6b                                        
│                       │      │                  https://github.com/openssl/openssl/commit/f2f1465f2d2e5c61dfe
│                       │      │                  ac4d20fd093797d821139                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-14456              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260813.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-14456              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-13T15:19:31.82Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-18798 
│                       │      ├ PkgID           : libcrypto3@3.5.7-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.7-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.1 
│                       │      │                  ╰ UID : 9ce2cdb3f0bf014b 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18798 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:bb5dc397cd05d4b4b5b76046eafc43006ac31564b98b97bb1ef7f
│                       │      │                   e170178c913 
│                       │      ├ Title           : openssl: QUIC server may trigger double free when processing
│                       │      │                    INITIAL packet 
│                       │      ├ Description     : Issue summary: QUIC server may double free QRX (QUIC record
│                       │      │                   layer RX) object
│                       │      │                   when channel creation fails for initial packet.
│                       │      │                   
│                       │      │                   Impact summary: Double free leads to heap corruption, which
│                       │      │                   typically results in 
│                       │      │                   termination of QUIC server process, leading to Denial of
│                       │      │                   Service. There is so
│                       │      │                   far no evidence that this double free is exploitable for
│                       │      │                   remote code execution,
│                       │      │                   thus it is considered highly improbable.
│                       │      │                   CWE: CWE-415: Double Free
│                       │      │                   Description: In order to validate initial packet, OpenSSL
│                       │      │                   QUIC stack default
│                       │      │                   packet handler (port_default_packet_handler()) creates a
│                       │      │                   so-called QRX object.
│                       │      │                   If the initial packet validates successfully with QRX
│                       │      │                   object, the default packet
│                       │      │                   handler proceeds to channel (connection object) creation.
│                       │      │                   The QRX object used
│                       │      │                   for packet validation is passed to port_bind_channel(), so
│                       │      │                   it becomes part of
│                       │      │                   the newly created connection. If port_bind_channel() fails,
│                       │      │                   then it also frees
│                       │      │                   the QRX object. Once port_bind_channel() returns, the
│                       │      │                   port_default_packet_handler()
│                       │      │                   detects the failure and proceeds to the error branch, where
│                       │      │                   the same QRX object is
│                       │      │                   freed for the second time.
│                       │      │                   The failure in port_bind_channel() function can be induced
│                       │      │                   with a relatively
│                       │      │                   low effort by a malformed (non RFC 9000 compliant) INITIAL
│                       │      │                   packet. If the packet
│                       │      │                   carries DCID (destination connection ID) which is shorter
│                       │      │                   than 8 bytes, then
│                       │      │                   port_bind_channel() jumps to the error path after
│                       │      │                   ossl_quic_lcidm_enrol_odcid()
│                       │      │                   detects that the DCID has invalid length.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS module is not affected, as the QUIC implementation
│                       │      │                   is outside of
│                       │      │                   the OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-415
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18798        
│                       │      │                  https://github.com/openssl/openssl/commit/70cebd74d3592f52729
│                       │      │                  45501b58a60374c4e13af                                        
│                       │      │                  https://github.com/openssl/openssl/commit/967582d5037f01a26b6
│                       │      │                  d19beae19af62a1b15c3c                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a14a1deac403522fbea
│                       │      │                  fabcb198503cf6caa7dc4                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18798              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18798              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:17:49.813Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-63072 
│                       │      ├ PkgID           : libcrypto3@3.5.7-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.7-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.1 
│                       │      │                  ╰ UID : 9ce2cdb3f0bf014b 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63072 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:02ca209b3249a97f3d5326130141475a5eaf5c5eee267cd6f4d56
│                       │      │                   ffa0f40f860 
│                       │      ├ Title           : openssl: heap buffer overflow in CMS key unwrapping 
│                       │      ├ Description     : Issue summary: OpenSSL CMS decryption sizes the key-unwrap
│                       │      │                   output buffer based
│                       │      │                   on querying the unwrapped key size, but the AES-WRAP-PAD
│                       │      │                   unwrap primitive
│                       │      │                   can write and cleanse more bytes than that query reports,
│                       │      │                   causing an 8-byte
│                       │      │                   out-of-bounds heap write.
│                       │      │                   
│                       │      │                   Impact summary: An attacker who supplies a crafted CMS
│                       │      │                   message can trigger a
│                       │      │                   deterministic 8-byte out-of-bounds heap write when the
│                       │      │                   victim decrypts it
│                       │      │                   with CMS_decrypt(), corrupting the heap and typically
│                       │      │                   resulting in a Denial
│                       │      │                   of Service.
│                       │      │                   CWE: CWE-787: Out-of-bounds Write
│                       │      │                   Description: The key-wrap OID is potentially
│                       │      │                   attacker-controlled on the wire.
│                       │      │                   CMS unwrapping allows both id-aesNNN-wrap-pad and
│                       │      │                   id-aesNNN-wrap ciphers.
│                       │      │                   An attacker can take a legitimate message and change a
│                       │      │                   single OID byte to
│                       │      │                   select the padded variant while leaving the message
│                       │      │                   otherwise valid. Since
│                       │      │                   the unwrap key is derived from the recipient's private
│                       │      │                   operation (ECDH key
│                       │      │                   agreement or ML-KEM decapsulation), the RFC 5649 integrity
│                       │      │                   check cannot
│                       │      │                   pass, and the decryption fails with integrity failure.
│                       │      │                   The write is a fixed-size (8-byte), fixed-value (zero) heap
│                       │      │                   overflow
│                       │      │                   immediately past the allocation, requires no special
│                       │      │                   configuration, and is
│                       │      │                   reachable from the public CMS_decrypt() function. The
│                       │      │                   consequence is
│                       │      │                   a heap corruption leading to a Denial of Service. The fix in
│                       │      │                    the CMS code
│                       │      │                   sizes the unwrap output buffer for the worst case so a
│                       │      │                   failed unwrap cannot
│                       │      │                   write past the allocation.
│                       │      │                   FIPS impact: no
│                       │      │                   As the CMS code lives outside the FIPS module boundary, no
│                       │      │                   FIPS
│                       │      │                   modules are affected by this CVE. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-787
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63072        
│                       │      │                  https://github.com/openssl/openssl/commit/2a3dac874c8057c1f01
│                       │      │                  86849bf1ede1ae7b6b756                                        
│                       │      │                  https://github.com/openssl/openssl/commit/87784ad619af36b8807
│                       │      │                  c2044b3940006fccc1e42                                        
│                       │      │                  https://github.com/openssl/openssl/commit/9530a5fd1aacaeccdce
│                       │      │                  d4478ea2340a480613335                                        
│                       │      │                  https://github.com/openssl/openssl/commit/9ec2f6d2ae2bcad907c
│                       │      │                  f7ee38584855bafe4979a                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a0c8ec557d9cac078f0
│                       │      │                  32d76cdf684fe743eb382                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63072              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63072              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.01Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-63076 
│                       │      ├ PkgID           : libcrypto3@3.5.7-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.7-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.1 
│                       │      │                  ╰ UID : 9ce2cdb3f0bf014b 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63076 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e74381cf39e2403858f81a2d60290f160910b12bcb16fe35dff08
│                       │      │                   66fca271d85 
│                       │      ├ Title           : openssl: invalid pointer dereference in CMP server via
│                       │      │                   crafted protectionAlg 
│                       │      ├ Description     : Issue summary: OpenSSL CMP password based protection
│                       │      │                   verification only
│                       │      │                   checks whether the protectionAlg parameter was not NULL and
│                       │      │                   not its
│                       │      │                   ASN.1 type, before treating it as a PBMParameter. A crafted
│                       │      │                   message can
│                       │      │                   contain a parameter of a different type, which is then
│                       │      │                   dereferenced as an
│                       │      │                   invalid pointer.
│                       │      │                   
│                       │      │                   Impact summary: A remote, unauthenticated attacker can crash
│                       │      │                    an application
│                       │      │                   acting as a CMP server that accepts PBM-protected messages,
│                       │      │                   or a CMP client
│                       │      │                   talking to a malicious or intercepted CMP server, resulting
│                       │      │                   in a Denial of
│                       │      │                   Service.
│                       │      │                   CWE: CWE-476: NULL Pointer Dereference
│                       │      │                   Description: When verifying the password-based MAC
│                       │      │                   protection of a CMP
│                       │      │                   message, OpenSSL library reads the protectionAlg algorithm
│                       │      │                   parameter with
│                       │      │                   X509_ALGOR_get0(), which returns both the parameter type and
│                       │      │                    its value
│                       │      │                   pointer. The value is then cast to an ASN1_STRING and
│                       │      │                   treated as the
│                       │      │                   expected PBMParameter after only checking that pointer is
│                       │      │                   not NULL. The
│                       │      │                   parameter type returned by X509_ALGOR_get0() was never
│                       │      │                   consulted.
│                       │      │                   This happens during protection verification, before any MAC
│                       │      │                   is computed, so
│                       │      │                   no knowledge of the PBM shared secret is required; the only
│                       │      │                   precondition is
│                       │      │                   that PBM verification is reachable. On the server side this
│                       │      │                   is reached from
│                       │      │                   OSSL_CMP_SRV_process_request() for any application that
│                       │      │                   stands up a CMP
│                       │      │                   server accepting PBM-protected messages, and on the client
│                       │      │                   side from CMP
│                       │      │                   response validation against a malicious or on-path (MITM)
│                       │      │                   server. The
│                       │      │                   reliable consequence is a denial of service; there is no
│                       │      │                   memory disclosure,
│                       │      │                   no controlled memory write, and no path to code execution.
│                       │      │                   CMP is a
│                       │      │                   specialized feature that an application must explicitly
│                       │      │                   enable.
│                       │      │                   FIPS impact: no
│                       │      │                   As the CMP code lives outside the FIPS module boundary, no
│                       │      │                   FIPS modules
│                       │      │                   are affected by this CVE. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-476
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63076        
│                       │      │                  https://github.com/openssl/openssl/commit/37882aa2e0256e10724
│                       │      │                  42a8f62f7db45b995c45b                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a17cc8d612ecff6d94a
│                       │      │                  9b7ca8b5283ddf5ff570e                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a1f348ccb328c3afbd4
│                       │      │                  ba6883f9b7c813c043259                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a7af46a92d0ce19a90e
│                       │      │                  669ef56d2576a07924226                                        
│                       │      │                  https://github.com/openssl/openssl/commit/cdacfff557389abfa9e
│                       │      │                  4615abded2ec984517d6c                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63076              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63076              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.543Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-14457 
│                       │      ├ PkgID           : libcrypto3@3.5.7-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.7-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.1 
│                       │      │                  ╰ UID : 9ce2cdb3f0bf014b 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-14457 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:232a09eaa8ba9bc9c991463a59d31e28797604f0e534b06ae838e
│                       │      │                   298d523121a 
│                       │      ├ Title           : openssl: RPK server signature algorithm selection can
│                       │      │                   dereference a missing certificate 
│                       │      ├ Description     : Issue summary: In a server or client configuration with
│                       │      │                   RFC7250 Raw Public Keys (RPKs)
│                       │      │                   enabled, and only the private key (with no associated
│                       │      │                   certificate) configured locally,
│                       │      │                   a NULL pointer dereference may occur when the remote peer
│                       │      │                   solicits raw public keys and
│                       │      │                   also sends the typically omitted "signature_algorithms_cert"
│                       │      │                    TLS extension.
│                       │      │                   
│                       │      │                   Impact summary: The impact is limited to a possible Denial
│                       │      │                   of Service as a result of
│                       │      │                   an application abort, no data disclosure or remote command
│                       │      │                   execution are possible.
│                       │      │                   CWE: CWE-476: NULL Pointer Dereference
│                       │      │                   Description: While a passing comment in sample code in the
│                       │      │                   documentation suggests
│                       │      │                   that key-only RPK configurations are supported, the
│                       │      │                   best-practice RPK configuration
│                       │      │                   is to always configure a corresponding certificate (possibly
│                       │      │                    self-signed or
│                       │      │                   signed by any convenient CA).
│                       │      │                   When the private key is configured along with a matching
│                       │      │                   certificate, the
│                       │      │                   "signature_algorithms_cert" extension is handled reliably
│                       │      │                   even without the
│                       │      │                   fix, and peer clients or servers that don't support raw
│                       │      │                   public keys may be
│                       │      │                   able to complete a TLS connection by pinning or verifying
│                       │      │                   the corresponding
│                       │      │                   certificate or its public key.
│                       │      │                   Deployments that prefer to configure just a private key with
│                       │      │                    no certificate
│                       │      │                   need to upgrade to an updated release as noted below.
│                       │      │                   FIPS impact: no
│                       │      │                   No FIPS modules are affected by this issue, as the SSL
│                       │      │                   protocol implementation
│                       │      │                   is outside the OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-476
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-14457        
│                       │      │                  https://github.com/openssl/openssl/commit/1e8c398db67404babd3
│                       │      │                  e5af999bb6bd86f720c76                                        
│                       │      │                  https://github.com/openssl/openssl/commit/581aaa0f0a35d214740
│                       │      │                  f0fe1f5283ec41f1212e1                                        
│                       │      │                  https://github.com/openssl/openssl/commit/d0af20478688a6aa2f5
│                       │      │                  9d61caa3f82136b181d7f                                        
│                       │      │                  https://github.com/openssl/openssl/commit/dad836b071da6579510
│                       │      │                  c968615848ba03cac593b                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-14457              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-14457              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:17:49.533Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-54874 
│                       │      ├ PkgID           : libcrypto3@3.5.7-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.7-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.1 
│                       │      │                  ╰ UID : 9ce2cdb3f0bf014b 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54874 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:b41b19cdac9f8acf499b079261cc92a10fc6ef2df3bc66ed3b19c
│                       │      │                   1294f802643 
│                       │      ├ Title           : openssl: excessive memory use buffering DTLS records for a
│                       │      │                   future epoch 
│                       │      ├ Description     : Issue summary: Receiving a DTLS record for a future epoch
│                       │      │                   while a handshake
│                       │      │                   is in progress causes OpenSSL to buffer far more memory than
│                       │      │                    the record
│                       │      │                   itself requires.
│                       │      │                   
│                       │      │                   Impact summary: A peer can use a small amount of network
│                       │      │                   traffic to make an
│                       │      │                   OpenSSL DTLS endpoint retain a disproportionately large
│                       │      │                   amount of memory,
│                       │      │                   which may lead to a Denial of Service.
│                       │      │                   CWE: CWE-405: Asymmetric Resource Consumption
│                       │      │                   (Amplification)
│                       │      │                   Description: While a DTLS handshake is in progress, a peer
│                       │      │                   may legitimately
│                       │      │                   have already moved on to the next epoch (for example, having
│                       │      │                    sent its
│                       │      │                   ChangeCipherSpec and Finished messages) before the local
│                       │      │                   endpoint has
│                       │      │                   processed the same transition, typically because of
│                       │      │                   reordering on the
│                       │      │                   underlying UDP transport. OpenSSL buffers such early records
│                       │      │                    so that they
│                       │      │                   can be processed once the local endpoint catches up.
│                       │      │                   Buffering a record currently retains the entire read buffer
│                       │      │                   it arrived in,
│                       │      │                   which is sized to hold the largest possible DTLS record
│                       │      │                   (around 16
│                       │      │                   kilobytes), rather than just the bytes that make up the
│                       │      │                   record itself. Up
│                       │      │                   to 100 such records may be buffered per connection. As a
│                       │      │                   result, a peer
│                       │      │                   that sends a stream of small forged records claiming to
│                       │      │                   belong to the next
│                       │      │                   epoch can cause an OpenSSL DTLS endpoint to retain around
│                       │      │                   1.7 megabytes of
│                       │      │                   memory, despite sending only a small fraction of that amount
│                       │      │                    of data over
│                       │      │                   the network.
│                       │      │                   An attacker therefore gains a memory amplification factor of
│                       │      │                    around 1200,
│                       │      │                   and can multiply the effect across as many associations as
│                       │      │                   it is able to
│                       │      │                   open, making this a remote memory exhaustion Denial of
│                       │      │                   Service risk for
│                       │      │                   DTLS servers. Since the memory retained per connection
│                       │      │                   remains bounded,
│                       │      │                   and any limit an application already places on the number of
│                       │      │                    concurrent
│                       │      │                   associations also bounds the total exposure, this issue has
│                       │      │                   been assessed
│                       │      │                   as Low severity.
│                       │      │                   FIPS impact: no
│                       │      │                   No FIPS modules are affected by this issue as the affected
│                       │      │                   code is outside
│                       │      │                   the OpenSSL FIPS module boundary.
│                       │      │                   OpenSSL 4.0, 3.6, 3.5, 3.4, 3.0, 1.1.1 and 1.0.2 are
│                       │      │                   vulnerable to this
│                       │      │                   issue.
│                       │      │                   OpenSSL 4.0 users should upgrade to OpenSSL 4.0.2.
│                       │      │                   OpenSSL 3.6 users should upgrade to OpenSSL 3.6.4.
│                       │      │                   OpenSSL 3.5 users should upgrade to OpenSSL 3.5.8.
│                       │      │                   OpenSSL 3.4 users should upgrade to OpenSSL 3.4.7.
│                       │      │                   OpenSSL 3.0 users should upgrade to OpenSSL 3.0.22.
│                       │      │                   Premium support customers only:
│                       │      │                   OpenSSL 1.1.1 users should upgrade to OpenSSL 1.1.1zi
│                       │      │                   OpenSSL 1.0.2 users should upgrade to OpenSSL 1.0.2zr
│                       │      │                   This issue was reported on 18 May 2026 by Amazon Web
│                       │      │                   Services.
│                       │      │                   The fix has been developed by Matt Caswell.
│                       │      │                   -- cut (non-publishing metadata for internal use) --
│                       │      │                   Reported by: Amazon Web Services
│                       │      │                   Fixed by: Matt Caswell 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-405
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-54874        
│                       │      │                  https://github.com/openssl/openssl/commit/4808b5d64176451f3d9
│                       │      │                  3d87d0ac9c81a9b13fb23                                        
│                       │      │                  https://github.com/openssl/openssl/commit/7110cb2f75806d0bf80
│                       │      │                  9eb2f90790d477900be40                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a0c8ec557d9cac078f0
│                       │      │                  32d76cdf684fe743eb382                                        
│                       │      │                  https://github.com/openssl/openssl/commit/cc0c6710917cd5eec00
│                       │      │                  1b297355d2ba723505107                                        
│                       │      │                  https://github.com/openssl/openssl/commit/f52ffc11b90737ac890
│                       │      │                  83909618dc2e1f42c561c                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-54874              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-54874              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:24.033Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2026-63073 
│                       │      ├ PkgID           : libcrypto3@3.5.7-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.7-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.1 
│                       │      │                  ╰ UID : 9ce2cdb3f0bf014b 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63073 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:a06d026dfb5193c1701ed2a1d87d1b5a6965f1d635a6b06418bef
│                       │      │                   19395cab534 
│                       │      ├ Title           : openssl: untrusted sender DN used as format string in CMP
│                       │      │                   response validation 
│                       │      ├ Description     : Issue summary: OpenSSL CMP response validation passed an
│                       │      │                   unexpected response
│                       │      │                   sender distinguished name directly as the format string to
│                       │      │                   `ERR_raise_data()`.
│                       │      │                   
│                       │      │                   Impact summary: A malicious or intercepted CMP endpoint can
│                       │      │                   crash a CMP client
│                       │      │                   that enforces an expected sender or uses a pinned server
│                       │      │                   certificate whose
│                       │      │                   subject becomes the default expected sender.
│                       │      │                   CWE: CWE-134 (Use of Externally-Controlled Format String)
│                       │      │                   Description: When validating a received CMP message,
│                       │      │                   ossl_cmp_msg_check_update()
│                       │      │                   converts the peer-supplied sender distinguished name with
│                       │      │                   X509_NAME_oneline()
│                       │      │                   and passes it directly as the format argument to
│                       │      │                   ERR_raise_data(). Percent
│                       │      │                   characters survive the conversion, so a sender DN such as
│                       │      │                   "CN=%s%n" reaches
│                       │      │                   BIO_vsnprintf() as an attacker-controlled format string with
│                       │      │                    no matching variadic
│                       │      │                   arguments. This path is only reached when the caller
│                       │      │                   configures an expected
│                       │      │                   sender or pins a server certificate, which is the normal
│                       │      │                   configuration for a
│                       │      │                   CMP client validating server responses.
│                       │      │                   Since the attacker controls the format string but none of
│                       │      │                   the variadic
│                       │      │                   arguments, such specifiers as %s and %n dereference or write
│                       │      │                    through unrelated
│                       │      │                   stack contents and crash the client. The reliable
│                       │      │                   consequence is a denial of
│                       │      │                   service, when the response comes from a malicious or
│                       │      │                   intercepted CMP endpoint.
│                       │      │                   There is no controlled memory write, arbitrary-address read,
│                       │      │                    or reliable path
│                       │      │                   to remote code execution.
│                       │      │                   FIPS impact: no
│                       │      │                   No FIPS modules are affected by this issue, as the CMP
│                       │      │                   protocol
│                       │      │                   implementation is outside the OpenSSL FIPS module
│                       │      │                   boundary. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-134
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63073        
│                       │      │                  https://github.com/openssl/openssl/commit/0cc20b322639919aa42
│                       │      │                  3e90799d9a57c3b4b76ca                                        
│                       │      │                  https://github.com/openssl/openssl/commit/6a0acc072b4d37a7cac
│                       │      │                  1252a29c1ce1f00c5ec29                                        
│                       │      │                  https://github.com/openssl/openssl/commit/7eb2e3ec9d1d4f35c80
│                       │      │                  22fccd4b03398b3f33e21                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a7e5a6eea8fd3ccca6b
│                       │      │                  6fbba031a5fbf8a3d93b4                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63073              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63073              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.147Z 
│                       │      ╰ LastModifiedDate: 2026-08-31T20:17:07.54Z 
│                       ├ [18] ╭ VulnerabilityID : CVE-2026-63074 
│                       │      ├ PkgID           : libcrypto3@3.5.7-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.7-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.1 
│                       │      │                  ╰ UID : 9ce2cdb3f0bf014b 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63074 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:064f237713c9dcd9dae15a33064605be5d14ac311bfe94f01e659
│                       │      │                   3d266e673ae 
│                       │      ├ Title           : openssl: CMP indefinite cache growth of ExtraCerts 
│                       │      ├ Description     : Issue summary: The OpenSSL Certificate Management Protocol
│                       │      │                   (CMP) caches
│                       │      │                   additional certificates (extraCerts) sent in a CMP message,
│                       │      │                   but never expunges
│                       │      │                   them (for instance if they are invalid).  If a server reuses
│                       │      │                    an OSSL_CMP_CTX
│                       │      │                   frequently, this cache of extraCerts may grow unboundedly,
│                       │      │                   and a malicious
│                       │      │                   client may flood a CMP server with requests driving this
│                       │      │                   growth.
│                       │      │                   
│                       │      │                   Impact summary: Users utilizing a CMP server that reuses a
│                       │      │                   single OSSL_CMP_CTX
│                       │      │                   for the lifetime of a server process may observe unbounded
│                       │      │                   memory growth in the
│                       │      │                   event a malicious client repeatedly sends requests
│                       │      │                   containing unique extra
│                       │      │                   certificates, which may lead to OOM conditions.
│                       │      │                   CWE: CWE-770: Allocation of Resources Without Limits or
│                       │      │                   Throttling
│                       │      │                   Description: If a remote user sends CMP messages to a server
│                       │      │                    with a list of
│                       │      │                   extraCerts and the message is rejected, the extraCerts from
│                       │      │                   the message remains
│                       │      │                   in the server contexts untrusted certificate stack.  This
│                       │      │                   exposes servers with
│                       │      │                   long lived ctx objects to Denial of Service attacks in which
│                       │      │                    an attacker sends
│                       │      │                   messages intending to be rejected with a large list of
│                       │      │                   additional certificates
│                       │      │                   repeatedly, forcing the server to store them indefinitely.
│                       │      │                      
│                       │      │                   The issue was fixed by removing the added extra certs if the
│                       │      │                    message is
│                       │      │                   rejected, using the same method as when the context is
│                       │      │                   configured to not do
│                       │      │                   caching at all.
│                       │      │                   FIPS impact: no
│                       │      │                   As the CMP code lives outside the FIPS module boundary, no
│                       │      │                   FIPS
│                       │      │                   modules are affected by this CVE. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-770
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63074        
│                       │      │                  https://github.com/openssl/openssl/commit/01e567978a55fba1814
│                       │      │                  2a230380c31296049fae7                                        
│                       │      │                  https://github.com/openssl/openssl/commit/21a5d9658b0c66daace
│                       │      │                  60e10ea18ff32a448de9f                                        
│                       │      │                  https://github.com/openssl/openssl/commit/74ae7f6df47a5767c10
│                       │      │                  10b88c47507dfc5b32c46                                        
│                       │      │                  https://github.com/openssl/openssl/commit/75360af9650d4e0c82b
│                       │      │                  a0050c5c9912cd79e54af                                        
│                       │      │                  https://github.com/openssl/openssl/commit/f636f9ca0fa1bae5b42
│                       │      │                  f9e787f025c96fb09c43a                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63074              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63074              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.283Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [19] ╭ VulnerabilityID : CVE-2026-63075 
│                       │      ├ PkgID           : libcrypto3@3.5.7-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.7-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.1 
│                       │      │                  ╰ UID : 9ce2cdb3f0bf014b 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63075 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:75aae31b4e7f04644695a3bec46f3451bfc541932bc5cbe5b56c7
│                       │      │                   2416c37487b 
│                       │      ├ Title           : openssl: QUIC ACK-only packet retention can cause memory
│                       │      │                   exhaustion 
│                       │      ├ Description     : Issue summary: When OpenSSL processes QUIC traffic from a
│                       │      │                   peer that repeatedly
│                       │      │                   sends ack-eliciting packets while not acknowledging ACK-only
│                       │      │                    responses, the
│                       │      │                   QUIC stack can retain ACK-only packet metadata for the
│                       │      │                   lifetime of the
│                       │      │                   connection.
│                       │      │                   
│                       │      │                   Impact summary: A remote peer that can complete a QUIC
│                       │      │                   handshake can
│                       │      │                   cause connection-scoped memory growth which may lead to
│                       │      │                   Denial of Service
│                       │      │                   through memory exhaustion, especially with sustained traffic
│                       │      │                    or many concurrent
│                       │      │                   QUIC connections.
│                       │      │                   CWE: CWE-770: Allocation of Resources Without Limits or
│                       │      │                   Throttling
│                       │      │                   Description: When the OpenSSL QUIC stack sends an ACK-only
│                       │      │                   packet,
│                       │      │                   there is no requirement by the QUIC protocol that the peer
│                       │      │                   will acknowledge
│                       │      │                   that ACK-only packet (i.e. it is itself not ack-eliciting).
│                       │      │                   However, the OpenSSL
│                       │      │                   implementation stores the metadata about the ACK frames
│                       │      │                   regardless.
│                       │      │                   In and of itself that's ok, but if a malicious peer
│                       │      │                   establishes a connection, and
│                       │      │                   then drives the connection such that ACK-only packets are
│                       │      │                   forced from the 
│                       │      │                   OpenSSL implementation peer (i.e., by sending numerous PING
│                       │      │                   frames),
│                       │      │                   and then withholding any subsequent acks for ack-eliciting
│                       │      │                   data, like
│                       │      │                   legitimate data, said malicious peer can force inappropriate
│                       │      │                    memory growth
│                       │      │                   on the OpenSSL peer, potentially leading to a Denial of
│                       │      │                   Service.
│                       │      │                   The fix is to ensure that we account for the transmission of
│                       │      │                    the ACK-only
│                       │      │                   packet in the packet histories high and low watermark
│                       │      │                   without actually storing
│                       │      │                   the ACK-only packet metadata itself.
│                       │      │                   FIPS impact: no
│                       │      │                   The OpenSSL FIPS module is not affected as the QUIC code is
│                       │      │                   outside the FIPS module boundary. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-770
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63075        
│                       │      │                  https://github.com/openssl/openssl/commit/7308946576b12e64b8b
│                       │      │                  e53bcf0a120354b2b42bc                                        
│                       │      │                  https://github.com/openssl/openssl/commit/7c98d79738549df9286
│                       │      │                  8e7dd9be4bbf061eed709                                        
│                       │      │                  https://github.com/openssl/openssl/commit/bf84721c2548351176e
│                       │      │                  367e6de505792f0118dc6                                        
│                       │      │                  https://github.com/openssl/openssl/commit/c902e5f16d6a9e130e9
│                       │      │                  6d3ca6d8f64d71652e393                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63075              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63075              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.413Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [20] ╭ VulnerabilityID : CVE-2026-75803 
│                       │      ├ PkgID           : libcrypto3@3.5.7-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.7-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.1 
│                       │      │                  ╰ UID : 9ce2cdb3f0bf014b 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-75803 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:9563250edef406fcca460ff2997de401351ad0e26c8401581b342
│                       │      │                   5e3a8da0458 
│                       │      ├ Title           : Issue summary: ChaCha20-Poly1305 and AES-OCB decryption with
│                       │      │                    an empty  ... 
│                       │      ├ Description     : Issue summary: ChaCha20-Poly1305 and AES-OCB decryption with
│                       │      │                    an empty
│                       │      │                   ciphertext can report success without verifying the supplied
│                       │      │                    authentication
│                       │      │                   tag when the operation is finalized by calling the
│                       │      │                   EVP_Cipher() function.
│                       │      │                   
│                       │      │                   Impact summary: Applications calling EVP_Cipher() on an
│                       │      │                   empty ciphertext and
│                       │      │                   expecting the call to check the AEAD tag may accept forged
│                       │      │                   messages.
│                       │      │                   CWE: CWE-354 (Improper Validation of Integrity Check Value)
│                       │      │                   Description: The EVP_Cipher() API call for AEAD ciphers
│                       │      │                   behaves like a one
│                       │      │                   shot encryption and decryption call. It also verifies the
│                       │      │                   AEAD tag after the
│                       │      │                   decryption operation. However for AES-OCB and
│                       │      │                   ChaCha20-Poly1305 ciphers
│                       │      │                   it skipped the AEAD tag verification when an empty
│                       │      │                   ciphertext was passed to
│                       │      │                   the function. The callers of this function might believe
│                       │      │                   that a successful
│                       │      │                   return indicates a valid AEAD tag for these ciphers, even
│                       │      │                   when that has not
│                       │      │                   truly been validated in this case.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules in 4.0, 3.6, 3.5, 3.4, and 3.0 are not
│                       │      │                   affected by this CVE
│                       │      │                   as the affected algorithms are not FIPS approved and thus
│                       │      │                   not implemented
│                       │      │                   in the FIPS module. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-354
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/openssl/openssl/commit/119ab9555dc62275bbd
│                       │      │                  71f6f49529b1a44feba42                                        
│                       │      │                  https://github.com/openssl/openssl/commit/3621257986e27e540bf
│                       │      │                  96a11570929a6e5a9e05b                                        
│                       │      │                  https://github.com/openssl/openssl/commit/6c7aa6f8f6449b7fe01
│                       │      │                  37ee8be65fcd239bd7d6a                                        
│                       │      │                  https://github.com/openssl/openssl/commit/bdeb0cd994d91534278
│                       │      │                  7f117ee75044f0dc36f34                                        
│                       │      │                  https://github.com/openssl/openssl/commit/bf95f5f772e9362f87b
│                       │      │                  25cfa2f8cb15d984865b9                                        
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-3               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-75803              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:29.57Z 
│                       │      ╰ LastModifiedDate: 2026-09-01T19:17:27.543Z 
│                       ├ [21] ╭ VulnerabilityID : CVE-2026-13608 
│                       │      ├ PkgID           : libcurl@8.21.0-r0 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.21.0-r0?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 41bd97351e4e8b71 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13608 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:6477a0cec07cc315dad5678b677e794b079faae297a6af1278e3c
│                       │      │                   c279a4f84fc 
│                       │      ├ Title           : [Unknown description] 
│                       │      ├ Description     : [Unknown description] 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [22] ╭ VulnerabilityID : CVE-2026-18924 
│                       │      ├ PkgID           : libcurl@8.21.0-r0 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.21.0-r0?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 41bd97351e4e8b71 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18924 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:fca886699cfcb4ee92be4025d3001db0d5abac9c85d247f87a192
│                       │      │                   9c4c185d4ad 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : Description Not Available 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [23] ╭ VulnerabilityID : CVE-2026-19931 
│                       │      ├ PkgID           : libcurl@8.21.0-r0 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.21.0-r0?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 41bd97351e4e8b71 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-19931 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:6f524b5da2711fbbf0571aa27dc05b31cf2484e9d40ca41c9a96e
│                       │      │                   76a97ed5307 
│                       │      ├ Title           : CVE-2026-19931 
│                       │      ├ Description     : A flaw in libcurl makes it wrongly reuse an HTTP connection
│                       │      │                   setup for a given hostname using Negotiate authentication,
│                       │      │                   when the initial request is done using empty credentials.
│                       │      │                   This can make user B's request get sent over user A's
│                       │      │                   previously authenticated connection. 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [24] ╭ VulnerabilityID : CVE-2026-80229 
│                       │      ├ PkgID           : libcurl@8.21.0-r0 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.21.0-r0?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 41bd97351e4e8b71 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80229 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:318358ca31d4a9ddc7e77840cc4cdecafe9a6814be2df79934f2f
│                       │      │                   b274e2e022a 
│                       │      ├ Title           : [Unknown description] 
│                       │      ├ Description     : [Unknown description] 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [25] ╭ VulnerabilityID : CVE-2026-80230 
│                       │      ├ PkgID           : libcurl@8.21.0-r0 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.21.0-r0?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 41bd97351e4e8b71 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80230 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:fd92ca029e4a058c71598384286380a8217e555d2e7d1bce3d05d
│                       │      │                   27d7493ce71 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : Description Not Available 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [26] ╭ VulnerabilityID : CVE-2026-80231 
│                       │      ├ PkgID           : libcurl@8.21.0-r0 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.21.0-r0?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 41bd97351e4e8b71 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80231 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:bf7cd08e8065ea3b1a8f369bce167ffd350050d47c814fe241f10
│                       │      │                   afdbb699a9b 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : Description Not Available 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [27] ╭ VulnerabilityID : CVE-2026-80255 
│                       │      ├ PkgID           : libcurl@8.21.0-r0 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.21.0-r0?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 41bd97351e4e8b71 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80255 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:98e50040138c0a636d01378e779c8a8df7ff645be1f8dcbe63976
│                       │      │                   b786788fcf8 
│                       │      ├ Title           : [Unknown description] 
│                       │      ├ Description     : [Unknown description] 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [28] ╭ VulnerabilityID : CVE-2026-80256 
│                       │      ├ PkgID           : libcurl@8.21.0-r0 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.21.0-r0?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 41bd97351e4e8b71 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:a41ec119a949d06ea5a9f2090fb263323518ca9c1bd2b3a6da3ba
│                       │      │                   277f8074dd2 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [29] ╭ VulnerabilityID : CVE-2026-82208 
│                       │      ├ PkgID           : libcurl@8.21.0-r0 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.21.0-r0?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 41bd97351e4e8b71 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-82208 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:1a93ed7648b10b16a895c9b2f7991dbd323ef5a85c61a4a56a7b4
│                       │      │                   6de5b719439 
│                       │      ├ Title           : [Unknown description] 
│                       │      ├ Description     : [Unknown description] 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [30] ╭ VulnerabilityID : CVE-2026-82209 
│                       │      ├ PkgID           : libcurl@8.21.0-r0 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.21.0-r0?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 41bd97351e4e8b71 
│                       │      ├ InstalledVersion: 8.21.0-r0 
│                       │      ├ FixedVersion    : 8.22.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-82209 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:ccbad085602c54a490e7940d89be4140a0415ebcd3e42f79647b9
│                       │      │                   62409b9cad5 
│                       │      ├ Title           : domain-scoped PSL domain cookie 
│                       │      ├ Description     : When libpsl support is enabled, libcurl fails to enforce the
│                       │      │                    Public Suffix List boundary check when processing a
│                       │      │                   `Set-Cookie` header where the `Domain` attribute explicitly
│                       │      │                   matches an origin host that is itself a public suffix (e.g.,
│                       │      │                    `Domain=co.uk` set by `co.uk`). Instead of coercing it into
│                       │      │                    a strict host-only cookie, libcurl saves the cookie with
│                       │      │                   wildcard domain scope (`.co.uk`). Consequently, the cookie
│                       │      │                   is inappropriately included in subsequent outbound requests
│                       │      │                   or HTTP redirects to arbitrary sibling subdomains under the
│                       │      │                   same public suffix (e.g., `attacker.co.uk`). 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [31] ╭ VulnerabilityID : CVE-2026-14456 
│                       │      ├ PkgID           : libssl3@3.5.7-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : a25152af95b643e0 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-14456 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:98893ccad85be210f4dc3c923721fd882c50ad5c55fbda83632d3
│                       │      │                   f407b74ad2f 
│                       │      ├ Title           : openssl: OpenSSL: Denial of Service via unbounded memory
│                       │      │                   growth in QUIC server 
│                       │      ├ Description     : Issue summary: When an OpenSSL QUIC server (Listener SSL
│                       │      │                   object) processes
│                       │      │                   valid QUIC Initial packets for unknown destination
│                       │      │                   connection IDs, it
│                       │      │                   can allocate and queue new incoming channels without
│                       │      │                   enforcing any limit.
│                       │      │                   
│                       │      │                   Impact summary: A remote peer that can make many Initial
│                       │      │                   packets reach the
│                       │      │                   server listener faster than the application accepts
│                       │      │                   connections, can cause the
│                       │      │                   memory allocated to store the per-channel state to grow
│                       │      │                   without any limits,
│                       │      │                   potentially making the QUIC listener unavailable and causing
│                       │      │                    Denial of Service.
│                       │      │                   CWE: CWE-770: Allocation of Resources Without Limits or
│                       │      │                   Throttling
│                       │      │                   Description: The function that handles inbound QUIC packets
│                       │      │                   uses
│                       │      │                   Connection-Id from the packet header to find an existing
│                       │      │                   connection
│                       │      │                   (QUIC channel). If no existing connection is found and the
│                       │      │                   packet
│                       │      │                   type is INITIAL, the function treats the packet as a new
│                       │      │                   connection. It
│                       │      │                   allocates a new channel object and inserts it into a queue
│                       │      │                   where it
│                       │      │                   waits to be accepted by the local application with
│                       │      │                   SSL_accept(3ossl).
│                       │      │                   The memory occupied by these initial channel objects may
│                       │      │                   grow
│                       │      │                   without bounds if the application is not able to call
│                       │      │                   SSL_accept()
│                       │      │                   frequently enough to serve these inbound connection
│                       │      │                   requests.
│                       │      │                   The issue is present since OpenSSL 3.5 when the QUIC server
│                       │      │                   implementation
│                       │      │                   was added.
│                       │      │                   The fix introduces a limit for pending connections. The
│                       │      │                   default limit is set
│                       │      │                   to 256 pending connections (waiting to be accepted by the
│                       │      │                   local application).
│                       │      │                   Applications may change the default by calling
│                       │      │                   SSL_set_value_uint(3ossl).
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS module is not affected as the QUIC implementation
│                       │      │                   is outside of
│                       │      │                   the OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-770
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ photon: 3 
│                       │      │                  ├ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/08/13/4      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-14456        
│                       │      │                  https://github.com/openssl/openssl/commit/08e7756c3900bcfd77a
│                       │      │                  720e7b74e27d6e4ed01a9                                        
│                       │      │                  https://github.com/openssl/openssl/commit/4084152e040329ca019
│                       │      │                  4c4c1750b9b46d00a5b6b                                        
│                       │      │                  https://github.com/openssl/openssl/commit/f2f1465f2d2e5c61dfe
│                       │      │                  ac4d20fd093797d821139                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-14456              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260813.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-14456              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-13T15:19:31.82Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [32] ╭ VulnerabilityID : CVE-2026-18798 
│                       │      ├ PkgID           : libssl3@3.5.7-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : a25152af95b643e0 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18798 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:df135c2b84250b57e5105671b81a713f71eec7cdd789f10e735d9
│                       │      │                   dc02b12d00d 
│                       │      ├ Title           : openssl: QUIC server may trigger double free when processing
│                       │      │                    INITIAL packet 
│                       │      ├ Description     : Issue summary: QUIC server may double free QRX (QUIC record
│                       │      │                   layer RX) object
│                       │      │                   when channel creation fails for initial packet.
│                       │      │                   
│                       │      │                   Impact summary: Double free leads to heap corruption, which
│                       │      │                   typically results in 
│                       │      │                   termination of QUIC server process, leading to Denial of
│                       │      │                   Service. There is so
│                       │      │                   far no evidence that this double free is exploitable for
│                       │      │                   remote code execution,
│                       │      │                   thus it is considered highly improbable.
│                       │      │                   CWE: CWE-415: Double Free
│                       │      │                   Description: In order to validate initial packet, OpenSSL
│                       │      │                   QUIC stack default
│                       │      │                   packet handler (port_default_packet_handler()) creates a
│                       │      │                   so-called QRX object.
│                       │      │                   If the initial packet validates successfully with QRX
│                       │      │                   object, the default packet
│                       │      │                   handler proceeds to channel (connection object) creation.
│                       │      │                   The QRX object used
│                       │      │                   for packet validation is passed to port_bind_channel(), so
│                       │      │                   it becomes part of
│                       │      │                   the newly created connection. If port_bind_channel() fails,
│                       │      │                   then it also frees
│                       │      │                   the QRX object. Once port_bind_channel() returns, the
│                       │      │                   port_default_packet_handler()
│                       │      │                   detects the failure and proceeds to the error branch, where
│                       │      │                   the same QRX object is
│                       │      │                   freed for the second time.
│                       │      │                   The failure in port_bind_channel() function can be induced
│                       │      │                   with a relatively
│                       │      │                   low effort by a malformed (non RFC 9000 compliant) INITIAL
│                       │      │                   packet. If the packet
│                       │      │                   carries DCID (destination connection ID) which is shorter
│                       │      │                   than 8 bytes, then
│                       │      │                   port_bind_channel() jumps to the error path after
│                       │      │                   ossl_quic_lcidm_enrol_odcid()
│                       │      │                   detects that the DCID has invalid length.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS module is not affected, as the QUIC implementation
│                       │      │                   is outside of
│                       │      │                   the OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-415
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18798        
│                       │      │                  https://github.com/openssl/openssl/commit/70cebd74d3592f52729
│                       │      │                  45501b58a60374c4e13af                                        
│                       │      │                  https://github.com/openssl/openssl/commit/967582d5037f01a26b6
│                       │      │                  d19beae19af62a1b15c3c                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a14a1deac403522fbea
│                       │      │                  fabcb198503cf6caa7dc4                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18798              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18798              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:17:49.813Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [33] ╭ VulnerabilityID : CVE-2026-63072 
│                       │      ├ PkgID           : libssl3@3.5.7-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : a25152af95b643e0 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63072 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:68ec11e98fdf2aab2e0f85f8658eb693937c80148a3073f78ec47
│                       │      │                   95c2acb9f03 
│                       │      ├ Title           : openssl: heap buffer overflow in CMS key unwrapping 
│                       │      ├ Description     : Issue summary: OpenSSL CMS decryption sizes the key-unwrap
│                       │      │                   output buffer based
│                       │      │                   on querying the unwrapped key size, but the AES-WRAP-PAD
│                       │      │                   unwrap primitive
│                       │      │                   can write and cleanse more bytes than that query reports,
│                       │      │                   causing an 8-byte
│                       │      │                   out-of-bounds heap write.
│                       │      │                   
│                       │      │                   Impact summary: An attacker who supplies a crafted CMS
│                       │      │                   message can trigger a
│                       │      │                   deterministic 8-byte out-of-bounds heap write when the
│                       │      │                   victim decrypts it
│                       │      │                   with CMS_decrypt(), corrupting the heap and typically
│                       │      │                   resulting in a Denial
│                       │      │                   of Service.
│                       │      │                   CWE: CWE-787: Out-of-bounds Write
│                       │      │                   Description: The key-wrap OID is potentially
│                       │      │                   attacker-controlled on the wire.
│                       │      │                   CMS unwrapping allows both id-aesNNN-wrap-pad and
│                       │      │                   id-aesNNN-wrap ciphers.
│                       │      │                   An attacker can take a legitimate message and change a
│                       │      │                   single OID byte to
│                       │      │                   select the padded variant while leaving the message
│                       │      │                   otherwise valid. Since
│                       │      │                   the unwrap key is derived from the recipient's private
│                       │      │                   operation (ECDH key
│                       │      │                   agreement or ML-KEM decapsulation), the RFC 5649 integrity
│                       │      │                   check cannot
│                       │      │                   pass, and the decryption fails with integrity failure.
│                       │      │                   The write is a fixed-size (8-byte), fixed-value (zero) heap
│                       │      │                   overflow
│                       │      │                   immediately past the allocation, requires no special
│                       │      │                   configuration, and is
│                       │      │                   reachable from the public CMS_decrypt() function. The
│                       │      │                   consequence is
│                       │      │                   a heap corruption leading to a Denial of Service. The fix in
│                       │      │                    the CMS code
│                       │      │                   sizes the unwrap output buffer for the worst case so a
│                       │      │                   failed unwrap cannot
│                       │      │                   write past the allocation.
│                       │      │                   FIPS impact: no
│                       │      │                   As the CMS code lives outside the FIPS module boundary, no
│                       │      │                   FIPS
│                       │      │                   modules are affected by this CVE. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-787
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63072        
│                       │      │                  https://github.com/openssl/openssl/commit/2a3dac874c8057c1f01
│                       │      │                  86849bf1ede1ae7b6b756                                        
│                       │      │                  https://github.com/openssl/openssl/commit/87784ad619af36b8807
│                       │      │                  c2044b3940006fccc1e42                                        
│                       │      │                  https://github.com/openssl/openssl/commit/9530a5fd1aacaeccdce
│                       │      │                  d4478ea2340a480613335                                        
│                       │      │                  https://github.com/openssl/openssl/commit/9ec2f6d2ae2bcad907c
│                       │      │                  f7ee38584855bafe4979a                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a0c8ec557d9cac078f0
│                       │      │                  32d76cdf684fe743eb382                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63072              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63072              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.01Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [34] ╭ VulnerabilityID : CVE-2026-63076 
│                       │      ├ PkgID           : libssl3@3.5.7-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : a25152af95b643e0 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63076 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:015825b9153e3c7838ff1492b0b72081238e9d795ca56b3f24e72
│                       │      │                   41b886c8e79 
│                       │      ├ Title           : openssl: invalid pointer dereference in CMP server via
│                       │      │                   crafted protectionAlg 
│                       │      ├ Description     : Issue summary: OpenSSL CMP password based protection
│                       │      │                   verification only
│                       │      │                   checks whether the protectionAlg parameter was not NULL and
│                       │      │                   not its
│                       │      │                   ASN.1 type, before treating it as a PBMParameter. A crafted
│                       │      │                   message can
│                       │      │                   contain a parameter of a different type, which is then
│                       │      │                   dereferenced as an
│                       │      │                   invalid pointer.
│                       │      │                   
│                       │      │                   Impact summary: A remote, unauthenticated attacker can crash
│                       │      │                    an application
│                       │      │                   acting as a CMP server that accepts PBM-protected messages,
│                       │      │                   or a CMP client
│                       │      │                   talking to a malicious or intercepted CMP server, resulting
│                       │      │                   in a Denial of
│                       │      │                   Service.
│                       │      │                   CWE: CWE-476: NULL Pointer Dereference
│                       │      │                   Description: When verifying the password-based MAC
│                       │      │                   protection of a CMP
│                       │      │                   message, OpenSSL library reads the protectionAlg algorithm
│                       │      │                   parameter with
│                       │      │                   X509_ALGOR_get0(), which returns both the parameter type and
│                       │      │                    its value
│                       │      │                   pointer. The value is then cast to an ASN1_STRING and
│                       │      │                   treated as the
│                       │      │                   expected PBMParameter after only checking that pointer is
│                       │      │                   not NULL. The
│                       │      │                   parameter type returned by X509_ALGOR_get0() was never
│                       │      │                   consulted.
│                       │      │                   This happens during protection verification, before any MAC
│                       │      │                   is computed, so
│                       │      │                   no knowledge of the PBM shared secret is required; the only
│                       │      │                   precondition is
│                       │      │                   that PBM verification is reachable. On the server side this
│                       │      │                   is reached from
│                       │      │                   OSSL_CMP_SRV_process_request() for any application that
│                       │      │                   stands up a CMP
│                       │      │                   server accepting PBM-protected messages, and on the client
│                       │      │                   side from CMP
│                       │      │                   response validation against a malicious or on-path (MITM)
│                       │      │                   server. The
│                       │      │                   reliable consequence is a denial of service; there is no
│                       │      │                   memory disclosure,
│                       │      │                   no controlled memory write, and no path to code execution.
│                       │      │                   CMP is a
│                       │      │                   specialized feature that an application must explicitly
│                       │      │                   enable.
│                       │      │                   FIPS impact: no
│                       │      │                   As the CMP code lives outside the FIPS module boundary, no
│                       │      │                   FIPS modules
│                       │      │                   are affected by this CVE. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-476
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63076        
│                       │      │                  https://github.com/openssl/openssl/commit/37882aa2e0256e10724
│                       │      │                  42a8f62f7db45b995c45b                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a17cc8d612ecff6d94a
│                       │      │                  9b7ca8b5283ddf5ff570e                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a1f348ccb328c3afbd4
│                       │      │                  ba6883f9b7c813c043259                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a7af46a92d0ce19a90e
│                       │      │                  669ef56d2576a07924226                                        
│                       │      │                  https://github.com/openssl/openssl/commit/cdacfff557389abfa9e
│                       │      │                  4615abded2ec984517d6c                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63076              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63076              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.543Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [35] ╭ VulnerabilityID : CVE-2026-14457 
│                       │      ├ PkgID           : libssl3@3.5.7-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : a25152af95b643e0 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-14457 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:508b205e9aff82d59a5223e738614e0155b4faf212db80ed80219
│                       │      │                   ef98ae4c4e2 
│                       │      ├ Title           : openssl: RPK server signature algorithm selection can
│                       │      │                   dereference a missing certificate 
│                       │      ├ Description     : Issue summary: In a server or client configuration with
│                       │      │                   RFC7250 Raw Public Keys (RPKs)
│                       │      │                   enabled, and only the private key (with no associated
│                       │      │                   certificate) configured locally,
│                       │      │                   a NULL pointer dereference may occur when the remote peer
│                       │      │                   solicits raw public keys and
│                       │      │                   also sends the typically omitted "signature_algorithms_cert"
│                       │      │                    TLS extension.
│                       │      │                   
│                       │      │                   Impact summary: The impact is limited to a possible Denial
│                       │      │                   of Service as a result of
│                       │      │                   an application abort, no data disclosure or remote command
│                       │      │                   execution are possible.
│                       │      │                   CWE: CWE-476: NULL Pointer Dereference
│                       │      │                   Description: While a passing comment in sample code in the
│                       │      │                   documentation suggests
│                       │      │                   that key-only RPK configurations are supported, the
│                       │      │                   best-practice RPK configuration
│                       │      │                   is to always configure a corresponding certificate (possibly
│                       │      │                    self-signed or
│                       │      │                   signed by any convenient CA).
│                       │      │                   When the private key is configured along with a matching
│                       │      │                   certificate, the
│                       │      │                   "signature_algorithms_cert" extension is handled reliably
│                       │      │                   even without the
│                       │      │                   fix, and peer clients or servers that don't support raw
│                       │      │                   public keys may be
│                       │      │                   able to complete a TLS connection by pinning or verifying
│                       │      │                   the corresponding
│                       │      │                   certificate or its public key.
│                       │      │                   Deployments that prefer to configure just a private key with
│                       │      │                    no certificate
│                       │      │                   need to upgrade to an updated release as noted below.
│                       │      │                   FIPS impact: no
│                       │      │                   No FIPS modules are affected by this issue, as the SSL
│                       │      │                   protocol implementation
│                       │      │                   is outside the OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-476
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-14457        
│                       │      │                  https://github.com/openssl/openssl/commit/1e8c398db67404babd3
│                       │      │                  e5af999bb6bd86f720c76                                        
│                       │      │                  https://github.com/openssl/openssl/commit/581aaa0f0a35d214740
│                       │      │                  f0fe1f5283ec41f1212e1                                        
│                       │      │                  https://github.com/openssl/openssl/commit/d0af20478688a6aa2f5
│                       │      │                  9d61caa3f82136b181d7f                                        
│                       │      │                  https://github.com/openssl/openssl/commit/dad836b071da6579510
│                       │      │                  c968615848ba03cac593b                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-14457              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-14457              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:17:49.533Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [36] ╭ VulnerabilityID : CVE-2026-54874 
│                       │      ├ PkgID           : libssl3@3.5.7-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : a25152af95b643e0 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54874 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8258194f0f36c6b5f47042da76995e390707ca748b2f4a05242dd
│                       │      │                   e90b6f1454e 
│                       │      ├ Title           : openssl: excessive memory use buffering DTLS records for a
│                       │      │                   future epoch 
│                       │      ├ Description     : Issue summary: Receiving a DTLS record for a future epoch
│                       │      │                   while a handshake
│                       │      │                   is in progress causes OpenSSL to buffer far more memory than
│                       │      │                    the record
│                       │      │                   itself requires.
│                       │      │                   
│                       │      │                   Impact summary: A peer can use a small amount of network
│                       │      │                   traffic to make an
│                       │      │                   OpenSSL DTLS endpoint retain a disproportionately large
│                       │      │                   amount of memory,
│                       │      │                   which may lead to a Denial of Service.
│                       │      │                   CWE: CWE-405: Asymmetric Resource Consumption
│                       │      │                   (Amplification)
│                       │      │                   Description: While a DTLS handshake is in progress, a peer
│                       │      │                   may legitimately
│                       │      │                   have already moved on to the next epoch (for example, having
│                       │      │                    sent its
│                       │      │                   ChangeCipherSpec and Finished messages) before the local
│                       │      │                   endpoint has
│                       │      │                   processed the same transition, typically because of
│                       │      │                   reordering on the
│                       │      │                   underlying UDP transport. OpenSSL buffers such early records
│                       │      │                    so that they
│                       │      │                   can be processed once the local endpoint catches up.
│                       │      │                   Buffering a record currently retains the entire read buffer
│                       │      │                   it arrived in,
│                       │      │                   which is sized to hold the largest possible DTLS record
│                       │      │                   (around 16
│                       │      │                   kilobytes), rather than just the bytes that make up the
│                       │      │                   record itself. Up
│                       │      │                   to 100 such records may be buffered per connection. As a
│                       │      │                   result, a peer
│                       │      │                   that sends a stream of small forged records claiming to
│                       │      │                   belong to the next
│                       │      │                   epoch can cause an OpenSSL DTLS endpoint to retain around
│                       │      │                   1.7 megabytes of
│                       │      │                   memory, despite sending only a small fraction of that amount
│                       │      │                    of data over
│                       │      │                   the network.
│                       │      │                   An attacker therefore gains a memory amplification factor of
│                       │      │                    around 1200,
│                       │      │                   and can multiply the effect across as many associations as
│                       │      │                   it is able to
│                       │      │                   open, making this a remote memory exhaustion Denial of
│                       │      │                   Service risk for
│                       │      │                   DTLS servers. Since the memory retained per connection
│                       │      │                   remains bounded,
│                       │      │                   and any limit an application already places on the number of
│                       │      │                    concurrent
│                       │      │                   associations also bounds the total exposure, this issue has
│                       │      │                   been assessed
│                       │      │                   as Low severity.
│                       │      │                   FIPS impact: no
│                       │      │                   No FIPS modules are affected by this issue as the affected
│                       │      │                   code is outside
│                       │      │                   the OpenSSL FIPS module boundary.
│                       │      │                   OpenSSL 4.0, 3.6, 3.5, 3.4, 3.0, 1.1.1 and 1.0.2 are
│                       │      │                   vulnerable to this
│                       │      │                   issue.
│                       │      │                   OpenSSL 4.0 users should upgrade to OpenSSL 4.0.2.
│                       │      │                   OpenSSL 3.6 users should upgrade to OpenSSL 3.6.4.
│                       │      │                   OpenSSL 3.5 users should upgrade to OpenSSL 3.5.8.
│                       │      │                   OpenSSL 3.4 users should upgrade to OpenSSL 3.4.7.
│                       │      │                   OpenSSL 3.0 users should upgrade to OpenSSL 3.0.22.
│                       │      │                   Premium support customers only:
│                       │      │                   OpenSSL 1.1.1 users should upgrade to OpenSSL 1.1.1zi
│                       │      │                   OpenSSL 1.0.2 users should upgrade to OpenSSL 1.0.2zr
│                       │      │                   This issue was reported on 18 May 2026 by Amazon Web
│                       │      │                   Services.
│                       │      │                   The fix has been developed by Matt Caswell.
│                       │      │                   -- cut (non-publishing metadata for internal use) --
│                       │      │                   Reported by: Amazon Web Services
│                       │      │                   Fixed by: Matt Caswell 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-405
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-54874        
│                       │      │                  https://github.com/openssl/openssl/commit/4808b5d64176451f3d9
│                       │      │                  3d87d0ac9c81a9b13fb23                                        
│                       │      │                  https://github.com/openssl/openssl/commit/7110cb2f75806d0bf80
│                       │      │                  9eb2f90790d477900be40                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a0c8ec557d9cac078f0
│                       │      │                  32d76cdf684fe743eb382                                        
│                       │      │                  https://github.com/openssl/openssl/commit/cc0c6710917cd5eec00
│                       │      │                  1b297355d2ba723505107                                        
│                       │      │                  https://github.com/openssl/openssl/commit/f52ffc11b90737ac890
│                       │      │                  83909618dc2e1f42c561c                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-54874              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-54874              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:24.033Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [37] ╭ VulnerabilityID : CVE-2026-63073 
│                       │      ├ PkgID           : libssl3@3.5.7-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : a25152af95b643e0 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63073 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8656e8fa1a8dd33a071f97f1e6bf05788663c92daf50a1d0b4a32
│                       │      │                   489670f6611 
│                       │      ├ Title           : openssl: untrusted sender DN used as format string in CMP
│                       │      │                   response validation 
│                       │      ├ Description     : Issue summary: OpenSSL CMP response validation passed an
│                       │      │                   unexpected response
│                       │      │                   sender distinguished name directly as the format string to
│                       │      │                   `ERR_raise_data()`.
│                       │      │                   
│                       │      │                   Impact summary: A malicious or intercepted CMP endpoint can
│                       │      │                   crash a CMP client
│                       │      │                   that enforces an expected sender or uses a pinned server
│                       │      │                   certificate whose
│                       │      │                   subject becomes the default expected sender.
│                       │      │                   CWE: CWE-134 (Use of Externally-Controlled Format String)
│                       │      │                   Description: When validating a received CMP message,
│                       │      │                   ossl_cmp_msg_check_update()
│                       │      │                   converts the peer-supplied sender distinguished name with
│                       │      │                   X509_NAME_oneline()
│                       │      │                   and passes it directly as the format argument to
│                       │      │                   ERR_raise_data(). Percent
│                       │      │                   characters survive the conversion, so a sender DN such as
│                       │      │                   "CN=%s%n" reaches
│                       │      │                   BIO_vsnprintf() as an attacker-controlled format string with
│                       │      │                    no matching variadic
│                       │      │                   arguments. This path is only reached when the caller
│                       │      │                   configures an expected
│                       │      │                   sender or pins a server certificate, which is the normal
│                       │      │                   configuration for a
│                       │      │                   CMP client validating server responses.
│                       │      │                   Since the attacker controls the format string but none of
│                       │      │                   the variadic
│                       │      │                   arguments, such specifiers as %s and %n dereference or write
│                       │      │                    through unrelated
│                       │      │                   stack contents and crash the client. The reliable
│                       │      │                   consequence is a denial of
│                       │      │                   service, when the response comes from a malicious or
│                       │      │                   intercepted CMP endpoint.
│                       │      │                   There is no controlled memory write, arbitrary-address read,
│                       │      │                    or reliable path
│                       │      │                   to remote code execution.
│                       │      │                   FIPS impact: no
│                       │      │                   No FIPS modules are affected by this issue, as the CMP
│                       │      │                   protocol
│                       │      │                   implementation is outside the OpenSSL FIPS module
│                       │      │                   boundary. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-134
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63073        
│                       │      │                  https://github.com/openssl/openssl/commit/0cc20b322639919aa42
│                       │      │                  3e90799d9a57c3b4b76ca                                        
│                       │      │                  https://github.com/openssl/openssl/commit/6a0acc072b4d37a7cac
│                       │      │                  1252a29c1ce1f00c5ec29                                        
│                       │      │                  https://github.com/openssl/openssl/commit/7eb2e3ec9d1d4f35c80
│                       │      │                  22fccd4b03398b3f33e21                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a7e5a6eea8fd3ccca6b
│                       │      │                  6fbba031a5fbf8a3d93b4                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63073              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63073              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.147Z 
│                       │      ╰ LastModifiedDate: 2026-08-31T20:17:07.54Z 
│                       ├ [38] ╭ VulnerabilityID : CVE-2026-63074 
│                       │      ├ PkgID           : libssl3@3.5.7-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : a25152af95b643e0 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63074 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:2015e8324a0f10c428d05b20971d88a897caa763d0680347c4947
│                       │      │                   aa96d2cb760 
│                       │      ├ Title           : openssl: CMP indefinite cache growth of ExtraCerts 
│                       │      ├ Description     : Issue summary: The OpenSSL Certificate Management Protocol
│                       │      │                   (CMP) caches
│                       │      │                   additional certificates (extraCerts) sent in a CMP message,
│                       │      │                   but never expunges
│                       │      │                   them (for instance if they are invalid).  If a server reuses
│                       │      │                    an OSSL_CMP_CTX
│                       │      │                   frequently, this cache of extraCerts may grow unboundedly,
│                       │      │                   and a malicious
│                       │      │                   client may flood a CMP server with requests driving this
│                       │      │                   growth.
│                       │      │                   
│                       │      │                   Impact summary: Users utilizing a CMP server that reuses a
│                       │      │                   single OSSL_CMP_CTX
│                       │      │                   for the lifetime of a server process may observe unbounded
│                       │      │                   memory growth in the
│                       │      │                   event a malicious client repeatedly sends requests
│                       │      │                   containing unique extra
│                       │      │                   certificates, which may lead to OOM conditions.
│                       │      │                   CWE: CWE-770: Allocation of Resources Without Limits or
│                       │      │                   Throttling
│                       │      │                   Description: If a remote user sends CMP messages to a server
│                       │      │                    with a list of
│                       │      │                   extraCerts and the message is rejected, the extraCerts from
│                       │      │                   the message remains
│                       │      │                   in the server contexts untrusted certificate stack.  This
│                       │      │                   exposes servers with
│                       │      │                   long lived ctx objects to Denial of Service attacks in which
│                       │      │                    an attacker sends
│                       │      │                   messages intending to be rejected with a large list of
│                       │      │                   additional certificates
│                       │      │                   repeatedly, forcing the server to store them indefinitely.
│                       │      │                      
│                       │      │                   The issue was fixed by removing the added extra certs if the
│                       │      │                    message is
│                       │      │                   rejected, using the same method as when the context is
│                       │      │                   configured to not do
│                       │      │                   caching at all.
│                       │      │                   FIPS impact: no
│                       │      │                   As the CMP code lives outside the FIPS module boundary, no
│                       │      │                   FIPS
│                       │      │                   modules are affected by this CVE. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-770
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63074        
│                       │      │                  https://github.com/openssl/openssl/commit/01e567978a55fba1814
│                       │      │                  2a230380c31296049fae7                                        
│                       │      │                  https://github.com/openssl/openssl/commit/21a5d9658b0c66daace
│                       │      │                  60e10ea18ff32a448de9f                                        
│                       │      │                  https://github.com/openssl/openssl/commit/74ae7f6df47a5767c10
│                       │      │                  10b88c47507dfc5b32c46                                        
│                       │      │                  https://github.com/openssl/openssl/commit/75360af9650d4e0c82b
│                       │      │                  a0050c5c9912cd79e54af                                        
│                       │      │                  https://github.com/openssl/openssl/commit/f636f9ca0fa1bae5b42
│                       │      │                  f9e787f025c96fb09c43a                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63074              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63074              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.283Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [39] ╭ VulnerabilityID : CVE-2026-63075 
│                       │      ├ PkgID           : libssl3@3.5.7-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : a25152af95b643e0 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63075 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:b09c8021db59d44a9f3930de65419892ea077d5e45aeb2aa99353
│                       │      │                   b4f85ae8d51 
│                       │      ├ Title           : openssl: QUIC ACK-only packet retention can cause memory
│                       │      │                   exhaustion 
│                       │      ├ Description     : Issue summary: When OpenSSL processes QUIC traffic from a
│                       │      │                   peer that repeatedly
│                       │      │                   sends ack-eliciting packets while not acknowledging ACK-only
│                       │      │                    responses, the
│                       │      │                   QUIC stack can retain ACK-only packet metadata for the
│                       │      │                   lifetime of the
│                       │      │                   connection.
│                       │      │                   
│                       │      │                   Impact summary: A remote peer that can complete a QUIC
│                       │      │                   handshake can
│                       │      │                   cause connection-scoped memory growth which may lead to
│                       │      │                   Denial of Service
│                       │      │                   through memory exhaustion, especially with sustained traffic
│                       │      │                    or many concurrent
│                       │      │                   QUIC connections.
│                       │      │                   CWE: CWE-770: Allocation of Resources Without Limits or
│                       │      │                   Throttling
│                       │      │                   Description: When the OpenSSL QUIC stack sends an ACK-only
│                       │      │                   packet,
│                       │      │                   there is no requirement by the QUIC protocol that the peer
│                       │      │                   will acknowledge
│                       │      │                   that ACK-only packet (i.e. it is itself not ack-eliciting).
│                       │      │                   However, the OpenSSL
│                       │      │                   implementation stores the metadata about the ACK frames
│                       │      │                   regardless.
│                       │      │                   In and of itself that's ok, but if a malicious peer
│                       │      │                   establishes a connection, and
│                       │      │                   then drives the connection such that ACK-only packets are
│                       │      │                   forced from the 
│                       │      │                   OpenSSL implementation peer (i.e., by sending numerous PING
│                       │      │                   frames),
│                       │      │                   and then withholding any subsequent acks for ack-eliciting
│                       │      │                   data, like
│                       │      │                   legitimate data, said malicious peer can force inappropriate
│                       │      │                    memory growth
│                       │      │                   on the OpenSSL peer, potentially leading to a Denial of
│                       │      │                   Service.
│                       │      │                   The fix is to ensure that we account for the transmission of
│                       │      │                    the ACK-only
│                       │      │                   packet in the packet histories high and low watermark
│                       │      │                   without actually storing
│                       │      │                   the ACK-only packet metadata itself.
│                       │      │                   FIPS impact: no
│                       │      │                   The OpenSSL FIPS module is not affected as the QUIC code is
│                       │      │                   outside the FIPS module boundary. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-770
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63075        
│                       │      │                  https://github.com/openssl/openssl/commit/7308946576b12e64b8b
│                       │      │                  e53bcf0a120354b2b42bc                                        
│                       │      │                  https://github.com/openssl/openssl/commit/7c98d79738549df9286
│                       │      │                  8e7dd9be4bbf061eed709                                        
│                       │      │                  https://github.com/openssl/openssl/commit/bf84721c2548351176e
│                       │      │                  367e6de505792f0118dc6                                        
│                       │      │                  https://github.com/openssl/openssl/commit/c902e5f16d6a9e130e9
│                       │      │                  6d3ca6d8f64d71652e393                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63075              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63075              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.413Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [40] ╭ VulnerabilityID : CVE-2026-75803 
│                       │      ├ PkgID           : libssl3@3.5.7-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : a25152af95b643e0 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-75803 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:d4d04176f0a7dc2a8e8502f1d3b9063c3229a3e875bfb2d4f826e
│                       │      │                   26abe48f314 
│                       │      ├ Title           : Issue summary: ChaCha20-Poly1305 and AES-OCB decryption with
│                       │      │                    an empty  ... 
│                       │      ├ Description     : Issue summary: ChaCha20-Poly1305 and AES-OCB decryption with
│                       │      │                    an empty
│                       │      │                   ciphertext can report success without verifying the supplied
│                       │      │                    authentication
│                       │      │                   tag when the operation is finalized by calling the
│                       │      │                   EVP_Cipher() function.
│                       │      │                   
│                       │      │                   Impact summary: Applications calling EVP_Cipher() on an
│                       │      │                   empty ciphertext and
│                       │      │                   expecting the call to check the AEAD tag may accept forged
│                       │      │                   messages.
│                       │      │                   CWE: CWE-354 (Improper Validation of Integrity Check Value)
│                       │      │                   Description: The EVP_Cipher() API call for AEAD ciphers
│                       │      │                   behaves like a one
│                       │      │                   shot encryption and decryption call. It also verifies the
│                       │      │                   AEAD tag after the
│                       │      │                   decryption operation. However for AES-OCB and
│                       │      │                   ChaCha20-Poly1305 ciphers
│                       │      │                   it skipped the AEAD tag verification when an empty
│                       │      │                   ciphertext was passed to
│                       │      │                   the function. The callers of this function might believe
│                       │      │                   that a successful
│                       │      │                   return indicates a valid AEAD tag for these ciphers, even
│                       │      │                   when that has not
│                       │      │                   truly been validated in this case.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules in 4.0, 3.6, 3.5, 3.4, and 3.0 are not
│                       │      │                   affected by this CVE
│                       │      │                   as the affected algorithms are not FIPS approved and thus
│                       │      │                   not implemented
│                       │      │                   in the FIPS module. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-354
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/openssl/openssl/commit/119ab9555dc62275bbd
│                       │      │                  71f6f49529b1a44feba42                                        
│                       │      │                  https://github.com/openssl/openssl/commit/3621257986e27e540bf
│                       │      │                  96a11570929a6e5a9e05b                                        
│                       │      │                  https://github.com/openssl/openssl/commit/6c7aa6f8f6449b7fe01
│                       │      │                  37ee8be65fcd239bd7d6a                                        
│                       │      │                  https://github.com/openssl/openssl/commit/bdeb0cd994d91534278
│                       │      │                  7f117ee75044f0dc36f34                                        
│                       │      │                  https://github.com/openssl/openssl/commit/bf95f5f772e9362f87b
│                       │      │                  25cfa2f8cb15d984865b9                                        
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-3               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-75803              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:29.57Z 
│                       │      ╰ LastModifiedDate: 2026-09-01T19:17:27.543Z 
│                       ├ [41] ╭ VulnerabilityID : CVE-2026-41254 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-41254 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:2bef2682fb65c8381f097130f3c17faa2f505f3e43d06dd9af42c
│                       │      │                   88b7b1465d8 
│                       │      ├ Title           : Little CMS: lcms2: mm2/Little-CMS: Little CMS: Information
│                       │      │                   disclosure or denial of service via integer overflow in
│                       │      │                   CubeSize 
│                       │      ├ Description     : Little CMS (lcms2) through 2.18 has an integer overflow in
│                       │      │                   CubeSize in cmslut.c because the overflow check is performed
│                       │      │                    after the multiplication. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-696
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ julia      : 3 
│                       │      │                  ├ nvd        : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ├ julia   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ├ nvd     ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:
│                       │      │                            │           N/A:H 
│                       │      │                            ╰ V3Score : 6.1 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://abhinavagarwal07.github.io/posts/lcms2-cubesize-overf
│                       │      │                  low/                                                         
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899             
│                       │      │                                                                               
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-41254        
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2459420                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502751                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502782                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502783                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502784                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502791                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502792                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502793                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2503636                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636          
│                       │      │                                                                               
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147
│                       │      │                                                                               
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html          
│                       │      │                                                                               
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                
│                       │      │                                                                               
│                       │      │                  https://github.com/mm2/Little-CMS/commit/da6110b1d14abc394633
│                       │      │                  a388209abd5ebedd7ab0                                         
│                       │      │                  https://github.com/mm2/Little-CMS/commit/e0641b1828d0a1af5ecb
│                       │      │                  1b11fe22f24fceefd4bc                                         
│                       │      │                  https://github.com/mm2/Little-CMS/commit/e0641b1828d0a1af5ecb
│                       │      │                  1b11fe22f24fceefd4bc#commitcomment-183284136                 
│                       │      │                  https://github.com/mm2/Little-CMS/security/advisories/GHSA-4x
│                       │      │                  p6-rcgg-m9qq                                                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-41254.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html         
│                       │      │                                                                               
│                       │      │                  https://lists.debian.org/debian-lts-announce/2026/05/msg00014
│                       │      │                  .html                                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-41254              
│                       │      │                                                                               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-2
│                       │      │                  1                                                            
│                       │      │                  https://ubuntu.com/security/notices/USN-8209-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8209-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-41254              
│                       │      │                                                                               
│                       │      │                  https://www.openwall.com/lists/oss-security/2026/04/17/16    
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-18T07:16:10.807Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:46:23.47Z 
│                       ├ [42] ╭ VulnerabilityID : CVE-2026-47063 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47063 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:9fe36ed2bcec4f635f32c0c2d64ef9126de872f12ae7e8f7269f3
│                       │      │                   43ba93b1f7e 
│                       │      ├ Title           : openjdk: Enhance Jar handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Libraries).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u491, 8u491-perf, 11.0.31,
│                       │      │                   17.0.19, 21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK:
│                       │      │                   17.0.19 and  21.0.11; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.18. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   7.5 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 7.5 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47063         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47063.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47063               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47063               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:12.19Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:50:40.373Z 
│                       ├ [43] ╭ VulnerabilityID : CVE-2026-62574 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-62574 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:228f8317c8a604f2e75d690baa45a0be40d2e86f0d4d34d6ee6ea
│                       │      │                   19d05cf5b44 
│                       │      ├ Title           : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Orac ... 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Install).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u501, 11.0.32, 17.0.20, 21.0.12,
│                       │      │                   25.0.4, 26.0.2; Oracle GraalVM for JDK: 17.0.20 and 
│                       │      │                   21.0.12; Oracle GraalVM Enterprise Edition: 21.3.19. Easily
│                       │      │                   exploitable vulnerability allows low privileged attacker
│                       │      │                   with logon to the infrastructure where Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   executes to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in takeover of Oracle Java
│                       │      │                   SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. CVSS 3.1 Base Score 7.8 (Confidentiality, Integrity
│                       │      │                    and Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ─ bitnami: 3 
│                       │      ├ CVSS             ─ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:
│                       │      │                            │           H/A:H 
│                       │      │                            ╰ V3Score : 7.8 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-62574               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  https://www.oracle.com/security-alerts/cspuaug2026.html       
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:19:09.667Z 
│                       │      ╰ LastModifiedDate: 2026-08-18T21:17:09.31Z 
│                       ├ [44] ╭ VulnerabilityID : CVE-2026-46917 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46917 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:1e1f2ba0ce0c258b728426fd4e7ff75f222e14632c2af9a417b8d
│                       │      │                   90326313649 
│                       │      ├ Title           : openjdk: Improve DTLS handshaking (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Easily exploitable
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via TLS to compromise Oracle Java SE, Oracle GraalVM
│                       │      │                   for JDK, Oracle GraalVM Enterprise Edition.  Successful
│                       │      │                   attacks of this vulnerability can result in unauthorized
│                       │      │                   ability to cause a partial denial of service (partial DOS)
│                       │      │                   of Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition. Note: This vulnerability can only be
│                       │      │                   exploited by supplying data to APIs in the specified
│                       │      │                   Component without using Untrusted Java Web Start
│                       │      │                   applications or Untrusted Java applets, such as through a
│                       │      │                   web service. CVSS 3.1 Base Score 5.3 (Availability impacts).
│                       │      │                     CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-46917         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-46917.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-46917               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-46917               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:01.81Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:55:54.35Z 
│                       ├ [45] ╭ VulnerabilityID : CVE-2026-46968 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46968 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:2634158dfd94f0a275198edd86c54b4fdd4cd110617208dfb70aa
│                       │      │                   5ea5b25db38 
│                       │      ├ Title           : openjdk: Enhance TLS certificate handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: JSSE). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u491, 8u491-perf, 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Difficult to exploit
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via TLS to compromise Oracle Java SE.  Successful
│                       │      │                   attacks of this vulnerability can result in  unauthorized
│                       │      │                   creation, deletion or modification access to critical data
│                       │      │                   or all Oracle Java SE accessible data. Note: This
│                       │      │                   vulnerability can only be exploited by supplying data to
│                       │      │                   APIs in the specified Component without using Untrusted Java
│                       │      │                    Web Start applications or Untrusted Java applets, such as
│                       │      │                   through a web service. CVSS 3.1 Base Score 5.9 (Integrity
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 5.9 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 5.9 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-46968         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-46968.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-46968               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-46968               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:02.76Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T15:27:29.943Z 
│                       ├ [46] ╭ VulnerabilityID : CVE-2026-47021 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47021 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:0795c3db7b2138428578056f21b1bef7fcf8ceb32d6cc173fe8a5
│                       │      │                   c9e1815919b 
│                       │      ├ Title           : openjdk: Enhance XBM image support (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Easily exploitable vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 5.3 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-400
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47021         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47021.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47021               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47021               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:07.67Z 
│                       │      ╰ LastModifiedDate: 2026-08-12T20:17:44.44Z 
│                       ├ [47] ╭ VulnerabilityID : CVE-2026-47027 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47027 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:35142c28677757fbfc10574eb8f2b199d4847d8dd69b6ca00b5a0
│                       │      │                   79210140775 
│                       │      ├ Title           : openjdk: Enhance Jar file processing (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: Libraries). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u491, 8u491-perf, 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Easily exploitable
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via multiple protocols to compromise Oracle Java SE. 
│                       │      │                    Successful attacks of this vulnerability can result in
│                       │      │                   unauthorized ability to cause a partial denial of service
│                       │      │                   (partial DOS) of Oracle Java SE. Note: This vulnerability
│                       │      │                   can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   5.3 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47027         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47027.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47027               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47027               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:08.25Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:55:05.263Z 
│                       ├ [48] ╭ VulnerabilityID : CVE-2026-60147 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-60147 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:27e9f0d41c57aab59d7245642c431bd97417138a736acb1a641c0
│                       │      │                   b4d949594cb 
│                       │      ├ Title           : openjdk: Improve certification checking (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u491, 8u491-perf, 11.0.31,
│                       │      │                   17.0.19, 21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK:
│                       │      │                   17.0.19 and  21.0.11; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.18. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized update,
│                       │      │                   insert or delete access to some of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data as well as  unauthorized read access to a
│                       │      │                   subset of Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition accessible data. Note: This
│                       │      │                   vulnerability can be exploited by using APIs in the
│                       │      │                   specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 6.5 (Confidentiality and Integrity impacts). 
│                       │      │                    CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │      │                  │         │           L/A:N 
│                       │      │                  │         ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │      │                            │           L/A:N 
│                       │      │                            ╰ V3Score : 6.5 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-60147         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-60147.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-60147               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-60147               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:15.407Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:49:46.977Z 
│                       ├ [49] ╭ VulnerabilityID : CVE-2026-47010 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47010 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:5d9e3505ed2ce9eb04ffdab2f12f8b08508282c98d162e0aa4c3b
│                       │      │                   087ec3f0afa 
│                       │      ├ Title           : openjdk: Enhance JPEG handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: ImageIO).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 3.7 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           L/A:N 
│                       │      │                  │         ╰ V3Score : 3.7 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           L/A:N 
│                       │      │                            ╰ V3Score : 3.7 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47010         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47010.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47010               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47010               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:06.497Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T15:13:21.283Z 
│                       ├ [50] ╭ VulnerabilityID : CVE-2026-47059 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47059 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:d9431d7befd15916945ef2b75ef2acfc0186ca114ea16a538ebac
│                       │      │                   b1e0df2494a 
│                       │      ├ Title           : openjdk: Enhance AWT ImagingLib (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. This vulnerability
│                       │      │                   does not apply to Java deployments, typically in servers,
│                       │      │                   that load and run only trusted code (e.g., code installed by
│                       │      │                    an administrator). CVSS 3.1 Base Score 3.7 (Availability
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 3.7 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 3.7 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47059         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47059.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47059               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47059               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:11.727Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:51:30.65Z 
│                       ├ [51] ╭ VulnerabilityID : CVE-2026-41254 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-41254 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:75093146b82276a800dc70253b8788a680c2712997703c16185a9
│                       │      │                   550b5825a14 
│                       │      ├ Title           : Little CMS: lcms2: mm2/Little-CMS: Little CMS: Information
│                       │      │                   disclosure or denial of service via integer overflow in
│                       │      │                   CubeSize 
│                       │      ├ Description     : Little CMS (lcms2) through 2.18 has an integer overflow in
│                       │      │                   CubeSize in cmslut.c because the overflow check is performed
│                       │      │                    after the multiplication. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-696
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ julia      : 3 
│                       │      │                  ├ nvd        : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ├ julia   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ├ nvd     ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:
│                       │      │                            │           N/A:H 
│                       │      │                            ╰ V3Score : 6.1 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://abhinavagarwal07.github.io/posts/lcms2-cubesize-overf
│                       │      │                  low/                                                         
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899             
│                       │      │                                                                               
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-41254        
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2459420                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502751                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502782                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502783                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502784                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502791                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502792                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502793                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2503636                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636          
│                       │      │                                                                               
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147
│                       │      │                                                                               
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html          
│                       │      │                                                                               
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                
│                       │      │                                                                               
│                       │      │                  https://github.com/mm2/Little-CMS/commit/da6110b1d14abc394633
│                       │      │                  a388209abd5ebedd7ab0                                         
│                       │      │                  https://github.com/mm2/Little-CMS/commit/e0641b1828d0a1af5ecb
│                       │      │                  1b11fe22f24fceefd4bc                                         
│                       │      │                  https://github.com/mm2/Little-CMS/commit/e0641b1828d0a1af5ecb
│                       │      │                  1b11fe22f24fceefd4bc#commitcomment-183284136                 
│                       │      │                  https://github.com/mm2/Little-CMS/security/advisories/GHSA-4x
│                       │      │                  p6-rcgg-m9qq                                                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-41254.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html         
│                       │      │                                                                               
│                       │      │                  https://lists.debian.org/debian-lts-announce/2026/05/msg00014
│                       │      │                  .html                                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-41254              
│                       │      │                                                                               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-2
│                       │      │                  1                                                            
│                       │      │                  https://ubuntu.com/security/notices/USN-8209-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8209-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-41254              
│                       │      │                                                                               
│                       │      │                  https://www.openwall.com/lists/oss-security/2026/04/17/16    
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-18T07:16:10.807Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:46:23.47Z 
│                       ├ [52] ╭ VulnerabilityID : CVE-2026-47063 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47063 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:b964b7a30eb558f5309600c87b07db275966468bed385faa4b5b2
│                       │      │                   dc3a932790e 
│                       │      ├ Title           : openjdk: Enhance Jar handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Libraries).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u491, 8u491-perf, 11.0.31,
│                       │      │                   17.0.19, 21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK:
│                       │      │                   17.0.19 and  21.0.11; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.18. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   7.5 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 7.5 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47063         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47063.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47063               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47063               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:12.19Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:50:40.373Z 
│                       ├ [53] ╭ VulnerabilityID : CVE-2026-62574 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-62574 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8f8bc80b4134868875ae2a165262b387c23cdbf778ccfdb364a72
│                       │      │                   5335e88b742 
│                       │      ├ Title           : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Orac ... 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Install).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u501, 11.0.32, 17.0.20, 21.0.12,
│                       │      │                   25.0.4, 26.0.2; Oracle GraalVM for JDK: 17.0.20 and 
│                       │      │                   21.0.12; Oracle GraalVM Enterprise Edition: 21.3.19. Easily
│                       │      │                   exploitable vulnerability allows low privileged attacker
│                       │      │                   with logon to the infrastructure where Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   executes to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in takeover of Oracle Java
│                       │      │                   SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. CVSS 3.1 Base Score 7.8 (Confidentiality, Integrity
│                       │      │                    and Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ─ bitnami: 3 
│                       │      ├ CVSS             ─ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:
│                       │      │                            │           H/A:H 
│                       │      │                            ╰ V3Score : 7.8 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-62574               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  https://www.oracle.com/security-alerts/cspuaug2026.html       
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:19:09.667Z 
│                       │      ╰ LastModifiedDate: 2026-08-18T21:17:09.31Z 
│                       ├ [54] ╭ VulnerabilityID : CVE-2026-46917 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46917 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:ddd2eba843ebd1588653335b15b7bfd372a794a8dec1593189c1f
│                       │      │                   e34ae1067ea 
│                       │      ├ Title           : openjdk: Improve DTLS handshaking (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Easily exploitable
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via TLS to compromise Oracle Java SE, Oracle GraalVM
│                       │      │                   for JDK, Oracle GraalVM Enterprise Edition.  Successful
│                       │      │                   attacks of this vulnerability can result in unauthorized
│                       │      │                   ability to cause a partial denial of service (partial DOS)
│                       │      │                   of Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition. Note: This vulnerability can only be
│                       │      │                   exploited by supplying data to APIs in the specified
│                       │      │                   Component without using Untrusted Java Web Start
│                       │      │                   applications or Untrusted Java applets, such as through a
│                       │      │                   web service. CVSS 3.1 Base Score 5.3 (Availability impacts).
│                       │      │                     CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-46917         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-46917.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-46917               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-46917               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:01.81Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:55:54.35Z 
│                       ├ [55] ╭ VulnerabilityID : CVE-2026-46968 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46968 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:f3e24b0a70e8184de65d7b1b9f8bd07cd613c7f0663a549f1655b
│                       │      │                   31c1b149779 
│                       │      ├ Title           : openjdk: Enhance TLS certificate handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: JSSE). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u491, 8u491-perf, 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Difficult to exploit
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via TLS to compromise Oracle Java SE.  Successful
│                       │      │                   attacks of this vulnerability can result in  unauthorized
│                       │      │                   creation, deletion or modification access to critical data
│                       │      │                   or all Oracle Java SE accessible data. Note: This
│                       │      │                   vulnerability can only be exploited by supplying data to
│                       │      │                   APIs in the specified Component without using Untrusted Java
│                       │      │                    Web Start applications or Untrusted Java applets, such as
│                       │      │                   through a web service. CVSS 3.1 Base Score 5.9 (Integrity
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 5.9 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 5.9 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-46968         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-46968.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-46968               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-46968               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:02.76Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T15:27:29.943Z 
│                       ├ [56] ╭ VulnerabilityID : CVE-2026-47021 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47021 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:d24fc531250329a906054344a5b6dd1ac176431a923ba3d6f9173
│                       │      │                   88e54d5cd5f 
│                       │      ├ Title           : openjdk: Enhance XBM image support (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Easily exploitable vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 5.3 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-400
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47021         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47021.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47021               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47021               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:07.67Z 
│                       │      ╰ LastModifiedDate: 2026-08-12T20:17:44.44Z 
│                       ├ [57] ╭ VulnerabilityID : CVE-2026-47027 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47027 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:acb69b5edc29e23b41b13633c8485841a833bf55b8bc255386fab
│                       │      │                   64fb938c588 
│                       │      ├ Title           : openjdk: Enhance Jar file processing (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: Libraries). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u491, 8u491-perf, 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Easily exploitable
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via multiple protocols to compromise Oracle Java SE. 
│                       │      │                    Successful attacks of this vulnerability can result in
│                       │      │                   unauthorized ability to cause a partial denial of service
│                       │      │                   (partial DOS) of Oracle Java SE. Note: This vulnerability
│                       │      │                   can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   5.3 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47027         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47027.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47027               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47027               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:08.25Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:55:05.263Z 
│                       ├ [58] ╭ VulnerabilityID : CVE-2026-60147 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-60147 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:1f07f91c86dfff15476ce610885b5d415ea0865eb645c428304f0
│                       │      │                   80a4b219d22 
│                       │      ├ Title           : openjdk: Improve certification checking (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u491, 8u491-perf, 11.0.31,
│                       │      │                   17.0.19, 21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK:
│                       │      │                   17.0.19 and  21.0.11; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.18. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized update,
│                       │      │                   insert or delete access to some of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data as well as  unauthorized read access to a
│                       │      │                   subset of Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition accessible data. Note: This
│                       │      │                   vulnerability can be exploited by using APIs in the
│                       │      │                   specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 6.5 (Confidentiality and Integrity impacts). 
│                       │      │                    CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │      │                  │         │           L/A:N 
│                       │      │                  │         ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │      │                            │           L/A:N 
│                       │      │                            ╰ V3Score : 6.5 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-60147         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-60147.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-60147               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-60147               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:15.407Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:49:46.977Z 
│                       ├ [59] ╭ VulnerabilityID : CVE-2026-47010 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47010 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:86530604ae017e1e265cef1437d4693242198413cc5839b17b086
│                       │      │                   6163023e6bb 
│                       │      ├ Title           : openjdk: Enhance JPEG handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: ImageIO).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 3.7 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           L/A:N 
│                       │      │                  │         ╰ V3Score : 3.7 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           L/A:N 
│                       │      │                            ╰ V3Score : 3.7 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47010         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47010.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47010               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47010               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:06.497Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T15:13:21.283Z 
│                       ├ [60] ╭ VulnerabilityID : CVE-2026-47059 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47059 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e9c60a27ae14d588fe402536a048d2727fc02ba54af8274dd61f9
│                       │      │                   b49397d472e 
│                       │      ├ Title           : openjdk: Enhance AWT ImagingLib (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. This vulnerability
│                       │      │                   does not apply to Java deployments, typically in servers,
│                       │      │                   that load and run only trusted code (e.g., code installed by
│                       │      │                    an administrator). CVSS 3.1 Base Score 3.7 (Availability
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 3.7 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 3.7 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47059         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47059.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47059               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://ubuntu.com/security/notices/USN-8673-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8674-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8676-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8677-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8681-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8689-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8693-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8694-1                
│                       │      │                  https://ubuntu.com/security/notices/USN-8695-1                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47059               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:11.727Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:51:30.65Z 
│                       ├ [61] ╭ VulnerabilityID : CVE-2026-14456 
│                       │      ├ PkgID           : openssl@3.5.7-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : cb3cb2d163c67290 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-14456 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e8b0a6fc37d3a910dcc929b217b485acef2d62941fd46f795d2b9
│                       │      │                   a314dbba849 
│                       │      ├ Title           : openssl: OpenSSL: Denial of Service via unbounded memory
│                       │      │                   growth in QUIC server 
│                       │      ├ Description     : Issue summary: When an OpenSSL QUIC server (Listener SSL
│                       │      │                   object) processes
│                       │      │                   valid QUIC Initial packets for unknown destination
│                       │      │                   connection IDs, it
│                       │      │                   can allocate and queue new incoming channels without
│                       │      │                   enforcing any limit.
│                       │      │                   
│                       │      │                   Impact summary: A remote peer that can make many Initial
│                       │      │                   packets reach the
│                       │      │                   server listener faster than the application accepts
│                       │      │                   connections, can cause the
│                       │      │                   memory allocated to store the per-channel state to grow
│                       │      │                   without any limits,
│                       │      │                   potentially making the QUIC listener unavailable and causing
│                       │      │                    Denial of Service.
│                       │      │                   CWE: CWE-770: Allocation of Resources Without Limits or
│                       │      │                   Throttling
│                       │      │                   Description: The function that handles inbound QUIC packets
│                       │      │                   uses
│                       │      │                   Connection-Id from the packet header to find an existing
│                       │      │                   connection
│                       │      │                   (QUIC channel). If no existing connection is found and the
│                       │      │                   packet
│                       │      │                   type is INITIAL, the function treats the packet as a new
│                       │      │                   connection. It
│                       │      │                   allocates a new channel object and inserts it into a queue
│                       │      │                   where it
│                       │      │                   waits to be accepted by the local application with
│                       │      │                   SSL_accept(3ossl).
│                       │      │                   The memory occupied by these initial channel objects may
│                       │      │                   grow
│                       │      │                   without bounds if the application is not able to call
│                       │      │                   SSL_accept()
│                       │      │                   frequently enough to serve these inbound connection
│                       │      │                   requests.
│                       │      │                   The issue is present since OpenSSL 3.5 when the QUIC server
│                       │      │                   implementation
│                       │      │                   was added.
│                       │      │                   The fix introduces a limit for pending connections. The
│                       │      │                   default limit is set
│                       │      │                   to 256 pending connections (waiting to be accepted by the
│                       │      │                   local application).
│                       │      │                   Applications may change the default by calling
│                       │      │                   SSL_set_value_uint(3ossl).
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS module is not affected as the QUIC implementation
│                       │      │                   is outside of
│                       │      │                   the OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-770
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ photon: 3 
│                       │      │                  ├ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/08/13/4      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-14456        
│                       │      │                  https://github.com/openssl/openssl/commit/08e7756c3900bcfd77a
│                       │      │                  720e7b74e27d6e4ed01a9                                        
│                       │      │                  https://github.com/openssl/openssl/commit/4084152e040329ca019
│                       │      │                  4c4c1750b9b46d00a5b6b                                        
│                       │      │                  https://github.com/openssl/openssl/commit/f2f1465f2d2e5c61dfe
│                       │      │                  ac4d20fd093797d821139                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-14456              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260813.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-14456              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-13T15:19:31.82Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [62] ╭ VulnerabilityID : CVE-2026-18798 
│                       │      ├ PkgID           : openssl@3.5.7-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : cb3cb2d163c67290 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18798 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:f7b550db8d0932e99be1a449e162f3341d1ac0d625e88fb06d140
│                       │      │                   01e2e74e6b4 
│                       │      ├ Title           : openssl: QUIC server may trigger double free when processing
│                       │      │                    INITIAL packet 
│                       │      ├ Description     : Issue summary: QUIC server may double free QRX (QUIC record
│                       │      │                   layer RX) object
│                       │      │                   when channel creation fails for initial packet.
│                       │      │                   
│                       │      │                   Impact summary: Double free leads to heap corruption, which
│                       │      │                   typically results in 
│                       │      │                   termination of QUIC server process, leading to Denial of
│                       │      │                   Service. There is so
│                       │      │                   far no evidence that this double free is exploitable for
│                       │      │                   remote code execution,
│                       │      │                   thus it is considered highly improbable.
│                       │      │                   CWE: CWE-415: Double Free
│                       │      │                   Description: In order to validate initial packet, OpenSSL
│                       │      │                   QUIC stack default
│                       │      │                   packet handler (port_default_packet_handler()) creates a
│                       │      │                   so-called QRX object.
│                       │      │                   If the initial packet validates successfully with QRX
│                       │      │                   object, the default packet
│                       │      │                   handler proceeds to channel (connection object) creation.
│                       │      │                   The QRX object used
│                       │      │                   for packet validation is passed to port_bind_channel(), so
│                       │      │                   it becomes part of
│                       │      │                   the newly created connection. If port_bind_channel() fails,
│                       │      │                   then it also frees
│                       │      │                   the QRX object. Once port_bind_channel() returns, the
│                       │      │                   port_default_packet_handler()
│                       │      │                   detects the failure and proceeds to the error branch, where
│                       │      │                   the same QRX object is
│                       │      │                   freed for the second time.
│                       │      │                   The failure in port_bind_channel() function can be induced
│                       │      │                   with a relatively
│                       │      │                   low effort by a malformed (non RFC 9000 compliant) INITIAL
│                       │      │                   packet. If the packet
│                       │      │                   carries DCID (destination connection ID) which is shorter
│                       │      │                   than 8 bytes, then
│                       │      │                   port_bind_channel() jumps to the error path after
│                       │      │                   ossl_quic_lcidm_enrol_odcid()
│                       │      │                   detects that the DCID has invalid length.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS module is not affected, as the QUIC implementation
│                       │      │                   is outside of
│                       │      │                   the OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-415
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18798        
│                       │      │                  https://github.com/openssl/openssl/commit/70cebd74d3592f52729
│                       │      │                  45501b58a60374c4e13af                                        
│                       │      │                  https://github.com/openssl/openssl/commit/967582d5037f01a26b6
│                       │      │                  d19beae19af62a1b15c3c                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a14a1deac403522fbea
│                       │      │                  fabcb198503cf6caa7dc4                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18798              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18798              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:17:49.813Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [63] ╭ VulnerabilityID : CVE-2026-63072 
│                       │      ├ PkgID           : openssl@3.5.7-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : cb3cb2d163c67290 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63072 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:36bd83f3fab59ba1b34f8c9d3ccf3af0a7971ff0b5241410889f7
│                       │      │                   cc6ef59342a 
│                       │      ├ Title           : openssl: heap buffer overflow in CMS key unwrapping 
│                       │      ├ Description     : Issue summary: OpenSSL CMS decryption sizes the key-unwrap
│                       │      │                   output buffer based
│                       │      │                   on querying the unwrapped key size, but the AES-WRAP-PAD
│                       │      │                   unwrap primitive
│                       │      │                   can write and cleanse more bytes than that query reports,
│                       │      │                   causing an 8-byte
│                       │      │                   out-of-bounds heap write.
│                       │      │                   
│                       │      │                   Impact summary: An attacker who supplies a crafted CMS
│                       │      │                   message can trigger a
│                       │      │                   deterministic 8-byte out-of-bounds heap write when the
│                       │      │                   victim decrypts it
│                       │      │                   with CMS_decrypt(), corrupting the heap and typically
│                       │      │                   resulting in a Denial
│                       │      │                   of Service.
│                       │      │                   CWE: CWE-787: Out-of-bounds Write
│                       │      │                   Description: The key-wrap OID is potentially
│                       │      │                   attacker-controlled on the wire.
│                       │      │                   CMS unwrapping allows both id-aesNNN-wrap-pad and
│                       │      │                   id-aesNNN-wrap ciphers.
│                       │      │                   An attacker can take a legitimate message and change a
│                       │      │                   single OID byte to
│                       │      │                   select the padded variant while leaving the message
│                       │      │                   otherwise valid. Since
│                       │      │                   the unwrap key is derived from the recipient's private
│                       │      │                   operation (ECDH key
│                       │      │                   agreement or ML-KEM decapsulation), the RFC 5649 integrity
│                       │      │                   check cannot
│                       │      │                   pass, and the decryption fails with integrity failure.
│                       │      │                   The write is a fixed-size (8-byte), fixed-value (zero) heap
│                       │      │                   overflow
│                       │      │                   immediately past the allocation, requires no special
│                       │      │                   configuration, and is
│                       │      │                   reachable from the public CMS_decrypt() function. The
│                       │      │                   consequence is
│                       │      │                   a heap corruption leading to a Denial of Service. The fix in
│                       │      │                    the CMS code
│                       │      │                   sizes the unwrap output buffer for the worst case so a
│                       │      │                   failed unwrap cannot
│                       │      │                   write past the allocation.
│                       │      │                   FIPS impact: no
│                       │      │                   As the CMS code lives outside the FIPS module boundary, no
│                       │      │                   FIPS
│                       │      │                   modules are affected by this CVE. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-787
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63072        
│                       │      │                  https://github.com/openssl/openssl/commit/2a3dac874c8057c1f01
│                       │      │                  86849bf1ede1ae7b6b756                                        
│                       │      │                  https://github.com/openssl/openssl/commit/87784ad619af36b8807
│                       │      │                  c2044b3940006fccc1e42                                        
│                       │      │                  https://github.com/openssl/openssl/commit/9530a5fd1aacaeccdce
│                       │      │                  d4478ea2340a480613335                                        
│                       │      │                  https://github.com/openssl/openssl/commit/9ec2f6d2ae2bcad907c
│                       │      │                  f7ee38584855bafe4979a                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a0c8ec557d9cac078f0
│                       │      │                  32d76cdf684fe743eb382                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63072              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63072              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.01Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [64] ╭ VulnerabilityID : CVE-2026-63076 
│                       │      ├ PkgID           : openssl@3.5.7-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : cb3cb2d163c67290 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63076 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:ab992e4cc378272c070134fec516f14259139132151cff2b7e266
│                       │      │                   65568d0381e 
│                       │      ├ Title           : openssl: invalid pointer dereference in CMP server via
│                       │      │                   crafted protectionAlg 
│                       │      ├ Description     : Issue summary: OpenSSL CMP password based protection
│                       │      │                   verification only
│                       │      │                   checks whether the protectionAlg parameter was not NULL and
│                       │      │                   not its
│                       │      │                   ASN.1 type, before treating it as a PBMParameter. A crafted
│                       │      │                   message can
│                       │      │                   contain a parameter of a different type, which is then
│                       │      │                   dereferenced as an
│                       │      │                   invalid pointer.
│                       │      │                   
│                       │      │                   Impact summary: A remote, unauthenticated attacker can crash
│                       │      │                    an application
│                       │      │                   acting as a CMP server that accepts PBM-protected messages,
│                       │      │                   or a CMP client
│                       │      │                   talking to a malicious or intercepted CMP server, resulting
│                       │      │                   in a Denial of
│                       │      │                   Service.
│                       │      │                   CWE: CWE-476: NULL Pointer Dereference
│                       │      │                   Description: When verifying the password-based MAC
│                       │      │                   protection of a CMP
│                       │      │                   message, OpenSSL library reads the protectionAlg algorithm
│                       │      │                   parameter with
│                       │      │                   X509_ALGOR_get0(), which returns both the parameter type and
│                       │      │                    its value
│                       │      │                   pointer. The value is then cast to an ASN1_STRING and
│                       │      │                   treated as the
│                       │      │                   expected PBMParameter after only checking that pointer is
│                       │      │                   not NULL. The
│                       │      │                   parameter type returned by X509_ALGOR_get0() was never
│                       │      │                   consulted.
│                       │      │                   This happens during protection verification, before any MAC
│                       │      │                   is computed, so
│                       │      │                   no knowledge of the PBM shared secret is required; the only
│                       │      │                   precondition is
│                       │      │                   that PBM verification is reachable. On the server side this
│                       │      │                   is reached from
│                       │      │                   OSSL_CMP_SRV_process_request() for any application that
│                       │      │                   stands up a CMP
│                       │      │                   server accepting PBM-protected messages, and on the client
│                       │      │                   side from CMP
│                       │      │                   response validation against a malicious or on-path (MITM)
│                       │      │                   server. The
│                       │      │                   reliable consequence is a denial of service; there is no
│                       │      │                   memory disclosure,
│                       │      │                   no controlled memory write, and no path to code execution.
│                       │      │                   CMP is a
│                       │      │                   specialized feature that an application must explicitly
│                       │      │                   enable.
│                       │      │                   FIPS impact: no
│                       │      │                   As the CMP code lives outside the FIPS module boundary, no
│                       │      │                   FIPS modules
│                       │      │                   are affected by this CVE. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-476
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63076        
│                       │      │                  https://github.com/openssl/openssl/commit/37882aa2e0256e10724
│                       │      │                  42a8f62f7db45b995c45b                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a17cc8d612ecff6d94a
│                       │      │                  9b7ca8b5283ddf5ff570e                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a1f348ccb328c3afbd4
│                       │      │                  ba6883f9b7c813c043259                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a7af46a92d0ce19a90e
│                       │      │                  669ef56d2576a07924226                                        
│                       │      │                  https://github.com/openssl/openssl/commit/cdacfff557389abfa9e
│                       │      │                  4615abded2ec984517d6c                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63076              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63076              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.543Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [65] ╭ VulnerabilityID : CVE-2026-14457 
│                       │      ├ PkgID           : openssl@3.5.7-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : cb3cb2d163c67290 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-14457 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:21d71542add18ed4bba14d34c0ced669725793604f5d26299ea95
│                       │      │                   59c308319aa 
│                       │      ├ Title           : openssl: RPK server signature algorithm selection can
│                       │      │                   dereference a missing certificate 
│                       │      ├ Description     : Issue summary: In a server or client configuration with
│                       │      │                   RFC7250 Raw Public Keys (RPKs)
│                       │      │                   enabled, and only the private key (with no associated
│                       │      │                   certificate) configured locally,
│                       │      │                   a NULL pointer dereference may occur when the remote peer
│                       │      │                   solicits raw public keys and
│                       │      │                   also sends the typically omitted "signature_algorithms_cert"
│                       │      │                    TLS extension.
│                       │      │                   
│                       │      │                   Impact summary: The impact is limited to a possible Denial
│                       │      │                   of Service as a result of
│                       │      │                   an application abort, no data disclosure or remote command
│                       │      │                   execution are possible.
│                       │      │                   CWE: CWE-476: NULL Pointer Dereference
│                       │      │                   Description: While a passing comment in sample code in the
│                       │      │                   documentation suggests
│                       │      │                   that key-only RPK configurations are supported, the
│                       │      │                   best-practice RPK configuration
│                       │      │                   is to always configure a corresponding certificate (possibly
│                       │      │                    self-signed or
│                       │      │                   signed by any convenient CA).
│                       │      │                   When the private key is configured along with a matching
│                       │      │                   certificate, the
│                       │      │                   "signature_algorithms_cert" extension is handled reliably
│                       │      │                   even without the
│                       │      │                   fix, and peer clients or servers that don't support raw
│                       │      │                   public keys may be
│                       │      │                   able to complete a TLS connection by pinning or verifying
│                       │      │                   the corresponding
│                       │      │                   certificate or its public key.
│                       │      │                   Deployments that prefer to configure just a private key with
│                       │      │                    no certificate
│                       │      │                   need to upgrade to an updated release as noted below.
│                       │      │                   FIPS impact: no
│                       │      │                   No FIPS modules are affected by this issue, as the SSL
│                       │      │                   protocol implementation
│                       │      │                   is outside the OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-476
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-14457        
│                       │      │                  https://github.com/openssl/openssl/commit/1e8c398db67404babd3
│                       │      │                  e5af999bb6bd86f720c76                                        
│                       │      │                  https://github.com/openssl/openssl/commit/581aaa0f0a35d214740
│                       │      │                  f0fe1f5283ec41f1212e1                                        
│                       │      │                  https://github.com/openssl/openssl/commit/d0af20478688a6aa2f5
│                       │      │                  9d61caa3f82136b181d7f                                        
│                       │      │                  https://github.com/openssl/openssl/commit/dad836b071da6579510
│                       │      │                  c968615848ba03cac593b                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-14457              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-14457              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:17:49.533Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [66] ╭ VulnerabilityID : CVE-2026-54874 
│                       │      ├ PkgID           : openssl@3.5.7-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : cb3cb2d163c67290 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54874 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:a2f35fb05848aa0ebb08e124059e70ae2b923ce5104341b103d29
│                       │      │                   23046ba59bc 
│                       │      ├ Title           : openssl: excessive memory use buffering DTLS records for a
│                       │      │                   future epoch 
│                       │      ├ Description     : Issue summary: Receiving a DTLS record for a future epoch
│                       │      │                   while a handshake
│                       │      │                   is in progress causes OpenSSL to buffer far more memory than
│                       │      │                    the record
│                       │      │                   itself requires.
│                       │      │                   
│                       │      │                   Impact summary: A peer can use a small amount of network
│                       │      │                   traffic to make an
│                       │      │                   OpenSSL DTLS endpoint retain a disproportionately large
│                       │      │                   amount of memory,
│                       │      │                   which may lead to a Denial of Service.
│                       │      │                   CWE: CWE-405: Asymmetric Resource Consumption
│                       │      │                   (Amplification)
│                       │      │                   Description: While a DTLS handshake is in progress, a peer
│                       │      │                   may legitimately
│                       │      │                   have already moved on to the next epoch (for example, having
│                       │      │                    sent its
│                       │      │                   ChangeCipherSpec and Finished messages) before the local
│                       │      │                   endpoint has
│                       │      │                   processed the same transition, typically because of
│                       │      │                   reordering on the
│                       │      │                   underlying UDP transport. OpenSSL buffers such early records
│                       │      │                    so that they
│                       │      │                   can be processed once the local endpoint catches up.
│                       │      │                   Buffering a record currently retains the entire read buffer
│                       │      │                   it arrived in,
│                       │      │                   which is sized to hold the largest possible DTLS record
│                       │      │                   (around 16
│                       │      │                   kilobytes), rather than just the bytes that make up the
│                       │      │                   record itself. Up
│                       │      │                   to 100 such records may be buffered per connection. As a
│                       │      │                   result, a peer
│                       │      │                   that sends a stream of small forged records claiming to
│                       │      │                   belong to the next
│                       │      │                   epoch can cause an OpenSSL DTLS endpoint to retain around
│                       │      │                   1.7 megabytes of
│                       │      │                   memory, despite sending only a small fraction of that amount
│                       │      │                    of data over
│                       │      │                   the network.
│                       │      │                   An attacker therefore gains a memory amplification factor of
│                       │      │                    around 1200,
│                       │      │                   and can multiply the effect across as many associations as
│                       │      │                   it is able to
│                       │      │                   open, making this a remote memory exhaustion Denial of
│                       │      │                   Service risk for
│                       │      │                   DTLS servers. Since the memory retained per connection
│                       │      │                   remains bounded,
│                       │      │                   and any limit an application already places on the number of
│                       │      │                    concurrent
│                       │      │                   associations also bounds the total exposure, this issue has
│                       │      │                   been assessed
│                       │      │                   as Low severity.
│                       │      │                   FIPS impact: no
│                       │      │                   No FIPS modules are affected by this issue as the affected
│                       │      │                   code is outside
│                       │      │                   the OpenSSL FIPS module boundary.
│                       │      │                   OpenSSL 4.0, 3.6, 3.5, 3.4, 3.0, 1.1.1 and 1.0.2 are
│                       │      │                   vulnerable to this
│                       │      │                   issue.
│                       │      │                   OpenSSL 4.0 users should upgrade to OpenSSL 4.0.2.
│                       │      │                   OpenSSL 3.6 users should upgrade to OpenSSL 3.6.4.
│                       │      │                   OpenSSL 3.5 users should upgrade to OpenSSL 3.5.8.
│                       │      │                   OpenSSL 3.4 users should upgrade to OpenSSL 3.4.7.
│                       │      │                   OpenSSL 3.0 users should upgrade to OpenSSL 3.0.22.
│                       │      │                   Premium support customers only:
│                       │      │                   OpenSSL 1.1.1 users should upgrade to OpenSSL 1.1.1zi
│                       │      │                   OpenSSL 1.0.2 users should upgrade to OpenSSL 1.0.2zr
│                       │      │                   This issue was reported on 18 May 2026 by Amazon Web
│                       │      │                   Services.
│                       │      │                   The fix has been developed by Matt Caswell.
│                       │      │                   -- cut (non-publishing metadata for internal use) --
│                       │      │                   Reported by: Amazon Web Services
│                       │      │                   Fixed by: Matt Caswell 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-405
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-54874        
│                       │      │                  https://github.com/openssl/openssl/commit/4808b5d64176451f3d9
│                       │      │                  3d87d0ac9c81a9b13fb23                                        
│                       │      │                  https://github.com/openssl/openssl/commit/7110cb2f75806d0bf80
│                       │      │                  9eb2f90790d477900be40                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a0c8ec557d9cac078f0
│                       │      │                  32d76cdf684fe743eb382                                        
│                       │      │                  https://github.com/openssl/openssl/commit/cc0c6710917cd5eec00
│                       │      │                  1b297355d2ba723505107                                        
│                       │      │                  https://github.com/openssl/openssl/commit/f52ffc11b90737ac890
│                       │      │                  83909618dc2e1f42c561c                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-54874              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-54874              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:24.033Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [67] ╭ VulnerabilityID : CVE-2026-63073 
│                       │      ├ PkgID           : openssl@3.5.7-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : cb3cb2d163c67290 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63073 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:63f4a7c82abac6da45a706152a602a56ba2c62a1598d80693577c
│                       │      │                   e6a33d2fe86 
│                       │      ├ Title           : openssl: untrusted sender DN used as format string in CMP
│                       │      │                   response validation 
│                       │      ├ Description     : Issue summary: OpenSSL CMP response validation passed an
│                       │      │                   unexpected response
│                       │      │                   sender distinguished name directly as the format string to
│                       │      │                   `ERR_raise_data()`.
│                       │      │                   
│                       │      │                   Impact summary: A malicious or intercepted CMP endpoint can
│                       │      │                   crash a CMP client
│                       │      │                   that enforces an expected sender or uses a pinned server
│                       │      │                   certificate whose
│                       │      │                   subject becomes the default expected sender.
│                       │      │                   CWE: CWE-134 (Use of Externally-Controlled Format String)
│                       │      │                   Description: When validating a received CMP message,
│                       │      │                   ossl_cmp_msg_check_update()
│                       │      │                   converts the peer-supplied sender distinguished name with
│                       │      │                   X509_NAME_oneline()
│                       │      │                   and passes it directly as the format argument to
│                       │      │                   ERR_raise_data(). Percent
│                       │      │                   characters survive the conversion, so a sender DN such as
│                       │      │                   "CN=%s%n" reaches
│                       │      │                   BIO_vsnprintf() as an attacker-controlled format string with
│                       │      │                    no matching variadic
│                       │      │                   arguments. This path is only reached when the caller
│                       │      │                   configures an expected
│                       │      │                   sender or pins a server certificate, which is the normal
│                       │      │                   configuration for a
│                       │      │                   CMP client validating server responses.
│                       │      │                   Since the attacker controls the format string but none of
│                       │      │                   the variadic
│                       │      │                   arguments, such specifiers as %s and %n dereference or write
│                       │      │                    through unrelated
│                       │      │                   stack contents and crash the client. The reliable
│                       │      │                   consequence is a denial of
│                       │      │                   service, when the response comes from a malicious or
│                       │      │                   intercepted CMP endpoint.
│                       │      │                   There is no controlled memory write, arbitrary-address read,
│                       │      │                    or reliable path
│                       │      │                   to remote code execution.
│                       │      │                   FIPS impact: no
│                       │      │                   No FIPS modules are affected by this issue, as the CMP
│                       │      │                   protocol
│                       │      │                   implementation is outside the OpenSSL FIPS module
│                       │      │                   boundary. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-134
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63073        
│                       │      │                  https://github.com/openssl/openssl/commit/0cc20b322639919aa42
│                       │      │                  3e90799d9a57c3b4b76ca                                        
│                       │      │                  https://github.com/openssl/openssl/commit/6a0acc072b4d37a7cac
│                       │      │                  1252a29c1ce1f00c5ec29                                        
│                       │      │                  https://github.com/openssl/openssl/commit/7eb2e3ec9d1d4f35c80
│                       │      │                  22fccd4b03398b3f33e21                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a7e5a6eea8fd3ccca6b
│                       │      │                  6fbba031a5fbf8a3d93b4                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63073              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63073              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.147Z 
│                       │      ╰ LastModifiedDate: 2026-08-31T20:17:07.54Z 
│                       ├ [68] ╭ VulnerabilityID : CVE-2026-63074 
│                       │      ├ PkgID           : openssl@3.5.7-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : cb3cb2d163c67290 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63074 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:2d1164b8a729e425b451682606eac1709bef53af00a3d27c5a150
│                       │      │                   4c0e995b29a 
│                       │      ├ Title           : openssl: CMP indefinite cache growth of ExtraCerts 
│                       │      ├ Description     : Issue summary: The OpenSSL Certificate Management Protocol
│                       │      │                   (CMP) caches
│                       │      │                   additional certificates (extraCerts) sent in a CMP message,
│                       │      │                   but never expunges
│                       │      │                   them (for instance if they are invalid).  If a server reuses
│                       │      │                    an OSSL_CMP_CTX
│                       │      │                   frequently, this cache of extraCerts may grow unboundedly,
│                       │      │                   and a malicious
│                       │      │                   client may flood a CMP server with requests driving this
│                       │      │                   growth.
│                       │      │                   
│                       │      │                   Impact summary: Users utilizing a CMP server that reuses a
│                       │      │                   single OSSL_CMP_CTX
│                       │      │                   for the lifetime of a server process may observe unbounded
│                       │      │                   memory growth in the
│                       │      │                   event a malicious client repeatedly sends requests
│                       │      │                   containing unique extra
│                       │      │                   certificates, which may lead to OOM conditions.
│                       │      │                   CWE: CWE-770: Allocation of Resources Without Limits or
│                       │      │                   Throttling
│                       │      │                   Description: If a remote user sends CMP messages to a server
│                       │      │                    with a list of
│                       │      │                   extraCerts and the message is rejected, the extraCerts from
│                       │      │                   the message remains
│                       │      │                   in the server contexts untrusted certificate stack.  This
│                       │      │                   exposes servers with
│                       │      │                   long lived ctx objects to Denial of Service attacks in which
│                       │      │                    an attacker sends
│                       │      │                   messages intending to be rejected with a large list of
│                       │      │                   additional certificates
│                       │      │                   repeatedly, forcing the server to store them indefinitely.
│                       │      │                      
│                       │      │                   The issue was fixed by removing the added extra certs if the
│                       │      │                    message is
│                       │      │                   rejected, using the same method as when the context is
│                       │      │                   configured to not do
│                       │      │                   caching at all.
│                       │      │                   FIPS impact: no
│                       │      │                   As the CMP code lives outside the FIPS module boundary, no
│                       │      │                   FIPS
│                       │      │                   modules are affected by this CVE. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-770
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63074        
│                       │      │                  https://github.com/openssl/openssl/commit/01e567978a55fba1814
│                       │      │                  2a230380c31296049fae7                                        
│                       │      │                  https://github.com/openssl/openssl/commit/21a5d9658b0c66daace
│                       │      │                  60e10ea18ff32a448de9f                                        
│                       │      │                  https://github.com/openssl/openssl/commit/74ae7f6df47a5767c10
│                       │      │                  10b88c47507dfc5b32c46                                        
│                       │      │                  https://github.com/openssl/openssl/commit/75360af9650d4e0c82b
│                       │      │                  a0050c5c9912cd79e54af                                        
│                       │      │                  https://github.com/openssl/openssl/commit/f636f9ca0fa1bae5b42
│                       │      │                  f9e787f025c96fb09c43a                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63074              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63074              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.283Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ├ [69] ╭ VulnerabilityID : CVE-2026-63075 
│                       │      ├ PkgID           : openssl@3.5.7-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.7-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.1 
│                       │      │                  ╰ UID : cb3cb2d163c67290 
│                       │      ├ InstalledVersion: 3.5.7-r0 
│                       │      ├ FixedVersion    : 3.5.8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-63075 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:095c7f6420b6dee333797e3c009f3a80b99102e945121d58d5b09
│                       │      │                   8516a858cee 
│                       │      ├ Title           : openssl: QUIC ACK-only packet retention can cause memory
│                       │      │                   exhaustion 
│                       │      ├ Description     : Issue summary: When OpenSSL processes QUIC traffic from a
│                       │      │                   peer that repeatedly
│                       │      │                   sends ack-eliciting packets while not acknowledging ACK-only
│                       │      │                    responses, the
│                       │      │                   QUIC stack can retain ACK-only packet metadata for the
│                       │      │                   lifetime of the
│                       │      │                   connection.
│                       │      │                   
│                       │      │                   Impact summary: A remote peer that can complete a QUIC
│                       │      │                   handshake can
│                       │      │                   cause connection-scoped memory growth which may lead to
│                       │      │                   Denial of Service
│                       │      │                   through memory exhaustion, especially with sustained traffic
│                       │      │                    or many concurrent
│                       │      │                   QUIC connections.
│                       │      │                   CWE: CWE-770: Allocation of Resources Without Limits or
│                       │      │                   Throttling
│                       │      │                   Description: When the OpenSSL QUIC stack sends an ACK-only
│                       │      │                   packet,
│                       │      │                   there is no requirement by the QUIC protocol that the peer
│                       │      │                   will acknowledge
│                       │      │                   that ACK-only packet (i.e. it is itself not ack-eliciting).
│                       │      │                   However, the OpenSSL
│                       │      │                   implementation stores the metadata about the ACK frames
│                       │      │                   regardless.
│                       │      │                   In and of itself that's ok, but if a malicious peer
│                       │      │                   establishes a connection, and
│                       │      │                   then drives the connection such that ACK-only packets are
│                       │      │                   forced from the 
│                       │      │                   OpenSSL implementation peer (i.e., by sending numerous PING
│                       │      │                   frames),
│                       │      │                   and then withholding any subsequent acks for ack-eliciting
│                       │      │                   data, like
│                       │      │                   legitimate data, said malicious peer can force inappropriate
│                       │      │                    memory growth
│                       │      │                   on the OpenSSL peer, potentially leading to a Denial of
│                       │      │                   Service.
│                       │      │                   The fix is to ensure that we account for the transmission of
│                       │      │                    the ACK-only
│                       │      │                   packet in the packet histories high and low watermark
│                       │      │                   without actually storing
│                       │      │                   the ACK-only packet metadata itself.
│                       │      │                   FIPS impact: no
│                       │      │                   The OpenSSL FIPS module is not affected as the QUIC code is
│                       │      │                   outside the FIPS module boundary. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-770
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-63075        
│                       │      │                  https://github.com/openssl/openssl/commit/7308946576b12e64b8b
│                       │      │                  e53bcf0a120354b2b42bc                                        
│                       │      │                  https://github.com/openssl/openssl/commit/7c98d79738549df9286
│                       │      │                  8e7dd9be4bbf061eed709                                        
│                       │      │                  https://github.com/openssl/openssl/commit/bf84721c2548351176e
│                       │      │                  367e6de505792f0118dc6                                        
│                       │      │                  https://github.com/openssl/openssl/commit/c902e5f16d6a9e130e9
│                       │      │                  6d3ca6d8f64d71652e393                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-63075              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20260825.txt         
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8678-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-63075              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T13:19:26.413Z 
│                       │      ╰ LastModifiedDate: 2026-08-28T19:46:29.323Z 
│                       ╰ [70] ╭ VulnerabilityID : CVE-2026-75803 
│                              ├ PkgID           : openssl@3.5.7-r0 
│                              ├ PkgName         : openssl 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.7-r0?arch=x86_64&distro=3.
│                              │                  │       24.1 
│                              │                  ╰ UID : cb3cb2d163c67290 
│                              ├ InstalledVersion: 3.5.7-r0 
│                              ├ FixedVersion    : 3.5.8-r0 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                              │                  │         4e4c9f62e347164a4006 
│                              │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                              │                            77bbbb6e1ea62d15f4ee 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-75803 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Fingerprint     : sha256:3905083a7b63e7ec75a56bb567e1b12cacfa7e5c2e3444212e6bf
│                              │                   8e657c2f129 
│                              ├ Title           : Issue summary: ChaCha20-Poly1305 and AES-OCB decryption with
│                              │                    an empty  ... 
│                              ├ Description     : Issue summary: ChaCha20-Poly1305 and AES-OCB decryption with
│                              │                    an empty
│                              │                   ciphertext can report success without verifying the supplied
│                              │                    authentication
│                              │                   tag when the operation is finalized by calling the
│                              │                   EVP_Cipher() function.
│                              │                   
│                              │                   Impact summary: Applications calling EVP_Cipher() on an
│                              │                   empty ciphertext and
│                              │                   expecting the call to check the AEAD tag may accept forged
│                              │                   messages.
│                              │                   CWE: CWE-354 (Improper Validation of Integrity Check Value)
│                              │                   Description: The EVP_Cipher() API call for AEAD ciphers
│                              │                   behaves like a one
│                              │                   shot encryption and decryption call. It also verifies the
│                              │                   AEAD tag after the
│                              │                   decryption operation. However for AES-OCB and
│                              │                   ChaCha20-Poly1305 ciphers
│                              │                   it skipped the AEAD tag verification when an empty
│                              │                   ciphertext was passed to
│                              │                   the function. The callers of this function might believe
│                              │                   that a successful
│                              │                   return indicates a valid AEAD tag for these ciphers, even
│                              │                   when that has not
│                              │                   truly been validated in this case.
│                              │                   FIPS impact: no
│                              │                   The FIPS modules in 4.0, 3.6, 3.5, 3.4, and 3.0 are not
│                              │                   affected by this CVE
│                              │                   as the affected algorithms are not FIPS approved and thus
│                              │                   not implemented
│                              │                   in the FIPS module. 
│                              ├ Severity        : LOW 
│                              ├ CweIDs                  
│                              │                  ───────
│                              │                  CWE-354
│                              │                  
│                              ├ VendorSeverity   ─ ubuntu: 1 
│                              ├ References                                                                    
│                              │                  ─────────────────────────────────────────────────────────────
│                              │                  https://github.com/openssl/openssl/commit/119ab9555dc62275bbd
│                              │                  71f6f49529b1a44feba42                                        
│                              │                  https://github.com/openssl/openssl/commit/3621257986e27e540bf
│                              │                  96a11570929a6e5a9e05b                                        
│                              │                  https://github.com/openssl/openssl/commit/6c7aa6f8f6449b7fe01
│                              │                  37ee8be65fcd239bd7d6a                                        
│                              │                  https://github.com/openssl/openssl/commit/bdeb0cd994d91534278
│                              │                  7f117ee75044f0dc36f34                                        
│                              │                  https://github.com/openssl/openssl/commit/bf95f5f772e9362f87b
│                              │                  25cfa2f8cb15d984865b9                                        
│                              │                  https://openssl-library.org/news/secadv/20260825.txt         
│                              │                                                                               
│                              │                  https://ubuntu.com/security/notices/USN-8678-1               
│                              │                                                                               
│                              │                  https://ubuntu.com/security/notices/USN-8678-3               
│                              │                                                                               
│                              │                  https://www.cve.org/CVERecord?id=CVE-2026-75803              
│                              │                                                                               
│                              │                  
│                              ├ PublishedDate   : 2026-08-25T13:19:29.57Z 
│                              ╰ LastModifiedDate: 2026-09-01T19:17:27.543Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages 
```
