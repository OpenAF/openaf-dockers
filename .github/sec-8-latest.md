````yaml
╭ [0] ╭ Target         : openaf/oaf:8-latest (alpine 3.20.3) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2024-9143 
│                       │     ├ PkgID           : libcrypto3@3.3.2-r0 
│                       │     ├ PkgName         : libcrypto3 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.3.2-r0?arch=x86_64&distro=
│                       │     │                  │       3.20.3 
│                       │     │                  ╰ UID : 33eb4551a5ab015e 
│                       │     ├ InstalledVersion: 3.3.2-r0 
│                       │     ├ FixedVersion    : 3.3.2-r1 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee2
│                       │     │                  │         801b3e28133325c482b 
│                       │     │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed2
│                       │     │                            8ea1250ef005595c5f9 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-9143 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : openssl: Low-level invalid GF(2^m) parameters lead to OOB
│                       │     │                   memory access 
│                       │     ├ Description     : Issue summary: Use of the low-level GF(2^m) elliptic curve
│                       │     │                   APIs with untrusted
│                       │     │                   explicit values for the field polynomial can lead to
│                       │     │                   out-of-bounds memory reads
│                       │     │                   or writes.
│                       │     │                   
│                       │     │                   Impact summary: Out of bound memory writes can lead to an
│                       │     │                   application crash or
│                       │     │                   even a possibility of a remote code execution, however, in
│                       │     │                   all the protocols
│                       │     │                   involving Elliptic Curve Cryptography that we're aware of,
│                       │     │                   either only "named
│                       │     │                   curves" are supported, or, if explicit curve parameters are
│                       │     │                   supported, they
│                       │     │                   specify an X9.62 encoding of binary (GF(2^m)) curves that
│                       │     │                   can't represent
│                       │     │                   problematic input values. Thus the likelihood of existence of
│                       │     │                    a vulnerable
│                       │     │                   application is low.
│                       │     │                   In particular, the X9.62 encoding is used for ECC keys in
│                       │     │                   X.509 certificates,
│                       │     │                   so problematic inputs cannot occur in the context of
│                       │     │                   processing X.509
│                       │     │                   certificates.  Any problematic use-cases would have to be
│                       │     │                   using an "exotic"
│                       │     │                   curve encoding.
│                       │     │                   The affected APIs include: EC_GROUP_new_curve_GF2m(),
│                       │     │                   EC_GROUP_new_from_params(),
│                       │     │                   and various supporting BN_GF2m_*() functions.
│                       │     │                   Applications working with "exotic" explicit binary (GF(2^m))
│                       │     │                   curve parameters,
│                       │     │                   that make it possible to represent invalid field polynomials
│                       │     │                   with a zero
│                       │     │                   constant term, via the above or similar APIs, may terminate
│                       │     │                   abruptly as a
│                       │     │                   result of reading or writing outside of array bounds.  Remote
│                       │     │                    code execution
│                       │     │                   cannot easily be ruled out.
│                       │     │                   The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected by
│                       │     │                    this issue. 
│                       │     ├ Severity        : LOW 
│                       │     ├ CweIDs           ─ [0]: CWE-787 
│                       │     ├ VendorSeverity   ╭ redhat: 1 
│                       │     │                  ╰ ubuntu: 1 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/
│                       │     │                           │           A:L 
│                       │     │                           ╰ V3Score : 3.7 
│                       │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-9143 
│                       │     │                  ├ [1]: https://github.com/openssl/openssl/commit/72ae83ad214d2
│                       │     │                  │      eef262461365a1975707f862712 
│                       │     │                  ├ [2]: https://github.com/openssl/openssl/commit/bc7e04d7c8d50
│                       │     │                  │      9fb78fc0e285aa948fb0da04700 
│                       │     │                  ├ [3]: https://github.com/openssl/openssl/commit/c0d3e4d32d280
│                       │     │                  │      5f49bec30547f225bc4d092e1f4 
│                       │     │                  ├ [4]: https://github.com/openssl/openssl/commit/fdf6723362ca5
│                       │     │                  │      1bd883295efe206cb5b1cfa5154 
│                       │     │                  ├ [5]: https://github.openssl.org/openssl/extended-releases/co
│                       │     │                  │      mmit/8efc0cbaa8ebba8e116f7b81a876a4123594d86a 
│                       │     │                  ├ [6]: https://github.openssl.org/openssl/extended-releases/co
│                       │     │                  │      mmit/9d576994cec2b7aa37a91740ea7e680810957e41 
│                       │     │                  ├ [7]: https://nvd.nist.gov/vuln/detail/CVE-2024-9143 
│                       │     │                  ├ [8]: https://openssl-library.org/news/secadv/20241016.txt 
│                       │     │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2024-9143 
│                       │     ├ PublishedDate   : 2024-10-16T17:15:18.13Z 
│                       │     ╰ LastModifiedDate: 2024-10-18T12:53:04.627Z 
│                       ├ [1] ╭ VulnerabilityID : CVE-2024-9143 
│                       │     ├ PkgID           : libssl3@3.3.2-r0 
│                       │     ├ PkgName         : libssl3 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.3.2-r0?arch=x86_64&distro=3.2
│                       │     │                  │       0.3 
│                       │     │                  ╰ UID : aa5719d6e39bba43 
│                       │     ├ InstalledVersion: 3.3.2-r0 
│                       │     ├ FixedVersion    : 3.3.2-r1 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee2
│                       │     │                  │         801b3e28133325c482b 
│                       │     │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed2
│                       │     │                            8ea1250ef005595c5f9 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-9143 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : openssl: Low-level invalid GF(2^m) parameters lead to OOB
│                       │     │                   memory access 
│                       │     ├ Description     : Issue summary: Use of the low-level GF(2^m) elliptic curve
│                       │     │                   APIs with untrusted
│                       │     │                   explicit values for the field polynomial can lead to
│                       │     │                   out-of-bounds memory reads
│                       │     │                   or writes.
│                       │     │                   
│                       │     │                   Impact summary: Out of bound memory writes can lead to an
│                       │     │                   application crash or
│                       │     │                   even a possibility of a remote code execution, however, in
│                       │     │                   all the protocols
│                       │     │                   involving Elliptic Curve Cryptography that we're aware of,
│                       │     │                   either only "named
│                       │     │                   curves" are supported, or, if explicit curve parameters are
│                       │     │                   supported, they
│                       │     │                   specify an X9.62 encoding of binary (GF(2^m)) curves that
│                       │     │                   can't represent
│                       │     │                   problematic input values. Thus the likelihood of existence of
│                       │     │                    a vulnerable
│                       │     │                   application is low.
│                       │     │                   In particular, the X9.62 encoding is used for ECC keys in
│                       │     │                   X.509 certificates,
│                       │     │                   so problematic inputs cannot occur in the context of
│                       │     │                   processing X.509
│                       │     │                   certificates.  Any problematic use-cases would have to be
│                       │     │                   using an "exotic"
│                       │     │                   curve encoding.
│                       │     │                   The affected APIs include: EC_GROUP_new_curve_GF2m(),
│                       │     │                   EC_GROUP_new_from_params(),
│                       │     │                   and various supporting BN_GF2m_*() functions.
│                       │     │                   Applications working with "exotic" explicit binary (GF(2^m))
│                       │     │                   curve parameters,
│                       │     │                   that make it possible to represent invalid field polynomials
│                       │     │                   with a zero
│                       │     │                   constant term, via the above or similar APIs, may terminate
│                       │     │                   abruptly as a
│                       │     │                   result of reading or writing outside of array bounds.  Remote
│                       │     │                    code execution
│                       │     │                   cannot easily be ruled out.
│                       │     │                   The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected by
│                       │     │                    this issue. 
│                       │     ├ Severity        : LOW 
│                       │     ├ CweIDs           ─ [0]: CWE-787 
│                       │     ├ VendorSeverity   ╭ redhat: 1 
│                       │     │                  ╰ ubuntu: 1 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/
│                       │     │                           │           A:L 
│                       │     │                           ╰ V3Score : 3.7 
│                       │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-9143 
│                       │     │                  ├ [1]: https://github.com/openssl/openssl/commit/72ae83ad214d2
│                       │     │                  │      eef262461365a1975707f862712 
│                       │     │                  ├ [2]: https://github.com/openssl/openssl/commit/bc7e04d7c8d50
│                       │     │                  │      9fb78fc0e285aa948fb0da04700 
│                       │     │                  ├ [3]: https://github.com/openssl/openssl/commit/c0d3e4d32d280
│                       │     │                  │      5f49bec30547f225bc4d092e1f4 
│                       │     │                  ├ [4]: https://github.com/openssl/openssl/commit/fdf6723362ca5
│                       │     │                  │      1bd883295efe206cb5b1cfa5154 
│                       │     │                  ├ [5]: https://github.openssl.org/openssl/extended-releases/co
│                       │     │                  │      mmit/8efc0cbaa8ebba8e116f7b81a876a4123594d86a 
│                       │     │                  ├ [6]: https://github.openssl.org/openssl/extended-releases/co
│                       │     │                  │      mmit/9d576994cec2b7aa37a91740ea7e680810957e41 
│                       │     │                  ├ [7]: https://nvd.nist.gov/vuln/detail/CVE-2024-9143 
│                       │     │                  ├ [8]: https://openssl-library.org/news/secadv/20241016.txt 
│                       │     │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2024-9143 
│                       │     ├ PublishedDate   : 2024-10-16T17:15:18.13Z 
│                       │     ╰ LastModifiedDate: 2024-10-18T12:53:04.627Z 
│                       ╰ [2] ╭ VulnerabilityID : CVE-2024-9143 
│                             ├ PkgID           : openssl@3.3.2-r0 
│                             ├ PkgName         : openssl 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.3.2-r0?arch=x86_64&distro=3.2
│                             │                  │       0.3 
│                             │                  ╰ UID : aad39ba6d762dc14 
│                             ├ InstalledVersion: 3.3.2-r0 
│                             ├ FixedVersion    : 3.3.2-r1 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:b1f4bc594d61f8bac28325b4a3ba24e1ffdc31d557ee2
│                             │                  │         801b3e28133325c482b 
│                             │                  ╰ DiffID: sha256:8cd304aad7f5e6704c8926ba33357a932f26ae5516ed2
│                             │                            8ea1250ef005595c5f9 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-9143 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Title           : openssl: Low-level invalid GF(2^m) parameters lead to OOB
│                             │                   memory access 
│                             ├ Description     : Issue summary: Use of the low-level GF(2^m) elliptic curve
│                             │                   APIs with untrusted
│                             │                   explicit values for the field polynomial can lead to
│                             │                   out-of-bounds memory reads
│                             │                   or writes.
│                             │                   
│                             │                   Impact summary: Out of bound memory writes can lead to an
│                             │                   application crash or
│                             │                   even a possibility of a remote code execution, however, in
│                             │                   all the protocols
│                             │                   involving Elliptic Curve Cryptography that we're aware of,
│                             │                   either only "named
│                             │                   curves" are supported, or, if explicit curve parameters are
│                             │                   supported, they
│                             │                   specify an X9.62 encoding of binary (GF(2^m)) curves that
│                             │                   can't represent
│                             │                   problematic input values. Thus the likelihood of existence of
│                             │                    a vulnerable
│                             │                   application is low.
│                             │                   In particular, the X9.62 encoding is used for ECC keys in
│                             │                   X.509 certificates,
│                             │                   so problematic inputs cannot occur in the context of
│                             │                   processing X.509
│                             │                   certificates.  Any problematic use-cases would have to be
│                             │                   using an "exotic"
│                             │                   curve encoding.
│                             │                   The affected APIs include: EC_GROUP_new_curve_GF2m(),
│                             │                   EC_GROUP_new_from_params(),
│                             │                   and various supporting BN_GF2m_*() functions.
│                             │                   Applications working with "exotic" explicit binary (GF(2^m))
│                             │                   curve parameters,
│                             │                   that make it possible to represent invalid field polynomials
│                             │                   with a zero
│                             │                   constant term, via the above or similar APIs, may terminate
│                             │                   abruptly as a
│                             │                   result of reading or writing outside of array bounds.  Remote
│                             │                    code execution
│                             │                   cannot easily be ruled out.
│                             │                   The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected by
│                             │                    this issue. 
│                             ├ Severity        : LOW 
│                             ├ CweIDs           ─ [0]: CWE-787 
│                             ├ VendorSeverity   ╭ redhat: 1 
│                             │                  ╰ ubuntu: 1 
│                             ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/
│                             │                           │           A:L 
│                             │                           ╰ V3Score : 3.7 
│                             ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-9143 
│                             │                  ├ [1]: https://github.com/openssl/openssl/commit/72ae83ad214d2
│                             │                  │      eef262461365a1975707f862712 
│                             │                  ├ [2]: https://github.com/openssl/openssl/commit/bc7e04d7c8d50
│                             │                  │      9fb78fc0e285aa948fb0da04700 
│                             │                  ├ [3]: https://github.com/openssl/openssl/commit/c0d3e4d32d280
│                             │                  │      5f49bec30547f225bc4d092e1f4 
│                             │                  ├ [4]: https://github.com/openssl/openssl/commit/fdf6723362ca5
│                             │                  │      1bd883295efe206cb5b1cfa5154 
│                             │                  ├ [5]: https://github.openssl.org/openssl/extended-releases/co
│                             │                  │      mmit/8efc0cbaa8ebba8e116f7b81a876a4123594d86a 
│                             │                  ├ [6]: https://github.openssl.org/openssl/extended-releases/co
│                             │                  │      mmit/9d576994cec2b7aa37a91740ea7e680810957e41 
│                             │                  ├ [7]: https://nvd.nist.gov/vuln/detail/CVE-2024-9143 
│                             │                  ├ [8]: https://openssl-library.org/news/secadv/20241016.txt 
│                             │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2024-9143 
│                             ├ PublishedDate   : 2024-10-16T17:15:18.13Z 
│                             ╰ LastModifiedDate: 2024-10-18T12:53:04.627Z 
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
                              ├ Severity        : LOW 
                              ├ CweIDs           ─ [0]: CWE-1286 
                              ├ VendorSeverity   ╭ ghsa  : 1 
                              │                  ╰ redhat: 1 
                              ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/
                              │                  │        │           A:N 
                              │                  │        ╰ V3Score : 3.7 
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
                              ╰ LastModifiedDate: 2024-10-15T12:57:46.88Z 
````
