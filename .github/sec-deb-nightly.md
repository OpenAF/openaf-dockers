```yaml
╭ [0] ╭ Target  : openaf/oaf:deb-nightly (debian forky/sid) 
│     ├ Class   : os-pkgs 
│     ├ Type    : debian 
│     ╰ Packages 
├ [1] ╭ Target  : Java 
│     ├ Class   : lang-pkgs 
│     ├ Type    : jar 
│     ╰ Packages 
╰ [2] ╭ Target         : usr/bin/pebble 
      ├ Class          : lang-pkgs 
      ├ Type           : gobinary 
      ├ Packages        
      ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-111943 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6809
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.10, 1.27.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-111943 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:c1f5a439d3289f2e753b870420b4cc17600d4ab00d0a3a8ace80e
                        │      │                   77518bf09ba 
                        │      ├ Title           : crypto/x509: golang: crypto/x509: Man-in-the-middle attacks
                        │      │                   via untrusted intermediate certificates 
                        │      ├ Description     : On most platforms, Go uses the given system root
                        │      │                   certificates. However, in some narrower cases, the system
                        │      │                   trust stores may not be updated without further action. To
                        │      │                   defend against the narrower set of cases that may remain
                        │      │                   affected, a denylist was added in crypto/x509 to return an
                        │      │                   error when calling Verify with any of the known intermediate
                        │      │                    certificates that are no longer considered to be
                        │      │                   trustworthy. 
                        │      ├ Severity        : HIGH 
                        │      ├ VendorSeverity   ╭ alma       : 4 
                        │      │                  ├ oracle-oval: 4 
                        │      │                  ├ redhat     : 3 
                        │      │                  ╰ rocky      : 3 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 6.8 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  http://www.openwall.com/lists/oss-security/2026/10/20/29      
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/errata/RHSA-2026:88354              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-111943        
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-88354.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86196                 
                        │      │                  https://github.com/golang/go/issues/82345                     
                        │      │                  https://go.dev/cl/851047                                      
                        │      │                  https://go.dev/issue/82345                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/66pojueaQek     
                        │      │                  https://groups.google.com/g/golang-nuts/c/K22sG2AYnKU         
                        │      │                  https://linux.oracle.com/cve/CVE-2026-111943.html             
                        │      │                  https://linux.oracle.com/errata/ELSA-2026-88354.html          
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-111943              
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6809                          
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-111943              
                        │      ├ PublishedDate   : 2026-10-21T01:17:20.797Z 
                        │      ╰ LastModifiedDate: 2026-10-22T16:18:19.04Z 
                        ├ [1]  ╭ VulnerabilityID : CVE-2026-78667 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6609
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78667 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:2853a79636e57340d912c109e1fce815a19c8ce54d83e5bde344f
                        │      │                   93b05a2e711 
                        │      ├ Title           : net/http: golang: golang: Denial of Service via crafted HTTP
                        │      │                    Range headers 
                        │      ├ Description     : When parsing a Range header containing a large number of
                        │      │                   small ranges, FileServer(FS), ServeContent, and
                        │      │                   ServeFile(FS) can consume an excessive amount of CPU. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-770
                        │      ├ VendorSeverity   ╭ alma       : 3 
                        │      │                  ├ bitnami    : 3 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ redhat     : 3 
                        │      │                  ├ rocky      : 3 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-78667         
                        │      │                  https://bugzilla.redhat.com/2548334                           
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-86196.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86196                 
                        │      │                  https://github.com/golang/go/issues/81858                     
                        │      │                  https://go.dev/cl/847309                                      
                        │      │                  https://go.dev/issue/81858                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI     
                        │      │                  https://linux.oracle.com/cve/CVE-2026-78667.html              
                        │      │                  https://linux.oracle.com/errata/ELSA-2026-88336.html          
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-78667               
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6609                          
                        │      │                  https://ubuntu.com/security/notices/USN-8935-1                
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78667               
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9      
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.88Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:49.69Z 
                        ├ [2]  ╭ VulnerabilityID : CVE-2026-78669 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6611
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78669 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:cb8692626b159d045e701308abc8ba816639f0cc65e43ecc02baa
                        │      │                   cd2b322b0a0 
                        │      ├ Title           : net/http: net/http/internal/http2: golang.org/x/net/http2:
                        │      │                   net/http: Denial of Service via excessive HTTP/2 SETTINGS
                        │      │                   frames 
                        │      ├ Description     : A malicious HTTP/2 peer can cause excessive CPU consumption
                        │      │                   in the client or server by opening a large number of streams
                        │      │                    and then sending many small SETTINGS frames containing
                        │      │                   SETTINGS_INITIAL_WINDOW_SIZE values. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-405
                        │      ├ VendorSeverity   ╭ alma       : 4 
                        │      │                  ├ azure      : 3 
                        │      │                  ├ bitnami    : 3 
                        │      │                  ├ oracle-oval: 4 
                        │      │                  ├ redhat     : 3 
                        │      │                  ├ rocky      : 3 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/errata/RHSA-2026:88354              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-78669         
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-88354.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86196                 
                        │      │                  https://github.com/golang/go/issues/81742                     
                        │      │                  https://go.dev/cl/847186                                      
                        │      │                  https://go.dev/cl/847308                                      
                        │      │                  https://go.dev/issue/81742                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI     
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs     
                        │      │                  https://linux.oracle.com/cve/CVE-2026-78669.html              
                        │      │                  https://linux.oracle.com/errata/ELSA-2026-88354.html          
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-78669               
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6611                          
                        │      │                  https://ubuntu.com/security/notices/USN-8935-1                
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78669               
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9      
                        │      ├ PublishedDate   : 2026-10-08T23:17:04.01Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:49.857Z 
                        ├ [3]  ╭ VulnerabilityID : CVE-2026-97031 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6607
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97031 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:3add51312bf7ab7ccd84b2b1dc733eed7ebe98b50e736fda8446d
                        │      │                   1f3309c1643 
                        │      ├ Title           : crypto/tls: golang: crypto/tls: Denial of Service via
                        │      │                   multiple ECH outer extension references 
                        │      ├ Description     : Multiple ECH outer extension references are not permitted
                        │      │                   under RFC 9849; previously, a client could send a
                        │      │                   well-crafted packet that could trigger memory exhaustion in
                        │      │                   the server process by specifying multiple references. We now
                        │      │                    reject these as malformed and curb the memory amplification
                        │      │                    vector as a result. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-405
                        │      ├ VendorSeverity   ╭ alma       : 4 
                        │      │                  ├ bitnami    : 3 
                        │      │                  ├ oracle-oval: 4 
                        │      │                  ├ redhat     : 3 
                        │      │                  ╰ rocky      : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/errata/RHSA-2026:88354              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-97031         
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-88354.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86196                 
                        │      │                  https://go.dev/cl/847312                                      
                        │      │                  https://go.dev/issue/81855                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI     
                        │      │                  https://linux.oracle.com/cve/CVE-2026-97031.html              
                        │      │                  https://linux.oracle.com/errata/ELSA-2026-88354.html          
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-97031               
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6607                          
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-97031               
                        │      ├ PublishedDate   : 2026-10-08T23:17:06.037Z 
                        │      ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
                        ├ [4]  ╭ VulnerabilityID : CVE-2026-56866 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6605
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56866 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:9a50a0bf8f29526db66bad3c35b5096fa799f0facf71a8de9abb7
                        │      │                   fb2010d9785 
                        │      ├ Title           : net/http: golang: golang: Cross-user response poisoning via
                        │      │                   desynchronized HTTP CONNECT connections 
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
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-444
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ bitnami: 3 
                        │      │                  ├ redhat : 2 
                        │      │                  ├ rocky  : 3 
                        │      │                  ╰ ubuntu : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
                        │      │                  │         │           N/A:N 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
                        │      │                            │           L/A:N 
                        │      │                            ╰ V3Score : 6.5 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86203              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56866         
                        │      │                  https://bugzilla.redhat.com/2548334                           
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548335           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548337           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548338           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548339           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548340           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548341           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548342           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548343           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548345           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548346           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548347           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56866 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78659 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78660 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78663 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94439 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94440 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94444 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94447 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94448 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97030 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97032 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-86196.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86203                 
                        │      │                  https://github.com/golang/go/issues/81740                     
                        │      │                  https://go.dev/cl/847306                                      
                        │      │                  https://go.dev/issue/81740                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI     
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56866               
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6605                          
                        │      │                  https://ubuntu.com/security/notices/USN-8935-1                
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56866               
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9      
                        │      ├ PublishedDate   : 2026-10-08T23:17:01.62Z 
                        │      ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
                        ├ [5]  ╭ VulnerabilityID : CVE-2026-78659 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6603
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78659 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:0c4792ff534369541a45344593d6a01d26327911baa8f8ff94272
                        │      │                   8b129062fd1 
                        │      ├ Title           : net/http: golang.org/x/net/http2: golang: net/http: Denial
                        │      │                   of Service via HTTP/2 trailer header memory exhaustion 
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
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-405
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ azure  : 2 
                        │      │                  ├ bitnami: 3 
                        │      │                  ├ redhat : 2 
                        │      │                  ├ rocky  : 3 
                        │      │                  ╰ ubuntu : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86203              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-78659         
                        │      │                  https://bugzilla.redhat.com/2548334                           
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548335           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548337           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548338           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548339           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548340           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548341           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548342           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548343           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548345           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548346           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548347           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56866 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78659 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78660 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78663 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94439 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94440 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94444 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94447 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94448 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97030 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97032 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-86196.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86203                 
                        │      │                  https://github.com/golang/go/issues/81857                     
                        │      │                  https://go.dev/cl/847185                                      
                        │      │                  https://go.dev/cl/847314                                      
                        │      │                  https://go.dev/issue/81857                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI     
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs     
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-78659               
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6603                          
                        │      │                  https://ubuntu.com/security/notices/USN-8935-1                
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78659               
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9      
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.27Z 
                        │      ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
                        ├ [6]  ╭ VulnerabilityID : CVE-2026-78660 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6610
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78660 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:f3a4e89976e2df14ebbc9cb86e42cfadd95e4750a7c4c094c049d
                        │      │                   2e7d692aae8 
                        │      ├ Title           : net/http: golang: golang.org/x/net/http2: net/http: HTTP
                        │      │                   response smuggling via malformed HTTP/2 framing headers 
                        │      ├ Description     : Historically, we have been rather lax about malformed
                        │      │                   framing-related headers in our HTTP/2 implementation, as
                        │      │                   they cannot interfere with HTTP/2 framing. However, this
                        │      │                   makes it possible for our HTTP/2 implementation to forward
                        │      │                   responses containing such headers to an HTTP/1 client when
                        │      │                   acting as a reverse proxy. If the HTTP/1 client also does
                        │      │                   not behave strictly enough, this can result in response
                        │      │                   smuggling. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-444
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ azure  : 3 
                        │      │                  ├ bitnami: 3 
                        │      │                  ├ redhat : 2 
                        │      │                  ├ rocky  : 3 
                        │      │                  ╰ ubuntu : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           H/A:N 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           H/A:N 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86203              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-78660         
                        │      │                  https://bugzilla.redhat.com/2548334                           
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548335           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548337           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548338           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548339           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548340           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548341           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548342           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548343           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548345           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548346           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548347           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56866 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78659 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78660 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78663 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94439 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94440 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94444 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94447 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94448 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97030 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97032 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-86196.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86203                 
                        │      │                  https://github.com/golang/go/issues/81115                     
                        │      │                  https://go.dev/cl/835145                                      
                        │      │                  https://go.dev/cl/836385                                      
                        │      │                  https://go.dev/issue/81115                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI     
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-78660               
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6610                          
                        │      │                  https://ubuntu.com/security/notices/USN-8935-1                
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78660               
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9      
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.51Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:49.243Z 
                        ├ [7]  ╭ VulnerabilityID : CVE-2026-78663 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6612
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78663 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:8f388e9db77bcba52a130f4d453488c0b5505cb3bad161538270c
                        │      │                   51f4ec75bbb 
                        │      ├ Title           : net/http: net/http/internal/http2: golang:
                        │      │                   golang.org/x/net/http2: golang: flow control limit bypass
                        │      │                   via double refund in HTTP/2 server 
                        │      ├ Description     : The HTTP/2 server can refund connection-level flow control
                        │      │                   twice for the same data: Once when a client resets a stream
                        │      │                   (refunding data for any sent-but-unread portion of the
                        │      │                   stream), and again when a request handler reads the buffered
                        │      │                    data. A malicious client can exploit this to bypass the
                        │      │                   configured connection-level flow control limit
                        │      │                   (MaxReceiveBufferPerConnection). Total buffered data is
                        │      │                   still limited by the concurrent stream limit and
                        │      │                   stream-level flow control. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-675
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ azure  : 3 
                        │      │                  ├ bitnami: 4 
                        │      │                  ├ redhat : 2 
                        │      │                  ├ rocky  : 3 
                        │      │                  ╰ ubuntu : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           H/A:H 
                        │      │                  │         ╰ V3Score : 9.1 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:L 
                        │      │                            ╰ V3Score : 5.3 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86203              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-78663         
                        │      │                  https://bugzilla.redhat.com/2548334                           
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548335           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548337           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548338           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548339           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548340           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548341           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548342           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548343           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548345           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548346           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548347           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56866 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78659 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78660 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78663 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94439 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94440 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94444 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94447 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94448 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97030 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97032 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-86196.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86203                 
                        │      │                  https://github.com/golang/go/issues/81743                     
                        │      │                  https://go.dev/cl/847187                                      
                        │      │                  https://go.dev/cl/847310                                      
                        │      │                  https://go.dev/issue/81743                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI     
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs     
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-78663               
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6612                          
                        │      │                  https://ubuntu.com/security/notices/USN-8935-1                
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78663               
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9      
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.647Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:49.42Z 
                        ├ [8]  ╭ VulnerabilityID : CVE-2026-94439 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6613
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94439 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:1a37506d5eb8396be34b8c4fe99bb30c67f8e5b9417edf833e31b
                        │      │                   8cbaf08c5bc 
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
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-444
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ bitnami: 3 
                        │      │                  ├ redhat : 2 
                        │      │                  ├ rocky  : 3 
                        │      │                  ╰ ubuntu : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
                        │      │                  │         │           N/A:N 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
                        │      │                            │           L/A:N 
                        │      │                            ╰ V3Score : 6.5 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86203              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-94439         
                        │      │                  https://bugzilla.redhat.com/2548334                           
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548335           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548337           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548338           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548339           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548340           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548341           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548342           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548343           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548345           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548346           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548347           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56866 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78659 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78660 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78663 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94439 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94440 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94444 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94447 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94448 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97030 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97032 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-86196.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86203                 
                        │      │                  https://github.com/golang/go/issues/81744                     
                        │      │                  https://go.dev/cl/847311                                      
                        │      │                  https://go.dev/issue/81744                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI     
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94439               
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6613                          
                        │      │                  https://ubuntu.com/security/notices/USN-8935-1                
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94439               
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9      
                        │      ├ PublishedDate   : 2026-10-08T23:17:04.76Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:50.703Z 
                        ├ [9]  ╭ VulnerabilityID : CVE-2026-94440 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6608
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94440 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:ec1b2043e5bb80e324eb7ce4e247b08f76db89e628ba827c7058e
                        │      │                   1a061d2ca32 
                        │      ├ Title           : net/textproto: mime/multipart: golang: golang: Denial of
                        │      │                   Service via memory limit bypass in multipart form parsing 
                        │      ├ Description     : Parsing a multipart form can bypass memory limits and read
                        │      │                   an arbitrarily long line into memory when the remaining
                        │      │                   limit at the start of a part is less than 400 bytes. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-770
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ bitnami: 3 
                        │      │                  ├ redhat : 2 
                        │      │                  ├ rocky  : 3 
                        │      │                  ╰ ubuntu : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86203              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-94440         
                        │      │                  https://bugzilla.redhat.com/2548334                           
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548335           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548337           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548338           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548339           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548340           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548341           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548342           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548343           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548345           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548346           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548347           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56866 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78659 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78660 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78663 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94439 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94440 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94444 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94447 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94448 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97030 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97032 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-86196.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86203                 
                        │      │                  https://github.com/golang/go/issues/81741                     
                        │      │                  https://go.dev/cl/847307                                      
                        │      │                  https://go.dev/issue/81741                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI     
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94440               
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6608                          
                        │      │                  https://ubuntu.com/security/notices/USN-8935-1                
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94440               
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9      
                        │      ├ PublishedDate   : 2026-10-08T23:17:04.917Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:50.907Z 
                        ├ [10] ╭ VulnerabilityID : CVE-2026-94448 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6599
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94448 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:26f321da29675898d5899cb5a226a4a73b37287b98c3480f89a9e
                        │      │                   6df2b99a586 
                        │      ├ Title           : html/template: golang: golang: cross-site scripting via
                        │      │                   consecutive expressions in JavaScript template literals 
                        │      ├ Description     : When a JavaScript template literal contains consecutive
                        │      │                   expressions, the context tracking state was not properly
                        │      │                   reset upon entering a new expression. We now ensure that
                        │      │                   template-literal expression entries correctly reset context
                        │      │                   variables so all subsequent regular expression literals are
                        │      │                   accurately recognized and escaped. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                 
                        │      │                  ──────
                        │      │                  CWE-79
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ bitnami: 2 
                        │      │                  ├ redhat : 2 
                        │      │                  ╰ rocky  : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:
                        │      │                  │         │           L/A:N 
                        │      │                  │         ╰ V3Score : 6.1 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:
                        │      │                            │           L/A:N 
                        │      │                            ╰ V3Score : 6.1 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86203              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-94448         
                        │      │                  https://bugzilla.redhat.com/2548334                           
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548335           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548337           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548338           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548339           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548340           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548341           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548342           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548343           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548345           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548346           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548347           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56866 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78659 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78660 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78663 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94439 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94440 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94444 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94447 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94448 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97030 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97032 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-86196.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86203                 
                        │      │                  https://go.dev/cl/839866                                      
                        │      │                  https://go.dev/issue/81821                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI     
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94448               
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6599                          
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94448               
                        │      ├ PublishedDate   : 2026-10-08T23:17:05.3Z 
                        │      ╰ LastModifiedDate: 2026-10-15T16:18:24.327Z 
                        ├ [11] ╭ VulnerabilityID : CVE-2026-97030 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6600
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97030 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:4ae83daa7bbb440e69357a3b3c1559ccfc9b8d7ec4952d246849f
                        │      │                   41fdff89ab5 
                        │      ├ Title           : html/template: golang: html/template: Cross-site scripting
                        │      │                   via improper escaping of yield keyword 
                        │      ├ Description     : A trusted template author may have previously written a
                        │      │                   valid template wherein the use of the 'yield' keyword would
                        │      │                   not be correctly escaped. We now ensure that valid keyword
                        │      │                   uses are escaped and non-keyword uses are not escaped. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                 
                        │      │                  ──────
                        │      │                  CWE-79
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ bitnami: 2 
                        │      │                  ├ redhat : 2 
                        │      │                  ╰ rocky  : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:
                        │      │                  │         │           L/A:N 
                        │      │                  │         ╰ V3Score : 6.1 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:
                        │      │                            │           L/A:N 
                        │      │                            ╰ V3Score : 6.1 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86203              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-97030         
                        │      │                  https://bugzilla.redhat.com/2548334                           
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548335           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548337           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548338           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548339           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548340           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548341           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548342           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548343           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548345           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548346           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548347           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56866 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78659 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78660 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78663 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94439 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94440 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94444 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94447 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94448 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97030 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97032 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-86196.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86203                 
                        │      │                  https://go.dev/cl/840925                                      
                        │      │                  https://go.dev/issue/81823                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI     
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-97030               
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6600                          
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-97030               
                        │      ├ PublishedDate   : 2026-10-08T23:17:05.91Z 
                        │      ╰ LastModifiedDate: 2026-10-15T16:18:24.817Z 
                        ├ [12] ╭ VulnerabilityID : CVE-2026-97032 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6617
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                        │      │                  │         c2027f3cf037c583465d 
                        │      │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                        │      │                            20362b481fd7d5556be4 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97032 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:c1adf7877ea40f5d05eb1fbcb4026d60201ca05a5a51f14f019ad
                        │      │                   e39f2777c22 
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
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-362
                        │      ├ VendorSeverity   ╭ alma   : 3 
                        │      │                  ├ azure  : 2 
                        │      │                  ├ bitnami: 3 
                        │      │                  ├ redhat : 2 
                        │      │                  ╰ rocky  : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 5.9 
                        │      ├ References                                                                     
                        │      │                  ──────────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86196              
                        │      │                  https://access.redhat.com/errata/RHSA-2026:86203              
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-97032         
                        │      │                  https://bugzilla.redhat.com/2548334                           
                        │      │                  https://bugzilla.redhat.com/2548336                           
                        │      │                  https://bugzilla.redhat.com/2548344                           
                        │      │                  https://bugzilla.redhat.com/2556068                           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548334           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548335           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548336           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548337           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548338           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548339           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548340           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548341           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548342           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548343           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548344           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548345           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548346           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2548347           
                        │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2556068           
                        │      │                  https://creativecommons.org/licenses/by/4.0/                  
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56866 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78659 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78660 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78663 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78667 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-78669 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94439 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94440 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94444 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94447 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-94448 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97030 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97031 
                        │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97032 
                        │      │                  https://errata.almalinux.org/9/ALSA-2026-86196.html           
                        │      │                  https://errata.rockylinux.org/RLSA-2026:86203                 
                        │      │                  https://go.dev/cl/847188                                      
                        │      │                  https://go.dev/cl/847313                                      
                        │      │                  https://go.dev/issue/81867                                    
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI     
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs     
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-97032               
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6617                          
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-97032               
                        │      ├ PublishedDate   : 2026-10-08T23:17:06.213Z 
                        │      ╰ LastModifiedDate: 2026-10-15T16:18:24.967Z 
                        ╰ [13] ╭ VulnerabilityID : CVE-2026-56857 
                               ├ VendorIDs                    
                               │                  ────────────
                               │                  GO-2026-6604
                               ├ PkgID           : stdlib@v1.27.1 
                               ├ PkgName         : stdlib 
                               ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                               │                  ╰ UID : c9698e88b56a1f6e 
                               ├ InstalledVersion: v1.27.1 
                               ├ FixedVersion    : 1.26.9, 1.27.2 
                               ├ Status          : fixed 
                               ├ Layer            ╭ Digest: sha256:a253a63884f604328174facdd774aebf684bbf903137
                               │                  │         c2027f3cf037c583465d 
                               │                  ╰ DiffID: sha256:4f2552b1bf6933008d919ff056b92aa734444b2f8526
                               │                            20362b481fd7d5556be4 
                               ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56857 
                               ├ DataSource       ╭ ID  : govulndb 
                               │                  ├ Name: The Go Vulnerability Database 
                               │                  ╰ URL : https://pkg.go.dev/vuln/ 
                               ├ Fingerprint     : sha256:bfd2e8bb9f0588c00433ddd17d7170ffd5e52ae2e0e9454830b26
                               │                   8570f1c25d4 
                               ├ Title           : os: golang: golang: Directory traversal via Windows junction
                               │                    handling 
                               ├ Description     : On Windows, when the target of Root.Mkdir or Root.MkdirAll
                               │                   is a junction pointing to an empty location, the operation
                               │                   can create a directory at the junction target even when that
                               │                    target is located outside the root. This only applies to
                               │                   operations where the last path component is a junction
                               │                   (path/to/junction, but not path/junction/target). 
                               ├ Severity        : LOW 
                               ├ CweIDs                   
                               │                  ────────
                               │                  CWE-1386
                               ├ VendorSeverity   ╭ bitnami: 4 
                               │                  ╰ redhat : 1 
                               ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
                               │                  │         │           H/A:H 
                               │                  │         ╰ V3Score : 9.8 
                               │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:
                               │                            │           L/A:N 
                               │                            ╰ V3Score : 3.3 
                               ├ References                                                                
                               │                  ─────────────────────────────────────────────────────────
                               │                  https://access.redhat.com/security/cve/CVE-2026-56857    
                               │                  https://go.dev/cl/847305                                 
                               │                  https://go.dev/issue/81739                               
                               │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                               │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56857          
                               │                  https://pkg.go.dev/vuln/GO-2026-6604                     
                               │                  https://www.cve.org/CVERecord?id=CVE-2026-56857          
                               ├ PublishedDate   : 2026-10-08T23:17:01.487Z 
                               ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
```
