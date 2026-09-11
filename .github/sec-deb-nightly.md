```yaml
╭ [0] ╭ Target         : openaf/oaf:deb-nightly (ubuntu 26.04) 
│     ├ Class          : os-pkgs 
│     ├ Type           : ubuntu 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-13608 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13608 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3f4394d490991a45e596e9d6bb6718f31ac580f076f28ffaf10bf
│                       │      │                   94e853c80e1 
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
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18924 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:34401c554f4a7647ccc56293811e716b3e778f0064a5e7f6fe749
│                       │      │                   67ac0d2110a 
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
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-19931 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:4f774192db757309a4978c1995d56877f2fd668de590e92dd61cf
│                       │      │                   d1e73c0a179 
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
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80229 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:30d20016250b86e457a0205ba9cae1abf1ac070a40844a19fe663
│                       │      │                   5894023a915 
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
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80230 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:700762a8bf3d3d291f30bba6b4491fc5eaacea7999381e6f524fa
│                       │      │                   f27cecb5c70 
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
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80255 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:32b45d5bfb353fa733235aff5161f9545e3ae0fade956b0263a77
│                       │      │                   a6e9c899f4c 
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
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-82209 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d7e81c02faa7f928db6df03fb4881e1724c3aac183506a452d0c7
│                       │      │                   21e9b5fc2e9 
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
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-18374 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2.4?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04 
│                       │      │                  ╰ UID : b964ecf8d3a43faa 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f7447fe0103848be47d79aa1cf8eadc1aedde282a49a15dcbddb9
│                       │      │                   99fe236c274 
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
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-18374 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       .4?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : bbb7a8f7a59474e8 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c3991f79168f70f59b31f90262a93972f7e6e96d35d9fedfe90ee
│                       │      │                   abda9c63e08 
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
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-18374 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2.4?arch=amd64&distr
│                       │      │                  │       o=ubuntu-26.04 
│                       │      │                  ╰ UID : fe574f54c2bc3102 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3c9a051cf4b80bc58e42ced4691bb572942f37d2d1a6de36f5a4f
│                       │      │                   cb9331ddd32 
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
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-13608 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13608 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7d7d5e80e0d3f59b7031b9ef4f55bde9a86693b4807e4a353921a
│                       │      │                   efa8d60d833 
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
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-18924 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18924 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:8f21ed134b0f2a00712b11d1c3f8de98d592b513f73d49eef858b
│                       │      │                   c43fe04f25e 
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
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-19931 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-19931 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a9297e7d23136e7cf78b7f0db0ee738c0673b6c5fb352df201c44
│                       │      │                   b4086e8ca4e 
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
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-80229 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80229 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:2266c803ea548c2f5f93f1449c2d414c960b58b0b4dde9f12e4b0
│                       │      │                   5d1029bf115 
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
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-80230 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80230 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0cf65e75cd77e0186c6048f934055c2bdc1d04f858b8b1d913d33
│                       │      │                   21e52049e72 
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
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-80255 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80255 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:03384a37a7545489c69c090890dbc15eee778964c12e9f7917b57
│                       │      │                   322557e8fd2 
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
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-82209 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-82209 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e77996bc1e13dece1e9d8a9ebdcb471c14fd9b6df455cae308955
│                       │      │                   3c5f34fb9b9 
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
│                       ├ [17] ╭ VulnerabilityID : CVE-2025-66382 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-66382 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:9a7881cf608e04295cd3d0130e4e1e2f8dabe1f14f77b0b41f981
│                       │      │                   54067797987 
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
│                       ├ [18] ╭ VulnerabilityID : CVE-2026-32776 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-32776 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e877cd30c80a754b8632fe36026664f0c5c6abbf3daad92586f66
│                       │      │                   0148b9eefe2 
│                       │      ├ Title           : libexpat: libexpat: Denial of Service due to NULL pointer
│                       │      │                   dereference 
│                       │      ├ Description     : libexpat before 2.7.5 allows a NULL pointer dereference with
│                       │      │                    empty external parameter entity content. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-476
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 2 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-32776        
│                       │      │                  https://cert-portal.siemens.com/productcert/html/ssa-082556.h
│                       │      │                  tml                                                          
│                       │      │                  https://github.com/libexpat/libexpat/pull/1158               
│                       │      │                                                                               
│                       │      │                  https://github.com/libexpat/libexpat/pull/1159               
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-32776              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-32776              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-03-16T14:19:44.6Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:49.53Z 
│                       ├ [19] ╭ VulnerabilityID : CVE-2026-32777 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-32777 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d2997177c7c66ecc2b5623f9c9e53251311ace4c2280d1f83b53a
│                       │      │                   bcc0d99814e 
│                       │      ├ Title           : libexpat: libexpat: Denial of Service via infinite loop in
│                       │      │                   DTD content parsing 
│                       │      ├ Description     : libexpat before 2.7.5 allows an infinite loop while parsing
│                       │      │                   DTD content. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-835
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 2 
│                       │      │                  ├ azure : 1 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-32777        
│                       │      │                  https://cert-portal.siemens.com/productcert/html/ssa-082556.h
│                       │      │                  tml                                                          
│                       │      │                  https://github.com/libexpat/libexpat/issues/1161             
│                       │      │                                                                               
│                       │      │                  https://github.com/libexpat/libexpat/pull/1159               
│                       │      │                                                                               
│                       │      │                  https://github.com/libexpat/libexpat/pull/1162               
│                       │      │                                                                               
│                       │      │                  https://issues.oss-fuzz.com/issues/486993411                 
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-32777              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-32777              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-03-16T14:19:44.78Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:49.687Z 
│                       ├ [20] ╭ VulnerabilityID : CVE-2026-32778 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-32778 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:32e34db57bada36e18b4f9cd04165a870d9e83c0a750e6764c866
│                       │      │                   a0c21e24933 
│                       │      ├ Title           : libexpat: libexpat: Denial of Service via NULL pointer
│                       │      │                   dereference after out-of-memory condition 
│                       │      ├ Description     : libexpat before 2.7.5 allows a NULL pointer dereference in
│                       │      │                   the function setContext on retry after an earlier
│                       │      │                   ouf-of-memory condition. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-476
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 2 
│                       │      │                  ├ azure : 1 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.1 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-32778        
│                       │      │                  https://cert-portal.siemens.com/productcert/html/ssa-082556.h
│                       │      │                  tml                                                          
│                       │      │                  https://github.com/libexpat/libexpat/pull/1159               
│                       │      │                                                                               
│                       │      │                  https://github.com/libexpat/libexpat/pull/1163               
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-32778              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-32778              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-03-16T14:19:44.97Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:49.843Z 
│                       ├ [21] ╭ VulnerabilityID : CVE-2026-41080 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-41080 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5b9a1503bae92fb4718a8d985e23bd092de184fc72cf323ba248e
│                       │      │                   dc0ed03bab5 
│                       │      ├ Title           : libexpat: expat: libexpat: Denial of Service via hash
│                       │      │                   flooding with crafted XML 
│                       │      ├ Description     : libexpat before 2.8.0 uses insufficient entropy, and thus
│                       │      │                   hash flooding can occur via a crafted XML document. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-331
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 1 
│                       │      │                  ├ azure : 1 
│                       │      │                  ├ julia : 1 
│                       │      │                  ├ photon: 3 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 2.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/04/26/1      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-41080        
│                       │      │                  https://blog.hartwork.org/posts/expat-2-8-0-released/        
│                       │      │                  https://cert-portal.siemens.com/productcert/html/ssa-082556.h
│                       │      │                  tml                                                          
│                       │      │                  https://github.com/libexpat/libexpat/issues/47               
│                       │      │                                                                               
│                       │      │                  https://github.com/libexpat/libexpat/pull/1183               
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-41080              
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8520-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-41080              
│                       │      │                                                                               
│                       │      │                  https://www.openwall.com/lists/oss-security/2026/04/26/1     
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-16T17:16:54.917Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:51.257Z 
│                       ├ [22] ╭ VulnerabilityID : CVE-2026-45186 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-45186 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3b8d2ca73c94aafd5ce4fe6e64daa8a397b1693d1a96df8844ebd
│                       │      │                   78ac55faac3 
│                       │      ├ Title           : libexpat: denial of service via crafted XML input 
│                       │      ├ Description     : In libexpat before 2.8.1, the computational complexity of
│                       │      │                   attribute name collision checks allows a denial of service
│                       │      │                   via moderately sized crafted XML input. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-407
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 1 
│                       │      │                  ├ julia      : 3 
│                       │      │                  ├ nvd        : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.5 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/05/11/16     
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:22715             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:22721             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:23230             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:26319             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:27201             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:29197             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:58981             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-45186        
│                       │      │                  https://bugzilla.redhat.com/2468575                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2468575          
│                       │      │                  https://cert-portal.siemens.com/productcert/html/ssa-082556.h
│                       │      │                  tml                                                          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-45186
│                       │      │                                                                               
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-23230.html          
│                       │      │                                                                               
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:23230                
│                       │      │                                                                               
│                       │      │                  https://github.com/libexpat/libexpat/pull/1216               
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-45186.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-23230.html         
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-45186              
│                       │      │                                                                               
│                       │      │                  https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-
│                       │      │                  2026-45186.json                                              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-45186              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-05-10T07:16:07.883Z 
│                       │      ╰ LastModifiedDate: 2026-08-25T13:19:12.733Z 
│                       ├ [23] ╭ VulnerabilityID : CVE-2026-50219 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-50219 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3e512763c4827745420e60acb97acfbe763b32ab07fb68ab79d04
│                       │      │                   73a7e87d9b7 
│                       │      ├ Title           : expat: libexpat: Use-after-free vulnerability due to
│                       │      │                   improper handler call depth tracking 
│                       │      ├ Description     : libexpat before 2.8.2 lacks handler call depth tracking for
│                       │      │                   calls to XML_GetBuffer, XML_Parse, XML_ParseBuffer,
│                       │      │                   XML_ParserFree, or XML_ParserReset from within handlers in
│                       │      │                   cases of a policy violation. Thus, a use-after-free can
│                       │      │                   occur, 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-416
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 1 
│                       │      │                  ├ julia      : 2 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 5.9 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 5.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:64812             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-50219        
│                       │      │                  https://bugzilla.redhat.com/2484620                          
│                       │      │                  https://bugzilla.redhat.com/2490669                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2484620          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2490669          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-50219
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56132
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-64812.html          
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:64812                
│                       │      │                  https://github.com/libexpat/libexpat/pull/1246               
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-50219.html             
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-64812-0.html       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-50219              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-50219              
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-04T06:16:25.05Z 
│                       │      ╰ LastModifiedDate: 2026-07-22T20:10:00.127Z 
│                       ├ [24] ╭ VulnerabilityID : CVE-2026-56131 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56131 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5c35d7ac960944d4dcad747321bb7df50592ffaca11448e0fd27b
│                       │      │                   5e445c2f324 
│                       │      ├ Title           : libexpat: libexpat: Use-after-free vulnerability due to
│                       │      │                   insufficient handler call depth tracking 
│                       │      ├ Description     : libexpat before 2.8.2 lacks handler call depth tracking for
│                       │      │                   calls to XML_ResumeParser from within handlers in cases of a
│                       │      │                    policy violation. Thus, a use-after-free can occur (similar
│                       │      │                    to the CVE-2026-50219 situation). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-416
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 4.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.5 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-56131
│                       │      │                  https://github.com/libexpat/libexpat/pull/1267       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56131      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56131      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-19T06:17:10.107Z 
│                       │      ╰ LastModifiedDate: 2026-06-23T20:15:48.007Z 
│                       ├ [25] ╭ VulnerabilityID : CVE-2026-56132 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56132 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c02293d3de713e550de71f228c9933ac60f5ffa5acd600ca575ba
│                       │      │                   def7e0713e2 
│                       │      ├ Title           : expat: libexpat: Arbitrary Code Execution via Heap-based
│                       │      │                   Buffer Overflow 
│                       │      ├ Description     : In libexpat before 2.8.2, there is a heap-based buffer
│                       │      │                   overflow in doProlog in xmlparse.c because scaffold backing
│                       │      │                   array reallocation is mishandled when there is
│                       │      │                   data-structure sharing across parsers. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-821
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ julia      : 2 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.9 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 6.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:64812             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-56132        
│                       │      │                  https://bugzilla.redhat.com/2484620                          
│                       │      │                  https://bugzilla.redhat.com/2490669                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2484620          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2490669          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-50219
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56132
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-64812.html          
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:64812                
│                       │      │                  https://github.com/libexpat/libexpat/pull/1272               
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-56132.html             
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-64812-0.html       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56132              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56132              
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-19T06:17:10.253Z 
│                       │      ╰ LastModifiedDate: 2026-06-23T20:15:26.23Z 
│                       ├ [26] ╭ VulnerabilityID : CVE-2026-56403 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56403 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:258fcb9a183d349a3b16b4ebf948f4b5380902851fe8888da3e10
│                       │      │                   2768b6e43d9 
│                       │      ├ Title           : libexpat: libexpat: Arbitrary code execution due to integer
│                       │      │                   overflow in storeAtts 
│                       │      ├ Description     : libexpat before 2.8.2 has an integer overflow in storeAtts. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.9 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 6.9 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-56403
│                       │      │                  https://github.com/libexpat/libexpat/pull/1232       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56403      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56403      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-21T16:16:26.59Z 
│                       │      ╰ LastModifiedDate: 2026-06-23T20:15:16.76Z 
│                       ├ [27] ╭ VulnerabilityID : CVE-2026-56404 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56404 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c4b4723e286469d0771c3db4f25cec9269f94e4a41254e193f7ba
│                       │      │                   b7d2a3e736c 
│                       │      ├ Title           : libexpat: libexpat: Arbitrary Code Execution via integer
│                       │      │                   overflow in addBinding 
│                       │      ├ Description     : libexpat before 2.8.2 has an integer overflow in addBinding. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.9 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 6.9 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-56404
│                       │      │                  https://github.com/libexpat/libexpat/pull/1249       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56404      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56404      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-21T16:16:27.62Z 
│                       │      ╰ LastModifiedDate: 2026-06-23T20:15:05.85Z 
│                       ├ [28] ╭ VulnerabilityID : CVE-2026-56405 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56405 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:18fd76973f72c278343ef75717e1d9f7e2e58f8fd98ad05709fed
│                       │      │                   06e9cd920c6 
│                       │      ├ Title           : libexpat: libexpat: Information disclosure and arbitrary
│                       │      │                   code execution via integer overflow 
│                       │      ├ Description     : libexpat before 2.8.2 has an integer overflow in
│                       │      │                   getAttributeId. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.9 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.9 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-56405
│                       │      │                  https://github.com/libexpat/libexpat/pull/1251       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56405      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56405      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-21T16:16:27.74Z 
│                       │      ╰ LastModifiedDate: 2026-06-23T20:14:51.73Z 
│                       ├ [29] ╭ VulnerabilityID : CVE-2026-56406 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56406 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:03ca8acf9804e0f3ac702ade6f591dcfd097a04010147e7dd596e
│                       │      │                   9b2fa4bed61 
│                       │      ├ Title           : libexpat: libexpat: Arbitrary code execution via integer
│                       │      │                   overflow in XML_ParseBuffer 
│                       │      ├ Description     : libexpat before 2.8.2 has an integer overflow in
│                       │      │                   XML_ParseBuffer because it lacked a check that was present
│                       │      │                   in XML_Parse. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 6.9 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-56406
│                       │      │                  https://github.com/libexpat/libexpat/pull/1255       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56406      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56406      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-21T16:16:27.87Z 
│                       │      ╰ LastModifiedDate: 2026-06-23T16:29:06.077Z 
│                       ├ [30] ╭ VulnerabilityID : CVE-2026-56407 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56407 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:fcb9ae17a2a7639765f5a579988596ef95bf90ee893d9cddb292a
│                       │      │                   f2219e70fbc 
│                       │      ├ Title           : libexpat: libexpat: Arbitrary code execution due to integer
│                       │      │                   overflow 
│                       │      ├ Description     : libexpat before 2.8.2 has an integer overflow in doProlog
│                       │      │                   that is related to storeEntityValue and entity textLen. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 6.9 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-56407
│                       │      │                  https://github.com/libexpat/libexpat/pull/1262       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56407      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56407      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-21T16:16:27.987Z 
│                       │      ╰ LastModifiedDate: 2026-06-23T16:28:29.983Z 
│                       ├ [31] ╭ VulnerabilityID : CVE-2026-56408 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56408 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:17d5a72bef830036202a8a5d66a5c552244d8c8a442d50ad30484
│                       │      │                   9f8e0f36243 
│                       │      ├ Title           : libexpat before 2.8.2 has an integer overflow in copyString. 
│                       │      ├ Description     : libexpat before 2.8.2 has an integer overflow in copyString. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ julia ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H/
│                       │      │                          │           A:L 
│                       │      │                          ╰ V3Score : 6.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/libexpat/libexpat/commit/16e2efd867ea8567f
│                       │      │                  fa012210b52ef5918e20817                                      
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56408              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56408              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-21T16:16:28.11Z 
│                       │      ╰ LastModifiedDate: 2026-06-23T16:27:26.523Z 
│                       ├ [32] ╭ VulnerabilityID : CVE-2026-56409 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56409 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:02f2eb06461c623a2d3ac4b8487122fe87bf191ed22c001680f40
│                       │      │                   14cfff345e3 
│                       │      ├ Title           : xmlwf in libexpat before 2.8.2 has an integer overflow for
│                       │      │                   the output  ... 
│                       │      ├ Description     : xmlwf in libexpat before 2.8.2 has an integer overflow for
│                       │      │                   the output filename when -d outputDir is used. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ julia ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/
│                       │      │                          │           A:L 
│                       │      │                          ╰ V3Score : 6.5 
│                       │      ├ References                                                      
│                       │      │                  ───────────────────────────────────────────────
│                       │      │                  https://github.com/libexpat/libexpat/pull/1259 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56409
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56409
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-21T16:16:28.23Z 
│                       │      ╰ LastModifiedDate: 2026-06-23T16:21:55.607Z 
│                       ├ [33] ╭ VulnerabilityID : CVE-2026-56410 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56410 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:88832f45a4f0e4fc5e25bb133af7659234bd2b55ee49468a72ecc
│                       │      │                   d1fa4cb1ed8 
│                       │      ├ Title           : libexpat: libexpat: Integer overflow in xmlwf can lead to
│                       │      │                   information disclosure and arbitrary code execution. 
│                       │      ├ Description     : xmlwf in libexpat before 2.8.2 has an integer overflow in
│                       │      │                   resolveSystemId. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 6.9 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-56410
│                       │      │                  https://github.com/libexpat/libexpat/pull/1252       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56410      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56410      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-21T16:16:28.36Z 
│                       │      ╰ LastModifiedDate: 2026-06-23T16:18:16.427Z 
│                       ├ [34] ╭ VulnerabilityID : CVE-2026-56411 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56411 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:37c01a48f09aa484193e3b1a58407ca73ee52bd6590a7743d5e3d
│                       │      │                   2620b6b4655 
│                       │      ├ Title           : expat: libexpat: Integer Overflow Vulnerability Leading to
│                       │      │                   Information Disclosure or Code Execution 
│                       │      ├ Description     : xmlwf in libexpat before 2.8.2 has an integer overflow in
│                       │      │                   endDoctypeDecl via NOTATION declarations. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 6.9 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-56411
│                       │      │                  https://github.com/libexpat/libexpat/pull/1263       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56411      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56411      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-21T17:16:44.523Z 
│                       │      ╰ LastModifiedDate: 2026-06-23T16:16:36.417Z 
│                       ├ [35] ╭ VulnerabilityID : CVE-2026-56412 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56412 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7d91aa2a3ad83a44e81d2830b41450e29de31ee308165432f9e44
│                       │      │                   050d081e685 
│                       │      ├ Title           : libexpat: libexpat: Use-after-free vulnerability due to
│                       │      │                   improper handling of XML CDATA sections 
│                       │      ├ Description     : libexpat before 2.8.2 does not consider XML_TOK_DATA_CHARS
│                       │      │                   in doCdataSection and thus lacks handler call depth tracking
│                       │      │                    for various calls from within handlers in cases of a policy
│                       │      │                    violation. Thus, a use-after-free can occur. NOTE: this
│                       │      │                   issue exists because of an incomplete fix for
│                       │      │                   CVE-2026-50219. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-416
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 5.9 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 5.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.9 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-56412
│                       │      │                  https://github.com/libexpat/libexpat/pull/1278       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56412      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56412      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-06-21T17:16:44.657Z 
│                       │      ╰ LastModifiedDate: 2026-06-23T15:31:30.853Z 
│                       ├ [36] ╭ VulnerabilityID : CVE-2026-66046 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-66046 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:331ee4dfe80985569469012744a1cb23891f4f6229e4139e87d4f
│                       │      │                   4ac597d68c1 
│                       │      ├ Title           : Expat through 2.8.3 contains a denial of service
│                       │      │                   vulnerability caused  ... 
│                       │      ├ Description     : Expat through 2.8.3 contains a denial of service
│                       │      │                   vulnerability caused by quadratic algorithmic complexity in
│                       │      │                   the storeAtts() function in xmlparse.c, where processing N
│                       │      │                   specified attributes with non-normalized values triggers an
│                       │      │                   O(N^2) linear scan of elementType->defaultAtts to determine
│                       │      │                   CDATA status. A remote unauthenticated attacker can supply a
│                       │      │                    single well-formed XML document of a few megabytes to an
│                       │      │                   application parsing untrusted XML to cause excessive CPU
│                       │      │                   consumption, resulting in denial of service without
│                       │      │                   requiring authentication, external entity resolution, or
│                       │      │                   non-default parser options. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-407
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/libexpat/libexpat/pull/1321               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-66046              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-66046              
│                       │      │                  https://www.vulncheck.com/advisories/expat-denial-of-service-
│                       │      │                  via-storeatts-quadratic-complexity                           
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-18T15:16:57Z 
│                       │      ╰ LastModifiedDate: 2026-08-20T16:17:40.66Z 
│                       ├ [37] ╭ VulnerabilityID : CVE-2026-72522 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-72522 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:91314388c964926e29624f694e0a5e2684da1ff4421842d6e1fc7
│                       │      │                   abe8189f138 
│                       │      ├ Title           : expat: libexpat: Denial of Service due to incorrect Unicode
│                       │      │                   surrogate handling 
│                       │      ├ Description     : libexpat before 2.8.3 has an out-of-bounds read and
│                       │      │                   resultant infinite loop because low surrogates are treated
│                       │      │                   the same as high surrogates during Unicode processing in the
│                       │      │                    *_toUtf16 functions. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.2 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/08/11/5
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-72522  
│                       │      │                  https://bugzilla.mozilla.org/show_bug.cgi?id=2053153   
│                       │      │                  https://github.com/libexpat/libexpat/pull/1296         
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-72522        
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-72522        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-10T04:16:50.91Z 
│                       │      ╰ LastModifiedDate: 2026-08-31T19:33:11.197Z 
│                       ├ [38] ╭ VulnerabilityID : CVE-2026-76641 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-76641 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c00bc66b2342fa67bfa53c15d60b26e488d72f1916d6d580353d1
│                       │      │                   98c06422589 
│                       │      ├ Title           : CVE-2026-76641 affecting package expat for versions less
│                       │      │                   than 2.8.3-2 
│                       │      ├ Description     : Expat through 2.8.3 contains an out-of-bounds read
│                       │      │                   vulnerability that allows attackers to trigger memory
│                       │      │                   corruption by processing XML with external entity parsers
│                       │      │                   created via XML_ExternalEntityParserCreate. A struct size
│                       │      │                   mismatch between ELEMENT_TYPE members causes storeAtts to
│                       │      │                   read the attIndex member past allocated memory boundaries,
│                       │      │                   resulting in failure to normalize whitespace in non-CDATA
│                       │      │                   attributes or a wild pointer dereference causing a segfault.
│                       │      │                    This vulnerability was introduced by the fix for
│                       │      │                   CVE-2026-66046. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ azure : 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/libexpat/libexpat/commit/98599f6dcc2b46041
│                       │      │                  0881fe420f5f55d6bec63bf                                      
│                       │      │                  https://github.com/libexpat/libexpat/pull/1331               
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-76641              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-76641              
│                       │      │                                                                               
│                       │      │                  https://www.vulncheck.com/advisories/expat-out-of-bounds-read
│                       │      │                  -via-dtdcopy                                                 
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-20T18:16:51.887Z 
│                       │      ╰ LastModifiedDate: 2026-08-20T19:17:04.43Z 
│                       ├ [39] ╭ VulnerabilityID : CVE-2026-76957 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-76957 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:dae52091228630d413cdcdfe24f08af62c55521d803f59ce10e43
│                       │      │                   3fafd4c6933 
│                       │      ├ Title           : libexpat: libexpat: Memory corruption vulnerability allows
│                       │      │                   arbitrary code execution or denial of service 
│                       │      ├ Description     : libexpat before 2.8.4 lacks handler call depth tracking with
│                       │      │                    custom encoding callbacks. Thus, a use-after-free can
│                       │      │                   occur. NOTE: this is similar to CVE-2026-50219,
│                       │      │                   CVE-2026-56131 and CVE-2026-56412. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-416
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ nvd   : 3 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.8 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.9 
│                       │      ├ References                                                            
│                       │      │                  ─────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-76957
│                       │      │                  https://github.com/libexpat/libexpat/pull/1322       
│                       │      │                  https://github.com/libexpat/libexpat/pull/1329       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-76957      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-76957      
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-20T05:16:29.747Z 
│                       │      ╰ LastModifiedDate: 2026-09-08T20:56:31.86Z 
│                       ├ [40] ╭ VulnerabilityID : CVE-2026-13757 
│                       │      ├ PkgID           : libp11-kit0@0.26.2-2 
│                       │      ├ PkgName         : libp11-kit0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libp11-kit0@0.26.2-2?arch=amd64&distro
│                       │      │                  │       =ubuntu-26.04 
│                       │      │                  ╰ UID : 39936f33632ab742 
│                       │      ├ InstalledVersion: 0.26.2-2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13757 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d9ad54e5094fec6b46a32c8d6a05f57e67011b1b8e38b14b72f56
│                       │      │                   b193f006d3b 
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
│                       │      ╰ LastModifiedDate: 2026-09-01T13:18:10.253Z 
│                       ├ [41] ╭ VulnerabilityID : CVE-2026-39113 
│                       │      ├ PkgID           : libsqlite3-0@3.46.1-9ubuntu0.2 
│                       │      ├ PkgName         : libsqlite3-0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsqlite3-0@3.46.1-9ubuntu0.2?arch=am
│                       │      │                  │       d64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 9dfd58c8bc3fed25 
│                       │      ├ InstalledVersion: 3.46.1-9ubuntu0.2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-39113 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:34fe5178cbca40aea996d13fefdf25321c5cfea60e73ab1b58b81
│                       │      │                   bf16d64d25d 
│                       │      ├ Title           : Buffer Overflow vulnerability in SQLite affected version
│                       │      │                   source snapsh ... 
│                       │      ├ Description     : Buffer Overflow vulnerability in SQLite affected version
│                       │      │                   source snapshots/builds containing Fossil check-in
│                       │      │                   8bdc0d485e3ad0c7a1e818da66f106951d496b05cbe61d12c2c448f2f24b
│                       │      │                   6d5d (Git mirror 169f68ed88b34cb68f720191c64c058f2ccec508,
│                       │      │                   2026-03-11) and later snapshots/builds allows an attacker to
│                       │      │                    cause a denial of service via the ext/misc/sqlar.c,
│                       │      │                   sqlarUncompressFunc(), sqlar_uncompress(),
│                       │      │                   sqlite3_value_int64(), sqlite3_malloc(int), uncompress()
│                       │      │                   components 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-122
│                       │      │                  
│                       │      ├ VendorSeverity   ─ ubuntu: 2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://github.com/20000419/CVE-2026-39113                   
│                       │      │                  https://github.com/sqlite/sqlite/blob/169f68ed88b34cb68f72019
│                       │      │                  1c64c058f2ccec508/ext/misc/sqlar.c                           
│                       │      │                  https://github.com/sqlite/sqlite/commit/169f68ed88b34cb68f720
│                       │      │                  191c64c058f2ccec508                                          
│                       │      │                  https://github.com/sqlite/sqlite/commit/169f68ed88b34cb68f720
│                       │      │                  191c64c058f2ccec508%20%28version-3.53.0%29                   
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-39113              
│                       │      │                                                                               
│                       │      │                  https://www.sqlite.org/                                      
│                       │      │                                                                               
│                       │      │                  https://www.sqlite.org/sqlar.html                            
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-25T21:17:00.08Z 
│                       │      ╰ LastModifiedDate: 2026-09-09T16:04:24.933Z 
│                       ├ [42] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libsystemd0@259.5-0ubuntu3.4 
│                       │      ├ PkgName         : libsystemd0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsystemd0@259.5-0ubuntu3.4?arch=amd6
│                       │      │                  │       4&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8e41c7d584057e32 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:69c9e1adf9323795212c6b8ea1e1baf71484a0c7727740146bfb7
│                       │      │                   1f7abc1411f 
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
│                       ├ [43] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libudev1@259.5-0ubuntu3.4 
│                       │      ├ PkgName         : libudev1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libudev1@259.5-0ubuntu3.4?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : db6ded6155f534fe 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ef6ee32b7a5f5c11de96ced409b9cebbfd794aa1c9a4541115b1f
│                       │      │                   15263789bc4 
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
│                       ├ [44] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : login.defs@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : login.defs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login.defs@4.17.4-2ubuntu3?arch=all&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : eaf648d5e4e975f7 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6a13d128bbf59aaf93bfe0a7028de8d8d0b296b8462eeac04614e
│                       │      │                   554f2226d32 
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
│                       ├ [45] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : passwd@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : passwd 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/passwd@4.17.4-2ubuntu3?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : 12ffbe3e135ac553 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:bba4794ac16a1d2d8d1e7ca870bb18a52c80e3f8ddcca95144a9b
│                       │      │                   778af75406f 
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
│                       ├ [46] ╭ VulnerabilityID : CVE-2026-35341 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35341 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5711fbc6c95a44755a6aab56e415733bce1997ed37a2967ceb6b5
│                       │      │                   df4dee3774a 
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
│                       ├ [47] ╭ VulnerabilityID : CVE-2026-35344 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35344 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d28128f86668fd827e2466cd8fe31f448f7d4c1976d09e9e1db96
│                       │      │                   e81c0079f84 
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
│                       ├ [48] ╭ VulnerabilityID : CVE-2026-35345 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35345 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:238ca283f42109ce378f8eeb2efa463d8a0891efd271e098ae3e8
│                       │      │                   0bf46cc220b 
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
│                       ├ [49] ╭ VulnerabilityID : CVE-2026-35348 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35348 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:709f70be9116e72bca35ae375a6dd06c31a1830281ff551a0a5d9
│                       │      │                   63ba5d2bea9 
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
│                       ├ [50] ╭ VulnerabilityID : CVE-2026-35350 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35350 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:017619ae9c049ea8f1ee46fb152c49571ed59c0b8e60320e1ed9f
│                       │      │                   6108f9f9b8a 
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
│                       ├ [51] ╭ VulnerabilityID : CVE-2026-35351 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35351 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:1d1c2a895faec61848b025f7b829476aaf696a9cc98d401767c4c
│                       │      │                   b983c2f1a0a 
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
│                       ├ [52] ╭ VulnerabilityID : CVE-2026-35352 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35352 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f96c498c6b9c8fd6244d1955f1a8ab54a6a1e27783d9324831ab0
│                       │      │                   5d4be5f61dd 
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
│                       ├ [53] ╭ VulnerabilityID : CVE-2026-35354 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35354 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:01457e5008bb41f99862d3df94f85139c7483ef72f5aa15b20a1f
│                       │      │                   b65f7089e51 
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
│                       ├ [54] ╭ VulnerabilityID : CVE-2026-35357 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35357 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:2bed252e2b9a411012c3d5562f14e04c9e93b83cbe6870375132b
│                       │      │                   5b33bed5439 
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
│                       ├ [55] ╭ VulnerabilityID : CVE-2026-35359 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35359 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:558373a012ba9108364e784c4f17629400adbc8bae949582ccc60
│                       │      │                   70f37d0c75d 
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
│                       ├ [56] ╭ VulnerabilityID : CVE-2026-35360 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35360 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:aff50e09587d72c741f2b893080a2ff126f788cc42a93fdb5f970
│                       │      │                   eff6381c5e4 
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
│                       ├ [57] ╭ VulnerabilityID : CVE-2026-35363 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35363 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:77e3f1c773eb16864b45b4e53d3a045c13dca7246605279467d62
│                       │      │                   7ebf1dcca70 
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
│                       ├ [58] ╭ VulnerabilityID : CVE-2026-35364 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35364 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:69ed8864637bc3b4dea8adcce66bbb8b0565fb3adc58b11f4d824
│                       │      │                   c7391afc90d 
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
│                       ├ [59] ╭ VulnerabilityID : CVE-2026-35367 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35367 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:765392216b4f4a285cac3b906e9b364f1f601b82b71342623a4bb
│                       │      │                   1456f5a2606 
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
│                       ├ [60] ╭ VulnerabilityID : CVE-2026-35368 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35368 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:28c1a7d18fdc3b98b2eb4e3f9044773850488638cfea31cf8cfdf
│                       │      │                   7a21328b4fc 
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
│                       ├ [61] ╭ VulnerabilityID : CVE-2026-35370 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35370 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:2aa512d11da03d3ced806759ecbb48b2f0da6ab773b2d15e0a467
│                       │      │                   50a466d0b5b 
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
│                       ├ [62] ╭ VulnerabilityID : CVE-2026-35371 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35371 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5ab8a43f7bb1bbee949855a16f2d031fffb6e3a8609bc175abe75
│                       │      │                   061276ff798 
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
│                       ├ [63] ╭ VulnerabilityID : CVE-2026-35373 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35373 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c85504efa60298ebdc839bdd712b41d2dd5fcd0f21707210c349e
│                       │      │                   17cfe8e9b2d 
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
│                       ├ [64] ╭ VulnerabilityID : CVE-2026-35374 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:2d66db775484f5bacdedff93b537a98f6985aceb596386bd78bec
│                       │      │                   303c4082ea7 
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
│                       ├ [65] ╭ VulnerabilityID : CVE-2026-35377 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35377 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:4819714e7843b1454a25b0059c393164fb706196260084b8a75ae
│                       │      │                   117bba4432e 
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
│                       ├ [66] ╭ VulnerabilityID : CVE-2026-18477 
│                       │      ├ PkgID           : tar@1.35+dfsg-4ubuntu0.4 
│                       │      ├ PkgName         : tar 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-4ubuntu0.4?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 5867f93e7d45b368 
│                       │      ├ InstalledVersion: 1.35+dfsg-4ubuntu0.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                       │      │                  │         bfa8afa121bd16b90f02 
│                       │      │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                       │      │                            891363124f6eecad51be 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18477 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:53e9a9768432cc9cd76dad8e2807475aab0bb624e42b974b4ccf8
│                       │      │                   8dab5490c5d 
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
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-61586-0.html       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18477              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18477              
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-03T17:16:33.897Z 
│                       │      ╰ LastModifiedDate: 2026-09-10T18:17:56.97Z 
│                       ╰ [67] ╭ VulnerabilityID : CVE-2026-18508 
│                              ├ PkgID           : tar@1.35+dfsg-4ubuntu0.4 
│                              ├ PkgName         : tar 
│                              ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-4ubuntu0.4?arch=amd64&
│                              │                  │       distro=ubuntu-26.04 
│                              │                  ╰ UID : 5867f93e7d45b368 
│                              ├ InstalledVersion: 1.35+dfsg-4ubuntu0.4 
│                              ├ Status          : affected 
│                              ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153de
│                              │                  │         bfa8afa121bd16b90f02 
│                              │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc
│                              │                            891363124f6eecad51be 
│                              ├ SeveritySource  : ubuntu 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18508 
│                              ├ DataSource       ╭ ID  : ubuntu 
│                              │                  ├ Name: Ubuntu CVE Tracker 
│                              │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                              ├ Fingerprint     : sha256:27e2c22d390a40c1c695123686a9742c55c597d432a24037192c1
│                              │                   9242a3436c0 
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
│                              ├ VendorSeverity   ╭ alma       : 2 
│                              │                  ├ oracle-oval: 2 
│                              │                  ├ redhat     : 2 
│                              │                  ├ rocky      : 2 
│                              │                  ╰ ubuntu     : 2 
│                              ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L
│                              │                           │           /A:N 
│                              │                           ╰ V3Score : 4.4 
│                              ├ References                                                                    
│                              │                  ─────────────────────────────────────────────────────────────
│                              │                  https://access.redhat.com/errata/RHSA-2026:50807             
│                              │                  https://access.redhat.com/errata/RHSA-2026:61581             
│                              │                  https://access.redhat.com/errata/RHSA-2026:61586             
│                              │                  https://access.redhat.com/errata/RHSA-2026:61783             
│                              │                  https://access.redhat.com/errata/RHSA-2026:66018             
│                              │                  https://access.redhat.com/security/cve/CVE-2026-18508        
│                              │                  https://bugzilla.redhat.com/2455360                          
│                              │                  https://bugzilla.redhat.com/2509735                          
│                              │                  https://bugzilla.redhat.com/2509843                          
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2455360          
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2509735          
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2509843          
│                              │                  https://creativecommons.org/licenses/by/4.0/                 
│                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-18477
│                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-18508
│                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-5704 
│                              │                  https://errata.almalinux.org/9/ALSA-2026-61581.html          
│                              │                  https://errata.rockylinux.org/RLSA-2026:61581                
│                              │                  https://linux.oracle.com/cve/CVE-2026-18508.html             
│                              │                  https://linux.oracle.com/errata/ELSA-2026-61586-0.html       
│                              │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18508              
│                              │                  https://www.cve.org/CVERecord?id=CVE-2026-18508              
│                              │                  
│                              ├ PublishedDate   : 2026-08-03T16:16:28.387Z 
│                              ╰ LastModifiedDate: 2026-09-10T18:17:57.193Z 
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
                        │     ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153deb
                        │     │                  │         fa8afa121bd16b90f02 
                        │     │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc8
                        │     │                            91363124f6eecad51be 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-33818 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:8b49f9d09574a9fa028ce3dce588abc0d8df64c85fac93273bf55f
                        │     │                   0db763c5d5 
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
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65117             
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65886             
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-33818        
                        │     │                  https://bugzilla.redhat.com/2467809                          
                        │     │                  https://bugzilla.redhat.com/2467820                          
                        │     │                  https://bugzilla.redhat.com/2484204                          
                        │     │                  https://bugzilla.redhat.com/2484830                          
                        │     │                  https://bugzilla.redhat.com/2515815                          
                        │     │                  https://bugzilla.redhat.com/2515820                          
                        │     │                  https://bugzilla.redhat.com/2515827                          
                        │     │                  https://bugzilla.redhat.com/2515838                          
                        │     │                  https://bugzilla.redhat.com/2515839                          
                        │     │                  https://bugzilla.redhat.com/2515840                          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456333          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456339          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467809          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467822          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480756          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2484204          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │     │                  https://creativecommons.org/licenses/by/4.0/                 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32280
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32281
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33811
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39820
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39821
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42499
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42504
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │     │                  https://errata.almalinux.org/9/ALSA-2026-65117.html          
                        │     │                  https://errata.rockylinux.org/RLSA-2026:65886                
                        │     │                  https://go.dev/cl/814980                                     
                        │     │                  https://go.dev/issue/80405                                   
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                        │     │                  https://linux.oracle.com/cve/CVE-2026-33818.html             
                        │     │                  https://linux.oracle.com/errata/ELSA-2026-66364-0.html       
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-33818              
                        │     │                  https://pkg.go.dev/vuln/GO-2026-5972                         
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-33818              
                        │     │                  
                        │     ├ PublishedDate   : 2026-08-13T22:17:19.84Z 
                        │     ╰ LastModifiedDate: 2026-09-03T16:37:52.17Z 
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
                        │     ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153deb
                        │     │                  │         fa8afa121bd16b90f02 
                        │     │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc8
                        │     │                            91363124f6eecad51be 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-39821 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:f000ff7de4461bd156a71c7cb37d91bfe962d9f50730208ff8a472
                        │     │                   49befd9757 
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
                        │     │                  https://access.redhat.com/errata/RHSA-2026:62549              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:63134              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65126              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65153              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65359              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65534              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65886              
                        │     │                  https://access.redhat.com/errata/RHSA-2026:66016              
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-39821         
                        │     │                  https://bugzilla.redhat.com/2480756                           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456333           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456339           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467809           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467820           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467822           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480756           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2484204           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839           
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840           
                        │     │                  https://creativecommons.org/licenses/by/4.0/                  
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32280 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32281 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33811 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39820 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39821 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42499 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42504 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862 
                        │     │                  https://errata.almalinux.org/9/ALSA-2026-37435.html           
                        │     │                  https://errata.rockylinux.org/RLSA-2026:65886                 
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
                        │     ╰ LastModifiedDate: 2026-09-10T13:19:50.873Z 
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
                        │     ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153deb
                        │     │                  │         fa8afa121bd16b90f02 
                        │     │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc8
                        │     │                            91363124f6eecad51be 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46600 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:492e348c0e884bd5cc4b426463c9a37168e43737a8b66c52970b60
                        │     │                   194201014a 
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
                        │     ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153deb
                        │     │                  │         fa8afa121bd16b90f02 
                        │     │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc8
                        │     │                            91363124f6eecad51be 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56853 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:17aec7efe4d781aadd7889424e682267b4168879cc319162e90d0d
                        │     │                   138501447f 
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
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65117             
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65886             
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-56853        
                        │     │                  https://bugzilla.redhat.com/2467809                          
                        │     │                  https://bugzilla.redhat.com/2467820                          
                        │     │                  https://bugzilla.redhat.com/2484204                          
                        │     │                  https://bugzilla.redhat.com/2484830                          
                        │     │                  https://bugzilla.redhat.com/2515815                          
                        │     │                  https://bugzilla.redhat.com/2515820                          
                        │     │                  https://bugzilla.redhat.com/2515827                          
                        │     │                  https://bugzilla.redhat.com/2515838                          
                        │     │                  https://bugzilla.redhat.com/2515839                          
                        │     │                  https://bugzilla.redhat.com/2515840                          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456333          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456339          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467809          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467822          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480756          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2484204          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │     │                  https://creativecommons.org/licenses/by/4.0/                 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32280
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32281
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33811
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39820
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39821
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42499
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42504
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │     │                  https://errata.almalinux.org/9/ALSA-2026-65117.html          
                        │     │                  https://errata.rockylinux.org/RLSA-2026:65886                
                        │     │                  https://go.dev/cl/795540                                     
                        │     │                  https://go.dev/issue/80205                                   
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                        │     │                  https://linux.oracle.com/cve/CVE-2026-56853.html             
                        │     │                  https://linux.oracle.com/errata/ELSA-2026-64818-0.html       
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56853              
                        │     │                  https://pkg.go.dev/vuln/GO-2026-6089                         
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-56853              
                        │     │                  
                        │     ├ PublishedDate   : 2026-08-13T22:17:22.093Z 
                        │     ╰ LastModifiedDate: 2026-09-03T16:37:52.17Z 
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
                        │     ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153deb
                        │     │                  │         fa8afa121bd16b90f02 
                        │     │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc8
                        │     │                            91363124f6eecad51be 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56858 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:f1b41e883220eeb4921e97e32002f93e85ad610fb700be3c326d0e
                        │     │                   da053738a9 
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
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65117             
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65886             
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-56858        
                        │     │                  https://bugzilla.redhat.com/2467809                          
                        │     │                  https://bugzilla.redhat.com/2467820                          
                        │     │                  https://bugzilla.redhat.com/2484204                          
                        │     │                  https://bugzilla.redhat.com/2484830                          
                        │     │                  https://bugzilla.redhat.com/2515815                          
                        │     │                  https://bugzilla.redhat.com/2515820                          
                        │     │                  https://bugzilla.redhat.com/2515827                          
                        │     │                  https://bugzilla.redhat.com/2515838                          
                        │     │                  https://bugzilla.redhat.com/2515839                          
                        │     │                  https://bugzilla.redhat.com/2515840                          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456333          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456339          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467809          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467822          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480756          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2484204          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │     │                  https://creativecommons.org/licenses/by/4.0/                 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32280
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32281
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33811
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39820
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39821
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42499
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42504
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │     │                  https://errata.almalinux.org/9/ALSA-2026-65117.html          
                        │     │                  https://errata.rockylinux.org/RLSA-2026:65886                
                        │     │                  https://go.dev/cl/807100                                     
                        │     │                  https://go.dev/issue/80435                                   
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                        │     │                  https://linux.oracle.com/cve/CVE-2026-56858.html             
                        │     │                  https://linux.oracle.com/errata/ELSA-2026-64818-0.html       
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56858              
                        │     │                  https://pkg.go.dev/vuln/GO-2026-6091                         
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-56858              
                        │     │                  
                        │     ├ PublishedDate   : 2026-08-13T22:17:22.207Z 
                        │     ╰ LastModifiedDate: 2026-09-03T16:37:52.17Z 
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
                        │     ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153deb
                        │     │                  │         fa8afa121bd16b90f02 
                        │     │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc8
                        │     │                            91363124f6eecad51be 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56859 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:8e564274b3d0465f6bad55eae58eb1991d16a247248bc66cef3805
                        │     │                   c1e741f298 
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
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65117             
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65886             
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-56859        
                        │     │                  https://bugzilla.redhat.com/2467809                          
                        │     │                  https://bugzilla.redhat.com/2467820                          
                        │     │                  https://bugzilla.redhat.com/2484204                          
                        │     │                  https://bugzilla.redhat.com/2484830                          
                        │     │                  https://bugzilla.redhat.com/2515815                          
                        │     │                  https://bugzilla.redhat.com/2515820                          
                        │     │                  https://bugzilla.redhat.com/2515827                          
                        │     │                  https://bugzilla.redhat.com/2515838                          
                        │     │                  https://bugzilla.redhat.com/2515839                          
                        │     │                  https://bugzilla.redhat.com/2515840                          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456333          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456339          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467809          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467822          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480756          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2484204          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │     │                  https://creativecommons.org/licenses/by/4.0/                 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32280
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32281
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33811
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39820
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39821
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42499
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42504
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │     │                  https://errata.almalinux.org/9/ALSA-2026-65117.html          
                        │     │                  https://errata.rockylinux.org/RLSA-2026:65886                
                        │     │                  https://go.dev/cl/803320                                     
                        │     │                  https://go.dev/issue/80481                                   
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                        │     │                  https://linux.oracle.com/cve/CVE-2026-56859.html             
                        │     │                  https://linux.oracle.com/errata/ELSA-2026-63163-0.html       
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56859              
                        │     │                  https://pkg.go.dev/vuln/GO-2026-6088                         
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-56859              
                        │     │                  
                        │     ├ PublishedDate   : 2026-08-13T22:17:22.32Z 
                        │     ╰ LastModifiedDate: 2026-09-03T16:37:52.17Z 
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
                        │     ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153deb
                        │     │                  │         fa8afa121bd16b90f02 
                        │     │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc8
                        │     │                            91363124f6eecad51be 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56860 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:56ce4dd35767e6daed289c33bef307e505667e3ce61f5a74c84bed
                        │     │                   1140117e72 
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
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65117             
                        │     │                  https://access.redhat.com/errata/RHSA-2026:65886             
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-56860        
                        │     │                  https://bugzilla.redhat.com/2467809                          
                        │     │                  https://bugzilla.redhat.com/2467820                          
                        │     │                  https://bugzilla.redhat.com/2484204                          
                        │     │                  https://bugzilla.redhat.com/2484830                          
                        │     │                  https://bugzilla.redhat.com/2515815                          
                        │     │                  https://bugzilla.redhat.com/2515820                          
                        │     │                  https://bugzilla.redhat.com/2515827                          
                        │     │                  https://bugzilla.redhat.com/2515838                          
                        │     │                  https://bugzilla.redhat.com/2515839                          
                        │     │                  https://bugzilla.redhat.com/2515840                          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456333          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456339          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467809          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467822          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480756          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2484204          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                        │     │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                        │     │                  https://creativecommons.org/licenses/by/4.0/                 
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32280
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32281
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33811
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39820
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39821
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42499
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42504
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                        │     │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                        │     │                  https://errata.almalinux.org/9/ALSA-2026-65117.html          
                        │     │                  https://errata.rockylinux.org/RLSA-2026:65886                
                        │     │                  https://go.dev/cl/803681                                     
                        │     │                  https://go.dev/issue/80494                                   
                        │     │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                        │     │                  https://linux.oracle.com/cve/CVE-2026-56860.html             
                        │     │                  https://linux.oracle.com/errata/ELSA-2026-66364-0.html       
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56860              
                        │     │                  https://pkg.go.dev/vuln/GO-2026-6218                         
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-56860              
                        │     │                  
                        │     ├ PublishedDate   : 2026-08-13T22:17:22.44Z 
                        │     ╰ LastModifiedDate: 2026-09-03T16:37:52.17Z 
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
                              ├ Layer            ╭ Digest: sha256:2e2153d1f29b283ac9891660a980549fa2f2e40153deb
                              │                  │         fa8afa121bd16b90f02 
                              │                  ╰ DiffID: sha256:f34fca92cb8e7cdfb9753b6d48512215271fc412b1bc8
                              │                            91363124f6eecad51be 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56862 
                              ├ DataSource       ╭ ID  : govulndb 
                              │                  ├ Name: The Go Vulnerability Database 
                              │                  ╰ URL : https://pkg.go.dev/vuln/ 
                              ├ Fingerprint     : sha256:ff16e4448f00d6d4a1e81f0f5407176d87e19b3d2a449cb1be2f52
                              │                   ad1afbf3e1 
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
                              │                  https://access.redhat.com/errata/RHSA-2026:65117             
                              │                  https://access.redhat.com/errata/RHSA-2026:65886             
                              │                  https://access.redhat.com/security/cve/CVE-2026-56862        
                              │                  https://bugzilla.redhat.com/2467809                          
                              │                  https://bugzilla.redhat.com/2467820                          
                              │                  https://bugzilla.redhat.com/2484204                          
                              │                  https://bugzilla.redhat.com/2484830                          
                              │                  https://bugzilla.redhat.com/2515815                          
                              │                  https://bugzilla.redhat.com/2515820                          
                              │                  https://bugzilla.redhat.com/2515827                          
                              │                  https://bugzilla.redhat.com/2515838                          
                              │                  https://bugzilla.redhat.com/2515839                          
                              │                  https://bugzilla.redhat.com/2515840                          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456333          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2456339          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467809          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467820          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2467822          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2480756          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2484204          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515815          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515820          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515827          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515838          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515839          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2515840          
                              │                  https://creativecommons.org/licenses/by/4.0/                 
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32280
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-32281
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33811
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-33818
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39820
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-39821
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42499
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42504
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56853
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56858
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56859
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56860
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-56862
                              │                  https://errata.almalinux.org/9/ALSA-2026-65117.html          
                              │                  https://errata.rockylinux.org/RLSA-2026:65886                
                              │                  https://go.dev/cl/804261                                     
                              │                  https://go.dev/issue/80528                                   
                              │                  https://groups.google.com/g/golang-announce/c/94pEornpRlI    
                              │                  https://linux.oracle.com/cve/CVE-2026-56862.html             
                              │                  https://linux.oracle.com/errata/ELSA-2026-66364-0.html       
                              │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56862              
                              │                  https://pkg.go.dev/vuln/GO-2026-6090                         
                              │                  https://www.cve.org/CVERecord?id=CVE-2026-56862              
                              │                  
                              ├ PublishedDate   : 2026-08-13T22:17:22.55Z 
                              ╰ LastModifiedDate: 2026-09-03T16:37:52.17Z 
```
