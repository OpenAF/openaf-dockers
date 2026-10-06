```yaml
╭ [0] ╭ Target         : openaf/ojobrt:latest (alpine 3.24.2) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2026-46675 
│                       │     ├ PkgID           : libpng@1.6.58-r1 
│                       │     ├ PkgName         : libpng 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libpng@1.6.58-r1?arch=x86_64&distro=3.2
│                       │     │                  │       4.2 
│                       │     │                  ╰ UID : 5b702c6b0c8725ba 
│                       │     ├ InstalledVersion: 1.6.58-r1 
│                       │     ├ FixedVersion    : 1.6.59-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:06c54cb65310c28a866ff9e4b895ebfbcc73b27fc8189
│                       │     │                  │         16ef4f8c4b2518cc144 
│                       │     │                  ╰ DiffID: sha256:b9e52e0d13340693b80046e437eb2438140f248fb5b14
│                       │     │                            b3b32f9a7946f8182a6 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46675 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Fingerprint     : sha256:15098422827a7ce5f567d409f1ec9977ad883081d1c8be18725ac7
│                       │     │                   37ed64910b 
│                       │     ├ Title           : [Use-after-free of zlib input in `png_read_end` after
│                       │     │                   incomplete zTXt, iTXt or iCCP decompression] 
│                       │     ├ Description     : [Use-after-free of zlib input in `png_read_end` after
│                       │     │                   incomplete zTXt, iTXt or iCCP decompression] 
│                       │     ├ Severity        : MEDIUM 
│                       │     ├ VendorSeverity   ─ ubuntu: 2 
│                       │     ╰ References                                                                     
│                       │                        ──────────────────────────────────────────────────────────────
│                       │                        https://github.com/pnggroup/libpng/issues/855                 
│                       │                        https://github.com/pnggroup/libpng/security/advisories/GHSA-qv
│                       │                        g3-h654-xq3j                                                  
│                       │                        https://www.cve.org/CVERecord?id=CVE-2026-46675               
│                       │                                                                                      
│                       │                        
│                       ╰ [1] ╭ VulnerabilityID : CVE-2026-58055 
│                             ├ PkgID           : nghttp2-libs@1.69.0-r0 
│                             ├ PkgName         : nghttp2-libs 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/nghttp2-libs@1.69.0-r0?arch=x86_64&dist
│                             │                  │       ro=3.24.2 
│                             │                  ╰ UID : cdceee5bd778a45c 
│                             ├ InstalledVersion: 1.69.0-r0 
│                             ├ FixedVersion    : 1.70.0-r0 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:06c54cb65310c28a866ff9e4b895ebfbcc73b27fc8189
│                             │                  │         16ef4f8c4b2518cc144 
│                             │                  ╰ DiffID: sha256:b9e52e0d13340693b80046e437eb2438140f248fb5b14
│                             │                            b3b32f9a7946f8182a6 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-58055 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Fingerprint     : sha256:32ccbe14941623d53d8ee71c0499b6198a3a20bab4bdd1976f30b9
│                             │                   7f1328773e 
│                             ├ Title           : nghttp2: nghttp2: HTTP Request/Response Smuggling and
│                             │                   Response-Queue Poisoning via ambiguous HTTP/1.1 Upgrade
│                             │                   requests 
│                             ├ Description     : nghttp2's nghttpx proxy through 1.69.0 forwards an HTTP/1.1
│                             │                   Upgrade request that also carries a Content-Length header and
│                             │                    body onto reusable keep-alive backend connections, re-adding
│                             │                    the Upgrade and Connection headers while passing
│                             │                   Content-Length verbatim. A backend that resolves the
│                             │                   resulting ambiguous message in the attacker's favor enables
│                             │                   HTTP request/response smuggling and cross-client
│                             │                   response-queue poisoning. 
│                             ├ Severity        : MEDIUM 
│                             ├ CweIDs                  
│                             │                  ───────
│                             │                  CWE-444
│                             │                  
│                             ├ VendorSeverity   ╭ alma       : 2 
│                             │                  ├ azure      : 2 
│                             │                  ├ julia      : 2 
│                             │                  ├ oracle-oval: 2 
│                             │                  ├ redhat     : 2 
│                             │                  ├ rocky      : 2 
│                             │                  ╰ ubuntu     : 2 
│                             ├ CVSS             ╭ julia  ╭ V3Vector : CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:L
│                             │                  │        │            /A:N 
│                             │                  │        ├ V40Vector: CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:L/V
│                             │                  │        │            I:L/VA:N/SC:N/SI:L/SA:N 
│                             │                  │        ├ V3Score  : 5.4 
│                             │                  │        ╰ V40Score : 6.3 
│                             │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:L/
│                             │                           │           A:N 
│                             │                           ╰ V3Score : 5.4 
│                             ├ References                                                                     
│                             │                  ──────────────────────────────────────────────────────────────
│                             │                  https://access.redhat.com/errata/RHSA-2026:54662              
│                             │                  https://access.redhat.com/security/cve/CVE-2026-58055         
│                             │                  https://bugzilla.redhat.com/2493954                           
│                             │                  https://bugzilla.redhat.com/show_bug.cgi?id=2493954           
│                             │                  https://creativecommons.org/licenses/by/4.0/                  
│                             │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-58055 
│                             │                  https://errata.almalinux.org/9/ALSA-2026-54662.html           
│                             │                  https://errata.rockylinux.org/RLSA-2026:54662                 
│                             │                  https://github.com/advisories/GHSA-xrr7-82jr-v58x             
│                             │                  https://github.com/bikini/exploitarium/tree/main/nghttp2-nghtt
│                             │                  px-upgrade-queue-poison-poc                                   
│                             │                  https://github.com/nghttp2/nghttp2/commit/ab28105c4a0197da24f8
│                             │                  bfc414bc116055249e1e                                          
│                             │                  https://linux.oracle.com/cve/CVE-2026-58055.html              
│                             │                                                                                
│                             │                  https://linux.oracle.com/errata/ELSA-2026-55804.html          
│                             │                                                                                
│                             │                  https://nvd.nist.gov/vuln/detail/CVE-2026-58055               
│                             │                                                                                
│                             │                  https://ubuntu.com/security/notices/USN-8495-1                
│                             │                                                                                
│                             │                  https://www.cve.org/CVERecord?id=CVE-2026-58055               
│                             │                                                                                
│                             │                  https://www.vulncheck.com/advisories/nghttp2-nghttpx-http-requ
│                             │                  est-response-smuggling-via-upgrade-request-with-content-length
│                             │                  
│                             ├ PublishedDate   : 2026-06-28T02:16:32.677Z 
│                             ╰ LastModifiedDate: 2026-06-30T17:41:26.433Z 

```
