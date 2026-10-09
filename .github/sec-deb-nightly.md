```yaml
╭ [0] ╭ Target         : openaf/oaf:deb-nightly (ubuntu 26.04) 
│     ├ Class          : os-pkgs 
│     ├ Type           : ubuntu 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-18374 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2.4?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04 
│                       │      │                  ╰ UID : b964ecf8d3a43faa 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:402e7e3125bd86b8ff3f21febcb78440d52e295f5a74260971599
│                       │      │                   9f7a0ef544e 
│                       │      ├ Title           : glibc: glibc: Heap buffer overflow via attacker-controlled
│                       │      │                   fopen mode string 
│                       │      ├ Description     : Passing an effectively empty string to the `,ccs=` syntax
│                       │      │                   extension of the mode argument in the `fopen` function in
│                       │      │                   the GNU C Library version 2.45 or earlier may result in a
│                       │      │                   heap buffer overflow when the mode string input to the
│                       │      │                   function is attacker controlled.
│                       │      │                   
│                       │      │                   This usage pattern is not seen in applications in common
│                       │      │                   GNU/Linux distributions and applications that process
│                       │      │                   user-supplied values for `ccs` should not pass them through
│                       │      │                   without validation. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-787
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/08/27/6      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18374        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18374              
│                       │      │                  https://sourceware.org/bugzilla/show_bug.cgi?id=34574        
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/G
│                       │      │                  LIBC-SA-2026-0015                                            
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=adviso
│                       │      │                  ries/GLIBC-SA-2026-0015                                      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18374              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-27T20:17:03.553Z 
│                       │      ╰ LastModifiedDate: 2026-09-03T16:43:15.293Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-89092 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2.4?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04 
│                       │      │                  ╰ UID : b964ecf8d3a43faa 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89092 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:1a1836f2980b4157860643be2096b0bce39ce56f61c0384b36803
│                       │      │                   be527ae726c 
│                       │      ├ Title           : glibc: nscd stack overflow leads to degraded DNS resolution 
│                       │      ├ Description     : The nscd service in the GNU C Library 2.3.4 onwards may
│                       │      │                   crash due to a 
│                       │      │                   stack overflow when a malicious DNS server returns too large
│                       │      │                    a response 
│                       │      │                   for a DNS query, resulting in degraded DNS resolution for
│                       │      │                   the system.
│                       │      │                   
│                       │      │                   Exploitation of this bug needs a system that has nscd
│                       │      │                   enabled and using 
│                       │      │                   an untrusted DNS server for name resolution, with the
│                       │      │                   compromised DNS 
│                       │      │                   server being capable of processing records large enough to
│                       │      │                   result in a 
│                       │      │                   stack overflow in an nscd thread stack.  During
│                       │      │                   experimentation, bind 9 
│                       │      │                   was unable to handle large records, but that could change in
│                       │      │                    future or 
│                       │      │                   with a different name server.  In typical installations,
│                       │      │                   nscd is 
│                       │      │                   executed in an isolated context as its own user without a
│                       │      │                   shell, due to 
│                       │      │                   which any compromise of that service is isolated.
│                       │      │                   There is a remote possibility of nscd cache corruption if an
│                       │      │                    attacker 
│                       │      │                   manages to get the stack pointer into a desired point in the
│                       │      │                    heap, 
│                       │      │                   potentially resulting in other caches in nscd being
│                       │      │                   overwritten with 
│                       │      │                   corrupt data through the stack overflow, until the buggy
│                       │      │                   code path 
│                       │      │                   eventually results in a crash.
│                       │      │                   Finally, a crash in nscd may result in performance
│                       │      │                   degradation when 
│                       │      │                   resolving names, but it does not result in a denial of
│                       │      │                   service. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-789
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/09/11/2      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89092        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89092              
│                       │      │                  https://sourceware.org/bugzilla/show_bug.cgi?id=34624        
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/G
│                       │      │                  LIBC-SA-2026-0016                                            
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=adviso
│                       │      │                  ries/GLIBC-SA-2026-0016                                      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89092              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-11T02:18:35.46Z 
│                       │      ╰ LastModifiedDate: 2026-09-11T18:17:00.23Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-18374 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       .4?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : bbb7a8f7a59474e8 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c1495d017afc3f4af42825a82e176cd96d6d09288fc9cfddb0dc0
│                       │      │                   151173a5738 
│                       │      ├ Title           : glibc: glibc: Heap buffer overflow via attacker-controlled
│                       │      │                   fopen mode string 
│                       │      ├ Description     : Passing an effectively empty string to the `,ccs=` syntax
│                       │      │                   extension of the mode argument in the `fopen` function in
│                       │      │                   the GNU C Library version 2.45 or earlier may result in a
│                       │      │                   heap buffer overflow when the mode string input to the
│                       │      │                   function is attacker controlled.
│                       │      │                   
│                       │      │                   This usage pattern is not seen in applications in common
│                       │      │                   GNU/Linux distributions and applications that process
│                       │      │                   user-supplied values for `ccs` should not pass them through
│                       │      │                   without validation. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-787
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/08/27/6      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18374        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18374              
│                       │      │                  https://sourceware.org/bugzilla/show_bug.cgi?id=34574        
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/G
│                       │      │                  LIBC-SA-2026-0015                                            
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=adviso
│                       │      │                  ries/GLIBC-SA-2026-0015                                      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18374              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-27T20:17:03.553Z 
│                       │      ╰ LastModifiedDate: 2026-09-03T16:43:15.293Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-89092 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       .4?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : bbb7a8f7a59474e8 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89092 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e8026e8a35c5c75f13b09c2a0bfbfcd7e9cb89b94e3efd60aa36d
│                       │      │                   f0df02bd833 
│                       │      ├ Title           : glibc: nscd stack overflow leads to degraded DNS resolution 
│                       │      ├ Description     : The nscd service in the GNU C Library 2.3.4 onwards may
│                       │      │                   crash due to a 
│                       │      │                   stack overflow when a malicious DNS server returns too large
│                       │      │                    a response 
│                       │      │                   for a DNS query, resulting in degraded DNS resolution for
│                       │      │                   the system.
│                       │      │                   
│                       │      │                   Exploitation of this bug needs a system that has nscd
│                       │      │                   enabled and using 
│                       │      │                   an untrusted DNS server for name resolution, with the
│                       │      │                   compromised DNS 
│                       │      │                   server being capable of processing records large enough to
│                       │      │                   result in a 
│                       │      │                   stack overflow in an nscd thread stack.  During
│                       │      │                   experimentation, bind 9 
│                       │      │                   was unable to handle large records, but that could change in
│                       │      │                    future or 
│                       │      │                   with a different name server.  In typical installations,
│                       │      │                   nscd is 
│                       │      │                   executed in an isolated context as its own user without a
│                       │      │                   shell, due to 
│                       │      │                   which any compromise of that service is isolated.
│                       │      │                   There is a remote possibility of nscd cache corruption if an
│                       │      │                    attacker 
│                       │      │                   manages to get the stack pointer into a desired point in the
│                       │      │                    heap, 
│                       │      │                   potentially resulting in other caches in nscd being
│                       │      │                   overwritten with 
│                       │      │                   corrupt data through the stack overflow, until the buggy
│                       │      │                   code path 
│                       │      │                   eventually results in a crash.
│                       │      │                   Finally, a crash in nscd may result in performance
│                       │      │                   degradation when 
│                       │      │                   resolving names, but it does not result in a denial of
│                       │      │                   service. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-789
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/09/11/2      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89092        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89092              
│                       │      │                  https://sourceware.org/bugzilla/show_bug.cgi?id=34624        
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/G
│                       │      │                  LIBC-SA-2026-0016                                            
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=adviso
│                       │      │                  ries/GLIBC-SA-2026-0016                                      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89092              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-11T02:18:35.46Z 
│                       │      ╰ LastModifiedDate: 2026-09-11T18:17:00.23Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-18374 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2.4?arch=amd64&distr
│                       │      │                  │       o=ubuntu-26.04 
│                       │      │                  ╰ UID : fe574f54c2bc3102 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:23b852fdd681441ed2c73df60ab97f2ad7940a909b73964fe9a57
│                       │      │                   01d110410a5 
│                       │      ├ Title           : glibc: glibc: Heap buffer overflow via attacker-controlled
│                       │      │                   fopen mode string 
│                       │      ├ Description     : Passing an effectively empty string to the `,ccs=` syntax
│                       │      │                   extension of the mode argument in the `fopen` function in
│                       │      │                   the GNU C Library version 2.45 or earlier may result in a
│                       │      │                   heap buffer overflow when the mode string input to the
│                       │      │                   function is attacker controlled.
│                       │      │                   
│                       │      │                   This usage pattern is not seen in applications in common
│                       │      │                   GNU/Linux distributions and applications that process
│                       │      │                   user-supplied values for `ccs` should not pass them through
│                       │      │                   without validation. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-787
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/08/27/6      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18374        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18374              
│                       │      │                  https://sourceware.org/bugzilla/show_bug.cgi?id=34574        
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/G
│                       │      │                  LIBC-SA-2026-0015                                            
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=adviso
│                       │      │                  ries/GLIBC-SA-2026-0015                                      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18374              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-27T20:17:03.553Z 
│                       │      ╰ LastModifiedDate: 2026-09-03T16:43:15.293Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-89092 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2.4?arch=amd64&distr
│                       │      │                  │       o=ubuntu-26.04 
│                       │      │                  ╰ UID : fe574f54c2bc3102 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89092 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:82311951888239c21c9922f83f5aed818d023f572bb7123a9ef2e
│                       │      │                   3f7fa0db1a4 
│                       │      ├ Title           : glibc: nscd stack overflow leads to degraded DNS resolution 
│                       │      ├ Description     : The nscd service in the GNU C Library 2.3.4 onwards may
│                       │      │                   crash due to a 
│                       │      │                   stack overflow when a malicious DNS server returns too large
│                       │      │                    a response 
│                       │      │                   for a DNS query, resulting in degraded DNS resolution for
│                       │      │                   the system.
│                       │      │                   
│                       │      │                   Exploitation of this bug needs a system that has nscd
│                       │      │                   enabled and using 
│                       │      │                   an untrusted DNS server for name resolution, with the
│                       │      │                   compromised DNS 
│                       │      │                   server being capable of processing records large enough to
│                       │      │                   result in a 
│                       │      │                   stack overflow in an nscd thread stack.  During
│                       │      │                   experimentation, bind 9 
│                       │      │                   was unable to handle large records, but that could change in
│                       │      │                    future or 
│                       │      │                   with a different name server.  In typical installations,
│                       │      │                   nscd is 
│                       │      │                   executed in an isolated context as its own user without a
│                       │      │                   shell, due to 
│                       │      │                   which any compromise of that service is isolated.
│                       │      │                   There is a remote possibility of nscd cache corruption if an
│                       │      │                    attacker 
│                       │      │                   manages to get the stack pointer into a desired point in the
│                       │      │                    heap, 
│                       │      │                   potentially resulting in other caches in nscd being
│                       │      │                   overwritten with 
│                       │      │                   corrupt data through the stack overflow, until the buggy
│                       │      │                   code path 
│                       │      │                   eventually results in a crash.
│                       │      │                   Finally, a crash in nscd may result in performance
│                       │      │                   degradation when 
│                       │      │                   resolving names, but it does not result in a denial of
│                       │      │                   service. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-789
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/09/11/2      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89092        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89092              
│                       │      │                  https://sourceware.org/bugzilla/show_bug.cgi?id=34624        
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/G
│                       │      │                  LIBC-SA-2026-0016                                            
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=adviso
│                       │      │                  ries/GLIBC-SA-2026-0016                                      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89092              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-11T02:18:35.46Z 
│                       │      ╰ LastModifiedDate: 2026-09-11T18:17:00.23Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2025-66382 
│                       │      ├ PkgID           : libexpat1@2.7.4-1ubuntu0.2 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1ubuntu0.2?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 1019b85f746342f4 
│                       │      ├ InstalledVersion: 2.7.4-1ubuntu0.2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-66382 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:092af17660c932f921c24dda8fb4b5c2badb5bf6b6523a24d5636
│                       │      │                   b6c593a793f 
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
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-13757 
│                       │      ├ PkgID           : libp11-kit0@0.26.2-2 
│                       │      ├ PkgName         : libp11-kit0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libp11-kit0@0.26.2-2?arch=amd64&distro
│                       │      │                  │       =ubuntu-26.04 
│                       │      │                  ╰ UID : 39936f33632ab742 
│                       │      ├ InstalledVersion: 0.26.2-2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13757 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:285b3dfedef6b304314be02e068729985d03e3afa623e6db8442a
│                       │      │                   18f830e9ce7 
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
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:58981             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72394             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72395             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72399             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72470             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72475             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72476             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72502             
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8687-1               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-13757              
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-29T19:16:40.907Z 
│                       │      ╰ LastModifiedDate: 2026-09-29T01:16:45.04Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-86145 
│                       │      ├ PkgID           : libpcre2-8-0@10.46-1build1 
│                       │      ├ PkgName         : libpcre2-8-0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpcre2-8-0@10.46-1build1?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c9d0d8772a6e5e1d 
│                       │      ├ InstalledVersion: 10.46-1build1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-86145 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:666b1d2b69ef26278108a52b10716a0ac3ab7bddbca0f1ef7da1c
│                       │      │                   f717939e624 
│                       │      ├ Title           : pcre2: PCRE2: Out-of-bounds write allows arbitrary code
│                       │      │                   execution via crafted regular expressions 
│                       │      ├ Description     : PCRE2 before 10.48 allows a pcre2_dfa_match out-of-bounds
│                       │      │                   write because reuse of a cached workspace block, in a
│                       │      │                   recursive DFA matching workspace, lacks a size check (even
│                       │      │                   though a newly allocated block, for the same purpose, does
│                       │      │                   have a size check). This outcome requires an
│                       │      │                   attacker-controlled regular expression, or a recursive
│                       │      │                   pattern in conjunction with a small heap limit (this can be
│                       │      │                   set through the API). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-424
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 3 
│                       │      │                  ├ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 8.2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/09/05/3      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-86145        
│                       │      │                  https://github.com/PCRE2Project/pcre2/releases/tag/pcre2-10.4
│                       │      │                  8                                                            
│                       │      │                  https://github.com/PCRE2Project/pcre2/security/advisories/GHS
│                       │      │                  A-3r4p-g7gg-ppmf                                             
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-86145              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-86145              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-05T06:17:10.37Z 
│                       │      ╰ LastModifiedDate: 2026-09-09T16:04:24.933Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-89161 
│                       │      ├ PkgID           : libpcre2-8-0@10.46-1build1 
│                       │      ├ PkgName         : libpcre2-8-0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpcre2-8-0@10.46-1build1?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c9d0d8772a6e5e1d 
│                       │      ├ InstalledVersion: 10.46-1build1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89161 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a7db964650fc42f097e8fd3ad9db440fd9ded7c863f8778ca4e23
│                       │      │                   2d29a22bf77 
│                       │      ├ Title           : pcre2: PCRE2: Memory corruption vulnerability in
│                       │      │                   pcre2_jit_match 
│                       │      ├ Description     : In PCRE2 before 10.48, pcre2_jit_match mishandles a
│                       │      │                   previously copied subject being passed in as a context. An
│                       │      │                   incorrect free operation can occur. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-590
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ nvd   : 3 
│                       │      │                  ├ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.8 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89161        
│                       │      │                  https://github.com/PCRE2Project/pcre2/commit/1dcd0cf42a6a7cb6
│                       │      │                  2cc9a7c024196733abcfda95%20%28pcre2-10.48-RC1%29             
│                       │      │                  https://github.com/PCRE2Project/pcre2/pull/937               
│                       │      │                                                                               
│                       │      │                  https://github.com/PCRE2Project/pcre2/releases/tag/pcre2-10.4
│                       │      │                  8                                                            
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89161              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89161              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-11T04:18:04.47Z 
│                       │      ╰ LastModifiedDate: 2026-09-16T19:10:47.78Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libsystemd0@259.5-0ubuntu3.4 
│                       │      ├ PkgName         : libsystemd0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsystemd0@259.5-0ubuntu3.4?arch=amd6
│                       │      │                  │       4&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8e41c7d584057e32 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:2033003981cfbfb82d55542f9fd7f4896eb14f92a8490fa484527
│                       │      │                   3f0d5c37a20 
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
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libudev1@259.5-0ubuntu3.4 
│                       │      ├ PkgName         : libudev1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libudev1@259.5-0ubuntu3.4?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : db6ded6155f534fe 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e9fbd8c2b2ad71c40b8225234be9f23db07aa595cc046de7d0ec4
│                       │      │                   c31bbaa8afc 
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
│                       ├ [12] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : login.defs@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : login.defs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login.defs@4.17.4-2ubuntu3?arch=all&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : eaf648d5e4e975f7 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:9bb70548645ac83580d04b2caae56657deb77e8721ed7cb148af5
│                       │      │                   a77e2636b93 
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
│                       ├ [13] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : passwd@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : passwd 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/passwd@4.17.4-2ubuntu3?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : 12ffbe3e135ac553 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c67258cd0047933f151731db971045fd995983c89aecfe759113b
│                       │      │                   b708dac9b3f 
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
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-35341 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35341 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c535138840fbfd1bd31fce7199916e80550c2aee44233d8e82b7c
│                       │      │                   ea4a2f2d191 
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
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-35344 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35344 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:024fc149b46d5dfae7cc15f87c41cac38c56478921c2f520fb874
│                       │      │                   eaabaa44608 
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
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-35345 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35345 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:34f9edfdf69bce87ed84d5e30710894cbad56264f01391d7aa3da
│                       │      │                   3036ad9b27e 
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
│                       ├ [17] ╭ VulnerabilityID : CVE-2026-35348 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35348 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6172cedd390beea4121ccbc14e904c1fd6e920404eb14036c8e2e
│                       │      │                   60ae1cefc2f 
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
│                       ├ [18] ╭ VulnerabilityID : CVE-2026-35350 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35350 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0f931d58e154e91f9230836c92b9820bf93bc2bdbba82d54bb5aa
│                       │      │                   4edc32acb02 
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
│                       ├ [19] ╭ VulnerabilityID : CVE-2026-35351 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35351 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0f8327c0ac911a5ec54b9fb69ce66c15473b2120dd035cdf07fbb
│                       │      │                   21e5267410b 
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
│                       ├ [20] ╭ VulnerabilityID : CVE-2026-35352 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35352 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:89f35a6c65d38f28c8fb3155f0d7f16dbdbc6a52d39dfd66ca65a
│                       │      │                   42afbcd5363 
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
│                       ├ [21] ╭ VulnerabilityID : CVE-2026-35354 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35354 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:17c184d5961603c35e3ac9f8d943c257e3285135839877857dc2d
│                       │      │                   878dbc87481 
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
│                       ├ [22] ╭ VulnerabilityID : CVE-2026-35357 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35357 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:317b1b64caf9556395822c1ca1629019124f5643c25daf7ee7187
│                       │      │                   d010d897722 
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
│                       ├ [23] ╭ VulnerabilityID : CVE-2026-35359 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35359 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b7093b40ff4d582d03d7ef942975eac9726f9dd239036d61ee3c9
│                       │      │                   f8c66bc0d67 
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
│                       ├ [24] ╭ VulnerabilityID : CVE-2026-35360 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35360 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5dfc683593aea135e958df996dca20f418985fd2d3c52b589fef6
│                       │      │                   aa07a3f0865 
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
│                       ├ [25] ╭ VulnerabilityID : CVE-2026-35363 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35363 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d011f2253285fa95986b724c8cdaba878ad146fffa9a10359cda8
│                       │      │                   5872dca0781 
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
│                       ├ [26] ╭ VulnerabilityID : CVE-2026-35364 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35364 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:fca457ad5bf571b4d208c922bb5ea8dfa3e5629c8c3ea131d2169
│                       │      │                   c74a780c8aa 
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
│                       ├ [27] ╭ VulnerabilityID : CVE-2026-35367 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35367 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3c5a737384552e3b39b915faba2daea11011f66183ac181d4ffb5
│                       │      │                   13ce7f3d2de 
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
│                       ├ [28] ╭ VulnerabilityID : CVE-2026-35368 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35368 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b8698e17cd5ad95e39bed1c5abc3ade0c58b718657a02e0dc6eb9
│                       │      │                   d2183625a1b 
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
│                       ├ [29] ╭ VulnerabilityID : CVE-2026-35370 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35370 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5888bbd870f08685aa5108d6858588741b6065ed16ecca8ce63bf
│                       │      │                   8b6bb73d754 
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
│                       ├ [30] ╭ VulnerabilityID : CVE-2026-35371 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35371 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b14cc285407209eb849dc0c5720b7c7bf2cc188760d82ad64e45b
│                       │      │                   bc47a9edbe6 
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
│                       ├ [31] ╭ VulnerabilityID : CVE-2026-35373 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35373 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:47e4bfe55118fbdeefe8b35f6552eb6579ece7372bd49346be524
│                       │      │                   f34d12c61ec 
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
│                       ├ [32] ╭ VulnerabilityID : CVE-2026-35374 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:8183815d40622ce98cdafcd5b251d3b4bb11795aae1f01842f8bd
│                       │      │                   cb3b2106291 
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
│                       ├ [33] ╭ VulnerabilityID : CVE-2026-35377 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35377 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:346446db4b1d484c11222a835801c3137598c7c3ed2b8ebf253a9
│                       │      │                   94972439f9b 
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
│                       ├ [34] ╭ VulnerabilityID : CVE-2026-18477 
│                       │      ├ PkgID           : tar@1.35+dfsg-4ubuntu0.4 
│                       │      ├ PkgName         : tar 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-4ubuntu0.4?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 5867f93e7d45b368 
│                       │      ├ InstalledVersion: 1.35+dfsg-4ubuntu0.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18477 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:fc0e3a57fa3c22531cf3a3167e9f66a9ed1bb5f075c6b2641369e
│                       │      │                   8089f707778 
│                       │      ├ Title           : tar: tar: TOCTOU in incremental dumpdir 'X' rename handling
│                       │      │                   allows restore path escape 
│                       │      ├ Description     : A TOCTOU (Time-of-Check Time-of-Use) vulnerability in GNU
│                       │      │                   tar's incremental dumpdir 'X' rename handling allows a local
│                       │      │                    attacker with write access to a directory being backed up
│                       │      │                   to influence the restore process if the attacker has access
│                       │      │                   to the system where the restore is being performed. During
│                       │      │                   restoration, files or directories may be created, renamed or
│                       │      │                    overwritten outside the intended extraction directory. This
│                       │      │                    could lead to unauthorized file modification or, in some
│                       │      │                   cases, privilege escalation. Exploitation does not require
│                       │      │                   the attacker to modify or craft the archive, and standard
│                       │      │                   backup and restore workflows—including extracting into a
│                       │      │                   newly created directory without using the -P option do not
│                       │      │                   mitigate the issue. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-367
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ julia      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:R/S:U/C:N/I:H
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.4 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:R/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.4 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:49361             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:61581             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:61586             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:61783             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:66018             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:70390             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18477        
│                       │      │                  https://bugzilla.redhat.com/2455360                          
│                       │      │                  https://bugzilla.redhat.com/2509735                          
│                       │      │                  https://bugzilla.redhat.com/2509843                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2455360          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2509735          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2509843          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-18477
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-18508
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-5704 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-61581.html          
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:61581                
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-18477.html             
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-70390.html         
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18477              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18477              
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-03T17:16:33.897Z 
│                       │      ╰ LastModifiedDate: 2026-09-22T22:17:11.233Z 
│                       ├ [35] ╭ VulnerabilityID : CVE-2026-18508 
│                       │      ├ PkgID           : tar@1.35+dfsg-4ubuntu0.4 
│                       │      ├ PkgName         : tar 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-4ubuntu0.4?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 5867f93e7d45b368 
│                       │      ├ InstalledVersion: 1.35+dfsg-4ubuntu0.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                       │      │                  │         1c655b6edf399db737b6 
│                       │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                       │      │                            832db8d941f10dfbb08b 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18508 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:4aac2c895cf6232ea875c0546376cb575e2f7d115ee19659083c8
│                       │      │                   232962dcff8 
│                       │      ├ Title           : tar: tar: --one-top-level hardlink targets not confined to
│                       │      │                   top-level directory enabling arbitrary file overwrite 
│                       │      ├ Description     : A flaw was found in GNU tar. When extracting an archive with
│                       │      │                    the --one-top-level option, hardlink targets are not
│                       │      │                   confined to the designated top-level directory and may
│                       │      │                   resolve relative to the extraction working directory. A
│                       │      │                   crafted archive can create hardlinks that escape the
│                       │      │                   intended boundary and, when combined with a preexisting
│                       │      │                   symbolic link under the working directory, may allow writing
│                       │      │                    outside that boundary during a single extraction. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                 
│                       │      │                  ──────
│                       │      │                  CWE-59
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.4 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:50807             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:61581             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:61586             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:61783             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:66018             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:70390             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18508        
│                       │      │                  https://bugzilla.redhat.com/2455360                          
│                       │      │                  https://bugzilla.redhat.com/2509735                          
│                       │      │                  https://bugzilla.redhat.com/2509843                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2455360          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2509735          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2509843          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-18477
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-18508
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-5704 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-61581.html          
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:61581                
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-18508.html             
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-70390.html         
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18508              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18508              
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-03T16:16:28.387Z 
│                       │      ╰ LastModifiedDate: 2026-09-22T22:17:11.493Z 
│                       ╰ [36] ╭ VulnerabilityID : CVE-2026-85091 
│                              ├ PkgID           : zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu3.1 
│                              ├ PkgName         : zlib1g 
│                              ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/zlib1g@1.3.dfsg%2Breally1.3.1-1ubuntu3
│                              │                  │       .1?arch=amd64&distro=ubuntu-26.04&epoch=1 
│                              │                  ╰ UID : a4f0bcc5ee12eaad 
│                              ├ InstalledVersion: 1:1.3.dfsg+really1.3.1-1ubuntu3.1 
│                              ├ Status          : affected 
│                              ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
│                              │                  │         1c655b6edf399db737b6 
│                              │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
│                              │                            832db8d941f10dfbb08b 
│                              ├ SeveritySource  : ubuntu 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-85091 
│                              ├ DataSource       ╭ ID  : ubuntu 
│                              │                  ├ Name: Ubuntu CVE Tracker 
│                              │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                              ├ Fingerprint     : sha256:6c23d1d26bf7d535a8066f15b85708aa34ac024c4c34b3d2f24f7
│                              │                   a49347c9087 
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
│                              │                  
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
│                              │                  
│                              ├ PublishedDate   : 2026-09-03T13:06:20.573Z 
│                              ╰ LastModifiedDate: 2026-09-09T20:41:07.123Z 
├ [1] ╭ Target  : Java 
│     ├ Class   : lang-pkgs 
│     ├ Type    : jar 
│     ╰ Packages 
╰ [2] ╭ Target         : usr/bin/pebble 
      ├ Class          : lang-pkgs 
      ├ Type           : gobinary 
      ├ Packages        
      ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-78667 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6609
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                        │      │                  │         1c655b6edf399db737b6 
                        │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                        │      │                            832db8d941f10dfbb08b 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78667 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:7bb8401375f18235936eb64d954c02323820d791da4cfd4918816
                        │      │                   692afcd75b4 
                        │      ├ Title           : net/http: golang: golang: Denial of Service via crafted HTTP
                        │      │                    Range headers 
                        │      ├ Description     : When parsing a Range header containing a large number of
                        │      │                   small ranges, FileServer(FS), ServeContent, and
                        │      │                   ServeFile(FS) can consume an excessive amount of CPU. 
                        │      ├ Severity        : HIGH 
                        │      ├ VendorSeverity   ─ redhat: 3 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                           │           /A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-78667    
                        │      │                  https://go.dev/cl/847309                                 
                        │      │                  https://go.dev/issue/81858                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-78667          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6609                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78667          
                        │      │                  
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.88Z 
                        │      ╰ LastModifiedDate: 2026-10-08T23:17:03.88Z 
                        ├ [1]  ╭ VulnerabilityID : CVE-2026-97031 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6607
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                        │      │                  │         1c655b6edf399db737b6 
                        │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                        │      │                            832db8d941f10dfbb08b 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97031 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:ed73ffe5aff0d31a252bae0c837e5bb3ebbd3b0784de6f20272c6
                        │      │                   d45538aafbe 
                        │      ├ Title           : crypto/tls: golang: crypto/tls: Denial of Service via
                        │      │                   multiple ECH outer extension references 
                        │      ├ Description     : Multiple ECH outer extension references are not permitted
                        │      │                   under RFC 9849; previously, a client could send a
                        │      │                   well-crafted packet that could trigger memory exhaustion in
                        │      │                   the server process by specifying multiple references. We now
                        │      │                    reject these as malformed and curb the memory amplification
                        │      │                    vector as a result. 
                        │      ├ Severity        : HIGH 
                        │      ├ VendorSeverity   ─ redhat: 3 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                           │           /A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-97031    
                        │      │                  https://go.dev/cl/847312                                 
                        │      │                  https://go.dev/issue/81855                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-97031          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6607                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-97031          
                        │      │                  
                        │      ├ PublishedDate   : 2026-10-08T23:17:06.037Z 
                        │      ╰ LastModifiedDate: 2026-10-08T23:17:06.037Z 
                        ├ [2]  ╭ VulnerabilityID : CVE-2026-94439 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6613
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                        │      │                  │         1c655b6edf399db737b6 
                        │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                        │      │                            832db8d941f10dfbb08b 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94439 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:a0825a35b12a10d4564bee755e90082fed5eedd9880639018a8de
                        │      │                   235395a2128 
                        │      ├ Title           : net/http: golang: net/http: HTTP request smuggling via
                        │      │                   improper handling of HTTP/1 CONNECT responses 
                        │      ├ Description     : When an HTTP server handler sends a 2xx response to an
                        │      │                   HTTP/1 CONNECT request and returns without hijacking the
                        │      │                   connection, the server improperly continues to read and
                        │      │                   serve requests from the connection. Since a 2xx response to
                        │      │                   an HTTP/1 CONNECT converts the connection into a tunnel, the
                        │      │                    server should not treat the connection as continuing to
                        │      │                   contain HTTP. The impact of this misbehavior is mostly
                        │      │                   limited to potential request smuggling, where an
                        │      │                   intermediate proxy considers the data on the connection to
                        │      │                   be tunneled and the server considers it to be HTTP. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ VendorSeverity   ─ redhat: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-94439    
                        │      │                  https://go.dev/cl/847311                                 
                        │      │                  https://go.dev/issue/81744                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94439          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6613                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94439          
                        │      │                  
                        │      ├ PublishedDate   : 2026-10-08T23:17:04.76Z 
                        │      ╰ LastModifiedDate: 2026-10-08T23:17:04.76Z 
                        ├ [3]  ╭ VulnerabilityID : CVE-2026-97032 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6617
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                        │      │                  │         1c655b6edf399db737b6 
                        │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                        │      │                            832db8d941f10dfbb08b 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97032 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:e6ebf2a33d52ae891f373fc0fb0eca8d3a462b166fc34af309dfc
                        │      │                   29671b1c73e 
                        │      ├ Title           : net/http: net/http/internal/http2: golang:
                        │      │                   golang.org/x/net/http2: net/http: Denial of Service via
                        │      │                   concurrent HPACK encoder modification 
                        │      ├ Description     : HTTP/2 servers could end up crashing due to inadvertently
                        │      │                   modifying its HPACK encoder concurrently. This happens
                        │      │                   because the server modifies the HPACK encoder from two
                        │      │                   goroutines without synchronization: one uses the encoder to
                        │      │                   encode a HEADERS frame as part of a response sent to a
                        │      │                   client and the other modifies the encoder's table size when
                        │      │                   handling a SETTINGS frame containing
                        │      │                   SETTINGS_HEADER_TABLE_SIZE that a client sends. A malicious
                        │      │                   client can repeatedly send a request while changing the
                        │      │                   header table size to crash the server. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ VendorSeverity   ─ redhat: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
                        │      │                           │           /A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-97032    
                        │      │                  https://go.dev/cl/847188                                 
                        │      │                  https://go.dev/cl/847313                                 
                        │      │                  https://go.dev/issue/81867                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-97032          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6617                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-97032          
                        │      │                  
                        │      ├ PublishedDate   : 2026-10-08T23:17:06.213Z 
                        │      ╰ LastModifiedDate: 2026-10-08T23:17:06.213Z 
                        ├ [4]  ╭ VulnerabilityID : CVE-2026-56857 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6604
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                        │      │                  │         1c655b6edf399db737b6 
                        │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                        │      │                            832db8d941f10dfbb08b 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56857 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:1161a1f25d3f3056b49d98c41483f3181942643699764b2393615
                        │      │                   8c1e0db90e4 
                        │      ├ Title           : Root.Mkdir(All) can follow junctions out of the root on
                        │      │                   Windows in os 
                        │      ├ Description     : On Windows, when the target of Root.Mkdir or Root.MkdirAll
                        │      │                   is a junction pointing to an empty location, the operation
                        │      │                   can create a directory at the junction target even when that
                        │      │                    target is located outside the root. This only applies to
                        │      │                   operations where the last path component is a junction
                        │      │                   (path/to/junction, but not path/junction/target). 
                        │      ├ Severity        : UNKNOWN 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://go.dev/cl/847305                                 
                        │      │                  https://go.dev/issue/81739                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6604                     
                        │      │                  
                        │      ├ PublishedDate   : 2026-10-08T23:17:01.487Z 
                        │      ╰ LastModifiedDate: 2026-10-08T23:17:01.487Z 
                        ├ [5]  ╭ VulnerabilityID : CVE-2026-56866 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6605
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                        │      │                  │         1c655b6edf399db737b6 
                        │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                        │      │                            832db8d941f10dfbb08b 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56866 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:a26f109910d726483272a26aa8d11c262c69ba70cf24693d1829c
                        │      │                   d24da18805d 
                        │      ├ Title           : When http.Transport sends an HTTP/1 CONNECT request with a
                        │      │                   non-empty R ... 
                        │      ├ Description     : When http.Transport sends an HTTP/1 CONNECT request with a
                        │      │                   non-empty Request.Body, it writes the body directly to the
                        │      │                   connection without framing after the request headers. If the
                        │      │                    server rejects the CONNECT request with a non-2xx
                        │      │                   keep-alive response, Transport returns the connection to the
                        │      │                    idle pool. Because CONNECT requests do not have a request
                        │      │                   body, the server may interpret the trailing body bytes as a
                        │      │                   subsequent pipelined HTTP/1.1 request on the connection,
                        │      │                   leaving the pooled connection desynchronized and causing the
                        │      │                    next caller that reuses it to read the response to the
                        │      │                   injected request. In reverse proxies (including
                        │      │                   httputil.ReverseProxy) that forward CONNECT requests through
                        │      │                    a shared Transport, this can lead to cross-user response
                        │      │                   poisoning. 
                        │      ├ Severity        : UNKNOWN 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://go.dev/cl/847306                                 
                        │      │                  https://go.dev/issue/81740                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6605                     
                        │      │                  
                        │      ├ PublishedDate   : 2026-10-08T23:17:01.62Z 
                        │      ╰ LastModifiedDate: 2026-10-08T23:17:01.62Z 
                        ├ [6]  ╭ VulnerabilityID : CVE-2026-78659 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6603
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                        │      │                  │         1c655b6edf399db737b6 
                        │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                        │      │                            832db8d941f10dfbb08b 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78659 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:6f46a56f89280e339f5020de6d9af93ce702a52f3e83b87999d9b
                        │      │                   d8bf46acf0a 
                        │      ├ Title           : When "Trailer" headers are sent by a client, the HTTP server
                        │      │                    internall ... 
                        │      ├ Description     : When "Trailer" headers are sent by a client, the HTTP server
                        │      │                    internally uses the header values to populate the
                        │      │                   Request.Trailer map passed to the server handler. Because
                        │      │                   Request.Trailer is a map, each entry incurs memory overhead.
                        │      │                    For HTTP/2 servers, a malicious client can exploit this by
                        │      │                   sending a "Trailer" header that declares a large number of
                        │      │                   fields, causing the server to allocate a disproportionate
                        │      │                   amount of memory while bypassing Server.MaxHeaderValueCount
                        │      │                   and Server.MaxHeaderBytes limits. This exploit is not
                        │      │                   applicable for HTTP/1 servers, which do not support
                        │      │                   multiplexing a large number of requests over one TCP
                        │      │                   connection, and whose Server.MaxHeaderBytes are calculated
                        │      │                   differently. 
                        │      ├ Severity        : UNKNOWN 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://go.dev/cl/847185                                 
                        │      │                  https://go.dev/cl/847314                                 
                        │      │                  https://go.dev/issue/81857                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6603                     
                        │      │                  
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.27Z 
                        │      ╰ LastModifiedDate: 2026-10-08T23:17:03.27Z 
                        ├ [7]  ╭ VulnerabilityID : CVE-2026-78660 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6610
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                        │      │                  │         1c655b6edf399db737b6 
                        │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                        │      │                            832db8d941f10dfbb08b 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78660 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:9e844d4330ebb875fbb56390fa3c816daddd4a5adb53ec668b638
                        │      │                   a07bb104ce2 
                        │      ├ Title           : Historically, we have been rather lax about malformed
                        │      │                   framing-related  ... 
                        │      ├ Description     : Historically, we have been rather lax about malformed
                        │      │                   framing-related headers in our HTTP/2 implementation, as
                        │      │                   they cannot interfere with HTTP/2 framing. However, this
                        │      │                   makes it possible for our HTTP/2 implementation to forward
                        │      │                   responses containing such headers to an HTTP/1 client when
                        │      │                   acting as a reverse proxy. If the HTTP/1 client also does
                        │      │                   not behave strictly enough, this can result in response
                        │      │                   smuggling. 
                        │      ├ Severity        : UNKNOWN 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://go.dev/cl/835145                                 
                        │      │                  https://go.dev/cl/836385                                 
                        │      │                  https://go.dev/issue/81115                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6610                     
                        │      │                  
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.51Z 
                        │      ╰ LastModifiedDate: 2026-10-08T23:17:03.51Z 
                        ├ [8]  ╭ VulnerabilityID : CVE-2026-78663 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6612
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                        │      │                  │         1c655b6edf399db737b6 
                        │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                        │      │                            832db8d941f10dfbb08b 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78663 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:2dba7246299d4a932245b98c383e9abb12c63cab66d80f3d86cb4
                        │      │                   a2fadc7a568 
                        │      ├ Title           : The HTTP/2 server can refund connection-level flow control
                        │      │                   twice for t ... 
                        │      ├ Description     : The HTTP/2 server can refund connection-level flow control
                        │      │                   twice for the same data: Once when a client resets a stream
                        │      │                   (refunding data for any sent-but-unread portion of the
                        │      │                   stream), and again when a request handler reads the buffered
                        │      │                    data. A malicious client can exploit this to bypass the
                        │      │                   configured connection-level flow control limit
                        │      │                   (MaxReceiveBufferPerConnection). Total buffered data is
                        │      │                   still limited by the concurrent stream limit and
                        │      │                   stream-level flow control. 
                        │      ├ Severity        : UNKNOWN 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://go.dev/cl/847187                                 
                        │      │                  https://go.dev/cl/847310                                 
                        │      │                  https://go.dev/issue/81743                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6612                     
                        │      │                  
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.647Z 
                        │      ╰ LastModifiedDate: 2026-10-08T23:17:03.647Z 
                        ├ [9]  ╭ VulnerabilityID : CVE-2026-78669 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6611
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                        │      │                  │         1c655b6edf399db737b6 
                        │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                        │      │                            832db8d941f10dfbb08b 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78669 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:6adf62ed7dfbbed2ab1f7e8251dce8b49755c66b16678671b2035
                        │      │                   e47972f7736 
                        │      ├ Title           : A malicious HTTP/2 peer can cause excessive CPU consumption
                        │      │                   in the cli ... 
                        │      ├ Description     : A malicious HTTP/2 peer can cause excessive CPU consumption
                        │      │                   in the client or server by opening a large number of streams
                        │      │                    and then sending many small SETTINGS frames containing
                        │      │                   SETTINGS_INITIAL_WINDOW_SIZE values. 
                        │      ├ Severity        : UNKNOWN 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://go.dev/cl/847186                                 
                        │      │                  https://go.dev/cl/847308                                 
                        │      │                  https://go.dev/issue/81742                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6611                     
                        │      │                  
                        │      ├ PublishedDate   : 2026-10-08T23:17:04.01Z 
                        │      ╰ LastModifiedDate: 2026-10-08T23:17:04.01Z 
                        ├ [10] ╭ VulnerabilityID : CVE-2026-94440 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6608
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                        │      │                  │         1c655b6edf399db737b6 
                        │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                        │      │                            832db8d941f10dfbb08b 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94440 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:6eaf7c1f97a8ce39e94c709fbf03b94840ab2f3859ee20977889c
                        │      │                   0073161eeda 
                        │      ├ Title           : Parsing a multipart form can bypass memory limits and read
                        │      │                   an arbitrar ... 
                        │      ├ Description     : Parsing a multipart form can bypass memory limits and read
                        │      │                   an arbitrarily long line into memory when the remaining
                        │      │                   limit at the start of a part is less than 400 bytes. 
                        │      ├ Severity        : UNKNOWN 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://go.dev/cl/847307                                 
                        │      │                  https://go.dev/issue/81741                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6608                     
                        │      │                  
                        │      ├ PublishedDate   : 2026-10-08T23:17:04.917Z 
                        │      ╰ LastModifiedDate: 2026-10-08T23:17:04.917Z 
                        ├ [11] ╭ VulnerabilityID : CVE-2026-94448 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6599
                        │      │                  
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                        │      │                  │         1c655b6edf399db737b6 
                        │      │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                        │      │                            832db8d941f10dfbb08b 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94448 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:f3a51df48a7b2ab79753bad1ecf94241167991246d7ccc0c0b5dd
                        │      │                   47683e31735 
                        │      ├ Title           : When a JavaScript template literal contains consecutive
                        │      │                   expressions, t ... 
                        │      ├ Description     : When a JavaScript template literal contains consecutive
                        │      │                   expressions, the context tracking state was not properly
                        │      │                   reset upon entering a new expression. We now ensure that
                        │      │                   template-literal expression entries correctly reset context
                        │      │                   variables so all subsequent regular expression literals are
                        │      │                   accurately recognized and escaped. 
                        │      ├ Severity        : UNKNOWN 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://go.dev/cl/839866                                 
                        │      │                  https://go.dev/issue/81821                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6599                     
                        │      │                  
                        │      ├ PublishedDate   : 2026-10-08T23:17:05.3Z 
                        │      ╰ LastModifiedDate: 2026-10-08T23:17:05.3Z 
                        ╰ [12] ╭ VulnerabilityID : CVE-2026-97030 
                               ├ VendorIDs                    
                               │                  ────────────
                               │                  GO-2026-6600
                               │                  
                               ├ PkgID           : stdlib@v1.26.7 
                               ├ PkgName         : stdlib 
                               ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                               │                  ╰ UID : 69015e289f0fffad 
                               ├ InstalledVersion: v1.26.7 
                               ├ FixedVersion    : 1.26.9, 1.27.2 
                               ├ Status          : fixed 
                               ├ Layer            ╭ Digest: sha256:e14a634115b9acfba00451c5bbe51723bd537b78ca12
                               │                  │         1c655b6edf399db737b6 
                               │                  ╰ DiffID: sha256:c4c4def2c3b910b0babeab407da73b304644cdf4d98c
                               │                            832db8d941f10dfbb08b 
                               ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97030 
                               ├ DataSource       ╭ ID  : govulndb 
                               │                  ├ Name: The Go Vulnerability Database 
                               │                  ╰ URL : https://pkg.go.dev/vuln/ 
                               ├ Fingerprint     : sha256:bc8280f767e2ae829351dd2a8f1d27d579443cfb257961acbecd9
                               │                   b465bc26e6a 
                               ├ Title           : A trusted template author may have previously written a
                               │                   valid template ... 
                               ├ Description     : A trusted template author may have previously written a
                               │                   valid template wherein the use of the 'yield' keyword would
                               │                   not be correctly escaped. We now ensure that valid keyword
                               │                   uses are escaped and non-keyword uses are not escaped. 
                               ├ Severity        : UNKNOWN 
                               ├ References                                                                
                               │                  ─────────────────────────────────────────────────────────
                               │                  https://go.dev/cl/840925                                 
                               │                  https://go.dev/issue/81823                               
                               │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                               │                  https://pkg.go.dev/vuln/GO-2026-6600                     
                               │                  
                               ├ PublishedDate   : 2026-10-08T23:17:05.91Z 
                               ╰ LastModifiedDate: 2026-10-08T23:17:05.91Z 
```
