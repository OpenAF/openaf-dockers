```yaml

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
                        │      │                  ├ rocky      : 3 
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
                        │      │                  https://access.redhat.com/errata/RHSA-2026:22112             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:22120             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:22121             
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
                        │      │                  https://access.redhat.com/errata/RHSA-2026:49702             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:49712             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:50205             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54274             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54283             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54284             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54285             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54286             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:54287             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:56854             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:56912             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57191             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57194             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57365             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57367             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57408             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57545             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57649             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57845             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60520             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-33814        
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467809          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467810          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467811          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467813          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467815          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467820          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467822          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467823          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467825          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467826          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467827          
                        │      │                  https://creativecommons.org/licenses/by/4.0/                 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33811
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33814
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39817
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39819
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39820
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39823
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39825
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39826
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39836
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42499
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42501
                        │      │                  https://errata.rockylinux.org/RLSA-2026:22121                
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
                        │      ╰ LastModifiedDate: 2026-08-28T16:17:39.39Z 
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
                        │      │                  https://access.redhat.com/errata/RHSA-2026:49702             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:49712             
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
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57649             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57845             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:59546             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:59549             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:59562             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60315             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60354             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60387             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60520             
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
                        │      ╰ LastModifiedDate: 2026-08-28T16:17:48.517Z 
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
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ bitnami: 3 
                        │      │                  ├ redhat : 3 
                        │      │                  ╰ rocky  : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60304             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-33818        
                        │      │                  https://bugzilla.redhat.com/2515815                          
                        │      │                  https://bugzilla.redhat.com/2515820                          
                        │      │                  https://bugzilla.redhat.com/2515827                          
                        │      │                  https://bugzilla.redhat.com/2515838                          
                        │      │                  https://bugzilla.redhat.com/2515839                          
                        │      │                  https://bugzilla.redhat.com/2515840                          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │      │                  https://creativecommons.org/licenses/by/4.0/                 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-60304.html          
                        │      │                  https://errata.rockylinux.org/RLSA-2026:60304                
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
                        │      │                  https://access.redhat.com/errata/RHSA-2026:49702             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:49712             
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
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57649             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:57845             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:59546             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:59549             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:59562             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60315             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60354             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60387             
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60520             
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
                        │      ╰ LastModifiedDate: 2026-08-28T16:17:48.517Z 
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
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ bitnami: 3 
                        │      │                  ├ redhat : 3 
                        │      │                  ╰ rocky  : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60304             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56853        
                        │      │                  https://bugzilla.redhat.com/2515815                          
                        │      │                  https://bugzilla.redhat.com/2515820                          
                        │      │                  https://bugzilla.redhat.com/2515827                          
                        │      │                  https://bugzilla.redhat.com/2515838                          
                        │      │                  https://bugzilla.redhat.com/2515839                          
                        │      │                  https://bugzilla.redhat.com/2515840                          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │      │                  https://creativecommons.org/licenses/by/4.0/                 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-60304.html          
                        │      │                  https://errata.rockylinux.org/RLSA-2026:60304                
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
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ bitnami: 2 
                        │      │                  ├ redhat : 3 
                        │      │                  ╰ rocky  : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:
                        │      │                  │         │           L/A:N 
                        │      │                  │         ╰ V3Score : 6.1 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:
                        │      │                            │           H/A:N 
                        │      │                            ╰ V3Score : 8.1 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60304             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56858        
                        │      │                  https://bugzilla.redhat.com/2515815                          
                        │      │                  https://bugzilla.redhat.com/2515820                          
                        │      │                  https://bugzilla.redhat.com/2515827                          
                        │      │                  https://bugzilla.redhat.com/2515838                          
                        │      │                  https://bugzilla.redhat.com/2515839                          
                        │      │                  https://bugzilla.redhat.com/2515840                          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │      │                  https://creativecommons.org/licenses/by/4.0/                 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-60304.html          
                        │      │                  https://errata.rockylinux.org/RLSA-2026:60304                
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
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ bitnami: 3 
                        │      │                  ├ redhat : 3 
                        │      │                  ╰ rocky  : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60304             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56859        
                        │      │                  https://bugzilla.redhat.com/2515815                          
                        │      │                  https://bugzilla.redhat.com/2515820                          
                        │      │                  https://bugzilla.redhat.com/2515827                          
                        │      │                  https://bugzilla.redhat.com/2515838                          
                        │      │                  https://bugzilla.redhat.com/2515839                          
                        │      │                  https://bugzilla.redhat.com/2515840                          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │      │                  https://creativecommons.org/licenses/by/4.0/                 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-60304.html          
                        │      │                  https://errata.rockylinux.org/RLSA-2026:60304                
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
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ bitnami: 2 
                        │      │                  ├ redhat : 3 
                        │      │                  ╰ rocky  : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 5.9 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60304             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56860        
                        │      │                  https://bugzilla.redhat.com/2515815                          
                        │      │                  https://bugzilla.redhat.com/2515820                          
                        │      │                  https://bugzilla.redhat.com/2515827                          
                        │      │                  https://bugzilla.redhat.com/2515838                          
                        │      │                  https://bugzilla.redhat.com/2515839                          
                        │      │                  https://bugzilla.redhat.com/2515840                          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │      │                  https://creativecommons.org/licenses/by/4.0/                 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-60304.html          
                        │      │                  https://errata.rockylinux.org/RLSA-2026:60304                
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
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ bitnami: 3 
                        │      │                  ├ redhat : 3 
                        │      │                  ╰ rocky  : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                    
                        │      │                  ─────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:60304             
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56862        
                        │      │                  https://bugzilla.redhat.com/2515815                          
                        │      │                  https://bugzilla.redhat.com/2515820                          
                        │      │                  https://bugzilla.redhat.com/2515827                          
                        │      │                  https://bugzilla.redhat.com/2515838                          
                        │      │                  https://bugzilla.redhat.com/2515839                          
                        │      │                  https://bugzilla.redhat.com/2515840                          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │      │                  https://creativecommons.org/licenses/by/4.0/                 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-60304.html          
                        │      │                  https://errata.rockylinux.org/RLSA-2026:60304                
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
