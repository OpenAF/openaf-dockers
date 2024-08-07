````yaml
╭ [0] ╭ Target         : openaf/ojobrt:8-latest (alpine 3.20.1) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2024-6197 
│                       │     ├ PkgID           : curl@8.8.0-r0 
│                       │     ├ PkgName         : curl 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.8.0-r0?arch=x86_64&distro=3.20.1 
│                       │     │                  ╰ UID : 138f39ff73c06f19 
│                       │     ├ InstalledVersion: 8.8.0-r0 
│                       │     ├ FixedVersion    : 8.9.0-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:55783352ae40a41a855f2505478a8fb805bc1a11
│                       │     │                  │         60b1c5c9b91350e5a64a9262 
│                       │     │                  ╰ DiffID: sha256:7d44a7543042a0404622dbc9ae983829d063abc8
│                       │     │                            2d3bf284ad2440273a0c71ed 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-6197 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : curl: freeing stack buffer in utf8asn1str 
│                       │     ├ Description     : libcurl's ASN1 parser has this utf8asn1str() function
│                       │     │                   used for parsing an ASN.1 UTF-8 string. Itcan detect an
│                       │     │                   invalid field and return error. Unfortunately, when doing so
│                       │     │                   it also invokes `free()` on a 4 byte localstack buffer.  Most
│                       │     │                    modern malloc implementations detect this error and
│                       │     │                   immediately abort. Some however accept the input pointer and
│                       │     │                   add that memory to its list of available chunks. This leads
│                       │     │                   to the overwriting of nearby stack memory. The content of the
│                       │     │                    overwrite is decided by the `free()` implementation; likely
│                       │     │                   to be memory pointers and a set of flags.  The most likely
│                       │     │                   outcome of exploting this flaw is a crash, although it cannot
│                       │     │                    be ruled out that more serious results can be had in special
│                       │     │                    circumstances. 
│                       │     ├ Severity        : MEDIUM 
│                       │     ├ VendorSeverity   ╭ photon: 2 
│                       │     │                  ╰ redhat: 2 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N
│                       │     │                           │           /I:L/A:H 
│                       │     │                           ╰ V3Score : 6.5 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/07/24/1 
│                       │     │                  ├ [1]: http://www.openwall.com/lists/oss-security/2024/07/24/5 
│                       │     │                  ├ [2]: https://access.redhat.com/security/cve/CVE-2024-6197 
│                       │     │                  ├ [3]: https://curl.se/docs/CVE-2024-6197.html 
│                       │     │                  ├ [4]: https://curl.se/docs/CVE-2024-6197.json 
│                       │     │                  ├ [5]: https://hackerone.com/reports/2559516 
│                       │     │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2024-6197 
│                       │     │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2024-6197 
│                       │     ├ PublishedDate   : 2024-07-24T08:15:03.34Z 
│                       │     ╰ LastModifiedDate: 2024-08-01T14:00:14.76Z 
│                       ├ [1] ╭ VulnerabilityID : CVE-2024-6874 
│                       │     ├ PkgID           : curl@8.8.0-r0 
│                       │     ├ PkgName         : curl 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.8.0-r0?arch=x86_64&distro=3.20.1 
│                       │     │                  ╰ UID : 138f39ff73c06f19 
│                       │     ├ InstalledVersion: 8.8.0-r0 
│                       │     ├ FixedVersion    : 8.9.0-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:55783352ae40a41a855f2505478a8fb805bc1a11
│                       │     │                  │         60b1c5c9b91350e5a64a9262 
│                       │     │                  ╰ DiffID: sha256:7d44a7543042a0404622dbc9ae983829d063abc8
│                       │     │                            2d3bf284ad2440273a0c71ed 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-6874 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : curl: macidn punycode buffer overread 
│                       │     ├ Description     : libcurl's URL API function
│                       │     │                   [curl_url_get()](https://curl.se/libcurl/c/curl_url_get.html)
│                       │     │                    offers punycode
│                       │     │                   conversions, to and from IDN. Asking to convert a name that
│                       │     │                   is exactly 256
│                       │     │                   bytes, libcurl ends up reading outside of a stack based
│                       │     │                   buffer when built to
│                       │     │                   use the *macidn* IDN backend. The conversion function then
│                       │     │                   fills up the
│                       │     │                   provided buffer exactly - but does not null terminate the
│                       │     │                   string.
│                       │     │                   
│                       │     │                   This flaw can lead to stack contents accidently getting
│                       │     │                   returned as part of
│                       │     │                   the converted string. 
│                       │     ├ Severity        : MEDIUM 
│                       │     ├ VendorSeverity   ─ redhat: 1 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L
│                       │     │                           │           /I:N/A:N 
│                       │     │                           ╰ V3Score : 5.3 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/07/24/2 
│                       │     │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2024-6874 
│                       │     │                  ├ [2]: https://curl.se/docs/CVE-2024-6874.html 
│                       │     │                  ├ [3]: https://curl.se/docs/CVE-2024-6874.json 
│                       │     │                  ├ [4]: https://hackerone.com/reports/2604391 
│                       │     │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2024-6874 
│                       │     │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2024-6874 
│                       │     ├ PublishedDate   : 2024-07-24T08:15:03.413Z 
│                       │     ╰ LastModifiedDate: 2024-08-01T14:00:45.683Z 
│                       ├ [2] ╭ VulnerabilityID : CVE-2024-6197 
│                       │     ├ PkgID           : libcurl@8.8.0-r0 
│                       │     ├ PkgName         : libcurl 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.8.0-r0?arch=x86_64&distr
│                       │     │                  │       o=3.20.1 
│                       │     │                  ╰ UID : 99e4d7d379138467 
│                       │     ├ InstalledVersion: 8.8.0-r0 
│                       │     ├ FixedVersion    : 8.9.0-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:55783352ae40a41a855f2505478a8fb805bc1a11
│                       │     │                  │         60b1c5c9b91350e5a64a9262 
│                       │     │                  ╰ DiffID: sha256:7d44a7543042a0404622dbc9ae983829d063abc8
│                       │     │                            2d3bf284ad2440273a0c71ed 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-6197 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : curl: freeing stack buffer in utf8asn1str 
│                       │     ├ Description     : libcurl's ASN1 parser has this utf8asn1str() function
│                       │     │                   used for parsing an ASN.1 UTF-8 string. Itcan detect an
│                       │     │                   invalid field and return error. Unfortunately, when doing so
│                       │     │                   it also invokes `free()` on a 4 byte localstack buffer.  Most
│                       │     │                    modern malloc implementations detect this error and
│                       │     │                   immediately abort. Some however accept the input pointer and
│                       │     │                   add that memory to its list of available chunks. This leads
│                       │     │                   to the overwriting of nearby stack memory. The content of the
│                       │     │                    overwrite is decided by the `free()` implementation; likely
│                       │     │                   to be memory pointers and a set of flags.  The most likely
│                       │     │                   outcome of exploting this flaw is a crash, although it cannot
│                       │     │                    be ruled out that more serious results can be had in special
│                       │     │                    circumstances. 
│                       │     ├ Severity        : MEDIUM 
│                       │     ├ VendorSeverity   ╭ photon: 2 
│                       │     │                  ╰ redhat: 2 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N
│                       │     │                           │           /I:L/A:H 
│                       │     │                           ╰ V3Score : 6.5 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/07/24/1 
│                       │     │                  ├ [1]: http://www.openwall.com/lists/oss-security/2024/07/24/5 
│                       │     │                  ├ [2]: https://access.redhat.com/security/cve/CVE-2024-6197 
│                       │     │                  ├ [3]: https://curl.se/docs/CVE-2024-6197.html 
│                       │     │                  ├ [4]: https://curl.se/docs/CVE-2024-6197.json 
│                       │     │                  ├ [5]: https://hackerone.com/reports/2559516 
│                       │     │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2024-6197 
│                       │     │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2024-6197 
│                       │     ├ PublishedDate   : 2024-07-24T08:15:03.34Z 
│                       │     ╰ LastModifiedDate: 2024-08-01T14:00:14.76Z 
│                       ╰ [3] ╭ VulnerabilityID : CVE-2024-6874 
│                             ├ PkgID           : libcurl@8.8.0-r0 
│                             ├ PkgName         : libcurl 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.8.0-r0?arch=x86_64&distr
│                             │                  │       o=3.20.1 
│                             │                  ╰ UID : 99e4d7d379138467 
│                             ├ InstalledVersion: 8.8.0-r0 
│                             ├ FixedVersion    : 8.9.0-r0 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:55783352ae40a41a855f2505478a8fb805bc1a11
│                             │                  │         60b1c5c9b91350e5a64a9262 
│                             │                  ╰ DiffID: sha256:7d44a7543042a0404622dbc9ae983829d063abc8
│                             │                            2d3bf284ad2440273a0c71ed 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-6874 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Title           : curl: macidn punycode buffer overread 
│                             ├ Description     : libcurl's URL API function
│                             │                   [curl_url_get()](https://curl.se/libcurl/c/curl_url_get.html)
│                             │                    offers punycode
│                             │                   conversions, to and from IDN. Asking to convert a name that
│                             │                   is exactly 256
│                             │                   bytes, libcurl ends up reading outside of a stack based
│                             │                   buffer when built to
│                             │                   use the *macidn* IDN backend. The conversion function then
│                             │                   fills up the
│                             │                   provided buffer exactly - but does not null terminate the
│                             │                   string.
│                             │                   
│                             │                   This flaw can lead to stack contents accidently getting
│                             │                   returned as part of
│                             │                   the converted string. 
│                             ├ Severity        : MEDIUM 
│                             ├ VendorSeverity   ─ redhat: 1 
│                             ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L
│                             │                           │           /I:N/A:N 
│                             │                           ╰ V3Score : 5.3 
│                             ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/07/24/2 
│                             │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2024-6874 
│                             │                  ├ [2]: https://curl.se/docs/CVE-2024-6874.html 
│                             │                  ├ [3]: https://curl.se/docs/CVE-2024-6874.json 
│                             │                  ├ [4]: https://hackerone.com/reports/2604391 
│                             │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2024-6874 
│                             │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2024-6874 
│                             ├ PublishedDate   : 2024-07-24T08:15:03.413Z 
│                             ╰ LastModifiedDate: 2024-08-01T14:00:45.683Z 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2024-25638 
                        │     ├ PkgName         : dnsjava:dnsjava 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/dnsjava/dnsjava@3.5.3 
                        │     │                  ╰ UID : fcd3d0c2bf50859 
                        │     ├ InstalledVersion: 3.5.3 
                        │     ├ FixedVersion    : 3.6.0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:55783352ae40a41a855f2505478a8fb805bc1a11
                        │     │                  │         60b1c5c9b91350e5a64a9262 
                        │     │                  ╰ DiffID: sha256:7d44a7543042a0404622dbc9ae983829d063abc8
                        │     │                            2d3bf284ad2440273a0c71ed 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-25638 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areview
                        │     │                          ed+ecosystem%3Amaven 
                        │     ├ Title           : dnsjava: Improper response validation allowing DNSSEC bypass 
                        │     ├ Description     : dnsjava is an implementation of DNS in Java. Records in
                        │     │                   DNS replies are not checked for their relevance to the query,
                        │     │                    allowing an attacker to respond with RRs from different
                        │     │                   zones. This vulnerability is fixed in 3.6.0. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs           ╭ [0]: CWE-345 
                        │     │                  ╰ [1]: CWE-349 
                        │     ├ VendorSeverity   ╭ ghsa  : 3 
                        │     │                  ╰ redhat: 3 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H
                        │     │                  │        │           /I:H/A:L 
                        │     │                  │        ╰ V3Score : 8.9 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H
                        │     │                           │           /I:H/A:L 
                        │     │                           ╰ V3Score : 8.9 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-25638 
                        │     │                  ├ [1]: https://github.com/dnsjava/dnsjava 
                        │     │                  ├ [2]: https://github.com/dnsjava/dnsjava/commit/bc51df1c
                        │     │                  │      455e6c9fb7cbd42fcb6d62d16047818d 
                        │     │                  ├ [3]: https://github.com/dnsjava/dnsjava/security/adviso
                        │     │                  │      ries/GHSA-cfxw-4h78-h7fw 
                        │     │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-25638 
                        │     │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2024-25638 
                        │     ├ PublishedDate   : 2024-07-22T14:15:04.593Z 
                        │     ╰ LastModifiedDate: 2024-07-24T12:55:13.223Z 
                        ├ [1] ╭ VulnerabilityID : GHSA-crjg-w57m-rqqf 
                        │     ├ PkgName         : dnsjava:dnsjava 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/dnsjava/dnsjava@3.5.3 
                        │     │                  ╰ UID : fcd3d0c2bf50859 
                        │     ├ InstalledVersion: 3.5.3 
                        │     ├ FixedVersion    : 3.6.0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:55783352ae40a41a855f2505478a8fb805bc1a11
                        │     │                  │         60b1c5c9b91350e5a64a9262 
                        │     │                  ╰ DiffID: sha256:7d44a7543042a0404622dbc9ae983829d063abc8
                        │     │                            2d3bf284ad2440273a0c71ed 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://github.com/advisories/GHSA-crjg-w57m-rqqf 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areview
                        │     │                          ed+ecosystem%3Amaven 
                        │     ├ Title           : DNSJava vulnerable to KeyTrap - Denial-of-Service
                        │     │                   Algorithmic Complexity Attacks 
                        │     ├ Description     : ### Impact
                        │     │                   Users using the `ValidatingResolver` for DNSSEC validation
                        │     │                   can run into CPU exhaustion with specially crafted
                        │     │                   DNSSEC-signed zones.
                        │     │                   
                        │     │                   ### Patches
                        │     │                   Users should upgrade to dnsjava v3.6.0
                        │     │                   
                        │     │                   ### Workarounds
                        │     │                   Although not recommended, only using a non-validating
                        │     │                   resolver, will remove the vulnerability. 
                        │     │                   
                        │     │                   ### References
                        │     │                   https://www.athene-center.de/en/keytrap
                        │     │                    
                        │     ├ Severity        : MEDIUM 
                        │     ├ VendorSeverity   ─ ghsa: 2 
                        │     ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I
                        │     │                         │           :N/A:H 
                        │     │                         ╰ V3Score : 6.5 
                        │     ╰ References       ╭ [0]: https://github.com/dnsjava/dnsjava 
                        │                        ├ [1]: https://github.com/dnsjava/dnsjava/commit/07ac36a1
                        │                        │      1578cc1bce0cd8ddf2fe568f062aee78 
                        │                        ├ [2]: https://github.com/dnsjava/dnsjava/commit/3ddc45ce
                        │                        │      8cdb5c2274e10b7401416f497694e1cf 
                        │                        ╰ [3]: https://github.com/dnsjava/dnsjava/security/adviso
                        │                               ries/GHSA-crjg-w57m-rqqf 
                        ╰ [2] ╭ VulnerabilityID : GHSA-mmwx-rj87-vfgr 
                              ├ PkgName         : dnsjava:dnsjava 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ PkgIdentifier    ╭ PURL: pkg:maven/dnsjava/dnsjava@3.5.3 
                              │                  ╰ UID : fcd3d0c2bf50859 
                              ├ InstalledVersion: 3.5.3 
                              ├ FixedVersion    : 3.6.0 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:55783352ae40a41a855f2505478a8fb805bc1a11
                              │                  │         60b1c5c9b91350e5a64a9262 
                              │                  ╰ DiffID: sha256:7d44a7543042a0404622dbc9ae983829d063abc8
                              │                            2d3bf284ad2440273a0c71ed 
                              ├ SeveritySource  : ghsa 
                              ├ PrimaryURL      : https://github.com/advisories/GHSA-mmwx-rj87-vfgr 
                              ├ DataSource       ╭ ID  : ghsa 
                              │                  ├ Name: GitHub Security Advisory Maven 
                              │                  ╰ URL : https://github.com/advisories?query=type%3Areview
                              │                          ed+ecosystem%3Amaven 
                              ├ Title           : DNSJava affected by KeyTrap - NSEC3 closest encloser
                              │                   proof can exhaust CPU resources 
                              ├ Description     : ### Impact
                              │                   Users using the `ValidatingResolver` for DNSSEC validation
                              │                   can run into CPU exhaustion with specially crafted
                              │                   DNSSEC-signed zones.
                              │                   
                              │                   ### Patches
                              │                   Users should upgrade to dnsjava v3.6.0
                              │                   
                              │                   ### Workarounds
                              │                   Although not recommended, only using a non-validating
                              │                   resolver, will remove the vulnerability.
                              │                   
                              │                   ### References
                              │                   https://www.athene-center.de/en/keytrap
                              │                    
                              ├ Severity        : MEDIUM 
                              ├ VendorSeverity   ─ ghsa: 2 
                              ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I
                              │                         │           :N/A:H 
                              │                         ╰ V3Score : 6.5 
                              ╰ References       ╭ [0]: https://github.com/dnsjava/dnsjava 
                                                 ├ [1]: https://github.com/dnsjava/dnsjava/commit/711af79b
                                                 │      e3214f52daa5c846b95766dc0a075116 
                                                 ╰ [2]: https://github.com/dnsjava/dnsjava/security/adviso
                                                        ries/GHSA-mmwx-rj87-vfgr 
````
