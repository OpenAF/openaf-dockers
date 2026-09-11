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
│                       │      ├ Fingerprint     : sha256:108e88f115203913bec1d751c62165981bd04f3102e910e97bd14
│                       │      │                   a9b88e131de 
│                       │      ├ Title           : A flaw in the libcurl SASL negotiation for LDAP
│                       │      │                   authentication allows  ... 
│                       │      ├ Description     : A flaw in the libcurl SASL negotiation for LDAP
│                       │      │                   authentication allows an
│                       │      │                   incomplete handshake sequence to be misinterpreted as a
│                       │      │                   successful
│                       │      │                   cryptographic verification. An attacker executing a
│                       │      │                   Man-in-the-Middle (MITM)
│                       │      │                   attack can inject a premature or shortcut response that
│                       │      │                   bypasses complete peer
│                       │      │                   validation. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-923
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-13608.html                     
│                       │      │                  https://curl.se/docs/CVE-2026-13608.json                     
│                       │      │                  https://github.com/curl/curl/pull/22213/changes/1a00e2a73675c
│                       │      │                  9521d214aafd6c02b553bfeb022                                  
│                       │      │                  https://hackerone.com/reports/3822248                        
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-13608              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:19.81Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T16:18:00.317Z 
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
│                       │      ├ Fingerprint     : sha256:f9bc9371c54ae4fc71955cdd54b5840357aeab05188b5357d3962
│                       │      │                   200f3b5ad45 
│                       │      ├ Title           : A flaw in libcurl's handling of HTTP/2 Server Push streams,
│                       │      │                   when the p ... 
│                       │      ├ Description     : A flaw in libcurl's handling of HTTP/2 Server Push streams,
│                       │      │                   when the parent
│                       │      │                   handle is set to share connections with other handles, can
│                       │      │                   lead to
│                       │      │                   use-after-free in the cleanup process. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-416
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-18924.html                     
│                       │      │                  https://curl.se/docs/CVE-2026-18924.json                     
│                       │      │                  https://github.com/curl/curl/commit/90325ff0444cbdff368bda5d2
│                       │      │                  6d6                                                          
│                       │      │                  https://hackerone.com/reports/3916059                        
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18924              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:20.553Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T16:18:06Z 
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
│                       │      ├ Fingerprint     : sha256:64151dfdb3bd335a4e05b67646d4713b6d8096bc8087eaf1ca9ab
│                       │      │                   047cb37c60f 
│                       │      ├ Title           : A flaw in libcurl makes it wrongly reuse an HTTP connection
│                       │      │                   setup for  ... 
│                       │      ├ Description     : A flaw in libcurl makes it wrongly reuse an HTTP connection
│                       │      │                   setup for a given
│                       │      │                   hostname using Negotiate authentication, when the initial
│                       │      │                   request is done
│                       │      │                   using empty credentials. This can make user B's request get
│                       │      │                   sent over user A's
│                       │      │                   previously authenticated connection. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-488
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                 
│                       │      │                  ──────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-19931.html                  
│                       │      │                  https://curl.se/docs/CVE-2026-19931.json                  
│                       │      │                  https://github.com/curl/curl/commit/7103a93b05bc69ea98ed9d
│                       │      │                  https://hackerone.com/reports/3923520                     
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-19931           
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:20.733Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T16:18:07.08Z 
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
│                       │      ├ Fingerprint     : sha256:5e7baa6748ac925b2ccca5c70d86461da62442627aed47b4a3b2e
│                       │      │                   869dc071226 
│                       │      ├ Title           : When performing transfers via libcurl\u2019s multi
│                       │      │                   interface, pooled T ... 
│                       │      ├ Description     : When performing transfers via libcurl’s multi interface,
│                       │      │                   pooled TLS
│                       │      │                   connections can outlive their originating easy handles. In
│                       │      │                   OpenSSL 3 provider
│                       │      │                   configurations, libcurl attaches an allocated library
│                       │      │                   context to the easy
│                       │      │                   handle's state and passes it to OpenSSL without acquiring an
│                       │      │                    ownership
│                       │      │                   reference; destroying the easy handle prematurely frees this
│                       │      │                    context while the
│                       │      │                   active connection retains a dangling pointer, leading to a
│                       │      │                   heap-use-after-free
│                       │      │                   upon subsequent I/O or post-handshake operations. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-416
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                 
│                       │      │                  ──────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80229.html                  
│                       │      │                  https://curl.se/docs/CVE-2026-80229.json                  
│                       │      │                  https://github.com/curl/curl/commit/7ea37abc6ac0120ba5f6d9
│                       │      │                  https://hackerone.com/reports/3969255                     
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-80229           
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.217Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T16:18:15.72Z 
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
│                       │      ├ Fingerprint     : sha256:688fced8bbee8ed20d19202dcbdf4c20cc3707be02c751fbcbc6c
│                       │      │                   415a41f56a8 
│                       │      ├ Title           : When `CURLOPT_PINNEDPUBLICKEY` is configured alongside
│                       │      │                   options that di ... 
│                       │      ├ Description     : When `CURLOPT_PINNEDPUBLICKEY` is configured alongside
│                       │      │                   options that disable
│                       │      │                   standard peer verification (`CURLOPT_SSL_VERIFYPEER = 0`
│                       │      │                   and
│                       │      │                   `CURLOPT_SSL_VERIFYHOST = 0`), libcurl fails to enforce
│                       │      │                   public key pinning on
│                       │      │                   connections established without a presented server
│                       │      │                   certificate. Bypassing the
│                       │      │                   pinning check under these disabled-verification conditions
│                       │      │                   allows
│                       │      │                   unauthenticated connections to succeed when they should be
│                       │      │                   rejected. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-295
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                
│                       │      │                  ─────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80230.html                 
│                       │      │                  https://curl.se/docs/CVE-2026-80230.json                 
│                       │      │                  https://github.com/curl/curl/commit/5267ed859d545534d0c21
│                       │      │                  https://hackerone.com/reports/3969300                    
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-80230          
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.327Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T19:19:54.063Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-80255 
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
│                       │      ├ Fingerprint     : sha256:0bde39af8ee717489d30e1f543ef6fc5495193f7a963bc4458973
│                       │      │                   c8ffcce137d 
│                       │      ├ Title           : A `Set-Cookie:` header using tab (horizontal tab, ASCII code
│                       │      │                    9) instea ... 
│                       │      ├ Description     : A `Set-Cookie:` header using tab (horizontal tab, ASCII code
│                       │      │                    9) instead of
│                       │      │                   space (ascii code 32) immediately before the `Secure`
│                       │      │                   attribute causes curl to
│                       │      │                   store the cookie without its Secure flag. The cookie might
│                       │      │                   then wrongfully be
│                       │      │                   sent over plaintext HTTP on subsequent requests to the same
│                       │      │                   host. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-201
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                 
│                       │      │                  ──────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80255.html                  
│                       │      │                  https://curl.se/docs/CVE-2026-80255.json                  
│                       │      │                  https://github.com/curl/curl/commit/4f6aa41a0145e930e76677
│                       │      │                  https://hackerone.com/reports/3972395                     
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-80255           
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.623Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T19:19:54.52Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-82209 
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
│                       │      ├ Fingerprint     : sha256:500e2009e0f995f90f40e6025986403b3b9b4d9cd696b6a620346
│                       │      │                   4d93d1ea551 
│                       │      ├ Title           : When libpsl support is enabled, libcurl fails to enforce the
│                       │      │                    Public Su ... 
│                       │      ├ Description     : When libpsl support is enabled, libcurl fails to enforce the
│                       │      │                    Public Suffix
│                       │      │                   List boundary check when processing a `Set-Cookie` header
│                       │      │                   where the `Domain`
│                       │      │                   attribute explicitly matches an origin host that is itself a
│                       │      │                    public suffix
│                       │      │                   (e.g., `Domain=co.uk` set by `co.uk`).
│                       │      │                   
│                       │      │                   Instead of coercing it into a strict host-only cookie,
│                       │      │                   libcurl saves the
│                       │      │                   cookie with wildcard domain scope (`.co.uk`). Consequently,
│                       │      │                   the cookie is
│                       │      │                   inappropriately included in subsequent outbound requests or
│                       │      │                   HTTP redirects to
│                       │      │                   arbitrary sibling subdomains under the same public suffix
│                       │      │                   (e.g.,
│                       │      │                   `attacker.co.uk`). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-201
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                      
│                       │      │                  ───────────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-82209.html                       
│                       │      │                  https://curl.se/docs/CVE-2026-82209.json                       
│                       │      │                  https://github.com/curl/curl/commit/95c1e8915dce64606bd753fd47f
│                       │      │                  https://hackerone.com/reports/3972385                          
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-82209                
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.847Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T19:20:00.313Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-80231 
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
│                       │      ├ Fingerprint     : sha256:f79ea810c13ccb9db2864dcac2c443e3438912786f9c92770374f
│                       │      │                   d13437d94c1 
│                       │      ├ Title           : A flaw in libcurl makes it wrongly reuse an existing HTTPS
│                       │      │                   connec ... 
│                       │      ├ Description     : A flaw in libcurl makes it wrongly reuse an existing HTTPS
│                       │      │                   connection setup
│                       │      │                   for a given hostname even when using a different Native CA
│                       │      │                   Store setting
│                       │      │                   (`CURLSSLOPT_NATIVE_CA`) than when the connection was
│                       │      │                   created. 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-488
│                       │      │                  
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80231.html
│                       │      │                  https://curl.se/docs/CVE-2026-80231.json
│                       │      │                  https://hackerone.com/reports/3969368   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.5Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T19:19:54.307Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-80256 
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
│                       │      ├ Fingerprint     : sha256:f2fb79fdd6cb13f670848e01683ca4a74dd4c75f4c80963503396
│                       │      │                   858f0419d75 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-82208 
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
│                       │      ├ Fingerprint     : sha256:793f517123ebba19634c21135b28cc66d2074404c5712c8a73316
│                       │      │                   e6e225780f0 
│                       │      ├ Title           : With the wolfSSL backend, when CA caching is enabled and an
│                       │      │                   `CURLOPT_S ... 
│                       │      ├ Description     : With the wolfSSL backend, when CA caching is enabled and an
│                       │      │                   `CURLOPT_SSL_CTX_FUNCTION` callback replaces the trust
│                       │      │                   store, libcurl can
│                       │      │                   silently reinstall the cached store after the callback
│                       │      │                   returns. A certificate
│                       │      │                   trusted by the cached store but rejected by the
│                       │      │                   callback-selected store is
│                       │      │                   then incorrectly accepted. 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-295
│                       │      │                  
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-82208.html
│                       │      │                  https://curl.se/docs/CVE-2026-82208.json
│                       │      │                  https://hackerone.com/reports/3973090   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.733Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T19:20:00.13Z 
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
│                       │      ├ Fingerprint     : sha256:604f5b09dd57c94ecf73e78251484acabc5f196f5542a9d072dd2
│                       │      │                   09a1621621b 
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
│                       │      ├ Fingerprint     : sha256:eff9080eef84f8de3c4e1d7342ce172748a1c99481e73ffaf521b
│                       │      │                   49eebcebc65 
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
│                       │      ├ Fingerprint     : sha256:ac920973235c061781ddcc2aa8dbe66f73f1fb9516f08614447d4
│                       │      │                   a0ace3e1bc9 
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
│                       │      ├ Fingerprint     : sha256:10e06ed9c45a0451e70d76fec0ccaa33b0e035cd8e377be8b2d99
│                       │      │                   fb36a19fe87 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ redhat: 2 
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
│                       │      ├ Fingerprint     : sha256:8f17eee557592e6f95a6f356f92d18d3ab64420e9b5aa6eadd12a
│                       │      │                   10c555e379f 
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
│                       │      ├ VendorSeverity   ╭ azure : 3 
│                       │      │                  ├ redhat: 2 
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
│                       │      ├ Fingerprint     : sha256:d1412e3c80e1455bf55da016709ada72bfb543e72daab8a64885c
│                       │      │                   ba809091d06 
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
│                       │      ├ Fingerprint     : sha256:12111c26cdb3a8783548962404da9792f68d2ca0ff3cedb346c05
│                       │      │                   db17dfd436f 
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
│                       │      ├ Fingerprint     : sha256:595827c07e3f5015c40702ea2915820263c3262f94cbcf550b302
│                       │      │                   a8a6bb81cbf 
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
│                       │      ├ Fingerprint     : sha256:494ac1bd65afd3273c638255b7c153346f227e5c775282bd9dc91
│                       │      │                   e88e3e3394d 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ redhat: 1 
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
│                       │      ├ Fingerprint     : sha256:25b07374b6a18a468f94a6527612eecc21cd64e27875d648f43e5
│                       │      │                   d5a35e787bb 
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
│                       │      ├ Fingerprint     : sha256:6dd690a6d7512a102220ea85e3d3dcbb9baf673cd7a7920455790
│                       │      │                   3d975348156 
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
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ╰ ubuntu: 1 
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
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-75803              
│                       │      │                                                                               
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
│                       │      ├ Fingerprint     : sha256:6bad27ea0007d5e5064b3d785ee7dcbe57d07e720663027995b42
│                       │      │                   a257eae6240 
│                       │      ├ Title           : A flaw in the libcurl SASL negotiation for LDAP
│                       │      │                   authentication allows  ... 
│                       │      ├ Description     : A flaw in the libcurl SASL negotiation for LDAP
│                       │      │                   authentication allows an
│                       │      │                   incomplete handshake sequence to be misinterpreted as a
│                       │      │                   successful
│                       │      │                   cryptographic verification. An attacker executing a
│                       │      │                   Man-in-the-Middle (MITM)
│                       │      │                   attack can inject a premature or shortcut response that
│                       │      │                   bypasses complete peer
│                       │      │                   validation. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-923
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-13608.html                     
│                       │      │                  https://curl.se/docs/CVE-2026-13608.json                     
│                       │      │                  https://github.com/curl/curl/pull/22213/changes/1a00e2a73675c
│                       │      │                  9521d214aafd6c02b553bfeb022                                  
│                       │      │                  https://hackerone.com/reports/3822248                        
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-13608              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:19.81Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T16:18:00.317Z 
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
│                       │      ├ Fingerprint     : sha256:044ec838c3d2b8b3087249c9206264efa38585b0aac122381f4c5
│                       │      │                   30842ef362c 
│                       │      ├ Title           : A flaw in libcurl's handling of HTTP/2 Server Push streams,
│                       │      │                   when the p ... 
│                       │      ├ Description     : A flaw in libcurl's handling of HTTP/2 Server Push streams,
│                       │      │                   when the parent
│                       │      │                   handle is set to share connections with other handles, can
│                       │      │                   lead to
│                       │      │                   use-after-free in the cleanup process. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-416
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-18924.html                     
│                       │      │                  https://curl.se/docs/CVE-2026-18924.json                     
│                       │      │                  https://github.com/curl/curl/commit/90325ff0444cbdff368bda5d2
│                       │      │                  6d6                                                          
│                       │      │                  https://hackerone.com/reports/3916059                        
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18924              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:20.553Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T16:18:06Z 
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
│                       │      ├ Fingerprint     : sha256:8854d21ae2beb2acb0cea548891d496dcdfde5834b564e2a64c0f
│                       │      │                   20272123cc6 
│                       │      ├ Title           : A flaw in libcurl makes it wrongly reuse an HTTP connection
│                       │      │                   setup for  ... 
│                       │      ├ Description     : A flaw in libcurl makes it wrongly reuse an HTTP connection
│                       │      │                   setup for a given
│                       │      │                   hostname using Negotiate authentication, when the initial
│                       │      │                   request is done
│                       │      │                   using empty credentials. This can make user B's request get
│                       │      │                   sent over user A's
│                       │      │                   previously authenticated connection. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-488
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                 
│                       │      │                  ──────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-19931.html                  
│                       │      │                  https://curl.se/docs/CVE-2026-19931.json                  
│                       │      │                  https://github.com/curl/curl/commit/7103a93b05bc69ea98ed9d
│                       │      │                  https://hackerone.com/reports/3923520                     
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-19931           
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:20.733Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T16:18:07.08Z 
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
│                       │      ├ Fingerprint     : sha256:925f91b24debb22da546394dd718285434f66b26b8883e3cd5264
│                       │      │                   3a3dbaf5db7 
│                       │      ├ Title           : When performing transfers via libcurl\u2019s multi
│                       │      │                   interface, pooled T ... 
│                       │      ├ Description     : When performing transfers via libcurl’s multi interface,
│                       │      │                   pooled TLS
│                       │      │                   connections can outlive their originating easy handles. In
│                       │      │                   OpenSSL 3 provider
│                       │      │                   configurations, libcurl attaches an allocated library
│                       │      │                   context to the easy
│                       │      │                   handle's state and passes it to OpenSSL without acquiring an
│                       │      │                    ownership
│                       │      │                   reference; destroying the easy handle prematurely frees this
│                       │      │                    context while the
│                       │      │                   active connection retains a dangling pointer, leading to a
│                       │      │                   heap-use-after-free
│                       │      │                   upon subsequent I/O or post-handshake operations. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-416
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                 
│                       │      │                  ──────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80229.html                  
│                       │      │                  https://curl.se/docs/CVE-2026-80229.json                  
│                       │      │                  https://github.com/curl/curl/commit/7ea37abc6ac0120ba5f6d9
│                       │      │                  https://hackerone.com/reports/3969255                     
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-80229           
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.217Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T16:18:15.72Z 
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
│                       │      ├ Fingerprint     : sha256:8419177f77c161d6fff4d5ee170d2e86423556c133db725df3cc5
│                       │      │                   4b73465eb40 
│                       │      ├ Title           : When `CURLOPT_PINNEDPUBLICKEY` is configured alongside
│                       │      │                   options that di ... 
│                       │      ├ Description     : When `CURLOPT_PINNEDPUBLICKEY` is configured alongside
│                       │      │                   options that disable
│                       │      │                   standard peer verification (`CURLOPT_SSL_VERIFYPEER = 0`
│                       │      │                   and
│                       │      │                   `CURLOPT_SSL_VERIFYHOST = 0`), libcurl fails to enforce
│                       │      │                   public key pinning on
│                       │      │                   connections established without a presented server
│                       │      │                   certificate. Bypassing the
│                       │      │                   pinning check under these disabled-verification conditions
│                       │      │                   allows
│                       │      │                   unauthenticated connections to succeed when they should be
│                       │      │                   rejected. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-295
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                
│                       │      │                  ─────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80230.html                 
│                       │      │                  https://curl.se/docs/CVE-2026-80230.json                 
│                       │      │                  https://github.com/curl/curl/commit/5267ed859d545534d0c21
│                       │      │                  https://hackerone.com/reports/3969300                    
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-80230          
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.327Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T19:19:54.063Z 
│                       ├ [26] ╭ VulnerabilityID : CVE-2026-80255 
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
│                       │      ├ Fingerprint     : sha256:a54c27a28cac9edec7be8d16d784d1519108bd65ec196862d803a
│                       │      │                   f3a2c560ef6 
│                       │      ├ Title           : A `Set-Cookie:` header using tab (horizontal tab, ASCII code
│                       │      │                    9) instea ... 
│                       │      ├ Description     : A `Set-Cookie:` header using tab (horizontal tab, ASCII code
│                       │      │                    9) instead of
│                       │      │                   space (ascii code 32) immediately before the `Secure`
│                       │      │                   attribute causes curl to
│                       │      │                   store the cookie without its Secure flag. The cookie might
│                       │      │                   then wrongfully be
│                       │      │                   sent over plaintext HTTP on subsequent requests to the same
│                       │      │                   host. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-201
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                 
│                       │      │                  ──────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80255.html                  
│                       │      │                  https://curl.se/docs/CVE-2026-80255.json                  
│                       │      │                  https://github.com/curl/curl/commit/4f6aa41a0145e930e76677
│                       │      │                  https://hackerone.com/reports/3972395                     
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-80255           
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.623Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T19:19:54.52Z 
│                       ├ [27] ╭ VulnerabilityID : CVE-2026-82209 
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
│                       │      ├ Fingerprint     : sha256:329e7c99bfcb2192736bbf20ce33009d4fbc4df4c50b11fe4928c
│                       │      │                   a5c7ee4c8b2 
│                       │      ├ Title           : When libpsl support is enabled, libcurl fails to enforce the
│                       │      │                    Public Su ... 
│                       │      ├ Description     : When libpsl support is enabled, libcurl fails to enforce the
│                       │      │                    Public Suffix
│                       │      │                   List boundary check when processing a `Set-Cookie` header
│                       │      │                   where the `Domain`
│                       │      │                   attribute explicitly matches an origin host that is itself a
│                       │      │                    public suffix
│                       │      │                   (e.g., `Domain=co.uk` set by `co.uk`).
│                       │      │                   
│                       │      │                   Instead of coercing it into a strict host-only cookie,
│                       │      │                   libcurl saves the
│                       │      │                   cookie with wildcard domain scope (`.co.uk`). Consequently,
│                       │      │                   the cookie is
│                       │      │                   inappropriately included in subsequent outbound requests or
│                       │      │                   HTTP redirects to
│                       │      │                   arbitrary sibling subdomains under the same public suffix
│                       │      │                   (e.g.,
│                       │      │                   `attacker.co.uk`). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-201
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                      
│                       │      │                  ───────────────────────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-82209.html                       
│                       │      │                  https://curl.se/docs/CVE-2026-82209.json                       
│                       │      │                  https://github.com/curl/curl/commit/95c1e8915dce64606bd753fd47f
│                       │      │                  https://hackerone.com/reports/3972385                          
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-82209                
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.847Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T19:20:00.313Z 
│                       ├ [28] ╭ VulnerabilityID : CVE-2026-80231 
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
│                       │      ├ Fingerprint     : sha256:6cfe69137d59bd54fb1c7b31d6090c7951cab29c2e4ad3b2a3893
│                       │      │                   649e30f145c 
│                       │      ├ Title           : A flaw in libcurl makes it wrongly reuse an existing HTTPS
│                       │      │                   connec ... 
│                       │      ├ Description     : A flaw in libcurl makes it wrongly reuse an existing HTTPS
│                       │      │                   connection setup
│                       │      │                   for a given hostname even when using a different Native CA
│                       │      │                   Store setting
│                       │      │                   (`CURLSSLOPT_NATIVE_CA`) than when the connection was
│                       │      │                   created. 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-488
│                       │      │                  
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80231.html
│                       │      │                  https://curl.se/docs/CVE-2026-80231.json
│                       │      │                  https://hackerone.com/reports/3969368   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.5Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T19:19:54.307Z 
│                       ├ [29] ╭ VulnerabilityID : CVE-2026-80256 
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
│                       │      ├ Fingerprint     : sha256:c2fe4fed2ef6544e09cdbe7d695a971c56943c7931226d54424e1
│                       │      │                   f972bb5075d 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [30] ╭ VulnerabilityID : CVE-2026-82208 
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
│                       │      ├ Fingerprint     : sha256:7dd29c1bb8b6a10d4accd1d3517794675c021c3dc325e27d2f9f9
│                       │      │                   cf3107a43d4 
│                       │      ├ Title           : With the wolfSSL backend, when CA caching is enabled and an
│                       │      │                   `CURLOPT_S ... 
│                       │      ├ Description     : With the wolfSSL backend, when CA caching is enabled and an
│                       │      │                   `CURLOPT_SSL_CTX_FUNCTION` callback replaces the trust
│                       │      │                   store, libcurl can
│                       │      │                   silently reinstall the cached store after the callback
│                       │      │                   returns. A certificate
│                       │      │                   trusted by the cached store but rejected by the
│                       │      │                   callback-selected store is
│                       │      │                   then incorrectly accepted. 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-295
│                       │      │                  
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-82208.html
│                       │      │                  https://curl.se/docs/CVE-2026-82208.json
│                       │      │                  https://hackerone.com/reports/3973090   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.733Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T19:20:00.13Z 
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
│                       │      ├ Fingerprint     : sha256:5e7b9aa7edfe7003a1df3da0b8d551404bbb9942ec8c668499101
│                       │      │                   4c8542caf29 
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
│                       │      ├ Fingerprint     : sha256:0a3b07a66bbd35cfce9d0a3fac1131ef9b9aa123af970bf9af5e7
│                       │      │                   ae96ca0149e 
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
│                       │      ├ Fingerprint     : sha256:97839452e673ef1f0bff580f35843d0165c8e8dfe2a87f486f9c1
│                       │      │                   ac424bcbd6d 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ redhat: 2 
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
│                       │      ├ Fingerprint     : sha256:864892fcf3f943cb6322bbb4165da48b2a9a304826a4706c15853
│                       │      │                   7a1faa9af36 
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
│                       │      ├ VendorSeverity   ╭ azure : 3 
│                       │      │                  ├ redhat: 2 
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
│                       │      ├ Fingerprint     : sha256:dba437a668bce246202598088577921fe98cfafc280c8d8a1b08a
│                       │      │                   d98ac64e788 
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
│                       │      ├ Fingerprint     : sha256:db3508d76fb62123758f8ace7bf7d1e08aef9b7be922680aa5415
│                       │      │                   0453dd5ec4a 
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
│                       │      ├ Fingerprint     : sha256:caecbc4efbcd47862d93778673c91e53b0a7a1c19902c2917077f
│                       │      │                   d8b7808d3e4 
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
│                       │      ├ Fingerprint     : sha256:abc06bb07f5f3552559fa22069d8f855368e080816b1c132e9bd2
│                       │      │                   5e017f6e011 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ redhat: 1 
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
│                       │      ├ Fingerprint     : sha256:3fedf34bd13382d936db5da440af81f4d66b9ff0ee7581d09a9d0
│                       │      │                   762bdf26c5f 
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
│                       │      ├ Fingerprint     : sha256:3be6537346efc4d97ed88deaf2ee1da89d8943f614ba4314b2a8d
│                       │      │                   1c39c8cb121 
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
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ╰ ubuntu: 1 
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
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-75803              
│                       │      │                                                                               
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
│                       │      ├ Fingerprint     : sha256:ba64e3c269a531912a3494ce62f5461507cccc4f0ab3cc5a69260
│                       │      │                   7a738df66e0 
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
│                       │      ├ Fingerprint     : sha256:485cb061f657e007439d91ffd1c06fb8543b54b1d3d2dfe8e3469
│                       │      │                   09d3458a0bb 
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
│                       │      ├ Fingerprint     : sha256:8fab8b0096df2670d2c0f6196ad248f545a8bc92f1ae0244ba344
│                       │      │                   d48cbd35102 
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
│                       │      ├ Fingerprint     : sha256:089d5b704618be14eacc0d8904163f59dd3e9257f24334f7cf8d7
│                       │      │                   b08e4e82909 
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
│                       │      ├ Fingerprint     : sha256:1b6f7403166e4bc79e239152ac045463c3e883d45de6c67734648
│                       │      │                   e25b21ccf24 
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
│                       │      ├ Fingerprint     : sha256:96b8c0dd656c0dc7fb1e145c637b6b6dd2930f4d4308ab64431cd
│                       │      │                   af05116e18e 
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
│                       │      ├ Fingerprint     : sha256:c9eed8beca774ef6533455f6f7c7596d941f69ceaa1197d34f6a4
│                       │      │                   d27f4e01788 
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
│                       │      ├ Fingerprint     : sha256:1f15d8ded05ecb747f9ee55c17cdb993e170a9ad9762230820af5
│                       │      │                   c911829d06a 
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
│                       │      ├ Fingerprint     : sha256:498bdca9974ae43bdda854d56e8ca7baf3fb1dc50b13ba8d186d0
│                       │      │                   e399b125266 
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
│                       │      ├ Fingerprint     : sha256:7cdcab460f8c6e19c2c7c4841cc4a473d84514bf20aa53b633527
│                       │      │                   095ba6ef45f 
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
│                       │      ├ Fingerprint     : sha256:58a8c7de4ec7a942f6af6fdbd9800f98d58e4769154e78af8ab32
│                       │      │                   bc866dfa08f 
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
│                       │      ├ Fingerprint     : sha256:d585a12992e0f9ae193eaecbafb7abb629aa54904e01e312fbd6a
│                       │      │                   24b20120df9 
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
│                       │      ├ Fingerprint     : sha256:173be6cb5ba1260775a7b87536e5420ee29c169742b3a7b106db5
│                       │      │                   be2e6881d17 
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
│                       │      ├ Fingerprint     : sha256:d7e29e2dade684286aabc3092a22f7ca6ff93a26fc87372791dc1
│                       │      │                   d114dd45d38 
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
│                       │      ├ Fingerprint     : sha256:460fd5a1992abb7c93bbc917e85553cdf5f92e43df044a04e8f3c
│                       │      │                   b19548077eb 
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
│                       │      ├ Fingerprint     : sha256:4718a35229722a2f0e28d3954651393db2a4c4923d40ba57060a7
│                       │      │                   dce4dae5e07 
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
│                       │      ├ Fingerprint     : sha256:d59d3b1c9a6f15d25cf3832b6dcfd39a5122c19743cf46d314656
│                       │      │                   c4da0613aa8 
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
│                       │      ├ Fingerprint     : sha256:9743ee8cb4c20ad1c928ec64ae15b33ec81fe094004079c58b605
│                       │      │                   e63d59a31b2 
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
│                       │      ├ Fingerprint     : sha256:3d82749d42e1c951ebaa6bd3a8e16dfe4ce746122670c21a8f16a
│                       │      │                   87efd131016 
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
│                       │      ├ Fingerprint     : sha256:76fd351ff07295b47a0266a58dbfa2a908a4ea7485eaed9eeeca1
│                       │      │                   47c03f8075e 
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
│                       │      ├ Fingerprint     : sha256:0a5913e2ceb57f618b397d6e167687a085b80d79fdc6189df7077
│                       │      │                   03533e6de34 
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
│                       │      ├ Fingerprint     : sha256:0b7add75c4fe9547c747c25c5198b6dcc7ee35c9e32f9c1d6e426
│                       │      │                   4021629b8af 
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
│                       │      ├ Fingerprint     : sha256:96e5b003222ead69edba04f2de153e0e5dc84c12394b1b3c04e36
│                       │      │                   cdb50f72a96 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ redhat: 2 
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
│                       │      ├ Fingerprint     : sha256:bbc04cfd422d1ca69e735c4780c699c29f3daa340fc70e820880f
│                       │      │                   e836e025abc 
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
│                       │      ├ VendorSeverity   ╭ azure : 3 
│                       │      │                  ├ redhat: 2 
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
│                       │      ├ Fingerprint     : sha256:dbdb756bc2a9d39bd80a0eacdd40dcdb81286e17548fc62d4a76a
│                       │      │                   2b0d5f97e8a 
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
│                       │      ├ Fingerprint     : sha256:61f155a4e75bd4250ba220a90e3c1c729c8c96d9a95211d07f045
│                       │      │                   2f7d1af8ee3 
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
│                       │      ├ Fingerprint     : sha256:153944a4f87a1c3016831558a0e22dd222a05ce80b1e140e29650
│                       │      │                   d95e7da700b 
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
│                       │      ├ Fingerprint     : sha256:3000f1ef8e098e61338a4329b0810fc746b5f6b93932a82d2b4a8
│                       │      │                   e329047234c 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ redhat: 1 
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
│                       │      ├ Fingerprint     : sha256:d218a768b77f15ab6aade7182f91c99d6a8812b65d50d70ca8858
│                       │      │                   cfc5ae0296b 
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
│                              ├ Fingerprint     : sha256:affafeda9804c6543705d997b543b4a098970a685da86daab4ea9
│                              │                   2d982c1a6fc 
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
│                              ├ VendorSeverity   ╭ azure : 1 
│                              │                  ╰ ubuntu: 1 
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
│                              │                  https://nvd.nist.gov/vuln/detail/CVE-2026-75803              
│                              │                                                                               
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
