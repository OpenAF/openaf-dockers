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
│                       │      ├ Fingerprint     : sha256:80c4074fc2032d2181b2677d0f4a53777216cc3a053ba406da408
│                       │      │                   e45c1efe47d 
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
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-13608.html
│                       │      │                  https://curl.se/docs/CVE-2026-13608.json
│                       │      │                  https://hackerone.com/reports/3822248   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:19.81Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:19.81Z 
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
│                       │      ├ Fingerprint     : sha256:d440e7692f18c4961588bfadbd4319898743313d98fc5c7a40aa8
│                       │      │                   8e6ea9438c3 
│                       │      ├ Title           : A flaw in libcurl's handling of HTTP/2 Server Push streams,
│                       │      │                   when the p ... 
│                       │      ├ Description     : A flaw in libcurl's handling of HTTP/2 Server Push streams,
│                       │      │                   when the parent
│                       │      │                   handle is set to share connections with other handles, can
│                       │      │                   lead to
│                       │      │                   use-after-free in the cleanup process. 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-18924.html
│                       │      │                  https://curl.se/docs/CVE-2026-18924.json
│                       │      │                  https://hackerone.com/reports/3916059   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:20.553Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:20.553Z 
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
│                       │      ├ Fingerprint     : sha256:cbf2315562fea9756fbff964f3ceda05fc384ff9c3356247ce48e
│                       │      │                   e81c3aeaa36 
│                       │      ├ Title           : A flaw in libcurl makes it wrongly reuse an HTTP connection
│                       │      │                   setup for  ... 
│                       │      ├ Description     : A flaw in libcurl makes it wrongly reuse an HTTP connection
│                       │      │                   setup for a given
│                       │      │                   hostname using Negotiate authentication, when the initial
│                       │      │                   request is done
│                       │      │                   using empty credentials. This can make user B's request get
│                       │      │                   sent over user A's
│                       │      │                   previously authenticated connection. 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-19931.html
│                       │      │                  https://curl.se/docs/CVE-2026-19931.json
│                       │      │                  https://hackerone.com/reports/3923520   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:20.733Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:20.733Z 
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
│                       │      ├ Fingerprint     : sha256:eeadcb63272487a396f70182399494ff12cf9e1868c2c40bd512c
│                       │      │                   6d53594b504 
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
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80229.html
│                       │      │                  https://curl.se/docs/CVE-2026-80229.json
│                       │      │                  https://hackerone.com/reports/3969255   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.217Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:22.217Z 
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
│                       │      ├ Fingerprint     : sha256:54f445de8cf86bd52cc72a1a4b767c7afc17be712d26597732cfc
│                       │      │                   e1ea7ce679d 
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
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80230.html
│                       │      │                  https://curl.se/docs/CVE-2026-80230.json
│                       │      │                  https://hackerone.com/reports/3969300   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.327Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:22.327Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-80231 
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
│                       │      ├ Fingerprint     : sha256:16d5f96bac1f9b08edc38c6123f3e86e21e899261aebcc7240d8f
│                       │      │                   b9feae2cbed 
│                       │      ├ Title           : A flaw in libcurl makes it wrongly reuse an existing HTTPS
│                       │      │                   connec ... 
│                       │      ├ Description     : A flaw in libcurl makes it wrongly reuse an existing HTTPS
│                       │      │                   connection setup
│                       │      │                   for a given hostname even when using a different Native CA
│                       │      │                   Store setting
│                       │      │                   (`CURLSSLOPT_NATIVE_CA`) than when the connection was
│                       │      │                   created. 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80231.html
│                       │      │                  https://curl.se/docs/CVE-2026-80231.json
│                       │      │                  https://hackerone.com/reports/3969368   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.5Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:22.5Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-80255 
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
│                       │      ├ Fingerprint     : sha256:2957b5e5536def90e5146c6a940580d33a8c480a011d6d5241aaf
│                       │      │                   11f69af3f0c 
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
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80255.html
│                       │      │                  https://curl.se/docs/CVE-2026-80255.json
│                       │      │                  https://hackerone.com/reports/3972395   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.623Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:22.623Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-80256 
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
│                       │      ├ Fingerprint     : sha256:b515619697e44abc0f90e42d3e89ad83439168cf1503b589daa4a
│                       │      │                   790df14694c 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-82208 
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
│                       │      ├ Fingerprint     : sha256:2885cf55ad6af6230acb71fa86fb4694d031390c0dfb681d8d2c3
│                       │      │                   109a8ef9435 
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
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-82208.html
│                       │      │                  https://curl.se/docs/CVE-2026-82208.json
│                       │      │                  https://hackerone.com/reports/3973090   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.733Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:22.733Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-82209 
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
│                       │      ├ Fingerprint     : sha256:d1294cd53f9d51e6e1a2a7f9a00f13041cb4cb12e92058274220d
│                       │      │                   a3c688917fd 
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
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-82209.html
│                       │      │                  https://curl.se/docs/CVE-2026-82209.json
│                       │      │                  https://hackerone.com/reports/3972385   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.847Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:22.847Z 
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
│                       │      ├ Fingerprint     : sha256:c48c659306f9b0f247a3ee7943b8a5e1de7b754579920514256cd
│                       │      │                   282a13dfc54 
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
│                       │      ├ Fingerprint     : sha256:fbf3f0eb30ff869b824c3e1da5c7d5495999bbb633eb541e1d05c
│                       │      │                   594877a02e0 
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
│                       │      ├ Fingerprint     : sha256:8ada58dc38342d3420dcc0b331a9b4c7fdcb5f1353b46955d788c
│                       │      │                   6ab7d30cbc0 
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
│                       │      ├ Fingerprint     : sha256:be6eac817d45b68906aecc687faa12e76ca192dafb4af1703d257
│                       │      │                   250384ec6c4 
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
│                       │      ├ VendorSeverity   ╭ redhat: 2 
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
│                       │      ├ Fingerprint     : sha256:395bab73d37314068ef62cb6b5fc6a2395e8acd40da9bed8fcb8e
│                       │      │                   a8ff510a237 
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
│                       │      ├ VendorSeverity   ╭ redhat: 2 
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
│                       │      ├ Fingerprint     : sha256:a3656c3607517ce4f6e76e58ac7a259efc66327651882241a10df
│                       │      │                   3c64ff43484 
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
│                       │      ├ Fingerprint     : sha256:b69133384424c62f4b702739ec729976a3cad0850b86213e49d98
│                       │      │                   ae7d1b50939 
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
│                       │      ├ Fingerprint     : sha256:98cb8389b682577623213beca34c0a5db7303fe722c5c58214b02
│                       │      │                   bc494237ba6 
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
│                       │      ├ Fingerprint     : sha256:6e573e13bdca888f4433a12e1f3c14c5ff5f716e2bea876267fa3
│                       │      │                   a0d23f64a25 
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
│                       │      ├ VendorSeverity   ╭ redhat: 1 
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
│                       │      ├ Fingerprint     : sha256:cd7f8c8fa10a681b3845bffabd97afb36bfc408cd176bed7bd3d0
│                       │      │                   37d9110686e 
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
│                       │      ├ Fingerprint     : sha256:d798b693a6ca87bb06bf00c3c7dfddd6f6cf056f7232cfe2f715f
│                       │      │                   7b156f59b1f 
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
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
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
│                       │      ├ Fingerprint     : sha256:d14cc09457c1d6fb448007e09a5b41023f65e62351ae9570b4e09
│                       │      │                   7e1cfb92fa8 
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
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-13608.html
│                       │      │                  https://curl.se/docs/CVE-2026-13608.json
│                       │      │                  https://hackerone.com/reports/3822248   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:19.81Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:19.81Z 
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
│                       │      ├ Fingerprint     : sha256:c6ce80186dbc06602291915d82c066dab55fd2ae458e867ed94d0
│                       │      │                   aaf9323510c 
│                       │      ├ Title           : A flaw in libcurl's handling of HTTP/2 Server Push streams,
│                       │      │                   when the p ... 
│                       │      ├ Description     : A flaw in libcurl's handling of HTTP/2 Server Push streams,
│                       │      │                   when the parent
│                       │      │                   handle is set to share connections with other handles, can
│                       │      │                   lead to
│                       │      │                   use-after-free in the cleanup process. 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-18924.html
│                       │      │                  https://curl.se/docs/CVE-2026-18924.json
│                       │      │                  https://hackerone.com/reports/3916059   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:20.553Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:20.553Z 
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
│                       │      ├ Fingerprint     : sha256:e78028c95342933a19d73fe12492317005010edf5d41506a89ad2
│                       │      │                   4e3285ac1e5 
│                       │      ├ Title           : A flaw in libcurl makes it wrongly reuse an HTTP connection
│                       │      │                   setup for  ... 
│                       │      ├ Description     : A flaw in libcurl makes it wrongly reuse an HTTP connection
│                       │      │                   setup for a given
│                       │      │                   hostname using Negotiate authentication, when the initial
│                       │      │                   request is done
│                       │      │                   using empty credentials. This can make user B's request get
│                       │      │                   sent over user A's
│                       │      │                   previously authenticated connection. 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-19931.html
│                       │      │                  https://curl.se/docs/CVE-2026-19931.json
│                       │      │                  https://hackerone.com/reports/3923520   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:20.733Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:20.733Z 
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
│                       │      ├ Fingerprint     : sha256:9b4a27c91038dcc73f258be5ff2b98ef9cd879a713a65f69880bc
│                       │      │                   95196d61c7e 
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
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80229.html
│                       │      │                  https://curl.se/docs/CVE-2026-80229.json
│                       │      │                  https://hackerone.com/reports/3969255   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.217Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:22.217Z 
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
│                       │      ├ Fingerprint     : sha256:61c247fae3187bfa63382b35f0822db25ee89663b9be40e1c0f1d
│                       │      │                   275191abde8 
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
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80230.html
│                       │      │                  https://curl.se/docs/CVE-2026-80230.json
│                       │      │                  https://hackerone.com/reports/3969300   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.327Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:22.327Z 
│                       ├ [26] ╭ VulnerabilityID : CVE-2026-80231 
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
│                       │      ├ Fingerprint     : sha256:7ec97e2284674f6ac2f05870e2fc75fbdb76b9ae27de5cecbb20a
│                       │      │                   02e6025f7c1 
│                       │      ├ Title           : A flaw in libcurl makes it wrongly reuse an existing HTTPS
│                       │      │                   connec ... 
│                       │      ├ Description     : A flaw in libcurl makes it wrongly reuse an existing HTTPS
│                       │      │                   connection setup
│                       │      │                   for a given hostname even when using a different Native CA
│                       │      │                   Store setting
│                       │      │                   (`CURLSSLOPT_NATIVE_CA`) than when the connection was
│                       │      │                   created. 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80231.html
│                       │      │                  https://curl.se/docs/CVE-2026-80231.json
│                       │      │                  https://hackerone.com/reports/3969368   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.5Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:22.5Z 
│                       ├ [27] ╭ VulnerabilityID : CVE-2026-80255 
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
│                       │      ├ Fingerprint     : sha256:436a175421728943bdf434da8a209c0ffbc05099b8ca6a19f98ea
│                       │      │                   4297ea6a030 
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
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-80255.html
│                       │      │                  https://curl.se/docs/CVE-2026-80255.json
│                       │      │                  https://hackerone.com/reports/3972395   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.623Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:22.623Z 
│                       ├ [28] ╭ VulnerabilityID : CVE-2026-80256 
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
│                       │      ├ Fingerprint     : sha256:6b229a5981a08051fe6f506370a0aba07259e898fa1ba69be1581
│                       │      │                   ebf062cb77b 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [29] ╭ VulnerabilityID : CVE-2026-82208 
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
│                       │      ├ Fingerprint     : sha256:3091ae346f2ed5b24d979593f85e2e0220f36439c8ccbcc1be174
│                       │      │                   be691aa1629 
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
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-82208.html
│                       │      │                  https://curl.se/docs/CVE-2026-82208.json
│                       │      │                  https://hackerone.com/reports/3973090   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.733Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:22.733Z 
│                       ├ [30] ╭ VulnerabilityID : CVE-2026-82209 
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
│                       │      ├ Fingerprint     : sha256:6d3a2e002f668fd100925f6d77a2c0a841de017d5a75d1684a81e
│                       │      │                   16873a6285c 
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
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ References                                               
│                       │      │                  ────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-82209.html
│                       │      │                  https://curl.se/docs/CVE-2026-82209.json
│                       │      │                  https://hackerone.com/reports/3972385   
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-09-06T18:17:22.847Z 
│                       │      ╰ LastModifiedDate: 2026-09-06T18:17:22.847Z 
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
│                       │      ├ Fingerprint     : sha256:318d0c181fd853ef2649a4f43879195d9c5ff4efe28aa0bf1d0a1
│                       │      │                   39c058c844f 
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
│                       │      ├ Fingerprint     : sha256:8635bd8c1fab66bd1d9871a4bc0f6c9929207b7dc2cb979e765bb
│                       │      │                   e131208434f 
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
│                       │      ├ Fingerprint     : sha256:0150c3002e256d85c063b82095c38a977e6220bb303571d03c0ac
│                       │      │                   0c4cc9205df 
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
│                       │      ├ VendorSeverity   ╭ redhat: 2 
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
│                       │      ├ Fingerprint     : sha256:115ae0f34c0aab4c95d383e69c26835ad9a375c7530d86ec7c429
│                       │      │                   d64de725df4 
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
│                       │      ├ VendorSeverity   ╭ redhat: 2 
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
│                       │      ├ Fingerprint     : sha256:96f985349471b91b8c158a9f7af48531e0fcb7346e238f7defff2
│                       │      │                   c53f1702ea6 
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
│                       │      ├ Fingerprint     : sha256:0e0439bc93a44ef85bba4d8f45ebb3f6f705aaef01867e8e2a4e9
│                       │      │                   21683e11352 
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
│                       │      ├ Fingerprint     : sha256:7da00fd7e00b6c760449e9dc0818039fdf151437855f43d62c499
│                       │      │                   97d5de9a7ce 
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
│                       │      ├ Fingerprint     : sha256:b8f6ac60fde2fffe41394f27d3835316b8b0fb879267eeff8e7fa
│                       │      │                   14d17b960ba 
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
│                       │      ├ VendorSeverity   ╭ redhat: 1 
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
│                       │      ├ Fingerprint     : sha256:ebe03509acc094f991d1e258a2aeb2f65ed4c2eb4b71004a1182f
│                       │      │                   4cf0259af5d 
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
│                       │      ├ Fingerprint     : sha256:52b9c1ecd2c28e16ea4d9641acf06fab3c83140ec40f0c198f3b3
│                       │      │                   696a64aac78 
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
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
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
│                       │      ├ Fingerprint     : sha256:d639db0f8a293b10e174c67d2007ab6b51e52c3766212acefbeee
│                       │      │                   b7de665b272 
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
│                       │      ├ Fingerprint     : sha256:084f9dbcd48460e53039e536c8191cfd0737d03d34df99fe23137
│                       │      │                   7aacc0a4e4c 
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
│                       │      ├ Fingerprint     : sha256:189fac854c89db186389a018f9969c8e2a0c7654dbcc745583afa
│                       │      │                   9d68e3405da 
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
│                       │      ├ Fingerprint     : sha256:2c305c86ea43527163b1b317f0e98b2bddd62d9dcb203389fac84
│                       │      │                   f445e83a767 
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
│                       │      ├ Fingerprint     : sha256:567aff82100c7f4555af0f8c39c0db4515141fb2b4ed056e037a4
│                       │      │                   57503f8b248 
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
│                       │      ├ Fingerprint     : sha256:4e71c6b34e9f0585d30d7db8738cc2fa9cb4755fbbb8ef2061bb6
│                       │      │                   feba4cff114 
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
│                       │      ├ Fingerprint     : sha256:436b509faa7d86a8e509000a97e8d88812e67d20807d4957a80ff
│                       │      │                   f67a33ca02e 
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
│                       │      ├ Fingerprint     : sha256:3459ba5e014f35aa60b8af9c3cb6a3a630cef41c2e2fc18e396b6
│                       │      │                   b74030340b3 
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
│                       │      ├ Fingerprint     : sha256:d042f3e163ab3f78423178aa3bc140b0fd8ad0da7d0a53a55d466
│                       │      │                   7235fa8ff21 
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
│                       │      ├ Fingerprint     : sha256:2688810057c92760d07dc67be212ca2f8e124b4ca53a93ebe9289
│                       │      │                   bef0a4dbc5f 
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
│                       │      ├ Fingerprint     : sha256:d5fcd2b80b409831cd2ee2d0828edd364995505179b74c6cf3ab2
│                       │      │                   f6d10f92f99 
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
│                       │      ├ Fingerprint     : sha256:d2c65c862208537551ba03515fc75af2080174958de0748c034e9
│                       │      │                   26771473e88 
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
│                       │      ├ Fingerprint     : sha256:72cbe5e21f821d2e39306975a100c08ffda4629dac9e1f54e6001
│                       │      │                   aa4491f9d83 
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
│                       │      ├ Fingerprint     : sha256:62f94d4c93de4616e4b3ee13f0dd59e9528a0a4b197ffa231a485
│                       │      │                   f569b23e6f7 
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
│                       │      ├ Fingerprint     : sha256:2d7d0c9f8e90797e01a1c6589ce34477c0e5330064a000310682d
│                       │      │                   91a35367a31 
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
│                       │      ├ Fingerprint     : sha256:446b69424b552c7ba8b6bc93dc9105e4657f178f40bacc3929330
│                       │      │                   65d6d9b8c73 
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
│                       │      ├ Fingerprint     : sha256:9ee5d95dddb2fe76020bcbfc3cff8a7ff18649c82baebfb6414e5
│                       │      │                   651f483276e 
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
│                       │      ├ Fingerprint     : sha256:07ce4b2e111763a50ae1fdf5343919bf4c12f02a611b66c1fccdf
│                       │      │                   57e31576257 
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
│                       │      ├ Fingerprint     : sha256:913fef5da76f3f69dfaebbf8cd745b6eab3f94bf687b86a2b16e8
│                       │      │                   8cc3df66a1e 
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
│                       │      ├ Fingerprint     : sha256:359ec2767b240445f47f61333ce99b555a5c1d46e54fd33e7c8b3
│                       │      │                   e45b45716aa 
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
│                       │      ├ Fingerprint     : sha256:0900e0f2f586f83709fd05d451826d5ea75c9ad6fcc8c08afc157
│                       │      │                   56c6e5f004a 
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
│                       │      ├ Fingerprint     : sha256:fc6f6fe29c5be904ad940532108eed279b7fc6c6adec589a9eb22
│                       │      │                   296f36c85dd 
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
│                       │      ├ Fingerprint     : sha256:39d03483722e5ccebed2097b33c60181a689fd70689e4a3908cf9
│                       │      │                   14e1f4acfbf 
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
│                       │      ├ VendorSeverity   ╭ redhat: 2 
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
│                       │      ├ Fingerprint     : sha256:6295cbd5ea176b212dd0f26f6bb433c2957b8e7d59c5863864a77
│                       │      │                   f2af211c6d3 
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
│                       │      ├ VendorSeverity   ╭ redhat: 2 
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
│                       │      ├ Fingerprint     : sha256:88d16518609bbfa5bd0260717a4d8fd0f5924525fa01d9e8b0436
│                       │      │                   7e0eca39bc9 
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
│                       │      ├ Fingerprint     : sha256:984698f9e51f417d5d21543e48c02d8b0954b2d9fd92f9b94cdb5
│                       │      │                   ec6796cd111 
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
│                       │      ├ Fingerprint     : sha256:51069b80704f53105871a4130275de84ba04644505628aa22f494
│                       │      │                   448e346c731 
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
│                       │      ├ Fingerprint     : sha256:682531bc316ddd75bb9f4a69f7fba24050d8b8feffcb29458423c
│                       │      │                   d0da52bd238 
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
│                       │      ├ VendorSeverity   ╭ redhat: 1 
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
│                       │      ├ Fingerprint     : sha256:9602013dff8699b2318ecf9a4c78db7c02b951d1448079c4f5288
│                       │      │                   be0ce0fe43d 
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
│                              ├ Fingerprint     : sha256:e17cc672cf4683a4cdbaa459b70c2d63c3e02e0d5bd868c5c65e4
│                              │                   03175f510a0 
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
│                              ├ VendorSeverity   ─ ubuntu: 1 
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
