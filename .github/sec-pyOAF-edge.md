```yaml
╭ [0] ╭ Target         : openaf/pyoaf:edge (alpine 3.24.1) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-11352 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-11352 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:254876f9f2c11e0672dbab4884547ded35a968263b0024208462d
│                       │      │                   b0705f0ee22 
│                       │      ├ Title           : curl: libcurl: curl/libcurl: Remote denial of service via
│                       │      │                   QUIC UDP receive function vulnerability 
│                       │      ├ Description     : An issue in curl’s QUIC UDP receive function allows a
│                       │      │                   malicious HTTP/3 server
│                       │      │                   to trigger a remote denial of service against a curl or
│                       │      │                   libcurl client.
│                       │      │                   Because the helper function discards zero-length UDP
│                       │      │                   datagrams before counting
│                       │      │                   them toward the per-call packet budget, a connected QUIC
│                       │      │                   peer can continuously
│                       │      │                   stream empty datagrams to indefinitely stall the client. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-835 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-11352 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-11352.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-11352.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-11352.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3783438 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-11352 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-11352 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:23.693Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T18:01:19.013Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-11586 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-11586 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:5ae7b5e0bab372a6e2ffcf9302d245f9b5df1f33c55ba43a66266
│                       │      │                   b6231d0c855 
│                       │      ├ Title           : curl: curl: Denial of Service via WebSocket PING flood 
│                       │      ├ Description     : By default, curl automatically responds to WebSocket PING
│                       │      │                   frames. Because curl
│                       │      │                   lacks an upper bound on memory allocation for unacknowledged
│                       │      │                    frames, a
│                       │      │                   malicious server can exhaust all available memory by
│                       │      │                   flooding curl with rapid,
│                       │      │                   sequential PING messages. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-11586 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-11586.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-11586.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-11586.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3788931 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-11586 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-11586 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:23.883Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T17:59:46.92Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-12064 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-12064 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:b741dfe305c7f61869c3860675c86e7b1f7118249e991d1750e0b
│                       │      │                   9870d5ae9e1 
│                       │      ├ Title           : curl: curl: SSH host verification bypass when using
│                       │      │                   schemeless URLs with SFTP/SCP 
│                       │      ├ Description     : When a user invokes curl using a schemeless URL combined
│                       │      │                   with
│                       │      │                   `--proto-default` sftp (or scp), a disconnect occurs between
│                       │      │                    the tool layer
│                       │      │                   and libcurl. The tool layer incorrectly infers the URL
│                       │      │                   scheme, which
│                       │      │                   erroneously bypasses the initialization of critical SSH
│                       │      │                   security options like
│                       │      │                   CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 and
│                       │      │                   CURLOPT_SSH_KNOWNHOSTS. Conversely, the
│                       │      │                   libcurl runtime successfully honors CURLOPT_DEFAULT_PROTOCOL
│                       │      │                    and establishes
│                       │      │                   the connection via SFTP/SCP as specified. Because the tool
│                       │      │                   layer skipped the
│                       │      │                   security configuration, these SSH host verification options
│                       │      │                   are silently
│                       │      │                   omitted, causing curl to connect to an unverified SSH remote
│                       │      │                    host without
│                       │      │                   throwing an error. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-295 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-12064 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-12064.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-12064.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-12064.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3797526 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-12064 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-12064 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:24.217Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T19:43:11.187Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-8286 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8286 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e1c5c9413ade66786b323a172db1de8652ef974bc419f1ee9fb76
│                       │      │                   6cc79e64ce1 
│                       │      ├ Title           : curl: curl: Insecure connection establishment due to TLS
│                       │      │                   configuration mismatch 
│                       │      ├ Description     : A vulnerability exists where a new transfer that uses
│                       │      │                   STARTTLS to upgrade the
│                       │      │                   connection might reuse an existing live connection even
│                       │      │                   though the TLS
│                       │      │                   configuration mismatches so it should not. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-295 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 8.1 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-8286 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-8286.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8286.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-8286.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3718195 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-8286 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-8286 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:24.453Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T19:42:11.24Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-8925 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8925 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:fe42b9fb308f9c66c1e5303199e1401414259367381ac1ee1691f
│                       │      │                   71365ddf90d 
│                       │      ├ Title           : curl: curl: Double-free vulnerability in SASL authentication 
│                       │      ├ Description     : The curl logic that works with SASL authentication could end
│                       │      │                    up cleaning up
│                       │      │                   the GSASL context *twice* without clearing the pointer in
│                       │      │                   between, making it
│                       │      │                   `free()` the same pointer twice. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-415 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 8.1 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-8925 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-8925.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8925.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-8925.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3735193 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-8925 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-8925 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:24.95Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T23:04:29.69Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-8927 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8927 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:f4d27edbe4f1837b0553cc5e401f2bcbd3ab4b68b8021d4311fcd
│                       │      │                   c548165f401 
│                       │      ├ Title           : libcurl: libcurl: Information disclosure due to uncleared
│                       │      │                   proxy authentication state 
│                       │      ├ Description     : When reusing a libcurl handle for sequential transfers
│                       │      │                   driven by
│                       │      │                   environment-variable proxy configuration, libcurl fails to
│                       │      │                   clear the proxy
│                       │      │                   authentication state between requests. Specifically, if the
│                       │      │                   initial transfer
│                       │      │                   authenticates against `proxyA` using Digest auth, a
│                       │      │                   subsequent transfer routed
│                       │      │                   through `proxyB` erroneously leaks the
│                       │      │                   `Proxy-Authorization:` header intended
│                       │      │                   solely for `proxyA`. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-294 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-8927 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-8927.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8927.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-8927.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3744543 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-8927 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-8927 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.123Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T23:21:03.53Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-8932 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8932 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:efcbb0ac0f6273488f843b70ebea83d589da54885e9d11fac39b2
│                       │      │                   2466b2bfcad 
│                       │      ├ Title           : libcurl: libcurl: Security feature bypass due to improper
│                       │      │                   mTLS connection reuse 
│                       │      ├ Description     : libcurl would reuse a previously created connection even
│                       │      │                   when some mTLS config
│                       │      │                   related option had been changed that should have prohibited
│                       │      │                   reuse.
│                       │      │                   
│                       │      │                   libcurl keeps previously used connections in a connection
│                       │      │                   pool for subsequent
│                       │      │                   transfers to reuse if one of them matches the setup.
│                       │      │                   However, some TLS
│                       │      │                   settings related to client certificates were left out from
│                       │      │                   the configuration
│                       │      │                   match checks, making them match too easily. In particular
│                       │      │                   options related to
│                       │      │                   the private key. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ redhat: 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-8932 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-8932.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8932.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3733910 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-8932 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-8932 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.363Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T23:18:32.137Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-9079 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-9079 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:3091ce68983cee3caf6bf789a477457e01b7d91494dc75dca3c42
│                       │      │                   3175fc28ddb 
│                       │      ├ Title           : libcurl: libcurl: Information disclosure due to failure to
│                       │      │                   clear proxy authentication credentials 
│                       │      ├ Description     : libcurl had a flaw that when instructed to clear proxy
│                       │      │                   authentication
│                       │      │                   credentials which made it not do so, leaving the old
│                       │      │                   credentials around to get
│                       │      │                   used for subsequent transfers that should not know nor use
│                       │      │                   them. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-522 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-9079 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-9079.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-9079.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-9079.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3750295 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-9079 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-9079 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.62Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T15:05:55.933Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-9080 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-9080 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:120e1b3eccadf7b60ae6795fb3d3cb50167d601f9fc89a9ecb423
│                       │      │                   1f878d89b8c 
│                       │      ├ Title           : libcurl: libcurl: Use-after-free via curl_easy_pause() in
│                       │      │                   CURLMOPT_SOCKETFUNCTION callback 
│                       │      ├ Description     : Calling `curl_easy_pause()` within the event-based
│                       │      │                   `CURLMOPT_SOCKETFUNCTION`
│                       │      │                   callback triggers a use-after-free vulnerability, where
│                       │      │                   libcurl attempts to
│                       │      │                   store a flag using a dangling struct pointer immediately
│                       │      │                   after that pointer's
│                       │      │                   memory has been freed. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-416 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 7.3 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-9080 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-9080.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-9080.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-9080.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3749204 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-9080 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-9080 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.713Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T15:05:26.53Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-9545 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-9545 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:2cbbe4ab9e75a9d9718fd64dd3272a7052d93df0dca770e6069cc
│                       │      │                   3419a0de4a2 
│                       │      ├ Title           : libcurl: libcurl: Information disclosure via cached SSL
│                       │      │                   session and early data 
│                       │      ├ Description     : In this scenario, libcurl first uses a proper HTTP/3 server
│                       │      │                   for the initial
│                       │      │                   transfers, and when it makes a second transfer to the same
│                       │      │                   site it has been
│                       │      │                   replaced by the attacker's impostor machine - without a
│                       │      │                   valid certificate.
│                       │      │                   
│                       │      │                   When libcurl returns to the hostname the second time with a
│                       │      │                   cached SSL session
│                       │      │                   (`CURLOPT_SSL_SESSIONID_CACHE` is not disabled) and early
│                       │      │                   data enabled (the
│                       │      │                   `CURLSSLOPT_EARLYDATA` bit is set in `CURLOPT_SSL_OPTIONS`),
│                       │      │                    libcurl might
│                       │      │                   send off the second request's bytes on that new connection
│                       │      │                   *before* enforcing
│                       │      │                   the certificate verification failure. Potentially leaking
│                       │      │                   sensitive
│                       │      │                   information. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-9545 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-9545.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-9545.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-9545.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3752888 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-9545 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-9545 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.807Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T15:03:56.92Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-9546 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-9546 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8dde2ae7d79a6b85f59ae20326468846eb681888231e0215ea38b
│                       │      │                   88717ee8182 
│                       │      ├ Title           : libcurl: libcurl: Information disclosure due to persistent
│                       │      │                   Referer header 
│                       │      ├ Description     : A vulnerability in libcurl caused the HTTP `Referer:` header
│                       │      │                    to persist even
│                       │      │                   when explicitly cleared. While the documentation states that
│                       │      │                    passing NULL to
│                       │      │                   `CURLOPT_REFERER` suppresses the header, the option failed
│                       │      │                   to clear the
│                       │      │                   internal state. As a result the previous referrer string was
│                       │      │                    erroneously
│                       │      │                   reused and sent in subsequent requests, potentially leaking
│                       │      │                   sensitive
│                       │      │                   information to unintended servers. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ redhat: 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-9546 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-9546.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-9546.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3754343 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-9546 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-9546 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.893Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T14:53:26.517Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-9547 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-9547 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e2a0e084a15a64d3a05a685ee4a373510e26d466c8c7d289624ca
│                       │      │                   f365d0186e8 
│                       │      ├ Title           : curl: curl: Man-in-the-middle attack via SSH host key bypass 
│                       │      ├ Description     : When a libcurl-based application performs transfers via
│                       │      │                   `SCP://` or `SFTP://`
│                       │      │                   and utilizes the `CURLOPT_SSH_KEYFUNCTION` callback, it may
│                       │      │                   silently accept an
│                       │      │                   untrusted server. This vulnerability occurs when a server
│                       │      │                   presents a host key
│                       │      │                   type that does not match the specific key type already
│                       │      │                   recorded for that host
│                       │      │                   in the `known_hosts` file. Instead of rejecting the
│                       │      │                   mismatch, the callback
│                       │      │                   mechanism fails to properly enforce the restriction,
│                       │      │                   allowing the connection
│                       │      │                   to succeed without warning and risking a potential
│                       │      │                   man-in-the-middle attack. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-9547 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-9547.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-9547.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-9547.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3751712 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-9547 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-9547 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.99Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T14:52:29.503Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-8924 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8924 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:eeaf5ce05d7b625b121a8742b82af918a99430afa884d3bb05ce0
│                       │      │                   05f8484405d 
│                       │      ├ Title           : curl: curl: Cookie injection via malicious HTTP server using
│                       │      │                    super cookies 
│                       │      ├ Description     : A flaw in curl’s cookie parsing logic allows a malicious
│                       │      │                   HTTP server to set
│                       │      │                   'super cookies' that bypass the Public Suffix List check.
│                       │      │                   This enables an
│                       │      │                   attacker-controlled origin to inject cookies that curl
│                       │      │                   subsequently scopes and
│                       │      │                   transmits to unrelated third-party domains. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-8924 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-8924.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8924.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-8924.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3733905 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-8924 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-8924 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:24.793Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T23:06:00.797Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-8926 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8926 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:25d142557a219a4a7f8605e1b3958114c114e1186f1dcb33d34a3
│                       │      │                   d5a27ce3295 
│                       │      ├ Title           : curl: curl: Information disclosure via incorrect .netrc
│                       │      │                   password lookup 
│                       │      ├ Description     : When asking curl to use a `.netrc` file to find credentials
│                       │      │                   and at the same
│                       │      │                   time specifying a URL with a username(without a password),
│                       │      │                   like
│                       │      │                   `https://user@example.com/`, curl could wrongly get and use
│                       │      │                   the password for
│                       │      │                   *another* user set in the `.netrc` file for that host if
│                       │      │                   such a one exists and
│                       │      │                   there is no match for the specified user. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-522 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-8926 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-8926.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8926.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-8926.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3735184 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-8926 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-8926 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.037Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T23:02:54.49Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-10536 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-10536 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:ca7662c1b6ecf11c2723f0189d28e3d923bdeaa4121bb3323aa13
│                       │      │                   4b138aef612 
│                       │      ├ Title           : A use-after-free vulnerability exists in libcurl when an
│                       │      │                   application c ... 
│                       │      ├ Description     : A use-after-free vulnerability exists in libcurl when an
│                       │      │                   application
│                       │      │                   configures an HTTP/2 stream-dependency tree via
│                       │      │                   `CURLOPT_STREAM_DEPENDS` or
│                       │      │                   `CURLOPT_STREAM_DEPENDS_E`, subsequently invokes
│                       │      │                   `curl_easy_reset()`, and
│                       │      │                   finally terminates the handle with `curl_easy_cleanup()`.
│                       │      │                   During this final
│                       │      │                   cleanup phase, libcurl attempts to access and modify an
│                       │      │                   internal structure
│                       │      │                   that was already freed during the reset operation. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-416 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ├ References       ╭ [0]: https://curl.se/L7HzKXisfJ/CVE-2026-10536.md 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-10536.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-10536.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3751697 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-10536 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:23.563Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T18:02:03.89Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-11564 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-11564 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:31de5bbefee61e3abbb6f40c179f37b64d4883b33cc471cd338f1
│                       │      │                   41286669d34 
│                       │      ├ Title           : libcurl keeps previously used connections in a connection
│                       │      │                   pool for sub ... 
│                       │      ├ Description     : libcurl keeps previously used connections in a connection
│                       │      │                   pool for subsequent
│                       │      │                   transfers to reuse if one of them matches the setup.
│                       │      │                   
│                       │      │                   An easy handle that first uses default native CA trust can
│                       │      │                   continue trusting
│                       │      │                   the native platform store after the application switches
│                       │      │                   that same handle to
│                       │      │                   custom CA material for a later transfer. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-295 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ├ References       ╭ [0]: https://curl.se/L7HzKXisfJ/CVE-2026-11564.md 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-11564.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-11564.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3788984 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-11564 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:23.79Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T18:00:35.84Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-8458 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8458 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e12e838cb2d8b1dc4b4ca22e91f56de70710cc508a4164fbd62fd
│                       │      │                   006d0ea1e55 
│                       │      ├ Title           : libcurl might in some circumstances reuse the wrong
│                       │      │                   connection when as ... 
│                       │      ├ Description     : libcurl might in some circumstances reuse the wrong
│                       │      │                   connection when asked to
│                       │      │                   do Negotiate-authenticated ones, even when they are set to
│                       │      │                   use different
│                       │      │                   'services'.
│                       │      │                   
│                       │      │                   libcurl features a pool of recent connections so that
│                       │      │                   subsequent requests can
│                       │      │                   reuse an existing connection to avoid overhead.
│                       │      │                   When reusing a connection a range of criteria must be met.
│                       │      │                   Due to a logical
│                       │      │                   error in the code, a request that was issued by an
│                       │      │                   application could
│                       │      │                   wrongfully reuse an existing connection to the same server
│                       │      │                   that was
│                       │      │                   authenticated using different services. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ├ References       ╭ [0]: https://curl.se/L7HzKXisfJ/CVE-2026-8458.md 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-8458.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8458.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3721183 
│                       │      │                  ├ [4]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-8458 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:24.63Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T23:12:17.003Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2026-11856 
│                       │      ├ PkgID           : curl@8.20.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.20.0-r1?arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : 8c098d986f37fe67 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-11856 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:389fd3db01915fc2697e9fbf26256433616d992ec7cab124a00c9
│                       │      │                   bf6c5d56683 
│                       │      ├ Title           : Successfully using libcurl to do a transfer to a specific
│                       │      │                   HTTP origin  ... 
│                       │      ├ Description     : Successfully using libcurl to do a transfer to a specific
│                       │      │                   HTTP origin
│                       │      │                   (`hostA`) with **Digest** authentication and then changing
│                       │      │                   the origin to a
│                       │      │                   different one (`hostB`) for a second transfer, reusing the
│                       │      │                   same handle, makes
│                       │      │                   libcurl wrongly pass on the  `Authorization:` header field
│                       │      │                   meant for `hostA`,
│                       │      │                   to `hostB`. 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ CweIDs           ─ [0]: CWE-294 
│                       │      ├ References       ╭ [0]: https://curl.se/docs/CVE-2026-11856.html 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-11856.json 
│                       │      │                  ╰ [2]: https://hackerone.com/reports/3793260 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:23.973Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T19:43:55.6Z 
│                       ├ [18] ╭ VulnerabilityID : CVE-2026-11352 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-11352 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:6433d06bc59e02f3bbc66ff13b959cececd20a203e2192d5c57fd
│                       │      │                   d8ede2c8c59 
│                       │      ├ Title           : curl: libcurl: curl/libcurl: Remote denial of service via
│                       │      │                   QUIC UDP receive function vulnerability 
│                       │      ├ Description     : An issue in curl’s QUIC UDP receive function allows a
│                       │      │                   malicious HTTP/3 server
│                       │      │                   to trigger a remote denial of service against a curl or
│                       │      │                   libcurl client.
│                       │      │                   Because the helper function discards zero-length UDP
│                       │      │                   datagrams before counting
│                       │      │                   them toward the per-call packet budget, a connected QUIC
│                       │      │                   peer can continuously
│                       │      │                   stream empty datagrams to indefinitely stall the client. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-835 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-11352 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-11352.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-11352.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-11352.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3783438 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-11352 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-11352 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:23.693Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T18:01:19.013Z 
│                       ├ [19] ╭ VulnerabilityID : CVE-2026-11586 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-11586 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:c0f71678f9df2cc0e4eb2e7c27e5ec15b930463c95a21db313548
│                       │      │                   2d93e8555c4 
│                       │      ├ Title           : curl: curl: Denial of Service via WebSocket PING flood 
│                       │      ├ Description     : By default, curl automatically responds to WebSocket PING
│                       │      │                   frames. Because curl
│                       │      │                   lacks an upper bound on memory allocation for unacknowledged
│                       │      │                    frames, a
│                       │      │                   malicious server can exhaust all available memory by
│                       │      │                   flooding curl with rapid,
│                       │      │                   sequential PING messages. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-11586 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-11586.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-11586.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-11586.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3788931 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-11586 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-11586 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:23.883Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T17:59:46.92Z 
│                       ├ [20] ╭ VulnerabilityID : CVE-2026-12064 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-12064 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:30affe6869cd64c2fcb8719518d53ec2b64a3d1c5c193d6e7691f
│                       │      │                   c8759d1a26e 
│                       │      ├ Title           : curl: curl: SSH host verification bypass when using
│                       │      │                   schemeless URLs with SFTP/SCP 
│                       │      ├ Description     : When a user invokes curl using a schemeless URL combined
│                       │      │                   with
│                       │      │                   `--proto-default` sftp (or scp), a disconnect occurs between
│                       │      │                    the tool layer
│                       │      │                   and libcurl. The tool layer incorrectly infers the URL
│                       │      │                   scheme, which
│                       │      │                   erroneously bypasses the initialization of critical SSH
│                       │      │                   security options like
│                       │      │                   CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 and
│                       │      │                   CURLOPT_SSH_KNOWNHOSTS. Conversely, the
│                       │      │                   libcurl runtime successfully honors CURLOPT_DEFAULT_PROTOCOL
│                       │      │                    and establishes
│                       │      │                   the connection via SFTP/SCP as specified. Because the tool
│                       │      │                   layer skipped the
│                       │      │                   security configuration, these SSH host verification options
│                       │      │                   are silently
│                       │      │                   omitted, causing curl to connect to an unverified SSH remote
│                       │      │                    host without
│                       │      │                   throwing an error. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-295 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-12064 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-12064.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-12064.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-12064.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3797526 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-12064 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-12064 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:24.217Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T19:43:11.187Z 
│                       ├ [21] ╭ VulnerabilityID : CVE-2026-8286 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8286 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:ba666e76542c897b889b040e8b1637f6101b42c6ab526526227f2
│                       │      │                   5b4c9e9d71f 
│                       │      ├ Title           : curl: curl: Insecure connection establishment due to TLS
│                       │      │                   configuration mismatch 
│                       │      ├ Description     : A vulnerability exists where a new transfer that uses
│                       │      │                   STARTTLS to upgrade the
│                       │      │                   connection might reuse an existing live connection even
│                       │      │                   though the TLS
│                       │      │                   configuration mismatches so it should not. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-295 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 8.1 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-8286 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-8286.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8286.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-8286.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3718195 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-8286 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-8286 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:24.453Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T19:42:11.24Z 
│                       ├ [22] ╭ VulnerabilityID : CVE-2026-8925 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8925 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:56eb9c78ae169f4a74792658c90fbff38f07cae6e97ac2d71dcd6
│                       │      │                   6192476c327 
│                       │      ├ Title           : curl: curl: Double-free vulnerability in SASL authentication 
│                       │      ├ Description     : The curl logic that works with SASL authentication could end
│                       │      │                    up cleaning up
│                       │      │                   the GSASL context *twice* without clearing the pointer in
│                       │      │                   between, making it
│                       │      │                   `free()` the same pointer twice. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-415 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 8.1 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-8925 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-8925.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8925.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-8925.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3735193 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-8925 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-8925 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:24.95Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T23:04:29.69Z 
│                       ├ [23] ╭ VulnerabilityID : CVE-2026-8927 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8927 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:1857d7ffcf33930d25d2d90e848c91beb34a29c38e38b7fe72fea
│                       │      │                   df19aa56740 
│                       │      ├ Title           : libcurl: libcurl: Information disclosure due to uncleared
│                       │      │                   proxy authentication state 
│                       │      ├ Description     : When reusing a libcurl handle for sequential transfers
│                       │      │                   driven by
│                       │      │                   environment-variable proxy configuration, libcurl fails to
│                       │      │                   clear the proxy
│                       │      │                   authentication state between requests. Specifically, if the
│                       │      │                   initial transfer
│                       │      │                   authenticates against `proxyA` using Digest auth, a
│                       │      │                   subsequent transfer routed
│                       │      │                   through `proxyB` erroneously leaks the
│                       │      │                   `Proxy-Authorization:` header intended
│                       │      │                   solely for `proxyA`. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-294 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-8927 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-8927.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8927.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-8927.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3744543 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-8927 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-8927 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.123Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T23:21:03.53Z 
│                       ├ [24] ╭ VulnerabilityID : CVE-2026-8932 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8932 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:57aed4e0bc827bc4b5af130db29abf2fe5117dad46b3d6f43348a
│                       │      │                   beda5395b09 
│                       │      ├ Title           : libcurl: libcurl: Security feature bypass due to improper
│                       │      │                   mTLS connection reuse 
│                       │      ├ Description     : libcurl would reuse a previously created connection even
│                       │      │                   when some mTLS config
│                       │      │                   related option had been changed that should have prohibited
│                       │      │                   reuse.
│                       │      │                   
│                       │      │                   libcurl keeps previously used connections in a connection
│                       │      │                   pool for subsequent
│                       │      │                   transfers to reuse if one of them matches the setup.
│                       │      │                   However, some TLS
│                       │      │                   settings related to client certificates were left out from
│                       │      │                   the configuration
│                       │      │                   match checks, making them match too easily. In particular
│                       │      │                   options related to
│                       │      │                   the private key. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ redhat: 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-8932 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-8932.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8932.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3733910 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-8932 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-8932 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.363Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T23:18:32.137Z 
│                       ├ [25] ╭ VulnerabilityID : CVE-2026-9079 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-9079 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:121d92bc1291b1f8fedcfc1f07861797c465b4a1f73f758118a3d
│                       │      │                   83f939459aa 
│                       │      ├ Title           : libcurl: libcurl: Information disclosure due to failure to
│                       │      │                   clear proxy authentication credentials 
│                       │      ├ Description     : libcurl had a flaw that when instructed to clear proxy
│                       │      │                   authentication
│                       │      │                   credentials which made it not do so, leaving the old
│                       │      │                   credentials around to get
│                       │      │                   used for subsequent transfers that should not know nor use
│                       │      │                   them. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-522 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-9079 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-9079.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-9079.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-9079.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3750295 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-9079 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-9079 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.62Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T15:05:55.933Z 
│                       ├ [26] ╭ VulnerabilityID : CVE-2026-9080 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-9080 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:803b5095e26d56ca836a021be161351f0ee41c895c35b2254e6df
│                       │      │                   a335f8b585a 
│                       │      ├ Title           : libcurl: libcurl: Use-after-free via curl_easy_pause() in
│                       │      │                   CURLMOPT_SOCKETFUNCTION callback 
│                       │      ├ Description     : Calling `curl_easy_pause()` within the event-based
│                       │      │                   `CURLMOPT_SOCKETFUNCTION`
│                       │      │                   callback triggers a use-after-free vulnerability, where
│                       │      │                   libcurl attempts to
│                       │      │                   store a flag using a dangling struct pointer immediately
│                       │      │                   after that pointer's
│                       │      │                   memory has been freed. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-416 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 7.3 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-9080 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-9080.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-9080.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-9080.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3749204 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-9080 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-9080 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.713Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T15:05:26.53Z 
│                       ├ [27] ╭ VulnerabilityID : CVE-2026-9545 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-9545 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:c417b3372052971ab41e4f5b3cc957777bae01c83d93744aca4ff
│                       │      │                   ca5481696fa 
│                       │      ├ Title           : libcurl: libcurl: Information disclosure via cached SSL
│                       │      │                   session and early data 
│                       │      ├ Description     : In this scenario, libcurl first uses a proper HTTP/3 server
│                       │      │                   for the initial
│                       │      │                   transfers, and when it makes a second transfer to the same
│                       │      │                   site it has been
│                       │      │                   replaced by the attacker's impostor machine - without a
│                       │      │                   valid certificate.
│                       │      │                   
│                       │      │                   When libcurl returns to the hostname the second time with a
│                       │      │                   cached SSL session
│                       │      │                   (`CURLOPT_SSL_SESSIONID_CACHE` is not disabled) and early
│                       │      │                   data enabled (the
│                       │      │                   `CURLSSLOPT_EARLYDATA` bit is set in `CURLOPT_SSL_OPTIONS`),
│                       │      │                    libcurl might
│                       │      │                   send off the second request's bytes on that new connection
│                       │      │                   *before* enforcing
│                       │      │                   the certificate verification failure. Potentially leaking
│                       │      │                   sensitive
│                       │      │                   information. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-9545 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-9545.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-9545.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-9545.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3752888 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-9545 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-9545 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.807Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T15:03:56.92Z 
│                       ├ [28] ╭ VulnerabilityID : CVE-2026-9546 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-9546 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:5609eb469e9c107092c810177c9a8d611e194bba3cc921d7cccb3
│                       │      │                   7f6b8cc524f 
│                       │      ├ Title           : libcurl: libcurl: Information disclosure due to persistent
│                       │      │                   Referer header 
│                       │      ├ Description     : A vulnerability in libcurl caused the HTTP `Referer:` header
│                       │      │                    to persist even
│                       │      │                   when explicitly cleared. While the documentation states that
│                       │      │                    passing NULL to
│                       │      │                   `CURLOPT_REFERER` suppresses the header, the option failed
│                       │      │                   to clear the
│                       │      │                   internal state. As a result the previous referrer string was
│                       │      │                    erroneously
│                       │      │                   reused and sent in subsequent requests, potentially leaking
│                       │      │                   sensitive
│                       │      │                   information to unintended servers. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ redhat: 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-9546 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-9546.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-9546.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3754343 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-9546 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-9546 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.893Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T14:53:26.517Z 
│                       ├ [29] ╭ VulnerabilityID : CVE-2026-9547 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-9547 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:4f137e220bf6ff67336d9478aaa33beb57bc399eb6eecac1bb949
│                       │      │                   2fc3773a5a2 
│                       │      ├ Title           : curl: curl: Man-in-the-middle attack via SSH host key bypass 
│                       │      ├ Description     : When a libcurl-based application performs transfers via
│                       │      │                   `SCP://` or `SFTP://`
│                       │      │                   and utilizes the `CURLOPT_SSH_KEYFUNCTION` callback, it may
│                       │      │                   silently accept an
│                       │      │                   untrusted server. This vulnerability occurs when a server
│                       │      │                   presents a host key
│                       │      │                   type that does not match the specific key type already
│                       │      │                   recorded for that host
│                       │      │                   in the `known_hosts` file. Instead of rejecting the
│                       │      │                   mismatch, the callback
│                       │      │                   mechanism fails to properly enforce the restriction,
│                       │      │                   allowing the connection
│                       │      │                   to succeed without warning and risking a potential
│                       │      │                   man-in-the-middle attack. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ redhat: 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-9547 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-9547.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-9547.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-9547.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3751712 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-9547 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-9547 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.99Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T14:52:29.503Z 
│                       ├ [30] ╭ VulnerabilityID : CVE-2026-8924 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8924 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:7628d4999c0bb4e629f17b8518fcfff6d6b3977e423180246575a
│                       │      │                   c870366e732 
│                       │      ├ Title           : curl: curl: Cookie injection via malicious HTTP server using
│                       │      │                    super cookies 
│                       │      ├ Description     : A flaw in curl’s cookie parsing logic allows a malicious
│                       │      │                   HTTP server to set
│                       │      │                   'super cookies' that bypass the Public Suffix List check.
│                       │      │                   This enables an
│                       │      │                   attacker-controlled origin to inject cookies that curl
│                       │      │                   subsequently scopes and
│                       │      │                   transmits to unrelated third-party domains. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-8924 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-8924.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8924.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-8924.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3733905 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-8924 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-8924 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:24.793Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T23:06:00.797Z 
│                       ├ [31] ╭ VulnerabilityID : CVE-2026-8926 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8926 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e4b16e1adc45329622528789b221cbdfa341c6c335de05f05b272
│                       │      │                   5b9607bec5c 
│                       │      ├ Title           : curl: curl: Information disclosure via incorrect .netrc
│                       │      │                   password lookup 
│                       │      ├ Description     : When asking curl to use a `.netrc` file to find credentials
│                       │      │                   and at the same
│                       │      │                   time specifying a URL with a username(without a password),
│                       │      │                   like
│                       │      │                   `https://user@example.com/`, curl could wrongly get and use
│                       │      │                   the password for
│                       │      │                   *another* user set in the `.netrc` file for that host if
│                       │      │                   such a one exists and
│                       │      │                   there is no match for the specified user. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-522 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-8926 
│                       │      │                  ├ [1]: https://curl.se/L7HzKXisfJ/CVE-2026-8926.md 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8926.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-8926.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3735184 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-8926 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-8926 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:25.037Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T23:02:54.49Z 
│                       ├ [32] ╭ VulnerabilityID : CVE-2026-10536 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-10536 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:eec806b6dbc6ce527767486acbe3366ba35e805e93bb98ab8d4c7
│                       │      │                   bf838f16d05 
│                       │      ├ Title           : A use-after-free vulnerability exists in libcurl when an
│                       │      │                   application c ... 
│                       │      ├ Description     : A use-after-free vulnerability exists in libcurl when an
│                       │      │                   application
│                       │      │                   configures an HTTP/2 stream-dependency tree via
│                       │      │                   `CURLOPT_STREAM_DEPENDS` or
│                       │      │                   `CURLOPT_STREAM_DEPENDS_E`, subsequently invokes
│                       │      │                   `curl_easy_reset()`, and
│                       │      │                   finally terminates the handle with `curl_easy_cleanup()`.
│                       │      │                   During this final
│                       │      │                   cleanup phase, libcurl attempts to access and modify an
│                       │      │                   internal structure
│                       │      │                   that was already freed during the reset operation. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-416 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ├ References       ╭ [0]: https://curl.se/L7HzKXisfJ/CVE-2026-10536.md 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-10536.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-10536.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3751697 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-10536 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:23.563Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T18:02:03.89Z 
│                       ├ [33] ╭ VulnerabilityID : CVE-2026-11564 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-11564 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:0f1bbf2d9139eaaf80e9c530279da5a11ea929b584d45379cbbc9
│                       │      │                   583e1042f83 
│                       │      ├ Title           : libcurl keeps previously used connections in a connection
│                       │      │                   pool for sub ... 
│                       │      ├ Description     : libcurl keeps previously used connections in a connection
│                       │      │                   pool for subsequent
│                       │      │                   transfers to reuse if one of them matches the setup.
│                       │      │                   
│                       │      │                   An easy handle that first uses default native CA trust can
│                       │      │                   continue trusting
│                       │      │                   the native platform store after the application switches
│                       │      │                   that same handle to
│                       │      │                   custom CA material for a later transfer. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-295 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ├ References       ╭ [0]: https://curl.se/L7HzKXisfJ/CVE-2026-11564.md 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-11564.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-11564.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3788984 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-11564 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:23.79Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T18:00:35.84Z 
│                       ├ [34] ╭ VulnerabilityID : CVE-2026-8458 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8458 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:3ced0ac787338827115586184bff718499f8a8bc96ae6ebf98899
│                       │      │                   e5ae69a10ce 
│                       │      ├ Title           : libcurl might in some circumstances reuse the wrong
│                       │      │                   connection when as ... 
│                       │      ├ Description     : libcurl might in some circumstances reuse the wrong
│                       │      │                   connection when asked to
│                       │      │                   do Negotiate-authenticated ones, even when they are set to
│                       │      │                   use different
│                       │      │                   'services'.
│                       │      │                   
│                       │      │                   libcurl features a pool of recent connections so that
│                       │      │                   subsequent requests can
│                       │      │                   reuse an existing connection to avoid overhead.
│                       │      │                   When reusing a connection a range of criteria must be met.
│                       │      │                   Due to a logical
│                       │      │                   error in the code, a request that was issued by an
│                       │      │                   application could
│                       │      │                   wrongfully reuse an existing connection to the same server
│                       │      │                   that was
│                       │      │                   authenticated using different services. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ├ References       ╭ [0]: https://curl.se/L7HzKXisfJ/CVE-2026-8458.md 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-8458.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-8458.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3721183 
│                       │      │                  ├ [4]: https://ubuntu.com/security/notices/USN-8487-1 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-8458 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:24.63Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T23:12:17.003Z 
│                       ├ [35] ╭ VulnerabilityID : CVE-2026-11856 
│                       │      ├ PkgID           : libcurl@8.20.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.20.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 59b9580380420dad 
│                       │      ├ InstalledVersion: 8.20.0-r1 
│                       │      ├ FixedVersion    : 8.21.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-11856 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:a72a3da8b5b51e7cc57b9fc3929ac8b020ad0533f3dc60daee8de
│                       │      │                   548646442de 
│                       │      ├ Title           : Successfully using libcurl to do a transfer to a specific
│                       │      │                   HTTP origin  ... 
│                       │      ├ Description     : Successfully using libcurl to do a transfer to a specific
│                       │      │                   HTTP origin
│                       │      │                   (`hostA`) with **Digest** authentication and then changing
│                       │      │                   the origin to a
│                       │      │                   different one (`hostB`) for a second transfer, reusing the
│                       │      │                   same handle, makes
│                       │      │                   libcurl wrongly pass on the  `Authorization:` header field
│                       │      │                   meant for `hostA`,
│                       │      │                   to `hostB`. 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ CweIDs           ─ [0]: CWE-294 
│                       │      ├ References       ╭ [0]: https://curl.se/docs/CVE-2026-11856.html 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-11856.json 
│                       │      │                  ╰ [2]: https://hackerone.com/reports/3793260 
│                       │      ├ PublishedDate   : 2026-07-03T07:16:23.973Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T19:43:55.6Z 
│                       ├ [36] ╭ VulnerabilityID : CVE-2026-2100 
│                       │      ├ PkgID           : p11-kit@0.25.5-r2 
│                       │      ├ PkgName         : p11-kit 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/p11-kit@0.25.5-r2?arch=x86_64&distro=3
│                       │      │                  │       .24.1 
│                       │      │                  ╰ UID : 9d018f0737ae08a7 
│                       │      ├ InstalledVersion: 0.25.5-r2 
│                       │      ├ FixedVersion    : 0.26.2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                       │      │                  │         9427b17582323a475421 
│                       │      │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                       │      │                            d13c7ec0494711fcad72 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-2100 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:9274830e98fca5a5f45c86cb86bb59e9c4be85fc111192bd51077
│                       │      │                   83831296960 
│                       │      ├ Title           : p11-kit: NULL dereference via C_DeriveKey with specific NULL
│                       │      │                    parameters 
│                       │      ├ Description     : A flaw was found in p11-kit. A remote attacker could exploit
│                       │      │                    this vulnerability by calling the C_DeriveKey function on a
│                       │      │                    remote token with specific IBM kyber or IBM btc derive
│                       │      │                   mechanism parameters set to NULL. This could lead to the
│                       │      │                   RPC-client attempting to return an uninitialized value,
│                       │      │                   potentially resulting in a NULL dereference or undefined
│                       │      │                   behavior. This issue may cause an application level denial
│                       │      │                   of service or other unpredictable system states. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-824 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ nvd        : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:18143 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:18599 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2026:21275 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2026:22634 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2026:27998 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2026:7065 
│                       │      │                  ├ [6] : https://access.redhat.com/security/cve/CVE-2026-2100 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2437308 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2437308 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-2100 
│                       │      │                  ├ [10]: https://errata.almalinux.org/9/ALSA-2026-18599.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:18599 
│                       │      │                  ├ [12]: https://github.com/p11-glue/p11-kit/pull/740 
│                       │      │                  ├ [13]: https://github.com/p11-glue/p11-kit/releases/tag/0.26.2 
│                       │      │                  ├ [14]: https://linux.oracle.com/cve/CVE-2026-2100.html 
│                       │      │                  ├ [15]: https://linux.oracle.com/errata/ELSA-2026-18599.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2026-2100 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2026-2100 
│                       │      ├ PublishedDate   : 2026-03-26T21:17:04.247Z 
│                       │      ╰ LastModifiedDate: 2026-07-07T15:16:43.333Z 
│                       ╰ [37] ╭ VulnerabilityID : CVE-2026-2100 
│                              ├ PkgID           : p11-kit-trust@0.25.5-r2 
│                              ├ PkgName         : p11-kit-trust 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/p11-kit-trust@0.25.5-r2?arch=x86_64&di
│                              │                  │       stro=3.24.1 
│                              │                  ╰ UID : 40951c87f9e2103c 
│                              ├ InstalledVersion: 0.25.5-r2 
│                              ├ FixedVersion    : 0.26.2-r0 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c08834
│                              │                  │         9427b17582323a475421 
│                              │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25
│                              │                            d13c7ec0494711fcad72 
│                              ├ SeveritySource  : nvd 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-2100 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Fingerprint     : sha256:168049da9ffaa1fcd3853479a87f8b3649746e2520791d6eb58b9
│                              │                   be3ab6c7e91 
│                              ├ Title           : p11-kit: NULL dereference via C_DeriveKey with specific NULL
│                              │                    parameters 
│                              ├ Description     : A flaw was found in p11-kit. A remote attacker could exploit
│                              │                    this vulnerability by calling the C_DeriveKey function on a
│                              │                    remote token with specific IBM kyber or IBM btc derive
│                              │                   mechanism parameters set to NULL. This could lead to the
│                              │                   RPC-client attempting to return an uninitialized value,
│                              │                   potentially resulting in a NULL dereference or undefined
│                              │                   behavior. This issue may cause an application level denial
│                              │                   of service or other unpredictable system states. 
│                              ├ Severity        : HIGH 
│                              ├ CweIDs           ─ [0]: CWE-824 
│                              ├ VendorSeverity   ╭ alma       : 2 
│                              │                  ├ nvd        : 3 
│                              │                  ├ oracle-oval: 2 
│                              │                  ├ redhat     : 2 
│                              │                  ╰ rocky      : 2 
│                              ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                              │                  │        │           /A:H 
│                              │                  │        ╰ V3Score : 7.5 
│                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                              │                           │           /A:L 
│                              │                           ╰ V3Score : 5.3 
│                              ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:18143 
│                              │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:18599 
│                              │                  ├ [2] : https://access.redhat.com/errata/RHSA-2026:21275 
│                              │                  ├ [3] : https://access.redhat.com/errata/RHSA-2026:22634 
│                              │                  ├ [4] : https://access.redhat.com/errata/RHSA-2026:27998 
│                              │                  ├ [5] : https://access.redhat.com/errata/RHSA-2026:7065 
│                              │                  ├ [6] : https://access.redhat.com/security/cve/CVE-2026-2100 
│                              │                  ├ [7] : https://bugzilla.redhat.com/2437308 
│                              │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2437308 
│                              │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                              │                  │       26-2100 
│                              │                  ├ [10]: https://errata.almalinux.org/9/ALSA-2026-18599.html 
│                              │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:18599 
│                              │                  ├ [12]: https://github.com/p11-glue/p11-kit/pull/740 
│                              │                  ├ [13]: https://github.com/p11-glue/p11-kit/releases/tag/0.26.2 
│                              │                  ├ [14]: https://linux.oracle.com/cve/CVE-2026-2100.html 
│                              │                  ├ [15]: https://linux.oracle.com/errata/ELSA-2026-18599.html 
│                              │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2026-2100 
│                              │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2026-2100 
│                              ├ PublishedDate   : 2026-03-26T21:17:04.247Z 
│                              ╰ LastModifiedDate: 2026-07-07T15:16:43.333Z 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ├ Packages        
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2026-54512 
                        │     ├ VendorIDs        ─ [0]: GHSA-j3rv-43j4-c7qm 
                        │     ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                        │     │                  │       2.21.1 
                        │     │                  ╰ UID : 6bd66f14c6cb3d57 
                        │     ├ InstalledVersion: 2.21.1 
                        │     ├ FixedVersion    : 2.18.8, 3.1.4, 2.21.4 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                        │     │                  │         427b17582323a475421 
                        │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                        │     │                            13c7ec0494711fcad72 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54512 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:5c4cd244b24a117471764840b235d2ed22d7c61fbdd4236b2af781
                        │     │                   7df4c507d7 
                        │     ├ Title           : jackson-databind: jackson-databind: Arbitrary code execution
                        │     │                   via PolymorphicTypeValidator bypass 
                        │     ├ Description     : jackson-databind contains the general-purpose data-binding
                        │     │                   functionality and tree-model for Jackson Data Processor. From
                        │     │                    2.10.0 until 2.18.8, 2.21.4, and 3.1.4, jackson-databind's
                        │     │                   PolymorphicTypeValidator (PTV) is the primary safety
                        │     │                   mechanism guarding polymorphic deserialization. When
                        │     │                   polymorphic typing is enabled and a type identifier contains
                        │     │                   generic parameters (i.e. the type ID string contains <),
                        │     │                   DatabindContext._resolveAndValidateGeneric() validates only
                        │     │                   the raw container class name (the substring before <) against
                        │     │                    the configured PTV. If the container type is approved, the
                        │     │                   method parses the full canonical type string via
                        │     │                   TypeFactory.constructFromCanonical() and returns the fully
                        │     │                   parameterized type without ever validating the nested type
                        │     │                   arguments against the PTV. The nested type arguments are then
                        │     │                    resolved, instantiated, and populated as beans during
                        │     │                   deserialization. An attacker who controls the type ID can
                        │     │                   therefore place a denied class as a generic type parameter of
                        │     │                    an allowed container — for example
                        │     │                   java.util.ArrayList<com.evil.Gadget> when only
                        │     │                   java.util.ArrayList is allow-listed. The container passes the
                        │     │                    PTV check; com.evil.Gadget is loaded via Class.forName(name,
                        │     │                    true, loader), instantiated, and its properties are set from
                        │     │                    attacker-controlled JSON. This completely bypasses an
                        │     │                   explicitly configured PTV allow-list. This vulnerability is
                        │     │                   fixed in 2.18.8, 2.21.4, and 3.1.4. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs           ╭ [0]: CWE-184 
                        │     │                  ╰ [1]: CWE-502 
                        │     ├ VendorSeverity   ╭ ghsa  : 3 
                        │     │                  ╰ redhat: 3 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/
                        │     │                  │        │           A:H 
                        │     │                  │        ╰ V3Score : 8.1 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/
                        │     │                           │           A:H 
                        │     │                           ╰ V3Score : 8.1 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-54512 
                        │     │                  ├ [1]: https://github.com/FasterXML/jackson-databind 
                        │     │                  ├ [2]: https://github.com/FasterXML/jackson-databind/commit/43
                        │     │                  │      4d6c511de7fdd9872f29157aafb6162d12d8d5 
                        │     │                  ├ [3]: https://github.com/FasterXML/jackson-databind/issues/5988 
                        │     │                  ├ [4]: https://github.com/FasterXML/jackson-databind/security/
                        │     │                  │      advisories/GHSA-j3rv-43j4-c7qm 
                        │     │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-54512 
                        │     │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-54512 
                        │     ├ PublishedDate   : 2026-06-23T21:17:02.203Z 
                        │     ╰ LastModifiedDate: 2026-06-27T21:01:36.47Z 
                        ├ [1] ╭ VulnerabilityID : CVE-2026-54513 
                        │     ├ VendorIDs        ─ [0]: GHSA-rmj7-2vxq-3g9f 
                        │     ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                        │     │                  │       2.21.1 
                        │     │                  ╰ UID : 6bd66f14c6cb3d57 
                        │     ├ InstalledVersion: 2.21.1 
                        │     ├ FixedVersion    : 2.18.8, 2.21.4, 3.1.4 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                        │     │                  │         427b17582323a475421 
                        │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                        │     │                            13c7ec0494711fcad72 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54513 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:e7f006d517113cc9e33239cd4bfd0783c5163fd0ce16052e9c2de7
                        │     │                   c6471104c2 
                        │     ├ Title           : jackson-databind: Jackson-databind: Security bypass allows
                        │     │                   arbitrary code execution 
                        │     ├ Description     : jackson-databind contains the general-purpose data-binding
                        │     │                   functionality and tree-model for Jackson Data Processor. From
                        │     │                    2.10.0 until 2.18.8, 2.21.4, and 3.1.4,
                        │     │                   BasicPolymorphicTypeValidator.Builder.allowIfSubTypeIsArray()
                        │     │                    allowlists any array type based only on clazz.isArray(),
                        │     │                   without validating the array's component (element) type
                        │     │                   against the configured allowlist. A PTV built with
                        │     │                   allowIfSubTypeIsArray() plus an explicit concrete-type
                        │     │                   allowlist therefore still permits EvilType[] even though
                        │     │                   EvilType is not allowlisted. When Jackson deserializes the
                        │     │                   elements and no per-element type IDs are present, it
                        │     │                   instantiates the component type directly with no further PTV
                        │     │                   check, bypassing the allowlist. This vulnerability is fixed
                        │     │                   in 2.18.8, 2.21.4, and 3.1.4. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs           ─ [0]: CWE-184 
                        │     ├ VendorSeverity   ╭ ghsa  : 3 
                        │     │                  ╰ redhat: 3 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/
                        │     │                  │        │           A:H 
                        │     │                  │        ╰ V3Score : 8.1 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/
                        │     │                           │           A:H 
                        │     │                           ╰ V3Score : 8.1 
                        │     ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2026-54513 
                        │     │                  ├ [1] : https://bugzilla.redhat.com/show_bug.cgi?id=2492010 
                        │     │                  ├ [2] : https://github.com/FasterXML/jackson-databind 
                        │     │                  ├ [3] : https://github.com/FasterXML/jackson-databind/commit/0
                        │     │                  │       1d1692c8d0ed03e51a0e3c4f8a9e6908e4931e5 
                        │     │                  ├ [4] : https://github.com/FasterXML/jackson-databind/commit/2
                        │     │                  │       4529da29fdf46ff94ca38de9ebf31cd188f5e8e 
                        │     │                  ├ [5] : https://github.com/FasterXML/jackson-databind/issues/5
                        │     │                  │       981 
                        │     │                  ├ [6] : https://github.com/FasterXML/jackson-databind/issues/5
                        │     │                  │       983 
                        │     │                  ├ [7] : https://github.com/FasterXML/jackson-databind/pull/5984 
                        │     │                  ├ [8] : https://github.com/FasterXML/jackson-databind/security
                        │     │                  │       /advisories/GHSA-rmj7-2vxq-3g9f 
                        │     │                  ├ [9] : https://nvd.nist.gov/vuln/detail/CVE-2026-54513 
                        │     │                  ├ [10]: https://security.access.redhat.com/data/csaf/v2/vex/20
                        │     │                  │       26/cve-2026-54513.json 
                        │     │                  ╰ [11]: https://www.cve.org/CVERecord?id=CVE-2026-54513 
                        │     ├ PublishedDate   : 2026-06-23T21:17:02.333Z 
                        │     ╰ LastModifiedDate: 2026-07-03T13:17:29.627Z 
                        ├ [2] ╭ VulnerabilityID : CVE-2026-54514 
                        │     ├ VendorIDs        ─ [0]: GHSA-hgj6-7826-r7m5 
                        │     ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                        │     │                  │       2.21.1 
                        │     │                  ╰ UID : 6bd66f14c6cb3d57 
                        │     ├ InstalledVersion: 2.21.1 
                        │     ├ FixedVersion    : 2.18.8, 2.21.4, 3.1.4 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                        │     │                  │         427b17582323a475421 
                        │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                        │     │                            13c7ec0494711fcad72 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54514 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:8d752c55bb7ade342f9a8feae77c0de80590e5996f50a438f8d8ef
                        │     │                   2e7bcd98c0 
                        │     ├ Title           : jackson-databind: jackson-databind: Information Disclosure
                        │     │                   via Eager DNS Resolution 
                        │     ├ Description     : jackson-databind contains the general-purpose data-binding
                        │     │                   functionality and tree-model for Jackson Data Processor. From
                        │     │                    2.0.0 until 2.18.8, 2.21.4, and 3.1.4,
                        │     │                   JDKFromStringDeserializer constructed InetSocketAddress with
                        │     │                   new InetSocketAddress(host, port), which performs eager DNS
                        │     │                   name resolution for hostname inputs at deserialization time.
                        │     │                   An application that binds untrusted JSON into a type
                        │     │                   containing an InetSocketAddress field issues an
                        │     │                   attacker-chosen DNS query during readValue, before any
                        │     │                   application-level validation or connect logic. The fix uses
                        │     │                   InetSocketAddress.createUnresolved(host, port), deferring DNS
                        │     │                    to an explicit connect. This vulnerability is fixed in
                        │     │                   2.18.8, 2.21.4, and 3.1.4. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-918 
                        │     ├ VendorSeverity   ╭ ghsa  : 2 
                        │     │                  ╰ redhat: 2 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/
                        │     │                  │        │           A:N 
                        │     │                  │        ╰ V3Score : 5.3 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/
                        │     │                           │           A:N 
                        │     │                           ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-54514 
                        │     │                  ├ [1]: https://github.com/FasterXML/jackson-databind 
                        │     │                  ├ [2]: https://github.com/FasterXML/jackson-databind/commit/1f
                        │     │                  │      5a1037b1e9e05920e755cb35f198bcd46667e4 
                        │     │                  ├ [3]: https://github.com/FasterXML/jackson-databind/pull/5951 
                        │     │                  ├ [4]: https://github.com/FasterXML/jackson-databind/security/
                        │     │                  │      advisories/GHSA-hgj6-7826-r7m5 
                        │     │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-54514 
                        │     │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-54514 
                        │     ├ PublishedDate   : 2026-06-23T21:17:02.467Z 
                        │     ╰ LastModifiedDate: 2026-06-27T20:55:09.61Z 
                        ├ [3] ╭ VulnerabilityID : CVE-2026-54515 
                        │     ├ VendorIDs        ─ [0]: GHSA-5jmj-h7xm-6q6v 
                        │     ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                        │     │                  │       2.21.1 
                        │     │                  ╰ UID : 6bd66f14c6cb3d57 
                        │     ├ InstalledVersion: 2.21.1 
                        │     ├ FixedVersion    : 3.1.4, 2.18.9, 2.21.5, 2.22.1 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                        │     │                  │         427b17582323a475421 
                        │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                        │     │                            13c7ec0494711fcad72 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54515 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:1fa99c3799df4b71554b438014aa474fcf6968fe0386813966348b
                        │     │                   2f50cb76e5 
                        │     ├ Title           : jackson-databind: jackson-databind: Ignored properties can be
                        │     │                    unexpectedly modified 
                        │     ├ Description     : jackson-databind contains the general-purpose data-binding
                        │     │                   functionality and tree-model for Jackson Data Processor. From
                        │     │                    2.8.0 until 2.18.9, 2.21.5, and 3.1.4, in
                        │     │                   BeanDeserializerBase.createContextual(), per-property
                        │     │                   @JsonIgnoreProperties exclusions are applied by
                        │     │                   _handleByNameInclusion(), producing a contextual deserializer
                        │     │                    whose BeanPropertyMap has the ignored properties removed.
                        │     │                   The subsequent per-property case-insensitivity block
                        │     │                   (triggered by
                        │     │                   @JsonFormat(ACCEPT_CASE_INSENSITIVE_PROPERTIES)) rebuilds
                        │     │                   from this._beanProperties (the original, unfiltered map)
                        │     │                   instead of contextual._beanProperties, then overwrites the
                        │     │                   filtered map — restoring every property
                        │     │                   _handleByNameInclusion had just removed. The ignored property
                        │     │                    becomes writable again. This vulnerability is fixed in
                        │     │                   2.18.9, 2.21.5, and 3.1.4. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-915 
                        │     ├ VendorSeverity   ╭ ghsa  : 2 
                        │     │                  ╰ redhat: 2 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/
                        │     │                  │        │           A:N 
                        │     │                  │        ╰ V3Score : 5.3 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/
                        │     │                           │           A:N 
                        │     │                           ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-54515 
                        │     │                  ├ [1]: https://github.com/FasterXML/jackson-databind 
                        │     │                  ├ [2]: https://github.com/FasterXML/jackson-databind/commit/0e
                        │     │                  │      1b0b211f7a53baa62ba2f4c9bd006c7bf4d5fa 
                        │     │                  ├ [3]: https://github.com/FasterXML/jackson-databind/issues/5962 
                        │     │                  ├ [4]: https://github.com/FasterXML/jackson-databind/issues/5964 
                        │     │                  ├ [5]: https://github.com/FasterXML/jackson-databind/security/
                        │     │                  │      advisories/GHSA-5jmj-h7xm-6q6v 
                        │     │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-54515 
                        │     │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-54515 
                        │     ├ PublishedDate   : 2026-06-23T21:17:02.597Z 
                        │     ╰ LastModifiedDate: 2026-06-29T13:38:59.057Z 
                        ├ [4] ╭ VulnerabilityID : CVE-2026-54516 
                        │     ├ VendorIDs        ─ [0]: GHSA-9fxm-vc8v-hj55 
                        │     ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                        │     │                  │       2.21.1 
                        │     │                  ╰ UID : 6bd66f14c6cb3d57 
                        │     ├ InstalledVersion: 2.21.1 
                        │     ├ FixedVersion    : 2.21.4, 3.1.4 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                        │     │                  │         427b17582323a475421 
                        │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                        │     │                            13c7ec0494711fcad72 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54516 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:99623393200050120b9a413f4466e17a6d42f879557d8b50a15e9c
                        │     │                   711cd67e71 
                        │     ├ Title           : jackson-databind: jackson-databind: Security bypass due to
                        │     │                   improper handling of renamed properties 
                        │     ├ Description     : jackson-databind contains the general-purpose data-binding
                        │     │                   functionality and tree-model for Jackson Data Processor. From
                        │     │                    2.21.0 until 2.21.4 and 3.1.4,
                        │     │                   POJOPropertiesCollector._renameProperties() allows a property
                        │     │                    with @JsonProperty("renamed") on the getter and @JsonIgnore
                        │     │                   on the setter to be renamed rather than dropped. With
                        │     │                   MapperFeature.INFER_PROPERTY_MUTATORS enabled (default), the
                        │     │                   private backing field is retained; during deserialization
                        │     │                   BeanDeserializerFactory.addBeanProps() sees hasField()==true,
                        │     │                    builds a FieldProperty, and makes the backing field
                        │     │                   writable. An attacker supplying the renamed JSON key writes
                        │     │                   the backing field directly, bypassing the @JsonIgnore on the
                        │     │                   setter. This vulnerability is fixed in 3.1.4. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-915 
                        │     ├ VendorSeverity   ╭ ghsa  : 2 
                        │     │                  ╰ redhat: 2 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/
                        │     │                  │        │           A:N 
                        │     │                  │        ╰ V3Score : 5.3 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/
                        │     │                           │           A:N 
                        │     │                           ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-54516 
                        │     │                  ├ [1]: https://github.com/FasterXML/jackson-databind 
                        │     │                  ├ [2]: https://github.com/FasterXML/jackson-databind/commit/c3
                        │     │                  │      d56dd25d52319828147c5b9aeabf2d485c250a 
                        │     │                  ├ [3]: https://github.com/FasterXML/jackson-databind/commit/e8
                        │     │                  │      8cb17006b6af4883b973058f0bb6486e5074af 
                        │     │                  ├ [4]: https://github.com/FasterXML/jackson-databind/pull/5967 
                        │     │                  ├ [5]: https://github.com/FasterXML/jackson-databind/pull/5968 
                        │     │                  ├ [6]: https://github.com/FasterXML/jackson-databind/security/
                        │     │                  │      advisories/GHSA-9fxm-vc8v-hj55 
                        │     │                  ├ [7]: https://nvd.nist.gov/vuln/detail/CVE-2026-54516 
                        │     │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2026-54516 
                        │     ├ PublishedDate   : 2026-06-23T21:17:02.723Z 
                        │     ╰ LastModifiedDate: 2026-06-27T20:52:12.103Z 
                        ├ [5] ╭ VulnerabilityID : CVE-2026-54517 
                        │     ├ VendorIDs        ─ [0]: GHSA-5hh8-q8hv-fr38 
                        │     ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                        │     │                  │       2.21.1 
                        │     │                  ╰ UID : 6bd66f14c6cb3d57 
                        │     ├ InstalledVersion: 2.21.1 
                        │     ├ FixedVersion    : 2.21.4, 3.1.4 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                        │     │                  │         427b17582323a475421 
                        │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                        │     │                            13c7ec0494711fcad72 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54517 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:06cbbdec077f3dfc23a0738c4495a5f43af9862a781c8a304d96ea
                        │     │                   15b92ff9af 
                        │     ├ Title           : jackson-databind: jackson-databind: Information disclosure
                        │     │                   via improper JsonView filter application 
                        │     ├ Description     : jackson-databind contains the general-purpose data-binding
                        │     │                   functionality and tree-model for Jackson Data Processor. From
                        │     │                    2.21.0 until 2.21.4 and 3.1.4, in
                        │     │                   BeanDeserializer._deserializeUsingPropertyBased, the
                        │     │                   active-view (@JsonView) filter was applied only to creator
                        │     │                   properties; the regular property-buffering branch performed
                        │     │                   no prop.visibleInView(activeView) check. A change making
                        │     │                   SetterlessProperty.isMerging() return true routed setterless
                        │     │                   Collection/Map properties through this unguarded path, so a
                        │     │                   setterless collection annotated with a restricted @JsonView
                        │     │                   is populated from attacker JSON even when the active view
                        │     │                   excludes it. This vulnerability is fixed in 2.21.4 and
                        │     │                   3.1.4. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-863 
                        │     ├ VendorSeverity   ╭ ghsa  : 2 
                        │     │                  ╰ redhat: 2 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/
                        │     │                  │        │           A:N 
                        │     │                  │        ╰ V3Score : 5.3 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/
                        │     │                           │           A:N 
                        │     │                           ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-54517 
                        │     │                  ├ [1]: https://github.com/FasterXML/jackson-databind 
                        │     │                  ├ [2]: https://github.com/FasterXML/jackson-databind/commit/5b
                        │     │                  │      f23edb4221f7dd2ec8e71ff6d26c61640f261d 
                        │     │                  ├ [3]: https://github.com/FasterXML/jackson-databind/commit/94
                        │     │                  │      c5d215b3af1505098c686405d9641f041a9962 
                        │     │                  ├ [4]: https://github.com/FasterXML/jackson-databind/pull/5969 
                        │     │                  ├ [5]: https://github.com/FasterXML/jackson-databind/pull/5970 
                        │     │                  ├ [6]: https://github.com/FasterXML/jackson-databind/security/
                        │     │                  │      advisories/GHSA-5hh8-q8hv-fr38 
                        │     │                  ├ [7]: https://nvd.nist.gov/vuln/detail/CVE-2026-54517 
                        │     │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2026-54517 
                        │     ├ PublishedDate   : 2026-06-23T21:17:02.853Z 
                        │     ╰ LastModifiedDate: 2026-06-27T20:51:09.987Z 
                        ╰ [6] ╭ VulnerabilityID : CVE-2026-54518 
                              ├ VendorIDs        ─ [0]: GHSA-rcqc-6cw3-h962 
                              ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                              │                  │       2.21.1 
                              │                  ╰ UID : 6bd66f14c6cb3d57 
                              ├ InstalledVersion: 2.21.1 
                              ├ FixedVersion    : 2.21.4 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                              │                  │         427b17582323a475421 
                              │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                              │                            13c7ec0494711fcad72 
                              ├ SeveritySource  : ghsa 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54518 
                              ├ DataSource       ╭ ID  : ghsa 
                              │                  ├ Name: GitHub Security Advisory Maven 
                              │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                              │                          osystem%3Amaven 
                              ├ Fingerprint     : sha256:1810260d2fe85b9b14c8cc1e644f0db37e6d016701a22bff0b35f2
                              │                   77dc2d6794 
                              ├ Title           : jackson-databind: jackson-databind: Information disclosure
                              │                   and data manipulation via view-based access control bypass 
                              ├ Description     : jackson-databind contains the general-purpose data-binding
                              │                   functionality and tree-model for Jackson Data Processor. From
                              │                    2.21.0 until 2.21.4 and 3.1.4,
                              │                   UnwrappedPropertyHandler.processUnwrappedCreatorProperties()
                              │                   replays buffered JSON into creator parameters but never
                              │                   consults prop.visibleInView(activeView). The normal
                              │                   property-based creator path gates creator properties on the
                              │                   active view, but this unwrapped-creator replay path bypasses
                              │                   that check, so a constructor parameter annotated with both
                              │                   @JsonView(AdminView.class) and @JsonUnwrapped is populated
                              │                   from attacker JSON even when a more restrictive view is
                              │                   active. This vulnerability is fixed in 2.21.4 and 3.1.4. 
                              ├ Severity        : MEDIUM 
                              ├ CweIDs           ─ [0]: CWE-863 
                              ├ VendorSeverity   ╭ ghsa  : 2 
                              │                  ╰ redhat: 2 
                              ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/
                              │                  │        │           A:N 
                              │                  │        ╰ V3Score : 6.5 
                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/
                              │                           │           A:N 
                              │                           ╰ V3Score : 6.5 
                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-54518 
                              │                  ├ [1]: https://github.com/FasterXML/jackson-databind 
                              │                  ├ [2]: https://github.com/FasterXML/jackson-databind/commit/72
                              │                  │      1fa07ebbd4aab4a659a1a68940878315c3e341 
                              │                  ├ [3]: https://github.com/FasterXML/jackson-databind/commit/d6
                              │                  │      33bc038f200c1397c07f1a2b46f58e72c91eea 
                              │                  ├ [4]: https://github.com/FasterXML/jackson-databind/pull/5971 
                              │                  ├ [5]: https://github.com/FasterXML/jackson-databind/pull/5973 
                              │                  ├ [6]: https://github.com/FasterXML/jackson-databind/security/
                              │                  │      advisories/GHSA-rcqc-6cw3-h962 
                              │                  ├ [7]: https://nvd.nist.gov/vuln/detail/CVE-2026-54518 
                              │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2026-54518 
                              ├ PublishedDate   : 2026-06-23T22:16:32.073Z 
                              ╰ LastModifiedDate: 2026-06-27T20:49:30.977Z 
```
