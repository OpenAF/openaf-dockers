````yaml
╭ [0] ╭ Target         : openaf/oaf:8-latest (alpine 3.20.3) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2024-11053 
│                       │      ├ PkgID           : curl@8.10.1-r0 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.10.1-r0?arch=x86_64&distro=3.20.3 
│                       │      │                  ╰ UID : f07e06b001c6f80a 
│                       │      ├ InstalledVersion: 8.10.1-r0 
│                       │      ├ FixedVersion    : 8.11.1-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-11053 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : curl: curl netrc password leak 
│                       │      ├ Description     : When asked to both use a `.netrc` file for credentials and
│                       │      │                   to follow HTTP
│                       │      │                   redirects, curl could leak the password used for the first
│                       │      │                   host to the
│                       │      │                   followed-to host under certain circumstances.
│                       │      │                   
│                       │      │                   This flaw only manifests itself if the netrc file has an
│                       │      │                   entry that matches
│                       │      │                   the redirect target hostname but the entry either omits just
│                       │      │                    the password or
│                       │      │                   omits both login and password. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ azure      : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2024/12/11/1 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-11053 
│                       │      │                  ├ [2] : https://curl.se/docs/CVE-2024-11053.html 
│                       │      │                  ├ [3] : https://curl.se/docs/CVE-2024-11053.json 
│                       │      │                  ├ [4] : https://hackerone.com/reports/2829063 
│                       │      │                  ├ [5] : https://nvd.nist.gov/vuln/detail/CVE-2024-11053 
│                       │      │                  ├ [6] : https://security.netapp.com/advisory/ntap-20250124-00
│                       │      │                  │       12/ 
│                       │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-20250131-00
│                       │      │                  │       03/ 
│                       │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-7162-1 
│                       │      │                  ├ [9] : https://www.cve.org/CVERecord?id=CVE-2024-11053 
│                       │      │                  ╰ [10]: https://www.oracle.com/security-alerts/cpujan2025.htm
│                       │      │                          l#AppendixMSQL 
│                       │      ├ PublishedDate   : 2024-12-11T08:15:05.307Z 
│                       │      ╰ LastModifiedDate: 2025-01-31T15:15:12.4Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2024-9681 
│                       │      ├ PkgID           : curl@8.10.1-r0 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.10.1-r0?arch=x86_64&distro=3.20.3 
│                       │      │                  ╰ UID : f07e06b001c6f80a 
│                       │      ├ InstalledVersion: 8.10.1-r0 
│                       │      ├ FixedVersion    : 8.11.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-9681 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : curl: HSTS subdomain overwrites parent cache entry 
│                       │      ├ Description     : When curl is asked to use HSTS, the expiry time for a
│                       │      │                   subdomain might
│                       │      │                   overwrite a parent domain's cache entry, making it end
│                       │      │                   sooner or later than
│                       │      │                   otherwise intended.
│                       │      │                   
│                       │      │                   This affects curl using applications that enable HSTS and
│                       │      │                   use URLs with the
│                       │      │                   insecure `HTTP://` scheme and perform transfers with hosts
│                       │      │                   like
│                       │      │                   `x.example.com` as well as `example.com` where the first
│                       │      │                   host is a subdomain
│                       │      │                   of the second host.
│                       │      │                   (The HSTS cache either needs to have been populated manually
│                       │      │                    or there needs to
│                       │      │                   have been previous HTTPS accesses done as the cache needs to
│                       │      │                    have entries for
│                       │      │                   the domains involved to trigger this problem.)
│                       │      │                   When `x.example.com` responds with
│                       │      │                   `Strict-Transport-Security:` headers, this
│                       │      │                   bug can make the subdomain's expiry timeout *bleed over* and
│                       │      │                    get set for the
│                       │      │                   parent domain `example.com` in curl's HSTS cache.
│                       │      │                   The result of a triggered bug is that HTTP accesses to
│                       │      │                   `example.com` get
│                       │      │                   converted to HTTPS for a different period of time than what
│                       │      │                   was asked for by
│                       │      │                   the origin server. If `example.com` for example stops
│                       │      │                   supporting HTTPS at its
│                       │      │                   expiry time, curl might then fail to access
│                       │      │                   `http://example.com` until the
│                       │      │                   (wrongly set) timeout expires. This bug can also expire the
│                       │      │                   parent's entry
│                       │      │                   *earlier*, thus making curl inadvertently switch back to
│                       │      │                   insecure HTTP earlier
│                       │      │                   than otherwise intended. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-697 
│                       │      ├ VendorSeverity   ╭ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 2.5 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/11/06/2 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2024-9681 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2024-9681.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2024-9681.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/2764830 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2024-9681 
│                       │      │                  ├ [6]: https://security.netapp.com/advisory/ntap-20241213-0006/ 
│                       │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-7104-1 
│                       │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2024-9681 
│                       │      ├ PublishedDate   : 2024-11-06T08:15:03.74Z 
│                       │      ╰ LastModifiedDate: 2024-12-13T14:15:22.953Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2024-9143 
│                       │      ├ PkgID           : libcrypto3@3.3.2-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.3.2-r0?arch=x86_64&distro
│                       │      │                  │       =3.20.3 
│                       │      │                  ╰ UID : 33eb4551a5ab015e 
│                       │      ├ InstalledVersion: 3.3.2-r0 
│                       │      ├ FixedVersion    : 3.3.2-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-9143 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openssl: Low-level invalid GF(2^m) parameters lead to OOB
│                       │      │                   memory access 
│                       │      ├ Description     : Issue summary: Use of the low-level GF(2^m) elliptic curve
│                       │      │                   APIs with untrusted
│                       │      │                   explicit values for the field polynomial can lead to
│                       │      │                   out-of-bounds memory reads
│                       │      │                   or writes.
│                       │      │                   
│                       │      │                   Impact summary: Out of bound memory writes can lead to an
│                       │      │                   application crash or
│                       │      │                   even a possibility of a remote code execution, however, in
│                       │      │                   all the protocols
│                       │      │                   involving Elliptic Curve Cryptography that we're aware of,
│                       │      │                   either only "named
│                       │      │                   curves" are supported, or, if explicit curve parameters are
│                       │      │                   supported, they
│                       │      │                   specify an X9.62 encoding of binary (GF(2^m)) curves that
│                       │      │                   can't represent
│                       │      │                   problematic input values. Thus the likelihood of existence
│                       │      │                   of a vulnerable
│                       │      │                   application is low.
│                       │      │                   In particular, the X9.62 encoding is used for ECC keys in
│                       │      │                   X.509 certificates,
│                       │      │                   so problematic inputs cannot occur in the context of
│                       │      │                   processing X.509
│                       │      │                   certificates.  Any problematic use-cases would have to be
│                       │      │                   using an "exotic"
│                       │      │                   curve encoding.
│                       │      │                   The affected APIs include: EC_GROUP_new_curve_GF2m(),
│                       │      │                   EC_GROUP_new_from_params(),
│                       │      │                   and various supporting BN_GF2m_*() functions.
│                       │      │                   Applications working with "exotic" explicit binary (GF(2^m))
│                       │      │                    curve parameters,
│                       │      │                   that make it possible to represent invalid field polynomials
│                       │      │                    with a zero
│                       │      │                   constant term, via the above or similar APIs, may terminate
│                       │      │                   abruptly as a
│                       │      │                   result of reading or writing outside of array bounds. 
│                       │      │                   Remote code execution
│                       │      │                   cannot easily be ruled out.
│                       │      │                   The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected
│                       │      │                   by this issue. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-787 
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2024/10/16/1 
│                       │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2024/10/23/1 
│                       │      │                  ├ [2] : http://www.openwall.com/lists/oss-security/2024/10/24/1 
│                       │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2024-9143 
│                       │      │                  ├ [4] : https://github.com/openssl/openssl/commit/72ae83ad214
│                       │      │                  │       d2eef262461365a1975707f862712 
│                       │      │                  ├ [5] : https://github.com/openssl/openssl/commit/bc7e04d7c8d
│                       │      │                  │       509fb78fc0e285aa948fb0da04700 
│                       │      │                  ├ [6] : https://github.com/openssl/openssl/commit/c0d3e4d32d2
│                       │      │                  │       805f49bec30547f225bc4d092e1f4 
│                       │      │                  ├ [7] : https://github.com/openssl/openssl/commit/fdf6723362c
│                       │      │                  │       a51bd883295efe206cb5b1cfa5154 
│                       │      │                  ├ [8] : https://github.openssl.org/openssl/extended-releases/
│                       │      │                  │       commit/8efc0cbaa8ebba8e116f7b81a876a4123594d86a 
│                       │      │                  ├ [9] : https://github.openssl.org/openssl/extended-releases/
│                       │      │                  │       commit/9d576994cec2b7aa37a91740ea7e680810957e41 
│                       │      │                  ├ [10]: https://nvd.nist.gov/vuln/detail/CVE-2024-9143 
│                       │      │                  ├ [11]: https://openssl-library.org/news/secadv/20241016.txt 
│                       │      │                  ├ [12]: https://security.netapp.com/advisory/ntap-20241101-00
│                       │      │                  │       01/ 
│                       │      │                  ╰ [13]: https://www.cve.org/CVERecord?id=CVE-2024-9143 
│                       │      ├ PublishedDate   : 2024-10-16T17:15:18.13Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T09:54:04.817Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2024-11053 
│                       │      ├ PkgID           : libcurl@8.10.1-r0 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.10.1-r0?arch=x86_64&distro=3
│                       │      │                  │       .20.3 
│                       │      │                  ╰ UID : 49f1e7608626c36e 
│                       │      ├ InstalledVersion: 8.10.1-r0 
│                       │      ├ FixedVersion    : 8.11.1-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-11053 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : curl: curl netrc password leak 
│                       │      ├ Description     : When asked to both use a `.netrc` file for credentials and
│                       │      │                   to follow HTTP
│                       │      │                   redirects, curl could leak the password used for the first
│                       │      │                   host to the
│                       │      │                   followed-to host under certain circumstances.
│                       │      │                   
│                       │      │                   This flaw only manifests itself if the netrc file has an
│                       │      │                   entry that matches
│                       │      │                   the redirect target hostname but the entry either omits just
│                       │      │                    the password or
│                       │      │                   omits both login and password. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ azure      : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2024/12/11/1 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-11053 
│                       │      │                  ├ [2] : https://curl.se/docs/CVE-2024-11053.html 
│                       │      │                  ├ [3] : https://curl.se/docs/CVE-2024-11053.json 
│                       │      │                  ├ [4] : https://hackerone.com/reports/2829063 
│                       │      │                  ├ [5] : https://nvd.nist.gov/vuln/detail/CVE-2024-11053 
│                       │      │                  ├ [6] : https://security.netapp.com/advisory/ntap-20250124-00
│                       │      │                  │       12/ 
│                       │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-20250131-00
│                       │      │                  │       03/ 
│                       │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-7162-1 
│                       │      │                  ├ [9] : https://www.cve.org/CVERecord?id=CVE-2024-11053 
│                       │      │                  ╰ [10]: https://www.oracle.com/security-alerts/cpujan2025.htm
│                       │      │                          l#AppendixMSQL 
│                       │      ├ PublishedDate   : 2024-12-11T08:15:05.307Z 
│                       │      ╰ LastModifiedDate: 2025-01-31T15:15:12.4Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2024-9681 
│                       │      ├ PkgID           : libcurl@8.10.1-r0 
│                       │      ├ PkgName         : libcurl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.10.1-r0?arch=x86_64&distro=3
│                       │      │                  │       .20.3 
│                       │      │                  ╰ UID : 49f1e7608626c36e 
│                       │      ├ InstalledVersion: 8.10.1-r0 
│                       │      ├ FixedVersion    : 8.11.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-9681 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : curl: HSTS subdomain overwrites parent cache entry 
│                       │      ├ Description     : When curl is asked to use HSTS, the expiry time for a
│                       │      │                   subdomain might
│                       │      │                   overwrite a parent domain's cache entry, making it end
│                       │      │                   sooner or later than
│                       │      │                   otherwise intended.
│                       │      │                   
│                       │      │                   This affects curl using applications that enable HSTS and
│                       │      │                   use URLs with the
│                       │      │                   insecure `HTTP://` scheme and perform transfers with hosts
│                       │      │                   like
│                       │      │                   `x.example.com` as well as `example.com` where the first
│                       │      │                   host is a subdomain
│                       │      │                   of the second host.
│                       │      │                   (The HSTS cache either needs to have been populated manually
│                       │      │                    or there needs to
│                       │      │                   have been previous HTTPS accesses done as the cache needs to
│                       │      │                    have entries for
│                       │      │                   the domains involved to trigger this problem.)
│                       │      │                   When `x.example.com` responds with
│                       │      │                   `Strict-Transport-Security:` headers, this
│                       │      │                   bug can make the subdomain's expiry timeout *bleed over* and
│                       │      │                    get set for the
│                       │      │                   parent domain `example.com` in curl's HSTS cache.
│                       │      │                   The result of a triggered bug is that HTTP accesses to
│                       │      │                   `example.com` get
│                       │      │                   converted to HTTPS for a different period of time than what
│                       │      │                   was asked for by
│                       │      │                   the origin server. If `example.com` for example stops
│                       │      │                   supporting HTTPS at its
│                       │      │                   expiry time, curl might then fail to access
│                       │      │                   `http://example.com` until the
│                       │      │                   (wrongly set) timeout expires. This bug can also expire the
│                       │      │                   parent's entry
│                       │      │                   *earlier*, thus making curl inadvertently switch back to
│                       │      │                   insecure HTTP earlier
│                       │      │                   than otherwise intended. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-697 
│                       │      ├ VendorSeverity   ╭ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 2.5 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/11/06/2 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2024-9681 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2024-9681.html 
│                       │      │                  ├ [3]: https://curl.se/docs/CVE-2024-9681.json 
│                       │      │                  ├ [4]: https://hackerone.com/reports/2764830 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2024-9681 
│                       │      │                  ├ [6]: https://security.netapp.com/advisory/ntap-20241213-0006/ 
│                       │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-7104-1 
│                       │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2024-9681 
│                       │      ├ PublishedDate   : 2024-11-06T08:15:03.74Z 
│                       │      ╰ LastModifiedDate: 2024-12-13T14:15:22.953Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2024-50602 
│                       │      ├ PkgID           : libexpat@2.6.3-r0 
│                       │      ├ PkgName         : libexpat 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libexpat@2.6.3-r0?arch=x86_64&distro=3
│                       │      │                  │       .20.3 
│                       │      │                  ╰ UID : f84bf5e5b4df8fb1 
│                       │      ├ InstalledVersion: 2.6.3-r0 
│                       │      ├ FixedVersion    : 2.6.4-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-50602 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : libexpat: expat: DoS via XML_ResumeParser 
│                       │      ├ Description     : An issue was discovered in libexpat before 2.6.4. There is a
│                       │      │                    crash within the XML_ResumeParser function because
│                       │      │                   XML_StopParser can stop/suspend an unstarted parser. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-754 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 5.9 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:H 
│                       │      │                            ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9541 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-50602 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2321987 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2321987 
│                       │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-50602 
│                       │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2024-9541.html 
│                       │      │                  ├ [6] : https://errata.rockylinux.org/RLSA-2024:9502 
│                       │      │                  ├ [7] : https://github.com/libexpat/libexpat/pull/915 
│                       │      │                  ├ [8] : https://linux.oracle.com/cve/CVE-2024-50602.html 
│                       │      │                  ├ [9] : https://linux.oracle.com/errata/ELSA-2024-9541.html 
│                       │      │                  ├ [10]: https://nvd.nist.gov/vuln/detail/CVE-2024-50602 
│                       │      │                  ╰ [11]: https://www.cve.org/CVERecord?id=CVE-2024-50602 
│                       │      ├ PublishedDate   : 2024-10-27T05:15:04.09Z 
│                       │      ╰ LastModifiedDate: 2024-10-30T18:35:16.237Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2024-9143 
│                       │      ├ PkgID           : libssl3@3.3.2-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.3.2-r0?arch=x86_64&distro=3.
│                       │      │                  │       20.3 
│                       │      │                  ╰ UID : aa5719d6e39bba43 
│                       │      ├ InstalledVersion: 3.3.2-r0 
│                       │      ├ FixedVersion    : 3.3.2-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-9143 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openssl: Low-level invalid GF(2^m) parameters lead to OOB
│                       │      │                   memory access 
│                       │      ├ Description     : Issue summary: Use of the low-level GF(2^m) elliptic curve
│                       │      │                   APIs with untrusted
│                       │      │                   explicit values for the field polynomial can lead to
│                       │      │                   out-of-bounds memory reads
│                       │      │                   or writes.
│                       │      │                   
│                       │      │                   Impact summary: Out of bound memory writes can lead to an
│                       │      │                   application crash or
│                       │      │                   even a possibility of a remote code execution, however, in
│                       │      │                   all the protocols
│                       │      │                   involving Elliptic Curve Cryptography that we're aware of,
│                       │      │                   either only "named
│                       │      │                   curves" are supported, or, if explicit curve parameters are
│                       │      │                   supported, they
│                       │      │                   specify an X9.62 encoding of binary (GF(2^m)) curves that
│                       │      │                   can't represent
│                       │      │                   problematic input values. Thus the likelihood of existence
│                       │      │                   of a vulnerable
│                       │      │                   application is low.
│                       │      │                   In particular, the X9.62 encoding is used for ECC keys in
│                       │      │                   X.509 certificates,
│                       │      │                   so problematic inputs cannot occur in the context of
│                       │      │                   processing X.509
│                       │      │                   certificates.  Any problematic use-cases would have to be
│                       │      │                   using an "exotic"
│                       │      │                   curve encoding.
│                       │      │                   The affected APIs include: EC_GROUP_new_curve_GF2m(),
│                       │      │                   EC_GROUP_new_from_params(),
│                       │      │                   and various supporting BN_GF2m_*() functions.
│                       │      │                   Applications working with "exotic" explicit binary (GF(2^m))
│                       │      │                    curve parameters,
│                       │      │                   that make it possible to represent invalid field polynomials
│                       │      │                    with a zero
│                       │      │                   constant term, via the above or similar APIs, may terminate
│                       │      │                   abruptly as a
│                       │      │                   result of reading or writing outside of array bounds. 
│                       │      │                   Remote code execution
│                       │      │                   cannot easily be ruled out.
│                       │      │                   The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected
│                       │      │                   by this issue. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-787 
│                       │      ├ VendorSeverity   ╭ amazon: 3 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2024/10/16/1 
│                       │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2024/10/23/1 
│                       │      │                  ├ [2] : http://www.openwall.com/lists/oss-security/2024/10/24/1 
│                       │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2024-9143 
│                       │      │                  ├ [4] : https://github.com/openssl/openssl/commit/72ae83ad214
│                       │      │                  │       d2eef262461365a1975707f862712 
│                       │      │                  ├ [5] : https://github.com/openssl/openssl/commit/bc7e04d7c8d
│                       │      │                  │       509fb78fc0e285aa948fb0da04700 
│                       │      │                  ├ [6] : https://github.com/openssl/openssl/commit/c0d3e4d32d2
│                       │      │                  │       805f49bec30547f225bc4d092e1f4 
│                       │      │                  ├ [7] : https://github.com/openssl/openssl/commit/fdf6723362c
│                       │      │                  │       a51bd883295efe206cb5b1cfa5154 
│                       │      │                  ├ [8] : https://github.openssl.org/openssl/extended-releases/
│                       │      │                  │       commit/8efc0cbaa8ebba8e116f7b81a876a4123594d86a 
│                       │      │                  ├ [9] : https://github.openssl.org/openssl/extended-releases/
│                       │      │                  │       commit/9d576994cec2b7aa37a91740ea7e680810957e41 
│                       │      │                  ├ [10]: https://nvd.nist.gov/vuln/detail/CVE-2024-9143 
│                       │      │                  ├ [11]: https://openssl-library.org/news/secadv/20241016.txt 
│                       │      │                  ├ [12]: https://security.netapp.com/advisory/ntap-20241101-00
│                       │      │                  │       01/ 
│                       │      │                  ╰ [13]: https://www.cve.org/CVERecord?id=CVE-2024-9143 
│                       │      ├ PublishedDate   : 2024-10-16T17:15:18.13Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T09:54:04.817Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2024-21147 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21147 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: RangeCheckElimination array index overflow (8323231) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11,
│                       │      │                   21.0.3, 22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3,
│                       │      │                   22.0.1; Oracle GraalVM Enterprise Edition: 20.3.14 and 
│                       │      │                   21.3.10. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data as well as  unauthorized
│                       │      │                   access to critical data or complete access to all Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-200 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21147 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21147.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21147 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21147 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:16.377Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T08:53:52.63Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2024-21140 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21140 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Range Check Elimination (RCE) pre-loop limit
│                       │      │                   overflow (8320548) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11,
│                       │      │                   21.0.3, 22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3,
│                       │      │                   22.0.1; Oracle GraalVM Enterprise Edition: 20.3.14 and 
│                       │      │                   21.3.10. Difficult to exploit vulnerability allows
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
│                       │      │                   3.1 Base Score 4.8 (Confidentiality and Integrity impacts). 
│                       │      │                    CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N)
│                       │      │                   . 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-200 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21140 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21140.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21140 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21140 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:15.043Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T08:53:51.75Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2024-21145 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21145 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Out-of-bounds access in 2D image handling (8324559) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11, 21.0.3,
│                       │      │                    22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3, 22.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.14 and  21.3.10.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data as
│                       │      │                   well as  unauthorized read access to a subset of Oracle Java
│                       │      │                    SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 4.8
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.8 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21145 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21145.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21145 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21145 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:15.993Z 
│                       │      ╰ LastModifiedDate: 2024-12-16T20:13:37.007Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2024-21235 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.432.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21235 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : JDK: Integer conversion error leads to incorrect range check
│                       │      │                    (8332644) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u421, 8u421-perf, 11.0.24, 17.0.12,
│                       │      │                   21.0.4, 23;   Oracle GraalVM for JDK: 17.0.12, 21.0.4, 23;  
│                       │      │                    Oracle GraalVM Enterprise Edition: 20.3.15 and  21.3.11.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data as
│                       │      │                   well as  unauthorized read access to a subset of Oracle Java
│                       │      │                    SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 4.8
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:8127 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21235 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2251025 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2318524 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2318526 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2318530 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2318534 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2251025 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2318524 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2318526 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2318530 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2318534 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       23-48161 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21208 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21210 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21217 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21235 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-8127.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:8127 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21235.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-8127.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21235 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7099-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7124-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21235 
│                       │      │                  ╰ [28]: https://www.oracle.com/security-alerts/cpuoct2024.html 
│                       │      ├ PublishedDate   : 2024-10-15T20:15:12.643Z 
│                       │      ╰ LastModifiedDate: 2024-10-18T18:30:26.097Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2024-21011 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21011 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: long Exception message leading to crash (8319851) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u401, 8u401-perf, 11.0.22, 17.0.10,
│                       │      │                   21.0.2, 22; Oracle GraalVM for JDK: 17.0.10, 21.0.2, 22;  
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.13 and  21.3.9.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
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
│                       │      │                   3.1 Base Score 3.7 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 1 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:1828 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21011 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2274975 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2274977 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2275003 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2274975 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2274977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2275003 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21011 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21012 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21068 
│                       │      │                  ├ [11]: https://errata.almalinux.org/9/ALSA-2024-1828.html 
│                       │      │                  ├ [12]: https://errata.rockylinux.org/RLSA-2024:1828 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2024-21011.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2024-1828.html 
│                       │      │                  ├ [15]: https://lists.debian.org/debian-lts-announce/2024/04/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2024-21011 
│                       │      │                  ├ [17]: https://security.netapp.com/advisory/ntap-20240426-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-6810-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-6811-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6812-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-6813-1 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2024-21011 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2024.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2024.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-04-16T22:15:15.437Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T21:15:17.52Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2024-21068 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21068 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: integer overflow in C1 compiler address generation
│                       │      │                   (8322122) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u401-perf, 11.0.22, 17.0.10, 21.0.2,
│                       │      │                   22; Oracle GraalVM for JDK: 17.0.10, 21.0.2 and  22; Oracle
│                       │      │                   GraalVM Enterprise Edition: 21.3.9. Difficult to exploit
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via multiple protocols to compromise Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized update, insert or delete access to some of
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   3.7 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 1 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:1828 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21068 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2274975 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2274977 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2275003 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2274975 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2274977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2275003 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21011 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21012 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21068 
│                       │      │                  ├ [11]: https://errata.almalinux.org/9/ALSA-2024-1828.html 
│                       │      │                  ├ [12]: https://errata.rockylinux.org/RLSA-2024:1828 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2024-21068.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2024-1828.html 
│                       │      │                  ├ [15]: https://lists.debian.org/debian-lts-announce/2024/04/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2024-21068 
│                       │      │                  ├ [17]: https://security.netapp.com/advisory/ntap-20240426-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-6810-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-6811-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6812-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-6813-1 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2024-21068 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2024.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2024.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-04-16T22:15:25.307Z 
│                       │      ╰ LastModifiedDate: 2024-12-06T19:22:57.927Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2024-21085 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21085 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Pack200 excessive memory allocation (8322114) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM
│                       │      │                   Enterprise Edition product of Oracle Java SE (component:
│                       │      │                   Concurrency).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u401, 8u401-perf, 11.0.22; Oracle GraalVM
│                       │      │                   Enterprise Edition: 20.3.13 and  21.3.9. Difficult to
│                       │      │                   exploit vulnerability allows unauthenticated attacker with
│                       │      │                   network access via multiple protocols to compromise Oracle
│                       │      │                   Java SE, Oracle GraalVM Enterprise Edition.  Successful
│                       │      │                   attacks of this vulnerability can result in unauthorized
│                       │      │                   ability to cause a partial denial of service (partial DOS)
│                       │      │                   of Oracle Java SE, Oracle GraalVM Enterprise Edition. Note:
│                       │      │                   This vulnerability can be exploited by using APIs in the
│                       │      │                   specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 3.7 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 1 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:1822 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21085 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2274975 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2274977 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2275001 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2275003 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2275005 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2274975 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2274977 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2275001 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2275003 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2275005 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21011 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21012 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21068 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21085 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21094 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-1822.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:1822 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21085.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-1822.html 
│                       │      │                  ├ [21]: https://lists.debian.org/debian-lts-announce/2024/04/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2024-21085 
│                       │      │                  ├ [23]: https://security.netapp.com/advisory/ntap-20240426-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6810-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6811-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21085 
│                       │      │                  ├ [28]: https://www.oracle.com/security-alerts/cpuapr2024.html 
│                       │      │                  ╰ [29]: https://www.oracle.com/security-alerts/cpuapr2024.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-04-16T22:15:28.293Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T08:53:45.35Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2024-21094 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21094 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: C2 compilation fails with "Exceeded _node_regs
│                       │      │                   array" (8317507) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u401, 8u401-perf, 11.0.22, 17.0.10,
│                       │      │                   21.0.2, 22; Oracle GraalVM for JDK: 17.0.10, 21.0.2, 22;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.13 and  21.3.9.
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
│                       │      ├ CweIDs           ─ [0]: CWE-349 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 1 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:1825 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21094 
│                       │      │                  ├ [2] : https://bugs.openjdk.org/browse/JDK-8317507 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2274975 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2274977 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2275003 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2275005 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2274975 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2274977 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2275001 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2275003 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2275005 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21011 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21012 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21068 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21085 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21094 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-1825.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:1822 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21094.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-1825.html 
│                       │      │                  ├ [21]: https://lists.debian.org/debian-lts-announce/2024/04/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2024-21094 
│                       │      │                  ├ [23]: https://security.netapp.com/advisory/ntap-20240426-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6810-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6811-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6812-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-6813-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [29]: https://www.cve.org/CVERecord?id=CVE-2024-21094 
│                       │      │                  ├ [30]: https://www.oracle.com/security-alerts/cpuapr2024.html 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpuapr2024.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-04-16T22:15:29.857Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T08:53:46.35Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2024-21131 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21131 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: potential UTF8 size overflow (8314794) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11,
│                       │      │                   21.0.3, 22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3,
│                       │      │                   22.0.1; Oracle GraalVM Enterprise Edition: 20.3.14 and 
│                       │      │                   21.3.10. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized update,
│                       │      │                   insert or delete access to some of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability can be exploited
│                       │      │                   by using APIs in the specified Component, e.g., through a
│                       │      │                   web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 3.7
│                       │      │                   (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21131 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21131.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21131 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21131 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:13.21Z 
│                       │      ╰ LastModifiedDate: 2024-12-05T22:02:52.553Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2024-21138 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21138 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Excessive symbol length can lead to infinite loop
│                       │      │                   (8319859) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11,
│                       │      │                   21.0.3, 22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3,
│                       │      │                   22.0.1; Oracle GraalVM Enterprise Edition: 20.3.14 and 
│                       │      │                   21.3.10. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in unauthorized ability to
│                       │      │                   cause a partial denial of service (partial DOS) of Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability can be exploited by using
│                       │      │                   APIs in the specified Component, e.g., through a web service
│                       │      │                    which supplies data to the APIs. This vulnerability also
│                       │      │                   applies to Java deployments, typically in clients running
│                       │      │                   sandboxed Java Web Start applications or sandboxed Java
│                       │      │                   applets, that load and run untrusted code (e.g., code that
│                       │      │                   comes from the internet) and rely on the Java sandbox for
│                       │      │                   security. CVSS 3.1 Base Score 3.7 (Availability impacts). 
│                       │      │                   CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21138 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21138.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21138 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21138 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:14.62Z 
│                       │      ╰ LastModifiedDate: 2024-12-05T22:05:55.937Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2024-21144 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21144 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Pack200 increase loading time due to improper
│                       │      │                   header validation (8322106) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM
│                       │      │                   Enterprise Edition product of Oracle Java SE (component:
│                       │      │                   Concurrency).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u411, 8u411-perf, 11.0.23; Oracle GraalVM
│                       │      │                   Enterprise Edition: 20.3.14 and  21.3.10. Difficult to
│                       │      │                   exploit vulnerability allows unauthenticated attacker with
│                       │      │                   network access via multiple protocols to compromise Oracle
│                       │      │                   Java SE, Oracle GraalVM Enterprise Edition.  Successful
│                       │      │                   attacks of this vulnerability can result in unauthorized
│                       │      │                   ability to cause a partial denial of service (partial DOS)
│                       │      │                   of Oracle Java SE, Oracle GraalVM Enterprise Edition. Note:
│                       │      │                   This vulnerability applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. This vulnerability does not apply
│                       │      │                    to Java deployments, typically in servers, that load and
│                       │      │                   run only trusted code (e.g., code installed by an
│                       │      │                   administrator). CVSS 3.1 Base Score 3.7 (Availability
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ nvd        : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 3.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4567 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21144 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297964 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2024-4567.html 
│                       │      │                  ├ [9] : https://linux.oracle.com/cve/CVE-2024-21144.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/errata/ELSA-2024-4567.html 
│                       │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2024-21144 
│                       │      │                  ├ [12]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       07/ 
│                       │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-21144 
│                       │      │                  ╰ [18]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:15.81Z 
│                       │      ╰ LastModifiedDate: 2024-12-16T20:13:40.827Z 
│                       ├ [18] ╭ VulnerabilityID : CVE-2024-21208 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.432.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21208 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : JDK: HTTP client improper handling of maxHeaderSize (8328286) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Networking).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u421, 8u421-perf, 11.0.24,
│                       │      │                   17.0.12, 21.0.4, 23; Oracle GraalVM for JDK: 17.0.12,
│                       │      │                   21.0.4, 23; Oracle GraalVM Enterprise Edition: 20.3.15 and 
│                       │      │                   21.3.11. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in unauthorized ability to
│                       │      │                   cause a partial denial of service (partial DOS) of Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability applies to Java
│                       │      │                   deployments, typically in clients running sandboxed Java Web
│                       │      │                    Start applications or sandboxed Java applets, that load and
│                       │      │                    run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. This
│                       │      │                   vulnerability does not apply to Java deployments, typically
│                       │      │                   in servers, that load and run only trusted code (e.g., code
│                       │      │                   installed by an administrator). CVSS 3.1 Base Score 3.7
│                       │      │                   (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-203 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 1 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:8127 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21208 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2251025 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2318524 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2318526 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2318530 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2318534 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2251025 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2318524 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2318526 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2318530 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2318534 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       23-48161 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21208 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21210 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21217 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21235 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-8127.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:8127 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21208.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-8127.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21208 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7099-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7124-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21208 
│                       │      │                  ╰ [28]: https://www.oracle.com/security-alerts/cpuoct2024.html 
│                       │      ├ PublishedDate   : 2024-10-15T20:15:09.437Z 
│                       │      ╰ LastModifiedDate: 2024-10-31T13:35:05.287Z 
│                       ├ [19] ╭ VulnerabilityID : CVE-2024-21210 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.432.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21210 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : JDK: Array indexing integer overflow (8328544) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: Hotspot). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u421, 8u421-perf, 11.0.24, 17.0.12, 21.0.4 and  23.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE accessible data.
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
│                       │      ├ CweIDs           ─ [0]: CWE-203 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 1 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:8127 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21210 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2251025 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2318524 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2318526 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2318530 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2318534 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2251025 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2318524 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2318526 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2318530 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2318534 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       23-48161 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21208 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21210 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21217 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21235 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-8127.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:8127 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21210.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-8127.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21210 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7099-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7124-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21210 
│                       │      │                  ╰ [28]: https://www.oracle.com/security-alerts/cpuoct2024.html 
│                       │      ├ PublishedDate   : 2024-10-15T20:15:09.843Z 
│                       │      ╰ LastModifiedDate: 2024-10-31T13:35:06.037Z 
│                       ├ [20] ╭ VulnerabilityID : CVE-2024-21217 
│                       │      ├ PkgID           : openjdk8-jre@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre@8.402.06-r0?arch=x86_64&d
│                       │      │                  │       istro=3.20.3 
│                       │      │                  ╰ UID : 846de51689fe9413 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.432.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21217 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : JDK: Unbounded allocation leads to out-of-memory error
│                       │      │                   (8331446) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Serialization).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u421, 8u421-perf, 11.0.24,
│                       │      │                   17.0.12, 21.0.4, 23; Oracle GraalVM for JDK: 17.0.12,
│                       │      │                   21.0.4, 23; Oracle GraalVM Enterprise Edition: 20.3.15 and 
│                       │      │                   21.3.11. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in unauthorized ability to
│                       │      │                   cause a partial denial of service (partial DOS) of Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability can be exploited by using
│                       │      │                   APIs in the specified Component, e.g., through a web service
│                       │      │                    which supplies data to the APIs. This vulnerability also
│                       │      │                   applies to Java deployments, typically in clients running
│                       │      │                   sandboxed Java Web Start applications or sandboxed Java
│                       │      │                   applets, that load and run untrusted code (e.g., code that
│                       │      │                   comes from the internet) and rely on the Java sandbox for
│                       │      │                   security. CVSS 3.1 Base Score 3.7 (Availability impacts). 
│                       │      │                   CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 1 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:8127 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21217 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2251025 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2318524 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2318526 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2318530 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2318534 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2251025 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2318524 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2318526 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2318530 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2318534 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       23-48161 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21208 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21210 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21217 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21235 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-8127.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:8127 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21217.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-8127.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21217 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7099-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7124-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21217 
│                       │      │                  ╰ [28]: https://www.oracle.com/security-alerts/cpuoct2024.html 
│                       │      ├ PublishedDate   : 2024-10-15T20:15:11.197Z 
│                       │      ╰ LastModifiedDate: 2024-10-18T18:29:36.59Z 
│                       ├ [21] ╭ VulnerabilityID : CVE-2024-21147 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21147 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: RangeCheckElimination array index overflow (8323231) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11,
│                       │      │                   21.0.3, 22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3,
│                       │      │                   22.0.1; Oracle GraalVM Enterprise Edition: 20.3.14 and 
│                       │      │                   21.3.10. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data as well as  unauthorized
│                       │      │                   access to critical data or complete access to all Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-200 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21147 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21147.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21147 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21147 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:16.377Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T08:53:52.63Z 
│                       ├ [22] ╭ VulnerabilityID : CVE-2024-21140 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21140 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Range Check Elimination (RCE) pre-loop limit
│                       │      │                   overflow (8320548) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11,
│                       │      │                   21.0.3, 22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3,
│                       │      │                   22.0.1; Oracle GraalVM Enterprise Edition: 20.3.14 and 
│                       │      │                   21.3.10. Difficult to exploit vulnerability allows
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
│                       │      │                   3.1 Base Score 4.8 (Confidentiality and Integrity impacts). 
│                       │      │                    CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N)
│                       │      │                   . 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-200 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21140 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21140.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21140 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21140 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:15.043Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T08:53:51.75Z 
│                       ├ [23] ╭ VulnerabilityID : CVE-2024-21145 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21145 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Out-of-bounds access in 2D image handling (8324559) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11, 21.0.3,
│                       │      │                    22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3, 22.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.14 and  21.3.10.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data as
│                       │      │                   well as  unauthorized read access to a subset of Oracle Java
│                       │      │                    SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 4.8
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.8 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21145 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21145.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21145 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21145 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:15.993Z 
│                       │      ╰ LastModifiedDate: 2024-12-16T20:13:37.007Z 
│                       ├ [24] ╭ VulnerabilityID : CVE-2024-21235 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.432.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21235 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : JDK: Integer conversion error leads to incorrect range check
│                       │      │                    (8332644) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u421, 8u421-perf, 11.0.24, 17.0.12,
│                       │      │                   21.0.4, 23;   Oracle GraalVM for JDK: 17.0.12, 21.0.4, 23;  
│                       │      │                    Oracle GraalVM Enterprise Edition: 20.3.15 and  21.3.11.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data as
│                       │      │                   well as  unauthorized read access to a subset of Oracle Java
│                       │      │                    SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 4.8
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:8127 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21235 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2251025 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2318524 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2318526 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2318530 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2318534 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2251025 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2318524 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2318526 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2318530 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2318534 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       23-48161 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21208 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21210 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21217 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21235 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-8127.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:8127 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21235.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-8127.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21235 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7099-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7124-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21235 
│                       │      │                  ╰ [28]: https://www.oracle.com/security-alerts/cpuoct2024.html 
│                       │      ├ PublishedDate   : 2024-10-15T20:15:12.643Z 
│                       │      ╰ LastModifiedDate: 2024-10-18T18:30:26.097Z 
│                       ├ [25] ╭ VulnerabilityID : CVE-2024-21011 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21011 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: long Exception message leading to crash (8319851) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u401, 8u401-perf, 11.0.22, 17.0.10,
│                       │      │                   21.0.2, 22; Oracle GraalVM for JDK: 17.0.10, 21.0.2, 22;  
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.13 and  21.3.9.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
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
│                       │      │                   3.1 Base Score 3.7 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 1 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:1828 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21011 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2274975 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2274977 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2275003 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2274975 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2274977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2275003 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21011 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21012 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21068 
│                       │      │                  ├ [11]: https://errata.almalinux.org/9/ALSA-2024-1828.html 
│                       │      │                  ├ [12]: https://errata.rockylinux.org/RLSA-2024:1828 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2024-21011.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2024-1828.html 
│                       │      │                  ├ [15]: https://lists.debian.org/debian-lts-announce/2024/04/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2024-21011 
│                       │      │                  ├ [17]: https://security.netapp.com/advisory/ntap-20240426-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-6810-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-6811-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6812-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-6813-1 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2024-21011 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2024.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2024.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-04-16T22:15:15.437Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T21:15:17.52Z 
│                       ├ [26] ╭ VulnerabilityID : CVE-2024-21068 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21068 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: integer overflow in C1 compiler address generation
│                       │      │                   (8322122) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u401-perf, 11.0.22, 17.0.10, 21.0.2,
│                       │      │                   22; Oracle GraalVM for JDK: 17.0.10, 21.0.2 and  22; Oracle
│                       │      │                   GraalVM Enterprise Edition: 21.3.9. Difficult to exploit
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via multiple protocols to compromise Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized update, insert or delete access to some of
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   3.7 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 1 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:1828 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21068 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2274975 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2274977 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2275003 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2274975 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2274977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2275003 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21011 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21012 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21068 
│                       │      │                  ├ [11]: https://errata.almalinux.org/9/ALSA-2024-1828.html 
│                       │      │                  ├ [12]: https://errata.rockylinux.org/RLSA-2024:1828 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2024-21068.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2024-1828.html 
│                       │      │                  ├ [15]: https://lists.debian.org/debian-lts-announce/2024/04/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2024-21068 
│                       │      │                  ├ [17]: https://security.netapp.com/advisory/ntap-20240426-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-6810-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-6811-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6812-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-6813-1 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2024-21068 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2024.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2024.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-04-16T22:15:25.307Z 
│                       │      ╰ LastModifiedDate: 2024-12-06T19:22:57.927Z 
│                       ├ [27] ╭ VulnerabilityID : CVE-2024-21085 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21085 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Pack200 excessive memory allocation (8322114) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM
│                       │      │                   Enterprise Edition product of Oracle Java SE (component:
│                       │      │                   Concurrency).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u401, 8u401-perf, 11.0.22; Oracle GraalVM
│                       │      │                   Enterprise Edition: 20.3.13 and  21.3.9. Difficult to
│                       │      │                   exploit vulnerability allows unauthenticated attacker with
│                       │      │                   network access via multiple protocols to compromise Oracle
│                       │      │                   Java SE, Oracle GraalVM Enterprise Edition.  Successful
│                       │      │                   attacks of this vulnerability can result in unauthorized
│                       │      │                   ability to cause a partial denial of service (partial DOS)
│                       │      │                   of Oracle Java SE, Oracle GraalVM Enterprise Edition. Note:
│                       │      │                   This vulnerability can be exploited by using APIs in the
│                       │      │                   specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 3.7 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 1 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:1822 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21085 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2274975 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2274977 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2275001 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2275003 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2275005 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2274975 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2274977 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2275001 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2275003 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2275005 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21011 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21012 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21068 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21085 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21094 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-1822.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:1822 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21085.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-1822.html 
│                       │      │                  ├ [21]: https://lists.debian.org/debian-lts-announce/2024/04/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2024-21085 
│                       │      │                  ├ [23]: https://security.netapp.com/advisory/ntap-20240426-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6810-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6811-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21085 
│                       │      │                  ├ [28]: https://www.oracle.com/security-alerts/cpuapr2024.html 
│                       │      │                  ╰ [29]: https://www.oracle.com/security-alerts/cpuapr2024.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-04-16T22:15:28.293Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T08:53:45.35Z 
│                       ├ [28] ╭ VulnerabilityID : CVE-2024-21094 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21094 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: C2 compilation fails with "Exceeded _node_regs
│                       │      │                   array" (8317507) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u401, 8u401-perf, 11.0.22, 17.0.10,
│                       │      │                   21.0.2, 22; Oracle GraalVM for JDK: 17.0.10, 21.0.2, 22;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.13 and  21.3.9.
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
│                       │      ├ CweIDs           ─ [0]: CWE-349 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 1 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:1825 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21094 
│                       │      │                  ├ [2] : https://bugs.openjdk.org/browse/JDK-8317507 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2274975 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2274977 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2275003 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2275005 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2274975 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2274977 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2275001 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2275003 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2275005 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21011 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21012 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21068 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21085 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21094 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-1825.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:1822 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21094.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-1825.html 
│                       │      │                  ├ [21]: https://lists.debian.org/debian-lts-announce/2024/04/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2024-21094 
│                       │      │                  ├ [23]: https://security.netapp.com/advisory/ntap-20240426-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6810-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6811-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6812-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-6813-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [29]: https://www.cve.org/CVERecord?id=CVE-2024-21094 
│                       │      │                  ├ [30]: https://www.oracle.com/security-alerts/cpuapr2024.html 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpuapr2024.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-04-16T22:15:29.857Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T08:53:46.35Z 
│                       ├ [29] ╭ VulnerabilityID : CVE-2024-21131 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21131 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: potential UTF8 size overflow (8314794) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11,
│                       │      │                   21.0.3, 22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3,
│                       │      │                   22.0.1; Oracle GraalVM Enterprise Edition: 20.3.14 and 
│                       │      │                   21.3.10. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized update,
│                       │      │                   insert or delete access to some of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability can be exploited
│                       │      │                   by using APIs in the specified Component, e.g., through a
│                       │      │                   web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 3.7
│                       │      │                   (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21131 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21131.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21131 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21131 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:13.21Z 
│                       │      ╰ LastModifiedDate: 2024-12-05T22:02:52.553Z 
│                       ├ [30] ╭ VulnerabilityID : CVE-2024-21138 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21138 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Excessive symbol length can lead to infinite loop
│                       │      │                   (8319859) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11,
│                       │      │                   21.0.3, 22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3,
│                       │      │                   22.0.1; Oracle GraalVM Enterprise Edition: 20.3.14 and 
│                       │      │                   21.3.10. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in unauthorized ability to
│                       │      │                   cause a partial denial of service (partial DOS) of Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability can be exploited by using
│                       │      │                   APIs in the specified Component, e.g., through a web service
│                       │      │                    which supplies data to the APIs. This vulnerability also
│                       │      │                   applies to Java deployments, typically in clients running
│                       │      │                   sandboxed Java Web Start applications or sandboxed Java
│                       │      │                   applets, that load and run untrusted code (e.g., code that
│                       │      │                   comes from the internet) and rely on the Java sandbox for
│                       │      │                   security. CVSS 3.1 Base Score 3.7 (Availability impacts). 
│                       │      │                   CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21138 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21138.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21138 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21138 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:14.62Z 
│                       │      ╰ LastModifiedDate: 2024-12-05T22:05:55.937Z 
│                       ├ [31] ╭ VulnerabilityID : CVE-2024-21144 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21144 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Pack200 increase loading time due to improper
│                       │      │                   header validation (8322106) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM
│                       │      │                   Enterprise Edition product of Oracle Java SE (component:
│                       │      │                   Concurrency).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u411, 8u411-perf, 11.0.23; Oracle GraalVM
│                       │      │                   Enterprise Edition: 20.3.14 and  21.3.10. Difficult to
│                       │      │                   exploit vulnerability allows unauthenticated attacker with
│                       │      │                   network access via multiple protocols to compromise Oracle
│                       │      │                   Java SE, Oracle GraalVM Enterprise Edition.  Successful
│                       │      │                   attacks of this vulnerability can result in unauthorized
│                       │      │                   ability to cause a partial denial of service (partial DOS)
│                       │      │                   of Oracle Java SE, Oracle GraalVM Enterprise Edition. Note:
│                       │      │                   This vulnerability applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. This vulnerability does not apply
│                       │      │                    to Java deployments, typically in servers, that load and
│                       │      │                   run only trusted code (e.g., code installed by an
│                       │      │                   administrator). CVSS 3.1 Base Score 3.7 (Availability
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ nvd        : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 3.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4567 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21144 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297964 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2024-4567.html 
│                       │      │                  ├ [9] : https://linux.oracle.com/cve/CVE-2024-21144.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/errata/ELSA-2024-4567.html 
│                       │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2024-21144 
│                       │      │                  ├ [12]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       07/ 
│                       │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-21144 
│                       │      │                  ╰ [18]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:15.81Z 
│                       │      ╰ LastModifiedDate: 2024-12-16T20:13:40.827Z 
│                       ├ [32] ╭ VulnerabilityID : CVE-2024-21208 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.432.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21208 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : JDK: HTTP client improper handling of maxHeaderSize (8328286) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Networking).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u421, 8u421-perf, 11.0.24,
│                       │      │                   17.0.12, 21.0.4, 23; Oracle GraalVM for JDK: 17.0.12,
│                       │      │                   21.0.4, 23; Oracle GraalVM Enterprise Edition: 20.3.15 and 
│                       │      │                   21.3.11. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in unauthorized ability to
│                       │      │                   cause a partial denial of service (partial DOS) of Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability applies to Java
│                       │      │                   deployments, typically in clients running sandboxed Java Web
│                       │      │                    Start applications or sandboxed Java applets, that load and
│                       │      │                    run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. This
│                       │      │                   vulnerability does not apply to Java deployments, typically
│                       │      │                   in servers, that load and run only trusted code (e.g., code
│                       │      │                   installed by an administrator). CVSS 3.1 Base Score 3.7
│                       │      │                   (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-203 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 1 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:8127 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21208 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2251025 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2318524 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2318526 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2318530 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2318534 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2251025 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2318524 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2318526 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2318530 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2318534 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       23-48161 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21208 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21210 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21217 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21235 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-8127.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:8127 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21208.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-8127.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21208 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7099-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7124-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21208 
│                       │      │                  ╰ [28]: https://www.oracle.com/security-alerts/cpuoct2024.html 
│                       │      ├ PublishedDate   : 2024-10-15T20:15:09.437Z 
│                       │      ╰ LastModifiedDate: 2024-10-31T13:35:05.287Z 
│                       ├ [33] ╭ VulnerabilityID : CVE-2024-21210 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.432.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21210 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : JDK: Array indexing integer overflow (8328544) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: Hotspot). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u421, 8u421-perf, 11.0.24, 17.0.12, 21.0.4 and  23.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE accessible data.
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
│                       │      ├ CweIDs           ─ [0]: CWE-203 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 1 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:8127 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21210 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2251025 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2318524 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2318526 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2318530 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2318534 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2251025 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2318524 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2318526 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2318530 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2318534 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       23-48161 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21208 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21210 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21217 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21235 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-8127.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:8127 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21210.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-8127.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21210 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7099-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7124-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21210 
│                       │      │                  ╰ [28]: https://www.oracle.com/security-alerts/cpuoct2024.html 
│                       │      ├ PublishedDate   : 2024-10-15T20:15:09.843Z 
│                       │      ╰ LastModifiedDate: 2024-10-31T13:35:06.037Z 
│                       ├ [34] ╭ VulnerabilityID : CVE-2024-21217 
│                       │      ├ PkgID           : openjdk8-jre-base@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-base@8.402.06-r0?arch=x86
│                       │      │                  │       _64&distro=3.20.3 
│                       │      │                  ╰ UID : 55ca2adef4744de6 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.432.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21217 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : JDK: Unbounded allocation leads to out-of-memory error
│                       │      │                   (8331446) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Serialization).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u421, 8u421-perf, 11.0.24,
│                       │      │                   17.0.12, 21.0.4, 23; Oracle GraalVM for JDK: 17.0.12,
│                       │      │                   21.0.4, 23; Oracle GraalVM Enterprise Edition: 20.3.15 and 
│                       │      │                   21.3.11. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in unauthorized ability to
│                       │      │                   cause a partial denial of service (partial DOS) of Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability can be exploited by using
│                       │      │                   APIs in the specified Component, e.g., through a web service
│                       │      │                    which supplies data to the APIs. This vulnerability also
│                       │      │                   applies to Java deployments, typically in clients running
│                       │      │                   sandboxed Java Web Start applications or sandboxed Java
│                       │      │                   applets, that load and run untrusted code (e.g., code that
│                       │      │                   comes from the internet) and rely on the Java sandbox for
│                       │      │                   security. CVSS 3.1 Base Score 3.7 (Availability impacts). 
│                       │      │                   CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 1 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:8127 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21217 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2251025 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2318524 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2318526 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2318530 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2318534 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2251025 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2318524 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2318526 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2318530 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2318534 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       23-48161 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21208 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21210 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21217 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21235 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-8127.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:8127 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21217.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-8127.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21217 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7099-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7124-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21217 
│                       │      │                  ╰ [28]: https://www.oracle.com/security-alerts/cpuoct2024.html 
│                       │      ├ PublishedDate   : 2024-10-15T20:15:11.197Z 
│                       │      ╰ LastModifiedDate: 2024-10-18T18:29:36.59Z 
│                       ├ [35] ╭ VulnerabilityID : CVE-2024-21147 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21147 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: RangeCheckElimination array index overflow (8323231) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11,
│                       │      │                   21.0.3, 22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3,
│                       │      │                   22.0.1; Oracle GraalVM Enterprise Edition: 20.3.14 and 
│                       │      │                   21.3.10. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data as well as  unauthorized
│                       │      │                   access to critical data or complete access to all Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-200 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21147 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21147.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21147 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21147 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:16.377Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T08:53:52.63Z 
│                       ├ [36] ╭ VulnerabilityID : CVE-2024-21140 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21140 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Range Check Elimination (RCE) pre-loop limit
│                       │      │                   overflow (8320548) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11,
│                       │      │                   21.0.3, 22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3,
│                       │      │                   22.0.1; Oracle GraalVM Enterprise Edition: 20.3.14 and 
│                       │      │                   21.3.10. Difficult to exploit vulnerability allows
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
│                       │      │                   3.1 Base Score 4.8 (Confidentiality and Integrity impacts). 
│                       │      │                    CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N)
│                       │      │                   . 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-200 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21140 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21140.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21140 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21140 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:15.043Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T08:53:51.75Z 
│                       ├ [37] ╭ VulnerabilityID : CVE-2024-21145 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21145 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Out-of-bounds access in 2D image handling (8324559) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11, 21.0.3,
│                       │      │                    22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3, 22.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.14 and  21.3.10.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data as
│                       │      │                   well as  unauthorized read access to a subset of Oracle Java
│                       │      │                    SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 4.8
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.8 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21145 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21145.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21145 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21145 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:15.993Z 
│                       │      ╰ LastModifiedDate: 2024-12-16T20:13:37.007Z 
│                       ├ [38] ╭ VulnerabilityID : CVE-2024-21235 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.432.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21235 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : JDK: Integer conversion error leads to incorrect range check
│                       │      │                    (8332644) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u421, 8u421-perf, 11.0.24, 17.0.12,
│                       │      │                   21.0.4, 23;   Oracle GraalVM for JDK: 17.0.12, 21.0.4, 23;  
│                       │      │                    Oracle GraalVM Enterprise Edition: 20.3.15 and  21.3.11.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data as
│                       │      │                   well as  unauthorized read access to a subset of Oracle Java
│                       │      │                    SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 4.8
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:8127 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21235 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2251025 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2318524 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2318526 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2318530 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2318534 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2251025 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2318524 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2318526 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2318530 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2318534 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       23-48161 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21208 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21210 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21217 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21235 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-8127.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:8127 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21235.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-8127.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21235 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7099-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7124-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21235 
│                       │      │                  ╰ [28]: https://www.oracle.com/security-alerts/cpuoct2024.html 
│                       │      ├ PublishedDate   : 2024-10-15T20:15:12.643Z 
│                       │      ╰ LastModifiedDate: 2024-10-18T18:30:26.097Z 
│                       ├ [39] ╭ VulnerabilityID : CVE-2024-21011 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21011 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: long Exception message leading to crash (8319851) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u401, 8u401-perf, 11.0.22, 17.0.10,
│                       │      │                   21.0.2, 22; Oracle GraalVM for JDK: 17.0.10, 21.0.2, 22;  
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.13 and  21.3.9.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
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
│                       │      │                   3.1 Base Score 3.7 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 1 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:1828 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21011 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2274975 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2274977 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2275003 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2274975 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2274977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2275003 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21011 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21012 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21068 
│                       │      │                  ├ [11]: https://errata.almalinux.org/9/ALSA-2024-1828.html 
│                       │      │                  ├ [12]: https://errata.rockylinux.org/RLSA-2024:1828 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2024-21011.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2024-1828.html 
│                       │      │                  ├ [15]: https://lists.debian.org/debian-lts-announce/2024/04/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2024-21011 
│                       │      │                  ├ [17]: https://security.netapp.com/advisory/ntap-20240426-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-6810-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-6811-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6812-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-6813-1 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2024-21011 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2024.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2024.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-04-16T22:15:15.437Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T21:15:17.52Z 
│                       ├ [40] ╭ VulnerabilityID : CVE-2024-21068 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21068 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: integer overflow in C1 compiler address generation
│                       │      │                   (8322122) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u401-perf, 11.0.22, 17.0.10, 21.0.2,
│                       │      │                   22; Oracle GraalVM for JDK: 17.0.10, 21.0.2 and  22; Oracle
│                       │      │                   GraalVM Enterprise Edition: 21.3.9. Difficult to exploit
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via multiple protocols to compromise Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized update, insert or delete access to some of
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   3.7 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 1 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:1828 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21068 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2274975 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2274977 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2275003 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2274975 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2274977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2275003 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21011 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21012 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21068 
│                       │      │                  ├ [11]: https://errata.almalinux.org/9/ALSA-2024-1828.html 
│                       │      │                  ├ [12]: https://errata.rockylinux.org/RLSA-2024:1828 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2024-21068.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2024-1828.html 
│                       │      │                  ├ [15]: https://lists.debian.org/debian-lts-announce/2024/04/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2024-21068 
│                       │      │                  ├ [17]: https://security.netapp.com/advisory/ntap-20240426-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-6810-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-6811-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6812-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-6813-1 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2024-21068 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2024.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2024.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-04-16T22:15:25.307Z 
│                       │      ╰ LastModifiedDate: 2024-12-06T19:22:57.927Z 
│                       ├ [41] ╭ VulnerabilityID : CVE-2024-21085 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21085 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Pack200 excessive memory allocation (8322114) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM
│                       │      │                   Enterprise Edition product of Oracle Java SE (component:
│                       │      │                   Concurrency).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u401, 8u401-perf, 11.0.22; Oracle GraalVM
│                       │      │                   Enterprise Edition: 20.3.13 and  21.3.9. Difficult to
│                       │      │                   exploit vulnerability allows unauthenticated attacker with
│                       │      │                   network access via multiple protocols to compromise Oracle
│                       │      │                   Java SE, Oracle GraalVM Enterprise Edition.  Successful
│                       │      │                   attacks of this vulnerability can result in unauthorized
│                       │      │                   ability to cause a partial denial of service (partial DOS)
│                       │      │                   of Oracle Java SE, Oracle GraalVM Enterprise Edition. Note:
│                       │      │                   This vulnerability can be exploited by using APIs in the
│                       │      │                   specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 3.7 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 1 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:1822 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21085 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2274975 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2274977 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2275001 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2275003 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2275005 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2274975 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2274977 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2275001 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2275003 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2275005 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21011 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21012 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21068 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21085 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21094 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-1822.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:1822 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21085.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-1822.html 
│                       │      │                  ├ [21]: https://lists.debian.org/debian-lts-announce/2024/04/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2024-21085 
│                       │      │                  ├ [23]: https://security.netapp.com/advisory/ntap-20240426-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6810-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6811-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21085 
│                       │      │                  ├ [28]: https://www.oracle.com/security-alerts/cpuapr2024.html 
│                       │      │                  ╰ [29]: https://www.oracle.com/security-alerts/cpuapr2024.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-04-16T22:15:28.293Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T08:53:45.35Z 
│                       ├ [42] ╭ VulnerabilityID : CVE-2024-21094 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21094 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: C2 compilation fails with "Exceeded _node_regs
│                       │      │                   array" (8317507) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u401, 8u401-perf, 11.0.22, 17.0.10,
│                       │      │                   21.0.2, 22; Oracle GraalVM for JDK: 17.0.10, 21.0.2, 22;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.13 and  21.3.9.
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
│                       │      ├ CweIDs           ─ [0]: CWE-349 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 1 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:1825 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21094 
│                       │      │                  ├ [2] : https://bugs.openjdk.org/browse/JDK-8317507 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2274975 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2274977 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2275003 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2275005 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2274975 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2274977 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2275001 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2275003 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2275005 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21011 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21012 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21068 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21085 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21094 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-1825.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:1822 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21094.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-1825.html 
│                       │      │                  ├ [21]: https://lists.debian.org/debian-lts-announce/2024/04/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2024-21094 
│                       │      │                  ├ [23]: https://security.netapp.com/advisory/ntap-20240426-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6810-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6811-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6812-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-6813-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [29]: https://www.cve.org/CVERecord?id=CVE-2024-21094 
│                       │      │                  ├ [30]: https://www.oracle.com/security-alerts/cpuapr2024.html 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpuapr2024.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-04-16T22:15:29.857Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T08:53:46.35Z 
│                       ├ [43] ╭ VulnerabilityID : CVE-2024-21131 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21131 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: potential UTF8 size overflow (8314794) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11,
│                       │      │                   21.0.3, 22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3,
│                       │      │                   22.0.1; Oracle GraalVM Enterprise Edition: 20.3.14 and 
│                       │      │                   21.3.10. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized update,
│                       │      │                   insert or delete access to some of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability can be exploited
│                       │      │                   by using APIs in the specified Component, e.g., through a
│                       │      │                   web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 3.7
│                       │      │                   (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21131 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21131.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21131 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21131 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:13.21Z 
│                       │      ╰ LastModifiedDate: 2024-12-05T22:02:52.553Z 
│                       ├ [44] ╭ VulnerabilityID : CVE-2024-21138 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21138 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Excessive symbol length can lead to infinite loop
│                       │      │                   (8319859) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u411, 8u411-perf, 11.0.23, 17.0.11,
│                       │      │                   21.0.3, 22.0.1; Oracle GraalVM for JDK: 17.0.11, 21.0.3,
│                       │      │                   22.0.1; Oracle GraalVM Enterprise Edition: 20.3.14 and 
│                       │      │                   21.3.10. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in unauthorized ability to
│                       │      │                   cause a partial denial of service (partial DOS) of Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability can be exploited by using
│                       │      │                   APIs in the specified Component, e.g., through a web service
│                       │      │                    which supplies data to the APIs. This vulnerability also
│                       │      │                   applies to Java deployments, typically in clients running
│                       │      │                   sandboxed Java Web Start applications or sandboxed Java
│                       │      │                   applets, that load and run untrusted code (e.g., code that
│                       │      │                   comes from the internet) and rely on the Java sandbox for
│                       │      │                   security. CVSS 3.1 Base Score 3.7 (Availability impacts). 
│                       │      │                   CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4573 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21138 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2297961 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2297962 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2297963 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2297976 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2297977 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21131 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21140 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21145 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21147 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-4573.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:4573 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21138.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-4573.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21138 
│                       │      │                  ├ [22]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6931-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-6932-1 
│                       │      │                  ├ [27]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [29]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [30]: https://www.cve.org/CVERecord?id=CVE-2024-21138 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:14.62Z 
│                       │      ╰ LastModifiedDate: 2024-12-05T22:05:55.937Z 
│                       ├ [45] ╭ VulnerabilityID : CVE-2024-21144 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.422.05-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21144 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: Pack200 increase loading time due to improper
│                       │      │                   header validation (8322106) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM
│                       │      │                   Enterprise Edition product of Oracle Java SE (component:
│                       │      │                   Concurrency).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u411, 8u411-perf, 11.0.23; Oracle GraalVM
│                       │      │                   Enterprise Edition: 20.3.14 and  21.3.10. Difficult to
│                       │      │                   exploit vulnerability allows unauthenticated attacker with
│                       │      │                   network access via multiple protocols to compromise Oracle
│                       │      │                   Java SE, Oracle GraalVM Enterprise Edition.  Successful
│                       │      │                   attacks of this vulnerability can result in unauthorized
│                       │      │                   ability to cause a partial denial of service (partial DOS)
│                       │      │                   of Oracle Java SE, Oracle GraalVM Enterprise Edition. Note:
│                       │      │                   This vulnerability applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. This vulnerability does not apply
│                       │      │                    to Java deployments, typically in servers, that load and
│                       │      │                   run only trusted code (e.g., code installed by an
│                       │      │                   administrator). CVSS 3.1 Base Score 3.7 (Availability
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ nvd        : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 3.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:4567 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21144 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2297961 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2297962 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2297963 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2297964 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2297976 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2297977 
│                       │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2024-4567.html 
│                       │      │                  ├ [9] : https://linux.oracle.com/cve/CVE-2024-21144.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/errata/ELSA-2024-4567.html 
│                       │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2024-21144 
│                       │      │                  ├ [12]: https://security.netapp.com/advisory/ntap-20240719-00
│                       │      │                  │       07/ 
│                       │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-6929-1 
│                       │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6930-1 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-21144 
│                       │      │                  ╰ [18]: https://www.oracle.com/security-alerts/cpujul2024.html 
│                       │      ├ PublishedDate   : 2024-07-16T23:15:15.81Z 
│                       │      ╰ LastModifiedDate: 2024-12-16T20:13:40.827Z 
│                       ├ [46] ╭ VulnerabilityID : CVE-2024-21208 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.432.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21208 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : JDK: HTTP client improper handling of maxHeaderSize (8328286) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Networking).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u421, 8u421-perf, 11.0.24,
│                       │      │                   17.0.12, 21.0.4, 23; Oracle GraalVM for JDK: 17.0.12,
│                       │      │                   21.0.4, 23; Oracle GraalVM Enterprise Edition: 20.3.15 and 
│                       │      │                   21.3.11. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in unauthorized ability to
│                       │      │                   cause a partial denial of service (partial DOS) of Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability applies to Java
│                       │      │                   deployments, typically in clients running sandboxed Java Web
│                       │      │                    Start applications or sandboxed Java applets, that load and
│                       │      │                    run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. This
│                       │      │                   vulnerability does not apply to Java deployments, typically
│                       │      │                   in servers, that load and run only trusted code (e.g., code
│                       │      │                   installed by an administrator). CVSS 3.1 Base Score 3.7
│                       │      │                   (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-203 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 1 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:8127 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21208 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2251025 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2318524 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2318526 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2318530 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2318534 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2251025 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2318524 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2318526 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2318530 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2318534 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       23-48161 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21208 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21210 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21217 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21235 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-8127.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:8127 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21208.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-8127.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21208 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7099-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7124-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21208 
│                       │      │                  ╰ [28]: https://www.oracle.com/security-alerts/cpuoct2024.html 
│                       │      ├ PublishedDate   : 2024-10-15T20:15:09.437Z 
│                       │      ╰ LastModifiedDate: 2024-10-31T13:35:05.287Z 
│                       ├ [47] ╭ VulnerabilityID : CVE-2024-21210 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.432.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21210 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : JDK: Array indexing integer overflow (8328544) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: Hotspot). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u421, 8u421-perf, 11.0.24, 17.0.12, 21.0.4 and  23.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE accessible data.
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
│                       │      ├ CweIDs           ─ [0]: CWE-203 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 1 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:8127 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21210 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2251025 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2318524 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2318526 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2318530 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2318534 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2251025 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2318524 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2318526 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2318530 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2318534 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       23-48161 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21208 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21210 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21217 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21235 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-8127.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:8127 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21210.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-8127.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21210 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7099-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7124-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21210 
│                       │      │                  ╰ [28]: https://www.oracle.com/security-alerts/cpuoct2024.html 
│                       │      ├ PublishedDate   : 2024-10-15T20:15:09.843Z 
│                       │      ╰ LastModifiedDate: 2024-10-31T13:35:06.037Z 
│                       ├ [48] ╭ VulnerabilityID : CVE-2024-21217 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.402.06-r0 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.402.06-r0?arch=x86_
│                       │      │                  │       64&distro=3.20.3 
│                       │      │                  ╰ UID : eb2679006e2e15eb 
│                       │      ├ InstalledVersion: 8.402.06-r0 
│                       │      ├ FixedVersion    : 8.432.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                       │      │                  │         2801b3e28133325c482b 
│                       │      │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                       │      │                            28ea1250ef005595c5f9 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-21217 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : JDK: Unbounded allocation leads to out-of-memory error
│                       │      │                   (8331446) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Serialization).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u421, 8u421-perf, 11.0.24,
│                       │      │                   17.0.12, 21.0.4, 23; Oracle GraalVM for JDK: 17.0.12,
│                       │      │                   21.0.4, 23; Oracle GraalVM Enterprise Edition: 20.3.15 and 
│                       │      │                   21.3.11. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in unauthorized ability to
│                       │      │                   cause a partial denial of service (partial DOS) of Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability can be exploited by using
│                       │      │                   APIs in the specified Component, e.g., through a web service
│                       │      │                    which supplies data to the APIs. This vulnerability also
│                       │      │                   applies to Java deployments, typically in clients running
│                       │      │                   sandboxed Java Web Start applications or sandboxed Java
│                       │      │                   applets, that load and run untrusted code (e.g., code that
│                       │      │                   comes from the internet) and rely on the Java sandbox for
│                       │      │                   security. CVSS 3.1 Base Score 3.7 (Availability impacts). 
│                       │      │                   CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 1 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:8127 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-21217 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2251025 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2318524 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2318526 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2318530 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2318534 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2251025 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2318524 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2318526 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2318530 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2318534 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       23-48161 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21208 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21210 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21217 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-21235 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2024-8127.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2024:8127 
│                       │      │                  ├ [19]: https://linux.oracle.com/cve/CVE-2024-21217.html 
│                       │      │                  ├ [20]: https://linux.oracle.com/errata/ELSA-2024-8127.html 
│                       │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2024-21217 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7096-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7097-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7098-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7099-1 
│                       │      │                  ├ [26]: https://ubuntu.com/security/notices/USN-7124-1 
│                       │      │                  ├ [27]: https://www.cve.org/CVERecord?id=CVE-2024-21217 
│                       │      │                  ╰ [28]: https://www.oracle.com/security-alerts/cpuoct2024.html 
│                       │      ├ PublishedDate   : 2024-10-15T20:15:11.197Z 
│                       │      ╰ LastModifiedDate: 2024-10-18T18:29:36.59Z 
│                       ╰ [49] ╭ VulnerabilityID : CVE-2024-9143 
│                              ├ PkgID           : openssl@3.3.2-r0 
│                              ├ PkgName         : openssl 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.3.2-r0?arch=x86_64&distro=3.
│                              │                  │       20.3 
│                              │                  ╰ UID : aad39ba6d762dc14 
│                              ├ InstalledVersion: 3.3.2-r0 
│                              ├ FixedVersion    : 3.3.2-r1 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee
│                              │                  │         2801b3e28133325c482b 
│                              │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed
│                              │                            28ea1250ef005595c5f9 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-9143 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Title           : openssl: Low-level invalid GF(2^m) parameters lead to OOB
│                              │                   memory access 
│                              ├ Description     : Issue summary: Use of the low-level GF(2^m) elliptic curve
│                              │                   APIs with untrusted
│                              │                   explicit values for the field polynomial can lead to
│                              │                   out-of-bounds memory reads
│                              │                   or writes.
│                              │                   
│                              │                   Impact summary: Out of bound memory writes can lead to an
│                              │                   application crash or
│                              │                   even a possibility of a remote code execution, however, in
│                              │                   all the protocols
│                              │                   involving Elliptic Curve Cryptography that we're aware of,
│                              │                   either only "named
│                              │                   curves" are supported, or, if explicit curve parameters are
│                              │                   supported, they
│                              │                   specify an X9.62 encoding of binary (GF(2^m)) curves that
│                              │                   can't represent
│                              │                   problematic input values. Thus the likelihood of existence
│                              │                   of a vulnerable
│                              │                   application is low.
│                              │                   In particular, the X9.62 encoding is used for ECC keys in
│                              │                   X.509 certificates,
│                              │                   so problematic inputs cannot occur in the context of
│                              │                   processing X.509
│                              │                   certificates.  Any problematic use-cases would have to be
│                              │                   using an "exotic"
│                              │                   curve encoding.
│                              │                   The affected APIs include: EC_GROUP_new_curve_GF2m(),
│                              │                   EC_GROUP_new_from_params(),
│                              │                   and various supporting BN_GF2m_*() functions.
│                              │                   Applications working with "exotic" explicit binary (GF(2^m))
│                              │                    curve parameters,
│                              │                   that make it possible to represent invalid field polynomials
│                              │                    with a zero
│                              │                   constant term, via the above or similar APIs, may terminate
│                              │                   abruptly as a
│                              │                   result of reading or writing outside of array bounds. 
│                              │                   Remote code execution
│                              │                   cannot easily be ruled out.
│                              │                   The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected
│                              │                   by this issue. 
│                              ├ Severity        : LOW 
│                              ├ CweIDs           ─ [0]: CWE-787 
│                              ├ VendorSeverity   ╭ amazon: 3 
│                              │                  ├ redhat: 1 
│                              │                  ╰ ubuntu: 1 
│                              ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                              │                           │           /A:L 
│                              │                           ╰ V3Score : 3.7 
│                              ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2024/10/16/1 
│                              │                  ├ [1] : http://www.openwall.com/lists/oss-security/2024/10/23/1 
│                              │                  ├ [2] : http://www.openwall.com/lists/oss-security/2024/10/24/1 
│                              │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2024-9143 
│                              │                  ├ [4] : https://github.com/openssl/openssl/commit/72ae83ad214
│                              │                  │       d2eef262461365a1975707f862712 
│                              │                  ├ [5] : https://github.com/openssl/openssl/commit/bc7e04d7c8d
│                              │                  │       509fb78fc0e285aa948fb0da04700 
│                              │                  ├ [6] : https://github.com/openssl/openssl/commit/c0d3e4d32d2
│                              │                  │       805f49bec30547f225bc4d092e1f4 
│                              │                  ├ [7] : https://github.com/openssl/openssl/commit/fdf6723362c
│                              │                  │       a51bd883295efe206cb5b1cfa5154 
│                              │                  ├ [8] : https://github.openssl.org/openssl/extended-releases/
│                              │                  │       commit/8efc0cbaa8ebba8e116f7b81a876a4123594d86a 
│                              │                  ├ [9] : https://github.openssl.org/openssl/extended-releases/
│                              │                  │       commit/9d576994cec2b7aa37a91740ea7e680810957e41 
│                              │                  ├ [10]: https://nvd.nist.gov/vuln/detail/CVE-2024-9143 
│                              │                  ├ [11]: https://openssl-library.org/news/secadv/20241016.txt 
│                              │                  ├ [12]: https://security.netapp.com/advisory/ntap-20241101-00
│                              │                  │       01/ 
│                              │                  ╰ [13]: https://www.cve.org/CVERecord?id=CVE-2024-9143 
│                              ├ PublishedDate   : 2024-10-16T17:15:18.13Z 
│                              ╰ LastModifiedDate: 2024-11-21T09:54:04.817Z 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2024-6763 
                              ├ PkgName         : org.eclipse.jetty:jetty-http 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ PkgIdentifier    ╭ PURL: pkg:maven/org.eclipse.jetty/jetty-http@9.4.55.v20240627 
                              │                  ╰ UID : f7c6df4b894e0ce 
                              ├ InstalledVersion: 9.4.55.v20240627 
                              ├ FixedVersion    : 12.0.12 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee2
                              │                  │         801b3e28133325c482b 
                              │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed2
                              │                            8ea1250ef005595c5f9 
                              ├ SeveritySource  : ghsa 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-6763 
                              ├ DataSource       ╭ ID  : ghsa 
                              │                  ├ Name: GitHub Security Advisory Maven 
                              │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                              │                          osystem%3Amaven 
                              ├ Title           : org.eclipse.jetty:jetty-http: jetty: Jetty URI parsing of
                              │                   invalid authority 
                              ├ Description     : Eclipse Jetty is a lightweight, highly scalable, Java-based
                              │                   web server and Servlet engine . It includes a utility class,
                              │                   HttpURI, for URI/URL parsing.
                              │                   
                              │                   The HttpURI class does insufficient validation on the
                              │                   authority segment of a URI.  However the behaviour of
                              │                   HttpURI
                              │                    differs from the common browsers in how it handles a URI
                              │                   that would be 
                              │                   considered invalid if fully validated against the RRC. 
                              │                   Specifically HttpURI
                              │                    and the browser may differ on the value of the host
                              │                   extracted from an 
                              │                   invalid URI and thus a combination of Jetty and a vulnerable
                              │                   browser may
                              │                    be vulnerable to a open redirect attack or to a SSRF attack
                              │                   if the URI 
                              │                   is used after passing validation checks. 
                              ├ Severity        : MEDIUM 
                              ├ CweIDs           ─ [0]: CWE-1286 
                              ├ VendorSeverity   ╭ ghsa  : 2 
                              │                  ├ nvd   : 2 
                              │                  ╰ redhat: 1 
                              ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/
                              │                  │        │           A:N 
                              │                  │        ╰ V3Score : 3.7 
                              │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/
                              │                  │        │           A:N 
                              │                  │        ╰ V3Score : 5.3 
                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/
                              │                           │           A:N 
                              │                           ╰ V3Score : 3.7 
                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-6763 
                              │                  ├ [1]: https://github.com/jetty/jetty.project 
                              │                  ├ [2]: https://github.com/jetty/jetty.project/pull/12012 
                              │                  ├ [3]: https://github.com/jetty/jetty.project/security/advisor
                              │                  │      ies/GHSA-qh8g-58pp-2wxh 
                              │                  ├ [4]: https://gitlab.eclipse.org/security/cve-assignement/-/i
                              │                  │      ssues/25 
                              │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2024-6763 
                              │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2024-6763 
                              ├ PublishedDate   : 2024-10-14T16:15:04.163Z 
                              ╰ LastModifiedDate: 2024-11-08T21:15:57.677Z 
````
