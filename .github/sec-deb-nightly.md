```yaml
╭ [0] ╭ Target         : openaf/oaf:deb-nightly (ubuntu 26.04) 
│     ├ Class          : os-pkgs 
│     ├ Type           : ubuntu 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2025-66382 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-66382 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:778e6370afee049f8fd4d7f5ba8ec15a3cb3940b07d10e9542ba4
│                       │      │                   042945b4576 
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
│                       ├ [1]  ╭ VulnerabilityID : CVE-2024-2236 
│                       │      ├ PkgID           : libgcrypt20@1.12.0-2ubuntu1 
│                       │      ├ PkgName         : libgcrypt20 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgcrypt20@1.12.0-2ubuntu1?arch=amd64
│                       │      │                  │       &distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 45e5e1ad6adb0acd 
│                       │      ├ InstalledVersion: 1.12.0-2ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-2236 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:70a033b3b0b9101da1c962e582b256c50872a479a216100cd4fe4
│                       │      │                   f4d2fafc7ff 
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
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-13757 
│                       │      ├ PkgID           : libp11-kit0@0.26.2-2 
│                       │      ├ PkgName         : libp11-kit0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libp11-kit0@0.26.2-2?arch=amd64&distro
│                       │      │                  │       =ubuntu-26.04 
│                       │      │                  ╰ UID : 38d0559292d79a63 
│                       │      ├ InstalledVersion: 0.26.2-2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13757 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e9cbdf4da1ed45b92be83b5200f5ac98c1e5c7a2620b764bb2eaa
│                       │      │                   6baaa059772 
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
│                       │      ╰ LastModifiedDate: 2026-08-31T16:17:52.267Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libsystemd0@259.5-0ubuntu3.4 
│                       │      ├ PkgName         : libsystemd0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsystemd0@259.5-0ubuntu3.4?arch=amd6
│                       │      │                  │       4&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : fe76170faadcb974 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:194f2f57a442b24870a60d397a150dd9609766fb825e50797d223
│                       │      │                   e8f74cb60d1 
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
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libudev1@259.5-0ubuntu3.4 
│                       │      ├ PkgName         : libudev1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libudev1@259.5-0ubuntu3.4?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : 9d26e6690a3402fe 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6256191cefdd428084394fab27f8504212cd3015f388ddff23e03
│                       │      │                   b27f9569149 
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
│                       ├ [5]  ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : login.defs@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : login.defs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login.defs@4.17.4-2ubuntu3?arch=all&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : eaf648d5e4e975f7 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b520457dd1fc6c8fba9887da8f97deb2f904ceee0a7550a41b44d
│                       │      │                   e4e9084d3e8 
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
│                       ├ [6]  ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : passwd@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : passwd 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/passwd@4.17.4-2ubuntu3?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : 6f8f43a2d44eb6a2 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:78be74a57da67a36e4f783711f440d3102c17d601f763d94bb681
│                       │      │                   2dbcd509af6 
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
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-35341 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35341 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ddd96ccfb03a8a4ce8fb51ba536ebbb04155fb7068d4f52a487da
│                       │      │                   ed0aba73124 
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
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-35344 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35344 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:911c0ce7dd34efa5185ca5e802d49681301ef1fdd7c232a5b85c9
│                       │      │                   696a2a953f8 
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
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-35345 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35345 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:9eef2b5a61aaea05b56f3550e4c9e41f0e5a7591172a2dffe118c
│                       │      │                   c8e7f878def 
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
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-35348 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35348 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e0293d05013306a1bbcb61f521e413e9b8ad49eb75f4a3c082a0f
│                       │      │                   0aa66416be3 
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
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-35350 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35350 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:eab2f7117e10b2ddddaf31ffa4758e268f346658d47937a15275c
│                       │      │                   b4d04e407c6 
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
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-35351 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35351 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:841cecfb2b10d00ba7c79398adb8b330a2e3d2c16ec125ea32b97
│                       │      │                   7ca7cb89ba3 
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
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-35352 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35352 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f17091eece486f5f7ec8c7589cd42fd5a5651ced3a366daf74d43
│                       │      │                   07b29385f76 
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
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-35354 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35354 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c8972bfc5405046aba316b431c7cf6c74316052e67e4bf2a337cc
│                       │      │                   8a098fa08dd 
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
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-35357 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35357 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a9ba581a98760bf2e2933357c9dfa28fca4ecd4f70728d78b9f41
│                       │      │                   0e7a54be38d 
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
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-35359 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35359 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6cffe02cd1eb3af07be51fd3ab2219f1426c8803ac608051a24c6
│                       │      │                   afa7609360c 
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
│                       ├ [17] ╭ VulnerabilityID : CVE-2026-35360 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35360 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:275603e954f5001d11d9eabcfc275be658c90da044d2cc48efd95
│                       │      │                   d10acb23697 
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
│                       ├ [18] ╭ VulnerabilityID : CVE-2026-35363 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35363 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5f4f5a5c40bc8c48cf8fffa114ba87dbcfb77de170f21c58db535
│                       │      │                   18286a85422 
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
│                       ├ [19] ╭ VulnerabilityID : CVE-2026-35364 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35364 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:96674787470b6d49a68e799d655d3f0e464ad4bfa6e6992b09803
│                       │      │                   a9a19746c7f 
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
│                       ├ [20] ╭ VulnerabilityID : CVE-2026-35367 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35367 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f5bde50e08b37758f2140ca3451db17eca2fc44af1af6e3206739
│                       │      │                   ca71b517c25 
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
│                       ├ [21] ╭ VulnerabilityID : CVE-2026-35368 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35368 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ad022f96b368a3d8cc5f78b64b1fb7e350fab024e15f5e416ceb0
│                       │      │                   188712af4f1 
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
│                       ├ [22] ╭ VulnerabilityID : CVE-2026-35370 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35370 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6d17e467a5a26832311a8fa930a4b1b6c623520801e1e048d4aeb
│                       │      │                   bafab663adb 
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
│                       ├ [23] ╭ VulnerabilityID : CVE-2026-35371 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35371 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a63be90aecb368235fe1a0c56866f9d472a80b5ff563c0e9c912a
│                       │      │                   0448bb5b8b5 
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
│                       ├ [24] ╭ VulnerabilityID : CVE-2026-35373 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35373 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d8f9783548f8aa6d2d8faaba5f925f41d5716a36ce9ab4aa0da3d
│                       │      │                   9f30980921f 
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
│                       ├ [25] ╭ VulnerabilityID : CVE-2026-35374 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:1d695586c497328cff8c056d96f449e82dc7e11473fefc0e2e324
│                       │      │                   67abcb01432 
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
│                       ├ [26] ╭ VulnerabilityID : CVE-2026-35377 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 15e3b6ce4401d8b0 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35377 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:fe5ffc7c95e79510957ec99b765be344dd81a501735fe85af4d9d
│                       │      │                   6c641955a8c 
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
│                       ├ [27] ╭ VulnerabilityID : CVE-2026-18477 
│                       │      ├ PkgID           : tar@1.35+dfsg-4ubuntu0.4 
│                       │      ├ PkgName         : tar 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-4ubuntu0.4?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 5867f93e7d45b368 
│                       │      ├ InstalledVersion: 1.35+dfsg-4ubuntu0.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                       │      │                  │         ad3370eff506a802a23c 
│                       │      │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                       │      │                            b09f90775c2bf60d9c05 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18477 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f5cb380f79263a4a7ce9df53793e62c5c13a4eb52a32da4987f2a
│                       │      │                   fc7ab3bb42e 
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
│                       │      ├ VendorSeverity   ╭ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:R/S:U/C:N/I:H
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.4 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:R/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.4 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:49361     
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:61581     
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:61783     
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18477
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2509735  
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18477      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18477      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-03T17:16:33.897Z 
│                       │      ╰ LastModifiedDate: 2026-09-01T03:16:48.353Z 
│                       ╰ [28] ╭ VulnerabilityID : CVE-2026-18508 
│                              ├ PkgID           : tar@1.35+dfsg-4ubuntu0.4 
│                              ├ PkgName         : tar 
│                              ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-4ubuntu0.4?arch=amd64&
│                              │                  │       distro=ubuntu-26.04 
│                              │                  ╰ UID : 5867f93e7d45b368 
│                              ├ InstalledVersion: 1.35+dfsg-4ubuntu0.4 
│                              ├ Status          : affected 
│                              ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802
│                              │                  │         ad3370eff506a802a23c 
│                              │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7
│                              │                            b09f90775c2bf60d9c05 
│                              ├ SeveritySource  : ubuntu 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18508 
│                              ├ DataSource       ╭ ID  : ubuntu 
│                              │                  ├ Name: Ubuntu CVE Tracker 
│                              │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                              ├ Fingerprint     : sha256:d950510e256d22aa2e3671fe125785b92219d9f16b43a5aa3c8a6
│                              │                   4fc18f9fc3e 
│                              ├ Title           : tar: tar: --one-top-level hardlink targets not confined to
│                              │                   top-level directory enabling arbitrary file overwrite 
│                              ├ Description     : A flaw was found in GNU tar. When extracting an archive with
│                              │                    the --one-top-level option, hardlink targets are not
│                              │                   confined to the designated top-level directory and may
│                              │                   resolve relative to the extraction working directory. A
│                              │                   crafted archive can create hardlinks that escape the
│                              │                   intended boundary and, when combined with a preexisting
│                              │                   symbolic link under the working directory, may allow writing
│                              │                    outside that boundary during a single extraction. 
│                              ├ Severity        : MEDIUM 
│                              ├ CweIDs                 
│                              │                  ──────
│                              │                  CWE-59
│                              │                  
│                              ├ VendorSeverity   ╭ redhat: 2 
│                              │                  ╰ ubuntu: 2 
│                              ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L
│                              │                           │           /A:N 
│                              │                           ╰ V3Score : 4.4 
│                              ├ References                                                            
│                              │                  ─────────────────────────────────────────────────────
│                              │                  https://access.redhat.com/errata/RHSA-2026:50807     
│                              │                  https://access.redhat.com/errata/RHSA-2026:61581     
│                              │                  https://access.redhat.com/errata/RHSA-2026:61783     
│                              │                  https://access.redhat.com/security/cve/CVE-2026-18508
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2509843  
│                              │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18508      
│                              │                  https://www.cve.org/CVERecord?id=CVE-2026-18508      
│                              │                  
│                              ├ PublishedDate   : 2026-08-03T16:16:28.387Z 
│                              ╰ LastModifiedDate: 2026-09-01T03:16:48.52Z 
├ [1] ╭ Target  : Java 
│     ├ Class   : lang-pkgs 
│     ├ Type    : jar 
│     ╰ Packages 
╰ [2] ╭ Target         : usr/bin/pebble 
      ├ Class          : lang-pkgs 
      ├ Type           : gobinary 
      ├ Packages        
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2026-33818 
                        │     ├ VendorIDs                    
                        │     │                  ────────────
                        │     │                  GO-2026-5972
                        │     │                  
                        │     ├ PkgID           : stdlib@v1.26.5 
                        │     ├ PkgName         : stdlib 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.5 
                        │     │                  ╰ UID : 26d7064c5de1c97a 
                        │     ├ InstalledVersion: v1.26.5 
                        │     ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802a
                        │     │                  │         d3370eff506a802a23c 
                        │     │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7b
                        │     │                            09f90775c2bf60d9c05 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-33818 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:74236dbf833068bde83ea4893eff79ace9fa237e0ab57c4d6dccc6
                        │     │                   ebee4291d8 
                        │     ├ Title           : encoding/asn1: golang: Go encoding/asn1: Denial of Service
                        │     │                   via excessive recursion in Unmarshal 
                        │     ├ Description     : Enforce a recursion limit in Unmarshal to prevent stack
                        │     │                   exhaustion when parsing deeply-nested, recursive
                        │     │                   structures. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs                  
                        │     │                  ───────
                        │     │                  CWE-400
                        │     │                  
                        │     ├ VendorSeverity   ╭ alma       : 3 
                        │     │                  ├ amazon     : 3 
                        │     │                  ├ bitnami    : 3 
                        │     │                  ├ oracle-oval: 3 
                        │     │                  ├ redhat     : 3 
                        │     │                  ╰ rocky      : 3 
                        │     ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                  │         │           /A:H 
                        │     │                  │         ╰ V3Score : 7.5 
                        │     │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                            │           /A:H 
                        │     │                            ╰ V3Score : 7.5 
                        │     ├ References                                                                    
                        │     │                  ─────────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/errata/RHSA-2026:60304             
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-33818        
                        │     │                  https://bugzilla.redhat.com/2515815                          
                        │     │                  https://bugzilla.redhat.com/2515820                          
                        │     │                  https://bugzilla.redhat.com/2515827                          
                        │     │                  https://bugzilla.redhat.com/2515838                          
                        │     │                  https://bugzilla.redhat.com/2515839                          
                        │     │                  https://bugzilla.redhat.com/2515840                          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │     │                  https://creativecommons.org/licenses/by/4.0/                 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │     │                  https://errata.almalinux.org/9/ALSA-2026-60304.html          
                        │     │                  https://errata.rockylinux.org/RLSA-2026:60304                
                        │     │                  https://go.dev/cl/814980                                     
                        │     │                  https://go.dev/issue/80405                                   
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                        │     │                  https://linux.oracle.com/cve/CVE-2026-33818.html             
                        │     │                  https://linux.oracle.com/errata/ELSA-2026-60306-0.html       
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-33818              
                        │     │                  https://pkg.go.dev/vuln/GO-2026-5972                         
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-33818              
                        │     │                  
                        │     ├ PublishedDate   : 2026-08-13T22:17:19.84Z 
                        │     ╰ LastModifiedDate: 2026-08-14T16:16:55.317Z 
                        ├ [1] ╭ VulnerabilityID : CVE-2026-39821 
                        │     ├ VendorIDs                    
                        │     │                  ────────────
                        │     │                  GO-2026-5026
                        │     │                  
                        │     ├ PkgID           : stdlib@v1.26.5 
                        │     ├ PkgName         : stdlib 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.5 
                        │     │                  ╰ UID : 26d7064c5de1c97a 
                        │     ├ InstalledVersion: v1.26.5 
                        │     ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802a
                        │     │                  │         d3370eff506a802a23c 
                        │     │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7b
                        │     │                            09f90775c2bf60d9c05 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-39821 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:2743cf2c6d35767740c4f578735b1a0ffaa428c8f4a960045a03cd
                        │     │                   1fdd213ba0 
                        │     ├ Title           : golang.org/x/net/idna: golang: net/http:
                        │     │                   golang.org/x/net/idna: Privilege escalation via incorrect
                        │     │                   Punycode label processing 
                        │     ├ Description     : The ToASCII and ToUnicode functions incorrectly accept
                        │     │                   Punycode-encoded labels that decode to an ASCII-only label.
                        │     │                   For example, ToUnicode("xn--example-.com") incorrectly
                        │     │                   returns the name "example.com" rather than an error. This
                        │     │                   behavior can lead to privilege escalation in programs using
                        │     │                   the idna package. For example, a program which performs
                        │     │                   privilege checks on the ASCII hostname may reject
                        │     │                   "example.com" but permit "xn--example-.com". If that program
                        │     │                   subsequently converts the ASCII hostname to Unicode, it will
                        │     │                   inadvertently permits access to the Unicode name
                        │     │                   "example.com". 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs                   
                        │     │                  ────────
                        │     │                  CWE-1289
                        │     │                  
                        │     ├ VendorSeverity   ╭ alma       : 3 
                        │     │                  ├ amazon     : 3 
                        │     │                  ├ azure      : 4 
                        │     │                  ├ oracle-oval: 3 
                        │     │                  ├ redhat     : 3 
                        │     │                  ├ rocky      : 3 
                        │     │                  ╰ ubuntu     : 2 
                        │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/
                        │     │                           │           A:N 
                        │     │                           ╰ V3Score : 8.2 
                        │     ├ References                                                                     
                        │     │                  ──────────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/errata/RHSA-2026:23262              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:23264              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:26546              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:26547              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:30650              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:30651              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:30853              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:30854              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:30855              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:33155              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:33160              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:33163              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:33173              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:33183              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:33524              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:33531              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:34342              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:34357              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:34359              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:34364              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:34789              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:35826              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:35827              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:35828              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:35829              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:35830              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:35831              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:35993              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:35994              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:36105              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:36167              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:36207              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:36648              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:36651              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:36796              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:36797              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:36808              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:36820              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:36883              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:37387              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:37435              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:37436              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:38995              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:39005              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:39573              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:39879              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:40118              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:40262              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:40945              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:41019              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:41030              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:41031              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:41036              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:41055              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:41066              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:41928              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:41930              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42043              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42047              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42048              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42049              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42050              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42051              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42078              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42079              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42080              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42082              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42132              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42142              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42146              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42150              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42151              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42240              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42644              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42796              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:42852              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:43038              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:43052              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:43692              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:44622              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:44624              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:46395              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:47149              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:47735              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:47737              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:47952              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:49702              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:49712              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:50300              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:50843              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:51033              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:51112              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:51187              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:51194              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:51341              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:52826              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:53374              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:53412              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:53413              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:53415              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:53530              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54191              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54274              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54283              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54284              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54285              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54286              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54287              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54395              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54401              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54435              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54441              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54531              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54580              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:54757              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:56143              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:56223              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:56340              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:56431              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:57194              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:57541              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:57649              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:57845              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:59546              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:59549              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:59562              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:60315              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:60354              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:60387              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:60520              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:61245              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:61253              
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-39821         
                        │     │                  https://bugzilla.redhat.com/2480756                           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480756           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2498152           
                        │     │                  https://creativecommons.org/licenses/by/4.0/                  
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39821 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39822 
                        │     │                  https://errata.almalinux.org/9/ALSA-2026-37435.html           
                        │     │                  https://errata.rockylinux.org/RLSA-2026:37435                 
                        │     │                  https://github.com/golang/go/issues/78760                     
                        │     │                  https://go.dev/cl/767220                                      
                        │     │                  https://go.dev/issue/78760                                    
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI     
                        │     │                  https://groups.google.com/g/golang-announce/c/iI-mYSI0lu8     
                        │     │                  https://linux.oracle.com/cve/CVE-2026-39821.html              
                        │     │                  https://linux.oracle.com/errata/ELSA-2026-46395.html          
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-39821               
                        │     │                  https://pkg.go.dev/vuln/GO-2026-5026                          
                        │     │                  https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-2
                        │     │                  026-39821.json                                                
                        │     │                  https://ubuntu.com/security/notices/USN-8416-1                
                        │     │                                                                                
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-39821               
                        │     │                                                                                
                        │     │                  
                        │     ├ PublishedDate   : 2026-05-22T16:16:20.41Z 
                        │     ╰ LastModifiedDate: 2026-08-31T13:18:06.777Z 
                        ├ [2] ╭ VulnerabilityID : CVE-2026-46600 
                        │     ├ VendorIDs                    
                        │     │                  ────────────
                        │     │                  GO-2026-5942
                        │     │                  
                        │     ├ PkgID           : stdlib@v1.26.5 
                        │     ├ PkgName         : stdlib 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.5 
                        │     │                  ╰ UID : 26d7064c5de1c97a 
                        │     ├ InstalledVersion: v1.26.5 
                        │     ├ FixedVersion    : 1.26.6, 1.27.0-rc.3 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802a
                        │     │                  │         d3370eff506a802a23c 
                        │     │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7b
                        │     │                            09f90775c2bf60d9c05 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46600 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:70dd0b9bdc32fe89b0d1c34b148f21d1f7f4dbff64ba44e929434e
                        │     │                   bd0dd11615 
                        │     ├ Title           : golang.org/x/net/dns/dnsmessage:
                        │     │                   golang.org/x/net/dns/dnsmessage: Denial of Service via
                        │     │                   invalid DNS record parsing 
                        │     ├ Description     : Parsing an invalid SVCB or HTTPS RR can panic when the size
                        │     │                   of a parameter value overflows the message buffer. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs                  
                        │     │                  ───────
                        │     │                  CWE-125
                        │     │                  
                        │     ├ VendorSeverity   ╭ azure  : 2 
                        │     │                  ├ bitnami: 3 
                        │     │                  ╰ redhat : 3 
                        │     ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                  │         │           /A:H 
                        │     │                  │         ╰ V3Score : 7.5 
                        │     │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                            │           /A:H 
                        │     │                            ╰ V3Score : 7.5 
                        │     ├ References                                                                
                        │     │                  ─────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-46600    
                        │     │                  https://go.dev/cl/786345                                 
                        │     │                  https://go.dev/issue/79795                               
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-46600          
                        │     │                  https://pkg.go.dev/vuln/GO-2026-5942                     
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-46600          
                        │     │                  
                        │     ├ PublishedDate   : 2026-07-21T20:17:01.213Z 
                        │     ╰ LastModifiedDate: 2026-08-14T16:16:55.673Z 
                        ├ [3] ╭ VulnerabilityID : CVE-2026-56853 
                        │     ├ VendorIDs                    
                        │     │                  ────────────
                        │     │                  GO-2026-6089
                        │     │                  
                        │     ├ PkgID           : stdlib@v1.26.5 
                        │     ├ PkgName         : stdlib 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.5 
                        │     │                  ╰ UID : 26d7064c5de1c97a 
                        │     ├ InstalledVersion: v1.26.5 
                        │     ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802a
                        │     │                  │         d3370eff506a802a23c 
                        │     │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7b
                        │     │                            09f90775c2bf60d9c05 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56853 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:4d1c906023199f34a29412970570a38d5972b9660bf5a34d32354b
                        │     │                   f65c51f597 
                        │     ├ Title           : net/http: golang: Go net/http: Unencrypted HTTP/2 connections
                        │     │                    vulnerable to Denial of Service 
                        │     ├ Description     : When a server is configured to support unencrypted HTTP/2, it
                        │     │                    reads a few bytes from each new connection to see if they
                        │     │                   contain the HTTP/2 client preface. ReadHeaderTimeout is
                        │     │                   unexpectedly not being applied when doing this. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs                  
                        │     │                  ───────
                        │     │                  CWE-770
                        │     │                  
                        │     ├ VendorSeverity   ╭ alma       : 3 
                        │     │                  ├ amazon     : 3 
                        │     │                  ├ bitnami    : 3 
                        │     │                  ├ oracle-oval: 3 
                        │     │                  ├ redhat     : 3 
                        │     │                  ╰ rocky      : 3 
                        │     ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                  │         │           /A:H 
                        │     │                  │         ╰ V3Score : 7.5 
                        │     │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                            │           /A:H 
                        │     │                            ╰ V3Score : 7.5 
                        │     ├ References                                                                    
                        │     │                  ─────────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/errata/RHSA-2026:60304             
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-56853        
                        │     │                  https://bugzilla.redhat.com/2515815                          
                        │     │                  https://bugzilla.redhat.com/2515820                          
                        │     │                  https://bugzilla.redhat.com/2515827                          
                        │     │                  https://bugzilla.redhat.com/2515838                          
                        │     │                  https://bugzilla.redhat.com/2515839                          
                        │     │                  https://bugzilla.redhat.com/2515840                          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │     │                  https://creativecommons.org/licenses/by/4.0/                 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │     │                  https://errata.almalinux.org/9/ALSA-2026-60304.html          
                        │     │                  https://errata.rockylinux.org/RLSA-2026:60304                
                        │     │                  https://go.dev/cl/795540                                     
                        │     │                  https://go.dev/issue/80205                                   
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                        │     │                  https://linux.oracle.com/cve/CVE-2026-56853.html             
                        │     │                  https://linux.oracle.com/errata/ELSA-2026-60306-0.html       
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56853              
                        │     │                  https://pkg.go.dev/vuln/GO-2026-6089                         
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-56853              
                        │     │                  
                        │     ├ PublishedDate   : 2026-08-13T22:17:22.093Z 
                        │     ╰ LastModifiedDate: 2026-08-14T16:16:57.21Z 
                        ├ [4] ╭ VulnerabilityID : CVE-2026-56858 
                        │     ├ VendorIDs                    
                        │     │                  ────────────
                        │     │                  GO-2026-6091
                        │     │                  
                        │     ├ PkgID           : stdlib@v1.26.5 
                        │     ├ PkgName         : stdlib 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.5 
                        │     │                  ╰ UID : 26d7064c5de1c97a 
                        │     ├ InstalledVersion: v1.26.5 
                        │     ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802a
                        │     │                  │         d3370eff506a802a23c 
                        │     │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7b
                        │     │                            09f90775c2bf60d9c05 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56858 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:4761eec1d66921d7ec85a50b022b0466b231db2b15cf329a93f718
                        │     │                   0a53fd82e0 
                        │     ├ Title           : html/template: golang: Go html/template: Cross-Site Scripting
                        │     │                    via pathological input 
                        │     ├ Description     : Previously, pathological inputs could close an unescaped '/'
                        │     │                   early, allowing for attack-controlled data to inject
                        │     │                   arbitrary content, potentially leading to XSS. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs                 
                        │     │                  ──────
                        │     │                  CWE-79
                        │     │                  
                        │     ├ VendorSeverity   ╭ alma       : 3 
                        │     │                  ├ amazon     : 3 
                        │     │                  ├ bitnami    : 2 
                        │     │                  ├ oracle-oval: 3 
                        │     │                  ├ redhat     : 3 
                        │     │                  ╰ rocky      : 3 
                        │     ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L
                        │     │                  │         │           /A:N 
                        │     │                  │         ╰ V3Score : 6.1 
                        │     │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H
                        │     │                            │           /A:N 
                        │     │                            ╰ V3Score : 8.1 
                        │     ├ References                                                                    
                        │     │                  ─────────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/errata/RHSA-2026:60304             
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-56858        
                        │     │                  https://bugzilla.redhat.com/2515815                          
                        │     │                  https://bugzilla.redhat.com/2515820                          
                        │     │                  https://bugzilla.redhat.com/2515827                          
                        │     │                  https://bugzilla.redhat.com/2515838                          
                        │     │                  https://bugzilla.redhat.com/2515839                          
                        │     │                  https://bugzilla.redhat.com/2515840                          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │     │                  https://creativecommons.org/licenses/by/4.0/                 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │     │                  https://errata.almalinux.org/9/ALSA-2026-60304.html          
                        │     │                  https://errata.rockylinux.org/RLSA-2026:60304                
                        │     │                  https://go.dev/cl/807100                                     
                        │     │                  https://go.dev/issue/80435                                   
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                        │     │                  https://linux.oracle.com/cve/CVE-2026-56858.html             
                        │     │                  https://linux.oracle.com/errata/ELSA-2026-60306-0.html       
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56858              
                        │     │                  https://pkg.go.dev/vuln/GO-2026-6091                         
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-56858              
                        │     │                  
                        │     ├ PublishedDate   : 2026-08-13T22:17:22.207Z 
                        │     ╰ LastModifiedDate: 2026-08-14T16:16:57.367Z 
                        ├ [5] ╭ VulnerabilityID : CVE-2026-56859 
                        │     ├ VendorIDs                    
                        │     │                  ────────────
                        │     │                  GO-2026-6088
                        │     │                  
                        │     ├ PkgID           : stdlib@v1.26.5 
                        │     ├ PkgName         : stdlib 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.5 
                        │     │                  ╰ UID : 26d7064c5de1c97a 
                        │     ├ InstalledVersion: v1.26.5 
                        │     ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802a
                        │     │                  │         d3370eff506a802a23c 
                        │     │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7b
                        │     │                            09f90775c2bf60d9c05 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56859 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:7555f88f2daad5ce791834f3bf958f5afe6aaa7dbacc31a4ffc1dd
                        │     │                   d761984185 
                        │     ├ Title           : encoding/xml: golang: Go: Denial of Service via XML decoding
                        │     │                   recursion depth issue 
                        │     ├ Description     : Previously, DecodeElement would reset the depth counter
                        │     │                   causing it to never fire; this could lead to stack
                        │     │                   exhaustion. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs                  
                        │     │                  ───────
                        │     │                  CWE-770
                        │     │                  
                        │     ├ VendorSeverity   ╭ alma       : 3 
                        │     │                  ├ amazon     : 3 
                        │     │                  ├ bitnami    : 3 
                        │     │                  ├ oracle-oval: 3 
                        │     │                  ├ redhat     : 3 
                        │     │                  ╰ rocky      : 3 
                        │     ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                  │         │           /A:H 
                        │     │                  │         ╰ V3Score : 7.5 
                        │     │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                            │           /A:H 
                        │     │                            ╰ V3Score : 7.5 
                        │     ├ References                                                                    
                        │     │                  ─────────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/errata/RHSA-2026:60304             
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-56859        
                        │     │                  https://bugzilla.redhat.com/2515815                          
                        │     │                  https://bugzilla.redhat.com/2515820                          
                        │     │                  https://bugzilla.redhat.com/2515827                          
                        │     │                  https://bugzilla.redhat.com/2515838                          
                        │     │                  https://bugzilla.redhat.com/2515839                          
                        │     │                  https://bugzilla.redhat.com/2515840                          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │     │                  https://creativecommons.org/licenses/by/4.0/                 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │     │                  https://errata.almalinux.org/9/ALSA-2026-60304.html          
                        │     │                  https://errata.rockylinux.org/RLSA-2026:60304                
                        │     │                  https://go.dev/cl/803320                                     
                        │     │                  https://go.dev/issue/80481                                   
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                        │     │                  https://linux.oracle.com/cve/CVE-2026-56859.html             
                        │     │                  https://linux.oracle.com/errata/ELSA-2026-60306-0.html       
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56859              
                        │     │                  https://pkg.go.dev/vuln/GO-2026-6088                         
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-56859              
                        │     │                  
                        │     ├ PublishedDate   : 2026-08-13T22:17:22.32Z 
                        │     ╰ LastModifiedDate: 2026-08-14T16:16:57.523Z 
                        ├ [6] ╭ VulnerabilityID : CVE-2026-56860 
                        │     ├ VendorIDs                    
                        │     │                  ────────────
                        │     │                  GO-2026-6218
                        │     │                  
                        │     ├ PkgID           : stdlib@v1.26.5 
                        │     ├ PkgName         : stdlib 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.5 
                        │     │                  ╰ UID : 26d7064c5de1c97a 
                        │     ├ InstalledVersion: v1.26.5 
                        │     ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802a
                        │     │                  │         d3370eff506a802a23c 
                        │     │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7b
                        │     │                            09f90775c2bf60d9c05 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56860 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:f07524a5a63bc3340784c466317cbecc2a173a34005bb5c9ec6854
                        │     │                   83dbcde714 
                        │     ├ Title           : net/url: golang: golang net/url: Denial of Service from
                        │     │                   quadratic complexity in path resolution 
                        │     ├ Description     : Previously, resolving relative paths containing parent
                        │     │                   directory ('..') segments performed string conversions and
                        │     │                   buffer rewrites on each step, resulting in quadratic time
                        │     │                   complexity and high memory allocation overhead. Now, path
                        │     │                   resolution operates on a byte buffer using index-based
                        │     │                   backtracking for '..' segments, eliminating the quadratic
                        │     │                   time complexity and significantly reducing memory
                        │     │                   allocations. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs                  
                        │     │                  ───────
                        │     │                  CWE-407
                        │     │                  
                        │     ├ VendorSeverity   ╭ alma       : 3 
                        │     │                  ├ amazon     : 3 
                        │     │                  ├ bitnami    : 2 
                        │     │                  ├ oracle-oval: 3 
                        │     │                  ├ redhat     : 3 
                        │     │                  ╰ rocky      : 3 
                        │     ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
                        │     │                  │         │           /A:H 
                        │     │                  │         ╰ V3Score : 5.9 
                        │     │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                            │           /A:H 
                        │     │                            ╰ V3Score : 7.5 
                        │     ├ References                                                                    
                        │     │                  ─────────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/errata/RHSA-2026:60304             
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-56860        
                        │     │                  https://bugzilla.redhat.com/2515815                          
                        │     │                  https://bugzilla.redhat.com/2515820                          
                        │     │                  https://bugzilla.redhat.com/2515827                          
                        │     │                  https://bugzilla.redhat.com/2515838                          
                        │     │                  https://bugzilla.redhat.com/2515839                          
                        │     │                  https://bugzilla.redhat.com/2515840                          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │     │                  https://creativecommons.org/licenses/by/4.0/                 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │     │                  https://errata.almalinux.org/9/ALSA-2026-60304.html          
                        │     │                  https://errata.rockylinux.org/RLSA-2026:60304                
                        │     │                  https://go.dev/cl/803681                                     
                        │     │                  https://go.dev/issue/80494                                   
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                        │     │                  https://linux.oracle.com/cve/CVE-2026-56860.html             
                        │     │                  https://linux.oracle.com/errata/ELSA-2026-60306-0.html       
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56860              
                        │     │                  https://pkg.go.dev/vuln/GO-2026-6218                         
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-56860              
                        │     │                  
                        │     ├ PublishedDate   : 2026-08-13T22:17:22.44Z 
                        │     ╰ LastModifiedDate: 2026-08-14T17:19:13.91Z 
                        ╰ [7] ╭ VulnerabilityID : CVE-2026-56862 
                              ├ VendorIDs                    
                              │                  ────────────
                              │                  GO-2026-6090
                              │                  
                              ├ PkgID           : stdlib@v1.26.5 
                              ├ PkgName         : stdlib 
                              ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.5 
                              │                  ╰ UID : 26d7064c5de1c97a 
                              ├ InstalledVersion: v1.26.5 
                              ├ FixedVersion    : 1.25.13, 1.26.6, 1.27.0-rc.3 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:9e45e2ecd6f43d16713e881356d8a41e8384e9ae1802a
                              │                  │         d3370eff506a802a23c 
                              │                  ╰ DiffID: sha256:8ec16d0c3a78c1f2f1e1464e737363cd7bc3fed81ef7b
                              │                            09f90775c2bf60d9c05 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56862 
                              ├ DataSource       ╭ ID  : govulndb 
                              │                  ├ Name: The Go Vulnerability Database 
                              │                  ╰ URL : https://pkg.go.dev/vuln/ 
                              ├ Fingerprint     : sha256:9fbea22e4f28abc5f70cb69d25147d343e149782fa4fbe2d061610
                              │                   ac52056ba7 
                              ├ Title           : crypto/tls: golang: Golang crypto/tls: Denial of Service via
                              │                   indefinite KeyUpdate messages 
                              ├ Description     : Handshake messages, such as KeyUpdate, are always considered
                              │                   as state-advancing, regardless of whether a handshake has
                              │                   been completed or not. As a result, a malicious client can
                              │                   keep sending KeyUpdate messages to force the server to keep
                              │                   performing key derivation operations indefinitely. 
                              ├ Severity        : HIGH 
                              ├ CweIDs                  
                              │                  ───────
                              │                  CWE-770
                              │                  
                              ├ VendorSeverity   ╭ alma       : 3 
                              │                  ├ amazon     : 3 
                              │                  ├ bitnami    : 3 
                              │                  ├ oracle-oval: 3 
                              │                  ├ redhat     : 3 
                              │                  ╰ rocky      : 3 
                              ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                              │                  │         │           /A:H 
                              │                  │         ╰ V3Score : 7.5 
                              │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                              │                            │           /A:H 
                              │                            ╰ V3Score : 7.5 
                              ├ References                                                                    
                              │                  ─────────────────────────────────────────────────────────────
                              │                  https://access.redhat.com/errata/RHSA-2026:60304             
                              │                  https://access.redhat.com/security/cve/CVE-2026-56862        
                              │                  https://bugzilla.redhat.com/2515815                          
                              │                  https://bugzilla.redhat.com/2515820                          
                              │                  CWE-367                                                      
                              │                  https://bugzilla.redhat.com/2515838                          
                              │                  https://bugzilla.redhat.com/2515839                          
                              │                  https://bugzilla.redhat.com/2515840                          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                              │                  https://creativecommons.org/licenses/by/4.0/                 
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                              │                  https://errata.almalinux.org/9/ALSA-2026-60304.html          
                              │                  https://errata.rockylinux.org/RLSA-2026:60304                
                              │                  https://go.dev/cl/804261                                     
                              │                  https://go.dev/issue/80528                                   
                              │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                              │                  https://linux.oracle.com/cve/CVE-2026-56862.html             
                              │                  https://linux.oracle.com/errata/ELSA-2026-60306-0.html       
                              │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56862              
                              │                  https://pkg.go.dev/vuln/GO-2026-6090                         
                              │                  https://www.cve.org/CVERecord?id=CVE-2026-56862              
                              │                  
                              ├ PublishedDate   : 2026-08-13T22:17:22.55Z 
                              ╰ LastModifiedDate: 2026-08-14T16:16:57.717Z 
```
