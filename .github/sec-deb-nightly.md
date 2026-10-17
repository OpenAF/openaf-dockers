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
      ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-78667 
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
                        │      ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                        │      │                  │         f9912a3559dd645859fe 
                        │      │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                        │      │                            4f0763c4fdf4613b9d6c 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78667 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:b73b4a084cf40aff6f9404d6c4cca01b37249673dcb6d1a393ca0
                        │      │                   314d851a36d 
                        │      ├ Title           : net/http: golang: golang: Denial of Service via crafted HTTP
                        │      │                    Range headers 
                        │      ├ Description     : When parsing a Range header containing a large number of
                        │      │                   small ranges, FileServer(FS), ServeContent, and
                        │      │                   ServeFile(FS) can consume an excessive amount of CPU. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-770
                        │      ├ VendorSeverity   ╭ redhat: 3 
                        │      │                  ╰ ubuntu: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                           │           /A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-78667    
                        │      │                  https://github.com/golang/go/issues/81858                
                        │      │                  https://go.dev/cl/847309                                 
                        │      │                  https://go.dev/issue/81858                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-78667          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6609                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78667          
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9 
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.88Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:49.69Z 
                        ├ [1]  ╭ VulnerabilityID : CVE-2026-78669 
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
                        │      ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                        │      │                  │         f9912a3559dd645859fe 
                        │      │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                        │      │                            4f0763c4fdf4613b9d6c 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78669 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:3bea9160b1f0e53adf105eb65f5cef38a247ff3119ad9c4b435c2
                        │      │                   6c2e0d1f914 
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
                        │      ├ VendorSeverity   ╭ redhat: 3 
                        │      │                  ╰ ubuntu: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                           │           /A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-78669    
                        │      │                  https://github.com/golang/go/issues/81742                
                        │      │                  https://go.dev/cl/847186                                 
                        │      │                  https://go.dev/cl/847308                                 
                        │      │                  https://go.dev/issue/81742                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-78669          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6611                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78669          
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9 
                        │      ├ PublishedDate   : 2026-10-08T23:17:04.01Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:49.857Z 
                        ├ [2]  ╭ VulnerabilityID : CVE-2026-97031 
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
                        │      ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                        │      │                  │         f9912a3559dd645859fe 
                        │      │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                        │      │                            4f0763c4fdf4613b9d6c 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97031 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:8d191a250896c529c44c61f46d7344a82a92dec35b7d89ac27578
                        │      │                   cc87330d844 
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
                        │      ├ PublishedDate   : 2026-10-08T23:17:06.037Z 
                        │      ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
                        ├ [3]  ╭ VulnerabilityID : CVE-2026-56866 
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
                        │      ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                        │      │                  │         f9912a3559dd645859fe 
                        │      │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                        │      │                            4f0763c4fdf4613b9d6c 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56866 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:269e39c2cc90fa1ae9c7143358801aa8a73eeb68b1ff9bd579b98
                        │      │                   0da7b16c25a 
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
                        │      ├ VendorSeverity   ╭ redhat: 2 
                        │      │                  ╰ ubuntu: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56866    
                        │      │                  https://github.com/golang/go/issues/81740                
                        │      │                  https://go.dev/cl/847306                                 
                        │      │                  https://go.dev/issue/81740                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56866          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6605                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56866          
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9 
                        │      ├ PublishedDate   : 2026-10-08T23:17:01.62Z 
                        │      ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
                        ├ [4]  ╭ VulnerabilityID : CVE-2026-78659 
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
                        │      ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                        │      │                  │         f9912a3559dd645859fe 
                        │      │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                        │      │                            4f0763c4fdf4613b9d6c 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78659 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:213397545629cf2ae57133e2ba8fb63066f985533d3ec65beb3ae
                        │      │                   a545dac94e7 
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
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-405
                        │      ├ VendorSeverity   ─ ubuntu: 2 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://github.com/golang/go/issues/81857                
                        │      │                  https://go.dev/cl/847185                                 
                        │      │                  https://go.dev/cl/847314                                 
                        │      │                  https://go.dev/issue/81857                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6603                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78659          
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9 
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.27Z 
                        │      ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
                        ├ [5]  ╭ VulnerabilityID : CVE-2026-78660 
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
                        │      ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                        │      │                  │         f9912a3559dd645859fe 
                        │      │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                        │      │                            4f0763c4fdf4613b9d6c 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78660 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:da39fca27e5ade8bbbfc860261a853f69d8a940382242fa63020d
                        │      │                   14aa6f3c348 
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
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-444
                        │      ├ VendorSeverity   ─ ubuntu: 2 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://github.com/golang/go/issues/81115                
                        │      │                  https://go.dev/cl/835145                                 
                        │      │                  https://go.dev/cl/836385                                 
                        │      │                  https://go.dev/issue/81115                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6610                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78660          
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9 
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.51Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:49.243Z 
                        ├ [6]  ╭ VulnerabilityID : CVE-2026-78663 
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
                        │      ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                        │      │                  │         f9912a3559dd645859fe 
                        │      │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                        │      │                            4f0763c4fdf4613b9d6c 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78663 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:3f1885efc4851e59493e5387ffb4d22a0acfe12728b19c0539f0d
                        │      │                   e5e6c292b72 
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
                        │      ├ VendorSeverity   ╭ redhat: 2 
                        │      │                  ╰ ubuntu: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                           │           /A:L 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-78663    
                        │      │                  https://github.com/golang/go/issues/81743                
                        │      │                  https://go.dev/cl/847187                                 
                        │      │                  https://go.dev/cl/847310                                 
                        │      │                  https://go.dev/issue/81743                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-78663          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6612                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78663          
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9 
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.647Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:49.42Z 
                        ├ [7]  ╭ VulnerabilityID : CVE-2026-94439 
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
                        │      ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                        │      │                  │         f9912a3559dd645859fe 
                        │      │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                        │      │                            4f0763c4fdf4613b9d6c 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94439 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:441ea579742754e2ac414b0779d03feea9457fb84d48a1305af96
                        │      │                   ead2e4d539f 
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
                        │      ├ VendorSeverity   ╭ redhat: 2 
                        │      │                  ╰ ubuntu: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-94439    
                        │      │                  https://github.com/golang/go/issues/81744                
                        │      │                  https://go.dev/cl/847311                                 
                        │      │                  https://go.dev/issue/81744                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94439          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6613                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94439          
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9 
                        │      ├ PublishedDate   : 2026-10-08T23:17:04.76Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:50.703Z 
                        ├ [8]  ╭ VulnerabilityID : CVE-2026-94440 
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
                        │      ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                        │      │                  │         f9912a3559dd645859fe 
                        │      │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                        │      │                            4f0763c4fdf4613b9d6c 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94440 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:bfd3ce7225b1534593b6cdf357ed7c827026805f20b8d610eba5a
                        │      │                   8be40adc8e7 
                        │      ├ Title           : Parsing a multipart form can bypass memory limits and read
                        │      │                   an arbitrar ... 
                        │      ├ Description     : Parsing a multipart form can bypass memory limits and read
                        │      │                   an arbitrarily long line into memory when the remaining
                        │      │                   limit at the start of a part is less than 400 bytes. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-770
                        │      ├ VendorSeverity   ─ ubuntu: 2 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://github.com/golang/go/issues/81741                
                        │      │                  https://go.dev/cl/847307                                 
                        │      │                  https://go.dev/issue/81741                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6608                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94440          
                        │      │                  https://www.openwall.com/lists/oss-security/2026/10/08/9 
                        │      ├ PublishedDate   : 2026-10-08T23:17:04.917Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:50.907Z 
                        ├ [9]  ╭ VulnerabilityID : CVE-2026-94448 
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
                        │      ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                        │      │                  │         f9912a3559dd645859fe 
                        │      │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                        │      │                            4f0763c4fdf4613b9d6c 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94448 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:16b709229e990e2bd51a49397e022ce58bc8e06d4069098200d85
                        │      │                   1968acaa69a 
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
                        │      ├ VendorSeverity   ─ redhat: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 6.1 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-94448    
                        │      │                  https://go.dev/cl/839866                                 
                        │      │                  https://go.dev/issue/81821                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94448          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6599                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94448          
                        │      ├ PublishedDate   : 2026-10-08T23:17:05.3Z 
                        │      ╰ LastModifiedDate: 2026-10-15T16:18:24.327Z 
                        ├ [10] ╭ VulnerabilityID : CVE-2026-97032 
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
                        │      ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                        │      │                  │         f9912a3559dd645859fe 
                        │      │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                        │      │                            4f0763c4fdf4613b9d6c 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97032 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:db2904c9993f9c3348493b3cf27d119b32048b06783b5eae27080
                        │      │                   6520a840e1c 
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
                        │      ├ PublishedDate   : 2026-10-08T23:17:06.213Z 
                        │      ╰ LastModifiedDate: 2026-10-15T16:18:24.967Z 
                        ├ [11] ╭ VulnerabilityID : CVE-2026-56857 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6604
                        │      ├ PkgID           : stdlib@v1.27.1 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                        │      │                  ╰ UID : c9698e88b56a1f6e 
                        │      ├ InstalledVersion: v1.27.1 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                        │      │                  │         f9912a3559dd645859fe 
                        │      │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                        │      │                            4f0763c4fdf4613b9d6c 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56857 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:c6572768562484ddc176ca479e1f31280c3d3cec9c59387a2d7bc
                        │      │                   3896acfa0ff 
                        │      ├ Title           : os: golang: golang: Directory traversal via Windows junction
                        │      │                    handling 
                        │      ├ Description     : On Windows, when the target of Root.Mkdir or Root.MkdirAll
                        │      │                   is a junction pointing to an empty location, the operation
                        │      │                   can create a directory at the junction target even when that
                        │      │                    target is located outside the root. This only applies to
                        │      │                   operations where the last path component is a junction
                        │      │                   (path/to/junction, but not path/junction/target). 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs                   
                        │      │                  ────────
                        │      │                  CWE-1386
                        │      ├ VendorSeverity   ─ redhat: 1 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 3.3 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56857    
                        │      │                  https://go.dev/cl/847305                                 
                        │      │                  https://go.dev/issue/81739                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56857          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6604                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56857          
                        │      ├ PublishedDate   : 2026-10-08T23:17:01.487Z 
                        │      ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
                        ╰ [12] ╭ VulnerabilityID : CVE-2026-97030 
                               ├ VendorIDs                    
                               │                  ────────────
                               │                  GO-2026-6600
                               ├ PkgID           : stdlib@v1.27.1 
                               ├ PkgName         : stdlib 
                               ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.1 
                               │                  ╰ UID : c9698e88b56a1f6e 
                               ├ InstalledVersion: v1.27.1 
                               ├ FixedVersion    : 1.26.9, 1.27.2 
                               ├ Status          : fixed 
                               ├ Layer            ╭ Digest: sha256:768dfbf9840fedcd8e029cb028ae62439207c54b98c3
                               │                  │         f9912a3559dd645859fe 
                               │                  ╰ DiffID: sha256:be6070c5e8fd13fccba9c2804a2e9e5ca17cde8a3fb8
                               │                            4f0763c4fdf4613b9d6c 
                               ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97030 
                               ├ DataSource       ╭ ID  : govulndb 
                               │                  ├ Name: The Go Vulnerability Database 
                               │                  ╰ URL : https://pkg.go.dev/vuln/ 
                               ├ Fingerprint     : sha256:58d5b6a32df84bac469f1d64bef568a20ade948a778fa358f96f8
                               │                   6486f1862a0 
                               ├ Title           : A trusted template author may have previously written a
                               │                   valid template ... 
                               ├ Description     : A trusted template author may have previously written a
                               │                   valid template wherein the use of the 'yield' keyword would
                               │                   not be correctly escaped. We now ensure that valid keyword
                               │                   uses are escaped and non-keyword uses are not escaped. 
                               ├ Severity        : UNKNOWN 
                               ├ CweIDs                 
                               │                  ──────
                               │                  CWE-79
                               ├ References                                                                
                               │                  ─────────────────────────────────────────────────────────
                               │                  https://go.dev/cl/840925                                 
                               │                  https://go.dev/issue/81823                               
                               │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                               │                  https://pkg.go.dev/vuln/GO-2026-6600                     
                               ├ PublishedDate   : 2026-10-08T23:17:05.91Z 
                               ╰ LastModifiedDate: 2026-10-15T16:18:24.817Z 
```
