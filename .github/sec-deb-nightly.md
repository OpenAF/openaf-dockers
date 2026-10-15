```yaml
╭ [0] ╭ Target         : openaf/oaf:deb-nightly (ubuntu 26.04) 
│     ├ Class          : os-pkgs 
│     ├ Type           : ubuntu 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-92392 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92392 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e7b6a346b86043ced339d7d7993e4220b1232c4d6eef2de15c33b
│                       │      │                   593d918d8f0 
│                       │      ├ Title           : During an upload, curl mishandles HTTP/2 `RST_STREAM`
│                       │      │                   received from th ... 
│                       │      ├ Description     : During an upload, curl mishandles HTTP/2 `RST_STREAM`
│                       │      │                   received from the server
│                       │      │                   (with reason `HTTP_1_1_REQUIRED` or `REFUSED_STREAM`)
│                       │      │                   leading to a use after
│                       │      │                   free of a `struct Curl_easy` object. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ ubuntu: 3 
│                       │      ├ References                                                      
│                       │      │                  ───────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-92392.html       
│                       │      │                  https://curl.se/docs/CVE-2026-92392.json       
│                       │      │                  https://hackerone.com/reports/4030333          
│                       │      │                  https://ubuntu.com/security/notices/USN-8927-1 
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-92392
│                       │      ├ PublishedDate   : 2026-10-14T08:17:05.997Z 
│                       │      ╰ LastModifiedDate: 2026-10-15T04:18:29.19Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-107928 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-107928 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:faf13eb1a658f8f89b28682fc57d8c4afbbbe5443ed12a8beb6ee
│                       │      │                   4633d8aeafe 
│                       │      ├ Title           : When curl is built with GnuTLS, a malicious WebSocket server
│                       │      │                    can  
│                       │      ├ Description     : When curl is built with GnuTLS, a malicious WebSocket server
│                       │      │                    can make curl send memory past its send buffer. This is due
│                       │      │                    to an out of bounds read following when
│                       │      │                   `gnutls_record_send()` returns a number of bytes sent
│                       │      │                   greater than the number of bytes it was given to send.
│                       │      │                   GnuTLS does that after a blocked send. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                       
│                       │                         ────────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-107928.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1  
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-107928
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-107929 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-107929 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:4b13f5dcb11948f5e8eeca7e1aca6cad2dc26baa3cd684206f682
│                       │      │                   ab61aba9633 
│                       │      ├ Title           : When `CURLOPT_INTERFACE` (or the command line tool's
│                       │      │                   `--interface 
│                       │      ├ Description     : When `CURLOPT_INTERFACE` (or the command line tool's
│                       │      │                   `--interface` option) is set with one of the documented
│                       │      │                   prefixes (`if!`, `host!`, `ifhost!`), that binding is not
│                       │      │                   part of the connection reuse key, so a later transfer asking
│                       │      │                    for a different source can silently reuse an existing
│                       │      │                   connection and go out from the earlier transfer's source
│                       │      │                   address. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                       
│                       │                         ────────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-107929.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1  
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-107929
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-86409 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-86409 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:9b1421c1859d7be04d1b668d80326c54c8796772bf1ee11e3a318
│                       │      │                   d163af55dff 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : Setting `CURLOPT_AWS_SIGV4` to NULL does not disable SigV4
│                       │      │                   authentication, contrary to expectations and documentation.
│                       │      │                   A subsequent transfer on the same handle still sends an
│                       │      │                   `Authorization: AWS4-HMAC-SHA256` header to whatever URL is
│                       │      │                   set next, leaking state information. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-86409.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-86409
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-86410 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-86410 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3ded54e5cf8c38f2515435283c73319a6b53138140d0830f59ce1
│                       │      │                   ca00fe09e07 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : A flaw in the curl command line tool's logic makes it only
│                       │      │                   set SSH host verification options when interacting directly
│                       │      │                   using SFTP or SCP, and not as a result of following a
│                       │      │                   redirect. This means `--knownhosts`, `--hostpubsha256`, and
│                       │      │                   `--hostpubmd5` are never installed when the initial URL is
│                       │      │                   HTTPS. If `--location` and `--proto-redir +sftp` is used and
│                       │      │                    the server returns a `Location: sftp://example.com`
│                       │      │                   redirect, the SFTP connection proceeds without any of the
│                       │      │                   user's requested SSH host verification methods. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-86410.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-86410
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-86412 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-86412 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:2c22a3f4ec7be124ca94ead750c370bd50be1b0ec1770de2bd85e
│                       │      │                   c9b7ae54398 
│                       │      ├ Description     : A remote HTTP server can set a cookie that curl accepts and
│                       │      │                   writes to a Netscape cookie jar but cannot reload. On the
│                       │      │                   next invocation using the same path for `--cookie` and
│                       │      │                   `--cookie-jar`, curl fails before connecting, then the
│                       │      │                   cleanup procedure replaces the jar with an empty file,
│                       │      │                   deleting cookies for unrelated domains. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-86412.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-86412
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-86414 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-86414 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d688140d466455140834b1405f78e8c53ad751ac8cd0fc1446442
│                       │      │                   65cb4d7ad7c 
│                       │      ├ Title           : A HTTP proxy can trick libcurl into sending the origin's
│                       │      │                   credenti 
│                       │      ├ Description     : A HTTP proxy can trick libcurl into sending the origin's
│                       │      │                   credentials (Basic password, or a Negotiate/Kerberos ticket)
│                       │      │                    to the proxy itself, by answering the `CONNECT` tunnel
│                       │      │                   request with 401 `WWW-Authenticate:` instead of the expected
│                       │      │                    407 `Proxy-Authenticate:`. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-86414.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-86414
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-87862 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-87862 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:eab2e09741929ac5014c516de43f4b15d70ba8869d6a87518e03b
│                       │      │                   55fdb76d386 
│                       │      ├ Description     : Importing a `includeSubDomains` parent HSTS entry before a
│                       │      │                   longer-lived child entry, silently drops the child.
│                       │      │                   Consequently, when the parent expires, the child's valid
│                       │      │                   HSTS policy is lost, causing curl to issue unencrypted HTTP
│                       │      │                   requests rather than upgrading to HTTPS. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-87862.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-87862
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-87863 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-87863 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:97ab2a2cf29211e68f88f0e675edbb4c8eeec13964e580c6e669e
│                       │      │                   176f27e4f75 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : An authenticated HTTPS origin can supply an HSTS `max-age`
│                       │      │                   value that the parser accepts, but time serialization later
│                       │      │                   fails to process. On 64-bit systems, extreme max-age values
│                       │      │                   compute an absolute expiry within standard time integer
│                       │      │                   limits that exceeds calendar time structure bounds. During
│                       │      │                   cache saves, the original HSTS file is truncated before
│                       │      │                   writing a temporary replacement; when serialization fails,
│                       │      │                   the temporary file is deleted, leaving an empty or partial
│                       │      │                   cache. Because the save error is silently ignored during
│                       │      │                   cleanup, curl exits successfully despite the data loss. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-87863.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-87863
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-87864 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-87864 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0626fe1ef207e90faaf922dfb6391ca2ad7e36039233fdf7c9049
│                       │      │                   aed6baa1541 
│                       │      ├ Title           : IMAP APPEND plus CRLF conversion command injection 
│                       │      ├ Description     : Enabling `CURLOPT_CRLF` causes curl to advertise the raw
│                       │      │                   input byte count in the `IMAP APPEND {N}` literal while
│                       │      │                   transmitting line-ending expanded data. The server reads
│                       │      │                   only N bytes for the payload, causing the remaining overflow
│                       │      │                    bytes to be interpreted and executed as pipelined IMAP
│                       │      │                   commands within the authenticated session. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-87864.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-87864
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-87865 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-87865 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7676ba9ff3b0dfec48648ded1bf9a5dfacd185f8c03ece606e671
│                       │      │                   f0255cf9a9b 
│                       │      ├ Title           : When libcurl uses libssh2 with a hashed `known_hosts` file,
│                       │      │                   an un 
│                       │      ├ Description     : When libcurl uses libssh2 with a hashed `known_hosts` file,
│                       │      │                   an unrelated initial entry can cause host key validation to
│                       │      │                   report a key *mismatch* as a *missing* key to the
│                       │      │                   `CURLOPT_SSH_KEYFUNCTION` callback. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-87865.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-87865
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-92386 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92386 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0b6482add209e96867c9f25fe1279817c3bac50671246df409712
│                       │      │                   8f93bbc24b2 
│                       │      ├ Title           : When writing a long cookie name and value to a Netscape
│                       │      │                   cookie ja 
│                       │      ├ Description     : When writing a long cookie name and value to a Netscape
│                       │      │                   cookie jar, a remote HTTP server can make `curl` write a
│                       │      │                   record that exceeds its line-length parsing limit.
│                       │      │                   Consequently, any subsequent `curl` invocation reading from
│                       │      │                   that same cookie jar using `--cookie` will silently abort
│                       │      │                   parsing prematurely upon encountering the oversized line,
│                       │      │                   ignoring all subsequent valid cookies in the file. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-92386.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-92386
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-92387 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92387 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:787b98be8d43ce908194008cb93a81256c0eaaeea7e4ab9fd5004
│                       │      │                   63c7411a315 
│                       │      ├ Description     : By permanently omitting the final control-response line, a
│                       │      │                   malicious FTP, IMAP, POP3, or SMTP server can exploit
│                       │      │                   libcurl and completely bypass its configured transfer
│                       │      │                   timeout mechanism, indefinitely blocking all concurrent
│                       │      │                   transfers bound to the same multi-handle. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-92387.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-92387
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-92388 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92388 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f7798ac699a7bd936050cd06e5f4f344735814bcab245ebef5319
│                       │      │                   df6760bf46f 
│                       │      ├ Title           : curl: curl: FTP wildcard write callback mixup 
│                       │      ├ Description     : When an FTP wildcard `LIST` operation fails, libcurl omits
│                       │      │                   the restoration path meant for successful listings, leaving
│                       │      │                   the write callback set to the internal listing parser and
│                       │      │                   the write callback data pointing directly to the easy
│                       │      │                   handle. Subsequent reuse of this handle triggers an
│                       │      │                   immediate crash, and cloning it via `curl_easy_duphandle()`
│                       │      │                   copies this corrupted state into the duplicate. If the
│                       │      │                   original handle is subsequently freed, executing a transfer
│                       │      │                   on the cloned handle causes a heap use-after-free read
│                       │      │                   against the dangling handle reference; alternatively,
│                       │      │                   reusing the original or cloned handle while reconfiguring
│                       │      │                   only `CURLOPT_WRITEDATA` (and omitting
│                       │      │                   `CURLOPT_WRITEFUNCTION`) results in type confusion, forcing
│                       │      │                   the internal parser to interpret incoming server response
│                       │      │                   bytes into memory at the application-supplied write data
│                       │      │                   pointer. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-92388.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-92388
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-92389 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92389 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:11da3e0cf7c7cfda123dde9a2ce992b30285dae01fe37298f1d39
│                       │      │                   80406735c61 
│                       │      ├ Title           : TFTP direction confusion 
│                       │      ├ Description     : libcurl's TFTP state machine fails to validate state
│                       │      │                   transitions against the requested transfer direction,
│                       │      │                   accepting opening server responses for both reads and writes
│                       │      │                    interchangeably. A malicious TFTP server can respond to a
│                       │      │                   download request in a way that forces the client into
│                       │      │                   transmit mode, prompting libcurl to consume and transmit
│                       │      │                   data from the handle's persistent `CURLOPT_READDATA` pointer
│                       │      │                    - including data remaining from unrelated prior operations,
│                       │      │                    such as an HTTP POST request executed on a reused handle.[
│                       │      │                   m 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-92389.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-92389
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-92390 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92390 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:26b1f11844b9fb6c3e9843e086dbcd969b9f48383c9aa5eb80034
│                       │      │                   fca9a6ca082 
│                       │      ├ Title           : When invoked with `--remote-header-name` (`-J`), curl fails
│                       │      │                   to pr 
│                       │      ├ Description     : When invoked with `--remote-header-name` (`-J`), curl fails
│                       │      │                   to preserve its documented anti-clobbering protection if an
│                       │      │                   intermediate 103 Early Hints response precedes the final
│                       │      │                   HTTP response, or if an `ETag` header is processed before
│                       │      │                   `Content-Disposition` under `--etag-save`. This flaw allows
│                       │      │                   an HTTP(S) server to overwrite an existing local file
│                       │      │                   specified in the `Content-Disposition` header despite the
│                       │      │                   presence of the `-J` non-overwrite constraint. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-92390.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-92390
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-92391 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92391 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:841297b2b4d7a213932afbb3743f93fa9b5af9166876a6f0830c7
│                       │      │                   13af094d459 
│                       │      ├ Title           : curl_mime_free stack overflow by recursion 
│                       │      ├ Description     : A deeply nested multipart MIME structure constructed via the
│                       │      │                    public API causes a stack overflow in libcurl during normal
│                       │      │                    cleanup operations. An excessive recursion depth within
│                       │      │                   `curl_mime_free` leads to unbounded stack frame allocation
│                       │      │                   during structure traversal, ultimately crashing the host
│                       │      │                   process. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-92391.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-92391
│                       ├ [17] ╭ VulnerabilityID : CVE-2026-94266 
│                       │      ├ PkgID           : curl@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.18.0-1ubuntu2.7?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : c69738fa162111e2 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94266 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3d113df6c02871c69963eecf8fc95258ba47499e3bda86602ef43
│                       │      │                   217bc160a5f 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : libcurl could accidentally return a URL for
│                       │      │                   curl_easy_getinfo's `CURLINFO_EFFECTIVE_URL` option
│                       │      │                   containing credentials, even though neither the URL provided
│                       │      │                    to libcurl nor the redirected URL did. The curl tool
│                       │      │                   exposes the same information using the command line option
│                       │      │                   `--write-out '%{url_effective}'`. This credential leak can
│                       │      │                   happen when curl retrieves credentials from a `.netrc`
│                       │      │                   file. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-94266.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-94266
│                       ├ [18] ╭ VulnerabilityID : CVE-2026-18374 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2.4?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04 
│                       │      │                  ╰ UID : b964ecf8d3a43faa 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ed5e79df9ae2b016aa02b6352ab036b86e2d6520f5d3fd76a9637
│                       │      │                   fc828df1fae 
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
│                       │      ├ VendorSeverity   ╭ alma  : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ├ rocky : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/08/27/6      
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:79281             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18374        
│                       │      │                  https://bugzilla.redhat.com/2513603                          
│                       │      │                  https://bugzilla.redhat.com/2513608                          
│                       │      │                  https://bugzilla.redhat.com/2523249                          
│                       │      │                  https://bugzilla.redhat.com/2523274                          
│                       │      │                  https://bugzilla.redhat.com/2524870                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2513603          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2513608          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2523249          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2523274          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2524870          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2525256          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-18374
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-19542
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-6368 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-6791 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-77117
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-80489
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-79281.html          
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:79281                
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18374              
│                       │      │                  https://sourceware.org/bugzilla/show_bug.cgi?id=34574        
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/G
│                       │      │                  LIBC-SA-2026-0015                                            
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=adviso
│                       │      │                  ries/GLIBC-SA-2026-0015                                      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18374              
│                       │      ├ PublishedDate   : 2026-08-27T20:17:03.553Z 
│                       │      ╰ LastModifiedDate: 2026-09-03T16:43:15.293Z 
│                       ├ [19] ╭ VulnerabilityID : CVE-2026-89092 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2.4?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04 
│                       │      │                  ╰ UID : b964ecf8d3a43faa 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89092 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:48b3020b47ae48e7d6493dd39b90ade452a9c40c1a05b4c119ee3
│                       │      │                   d8fd2f5a73d 
│                       │      ├ Title           : glibc: nscd stack overflow leads to degraded DNS resolution 
│                       │      ├ Description     : The nscd service in the GNU C Library 2.3.4 onwards may
│                       │      │                   crash due to a 
│                       │      │                   stack overflow when a malicious DNS server returns too large
│                       │      │                    a response 
│                       │      │                   for a DNS query, resulting in degraded DNS resolution for
│                       │      │                   the system.
│                       │      │                   
│                       │      │                   Exploitation of this bug needs a system that has nscd
│                       │      │                   enabled and using 
│                       │      │                   an untrusted DNS server for name resolution, with the
│                       │      │                   compromised DNS 
│                       │      │                   server being capable of processing records large enough to
│                       │      │                   result in a 
│                       │      │                   stack overflow in an nscd thread stack.  During
│                       │      │                   experimentation, bind 9 
│                       │      │                   was unable to handle large records, but that could change in
│                       │      │                    future or 
│                       │      │                   with a different name server.  In typical installations,
│                       │      │                   nscd is 
│                       │      │                   executed in an isolated context as its own user without a
│                       │      │                   shell, due to 
│                       │      │                   which any compromise of that service is isolated.
│                       │      │                   There is a remote possibility of nscd cache corruption if an
│                       │      │                    attacker 
│                       │      │                   manages to get the stack pointer into a desired point in the
│                       │      │                    heap, 
│                       │      │                   potentially resulting in other caches in nscd being
│                       │      │                   overwritten with 
│                       │      │                   corrupt data through the stack overflow, until the buggy
│                       │      │                   code path 
│                       │      │                   eventually results in a crash.
│                       │      │                   Finally, a crash in nscd may result in performance
│                       │      │                   degradation when 
│                       │      │                   resolving names, but it does not result in a denial of
│                       │      │                   service. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-789
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/09/11/2      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89092        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89092              
│                       │      │                  https://sourceware.org/bugzilla/show_bug.cgi?id=34624        
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/G
│                       │      │                  LIBC-SA-2026-0016                                            
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=adviso
│                       │      │                  ries/GLIBC-SA-2026-0016                                      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89092              
│                       │      ├ PublishedDate   : 2026-09-11T02:18:35.46Z 
│                       │      ╰ LastModifiedDate: 2026-09-11T18:17:00.23Z 
│                       ├ [20] ╭ VulnerabilityID : CVE-2026-18374 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       .4?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : bbb7a8f7a59474e8 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:07c6b4e242ad6fbdc54b59bd0ac740cb9154a1e6a5beec632a3ec
│                       │      │                   1b6c3cefbf8 
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
│                       │      ├ VendorSeverity   ╭ alma  : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ├ rocky : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/08/27/6      
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:79281             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18374        
│                       │      │                  https://bugzilla.redhat.com/2513603                          
│                       │      │                  https://bugzilla.redhat.com/2513608                          
│                       │      │                  https://bugzilla.redhat.com/2523249                          
│                       │      │                  https://bugzilla.redhat.com/2523274                          
│                       │      │                  https://bugzilla.redhat.com/2524870                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2513603          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2513608          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2523249          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2523274          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2524870          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2525256          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-18374
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-19542
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-6368 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-6791 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-77117
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-80489
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-79281.html          
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:79281                
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18374              
│                       │      │                  https://sourceware.org/bugzilla/show_bug.cgi?id=34574        
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/G
│                       │      │                  LIBC-SA-2026-0015                                            
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=adviso
│                       │      │                  ries/GLIBC-SA-2026-0015                                      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18374              
│                       │      ├ PublishedDate   : 2026-08-27T20:17:03.553Z 
│                       │      ╰ LastModifiedDate: 2026-09-03T16:43:15.293Z 
│                       ├ [21] ╭ VulnerabilityID : CVE-2026-89092 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       .4?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : bbb7a8f7a59474e8 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89092 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d494186721d972ea4b49dac7c4b64c5b9d001f76a95d7f0805313
│                       │      │                   81481eacbcf 
│                       │      ├ Title           : glibc: nscd stack overflow leads to degraded DNS resolution 
│                       │      ├ Description     : The nscd service in the GNU C Library 2.3.4 onwards may
│                       │      │                   crash due to a 
│                       │      │                   stack overflow when a malicious DNS server returns too large
│                       │      │                    a response 
│                       │      │                   for a DNS query, resulting in degraded DNS resolution for
│                       │      │                   the system.
│                       │      │                   
│                       │      │                   Exploitation of this bug needs a system that has nscd
│                       │      │                   enabled and using 
│                       │      │                   an untrusted DNS server for name resolution, with the
│                       │      │                   compromised DNS 
│                       │      │                   server being capable of processing records large enough to
│                       │      │                   result in a 
│                       │      │                   stack overflow in an nscd thread stack.  During
│                       │      │                   experimentation, bind 9 
│                       │      │                   was unable to handle large records, but that could change in
│                       │      │                    future or 
│                       │      │                   with a different name server.  In typical installations,
│                       │      │                   nscd is 
│                       │      │                   executed in an isolated context as its own user without a
│                       │      │                   shell, due to 
│                       │      │                   which any compromise of that service is isolated.
│                       │      │                   There is a remote possibility of nscd cache corruption if an
│                       │      │                    attacker 
│                       │      │                   manages to get the stack pointer into a desired point in the
│                       │      │                    heap, 
│                       │      │                   potentially resulting in other caches in nscd being
│                       │      │                   overwritten with 
│                       │      │                   corrupt data through the stack overflow, until the buggy
│                       │      │                   code path 
│                       │      │                   eventually results in a crash.
│                       │      │                   Finally, a crash in nscd may result in performance
│                       │      │                   degradation when 
│                       │      │                   resolving names, but it does not result in a denial of
│                       │      │                   service. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-789
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/09/11/2      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89092        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89092              
│                       │      │                  https://sourceware.org/bugzilla/show_bug.cgi?id=34624        
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/G
│                       │      │                  LIBC-SA-2026-0016                                            
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=adviso
│                       │      │                  ries/GLIBC-SA-2026-0016                                      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89092              
│                       │      ├ PublishedDate   : 2026-09-11T02:18:35.46Z 
│                       │      ╰ LastModifiedDate: 2026-09-11T18:17:00.23Z 
│                       ├ [22] ╭ VulnerabilityID : CVE-2026-18374 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2.4?arch=amd64&distr
│                       │      │                  │       o=ubuntu-26.04 
│                       │      │                  ╰ UID : fe574f54c2bc3102 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:708acb0337868afd064da6577823a7b762c2eb8da89d0022ad847
│                       │      │                   8d945f58324 
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
│                       │      ├ VendorSeverity   ╭ alma  : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ├ rocky : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/08/27/6      
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:79281             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-18374        
│                       │      │                  https://bugzilla.redhat.com/2513603                          
│                       │      │                  https://bugzilla.redhat.com/2513608                          
│                       │      │                  https://bugzilla.redhat.com/2523249                          
│                       │      │                  https://bugzilla.redhat.com/2523274                          
│                       │      │                  https://bugzilla.redhat.com/2524870                          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2513603          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2513608          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2523249          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2523274          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2524870          
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2525256          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-18374
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-19542
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-6368 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-6791 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-77117
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-80489
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-79281.html          
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:79281                
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18374              
│                       │      │                  https://sourceware.org/bugzilla/show_bug.cgi?id=34574        
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/G
│                       │      │                  LIBC-SA-2026-0015                                            
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=adviso
│                       │      │                  ries/GLIBC-SA-2026-0015                                      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18374              
│                       │      ├ PublishedDate   : 2026-08-27T20:17:03.553Z 
│                       │      ╰ LastModifiedDate: 2026-09-03T16:43:15.293Z 
│                       ├ [23] ╭ VulnerabilityID : CVE-2026-89092 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2.4 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2.4?arch=amd64&distr
│                       │      │                  │       o=ubuntu-26.04 
│                       │      │                  ╰ UID : fe574f54c2bc3102 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89092 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:643724cd9bd1100cf6783fb9780b7bd55e26ffcd7b6dbdfd37c11
│                       │      │                   51d5dd5fe67 
│                       │      ├ Title           : glibc: nscd stack overflow leads to degraded DNS resolution 
│                       │      ├ Description     : The nscd service in the GNU C Library 2.3.4 onwards may
│                       │      │                   crash due to a 
│                       │      │                   stack overflow when a malicious DNS server returns too large
│                       │      │                    a response 
│                       │      │                   for a DNS query, resulting in degraded DNS resolution for
│                       │      │                   the system.
│                       │      │                   
│                       │      │                   Exploitation of this bug needs a system that has nscd
│                       │      │                   enabled and using 
│                       │      │                   an untrusted DNS server for name resolution, with the
│                       │      │                   compromised DNS 
│                       │      │                   server being capable of processing records large enough to
│                       │      │                   result in a 
│                       │      │                   stack overflow in an nscd thread stack.  During
│                       │      │                   experimentation, bind 9 
│                       │      │                   was unable to handle large records, but that could change in
│                       │      │                    future or 
│                       │      │                   with a different name server.  In typical installations,
│                       │      │                   nscd is 
│                       │      │                   executed in an isolated context as its own user without a
│                       │      │                   shell, due to 
│                       │      │                   which any compromise of that service is isolated.
│                       │      │                   There is a remote possibility of nscd cache corruption if an
│                       │      │                    attacker 
│                       │      │                   manages to get the stack pointer into a desired point in the
│                       │      │                    heap, 
│                       │      │                   potentially resulting in other caches in nscd being
│                       │      │                   overwritten with 
│                       │      │                   corrupt data through the stack overflow, until the buggy
│                       │      │                   code path 
│                       │      │                   eventually results in a crash.
│                       │      │                   Finally, a crash in nscd may result in performance
│                       │      │                   degradation when 
│                       │      │                   resolving names, but it does not result in a denial of
│                       │      │                   service. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-789
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/09/11/2      
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89092        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89092              
│                       │      │                  https://sourceware.org/bugzilla/show_bug.cgi?id=34624        
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob;f=advisories/G
│                       │      │                  LIBC-SA-2026-0016                                            
│                       │      │                  https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=adviso
│                       │      │                  ries/GLIBC-SA-2026-0016                                      
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89092              
│                       │      ├ PublishedDate   : 2026-09-11T02:18:35.46Z 
│                       │      ╰ LastModifiedDate: 2026-09-11T18:17:00.23Z 
│                       ├ [24] ╭ VulnerabilityID : CVE-2026-92392 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92392 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:67a96f91edbf169ccdfb83b558eb2eb33c80b9a15e90b9f803e18
│                       │      │                   39594161de7 
│                       │      ├ Title           : During an upload, curl mishandles HTTP/2 `RST_STREAM`
│                       │      │                   received from th ... 
│                       │      ├ Description     : During an upload, curl mishandles HTTP/2 `RST_STREAM`
│                       │      │                   received from the server
│                       │      │                   (with reason `HTTP_1_1_REQUIRED` or `REFUSED_STREAM`)
│                       │      │                   leading to a use after
│                       │      │                   free of a `struct Curl_easy` object. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ ubuntu: 3 
│                       │      ├ References                                                      
│                       │      │                  ───────────────────────────────────────────────
│                       │      │                  https://curl.se/docs/CVE-2026-92392.html       
│                       │      │                  https://curl.se/docs/CVE-2026-92392.json       
│                       │      │                  https://hackerone.com/reports/4030333          
│                       │      │                  https://ubuntu.com/security/notices/USN-8927-1 
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-92392
│                       │      ├ PublishedDate   : 2026-10-14T08:17:05.997Z 
│                       │      ╰ LastModifiedDate: 2026-10-15T04:18:29.19Z 
│                       ├ [25] ╭ VulnerabilityID : CVE-2026-107928 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-107928 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5ffe484f9aba1f49ddc4445435f3e32ac5df156baf16ee72615db
│                       │      │                   052cca282e1 
│                       │      ├ Title           : When curl is built with GnuTLS, a malicious WebSocket server
│                       │      │                    can  
│                       │      ├ Description     : When curl is built with GnuTLS, a malicious WebSocket server
│                       │      │                    can make curl send memory past its send buffer. This is due
│                       │      │                    to an out of bounds read following when
│                       │      │                   `gnutls_record_send()` returns a number of bytes sent
│                       │      │                   greater than the number of bytes it was given to send.
│                       │      │                   GnuTLS does that after a blocked send. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                       
│                       │                         ────────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-107928.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1  
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-107928
│                       ├ [26] ╭ VulnerabilityID : CVE-2026-107929 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-107929 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:33e4cfac8e6d139a9d1760f06b3d31b058f587d950f54be59e1c1
│                       │      │                   403d9f71a8d 
│                       │      ├ Title           : When `CURLOPT_INTERFACE` (or the command line tool's
│                       │      │                   `--interface 
│                       │      ├ Description     : When `CURLOPT_INTERFACE` (or the command line tool's
│                       │      │                   `--interface` option) is set with one of the documented
│                       │      │                   prefixes (`if!`, `host!`, `ifhost!`), that binding is not
│                       │      │                   part of the connection reuse key, so a later transfer asking
│                       │      │                    for a different source can silently reuse an existing
│                       │      │                   connection and go out from the earlier transfer's source
│                       │      │                   address. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                       
│                       │                         ────────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-107929.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1  
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-107929
│                       ├ [27] ╭ VulnerabilityID : CVE-2026-86409 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-86409 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7d37850554e399f41dacdbc52112c2546aed159b4773434d217d1
│                       │      │                   64999c29c00 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : Setting `CURLOPT_AWS_SIGV4` to NULL does not disable SigV4
│                       │      │                   authentication, contrary to expectations and documentation.
│                       │      │                   A subsequent transfer on the same handle still sends an
│                       │      │                   `Authorization: AWS4-HMAC-SHA256` header to whatever URL is
│                       │      │                   set next, leaking state information. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-86409.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-86409
│                       ├ [28] ╭ VulnerabilityID : CVE-2026-86410 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-86410 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a22877f93316459772baa321e2922f0d4e98ac9bc8248cc301066
│                       │      │                   c64137797f3 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : A flaw in the curl command line tool's logic makes it only
│                       │      │                   set SSH host verification options when interacting directly
│                       │      │                   using SFTP or SCP, and not as a result of following a
│                       │      │                   redirect. This means `--knownhosts`, `--hostpubsha256`, and
│                       │      │                   `--hostpubmd5` are never installed when the initial URL is
│                       │      │                   HTTPS. If `--location` and `--proto-redir +sftp` is used and
│                       │      │                    the server returns a `Location: sftp://example.com`
│                       │      │                   redirect, the SFTP connection proceeds without any of the
│                       │      │                   user's requested SSH host verification methods. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-86410.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-86410
│                       ├ [29] ╭ VulnerabilityID : CVE-2026-86412 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-86412 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:22db4cbb2740f03cfbd29cc1154bcdf7fef6faade54bdbcb40397
│                       │      │                   8938109f789 
│                       │      ├ Description     : A remote HTTP server can set a cookie that curl accepts and
│                       │      │                   writes to a Netscape cookie jar but cannot reload. On the
│                       │      │                   next invocation using the same path for `--cookie` and
│                       │      │                   `--cookie-jar`, curl fails before connecting, then the
│                       │      │                   cleanup procedure replaces the jar with an empty file,
│                       │      │                   deleting cookies for unrelated domains. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-86412.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-86412
│                       ├ [30] ╭ VulnerabilityID : CVE-2026-86414 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-86414 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:55ae3340be871c521920d3ac0ed685caa6f1f9e0e72ccc3e307c9
│                       │      │                   ef1c09259a7 
│                       │      ├ Title           : A HTTP proxy can trick libcurl into sending the origin's
│                       │      │                   credenti 
│                       │      ├ Description     : A HTTP proxy can trick libcurl into sending the origin's
│                       │      │                   credentials (Basic password, or a Negotiate/Kerberos ticket)
│                       │      │                    to the proxy itself, by answering the `CONNECT` tunnel
│                       │      │                   request with 401 `WWW-Authenticate:` instead of the expected
│                       │      │                    407 `Proxy-Authenticate:`. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-86414.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-86414
│                       ├ [31] ╭ VulnerabilityID : CVE-2026-87862 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-87862 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e0ac4700b68a040e392345bb3b6db929aed2f8f947dcdeff7665e
│                       │      │                   fc66bf8d470 
│                       │      ├ Description     : Importing a `includeSubDomains` parent HSTS entry before a
│                       │      │                   longer-lived child entry, silently drops the child.
│                       │      │                   Consequently, when the parent expires, the child's valid
│                       │      │                   HSTS policy is lost, causing curl to issue unencrypted HTTP
│                       │      │                   requests rather than upgrading to HTTPS. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-87862.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-87862
│                       ├ [32] ╭ VulnerabilityID : CVE-2026-87863 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-87863 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ed2a3de489ba4f6521ad33fd12b34d37c019bb1d253c83812bf37
│                       │      │                   729f6092905 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : An authenticated HTTPS origin can supply an HSTS `max-age`
│                       │      │                   value that the parser accepts, but time serialization later
│                       │      │                   fails to process. On 64-bit systems, extreme max-age values
│                       │      │                   compute an absolute expiry within standard time integer
│                       │      │                   limits that exceeds calendar time structure bounds. During
│                       │      │                   cache saves, the original HSTS file is truncated before
│                       │      │                   writing a temporary replacement; when serialization fails,
│                       │      │                   the temporary file is deleted, leaving an empty or partial
│                       │      │                   cache. Because the save error is silently ignored during
│                       │      │                   cleanup, curl exits successfully despite the data loss. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-87863.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-87863
│                       ├ [33] ╭ VulnerabilityID : CVE-2026-87864 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-87864 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:1716384d2b64b4170d9c394b933ae1a10e6ba9844c90ec83ed306
│                       │      │                   402cc5a0c39 
│                       │      ├ Title           : IMAP APPEND plus CRLF conversion command injection 
│                       │      ├ Description     : Enabling `CURLOPT_CRLF` causes curl to advertise the raw
│                       │      │                   input byte count in the `IMAP APPEND {N}` literal while
│                       │      │                   transmitting line-ending expanded data. The server reads
│                       │      │                   only N bytes for the payload, causing the remaining overflow
│                       │      │                    bytes to be interpreted and executed as pipelined IMAP
│                       │      │                   commands within the authenticated session. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-87864.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-87864
│                       ├ [34] ╭ VulnerabilityID : CVE-2026-87865 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-87865 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:1ecafbf9bb5edbd1d2b3ed56b289e1a03dbfa9459d7286a560504
│                       │      │                   b7da5bf9c01 
│                       │      ├ Title           : When libcurl uses libssh2 with a hashed `known_hosts` file,
│                       │      │                   an un 
│                       │      ├ Description     : When libcurl uses libssh2 with a hashed `known_hosts` file,
│                       │      │                   an unrelated initial entry can cause host key validation to
│                       │      │                   report a key *mismatch* as a *missing* key to the
│                       │      │                   `CURLOPT_SSH_KEYFUNCTION` callback. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-87865.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-87865
│                       ├ [35] ╭ VulnerabilityID : CVE-2026-92386 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92386 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:bc290a01fce863d99521a3a978061a75ecfffaafd4a9dcb37ee0a
│                       │      │                   21c06e73e5b 
│                       │      ├ Title           : When writing a long cookie name and value to a Netscape
│                       │      │                   cookie ja 
│                       │      ├ Description     : When writing a long cookie name and value to a Netscape
│                       │      │                   cookie jar, a remote HTTP server can make `curl` write a
│                       │      │                   record that exceeds its line-length parsing limit.
│                       │      │                   Consequently, any subsequent `curl` invocation reading from
│                       │      │                   that same cookie jar using `--cookie` will silently abort
│                       │      │                   parsing prematurely upon encountering the oversized line,
│                       │      │                   ignoring all subsequent valid cookies in the file. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-92386.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-92386
│                       ├ [36] ╭ VulnerabilityID : CVE-2026-92387 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92387 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:713691efa573d2363d2d3adb222c52435961927777504f15537d4
│                       │      │                   b76d10b6975 
│                       │      ├ Description     : By permanently omitting the final control-response line, a
│                       │      │                   malicious FTP, IMAP, POP3, or SMTP server can exploit
│                       │      │                   libcurl and completely bypass its configured transfer
│                       │      │                   timeout mechanism, indefinitely blocking all concurrent
│                       │      │                   transfers bound to the same multi-handle. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-92387.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-92387
│                       ├ [37] ╭ VulnerabilityID : CVE-2026-92388 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92388 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b7c680df0b3e980c604f60e9e27cb263659687fc481d32ed8e5bf
│                       │      │                   b69b5f58802 
│                       │      ├ Title           : curl: curl: FTP wildcard write callback mixup 
│                       │      ├ Description     : When an FTP wildcard `LIST` operation fails, libcurl omits
│                       │      │                   the restoration path meant for successful listings, leaving
│                       │      │                   the write callback set to the internal listing parser and
│                       │      │                   the write callback data pointing directly to the easy
│                       │      │                   handle. Subsequent reuse of this handle triggers an
│                       │      │                   immediate crash, and cloning it via `curl_easy_duphandle()`
│                       │      │                   copies this corrupted state into the duplicate. If the
│                       │      │                   original handle is subsequently freed, executing a transfer
│                       │      │                   on the cloned handle causes a heap use-after-free read
│                       │      │                   against the dangling handle reference; alternatively,
│                       │      │                   reusing the original or cloned handle while reconfiguring
│                       │      │                   only `CURLOPT_WRITEDATA` (and omitting
│                       │      │                   `CURLOPT_WRITEFUNCTION`) results in type confusion, forcing
│                       │      │                   the internal parser to interpret incoming server response
│                       │      │                   bytes into memory at the application-supplied write data
│                       │      │                   pointer. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-92388.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-92388
│                       ├ [38] ╭ VulnerabilityID : CVE-2026-92389 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92389 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d3d4a86dbe3df4be93ed5e9e7aabc104b1fbac605ee87addab344
│                       │      │                   ff93ec47602 
│                       │      ├ Title           : TFTP direction confusion 
│                       │      ├ Description     : libcurl's TFTP state machine fails to validate state
│                       │      │                   transitions against the requested transfer direction,
│                       │      │                   accepting opening server responses for both reads and writes
│                       │      │                    interchangeably. A malicious TFTP server can respond to a
│                       │      │                   download request in a way that forces the client into
│                       │      │                   transmit mode, prompting libcurl to consume and transmit
│                       │      │                   data from the handle's persistent `CURLOPT_READDATA` pointer
│                       │      │                    - including data remaining from unrelated prior operations,
│                       │      │                    such as an HTTP POST request executed on a reused handle.[
│                       │      │                   m 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-92389.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-92389
│                       ├ [39] ╭ VulnerabilityID : CVE-2026-92390 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92390 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:eab88f636a197d857862c0c1b7ee37358f0ac26267d9b6c8a18a6
│                       │      │                   323a0372eec 
│                       │      ├ Title           : When invoked with `--remote-header-name` (`-J`), curl fails
│                       │      │                   to pr 
│                       │      ├ Description     : When invoked with `--remote-header-name` (`-J`), curl fails
│                       │      │                   to preserve its documented anti-clobbering protection if an
│                       │      │                   intermediate 103 Early Hints response precedes the final
│                       │      │                   HTTP response, or if an `ETag` header is processed before
│                       │      │                   `Content-Disposition` under `--etag-save`. This flaw allows
│                       │      │                   an HTTP(S) server to overwrite an existing local file
│                       │      │                   specified in the `Content-Disposition` header despite the
│                       │      │                   presence of the `-J` non-overwrite constraint. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-92390.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-92390
│                       ├ [40] ╭ VulnerabilityID : CVE-2026-92391 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-92391 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e0c9372944ce8f0ee33a6bfbc97ca8404b7d4959e85c1d9323771
│                       │      │                   0d16bce79f3 
│                       │      ├ Title           : curl_mime_free stack overflow by recursion 
│                       │      ├ Description     : A deeply nested multipart MIME structure constructed via the
│                       │      │                    public API causes a stack overflow in libcurl during normal
│                       │      │                    cleanup operations. An excessive recursion depth within
│                       │      │                   `curl_mime_free` leads to unbounded stack frame allocation
│                       │      │                   during structure traversal, ultimately crashing the host
│                       │      │                   process. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-92391.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-92391
│                       ├ [41] ╭ VulnerabilityID : CVE-2026-94266 
│                       │      ├ PkgID           : libcurl4t64@8.18.0-1ubuntu2.7 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.18.0-1ubuntu2.7?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : b177b5ee6b7bd07c 
│                       │      ├ InstalledVersion: 8.18.0-1ubuntu2.7 
│                       │      ├ FixedVersion    : 8.18.0-1ubuntu2.8 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94266 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:acc818dcf3dc0f64c9d42cd80acd64e6b6c300d46e7e58378a4a6
│                       │      │                   a6f3a039b12 
│                       │      ├ Title           : Title Not Available 
│                       │      ├ Description     : libcurl could accidentally return a URL for
│                       │      │                   curl_easy_getinfo's `CURLINFO_EFFECTIVE_URL` option
│                       │      │                   containing credentials, even though neither the URL provided
│                       │      │                    to libcurl nor the redirected URL did. The curl tool
│                       │      │                   exposes the same information using the command line option
│                       │      │                   `--write-out '%{url_effective}'`. This credential leak can
│                       │      │                   happen when curl retrieves credentials from a `.netrc`
│                       │      │                   file. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ╰ References                                                      
│                       │                         ───────────────────────────────────────────────
│                       │                         https://curl.se/docs/CVE-2026-94266.html       
│                       │                         https://ubuntu.com/security/notices/USN-8927-1 
│                       │                         https://www.cve.org/CVERecord?id=CVE-2026-94266
│                       ├ [42] ╭ VulnerabilityID : CVE-2025-66382 
│                       │      ├ PkgID           : libexpat1@2.7.4-1ubuntu0.2 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1ubuntu0.2?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 1019b85f746342f4 
│                       │      ├ InstalledVersion: 2.7.4-1ubuntu0.2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-66382 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e917202860dc55380a473b53717241e51f8921f597e9dc93d311f
│                       │      │                   281ea8c44e1 
│                       │      ├ Title           : libexpat: libexpat: Denial of service via crafted file
│                       │      │                   processing 
│                       │      ├ Description     : In libexpat through 2.7.3, a crafted file with an
│                       │      │                   approximate size of 2 MiB can lead to dozens of seconds of
│                       │      │                   processing time. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-407
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
│                       │      ├ PublishedDate   : 2025-11-28T07:15:57.9Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T09:56:45.24Z 
│                       ├ [43] ╭ VulnerabilityID : CVE-2026-13757 
│                       │      ├ PkgID           : libp11-kit0@0.26.2-2 
│                       │      ├ PkgName         : libp11-kit0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libp11-kit0@0.26.2-2?arch=amd64&distro
│                       │      │                  │       =ubuntu-26.04 
│                       │      │                  ╰ UID : 39936f33632ab742 
│                       │      ├ InstalledVersion: 0.26.2-2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13757 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a11c7d2fb17aa5fa4fb54500c0bda60f75267ae5ef80cde355e29
│                       │      │                   da4c847fe33 
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
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72394             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72395             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72399             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72470             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72475             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72476             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:72502             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:81201             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:82304             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:82322             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:82336             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:82347             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:82354             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:82372             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:82857             
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:82888             
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
│                       │      ├ PublishedDate   : 2026-06-29T19:16:40.907Z 
│                       │      ╰ LastModifiedDate: 2026-10-14T20:17:32.733Z 
│                       ├ [44] ╭ VulnerabilityID : CVE-2026-103111 
│                       │      ├ PkgID           : libpcre2-8-0@10.46-1build1 
│                       │      ├ PkgName         : libpcre2-8-0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpcre2-8-0@10.46-1build1?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c9d0d8772a6e5e1d 
│                       │      ├ InstalledVersion: 10.46-1build1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-103111 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7ff0127951ce4f23aa7270a71900419dcef0bdd36b70db0deb573
│                       │      │                   33291578aa4 
│                       │      ├ Title           : pcre2: pcre2: Out-of-bounds write via crafted regular
│                       │      │                   expression 
│                       │      ├ Description     : PCRE2 before 10.49, when there is an attacker-controlled
│                       │      │                   regular expression and certain JIT API usage, allows an
│                       │      │                   out-of-bounds write with arbitrary data. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-787
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 7.6 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:81532             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-103111       
│                       │      │                  https://bugzilla.redhat.com/2528993                          
│                       │      │                  https://bugzilla.redhat.com/2531743                          
│                       │      │                  https://bugzilla.redhat.com/2531744                          
│                       │      │                  https://bugzilla.redhat.com/2531745                          
│                       │      │                  https://bugzilla.redhat.com/2531746                          
│                       │      │                  https://bugzilla.redhat.com/2531747                          
│                       │      │                  https://bugzilla.redhat.com/2543797                          
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-81532.html          
│                       │      │                  https://github.com/PCRE2Project/pcre2/security/advisories/GHS
│                       │      │                  A-r9hj-j2rw-4q3m                                             
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-103111.html            
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-81613.html         
│                       │      │                                                                               
│                       │      │                  https://lists.debian.org/debian-lts-announce/2026/10/msg00008
│                       │      │                  .html                                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-103111             
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-103111             
│                       │      ├ PublishedDate   : 2026-09-30T05:16:45.863Z 
│                       │      ╰ LastModifiedDate: 2026-10-04T00:16:35.563Z 
│                       ├ [45] ╭ VulnerabilityID : CVE-2026-86145 
│                       │      ├ PkgID           : libpcre2-8-0@10.46-1build1 
│                       │      ├ PkgName         : libpcre2-8-0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpcre2-8-0@10.46-1build1?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c9d0d8772a6e5e1d 
│                       │      ├ InstalledVersion: 10.46-1build1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-86145 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d84193ff25c3f3dba6f1323245ee4c2d28362a423fae6e88bf69a
│                       │      │                   9103e546755 
│                       │      ├ Title           : pcre2: PCRE2: Out-of-bounds write allows arbitrary code
│                       │      │                   execution via crafted regular expressions 
│                       │      ├ Description     : PCRE2 before 10.48 allows a pcre2_dfa_match out-of-bounds
│                       │      │                   write because reuse of a cached workspace block, in a
│                       │      │                   recursive DFA matching workspace, lacks a size check (even
│                       │      │                   though a newly allocated block, for the same purpose, does
│                       │      │                   have a size check). This outcome requires an
│                       │      │                   attacker-controlled regular expression, or a recursive
│                       │      │                   pattern in conjunction with a small heap limit (this can be
│                       │      │                   set through the API). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-424
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 8.2 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/09/05/3      
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:81532             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-86145        
│                       │      │                  https://bugzilla.redhat.com/2528993                          
│                       │      │                  https://bugzilla.redhat.com/2531743                          
│                       │      │                  https://bugzilla.redhat.com/2531744                          
│                       │      │                  https://bugzilla.redhat.com/2531745                          
│                       │      │                  https://bugzilla.redhat.com/2531746                          
│                       │      │                  https://bugzilla.redhat.com/2531747                          
│                       │      │                  https://bugzilla.redhat.com/2543797                          
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-81532.html          
│                       │      │                  https://github.com/PCRE2Project/pcre2/releases/tag/pcre2-10.4
│                       │      │                  8                                                            
│                       │      │                  https://github.com/PCRE2Project/pcre2/security/advisories/GHS
│                       │      │                  A-3r4p-g7gg-ppmf                                             
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-86145.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-81613.html         
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-86145              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-86145              
│                       │      ├ PublishedDate   : 2026-09-05T06:17:10.37Z 
│                       │      ╰ LastModifiedDate: 2026-09-09T16:04:24.933Z 
│                       ├ [46] ╭ VulnerabilityID : CVE-2026-89156 
│                       │      ├ PkgID           : libpcre2-8-0@10.46-1build1 
│                       │      ├ PkgName         : libpcre2-8-0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpcre2-8-0@10.46-1build1?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c9d0d8772a6e5e1d 
│                       │      ├ InstalledVersion: 10.46-1build1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89156 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:cccdcc583f72a1ed78376442674fe778503ab82a07ab8525caeda
│                       │      │                   810eb1077ce 
│                       │      ├ Title           : PCRE2: PCRE2: Out-of-bounds read via invalid UTF data during
│                       │      │                    JIT fallback 
│                       │      ├ Description     : PCRE2 before 10.48 has a pcre2_match out-of-bounds read
│                       │      │                   after a JIT fallback when an attacker can provide invalid
│                       │      │                   UTF data. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ azure      : 1 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.9 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 2.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:81532             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89156        
│                       │      │                  https://bugzilla.redhat.com/2528993                          
│                       │      │                  https://bugzilla.redhat.com/2531743                          
│                       │      │                  https://bugzilla.redhat.com/2531744                          
│                       │      │                  https://bugzilla.redhat.com/2531745                          
│                       │      │                  https://bugzilla.redhat.com/2531746                          
│                       │      │                  https://bugzilla.redhat.com/2531747                          
│                       │      │                  https://bugzilla.redhat.com/2543797                          
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-81532.html          
│                       │      │                  https://github.com/PCRE2Project/pcre2/releases/tag/pcre2-10.4
│                       │      │                  8                                                            
│                       │      │                  https://github.com/PCRE2Project/pcre2/security/advisories/GHS
│                       │      │                  A-2p8c-ff85-vh9x                                             
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-89156.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-81532.html         
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89156              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89156              
│                       │      ├ PublishedDate   : 2026-09-11T04:18:03.23Z 
│                       │      ╰ LastModifiedDate: 2026-09-16T19:27:01.327Z 
│                       ├ [47] ╭ VulnerabilityID : CVE-2026-89157 
│                       │      ├ PkgID           : libpcre2-8-0@10.46-1build1 
│                       │      ├ PkgName         : libpcre2-8-0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpcre2-8-0@10.46-1build1?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c9d0d8772a6e5e1d 
│                       │      ├ InstalledVersion: 10.46-1build1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89157 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:42ee40f6cf9e5eb3a1ed92b32bdd20ca902eada39480f8792a759
│                       │      │                   11597a28541 
│                       │      ├ Title           : pcre2: PCRE2: Out-of-bounds write via large pattern input 
│                       │      ├ Description     : PCRE2 before 10.48, on 32-bit platforms, has a
│                       │      │                   pcre2_pattern_convert out-of-bounds write when an attacker
│                       │      │                   can provide a large pattern. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-190
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ nvd        : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.4 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:81532             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89157        
│                       │      │                  https://bugzilla.redhat.com/2528993                          
│                       │      │                  https://bugzilla.redhat.com/2531743                          
│                       │      │                  https://bugzilla.redhat.com/2531744                          
│                       │      │                  https://bugzilla.redhat.com/2531745                          
│                       │      │                  https://bugzilla.redhat.com/2531746                          
│                       │      │                  https://bugzilla.redhat.com/2531747                          
│                       │      │                  https://bugzilla.redhat.com/2543797                          
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-81532.html          
│                       │      │                  https://github.com/PCRE2Project/pcre2/releases/tag/pcre2-10.4
│                       │      │                  8                                                            
│                       │      │                  https://github.com/PCRE2Project/pcre2/security/advisories/GHS
│                       │      │                  A-q8g2-wprr-34m9                                             
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-89157.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-81613.html         
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89157              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89157              
│                       │      ├ PublishedDate   : 2026-09-11T04:18:03.753Z 
│                       │      ╰ LastModifiedDate: 2026-09-16T19:25:08.88Z 
│                       ├ [48] ╭ VulnerabilityID : CVE-2026-89158 
│                       │      ├ PkgID           : libpcre2-8-0@10.46-1build1 
│                       │      ├ PkgName         : libpcre2-8-0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpcre2-8-0@10.46-1build1?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c9d0d8772a6e5e1d 
│                       │      ├ InstalledVersion: 10.46-1build1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89158 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:07dec5c7c41eb29a190db5d3465e393ad47d4e5917e8347700097
│                       │      │                   c4325be9f89 
│                       │      ├ Title           : PCRE2: PCRE2: Out-of-bounds write via integer overflow on
│                       │      │                   32-bit platforms 
│                       │      ├ Description     : PCRE2 before 10.48, on 32-bit platforms, has a
│                       │      │                   pcre2_compile_32 integer overflow and resultant
│                       │      │                   out-of-bounds write. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-190
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:81532             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89158        
│                       │      │                  https://bugzilla.redhat.com/2528993                          
│                       │      │                  https://bugzilla.redhat.com/2531743                          
│                       │      │                  https://bugzilla.redhat.com/2531744                          
│                       │      │                  https://bugzilla.redhat.com/2531745                          
│                       │      │                  https://bugzilla.redhat.com/2531746                          
│                       │      │                  https://bugzilla.redhat.com/2531747                          
│                       │      │                  https://bugzilla.redhat.com/2543797                          
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-81532.html          
│                       │      │                  https://github.com/PCRE2Project/pcre2/releases/tag/pcre2-10.4
│                       │      │                  8                                                            
│                       │      │                  https://github.com/PCRE2Project/pcre2/security/advisories/GHS
│                       │      │                  A-fmgr-6ggq-9859                                             
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-89158.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-81613.html         
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89158              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89158              
│                       │      ├ PublishedDate   : 2026-09-11T04:18:03.97Z 
│                       │      ╰ LastModifiedDate: 2026-09-16T19:23:41.45Z 
│                       ├ [49] ╭ VulnerabilityID : CVE-2026-89160 
│                       │      ├ PkgID           : libpcre2-8-0@10.46-1build1 
│                       │      ├ PkgName         : libpcre2-8-0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpcre2-8-0@10.46-1build1?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c9d0d8772a6e5e1d 
│                       │      ├ InstalledVersion: 10.46-1build1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89160 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7b728965bcffc2648993a4e65cef45afd9c60c1133f3faaa8097d
│                       │      │                   36217a4f8ca 
│                       │      ├ Title           : pcre2: PCRE2: Denial of Service via out-of-bounds read
│                       │      │                   during invalid UTF matching 
│                       │      ├ Description     : PCRE2 before 10.48 has a pcre2_match out-of-bounds read
│                       │      │                   during the PCRE2_MATCH_INVALID_UTF matching of an invalid
│                       │      │                   UTF subject. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ azure      : 1 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:81532             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89160        
│                       │      │                  https://bugzilla.redhat.com/2528993                          
│                       │      │                  https://bugzilla.redhat.com/2531743                          
│                       │      │                  https://bugzilla.redhat.com/2531744                          
│                       │      │                  https://bugzilla.redhat.com/2531745                          
│                       │      │                  https://bugzilla.redhat.com/2531746                          
│                       │      │                  https://bugzilla.redhat.com/2531747                          
│                       │      │                  https://bugzilla.redhat.com/2543797                          
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-81532.html          
│                       │      │                  https://github.com/PCRE2Project/pcre2/releases/tag/pcre2-10.4
│                       │      │                  8                                                            
│                       │      │                  https://github.com/PCRE2Project/pcre2/security/advisories/GHS
│                       │      │                  A-9qww-pwc4-77qq                                             
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-89160.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-81532.html         
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89160              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89160              
│                       │      ├ PublishedDate   : 2026-09-11T04:18:04.343Z 
│                       │      ╰ LastModifiedDate: 2026-09-16T19:15:29.443Z 
│                       ├ [50] ╭ VulnerabilityID : CVE-2026-89161 
│                       │      ├ PkgID           : libpcre2-8-0@10.46-1build1 
│                       │      ├ PkgName         : libpcre2-8-0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpcre2-8-0@10.46-1build1?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c9d0d8772a6e5e1d 
│                       │      ├ InstalledVersion: 10.46-1build1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89161 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e98e83cbe96a257fe98a271b1b8d0f3544909bae968752b422edd
│                       │      │                   c3ba45ffff5 
│                       │      ├ Title           : pcre2: PCRE2: Memory corruption vulnerability in
│                       │      │                   pcre2_jit_match 
│                       │      ├ Description     : In PCRE2 before 10.48, pcre2_jit_match mishandles a
│                       │      │                   previously copied subject being passed in as a context. An
│                       │      │                   incorrect free operation can occur. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-590
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ nvd        : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.8 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:81532             
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89161        
│                       │      │                  https://bugzilla.redhat.com/2528993                          
│                       │      │                  https://bugzilla.redhat.com/2531743                          
│                       │      │                  https://bugzilla.redhat.com/2531744                          
│                       │      │                  https://bugzilla.redhat.com/2531745                          
│                       │      │                  https://bugzilla.redhat.com/2531746                          
│                       │      │                  https://bugzilla.redhat.com/2531747                          
│                       │      │                  https://bugzilla.redhat.com/2543797                          
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-81532.html          
│                       │      │                  https://github.com/PCRE2Project/pcre2/commit/1dcd0cf42a6a7cb6
│                       │      │                  2cc9a7c024196733abcfda95%20%28pcre2-10.48-RC1%29             
│                       │      │                  https://github.com/PCRE2Project/pcre2/pull/937               
│                       │      │                                                                               
│                       │      │                  https://github.com/PCRE2Project/pcre2/releases/tag/pcre2-10.4
│                       │      │                  8                                                            
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-89161.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-81532.html         
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89161              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89161              
│                       │      ├ PublishedDate   : 2026-09-11T04:18:04.47Z 
│                       │      ╰ LastModifiedDate: 2026-09-16T19:10:47.78Z 
│                       ├ [51] ╭ VulnerabilityID : CVE-2026-89162 
│                       │      ├ PkgID           : libpcre2-8-0@10.46-1build1 
│                       │      ├ PkgName         : libpcre2-8-0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpcre2-8-0@10.46-1build1?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c9d0d8772a6e5e1d 
│                       │      ├ InstalledVersion: 10.46-1build1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-89162 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:cf6af3856d10823871fd30f76324990b17ae551b32ee4f1194033
│                       │      │                   d1bfd89d448 
│                       │      ├ Title           : pcre2: PCRE2: Information disclosure via
│                       │      │                   pcre2_serialize_encode 
│                       │      ├ Description     : In PCRE2 before 10.48, pcre2_serialize_encode might disclose
│                       │      │                    two bytes to an adversary, typically in a situation where
│                       │      │                   the access available to the adversary is already unsafe. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-669
│                       │      ├ VendorSeverity   ╭ nvd   : 1 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 3.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 2.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-89162        
│                       │      │                  https://github.com/PCRE2Project/pcre2/commit/edc111a6831591f6
│                       │      │                  8b5355a08cc9df8be8f35304%20%28pcre2-10.48-RC1%29             
│                       │      │                  https://github.com/PCRE2Project/pcre2/releases/tag/pcre2-10.4
│                       │      │                  8                                                            
│                       │      │                  https://github.com/PCRE2Project/pcre2/security/advisories/GHS
│                       │      │                  A-q7rw-r7qq-2hx6                                             
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-89162              
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-89162              
│                       │      ├ PublishedDate   : 2026-09-11T05:16:38.697Z 
│                       │      ╰ LastModifiedDate: 2026-09-16T18:56:28.643Z 
│                       ├ [52] ╭ VulnerabilityID : CVE-2026-107161 
│                       │      ├ PkgID           : libsasl2-2@2.1.28+dfsg1-9ubuntu3 
│                       │      ├ PkgName         : libsasl2-2 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsasl2-2@2.1.28%2Bdfsg1-9ubuntu3?arc
│                       │      │                  │       h=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : cb08e08f2a78be69 
│                       │      ├ InstalledVersion: 2.1.28+dfsg1-9ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-107161 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:bf1046b54d9d2ce6f0847900941a3382d18c92a5019bdd54b5400
│                       │      │                   dcb8358be43 
│                       │      ├ Title           : cyrus-sasl: Heap buffer overflow in cyrus-sasl
│                       │      │                   add_to_challenge() allows malicious server to crash or
│                       │      │                   compromise DIGEST-MD5 clients 
│                       │      ├ Description     : A heap-based buffer overflow flaw was found in Cyrus SASL.
│                       │      │                   The add_to_challenge() function in the DIGEST-MD5 plugin
│                       │      │                   computes the size of the buffer needed for a
│                       │      │                   challenge/response field before DIGEST-MD5 quoting is
│                       │      │                   applied, but does not recompute that size when quoting
│                       │      │                   (escaping special characters) makes the value longer. The
│                       │      │                   under-sized buffer is then passed to strcat(), causing a
│                       │      │                   heap-based out-of-bounds write whose size depends on
│                       │      │                   attacker-controlled input. A malicious or on-path DIGEST-MD5
│                       │      │                    (or HTTP Digest) server can trigger this flaw in a
│                       │      │                   connecting client by supplying a crafted challenge field,
│                       │      │                   such as realm or nonce, most likely resulting in a crash of
│                       │      │                   the client application. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-122
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                               
│                       │      │                  ────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/10/09/20
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-107161  
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2460420     
│                       │      │                  https://github.com/cyrusimap/cyrus-sasl/pull/892        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-107161        
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-107161        
│                       │      ├ PublishedDate   : 2026-10-07T20:17:10.977Z 
│                       │      ╰ LastModifiedDate: 2026-10-10T03:17:05.307Z 
│                       ├ [53] ╭ VulnerabilityID : CVE-2026-107161 
│                       │      ├ PkgID           : libsasl2-modules@2.1.28+dfsg1-9ubuntu3 
│                       │      ├ PkgName         : libsasl2-modules 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsasl2-modules@2.1.28%2Bdfsg1-9ubunt
│                       │      │                  │       u3?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c233aa9b84243212 
│                       │      ├ InstalledVersion: 2.1.28+dfsg1-9ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-107161 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:888fcf56961ea88698c6400477cda119131526be4e98c2c01b9e6
│                       │      │                   97c5890c06b 
│                       │      ├ Title           : cyrus-sasl: Heap buffer overflow in cyrus-sasl
│                       │      │                   add_to_challenge() allows malicious server to crash or
│                       │      │                   compromise DIGEST-MD5 clients 
│                       │      ├ Description     : A heap-based buffer overflow flaw was found in Cyrus SASL.
│                       │      │                   The add_to_challenge() function in the DIGEST-MD5 plugin
│                       │      │                   computes the size of the buffer needed for a
│                       │      │                   challenge/response field before DIGEST-MD5 quoting is
│                       │      │                   applied, but does not recompute that size when quoting
│                       │      │                   (escaping special characters) makes the value longer. The
│                       │      │                   under-sized buffer is then passed to strcat(), causing a
│                       │      │                   heap-based out-of-bounds write whose size depends on
│                       │      │                   attacker-controlled input. A malicious or on-path DIGEST-MD5
│                       │      │                    (or HTTP Digest) server can trigger this flaw in a
│                       │      │                   connecting client by supplying a crafted challenge field,
│                       │      │                   such as realm or nonce, most likely resulting in a crash of
│                       │      │                   the client application. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-122
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                               
│                       │      │                  ────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/10/09/20
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-107161  
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2460420     
│                       │      │                  https://github.com/cyrusimap/cyrus-sasl/pull/892        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-107161        
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-107161        
│                       │      ├ PublishedDate   : 2026-10-07T20:17:10.977Z 
│                       │      ╰ LastModifiedDate: 2026-10-10T03:17:05.307Z 
│                       ├ [54] ╭ VulnerabilityID : CVE-2026-107161 
│                       │      ├ PkgID           : libsasl2-modules-db@2.1.28+dfsg1-9ubuntu3 
│                       │      ├ PkgName         : libsasl2-modules-db 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsasl2-modules-db@2.1.28%2Bdfsg1-9ub
│                       │      │                  │       untu3?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 1e70df2d0651e5a4 
│                       │      ├ InstalledVersion: 2.1.28+dfsg1-9ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-107161 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:07f3241c7b98740b5719aa673b20b34ea3a9f4368019210702aac
│                       │      │                   014f8f7a133 
│                       │      ├ Title           : cyrus-sasl: Heap buffer overflow in cyrus-sasl
│                       │      │                   add_to_challenge() allows malicious server to crash or
│                       │      │                   compromise DIGEST-MD5 clients 
│                       │      ├ Description     : A heap-based buffer overflow flaw was found in Cyrus SASL.
│                       │      │                   The add_to_challenge() function in the DIGEST-MD5 plugin
│                       │      │                   computes the size of the buffer needed for a
│                       │      │                   challenge/response field before DIGEST-MD5 quoting is
│                       │      │                   applied, but does not recompute that size when quoting
│                       │      │                   (escaping special characters) makes the value longer. The
│                       │      │                   under-sized buffer is then passed to strcat(), causing a
│                       │      │                   heap-based out-of-bounds write whose size depends on
│                       │      │                   attacker-controlled input. A malicious or on-path DIGEST-MD5
│                       │      │                    (or HTTP Digest) server can trigger this flaw in a
│                       │      │                   connecting client by supplying a crafted challenge field,
│                       │      │                   such as realm or nonce, most likely resulting in a crash of
│                       │      │                   the client application. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-122
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References                                                               
│                       │      │                  ────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/10/09/20
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-107161  
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2460420     
│                       │      │                  https://github.com/cyrusimap/cyrus-sasl/pull/892        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-107161        
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-107161        
│                       │      ├ PublishedDate   : 2026-10-07T20:17:10.977Z 
│                       │      ╰ LastModifiedDate: 2026-10-10T03:17:05.307Z 
│                       ├ [55] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libsystemd0@259.5-0ubuntu3.4 
│                       │      ├ PkgName         : libsystemd0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsystemd0@259.5-0ubuntu3.4?arch=amd6
│                       │      │                  │       4&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 8e41c7d584057e32 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:8b9d9222edff3f5fa16ba782e1aa75cc4f1b0ba556a46d57a7f66
│                       │      │                   389977b76ac 
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
│                       │      ├ PublishedDate   : 2026-04-10T16:16:33.753Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:44:53.31Z 
│                       ├ [56] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libudev1@259.5-0ubuntu3.4 
│                       │      ├ PkgName         : libudev1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libudev1@259.5-0ubuntu3.4?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : db6ded6155f534fe 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:4209f1f014989c5b05ef8b45e8bf9f3eb9bb1f6fbd9c7bf3cb45a
│                       │      │                   68b4cfd9a77 
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
│                       │      ├ PublishedDate   : 2026-04-10T16:16:33.753Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:44:53.31Z 
│                       ├ [57] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : login.defs@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : login.defs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login.defs@4.17.4-2ubuntu3?arch=all&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : eaf648d5e4e975f7 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:585346cf2ec4f8213574c853fa46ddd0f85570509cfcc23d1b734
│                       │      │                   612b5fd90a4 
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
│                       │      │                  https://cert-portal.siemens.com/productcert/html/ssa-398330.h
│                       │      │                  tml                                                          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-56433
│                       │      │                                                                               
│                       │      │                  https://errata.almalinux.org/9/ALSA-2025-20559.html          
│                       │      │                                                                               
│                       │      │                  https://errata.rockylinux.org/RLSA-2025:20559                
│                       │      │                                                                               
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
│                       │      ├ PublishedDate   : 2024-12-26T09:15:07.267Z 
│                       │      ╰ LastModifiedDate: 2026-10-15T01:19:16.297Z 
│                       ├ [58] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : passwd@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : passwd 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/passwd@4.17.4-2ubuntu3?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : 12ffbe3e135ac553 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e57f8cd078599c70698a11f54bd2933447e94cc9a111f8aded508
│                       │      │                   d2fb12d6627 
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
│                       │      │                  https://cert-portal.siemens.com/productcert/html/ssa-398330.h
│                       │      │                  tml                                                          
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-56433
│                       │      │                                                                               
│                       │      │                  https://errata.almalinux.org/9/ALSA-2025-20559.html          
│                       │      │                                                                               
│                       │      │                  https://errata.rockylinux.org/RLSA-2025:20559                
│                       │      │                                                                               
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
│                       │      ├ PublishedDate   : 2024-12-26T09:15:07.267Z 
│                       │      ╰ LastModifiedDate: 2026-10-15T01:19:16.297Z 
│                       ├ [59] ╭ VulnerabilityID : CVE-2026-35341 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35341 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d627781c3c4c3d9ae6cf12ec61b8996628c00c5630384629c767d
│                       │      │                   a1485662d8e 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:36.06Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:25.5Z 
│                       ├ [60] ╭ VulnerabilityID : CVE-2026-35344 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35344 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7daedd1bb2c1ea67900ccb0e8148a82283ea986d5f72ee06c2cb4
│                       │      │                   f0241d1dfe1 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:36.49Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:25.833Z 
│                       ├ [61] ╭ VulnerabilityID : CVE-2026-35345 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35345 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7bd452853c16e28d965fdaa6d06cf7294987e91b5c9dc6fc339ea
│                       │      │                   9bd14630b93 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:36.627Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:25.943Z 
│                       ├ [62] ╭ VulnerabilityID : CVE-2026-35348 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35348 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d2a2998202bb56284fea621603a2b952d6bfecbb4250910529f0a
│                       │      │                   1c52ba72b35 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.04Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.27Z 
│                       ├ [63] ╭ VulnerabilityID : CVE-2026-35350 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35350 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:fbdd50664a221b3745b2c093a5c62c3d457f8d1b7c5245884c6ee
│                       │      │                   122004ae28d 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.327Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.48Z 
│                       ├ [64] ╭ VulnerabilityID : CVE-2026-35351 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35351 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:95cb3bf4aeb44546ecc37621506241efb0aa427404d28364283f1
│                       │      │                   b14ff205161 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.457Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.587Z 
│                       ├ [65] ╭ VulnerabilityID : CVE-2026-35352 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35352 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:feb0d2f4efa82abcf78ecb1579ffb40657757502dd6e6407ac0ff
│                       │      │                   7a212d8371d 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.597Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.69Z 
│                       ├ [66] ╭ VulnerabilityID : CVE-2026-35354 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35354 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0e8d6cd02fa68a835499fbef4d22cb3b1318e7b2e28a2d0772d69
│                       │      │                   106f4a7efbf 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.867Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.907Z 
│                       ├ [67] ╭ VulnerabilityID : CVE-2026-35357 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35357 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6b3045713c61037ad81f3de37b598d66425e8816c178c75509a5a
│                       │      │                   2ce259af430 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:38.267Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.223Z 
│                       ├ [68] ╭ VulnerabilityID : CVE-2026-35359 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35359 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6f133456c38d28cc442629e3a081ff4b389ff8d704cb550f6efd1
│                       │      │                   050f1f996bc 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:38.537Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.437Z 
│                       ├ [69] ╭ VulnerabilityID : CVE-2026-35360 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35360 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3673ea1543ebcca96696a42df55bab917e92ada5b3a188250191d
│                       │      │                   57f4ca08f0d 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:38.673Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.543Z 
│                       ├ [70] ╭ VulnerabilityID : CVE-2026-35363 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35363 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:33dafdfdd81286a9ae70c6f78112572b67c7bac5ee317a47bb123
│                       │      │                   61c333392b8 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:39.12Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.867Z 
│                       ├ [71] ╭ VulnerabilityID : CVE-2026-35364 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35364 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:1c9d9230ad433ac3f64add9a4ea9756b56261a8ebd537af99cd2a
│                       │      │                   daca089d5e6 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:39.737Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.97Z 
│                       ├ [72] ╭ VulnerabilityID : CVE-2026-35367 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35367 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a53c1ec937983d7bcd45f45b14a9ac35bbc45f17740f41b1d6ff8
│                       │      │                   1a23af1238b 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.423Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.297Z 
│                       ├ [73] ╭ VulnerabilityID : CVE-2026-35368 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35368 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:fca991139bb42a6b4eed4cfb59c7da8d5b296dfc9b20dac1c5908
│                       │      │                   d1df1eab8c0 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.56Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.4Z 
│                       ├ [74] ╭ VulnerabilityID : CVE-2026-35370 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35370 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:fa5a61c03e4a8ba8e72c717657a576165fab43666707760d40f10
│                       │      │                   7e019b59575 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.833Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.613Z 
│                       ├ [75] ╭ VulnerabilityID : CVE-2026-35371 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35371 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:54dc0688d3e9d74ee814f774fc33262cd10521bdb9d269bb8e6ef
│                       │      │                   0d597c826e8 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.987Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.723Z 
│                       ├ [76] ╭ VulnerabilityID : CVE-2026-35373 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35373 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e35e3a8953f81260d332e0026e0d49ac9ed7bb0a37750a4385c6f
│                       │      │                   4ea93d62554 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:41.997Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.933Z 
│                       ├ [77] ╭ VulnerabilityID : CVE-2026-35374 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6e72c497d400ded0765ba94cdec7b92f4cb292f13e5396506230e
│                       │      │                   9e0765976de 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:42.127Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:29.04Z 
│                       ├ [78] ╭ VulnerabilityID : CVE-2026-35377 
│                       │      ├ PkgID           : rust-coreutils@0.10.0-1ubuntu2~26.04.1 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.10.0-1ubuntu2~26.04.1
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 6c642eee022d7f9d 
│                       │      ├ InstalledVersion: 0.10.0-1ubuntu2~26.04.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35377 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:78b64799bd2deca0e09014f99996633a077c68f7fe9db72d588fe
│                       │      │                   3e1c11fc785 
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
│                       │      ├ PublishedDate   : 2026-04-22T17:16:42.577Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:29.357Z 
│                       ├ [79] ╭ VulnerabilityID : CVE-2026-18477 
│                       │      ├ PkgID           : tar@1.35+dfsg-4ubuntu0.4 
│                       │      ├ PkgName         : tar 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-4ubuntu0.4?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 5867f93e7d45b368 
│                       │      ├ InstalledVersion: 1.35+dfsg-4ubuntu0.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18477 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5b9ef380f32c61e7862bfc17481680b126ee72e6af228d637bc07
│                       │      │                   a7796b4bea7 
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
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:70390             
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
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-70390.html         
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18477              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18477              
│                       │      ├ PublishedDate   : 2026-08-03T17:16:33.897Z 
│                       │      ╰ LastModifiedDate: 2026-09-22T22:17:11.233Z 
│                       ├ [80] ╭ VulnerabilityID : CVE-2026-18508 
│                       │      ├ PkgID           : tar@1.35+dfsg-4ubuntu0.4 
│                       │      ├ PkgName         : tar 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-4ubuntu0.4?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 5867f93e7d45b368 
│                       │      ├ InstalledVersion: 1.35+dfsg-4ubuntu0.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                       │      │                  │         da61233cbddb495af9f2 
│                       │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                       │      │                            d6dd2c7c69455d167496 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-18508 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:24b44479ae6effde54845c446e9f0a82897d1c620e413ee4c4d75
│                       │      │                   eadca3af8bd 
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
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:70390             
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
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-70390.html         
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-18508              
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-18508              
│                       │      ├ PublishedDate   : 2026-08-03T16:16:28.387Z 
│                       │      ╰ LastModifiedDate: 2026-09-22T22:17:11.493Z 
│                       ╰ [81] ╭ VulnerabilityID : CVE-2026-85091 
│                              ├ PkgID           : zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu3.1 
│                              ├ PkgName         : zlib1g 
│                              ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/zlib1g@1.3.dfsg%2Breally1.3.1-1ubuntu3
│                              │                  │       .1?arch=amd64&distro=ubuntu-26.04&epoch=1 
│                              │                  ╰ UID : a4f0bcc5ee12eaad 
│                              ├ InstalledVersion: 1:1.3.dfsg+really1.3.1-1ubuntu3.1 
│                              ├ Status          : affected 
│                              ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
│                              │                  │         da61233cbddb495af9f2 
│                              │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
│                              │                            d6dd2c7c69455d167496 
│                              ├ SeveritySource  : ubuntu 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-85091 
│                              ├ DataSource       ╭ ID  : ubuntu 
│                              │                  ├ Name: Ubuntu CVE Tracker 
│                              │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                              ├ Fingerprint     : sha256:38caadb4c511be3f3d62f55b810afbda8a14c857c833a367cdd73
│                              │                   2f5e450e11b 
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
│                              ├ PublishedDate   : 2026-09-03T13:06:20.573Z 
│                              ╰ LastModifiedDate: 2026-09-09T20:41:07.123Z 
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
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                        │      │                  │         da61233cbddb495af9f2 
                        │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                        │      │                            d6dd2c7c69455d167496 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78667 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:a7d0ceb929f4d9c2fa91f7d2eb65e03b7b60ed52df2236948329d
                        │      │                   5a063c06313 
                        │      ├ Title           : net/http: golang: golang: Denial of Service via crafted HTTP
                        │      │                    Range headers 
                        │      ├ Description     : When parsing a Range header containing a large number of
                        │      │                   small ranges, FileServer(FS), ServeContent, and
                        │      │                   ServeFile(FS) can consume an excessive amount of CPU. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-770
                        │      ├ VendorSeverity   ─ redhat: 3 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                           │           /A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-78667    
                        │      │                  https://go.dev/cl/847309                                 
                        │      │                  https://go.dev/issue/81858                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-78667          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6609                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78667          
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.88Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:49.69Z 
                        ├ [1]  ╭ VulnerabilityID : CVE-2026-78669 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6611
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                        │      │                  │         da61233cbddb495af9f2 
                        │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                        │      │                            d6dd2c7c69455d167496 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78669 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:9274acef51456d7945c2f204e8413386e13212aa283976ca41209
                        │      │                   a17151d0c24 
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
                        │      ├ VendorSeverity   ─ redhat: 3 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                           │           /A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-78669    
                        │      │                  https://go.dev/cl/847186                                 
                        │      │                  https://go.dev/cl/847308                                 
                        │      │                  https://go.dev/issue/81742                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-78669          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6611                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78669          
                        │      ├ PublishedDate   : 2026-10-08T23:17:04.01Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:49.857Z 
                        ├ [2]  ╭ VulnerabilityID : CVE-2026-97031 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6607
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                        │      │                  │         da61233cbddb495af9f2 
                        │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                        │      │                            d6dd2c7c69455d167496 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97031 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:734ba265ea310e47cc380c6b8dfa191384f31575d3de714ffc822
                        │      │                   7a24701a559 
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
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                        │      │                  │         da61233cbddb495af9f2 
                        │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                        │      │                            d6dd2c7c69455d167496 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56866 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:bfe8d097e50aadaa82be42ddf6c452f0a4b676ebea3c11c998396
                        │      │                   775123ceb51 
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
                        │      ├ VendorSeverity   ─ redhat: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-56866    
                        │      │                  https://go.dev/cl/847306                                 
                        │      │                  https://go.dev/issue/81740                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-56866          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6605                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-56866          
                        │      ├ PublishedDate   : 2026-10-08T23:17:01.62Z 
                        │      ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
                        ├ [4]  ╭ VulnerabilityID : CVE-2026-78663 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6612
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                        │      │                  │         da61233cbddb495af9f2 
                        │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                        │      │                            d6dd2c7c69455d167496 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78663 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:81aa6accdea1e1c84d5ae8263ed91499fffa0ddcecdd16f69a4c6
                        │      │                   b33228edbed 
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
                        │      ├ VendorSeverity   ─ redhat: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                           │           /A:L 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-78663    
                        │      │                  https://go.dev/cl/847187                                 
                        │      │                  https://go.dev/cl/847310                                 
                        │      │                  https://go.dev/issue/81743                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-78663          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6612                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-78663          
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.647Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:49.42Z 
                        ├ [5]  ╭ VulnerabilityID : CVE-2026-94439 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6613
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                        │      │                  │         da61233cbddb495af9f2 
                        │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                        │      │                            d6dd2c7c69455d167496 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94439 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:4faa1b4699421c57a38313f8555529ff93f1a59f8b3b2a93e0bd3
                        │      │                   92e83d2419f 
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
                        │      ├ VendorSeverity   ─ redhat: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://access.redhat.com/security/cve/CVE-2026-94439    
                        │      │                  https://go.dev/cl/847311                                 
                        │      │                  https://go.dev/issue/81744                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-94439          
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6613                     
                        │      │                  https://www.cve.org/CVERecord?id=CVE-2026-94439          
                        │      ├ PublishedDate   : 2026-10-08T23:17:04.76Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:50.703Z 
                        ├ [6]  ╭ VulnerabilityID : CVE-2026-94448 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6599
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                        │      │                  │         da61233cbddb495af9f2 
                        │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                        │      │                            d6dd2c7c69455d167496 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94448 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:325dad4a4913701fe212c8ff8a5e4dba62a0a6a60f3b9229bce81
                        │      │                   56ad7ed4046 
                        │      ├ Title           : html/template: golang: golang: cross-site scripting via
                        │      │                   consecutive expressions in JavaScript template literals 
                        │      ├ Description     : When a JavaScript template literal contains consecutive
                        │      │                   expressions, the context tracking state was not properly
                        │      │                   reset upon entering a new expression. We now ensure that
                        │      │                   template-literal expression entries correctly reset context
                        │      │                   variables so all subsequent regular expression literals are
                        │      │                   accurately recognized and escaped. 
                        │      ├ Severity        : MEDIUM 
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
                        │      ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
                        ├ [7]  ╭ VulnerabilityID : CVE-2026-97032 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6617
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                        │      │                  │         da61233cbddb495af9f2 
                        │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                        │      │                            d6dd2c7c69455d167496 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97032 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:701e951ea195cc3d1c39808178d9495d9c05ccfab7ecfb555ced9
                        │      │                   abd5e8da2dd 
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
                        │      ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
                        ├ [8]  ╭ VulnerabilityID : CVE-2026-56857 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6604
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                        │      │                  │         da61233cbddb495af9f2 
                        │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                        │      │                            d6dd2c7c69455d167496 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-56857 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:9cfd7f014d0a95e7e903a78408aefc267ea7cb38ee74e29983746
                        │      │                   6e069b63dda 
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
                        ├ [9]  ╭ VulnerabilityID : CVE-2026-78659 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6603
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                        │      │                  │         da61233cbddb495af9f2 
                        │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                        │      │                            d6dd2c7c69455d167496 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78659 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:8a49097aac4a78e2aeb4bb93c8cafd06411f59fb7ed9bf8247f0e
                        │      │                   a9e1a7960d4 
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
                        │      ├ Severity        : UNKNOWN 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-405
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://go.dev/cl/847185                                 
                        │      │                  https://go.dev/cl/847314                                 
                        │      │                  https://go.dev/issue/81857                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://groups.google.com/g/golang-announce/c/ZPwCyRUuGBs
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6603                     
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.27Z 
                        │      ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
                        ├ [10] ╭ VulnerabilityID : CVE-2026-78660 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6610
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                        │      │                  │         da61233cbddb495af9f2 
                        │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                        │      │                            d6dd2c7c69455d167496 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-78660 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:f03afce57ed018df3d16148e2cb831593f9231abd15ae768b0f95
                        │      │                   fde467bcd64 
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
                        │      ├ Severity        : UNKNOWN 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-444
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://go.dev/cl/835145                                 
                        │      │                  https://go.dev/cl/836385                                 
                        │      │                  https://go.dev/issue/81115                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6610                     
                        │      ├ PublishedDate   : 2026-10-08T23:17:03.51Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:49.243Z 
                        ├ [11] ╭ VulnerabilityID : CVE-2026-94440 
                        │      ├ VendorIDs                    
                        │      │                  ────────────
                        │      │                  GO-2026-6608
                        │      ├ PkgID           : stdlib@v1.26.7 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                        │      │                  ╰ UID : 69015e289f0fffad 
                        │      ├ InstalledVersion: v1.26.7 
                        │      ├ FixedVersion    : 1.26.9, 1.27.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                        │      │                  │         da61233cbddb495af9f2 
                        │      │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                        │      │                            d6dd2c7c69455d167496 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-94440 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:2ccc42c01d6e51547e557f939be8b715b4beda4a3e6e0a233cf46
                        │      │                   a9faae20c0e 
                        │      ├ Title           : Parsing a multipart form can bypass memory limits and read
                        │      │                   an arbitrar ... 
                        │      ├ Description     : Parsing a multipart form can bypass memory limits and read
                        │      │                   an arbitrarily long line into memory when the remaining
                        │      │                   limit at the start of a part is less than 400 bytes. 
                        │      ├ Severity        : UNKNOWN 
                        │      ├ CweIDs                  
                        │      │                  ───────
                        │      │                  CWE-770
                        │      ├ References                                                                
                        │      │                  ─────────────────────────────────────────────────────────
                        │      │                  https://go.dev/cl/847307                                 
                        │      │                  https://go.dev/issue/81741                               
                        │      │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                        │      │                  https://pkg.go.dev/vuln/GO-2026-6608                     
                        │      ├ PublishedDate   : 2026-10-08T23:17:04.917Z 
                        │      ╰ LastModifiedDate: 2026-10-09T17:16:50.907Z 
                        ╰ [12] ╭ VulnerabilityID : CVE-2026-97030 
                               ├ VendorIDs                    
                               │                  ────────────
                               │                  GO-2026-6600
                               ├ PkgID           : stdlib@v1.26.7 
                               ├ PkgName         : stdlib 
                               ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.7 
                               │                  ╰ UID : 69015e289f0fffad 
                               ├ InstalledVersion: v1.26.7 
                               ├ FixedVersion    : 1.26.9, 1.27.2 
                               ├ Status          : fixed 
                               ├ Layer            ╭ Digest: sha256:bc17eac1246b2dfb5613d20b0d4ec56ef57db35ed3aa
                               │                  │         da61233cbddb495af9f2 
                               │                  ╰ DiffID: sha256:5c9386e59fc4cc43fd1019a5c4ffe5a94f608423fd65
                               │                            d6dd2c7c69455d167496 
                               ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97030 
                               ├ DataSource       ╭ ID  : govulndb 
                               │                  ├ Name: The Go Vulnerability Database 
                               │                  ╰ URL : https://pkg.go.dev/vuln/ 
                               ├ Fingerprint     : sha256:532b9de74a35ed3224abe3d1718553969cc964da8142ff3930f02
                               │                   dd02deebb82 
                               ├ Title           : A trusted template author may have previously written a
                               │                   valid template ... 
                               ├ Description     : A trusted template author may have previously written a
                               │                   valid template wherein the use of the 'yield' keyword would
                               │                   not be correctly escaped. We now ensure that valid keyword
                               │                   uses are escaped and non-keyword uses are not escaped. 
                               ├ Severity        : UNKNOWN 
                               ├ References                                                                
                               │                  ─────────────────────────────────────────────────────────
                               │                  https://go.dev/cl/840925                                 
                               │                  https://go.dev/issue/81823                               
                               │                  https://groups.google.com/g/golang-announce/c/U2fTuyDJznI
                               │                  https://pkg.go.dev/vuln/GO-2026-6600                     
                               ├ PublishedDate   : 2026-10-08T23:17:05.91Z 
                               ╰ LastModifiedDate: 2026-10-09T16:35:35.9Z 
```
