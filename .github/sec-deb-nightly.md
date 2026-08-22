```yaml

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
                        │     ├ Layer            ╭ Digest: sha256:de3238a5ec4d3db11079103736698ab6249e477670379
                        │     │                  │         034dca0ad08134837c6 
                        │     │                  ╰ DiffID: sha256:e3a5a27cb8f92e0d3bd6a735024cd6652a1105ea685eb
                        │     │                            fd01f096fe1d04df425 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-33818 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:673da5ff8b4c87dba906ba530841db73f05b5d2ea55318cec611f2
                        │     │                   d5b13c8bb2 
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
                        │     ├ VendorSeverity   ╭ bitnami: 3 
                        │     │                  ╰ redhat : 3 
                        │     ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                  │         │           /A:H 
                        │     │                  │         ╰ V3Score : 7.5 
                        │     │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                            │           /A:H 
                        │     │                            ╰ V3Score : 7.5 
                        │     ├ References                                                                
                        │     │                  ─────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-33818    
                        │     │                  https://go.dev/cl/814980                                 
                        │     │                  https://go.dev/issue/80405                               
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
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
                        │     ├ Layer            ╭ Digest: sha256:de3238a5ec4d3db11079103736698ab6249e477670379
                        │     │                  │         034dca0ad08134837c6 
                        │     │                  ╰ DiffID: sha256:e3a5a27cb8f92e0d3bd6a735024cd6652a1105ea685eb
                        │     │                            fd01f096fe1d04df425 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-39821 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:1843de568dd01b747e790537158d9ab22177db3e5bde9ff23a7ff1
                        │     │                   161831ba3d 
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
                        │     ╰ LastModifiedDate: 2026-08-21T13:17:38.087Z 
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
                        │     ├ Layer            ╭ Digest: sha256:de3238a5ec4d3db11079103736698ab6249e477670379
                        │     │                  │         034dca0ad08134837c6 
                        │     │                  ╰ DiffID: sha256:e3a5a27cb8f92e0d3bd6a735024cd6652a1105ea685eb
                        │     │                            fd01f096fe1d04df425 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46600 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:f4456882b79ddb08bf04c57f5c3c81123897e3ffa51c5cf2ee8133
                        │     │                   acfe97ed92 
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
                        │     ├ Layer            ╭ Digest: sha256:de3238a5ec4d3db11079103736698ab6249e477670379
                        │     │                  │         034dca0ad08134837c6 
                        │     │                  ╰ DiffID: sha256:e3a5a27cb8f92e0d3bd6a735024cd6652a1105ea685eb
                        │     │                            fd01f096fe1d04df425 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56853 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:c5e1e8691789a89658f4bd55697cf9edc4f5918f28a84d9b8adb61
                        │     │                   6d94d7c3e6 
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
                        │     ├ VendorSeverity   ╭ bitnami: 3 
                        │     │                  ╰ redhat : 3 
                        │     ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                  │         │           /A:H 
                        │     │                  │         ╰ V3Score : 7.5 
                        │     │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                            │           /A:H 
                        │     │                            ╰ V3Score : 7.5 
                        │     ├ References                                                                
                        │     │                  ─────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-56853    
                        │     │                  https://go.dev/cl/795540                                 
                        │     │                  https://go.dev/issue/80205                               
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
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
                        │     ├ Layer            ╭ Digest: sha256:de3238a5ec4d3db11079103736698ab6249e477670379
                        │     │                  │         034dca0ad08134837c6 
                        │     │                  ╰ DiffID: sha256:e3a5a27cb8f92e0d3bd6a735024cd6652a1105ea685eb
                        │     │                            fd01f096fe1d04df425 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56858 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:c8afafa80fee24d7624c8cb312800044e3ff621d757970f8eb6f2e
                        │     │                   45cca5c5f0 
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
                        │     ├ VendorSeverity   ╭ bitnami: 2 
                        │     │                  ╰ redhat : 3 
                        │     ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L
                        │     │                  │         │           /A:N 
                        │     │                  │         ╰ V3Score : 6.1 
                        │     │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H
                        │     │                            │           /A:N 
                        │     │                            ╰ V3Score : 8.1 
                        │     ├ References                                                                
                        │     │                  ─────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-56858    
                        │     │                  https://go.dev/cl/807100                                 
                        │     │                  https://go.dev/issue/80435                               
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
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
                        │     ├ Layer            ╭ Digest: sha256:de3238a5ec4d3db11079103736698ab6249e477670379
                        │     │                  │         034dca0ad08134837c6 
                        │     │                  ╰ DiffID: sha256:e3a5a27cb8f92e0d3bd6a735024cd6652a1105ea685eb
                        │     │                            fd01f096fe1d04df425 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56859 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:ce0b16a1a84d70875a09e94a51d088244a3625aeac00568f296dc6
                        │     │                   5a256edae7 
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
                        │     ├ VendorSeverity   ╭ bitnami: 3 
                        │     │                  ╰ redhat : 3 
                        │     ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                  │         │           /A:H 
                        │     │                  │         ╰ V3Score : 7.5 
                        │     │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                            │           /A:H 
                        │     │                            ╰ V3Score : 7.5 
                        │     ├ References                                                                
                        │     │                  ─────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-56859    
                        │     │                  https://go.dev/cl/803320                                 
                        │     │                  https://go.dev/issue/80481                               
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
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
                        │     ├ Layer            ╭ Digest: sha256:de3238a5ec4d3db11079103736698ab6249e477670379
                        │     │                  │         034dca0ad08134837c6 
                        │     │                  ╰ DiffID: sha256:e3a5a27cb8f92e0d3bd6a735024cd6652a1105ea685eb
                        │     │                            fd01f096fe1d04df425 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56860 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:21ea8176e71e9db5523039bb6ac1b3570caab9079c772bbf65689c
                        │     │                   a992403768 
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
                        │     ├ VendorSeverity   ╭ bitnami: 2 
                        │     │                  ╰ redhat : 3 
                        │     ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
                        │     │                  │         │           /A:H 
                        │     │                  │         ╰ V3Score : 5.9 
                        │     │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                            │           /A:H 
                        │     │                            ╰ V3Score : 7.5 
                        │     ├ References                                                                
                        │     │                  ─────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-56860    
                        │     │                  https://go.dev/cl/803681                                 
                        │     │                  https://go.dev/issue/80494                               
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
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
                              ├ Layer            ╭ Digest: sha256:de3238a5ec4d3db11079103736698ab6249e477670379
                              │                  │         034dca0ad08134837c6 
                              │                  ╰ DiffID: sha256:e3a5a27cb8f92e0d3bd6a735024cd6652a1105ea685eb
                              │                            fd01f096fe1d04df425 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56862 
                              ├ DataSource       ╭ ID  : govulndb 
                              │                  ├ Name: The Go Vulnerability Database 
                              │                  ╰ URL : https://pkg.go.dev/vuln/ 
                              ├ Fingerprint     : sha256:91774efe732f9731835646f7046f0c8de231774cbeefee5fe8ce0a
                              │                   f021b433eb 
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
                              ├ VendorSeverity   ╭ bitnami: 3 
                              │                  ╰ redhat : 3 
                              ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                              │                  │         │           /A:H 
                              │                  │         ╰ V3Score : 7.5 
                              │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                              │                            │           /A:H 
                              │                            ╰ V3Score : 7.5 
                              ├ References                                                                
                              │                  ─────────────────────────────────────────────────────────
                              │                  https://access.redhat.com/security/cve/CVE-2026-56862    
                              │                  https://go.dev/cl/804261                                 
                              │                  https://go.dev/issue/80528                               
                              │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI
                              │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56862          
                              │                  https://pkg.go.dev/vuln/GO-2026-6090                     
                              │                  https://www.cve.org/CVERecord?id=CVE-2026-56862          
                              │                  
                              ├ PublishedDate   : 2026-08-13T22:17:22.55Z 
                              ╰ LastModifiedDate: 2026-08-14T16:16:57.717Z 
```
