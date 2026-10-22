```yaml
╭ [0] ╭ Target         : openaf/ojobrt:latest (alpine 3.24.2) 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-88806 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:7e9dbef6b8e3cff23ecdcc4fac0f2e059135046b4ebe0d1da77fa
│                       │      │                   3bcaa0a5113 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94283 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:175cff6c07812d31f036ba8e5d856273f18daec26429a752222ae
│                       │      │                   3237392fad1 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94284 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:97faf74967b74c7bfc34dbf883bb890b6044d9b097e8278976e7b
│                       │      │                   8f95957967d 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94285 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:65bc86825eb925a46aec611e80cadb722b08b4439fbbcb24f57ea
│                       │      │                   187bb9f2fc7 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-93541 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:f1364d9a5e8953d0a3b6a58f63823017e8dd4bc2f1e53a48084d5
│                       │      │                   b7a6e6927fb 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-93542 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:eb36bba60b2b145f2c7a42835be74963dc21031e6ed747a8915e0
│                       │      │                   df55486f51a 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-93543 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:d741f9a7a7e18f3df7b32ce25d14eedd91dea8dbbae2d870afd22
│                       │      │                   d204e60cb33 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-93544 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:966ac9811992140ddcd114a8821d1631ee423b008475d44687be1
│                       │      │                   74fe8ccac39 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-93545 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:4537229b59f610ec76bfc916db84fe3fc91925d6e2da865106b98
│                       │      │                   c22137d7578 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94281 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:6e37c00e1e98a735eb8478db61191f63e543f8c6e14a11c439b26
│                       │      │                   72c2170f7e1 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94282 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:acf2c25716794bbf74222bff7e49d28029ef28b9290893b23e881
│                       │      │                   daf8714742e 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:a2440862a5dc725ea6656563ece3a9b010cc2aefade17bd7e59d7
│                       │      │                   55718a32a3f 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-109090 
│                       │      ├ PkgID           : libxi@1.8.3-r0 
│                       │      ├ PkgName         : libxi 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libxi@1.8.3-r0?arch=x86_64&distro=3.24.2 
│                       │      │                  ╰ UID : 48645fd8596750c6 
│                       │      ├ InstalledVersion: 1.8.3-r0 
│                       │      ├ FixedVersion    : 1.8.4-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:0b8cfedfb2b09e1b9ce6867efcb5aca4584e2ed86e586183e5574
│                       │      │                   e341c1a5215 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-88807 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:dc978fa803bd043de177b66876adae67d8e3b4edcd99844078fce
│                       │      │                   66276feda7c 
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94286 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:f1c25b71d3037ab4f44546fc9edf549ef75e204941ffcd6745440
│                       │      │                   995237187e4 
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8939-1                
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
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8e79b1c13d76c282de262af36459aa173656fc54ef94ec66b1eeb
│                       │      │                   ea077100aa8 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-107891 
│                       │      ├ PkgID           : musl@1.2.6-r2 
│                       │      ├ PkgName         : musl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/musl@1.2.6-r2?arch=x86_64&distro=3.24.2 
│                       │      │                  ╰ UID : 1f8cb44befe503d4 
│                       │      ├ InstalledVersion: 1.2.6-r2 
│                       │      ├ FixedVersion    : 1.2.6-r3 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:669ed1895ea880e404ee04ca8a57d22bd6419ef9b2fea67d5cfe5
│                       │      │                   6b52d018969 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [17] ╭ VulnerabilityID : CVE-2026-107891 
│                       │      ├ PkgID           : musl-utils@1.2.6-r2 
│                       │      ├ PkgName         : musl-utils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/musl-utils@1.2.6-r2?arch=x86_64&distro
│                       │      │                  │       =3.24.2 
│                       │      │                  ╰ UID : 4497482ec1d943e1 
│                       │      ├ InstalledVersion: 1.2.6-r2 
│                       │      ├ FixedVersion    : 1.2.6-r3 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:d0ce7df0bbc4295d4f953db44862f653fbf1e93c45102ab9e4672
│                       │      │                   18e97ca1ae6 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [18] ╭ VulnerabilityID : CVE-2026-96512 
│                       │      ├ PkgID           : sudo@1.9.17_p2-r1 
│                       │      ├ PkgName         : sudo 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/sudo@1.9.17_p2-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.2 
│                       │      │                  ╰ UID : 65e70d20e0b4f9aa 
│                       │      ├ InstalledVersion: 1.9.17_p2-r1 
│                       │      ├ FixedVersion    : 1.9.17_p2-r2 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                       │      │                  │         70772c2c9ce47dd20dfa 
│                       │      │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                       │      │                            448bbddb4b955424efcf 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-96512 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:167b6f5c36fe91a82c0336b83e0888ca62cf03645e7212b033293
│                       │      │                   8e9929209e4 
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
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:86634             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:86635             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:87026             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-96512        
│                       │      │                  https://bugzilla.redhat.com/2539327                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2539327          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-96512
│                       │      │                  https://errata.almalinux.org/8/ALSA-2026-75580.html          
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:75579                
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
│                       │      ╰ LastModifiedDate: 2026-10-21T20:17:28.187Z 
│                       ╰ [19] ╭ VulnerabilityID : CVE-2026-85091 
│                              ├ PkgID           : zlib@1.3.2-r0 
│                              ├ PkgName         : zlib 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/zlib@1.3.2-r0?arch=x86_64&distro=3.24.2 
│                              │                  ╰ UID : e37054a2982d6c16 
│                              ├ InstalledVersion: 1.3.2-r0 
│                              ├ FixedVersion    : 1.3.2-r1 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:cdbdeb8af7c2e6fdc7d7056c36b61be46938b2b96c23
│                              │                  │         70772c2c9ce47dd20dfa 
│                              │                  ╰ DiffID: sha256:7483f921077bf2164f41fdfb9fe5588e4430652971ff
│                              │                            448bbddb4b955424efcf 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-85091 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Fingerprint     : sha256:4da877efb1c19d18a7459a0e07e8ebf31fd67c0aa256f4735dd2d
│                              │                   b7efce8c2bb 
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
