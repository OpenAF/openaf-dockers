```yaml
╭ [0] ╭ Target         : openaf/pyoaf:edge (alpine 3.24.2) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-88806 
│                       │      ├ PkgID           : libx11@1.8.13-r0 
│                       │      ├ PkgName         : libx11 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libx11@1.8.13-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.2 
│                       │      │                  ╰ UID : f1e6fa6303e0c19a 
│                       │      ├ InstalledVersion: 1.8.13-r0 
│                       │      ├ FixedVersion    : 1.8.14-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-88806 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:911b3588cc889c2fd12f4bb35b3928c43f499bafa2e631ad43ff9
│                       │      │                   2753aaa09de 
│                       │      ├ Title           : libX11: libX11: Heap-based buffer overflow via malicious X
│                       │      │                   server 
│                       │      ├ Description     : A malicious X server could exploit a buffer overflow in
│                       │      │                   libX11 before 1.8.14 during handling of XkbGetMap
│                       │      │                   overflowing the key_sym_map. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-122
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 3 
│                       │      │                  ├ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-88806        
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libx11/-/merge_reques
│                       │      │                  ts/309                                                       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-88806              
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8913-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-88806              
│                       │      ├ PublishedDate   : 2026-09-21T14:17:22.273Z 
│                       │      ╰ LastModifiedDate: 2026-09-22T19:40:05.87Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-94283 
│                       │      ├ PkgID           : libx11@1.8.13-r0 
│                       │      ├ PkgName         : libx11 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libx11@1.8.13-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.2 
│                       │      │                  ╰ UID : f1e6fa6303e0c19a 
│                       │      ├ InstalledVersion: 1.8.13-r0 
│                       │      ├ FixedVersion    : 1.8.14-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94283 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:043e8f0af6ccd44dfb36680de9dcfe3350dbcfa15329c75c3b151
│                       │      │                   2ef447c0d22 
│                       │      ├ Title           : libX11: libX11: Denial of Service via out-of-bounds read in
│                       │      │                   XIM attribute parser 
│                       │      ├ Description     : An out-of-bounds read vulnerability in libX11's XIM (X Input
│                       │      │                    Method) attribute parser in libX11 before 1.8.14 could be
│                       │      │                   used by malicious X servers to crash attached X clients. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-94283         
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libx11/-/merge_request
│                       │      │                  s/310                                                         
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libx11/-/merge_request
│                       │      │                  s/310/diffs?commit_id=42d0303f243002a9856c76060569a61893c670dd
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94283               
│                       │      │                                                                                
│                       │      │                  https://ubuntu.com/security/notices/USN-8913-1                
│                       │      │                                                                                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94283               
│                       │      ├ PublishedDate   : 2026-09-28T09:17:08.133Z 
│                       │      ╰ LastModifiedDate: 2026-09-30T13:17:26.27Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-94284 
│                       │      ├ PkgID           : libx11@1.8.13-r0 
│                       │      ├ PkgName         : libx11 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libx11@1.8.13-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.2 
│                       │      │                  ╰ UID : f1e6fa6303e0c19a 
│                       │      ├ InstalledVersion: 1.8.13-r0 
│                       │      ├ FixedVersion    : 1.8.14-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94284 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:cd23bd5ba3b8a74f21647f409ae0496c3b9a8ef7f2cd436275ea0
│                       │      │                   76bb49251c6 
│                       │      ├ Title           : libX11: libX11: Denial of Service via out-of-bounds read in
│                       │      │                   XIM trigger-key registration parser 
│                       │      ├ Description     : An out-of-bounds read vulnerability in libX11's XIM
│                       │      │                   trigger-key registration parser in libX11 before 1.8.14
│                       │      │                   could be used by malicious X servers to crash attached X
│                       │      │                   clients. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.5 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-94284         
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libx11/-/merge_request
│                       │      │                  s/310                                                         
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libx11/-/merge_request
│                       │      │                  s/310/diffs?commit_id=1b7904002d212eed40949ccf4e8e7156f9fec0e2
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94284               
│                       │      │                                                                                
│                       │      │                  https://ubuntu.com/security/notices/USN-8913-1                
│                       │      │                                                                                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94284               
│                       │      ├ PublishedDate   : 2026-09-28T09:17:08.247Z 
│                       │      ╰ LastModifiedDate: 2026-09-30T13:17:26.41Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-94285 
│                       │      ├ PkgID           : libx11@1.8.13-r0 
│                       │      ├ PkgName         : libx11 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libx11@1.8.13-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.2 
│                       │      │                  ╰ UID : f1e6fa6303e0c19a 
│                       │      ├ InstalledVersion: 1.8.13-r0 
│                       │      ├ FixedVersion    : 1.8.14-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94285 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:156d70746a9f97f7102706db3bfc4454cf5447d04c6a74a30bfec
│                       │      │                   3c4129c2c95 
│                       │      ├ Title           : libX11: libX11: Denial of Service via out-of-bounds read in
│                       │      │                   byte-oriented codeset parser 
│                       │      ├ Description     : An out-of-bounds read in libX11's byte-oriented codeset
│                       │      │                   parser in libX11 before 1.8.14 could be used by malicious X
│                       │      │                   servers to crash attached X clients. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.1 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-94285         
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libx11/-/merge_request
│                       │      │                  s/310                                                         
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libx11/-/merge_request
│                       │      │                  s/310/diffs?commit_id=980868483446f24f9658d26aa5bfa42f3da6dd3a
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94285               
│                       │      │                                                                                
│                       │      │                  https://ubuntu.com/security/notices/USN-8913-1                
│                       │      │                                                                                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94285               
│                       │      ├ PublishedDate   : 2026-09-28T09:17:08.353Z 
│                       │      ╰ LastModifiedDate: 2026-09-30T13:17:26.57Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-93541 
│                       │      ├ PkgID           : libxi@1.8.3-r0 
│                       │      ├ PkgName         : libxi 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxi@1.8.3-r0?arch=x86_64&distro=3.24.2 
│                       │      │                  ╰ UID : 48645fd8596750c6 
│                       │      ├ InstalledVersion: 1.8.3-r0 
│                       │      ├ FixedVersion    : 1.8.4-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-93541 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:369431e31a151ae2431237f1e45bd125e5055340ad5a6299515db
│                       │      │                   cde9f2f977f 
│                       │      ├ Title           : libXi: Out-of-bounds read in libXi's XQueryDeviceState() 
│                       │      ├ Description     : An out-of-bounds read in libXi's XQueryDeviceState() in
│                       │      │                   libXi before 1.8.4 could be used by a 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-93541        
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libxi/-/merge_request
│                       │      │                  s/23/diffs?commit_id=7b6fffd13fd3914e0b39f3a4f131913da7f066e7
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-93541              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-93541              
│                       │      ├ PublishedDate   : 2026-09-24T16:17:26.163Z 
│                       │      ╰ LastModifiedDate: 2026-09-24T21:00:46.893Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-93542 
│                       │      ├ PkgID           : libxi@1.8.3-r0 
│                       │      ├ PkgName         : libxi 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxi@1.8.3-r0?arch=x86_64&distro=3.24.2 
│                       │      │                  ╰ UID : 48645fd8596750c6 
│                       │      ├ InstalledVersion: 1.8.3-r0 
│                       │      ├ FixedVersion    : 1.8.4-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-93542 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e9d058aec202cdf6f6563b40c392d1f0a80d8582b2b86b1d9db1a
│                       │      │                   58446d8d3ce 
│                       │      ├ Title           : libXi: libXi: Denial of Service via out-of-bounds read
│                       │      │                   during XI2 class parsing 
│                       │      ├ Description     : An out-of-bounds read in libXi's XI2 class parsing via
│                       │      │                   size_classes() and copy_classes() in libXi before 1.8.4
│                       │      │                   could be used by malicous servers to crash the X client. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-93542        
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libxi/-/merge_request
│                       │      │                  s/23/diffs?commit_id=f499944ad595b9bd7e7571c810842244caf150aa
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-93542              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-93542              
│                       │      ├ PublishedDate   : 2026-09-24T17:17:10.183Z 
│                       │      ╰ LastModifiedDate: 2026-09-24T21:00:46.893Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-93543 
│                       │      ├ PkgID           : libxi@1.8.3-r0 
│                       │      ├ PkgName         : libxi 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxi@1.8.3-r0?arch=x86_64&distro=3.24.2 
│                       │      │                  ╰ UID : 48645fd8596750c6 
│                       │      ├ InstalledVersion: 1.8.3-r0 
│                       │      ├ FixedVersion    : 1.8.4-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-93543 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:c195d16f7430202f3af29b4deaef8eb76888d1ac1da28206e9d88
│                       │      │                   25f25ed334b 
│                       │      ├ Title           : libXi: libXi: Denial of Service via out-of-bounds read in
│                       │      │                   XI2 class parser 
│                       │      ├ Description     : An out-of-bounds read in libXi's XI2 class parser in libXi
│                       │      │                   before 1.8.4 could be used by malicious X servers to crash
│                       │      │                   an attached X client. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-93543        
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libxi/-/merge_request
│                       │      │                  s/23/diffs?commit_id=e2089ab748828273f916bbffd4e65b506aa50fdc
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-93543              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-93543              
│                       │      ├ PublishedDate   : 2026-09-24T17:17:10.307Z 
│                       │      ╰ LastModifiedDate: 2026-09-24T21:00:46.893Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-93544 
│                       │      ├ PkgID           : libxi@1.8.3-r0 
│                       │      ├ PkgName         : libxi 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxi@1.8.3-r0?arch=x86_64&distro=3.24.2 
│                       │      │                  ╰ UID : 48645fd8596750c6 
│                       │      ├ InstalledVersion: 1.8.3-r0 
│                       │      ├ FixedVersion    : 1.8.4-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-93544 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:2246626490703846c4c7a9dadfb3bcc53dcc72fc17261ad910fc8
│                       │      │                   5f601e40661 
│                       │      ├ Title           : libXi: libXi: Denial of Service via out-of-bounds read in
│                       │      │                   XIQueryDevice reply parsing 
│                       │      ├ Description     : An out-of-bounds read in libXi's XI2 XIQueryDevice reply
│                       │      │                   parsing in libXi before 1.8.4 can be used by a malicious X
│                       │      │                   server to crash an attached X client. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-93544        
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libxi/-/merge_request
│                       │      │                  s/23/diffs?commit_id=a88a341135b79f6ed450f481e4a5d6ba502382af
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-93544              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-93544              
│                       │      ├ PublishedDate   : 2026-09-24T17:17:10.43Z 
│                       │      ╰ LastModifiedDate: 2026-09-24T21:00:46.893Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-93545 
│                       │      ├ PkgID           : libxi@1.8.3-r0 
│                       │      ├ PkgName         : libxi 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxi@1.8.3-r0?arch=x86_64&distro=3.24.2 
│                       │      │                  ╰ UID : 48645fd8596750c6 
│                       │      ├ InstalledVersion: 1.8.3-r0 
│                       │      ├ FixedVersion    : 1.8.4-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-93545 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:986870f6b03af26e7d3b6cb4c13bc8b7e26ebb868cd2823be5d69
│                       │      │                   2952b597003 
│                       │      ├ Title           : libXi: libXi: Denial of Service via out-of-bounds read in
│                       │      │                   XListInputDevices() 
│                       │      ├ Description     : An out-of-bounds read in libXi's XListInputDevices() in
│                       │      │                   libXi before 1.8.4 could be used by malicious X servers to
│                       │      │                   crash an attached X client. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-93545        
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libxi/-/merge_request
│                       │      │                  s/23/diffs?commit_id=234ce17d95c42d75f7f7fdb2bf7a24875451bc0a
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-93545              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-93545              
│                       │      ├ PublishedDate   : 2026-09-24T17:17:10.55Z 
│                       │      ╰ LastModifiedDate: 2026-09-24T21:00:46.893Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-94281 
│                       │      ├ PkgID           : libxi@1.8.3-r0 
│                       │      ├ PkgName         : libxi 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxi@1.8.3-r0?arch=x86_64&distro=3.24.2 
│                       │      │                  ╰ UID : 48645fd8596750c6 
│                       │      ├ InstalledVersion: 1.8.3-r0 
│                       │      ├ FixedVersion    : 1.8.4-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94281 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:9c93e8a2d3474f607fdb1e0985a209a85955d4a184c110766ac49
│                       │      │                   e3119036450 
│                       │      ├ Title           : libXi: libXi: Denial of Service via out-of-bounds read in
│                       │      │                   XListInputDevices() 
│                       │      ├ Description     : An out-of-bounds read in libXi's XListInputDevices() class
│                       │      │                   parsing in libXi before 1.8.4 could be used by malicious X
│                       │      │                   servers to crash an attached X client. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-94281        
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libxi/-/merge_request
│                       │      │                  s/23/diffs?commit_id=605f419d013153bf9e026cd100752ffbe930f3c1
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94281              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94281              
│                       │      ├ PublishedDate   : 2026-09-24T17:17:16.86Z 
│                       │      ╰ LastModifiedDate: 2026-09-24T21:00:46.893Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-94282 
│                       │      ├ PkgID           : libxi@1.8.3-r0 
│                       │      ├ PkgName         : libxi 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxi@1.8.3-r0?arch=x86_64&distro=3.24.2 
│                       │      │                  ╰ UID : 48645fd8596750c6 
│                       │      ├ InstalledVersion: 1.8.3-r0 
│                       │      ├ FixedVersion    : 1.8.4-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94282 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:fcdb603c3569069707b1274febd60817616b4f75ba0ccb2cf11bd
│                       │      │                   5559f7b1196 
│                       │      ├ Title           : libXi: libXi: Denial of Service via out-of-bounds read in
│                       │      │                   XI2 event processing 
│                       │      ├ Description     : An out-of-bounds read in libXi's XI2 enter/leave/focus
│                       │      │                   cookie conversion in libXi before 1.8.4 could be used by
│                       │      │                   malicious X server to crash an attached X client. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.1 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-94282        
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libxi/-/merge_request
│                       │      │                  s/23/diffs?commit_id=cecf160e9731fe01f3632f875f29ffcb598b052a
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94282              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94282              
│                       │      ├ PublishedDate   : 2026-09-28T09:17:08.003Z 
│                       │      ╰ LastModifiedDate: 2026-09-30T13:17:26.123Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-109089 
│                       │      ├ PkgID           : libxi@1.8.3-r0 
│                       │      ├ PkgName         : libxi 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxi@1.8.3-r0?arch=x86_64&distro=3.24.2 
│                       │      │                  ╰ UID : 48645fd8596750c6 
│                       │      ├ InstalledVersion: 1.8.3-r0 
│                       │      ├ FixedVersion    : 1.8.4-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:815a1f6a980082eb2a2922021593b2da8fa7bad106416ce55b2ef
│                       │      │                   b328e99d74a 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-109090 
│                       │      ├ PkgID           : libxi@1.8.3-r0 
│                       │      ├ PkgName         : libxi 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxi@1.8.3-r0?arch=x86_64&distro=3.24.2 
│                       │      │                  ╰ UID : 48645fd8596750c6 
│                       │      ├ InstalledVersion: 1.8.3-r0 
│                       │      ├ FixedVersion    : 1.8.4-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:49c273c8754966dd6cb3bbd0246f6690a5f6daa24b206415608c8
│                       │      │                   07d225c7160 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-88807 
│                       │      ├ PkgID           : libxrender@0.9.12-r0 
│                       │      ├ PkgName         : libxrender 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxrender@0.9.12-r0?arch=x86_64&distr
│                       │      │                  │       o=3.24.2 
│                       │      │                  ╰ UID : fb1c851a353fdee5 
│                       │      ├ InstalledVersion: 0.9.12-r0 
│                       │      ├ FixedVersion    : 0.9.13-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-88807 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:c5817a67967a632d77758fa90dfe3ab1c09e1d7c99a81f38ab54f
│                       │      │                   dc022ea694f 
│                       │      ├ Title           : libXrender: libXrender: Code injection via heap overflow in
│                       │      │                   RenderQueryPictFormats 
│                       │      ├ Description     : A heap overflow in libXrender before 0.9.13 in
│                       │      │                   RenderQueryPictFormats could be used by malicious X servers
│                       │      │                   to inject code into attached X clients. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-122
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 8.3 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-88807        
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libxrender/-/merge_re
│                       │      │                  quests/19                                                    
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-88807              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-88807              
│                       │      ├ PublishedDate   : 2026-09-21T14:17:22.41Z 
│                       │      ╰ LastModifiedDate: 2026-09-22T19:40:05.87Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-94286 
│                       │      ├ PkgID           : libxtst@1.2.5-r0 
│                       │      ├ PkgName         : libxtst 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxtst@1.2.5-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.2 
│                       │      │                  ╰ UID : ac79313a3705263d 
│                       │      ├ InstalledVersion: 1.2.5-r0 
│                       │      ├ FixedVersion    : 1.2.6-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94286 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:9cd8944a51ddaf104e6a77f0aab405d9c6e5a50f73122198f3e98
│                       │      │                   bbdae665324 
│                       │      ├ Title           : libXtst: libXtst: Denial of Service via out-of-bounds read
│                       │      │                   in RECORD reply parser 
│                       │      ├ Description     : An out-of-bounds read in libXtst's RECORD reply parser in
│                       │      │                   libXtst before 1.2.6 could be used by malicious X servers to
│                       │      │                    crash attached X clients. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-126
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.1 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-94286         
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libxtst/-/merge_reques
│                       │      │                  ts/10                                                         
│                       │      │                  https://gitlab.freedesktop.org/xorg/lib/libxtst/-/merge_reques
│                       │      │                  ts/10/diffs?commit_id=16023c86070e6af9407330deea3938fcef75815b
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94286               
│                       │      │                                                                                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94286               
│                       │      ├ PublishedDate   : 2026-09-28T09:17:08.463Z 
│                       │      ╰ LastModifiedDate: 2026-09-30T13:17:26.71Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-109088 
│                       │      ├ PkgID           : libxtst@1.2.5-r0 
│                       │      ├ PkgName         : libxtst 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxtst@1.2.5-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.2 
│                       │      │                  ╰ UID : ac79313a3705263d 
│                       │      ├ InstalledVersion: 1.2.5-r0 
│                       │      ├ FixedVersion    : 1.2.6-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:b1030c26abfb74ef3bc333f0585ea6703a4bcbb63653affd1642d
│                       │      │                   234bbb99544 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-96512 
│                       │      ├ PkgID           : sudo@1.9.17_p2-r1 
│                       │      ├ PkgName         : sudo 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/sudo@1.9.17_p2-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.2 
│                       │      │                  ╰ UID : 65e70d20e0b4f9aa 
│                       │      ├ InstalledVersion: 1.9.17_p2-r1 
│                       │      ├ FixedVersion    : 1.9.17_p2-r2 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                       │      │                  │         b772a5753e7fc58e07fb 
│                       │      │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                       │      │                            94e87222bd569e980daf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-96512 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:1882bd23dd1ba076e4756f212047a86a415b9d2c2e82a4d52face
│                       │      │                   c0bab1771b1 
│                       │      ├ Title           : sudo: sudo: TZ environment variable allows bypass of
│                       │      │                   NOTBEFORE/NOTAFTER time-based authorization 
│                       │      ├ Description     : A flaw was found in sudo. When sudoers rules use NOTBEFORE
│                       │      │                   or NOTAFTER time-based access restrictions with timestamps
│                       │      │                   that omit the trailing 'Z' timezone indicator, the time
│                       │      │                   evaluation relies on the TZ environment variable inherited
│                       │      │                   from the calling user. Because sudo is a setuid-root
│                       │      │                   program, an unprivileged local user can set TZ to an extreme
│                       │      │                    timezone offset to shift the authorization window by up to
│                       │      │                   approximately 25 hours, causing expired rules to be treated
│                       │      │                   as valid. This allows the user to execute commands outside
│                       │      │                   the intended time window. Authentication is not bypassed;
│                       │      │                   only the time-based authorization check is affected. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-863
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.8 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/09/24/4      
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:71609             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:75571             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:75579             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:75580             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:82939             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-96512        
│                       │      │                  https://bugzilla.redhat.com/2539327                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2539327          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-96512
│                       │      │                  https://errata.almalinux.org/8/ALSA-2026-75580.html          
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:75571                
│                       │      │                  https://github.com/sudo-project/sudo/commit/1820a349687522f51
│                       │      │                  023d1ae5925125f59679a8c                                      
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-96512.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-75580.html         
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-96512              
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8895-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-96512              
│                       │      ├ PublishedDate   : 2026-09-23T14:17:10.747Z 
│                       │      ╰ LastModifiedDate: 2026-10-14T19:17:23.22Z 
│                       ╰ [17] ╭ VulnerabilityID : CVE-2026-85091 
│                              ├ PkgID           : zlib@1.3.2-r0 
│                              ├ PkgName         : zlib 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/zlib@1.3.2-r0?arch=x86_64&distro=3.24.2 
│                              │                  ╰ UID : e37054a2982d6c16 
│                              ├ InstalledVersion: 1.3.2-r0 
│                              ├ FixedVersion    : 1.3.2-r1 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:b2cfc9a93ca5dedfcef9911da39297021e10c54a2d71
│                              │                  │         b772a5753e7fc58e07fb 
│                              │                  ╰ DiffID: sha256:f0d92923b340c27f4141728a2cdf3c7db3c463279c5c
│                              │                            94e87222bd569e980daf 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-85091 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Fingerprint     : sha256:269988755ea31f816ad4796a58113eaa39b8649b2d6caffbd565b
│                              │                   4bdca00d776 
│                              ├ Title           : zlib versions 1.3.1.2 through 1.3.2 contain a heap buffer
│                              │                   overflow vul ... 
│                              ├ Description     : zlib versions 1.3.1.2 through 1.3.2 contain a heap buffer
│                              │                   overflow vulnerability in the gz_vacate() function when
│                              │                   processing non-blocking gzwrite() operations with stale
│                              │                   external buffer pointers. Attackers can trigger the overflow
│                              │                    by calling gzprintf() or gzvprintf() after a write stall,
│                              │                   causing an unchecked memmove() to write beyond the internal
│                              │                   input buffer boundary. 
│                              ├ Severity        : MEDIUM 
│                              ├ CweIDs                  
│                              │                  ───────
│                              │                  CWE-787
│                              ├ VendorSeverity   ─ ubuntu: 2 
│                              ├ References                                                                    
│                              │                  ─────────────────────────────────────────────────────────────
│                              │                  https://gist.github.com/thesmartshadow/e0b9481792afb7c31e86fe
│                              │                  e1ff084490                                                   
│                              │                  https://github.com/madler/zlib                               
│                              │                                                                               
│                              │                  https://github.com/madler/zlib/blob/v1.3.2/gzwrite.c#L393    
│                              │                                                                               
│                              │                  https://www.cve.org/CVERecord?id=CVE-2026-85091              
│                              │                                                                               
│                              │                  https://www.vulncheck.com/advisories/zlib-1.3.1.2-through-1.3
│                              │                  .2-heap-buffer-overflow-via-gz-vacate                        
│                              ├ PublishedDate   : 2026-09-03T13:06:20.573Z 
│                              ╰ LastModifiedDate: 2026-09-09T20:41:07.123Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages 
```
