```yaml
╭ [0] ╭ Target         : openaf/oaf:latest (alpine 3.23.4) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2025-14017 
│                       │      ├ PkgID           : curl@8.17.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.17.0-r1?arch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : 1681fc3d2c57fb44 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-14017 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:121eeebc3aee774a201b6cf7d4073d949d67abace592576386b08
│                       │      │                   645bf5b0502 
│                       │      ├ Title           : curl: curl: Security bypass due to global TLS option changes
│                       │      │                    in multi-threaded LDAPS transfers 
│                       │      ├ Description     : When doing multi-threaded LDAPS transfers (LDAP over TLS)
│                       │      │                   with libcurl,
│                       │      │                   changing TLS options in one thread would inadvertently
│                       │      │                   change them globally
│                       │      │                   and therefore possibly also affect other concurrently setup
│                       │      │                   transfers.
│                       │      │                   
│                       │      │                   Disabling certificate verification for a specific transfer
│                       │      │                   could
│                       │      │                   unintentionally disable the feature for other threads as
│                       │      │                   well. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ julia      : 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 6.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/01/07/3 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2025-14017 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-14017.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2025-14017.json 
│                       │      │                  ├ [4]: https://github.com/advisories/GHSA-jh4h-2cg6-889h 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2025-14017 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8062-1 
│                       │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-8062-2 
│                       │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2025-14017 
│                       │      ├ PublishedDate   : 2026-01-08T10:15:45.667Z 
│                       │      ╰ LastModifiedDate: 2026-01-27T21:29:39.953Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2025-14524 
│                       │      ├ PkgID           : curl@8.17.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.17.0-r1?arch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : 1681fc3d2c57fb44 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-14524 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:7bcbcdb020492eb07d5bb81203a6abc1cd245a0bdfbb825db78ef
│                       │      │                   396cb852571 
│                       │      ├ Title           : curl: Information disclosure via cross-protocol redirect
│                       │      │                   with OAuth2 bearer token 
│                       │      ├ Description     : When an OAuth2 bearer token is used for an HTTP(S) transfer,
│                       │      │                    and that transfer
│                       │      │                   performs a cross-protocol redirect to a second URL that uses
│                       │      │                    an IMAP, LDAP,
│                       │      │                   POP3 or SMTP scheme, curl might wrongly pass on the bearer
│                       │      │                   token to the new
│                       │      │                   target host. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-601 
│                       │      ├ VendorSeverity   ╭ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ julia      : 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/01/07/4 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2025-14524 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-14524.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2025-14524.json 
│                       │      │                  ├ [4]: https://github.com/advisories/GHSA-g897-jvjx-78vg 
│                       │      │                  ├ [5]: https://hackerone.com/reports/3459417 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2025-14524 
│                       │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-8062-1 
│                       │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2025-14524 
│                       │      ├ PublishedDate   : 2026-01-08T10:15:46.607Z 
│                       │      ╰ LastModifiedDate: 2026-01-20T14:53:11.017Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2025-14819 
│                       │      ├ PkgID           : curl@8.17.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.17.0-r1?arch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : 1681fc3d2c57fb44 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-14819 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:82c45cdff70ce9cdb02b33b53542c843045939ec6866d73b2088d
│                       │      │                   6635dcd5496 
│                       │      ├ Title           : curl: libcurl: Improper certificate validation due to cached
│                       │      │                    TLS settings reuse 
│                       │      ├ Description     : When doing TLS related transfers with reused easy or multi
│                       │      │                   handles and
│                       │      │                   altering the  `CURLSSLOPT_NO_PARTIALCHAIN` option, libcurl
│                       │      │                   could accidentally
│                       │      │                   reuse a CA store cached in memory for which the partial
│                       │      │                   chain option was
│                       │      │                   reversed. Contrary to the user's wishes and expectations.
│                       │      │                   This could make
│                       │      │                   libcurl find and accept a trust chain that it otherwise
│                       │      │                   would not. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-295 
│                       │      ├ VendorSeverity   ╭ amazon: 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.8 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/01/07/5 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2025-14819 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-14819.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2025-14819.json 
│                       │      │                  ├ [4]: https://github.com/advisories/GHSA-vqhr-m87q-9jqh 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2025-14819 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8062-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2025-14819 
│                       │      ├ PublishedDate   : 2026-01-08T10:15:46.73Z 
│                       │      ╰ LastModifiedDate: 2026-01-20T14:51:26.263Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-1965 
│                       │      ├ PkgID           : curl@8.17.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.17.0-r1?arch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : 1681fc3d2c57fb44 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-1965 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:54202ccf44f6ac5437817ca82eb178aa641216e488deee72026fa
│                       │      │                   4540a1d98de 
│                       │      ├ Title           : curl: curl: Authentication bypass due to incorrect
│                       │      │                   connection reuse with Negotiate authentication 
│                       │      ├ Description     : libcurl can in some circumstances reuse the wrong connection
│                       │      │                    when asked to do
│                       │      │                   an Negotiate-authenticated HTTP or HTTPS request.
│                       │      │                   
│                       │      │                   libcurl features a pool of recent connections so that
│                       │      │                   subsequent requests can
│                       │      │                   reuse an existing connection to avoid overhead.
│                       │      │                   When reusing a connection a range of criterion must first be
│                       │      │                    met. Due to a
│                       │      │                   logical error in the code, a request that was issued by an
│                       │      │                   application could
│                       │      │                   wrongfully reuse an existing connection to the same server
│                       │      │                   that was
│                       │      │                   authenticated using different credentials. One underlying
│                       │      │                   reason being that
│                       │      │                   Negotiate sometimes authenticates *connections* and not
│                       │      │                   *requests*, contrary
│                       │      │                   to how HTTP is designed to work.
│                       │      │                   An application that allows Negotiate authentication to a
│                       │      │                   server (that responds
│                       │      │                   wanting Negotiate) with `user1:password1` and then does
│                       │      │                   another operation to
│                       │      │                   the same server also using Negotiate but with
│                       │      │                   `user2:password2` (while the
│                       │      │                   previous connection is still alive) - the second request
│                       │      │                   wrongly reused the
│                       │      │                   same connection and since it then sees that the Negotiate
│                       │      │                   negotiation is
│                       │      │                   already made, it just sends the request over that connection
│                       │      │                    thinking it uses
│                       │      │                   the user2 credentials when it is in fact still using the
│                       │      │                   connection
│                       │      │                   authenticated for user1...
│                       │      │                   The set of authentication methods to use is set with 
│                       │      │                   `CURLOPT_HTTPAUTH`.
│                       │      │                   Applications can disable libcurl's reuse of connections and
│                       │      │                   thus mitigate this
│                       │      │                   problem, by using one of the following libcurl options to
│                       │      │                   alter how
│                       │      │                   connections are or are not reused: `CURLOPT_FRESH_CONNECT`,
│                       │      │                   `CURLOPT_MAXCONNECTS` and `CURLMOPT_MAX_HOST_CONNECTIONS`
│                       │      │                   (if using the
│                       │      │                   curl_multi API). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-305 
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.8 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-1965 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-1965.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-1965.json 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-1965 
│                       │      │                  ├ [4]: https://ubuntu.com/security/notices/USN-8084-1 
│                       │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-8099-1 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-1965 
│                       │      ├ PublishedDate   : 2026-03-11T11:15:59.177Z 
│                       │      ╰ LastModifiedDate: 2026-03-12T14:11:19.07Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-3783 
│                       │      ├ PkgID           : curl@8.17.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.17.0-r1?arch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : 1681fc3d2c57fb44 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3783 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e3b8696f543c843b35eae79817c2cd1096141b8d736cef488ba28
│                       │      │                   6420d81a40f 
│                       │      ├ Title           : curl: curl: Information disclosure via OAuth2 bearer token
│                       │      │                   leakage during HTTP(S) redirect 
│                       │      ├ Description     : When an OAuth2 bearer token is used for an HTTP(S) transfer,
│                       │      │                    and that transfer
│                       │      │                   performs a redirect to a second URL, curl could leak that
│                       │      │                   token to the second
│                       │      │                   hostname under some circumstances.
│                       │      │                   
│                       │      │                   If the hostname that the first request is redirected to has
│                       │      │                   information in the
│                       │      │                   used .netrc file, with either of the `machine` or `default`
│                       │      │                   keywords, curl
│                       │      │                   would pass on the bearer token set for the first host also
│                       │      │                   to the second one. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-522 
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.7 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/03/11/2 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3783 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-3783.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-3783.json 
│                       │      │                  ├ [4]: https://github.com/advisories/GHSA-8whr-249c-vfjp 
│                       │      │                  ├ [5]: https://hackerone.com/reports/3583983 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-3783 
│                       │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-8084-1 
│                       │      │                  ├ [8]: https://ubuntu.com/security/notices/USN-8099-1 
│                       │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2026-3783 
│                       │      ├ PublishedDate   : 2026-03-11T11:16:00.08Z 
│                       │      ╰ LastModifiedDate: 2026-03-12T14:10:37.3Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-3784 
│                       │      ├ PkgID           : curl@8.17.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.17.0-r1?arch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : 1681fc3d2c57fb44 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3784 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:453d36eda12ebb79bfc2634a9873293e2697e2c43dd0879830e37
│                       │      │                   7c9ec957eb8 
│                       │      ├ Title           : curl: curl: Unauthorized access due to improper HTTP proxy
│                       │      │                   connection reuse 
│                       │      ├ Description     : curl would wrongly reuse an existing HTTP proxy connection
│                       │      │                   doing CONNECT to a
│                       │      │                   server, even if the new request uses different credentials
│                       │      │                   for the HTTP proxy.
│                       │      │                   The proper behavior is to create or use a separate
│                       │      │                   connection. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-305 
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/03/11/3 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3784 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-3784.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-3784.json 
│                       │      │                  ├ [4]: https://github.com/advisories/GHSA-5q3w-6p3j-mw6p 
│                       │      │                  ├ [5]: https://hackerone.com/reports/3584903 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-3784 
│                       │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-8084-1 
│                       │      │                  ├ [8]: https://ubuntu.com/security/notices/USN-8099-1 
│                       │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2026-3784 
│                       │      ├ PublishedDate   : 2026-03-11T11:16:00.437Z 
│                       │      ╰ LastModifiedDate: 2026-03-12T14:09:50.47Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-3805 
│                       │      ├ PkgID           : curl@8.17.0-r1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.17.0-r1?arch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : 1681fc3d2c57fb44 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3805 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e175f72d12cbcc6eceda9d552bacf4006a6b65af54cae5d5034b8
│                       │      │                   332ee012852 
│                       │      ├ Title           : curl: curl: Arbitrary code execution or Denial of Service
│                       │      │                   via use-after-free in SMB request handling 
│                       │      ├ Description     : When doing a second SMB request to the same host again, curl
│                       │      │                    would wrongly use
│                       │      │                   a data pointer pointing into already freed memory. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-416 
│                       │      ├ VendorSeverity   ╭ amazon: 2 
│                       │      │                  ├ julia : 3 
│                       │      │                  ├ photon: 3 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 6.3 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/03/11/4 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3805 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-3805.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-3805.json 
│                       │      │                  ├ [4]: https://github.com/advisories/GHSA-2289-hhfc-p684 
│                       │      │                  ├ [5]: https://hackerone.com/reports/3591944 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-3805 
│                       │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-8084-1 
│                       │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2026-3805 
│                       │      ├ PublishedDate   : 2026-03-11T11:16:00.967Z 
│                       │      ╰ LastModifiedDate: 2026-03-12T14:08:56.79Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2025-14017 
│                       │      ├ PkgID           : libcurl@8.17.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.17.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .23.4 
│                       │      │                  ╰ UID : 67c003c6efbeb161 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-14017 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:3832fdd4a34609e33174d3b8b30c5a65d10baf0123bcddd55242f
│                       │      │                   ab24f116359 
│                       │      ├ Title           : curl: curl: Security bypass due to global TLS option changes
│                       │      │                    in multi-threaded LDAPS transfers 
│                       │      ├ Description     : When doing multi-threaded LDAPS transfers (LDAP over TLS)
│                       │      │                   with libcurl,
│                       │      │                   changing TLS options in one thread would inadvertently
│                       │      │                   change them globally
│                       │      │                   and therefore possibly also affect other concurrently setup
│                       │      │                   transfers.
│                       │      │                   
│                       │      │                   Disabling certificate verification for a specific transfer
│                       │      │                   could
│                       │      │                   unintentionally disable the feature for other threads as
│                       │      │                   well. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ julia      : 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 6.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/01/07/3 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2025-14017 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-14017.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2025-14017.json 
│                       │      │                  ├ [4]: https://github.com/advisories/GHSA-jh4h-2cg6-889h 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2025-14017 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8062-1 
│                       │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-8062-2 
│                       │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2025-14017 
│                       │      ├ PublishedDate   : 2026-01-08T10:15:45.667Z 
│                       │      ╰ LastModifiedDate: 2026-01-27T21:29:39.953Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2025-14524 
│                       │      ├ PkgID           : libcurl@8.17.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.17.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .23.4 
│                       │      │                  ╰ UID : 67c003c6efbeb161 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-14524 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:dec4c10778d9edfb5caded7cd1e58126e39af6a166b048d878cd5
│                       │      │                   e4d1861e25f 
│                       │      ├ Title           : curl: Information disclosure via cross-protocol redirect
│                       │      │                   with OAuth2 bearer token 
│                       │      ├ Description     : When an OAuth2 bearer token is used for an HTTP(S) transfer,
│                       │      │                    and that transfer
│                       │      │                   performs a cross-protocol redirect to a second URL that uses
│                       │      │                    an IMAP, LDAP,
│                       │      │                   POP3 or SMTP scheme, curl might wrongly pass on the bearer
│                       │      │                   token to the new
│                       │      │                   target host. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-601 
│                       │      ├ VendorSeverity   ╭ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ julia      : 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/01/07/4 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2025-14524 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-14524.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2025-14524.json 
│                       │      │                  ├ [4]: https://github.com/advisories/GHSA-g897-jvjx-78vg 
│                       │      │                  ├ [5]: https://hackerone.com/reports/3459417 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2025-14524 
│                       │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-8062-1 
│                       │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2025-14524 
│                       │      ├ PublishedDate   : 2026-01-08T10:15:46.607Z 
│                       │      ╰ LastModifiedDate: 2026-01-20T14:53:11.017Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2025-14819 
│                       │      ├ PkgID           : libcurl@8.17.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.17.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .23.4 
│                       │      │                  ╰ UID : 67c003c6efbeb161 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-14819 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:912657a98cb09a68da7deef19ccf7f1034c8b7163a64cd4c0b82c
│                       │      │                   3b1b4d9aab3 
│                       │      ├ Title           : curl: libcurl: Improper certificate validation due to cached
│                       │      │                    TLS settings reuse 
│                       │      ├ Description     : When doing TLS related transfers with reused easy or multi
│                       │      │                   handles and
│                       │      │                   altering the  `CURLSSLOPT_NO_PARTIALCHAIN` option, libcurl
│                       │      │                   could accidentally
│                       │      │                   reuse a CA store cached in memory for which the partial
│                       │      │                   chain option was
│                       │      │                   reversed. Contrary to the user's wishes and expectations.
│                       │      │                   This could make
│                       │      │                   libcurl find and accept a trust chain that it otherwise
│                       │      │                   would not. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-295 
│                       │      ├ VendorSeverity   ╭ amazon: 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.8 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/01/07/5 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2025-14819 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-14819.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2025-14819.json 
│                       │      │                  ├ [4]: https://github.com/advisories/GHSA-vqhr-m87q-9jqh 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2025-14819 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-8062-1 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2025-14819 
│                       │      ├ PublishedDate   : 2026-01-08T10:15:46.73Z 
│                       │      ╰ LastModifiedDate: 2026-01-20T14:51:26.263Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-1965 
│                       │      ├ PkgID           : libcurl@8.17.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.17.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .23.4 
│                       │      │                  ╰ UID : 67c003c6efbeb161 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-1965 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:6402380694f3e4df1fec3846a2fa9ec04e96e34a5d6445ce8b945
│                       │      │                   1a68ed94500 
│                       │      ├ Title           : curl: curl: Authentication bypass due to incorrect
│                       │      │                   connection reuse with Negotiate authentication 
│                       │      ├ Description     : libcurl can in some circumstances reuse the wrong connection
│                       │      │                    when asked to do
│                       │      │                   an Negotiate-authenticated HTTP or HTTPS request.
│                       │      │                   
│                       │      │                   libcurl features a pool of recent connections so that
│                       │      │                   subsequent requests can
│                       │      │                   reuse an existing connection to avoid overhead.
│                       │      │                   When reusing a connection a range of criterion must first be
│                       │      │                    met. Due to a
│                       │      │                   logical error in the code, a request that was issued by an
│                       │      │                   application could
│                       │      │                   wrongfully reuse an existing connection to the same server
│                       │      │                   that was
│                       │      │                   authenticated using different credentials. One underlying
│                       │      │                   reason being that
│                       │      │                   Negotiate sometimes authenticates *connections* and not
│                       │      │                   *requests*, contrary
│                       │      │                   to how HTTP is designed to work.
│                       │      │                   An application that allows Negotiate authentication to a
│                       │      │                   server (that responds
│                       │      │                   wanting Negotiate) with `user1:password1` and then does
│                       │      │                   another operation to
│                       │      │                   the same server also using Negotiate but with
│                       │      │                   `user2:password2` (while the
│                       │      │                   previous connection is still alive) - the second request
│                       │      │                   wrongly reused the
│                       │      │                   same connection and since it then sees that the Negotiate
│                       │      │                   negotiation is
│                       │      │                   already made, it just sends the request over that connection
│                       │      │                    thinking it uses
│                       │      │                   the user2 credentials when it is in fact still using the
│                       │      │                   connection
│                       │      │                   authenticated for user1...
│                       │      │                   The set of authentication methods to use is set with 
│                       │      │                   `CURLOPT_HTTPAUTH`.
│                       │      │                   Applications can disable libcurl's reuse of connections and
│                       │      │                   thus mitigate this
│                       │      │                   problem, by using one of the following libcurl options to
│                       │      │                   alter how
│                       │      │                   connections are or are not reused: `CURLOPT_FRESH_CONNECT`,
│                       │      │                   `CURLOPT_MAXCONNECTS` and `CURLMOPT_MAX_HOST_CONNECTIONS`
│                       │      │                   (if using the
│                       │      │                   curl_multi API). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-305 
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.8 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-1965 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2026-1965.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-1965.json 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-1965 
│                       │      │                  ├ [4]: https://ubuntu.com/security/notices/USN-8084-1 
│                       │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-8099-1 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-1965 
│                       │      ├ PublishedDate   : 2026-03-11T11:15:59.177Z 
│                       │      ╰ LastModifiedDate: 2026-03-12T14:11:19.07Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-3783 
│                       │      ├ PkgID           : libcurl@8.17.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.17.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .23.4 
│                       │      │                  ╰ UID : 67c003c6efbeb161 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3783 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:9c76f60e898eb0bb9f94a6694a56596b56af7d1d4a44eaad65a37
│                       │      │                   343374c6059 
│                       │      ├ Title           : curl: curl: Information disclosure via OAuth2 bearer token
│                       │      │                   leakage during HTTP(S) redirect 
│                       │      ├ Description     : When an OAuth2 bearer token is used for an HTTP(S) transfer,
│                       │      │                    and that transfer
│                       │      │                   performs a redirect to a second URL, curl could leak that
│                       │      │                   token to the second
│                       │      │                   hostname under some circumstances.
│                       │      │                   
│                       │      │                   If the hostname that the first request is redirected to has
│                       │      │                   information in the
│                       │      │                   used .netrc file, with either of the `machine` or `default`
│                       │      │                   keywords, curl
│                       │      │                   would pass on the bearer token set for the first host also
│                       │      │                   to the second one. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-522 
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.7 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/03/11/2 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3783 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-3783.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-3783.json 
│                       │      │                  ├ [4]: https://github.com/advisories/GHSA-8whr-249c-vfjp 
│                       │      │                  ├ [5]: https://hackerone.com/reports/3583983 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-3783 
│                       │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-8084-1 
│                       │      │                  ├ [8]: https://ubuntu.com/security/notices/USN-8099-1 
│                       │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2026-3783 
│                       │      ├ PublishedDate   : 2026-03-11T11:16:00.08Z 
│                       │      ╰ LastModifiedDate: 2026-03-12T14:10:37.3Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-3784 
│                       │      ├ PkgID           : libcurl@8.17.0-r1 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.17.0-r1?arch=x86_64&distro=3
│                       │      │                  │       .23.4 
│                       │      │                  ╰ UID : 67c003c6efbeb161 
│                       │      ├ InstalledVersion: 8.17.0-r1 
│                       │      ├ FixedVersion    : 8.19.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                       │      │                  │         b7973fb793f01a8fa17a 
│                       │      │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                       │      │                            dc80e56ed091d50ea4fa 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3784 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:354abe8a9a680f1903f72fedf63dd8952e7bb5531b56995a41882
│                       │      │                   62ed4c662f1 
│                       │      ├ Title           : curl: curl: Unauthorized access due to improper HTTP proxy
│                       │      │                   connection reuse 
│                       │      ├ Description     : curl would wrongly reuse an existing HTTP proxy connection
│                       │      │                   doing CONNECT to a
│                       │      │                   server, even if the new request uses different credentials
│                       │      │                   for the HTTP proxy.
│                       │      │                   The proper behavior is to create or use a separate
│                       │      │                   connection. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-305 
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/03/11/3 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3784 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2026-3784.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2026-3784.json 
│                       │      │                  ├ [4]: https://github.com/advisories/GHSA-5q3w-6p3j-mw6p 
│                       │      │                  ├ [5]: https://hackerone.com/reports/3584903 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-3784 
│                       │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-8084-1 
│                       │      │                  ├ [8]: https://ubuntu.com/security/notices/USN-8099-1 
│                       │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2026-3784 
│                       │      ├ PublishedDate   : 2026-03-11T11:16:00.437Z 
│                       │      ╰ LastModifiedDate: 2026-03-12T14:09:50.47Z 
│                       ╰ [13] ╭ VulnerabilityID : CVE-2026-3805 
│                              ├ PkgID           : libcurl@8.17.0-r1 
│                              ├ PkgName         : libcurl 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.17.0-r1?arch=x86_64&distro=3
│                              │                  │       .23.4 
│                              │                  ╰ UID : 67c003c6efbeb161 
│                              ├ InstalledVersion: 8.17.0-r1 
│                              ├ FixedVersion    : 8.19.0-r0 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:10c96cd644d505a2b01a4d9db0f510c23d8dfdcbcd08
│                              │                  │         b7973fb793f01a8fa17a 
│                              │                  ╰ DiffID: sha256:44bb69a06a6b54cfbe5fcf784d4bb8c0b0c923b4334e
│                              │                            dc80e56ed091d50ea4fa 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3805 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Fingerprint     : sha256:59eda643c52868e0e71ea8e2d100b3967a25afc8d9dc6eeb85bf6
│                              │                   58cf7cc1ad7 
│                              ├ Title           : curl: curl: Arbitrary code execution or Denial of Service
│                              │                   via use-after-free in SMB request handling 
│                              ├ Description     : When doing a second SMB request to the same host again, curl
│                              │                    would wrongly use
│                              │                   a data pointer pointing into already freed memory. 
│                              ├ Severity        : MEDIUM 
│                              ├ CweIDs           ─ [0]: CWE-416 
│                              ├ VendorSeverity   ╭ amazon: 2 
│                              │                  ├ julia : 3 
│                              │                  ├ photon: 3 
│                              │                  ├ redhat: 2 
│                              │                  ╰ ubuntu: 2 
│                              ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                              │                  │        │           /A:H 
│                              │                  │        ╰ V3Score : 7.5 
│                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L
│                              │                           │           /A:L 
│                              │                           ╰ V3Score : 6.3 
│                              ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/03/11/4 
│                              │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3805 
│                              │                  ├ [2]: https://curl.se/docs/CVE-2026-3805.html 
│                              │                  ├ [3]: https://curl.se/docs/CVE-2026-3805.json 
│                              │                  ├ [4]: https://github.com/advisories/GHSA-2289-hhfc-p684 
│                              │                  ├ [5]: https://hackerone.com/reports/3591944 
│                              │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-3805 
│                              │                  ├ [7]: https://ubuntu.com/security/notices/USN-8084-1 
│                              │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2026-3805 
│                              ├ PublishedDate   : 2026-03-11T11:16:00.967Z 
│                              ╰ LastModifiedDate: 2026-03-12T14:08:56.79Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages 
```
