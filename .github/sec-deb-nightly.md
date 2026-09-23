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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13608 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5f4e66b990dacc99b136bf76f6f1afae10776bf5e2cfdf32faa3a
│                       │      │                   a3c16735095 
│                       │      ├ Title           : curl: curl: Authentication bypass in OpenLDAP SASL
│                       │      │                   negotiation via Man-in-the-Middle (MITM) attack 
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
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-13608        
│                       │      │                  https://curl.se/docs/CVE-2026-13608.html                     
│                       │      │                  https://curl.se/docs/CVE-2026-13608.json                     
│                       │      │                  https://github.com/curl/curl/pull/22213/changes/1a00e2a73675c
│                       │      │                  9521d214aafd6c02b553bfeb022                                  
│                       │      │                  https://hackerone.com/reports/3822248                        
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-13608              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-13608              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:19.81Z 
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:26.353Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-18924 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18924 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:2bf21bccec999bfd27590b6ffe01f176cfd7dd10cff9cc8a5a354
│                       │      │                   2bec1dd1c54 
│                       │      ├ Title           : curl: libcurl: Use-after-free in HTTP/2 Server Push with
│                       │      │                   shared connections 
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
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18924        
│                       │      │                  https://curl.se/docs/CVE-2026-18924.html                     
│                       │      │                  https://curl.se/docs/CVE-2026-18924.json                     
│                       │      │                  https://github.com/curl/curl/commit/90325ff0444cbdff368bda5d2
│                       │      │                  6d6                                                          
│                       │      │                  https://hackerone.com/reports/3916059                        
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18924              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18924              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:20.553Z 
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:27.063Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-19931 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-19931 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:057d0f91cb452d232b835ea3a82c2a2b0868e23e3280409ce98d5
│                       │      │                   3c08ec07213 
│                       │      ├ Title           : curl: libcurl: Information disclosure via incorrect
│                       │      │                   connection reuse with Negotiate authentication 
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
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                                 
│                       │      │                  ──────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-19931     
│                       │      │                  https://curl.se/docs/CVE-2026-19931.html                  
│                       │      │                  https://curl.se/docs/CVE-2026-19931.json                  
│                       │      │                  https://github.com/curl/curl/commit/7103a93b05bc69ea98ed9d
│                       │      │                  https://hackerone.com/reports/3923520                     
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-19931           
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-19931           
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:20.733Z 
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:27.29Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-80229 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80229 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0d3793ddd193e3a2fb61168ae5c6a43dadd7e1dfd03c6bb27f21b
│                       │      │                   d1acfd8d150 
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
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:30.157Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-80230 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80230 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b1acc02b7a6a319ff2a18a6c54777c103ef4ce82bf0213f4d537e
│                       │      │                   244780e6d51 
│                       │      ├ Title           : curl: curl: Public key pinning bypass allows unauthenticated
│                       │      │                    connections 
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
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                
│                       │      │                  ─────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-80230    
│                       │      │                  https://curl.se/docs/CVE-2026-80230.html                 
│                       │      │                  https://curl.se/docs/CVE-2026-80230.json                 
│                       │      │                  https://github.com/curl/curl/commit/5267ed859d545534d0c21
│                       │      │                  https://hackerone.com/reports/3969300                    
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-80230          
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-80230          
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.327Z 
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:30.337Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-80255 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80255 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3f2a6190d217c4911a2257d94e008032a75d872c4e2bfc8ddcf3c
│                       │      │                   283f8b164f4 
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
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:30.77Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-82209 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.5?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : 59f792208966fece 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-82209 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:83019ff2b08177f191c6d92208db551702e6ec43ada5bac1c3933
│                       │      │                   b6797bc00c8 
│                       │      ├ Title           : curl: libcurl: Information disclosure via improper Public
│                       │      │                   Suffix List boundary check 
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
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.1 
│                       │      ├ References                                                                      
│                       │      │                  ───────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-82209          
│                       │      │                  https://curl.se/docs/CVE-2026-82209.html                       
│                       │      │                  https://curl.se/docs/CVE-2026-82209.json                       
│                       │      │                  https://github.com/curl/curl/commit/95c1e8915dce64606bd753fd47f
│                       │      │                  https://hackerone.com/reports/3972385                          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-82209                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-82209                
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.847Z 
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:31.233Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-18374 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2.4?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04 
│                       │      │                  ╰ UID : b964ecf8d3a43faa 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7ca07ef9c574308e6fbd198ed7a59327575ee53202f2cc485daa2
│                       │      │                   473eb153787 
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a52fc30ccc1a7118b974d1939193e340a10f528ce0018cf179615
│                       │      │                   d87abf13862 
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:2b48d59c8a623eaf96174cda2e62d683511c40e469c25640a83f3
│                       │      │                   142a719bd14 
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13608 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6a5201e8d2d98bee8a7a1b7c7c79d5cc1116ca858738d1a6b93cb
│                       │      │                   cbe17143530 
│                       │      ├ Title           : curl: curl: Authentication bypass in OpenLDAP SASL
│                       │      │                   negotiation via Man-in-the-Middle (MITM) attack 
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
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-13608        
│                       │      │                  https://curl.se/docs/CVE-2026-13608.html                     
│                       │      │                  https://curl.se/docs/CVE-2026-13608.json                     
│                       │      │                  https://github.com/curl/curl/pull/22213/changes/1a00e2a73675c
│                       │      │                  9521d214aafd6c02b553bfeb022                                  
│                       │      │                  https://hackerone.com/reports/3822248                        
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-13608              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-13608              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:19.81Z 
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:26.353Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-18924 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18924 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0d1883506d19443e4ab563e0e8164030bc40cab151637bbdaa43a
│                       │      │                   00b4e711d13 
│                       │      ├ Title           : curl: libcurl: Use-after-free in HTTP/2 Server Push with
│                       │      │                   shared connections 
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
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18924        
│                       │      │                  https://curl.se/docs/CVE-2026-18924.html                     
│                       │      │                  https://curl.se/docs/CVE-2026-18924.json                     
│                       │      │                  https://github.com/curl/curl/commit/90325ff0444cbdff368bda5d2
│                       │      │                  6d6                                                          
│                       │      │                  https://hackerone.com/reports/3916059                        
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18924              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18924              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:20.553Z 
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:27.063Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-19931 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-19931 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d7467bc56a4c3c35b0485fb27d5a80ea7e569dc7b5fb8efd1efdf
│                       │      │                   81c8117e60e 
│                       │      ├ Title           : curl: libcurl: Information disclosure via incorrect
│                       │      │                   connection reuse with Negotiate authentication 
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
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                                 
│                       │      │                  ──────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-19931     
│                       │      │                  https://curl.se/docs/CVE-2026-19931.html                  
│                       │      │                  https://curl.se/docs/CVE-2026-19931.json                  
│                       │      │                  https://github.com/curl/curl/commit/7103a93b05bc69ea98ed9d
│                       │      │                  https://hackerone.com/reports/3923520                     
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-19931           
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-19931           
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:20.733Z 
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:27.29Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-80229 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80229 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:730cbf2e2200f5ed182a3ee4013427ff75181d7a05bcfb3833a02
│                       │      │                   faa10ef41d9 
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
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:30.157Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-80230 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80230 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e8aae53000a7aa9522c0d3eb576e15ce66137b76b51b3112cf265
│                       │      │                   1a1e5459df9 
│                       │      ├ Title           : curl: curl: Public key pinning bypass allows unauthenticated
│                       │      │                    connections 
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
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                
│                       │      │                  ─────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-80230    
│                       │      │                  https://curl.se/docs/CVE-2026-80230.html                 
│                       │      │                  https://curl.se/docs/CVE-2026-80230.json                 
│                       │      │                  https://github.com/curl/curl/commit/5267ed859d545534d0c21
│                       │      │                  https://hackerone.com/reports/3969300                    
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-80230          
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-80230          
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.327Z 
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:30.337Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-80255 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-80255 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a241dfdff3a08aff0a5b1a122ddd52fde2df2a34a27c17ae057c0
│                       │      │                   2cfa4142bad 
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
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:30.77Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-82209 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.5 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.5?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8758ff99a6247a97 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-82209 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:be8194b82d35c53aaff62bf259c89e86a0e5151749344140c5e94
│                       │      │                   7b8abf11a09 
│                       │      ├ Title           : curl: libcurl: Information disclosure via improper Public
│                       │      │                   Suffix List boundary check 
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
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.1 
│                       │      ├ References                                                                      
│                       │      │                  ───────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-82209          
│                       │      │                  https://curl.se/docs/CVE-2026-82209.html                       
│                       │      │                  https://curl.se/docs/CVE-2026-82209.json                       
│                       │      │                  https://github.com/curl/curl/commit/95c1e8915dce64606bd753fd47f
│                       │      │                  https://hackerone.com/reports/3972385                          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-82209                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-82209                
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.847Z 
│                       │      ╰ LastModifiedDate: 2026-09-15T07:16:31.233Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2025-66382 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-66382 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:46ce4fb0ff4d425c6a33c70378eb3e8d6821b1dfef0b4ec48e193
│                       │      │                   a6731bea7d1 
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
│                       │      ├ FixedVersion    : 2.7.4-1ubuntu0.1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-32776 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:547471bd1b4e9c5e7c82d7c594dd3b3c01dc7df530a83b4713800
│                       │      │                   e3b27dd455a 
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8790-1               
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
│                       │      ├ FixedVersion    : 2.7.4-1ubuntu0.1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-32777 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c823de7db1c265e9a316681fdb1a229f7a21ccd29ef807737daa3
│                       │      │                   63427536e3b 
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8790-1               
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
│                       │      ├ FixedVersion    : 2.7.4-1ubuntu0.1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-32778 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3e57e6444b66c566264fb534dc939be4b22c02979c20d76a54eca
│                       │      │                   26e8c45c0e8 
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8790-1               
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
│                       │      ├ FixedVersion    : 2.7.4-1ubuntu0.1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-41080 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:676ac805465593afef1dcf52eed3b091f20e9a78a86bf3be533d4
│                       │      │                   963f77c508e 
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8790-1               
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
│                       │      ├ FixedVersion    : 2.7.4-1ubuntu0.1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-45186 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c8c6714a4e11ad4f05f8ec855697a84e63aa193c96e928a300412
│                       │      │                   bbdc940a5a1 
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8790-1               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-45186              
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-05-10T07:16:07.883Z 
│                       │      ╰ LastModifiedDate: 2026-09-16T13:17:58.967Z 
│                       ├ [23] ╭ VulnerabilityID : CVE-2026-50219 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ FixedVersion    : 2.7.4-1ubuntu0.1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-50219 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a466ac9383cd2c89d4485e1b87102f7d95e7ad5014c16e1b91b9b
│                       │      │                   dc7bc4da84f 
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8790-1               
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56131 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:eacb172cda6e630d11399300c264329ed47c73b5240ac66f27fe8
│                       │      │                   40783aa56ad 
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56132 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:9bfdb9f7c8ad62e54276bee89bd84cdcd2e0144fbf482f30485bf
│                       │      │                   1865218a42d 
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
│                       │      ├ FixedVersion    : 2.7.4-1ubuntu0.1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56403 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:2696ee7a85959ffea1e470f71d617f455f146da6898e2367be71e
│                       │      │                   23899c0816a 
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8790-1       
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
│                       │      ├ FixedVersion    : 2.7.4-1ubuntu0.1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56404 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a281fb8795cd0e2d5947b4ef47bf32376fd1ee7198714cc5e23a7
│                       │      │                   c9b9e53b8d4 
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8790-1       
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
│                       │      ├ FixedVersion    : 2.7.4-1ubuntu0.1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56405 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:439a72cc091ac95c903a45531f2f8644dd12f6a58da5b711a43da
│                       │      │                   5c76a6e4f98 
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8790-1       
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56406 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c5cc5956bba43af31c2f3a832ed746dfdffe863c8598f12e3a11b
│                       │      │                   c79023f1429 
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56407 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:226903f5490c5fcece8b76927c2536579032c0dd90ca57fea2b8b
│                       │      │                   46eef4f453d 
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
│                       │      ├ FixedVersion    : 2.7.4-1ubuntu0.1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56408 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:89e5aebc4ed7f4ed7d2027901574febfa083d750146583c27a408
│                       │      │                   8abbaff30ed 
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8790-1               
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56409 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:89618a6ff96f901b626d23f64132bb2e33ba048ab0ae2bec7ff9d
│                       │      │                   460e0913609 
│                       │      ├ Title           : xmlwf in libexpat before 2.8.2 has an integer overflow for
│                       │      │                   the output  ... 
│                       │      ├ Description     : xmlwf in libexpat before 2.8.2 has an integer overflow for
│                       │      │                   the output filename when -d outputDir is used. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ azure : 2 
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56410 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:90b053ea9228a0a690d2900adae1bc198f8c855b79ebb421507bc
│                       │      │                   2cfe44710fa 
│                       │      ├ Title           : libexpat: libexpat: Integer overflow in xmlwf can lead to
│                       │      │                   information disclosure and arbitrary code execution. 
│                       │      ├ Description     : xmlwf in libexpat before 2.8.2 has an integer overflow in
│                       │      │                   resolveSystemId. 
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56411 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0cb3e2bf8295abbafa0451665a4634c5217ce4bbdd3a845265498
│                       │      │                   139cdfaf1dc 
│                       │      ├ Title           : expat: libexpat: Integer Overflow Vulnerability Leading to
│                       │      │                   Information Disclosure or Code Execution 
│                       │      ├ Description     : xmlwf in libexpat before 2.8.2 has an integer overflow in
│                       │      │                   endDoctypeDecl via NOTATION declarations. 
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
│                       │      ├ FixedVersion    : 2.7.4-1ubuntu0.1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56412 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e13f3c8abc0dd43b0a0be8cc036189e2af76a7886e82fb73effb2
│                       │      │                   896bfb04822 
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
│                       │      │                  https://ubuntu.com/security/notices/USN-8790-1       
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-66046 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f1d3f894f5fb1277ceb6207747fceba17afcd1a9f1c856896e057
│                       │      │                   d284d6ab074 
│                       │      ├ Title           : expat: Expat: Denial of Service via quadratic complexity in
│                       │      │                   attribute processing 
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
│                       │      │                  ├ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-66046        
│                       │      │                  https://github.com/libexpat/libexpat/pull/1321               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-66046              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-66046              
│                       │      │                  https://www.vulncheck.com/advisories/expat-denial-of-service-
│                       │      │                  via-storeatts-quadratic-complexity                           
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-18T15:16:57Z 
│                       │      ╰ LastModifiedDate: 2026-09-18T15:07:24.37Z 
│                       ├ [37] ╭ VulnerabilityID : CVE-2026-72522 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-72522 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:92bb0091dae8ea276e949cc2db7c2b32c67036ca250cc3677adf9
│                       │      │                   ab4a677c07e 
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-76641 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:960608ea2b6bad69bf19770b4f4a876096e09f338195cd62d71c9
│                       │      │                   e37d2ca1077 
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-76957 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7bae683097a514b209039d965f32b64d7da2378dd91dbb7b0fa75
│                       │      │                   57c1cd3c73e 
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
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13757 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:818d4edf06b81f48305bb0da67ca37c7b8d1aa22562342794b810
│                       │      │                   77d61707723 
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
│                       ├ [41] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libsystemd0@259.5-0ubuntu3.4 
│                       │      ├ PkgName         : libsystemd0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsystemd0@259.5-0ubuntu3.4?arch=amd6
│                       │      │                  │       4&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8e41c7d584057e32 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:4d82e19a5228362b07b02a2d899092af7dcef2d30dcec68ca7dc9
│                       │      │                   354453157c0 
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
│                       ├ [42] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libudev1@259.5-0ubuntu3.4 
│                       │      ├ PkgName         : libudev1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libudev1@259.5-0ubuntu3.4?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : db6ded6155f534fe 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f5438f5cff4afac65c073a18beea4eb14307c04524a7f80c7b38d
│                       │      │                   4bd0b60500f 
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
│                       ├ [43] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : login.defs@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : login.defs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login.defs@4.17.4-2ubuntu3?arch=all&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : eaf648d5e4e975f7 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:04a57cf87cf2e8fb81a4a935f647f12b2d40f9fa7209ffba63998
│                       │      │                   b9842a195f8 
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
│                       ├ [44] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : passwd@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : passwd 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/passwd@4.17.4-2ubuntu3?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : 12ffbe3e135ac553 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:aab01f7af1089ed01a798c8e0ec960d80c05c7cc2c90c4870774d
│                       │      │                   268f41f7303 
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
│                       ├ [45] ╭ VulnerabilityID : CVE-2026-35341 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35341 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a5f86e5039812d249fccb0a13e8cd14f874a8809bd35ebb1cf650
│                       │      │                   dbcbb5a8d11 
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
│                       ├ [46] ╭ VulnerabilityID : CVE-2026-35344 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35344 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:397a87f8972b468773a67378d4d5b6cfe445dea4e96eb0ed3532d
│                       │      │                   1568b230cf7 
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
│                       ├ [47] ╭ VulnerabilityID : CVE-2026-35345 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35345 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:09bac011c152a634cf23fe054fa059e520d01d525ee9fb0bb0020
│                       │      │                   b3c9d2da820 
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
│                       ├ [48] ╭ VulnerabilityID : CVE-2026-35348 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35348 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c75b83799b745a554280eda81c25c3e26c6472c7649910475af63
│                       │      │                   c80385f7bbf 
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
│                       ├ [49] ╭ VulnerabilityID : CVE-2026-35350 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35350 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6b52cdacaf50ac120eff00b8bab55a8db457e2951bfaddcf9a959
│                       │      │                   03678de4977 
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
│                       ├ [50] ╭ VulnerabilityID : CVE-2026-35351 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35351 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:4da702d3e6b6d94d2544faf54e71c9453e98a65ce034072fc01ea
│                       │      │                   c9851c6af93 
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
│                       ├ [51] ╭ VulnerabilityID : CVE-2026-35352 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35352 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:94a54340b6c1c4697352b4f3532bb9c700124f815335afa5436fd
│                       │      │                   9bdcffb2bce 
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
│                       ├ [52] ╭ VulnerabilityID : CVE-2026-35354 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35354 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:810acccae0070f0ee1837615f9d403d2c104abe656b7be0d5f8b5
│                       │      │                   3b2d57d5e35 
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
│                       ├ [53] ╭ VulnerabilityID : CVE-2026-35357 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35357 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:314cf92cec3e6554b63812647b874ed0e1b329c0beac6e5e97753
│                       │      │                   d859f4e34cb 
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
│                       ├ [54] ╭ VulnerabilityID : CVE-2026-35359 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35359 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b1583b528cd40aaf579e0e0d26879fc9a906f5f32085cf99d44f6
│                       │      │                   30f08762987 
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
│                       ├ [55] ╭ VulnerabilityID : CVE-2026-35360 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35360 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f810fc1d98bea0f67c06d86c8ee85187ffe174a7f32ff3759cd88
│                       │      │                   d11a02f21ee 
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
│                       ├ [56] ╭ VulnerabilityID : CVE-2026-35363 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35363 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:fb8556fa9e8d807bfc6c50f5d94c6de9a7aba13e6fcaae2a27207
│                       │      │                   0bd47824338 
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
│                       ├ [57] ╭ VulnerabilityID : CVE-2026-35364 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35364 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:8096b4cdd2dc05e4e4fc15a4238866518cd49d2b37896ba978af9
│                       │      │                   4fb2abf5842 
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
│                       ├ [58] ╭ VulnerabilityID : CVE-2026-35367 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35367 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:245a0e9f0f884545695b2c5ea135ea19de05710691222c1194c69
│                       │      │                   a1c44adfe8d 
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
│                       ├ [59] ╭ VulnerabilityID : CVE-2026-35368 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35368 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:249a54496a21b2af952f3982f1124b2ddb8f2acb0c37ab60d2c24
│                       │      │                   6207c07ee0b 
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
│                       ├ [60] ╭ VulnerabilityID : CVE-2026-35370 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35370 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ece451ad0a865443aec1c68d5b69bd4017bed485ebe69da039f7d
│                       │      │                   b3aa3d2cffd 
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
│                       ├ [61] ╭ VulnerabilityID : CVE-2026-35371 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35371 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:68a4208121c8e0ec33c4ccbc3bbfa1a560a6956ce1ef3c6d786a2
│                       │      │                   2d89816f29d 
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
│                       ├ [62] ╭ VulnerabilityID : CVE-2026-35373 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35373 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:1ab6b777a42006e10f35cabab98140dd784de5e3beff5addf1a2c
│                       │      │                   fc3aa1478c7 
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
│                       ├ [63] ╭ VulnerabilityID : CVE-2026-35374 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:9ebcb8c6c36597de2979de0834b27ab26e37ff69796626481619f
│                       │      │                   3e851e6d660 
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
│                       ├ [64] ╭ VulnerabilityID : CVE-2026-35377 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 2129e05d8c2e5188 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35377 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:cfbe701936ebb3b9177615218cea7e8dca79c35f7a41af095d4c3
│                       │      │                   aecd0896c7b 
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
│                       ├ [65] ╭ VulnerabilityID : CVE-2026-82474 
│                       │      ├ PkgID           : sudo@1.9.17p2-1ubuntu3 
│                       │      ├ PkgName         : sudo 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/sudo@1.9.17p2-1ubuntu3?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : b26025a68a135817 
│                       │      ├ InstalledVersion: 1.9.17p2-1ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-82474 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:4963f584319f5b022b3da1b2ad2ca4bc5510074b0ff6567055247
│                       │      │                   cbd6e91c298 
│                       │      ├ Title           : sudo: Sudo: Policy bypass allows unauthorized program
│                       │      │                   execution via execveat 
│                       │      ├ Description     : Sudo through 1.9.17p2 fails to apply intercept policy checks
│                       │      │                    to the execveat system call in ptrace-based intercept mode.
│                       │      │                    Users permitted to run specific commands can execute denied
│                       │      │                    programs by calling execveat directly or through fexecve,
│                       │      │                   bypassing policy enforcement and logging. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-693
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
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
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:68692             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-82474        
│                       │      │                  https://bugzilla.redhat.com/2525889                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2525889          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-82474
│                       │      │                  https://errata.almalinux.org/10/ALSA-2026-68692.html         
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:68692                
│                       │      │                  https://github.com/sudo-project/sudo                         
│                       │      │                  https://github.com/sudo-project/sudo/blob/v1.9.17p2/src/exec_
│                       │      │                  ptrace.c                                                     
│                       │      │                  https://github.com/sudo-project/sudo/commit/71fbe42dcd5a1c8f7
│                       │      │                  99540583a2dfb2ae6221edf                                      
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-82474.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-69123.html         
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-82474              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-82474              
│                       │      │                                                                               
│                       │      │                  https://www.vulncheck.com/advisories/sudo-through-1.9-17p2-in
│                       │      │                  tercept-policy-bypass-via-execveat                           
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-29T17:17:59.91Z 
│                       │      ╰ LastModifiedDate: 2026-09-10T19:54:25.81Z 
│                       ├ [66] ╭ VulnerabilityID : CVE-2026-18477 
│                       │      ├ PkgID           : tar@1.35+dfsg-4ubuntu0.4 
│                       │      ├ PkgName         : tar 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-4ubuntu0.4?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 5867f93e7d45b368 
│                       │      ├ InstalledVersion: 1.35+dfsg-4ubuntu0.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18477 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ae4b46993dfa2447a195e9d04a9dfa8c4c89a95eadfbb42cb99fd
│                       │      │                   cc99186de2b 
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
│                       ├ [67] ╭ VulnerabilityID : CVE-2026-18508 
│                       │      ├ PkgID           : tar@1.35+dfsg-4ubuntu0.4 
│                       │      ├ PkgName         : tar 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-4ubuntu0.4?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 5867f93e7d45b368 
│                       │      ├ InstalledVersion: 1.35+dfsg-4ubuntu0.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                       │      │                  │         3a347f6e785904615280 
│                       │      │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                       │      │                            313c804c118a5f66093d 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18508 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b51c1b6ea3e6d7d97f4c33ad4eee3607b589b16e3311aa52d00df
│                       │      │                   3e7215a2326 
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
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-61586-0.html       
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18508              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18508              
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-08-03T16:16:28.387Z 
│                       │      ╰ LastModifiedDate: 2026-09-10T18:17:57.193Z 
│                       ╰ [68] ╭ VulnerabilityID : CVE-2026-85091 
│                              ├ PkgID           : zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu3.1 
│                              ├ PkgName         : zlib1g 
│                              ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/zlib1g@1.3.dfsg%2Breally1.3.1-1ubuntu3
│                              │                  │       .1?arch=amd64&distro=ubuntu-26.04&epoch=1 
│                              │                  ╰ UID : a4f0bcc5ee12eaad 
│                              ├ InstalledVersion: 1:1.3.dfsg+really1.3.1-1ubuntu3.1 
│                              ├ Status          : affected 
│                              ├ Layer            ╭ Digest: sha256:bc7b34675bcc95557d18a3de3498a1e67c094fe7ce92
│                              │                  │         3a347f6e785904615280 
│                              │                  ╰ DiffID: sha256:679cfa546b588f483ac89daa568948a38d9d02ed240b
│                              │                            313c804c118a5f66093d 
│                              ├ SeveritySource  : ubuntu 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-85091 
│                              ├ DataSource       ╭ ID  : ubuntu 
│                              │                  ├ Name: Ubuntu CVE Tracker 
│                              │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                              ├ Fingerprint     : sha256:ad6c73e6c87aa4d51c116c3425fa80c5afe29c021cc2bb520cdbf
│                              │                   72b5edfb039 
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
╰ [2] ╭ Target  : usr/bin/pebble 
      ├ Class   : lang-pkgs 
      ├ Type    : gobinary 
      ╰ Packages 
```
