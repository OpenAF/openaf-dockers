````yaml
╭ [0] ╭ Target         : openaf/oaf:8-latest (alpine 3.20.2) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2024-7264 
│                       │     ├ PkgID           : curl@8.9.0-r0 
│                       │     ├ PkgName         : curl 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.9.0-r0?arch=x86_64&distro=3.20.2 
│                       │     │                  ╰ UID : 13907d381c8842c9 
│                       │     ├ InstalledVersion: 8.9.0-r0 
│                       │     ├ FixedVersion    : 8.9.1-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:cc26814656db9e473a7aad40b4b7cfecdb0a7db75a73b
│                       │     │                  │         38f91cf4a4f920a1cda 
│                       │     │                  ╰ DiffID: sha256:4f1f1815dddf626ca1c1e75b7e5e9ba3796324018f6cc
│                       │     │                            418c2d4c267aeae3829 
│                       │     ├ SeveritySource  : nvd 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-7264 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : curl: libcurl: ASN.1 date parser overread 
│                       │     ├ Description     : libcurl's ASN1 parser code has the `GTime2str()` function,
│                       │     │                   used for parsing an
│                       │     │                   ASN.1 Generalized Time field. If given an syntactically
│                       │     │                   incorrect field, the
│                       │     │                   parser might end up using -1 for the length of the *time
│                       │     │                   fraction*, leading to
│                       │     │                   a `strlen()` getting performed on a pointer to a heap buffer
│                       │     │                   area that is not
│                       │     │                   (purposely) null terminated.
│                       │     │                   
│                       │     │                   This flaw most likely leads to a crash, but can also lead to
│                       │     │                   heap contents
│                       │     │                   getting returned to the application when
│                       │     │                   [CURLINFO_CERTINFO](https://curl.se/libcurl/c/CURLINFO_CERTIN
│                       │     │                   FO.html) is used. 
│                       │     ├ Severity        : MEDIUM 
│                       │     ├ CweIDs           ─ [0]: CWE-125 
│                       │     ├ VendorSeverity   ╭ cbl-mariner: 2 
│                       │     │                  ├ nvd        : 2 
│                       │     │                  ├ photon     : 2 
│                       │     │                  ├ redhat     : 1 
│                       │     │                  ╰ ubuntu     : 2 
│                       │     ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/
│                       │     │                  │        │           A:H 
│                       │     │                  │        ╰ V3Score : 6.5 
│                       │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:N/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 5.3 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/07/31/1 
│                       │     │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2024-7264 
│                       │     │                  ├ [2]: https://curl.se/docs/CVE-2024-7264.html 
│                       │     │                  ├ [3]: https://curl.se/docs/CVE-2024-7264.json 
│                       │     │                  ├ [4]: https://hackerone.com/reports/2629968 
│                       │     │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2024-7264 
│                       │     │                  ├ [6]: https://ubuntu.com/security/notices/USN-6944-1 
│                       │     │                  ├ [7]: https://ubuntu.com/security/notices/USN-6944-2 
│                       │     │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2024-7264 
│                       │     ├ PublishedDate   : 2024-07-31T08:15:02.657Z 
│                       │     ╰ LastModifiedDate: 2024-08-12T17:30:51.88Z 
│                       ├ [1] ╭ VulnerabilityID : CVE-2024-6119 
│                       │     ├ PkgID           : libcrypto3@3.3.1-r3 
│                       │     ├ PkgName         : libcrypto3 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.3.1-r3?arch=x86_64&distro=
│                       │     │                  │       3.20.2 
│                       │     │                  ╰ UID : ed0921710eb7b515 
│                       │     ├ InstalledVersion: 3.3.1-r3 
│                       │     ├ FixedVersion    : 3.3.2-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:cc26814656db9e473a7aad40b4b7cfecdb0a7db75a73b
│                       │     │                  │         38f91cf4a4f920a1cda 
│                       │     │                  ╰ DiffID: sha256:4f1f1815dddf626ca1c1e75b7e5e9ba3796324018f6cc
│                       │     │                            418c2d4c267aeae3829 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-6119 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : openssl: Possible denial of service in X.509 name checks 
│                       │     ├ Description     : Issue summary: Applications performing certificate name
│                       │     │                   checks (e.g., TLS
│                       │     │                   clients checking server certificates) may attempt to read an
│                       │     │                   invalid memory
│                       │     │                   address resulting in abnormal termination of the application
│                       │     │                   process.
│                       │     │                   
│                       │     │                   Impact summary: Abnormal termination of an application can a
│                       │     │                   cause a denial of
│                       │     │                   service.
│                       │     │                   Applications performing certificate name checks (e.g., TLS
│                       │     │                   clients checking
│                       │     │                   server certificates) may attempt to read an invalid memory
│                       │     │                   address when
│                       │     │                   comparing the expected name with an `otherName` subject
│                       │     │                   alternative name of an
│                       │     │                   X.509 certificate. This may result in an exception that
│                       │     │                   terminates the
│                       │     │                   application program.
│                       │     │                   Note that basic certificate chain validation (signatures,
│                       │     │                   dates, ...) is not
│                       │     │                   affected, the denial of service can occur only when the
│                       │     │                   application also
│                       │     │                   specifies an expected DNS name, Email address or IP address.
│                       │     │                   TLS servers rarely solicit client certificates, and even when
│                       │     │                    they do, they
│                       │     │                   generally don't perform a name check against a reference
│                       │     │                   identifier (expected
│                       │     │                   identity), but rather extract the presented identity after
│                       │     │                   checking the
│                       │     │                   certificate chain.  So TLS servers are generally not affected
│                       │     │                    and the severity
│                       │     │                   of the issue is Moderate.
│                       │     │                   The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected by
│                       │     │                    this issue. 
│                       │     ├ Severity        : MEDIUM 
│                       │     ├ CweIDs           ─ [0]: CWE-843 
│                       │     ├ VendorSeverity   ╭ redhat: 2 
│                       │     │                  ╰ ubuntu: 2 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 5.9 
│                       │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-6119 
│                       │     │                  ├ [1]: https://github.com/openssl/openssl/commit/05f360d9e849a
│                       │     │                  │      1b277db628f1f13083a7f8dd04f 
│                       │     │                  ├ [2]: https://github.com/openssl/openssl/commit/06d1dc3fa96a2
│                       │     │                  │      ba5a3e22735a033012aadc9f0d6 
│                       │     │                  ├ [3]: https://github.com/openssl/openssl/commit/621f3729831b0
│                       │     │                  │      5ee828a3203eddb621d014ff2b2 
│                       │     │                  ├ [4]: https://github.com/openssl/openssl/commit/7dfcee2cd2a63
│                       │     │                  │      b2c64b9b4b0850be64cb695b0a0 
│                       │     │                  ├ [5]: https://github.com/openssl/openssl/security/advisories/
│                       │     │                  │      GHSA-5qrj-vq78-58fj 
│                       │     │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2024-6119 
│                       │     │                  ├ [7]: https://openssl-library.org/news/secadv/20240903.txt 
│                       │     │                  ├ [8]: https://ubuntu.com/security/notices/USN-6986-1 
│                       │     │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2024-6119 
│                       │     ├ PublishedDate   : 2024-09-03T16:15:07.177Z 
│                       │     ╰ LastModifiedDate: 2024-09-03T21:35:12.987Z 
│                       ├ [2] ╭ VulnerabilityID : CVE-2024-7264 
│                       │     ├ PkgID           : libcurl@8.9.0-r0 
│                       │     ├ PkgName         : libcurl 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.9.0-r0?arch=x86_64&distro=3.2
│                       │     │                  │       0.2 
│                       │     │                  ╰ UID : d23fb94f69337040 
│                       │     ├ InstalledVersion: 8.9.0-r0 
│                       │     ├ FixedVersion    : 8.9.1-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:cc26814656db9e473a7aad40b4b7cfecdb0a7db75a73b
│                       │     │                  │         38f91cf4a4f920a1cda 
│                       │     │                  ╰ DiffID: sha256:4f1f1815dddf626ca1c1e75b7e5e9ba3796324018f6cc
│                       │     │                            418c2d4c267aeae3829 
│                       │     ├ SeveritySource  : nvd 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-7264 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : curl: libcurl: ASN.1 date parser overread 
│                       │     ├ Description     : libcurl's ASN1 parser code has the `GTime2str()` function,
│                       │     │                   used for parsing an
│                       │     │                   ASN.1 Generalized Time field. If given an syntactically
│                       │     │                   incorrect field, the
│                       │     │                   parser might end up using -1 for the length of the *time
│                       │     │                   fraction*, leading to
│                       │     │                   a `strlen()` getting performed on a pointer to a heap buffer
│                       │     │                   area that is not
│                       │     │                   (purposely) null terminated.
│                       │     │                   
│                       │     │                   This flaw most likely leads to a crash, but can also lead to
│                       │     │                   heap contents
│                       │     │                   getting returned to the application when
│                       │     │                   [CURLINFO_CERTINFO](https://curl.se/libcurl/c/CURLINFO_CERTIN
│                       │     │                   FO.html) is used. 
│                       │     ├ Severity        : MEDIUM 
│                       │     ├ CweIDs           ─ [0]: CWE-125 
│                       │     ├ VendorSeverity   ╭ cbl-mariner: 2 
│                       │     │                  ├ nvd        : 2 
│                       │     │                  ├ photon     : 2 
│                       │     │                  ├ redhat     : 1 
│                       │     │                  ╰ ubuntu     : 2 
│                       │     ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/
│                       │     │                  │        │           A:H 
│                       │     │                  │        ╰ V3Score : 6.5 
│                       │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:N/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 5.3 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/07/31/1 
│                       │     │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2024-7264 
│                       │     │                  ├ [2]: https://curl.se/docs/CVE-2024-7264.html 
│                       │     │                  ├ [3]: https://curl.se/docs/CVE-2024-7264.json 
│                       │     │                  ├ [4]: https://hackerone.com/reports/2629968 
│                       │     │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2024-7264 
│                       │     │                  ├ [6]: https://ubuntu.com/security/notices/USN-6944-1 
│                       │     │                  ├ [7]: https://ubuntu.com/security/notices/USN-6944-2 
│                       │     │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2024-7264 
│                       │     ├ PublishedDate   : 2024-07-31T08:15:02.657Z 
│                       │     ╰ LastModifiedDate: 2024-08-12T17:30:51.88Z 
│                       ├ [3] ╭ VulnerabilityID : CVE-2024-45490 
│                       │     ├ PkgID           : libexpat@2.6.2-r0 
│                       │     ├ PkgName         : libexpat 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libexpat@2.6.2-r0?arch=x86_64&distro=3.
│                       │     │                  │       20.2 
│                       │     │                  ╰ UID : fede3295dcb07bb3 
│                       │     ├ InstalledVersion: 2.6.2-r0 
│                       │     ├ FixedVersion    : 2.6.3-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:cc26814656db9e473a7aad40b4b7cfecdb0a7db75a73b
│                       │     │                  │         38f91cf4a4f920a1cda 
│                       │     │                  ╰ DiffID: sha256:4f1f1815dddf626ca1c1e75b7e5e9ba3796324018f6cc
│                       │     │                            418c2d4c267aeae3829 
│                       │     ├ SeveritySource  : nvd 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-45490 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : libexpat: Negative Length Parsing Vulnerability in libexpat 
│                       │     ├ Description     : An issue was discovered in libexpat before 2.6.3. xmlparse.c
│                       │     │                   does not reject a negative length for XML_ParseBuffer. 
│                       │     ├ Severity        : CRITICAL 
│                       │     ├ CweIDs           ─ [0]: CWE-611 
│                       │     ├ VendorSeverity   ╭ nvd   : 4 
│                       │     │                  ├ photon: 4 
│                       │     │                  ├ redhat: 2 
│                       │     │                  ╰ ubuntu: 2 
│                       │     ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/
│                       │     │                  │        │           A:H 
│                       │     │                  │        ╰ V3Score : 9.8 
│                       │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:L/
│                       │     │                           │           A:L 
│                       │     │                           ╰ V3Score : 5.1 
│                       │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-45490 
│                       │     │                  ├ [1]: https://github.com/libexpat/libexpat/blob/R_2_6_3/expat
│                       │     │                  │      /Changes 
│                       │     │                  ├ [2]: https://github.com/libexpat/libexpat/issues/887 
│                       │     │                  ├ [3]: https://github.com/libexpat/libexpat/pull/890 
│                       │     │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-45490 
│                       │     │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2024-45490 
│                       │     ├ PublishedDate   : 2024-08-30T03:15:03.757Z 
│                       │     ╰ LastModifiedDate: 2024-09-04T14:28:19.313Z 
│                       ├ [4] ╭ VulnerabilityID : CVE-2024-45491 
│                       │     ├ PkgID           : libexpat@2.6.2-r0 
│                       │     ├ PkgName         : libexpat 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libexpat@2.6.2-r0?arch=x86_64&distro=3.
│                       │     │                  │       20.2 
│                       │     │                  ╰ UID : fede3295dcb07bb3 
│                       │     ├ InstalledVersion: 2.6.2-r0 
│                       │     ├ FixedVersion    : 2.6.3-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:cc26814656db9e473a7aad40b4b7cfecdb0a7db75a73b
│                       │     │                  │         38f91cf4a4f920a1cda 
│                       │     │                  ╰ DiffID: sha256:4f1f1815dddf626ca1c1e75b7e5e9ba3796324018f6cc
│                       │     │                            418c2d4c267aeae3829 
│                       │     ├ SeveritySource  : nvd 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-45491 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : libexpat: Integer Overflow or Wraparound 
│                       │     ├ Description     : An issue was discovered in libexpat before 2.6.3. dtdCopy in
│                       │     │                   xmlparse.c can have an integer overflow for nDefaultAtts on
│                       │     │                   32-bit platforms (where UINT_MAX equals SIZE_MAX). 
│                       │     ├ Severity        : CRITICAL 
│                       │     ├ CweIDs           ─ [0]: CWE-190 
│                       │     ├ VendorSeverity   ╭ nvd   : 4 
│                       │     │                  ├ photon: 4 
│                       │     │                  ├ redhat: 2 
│                       │     │                  ╰ ubuntu: 2 
│                       │     ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/
│                       │     │                  │        │           A:H 
│                       │     │                  │        ╰ V3Score : 9.8 
│                       │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 7.5 
│                       │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-45491 
│                       │     │                  ├ [1]: https://github.com/libexpat/libexpat/blob/R_2_6_3/expat
│                       │     │                  │      /Changes 
│                       │     │                  ├ [2]: https://github.com/libexpat/libexpat/issues/888 
│                       │     │                  ├ [3]: https://github.com/libexpat/libexpat/pull/891 
│                       │     │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-45491 
│                       │     │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2024-45491 
│                       │     ├ PublishedDate   : 2024-08-30T03:15:03.85Z 
│                       │     ╰ LastModifiedDate: 2024-09-04T14:28:33.953Z 
│                       ├ [5] ╭ VulnerabilityID : CVE-2024-45492 
│                       │     ├ PkgID           : libexpat@2.6.2-r0 
│                       │     ├ PkgName         : libexpat 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libexpat@2.6.2-r0?arch=x86_64&distro=3.
│                       │     │                  │       20.2 
│                       │     │                  ╰ UID : fede3295dcb07bb3 
│                       │     ├ InstalledVersion: 2.6.2-r0 
│                       │     ├ FixedVersion    : 2.6.3-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:cc26814656db9e473a7aad40b4b7cfecdb0a7db75a73b
│                       │     │                  │         38f91cf4a4f920a1cda 
│                       │     │                  ╰ DiffID: sha256:4f1f1815dddf626ca1c1e75b7e5e9ba3796324018f6cc
│                       │     │                            418c2d4c267aeae3829 
│                       │     ├ SeveritySource  : nvd 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-45492 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : libexpat: integer overflow 
│                       │     ├ Description     : An issue was discovered in libexpat before 2.6.3.
│                       │     │                   nextScaffoldPart in xmlparse.c can have an integer overflow
│                       │     │                   for m_groupSize on 32-bit platforms (where UINT_MAX equals
│                       │     │                   SIZE_MAX). 
│                       │     ├ Severity        : CRITICAL 
│                       │     ├ CweIDs           ─ [0]: CWE-190 
│                       │     ├ VendorSeverity   ╭ nvd   : 4 
│                       │     │                  ├ photon: 4 
│                       │     │                  ├ redhat: 2 
│                       │     │                  ╰ ubuntu: 2 
│                       │     ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/
│                       │     │                  │        │           A:H 
│                       │     │                  │        ╰ V3Score : 9.8 
│                       │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 6.2 
│                       │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-45492 
│                       │     │                  ├ [1]: https://github.com/libexpat/libexpat/blob/R_2_6_3/expat
│                       │     │                  │      /Changes 
│                       │     │                  ├ [2]: https://github.com/libexpat/libexpat/issues/889 
│                       │     │                  ├ [3]: https://github.com/libexpat/libexpat/pull/892 
│                       │     │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-45492 
│                       │     │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2024-45492 
│                       │     ├ PublishedDate   : 2024-08-30T03:15:03.93Z 
│                       │     ╰ LastModifiedDate: 2024-09-04T14:28:41.76Z 
│                       ├ [6] ╭ VulnerabilityID : CVE-2024-6119 
│                       │     ├ PkgID           : libssl3@3.3.1-r3 
│                       │     ├ PkgName         : libssl3 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.3.1-r3?arch=x86_64&distro=3.2
│                       │     │                  │       0.2 
│                       │     │                  ╰ UID : 8ede7598835f9c6c 
│                       │     ├ InstalledVersion: 3.3.1-r3 
│                       │     ├ FixedVersion    : 3.3.2-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:cc26814656db9e473a7aad40b4b7cfecdb0a7db75a73b
│                       │     │                  │         38f91cf4a4f920a1cda 
│                       │     │                  ╰ DiffID: sha256:4f1f1815dddf626ca1c1e75b7e5e9ba3796324018f6cc
│                       │     │                            418c2d4c267aeae3829 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-6119 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : openssl: Possible denial of service in X.509 name checks 
│                       │     ├ Description     : Issue summary: Applications performing certificate name
│                       │     │                   checks (e.g., TLS
│                       │     │                   clients checking server certificates) may attempt to read an
│                       │     │                   invalid memory
│                       │     │                   address resulting in abnormal termination of the application
│                       │     │                   process.
│                       │     │                   
│                       │     │                   Impact summary: Abnormal termination of an application can a
│                       │     │                   cause a denial of
│                       │     │                   service.
│                       │     │                   Applications performing certificate name checks (e.g., TLS
│                       │     │                   clients checking
│                       │     │                   server certificates) may attempt to read an invalid memory
│                       │     │                   address when
│                       │     │                   comparing the expected name with an `otherName` subject
│                       │     │                   alternative name of an
│                       │     │                   X.509 certificate. This may result in an exception that
│                       │     │                   terminates the
│                       │     │                   application program.
│                       │     │                   Note that basic certificate chain validation (signatures,
│                       │     │                   dates, ...) is not
│                       │     │                   affected, the denial of service can occur only when the
│                       │     │                   application also
│                       │     │                   specifies an expected DNS name, Email address or IP address.
│                       │     │                   TLS servers rarely solicit client certificates, and even when
│                       │     │                    they do, they
│                       │     │                   generally don't perform a name check against a reference
│                       │     │                   identifier (expected
│                       │     │                   identity), but rather extract the presented identity after
│                       │     │                   checking the
│                       │     │                   certificate chain.  So TLS servers are generally not affected
│                       │     │                    and the severity
│                       │     │                   of the issue is Moderate.
│                       │     │                   The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected by
│                       │     │                    this issue. 
│                       │     ├ Severity        : MEDIUM 
│                       │     ├ CweIDs           ─ [0]: CWE-843 
│                       │     ├ VendorSeverity   ╭ redhat: 2 
│                       │     │                  ╰ ubuntu: 2 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 5.9 
│                       │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-6119 
│                       │     │                  ├ [1]: https://github.com/openssl/openssl/commit/05f360d9e849a
│                       │     │                  │      1b277db628f1f13083a7f8dd04f 
│                       │     │                  ├ [2]: https://github.com/openssl/openssl/commit/06d1dc3fa96a2
│                       │     │                  │      ba5a3e22735a033012aadc9f0d6 
│                       │     │                  ├ [3]: https://github.com/openssl/openssl/commit/621f3729831b0
│                       │     │                  │      5ee828a3203eddb621d014ff2b2 
│                       │     │                  ├ [4]: https://github.com/openssl/openssl/commit/7dfcee2cd2a63
│                       │     │                  │      b2c64b9b4b0850be64cb695b0a0 
│                       │     │                  ├ [5]: https://github.com/openssl/openssl/security/advisories/
│                       │     │                  │      GHSA-5qrj-vq78-58fj 
│                       │     │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2024-6119 
│                       │     │                  ├ [7]: https://openssl-library.org/news/secadv/20240903.txt 
│                       │     │                  ├ [8]: https://ubuntu.com/security/notices/USN-6986-1 
│                       │     │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2024-6119 
│                       │     ├ PublishedDate   : 2024-09-03T16:15:07.177Z 
│                       │     ╰ LastModifiedDate: 2024-09-03T21:35:12.987Z 
│                       ╰ [7] ╭ VulnerabilityID : CVE-2024-6119 
│                             ├ PkgID           : openssl@3.3.1-r3 
│                             ├ PkgName         : openssl 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.3.1-r3?arch=x86_64&distro=3.2
│                             │                  │       0.2 
│                             │                  ╰ UID : 11fa069d45ee03bc 
│                             ├ InstalledVersion: 3.3.1-r3 
│                             ├ FixedVersion    : 3.3.2-r0 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:cc26814656db9e473a7aad40b4b7cfecdb0a7db75a73b
│                             │                  │         38f91cf4a4f920a1cda 
│                             │                  ╰ DiffID: sha256:4f1f1815dddf626ca1c1e75b7e5e9ba3796324018f6cc
│                             │                            418c2d4c267aeae3829 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-6119 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Title           : openssl: Possible denial of service in X.509 name checks 
│                             ├ Description     : Issue summary: Applications performing certificate name
│                             │                   checks (e.g., TLS
│                             │                   clients checking server certificates) may attempt to read an
│                             │                   invalid memory
│                             │                   address resulting in abnormal termination of the application
│                             │                   process.
│                             │                   
│                             │                   Impact summary: Abnormal termination of an application can a
│                             │                   cause a denial of
│                             │                   service.
│                             │                   Applications performing certificate name checks (e.g., TLS
│                             │                   clients checking
│                             │                   server certificates) may attempt to read an invalid memory
│                             │                   address when
│                             │                   comparing the expected name with an `otherName` subject
│                             │                   alternative name of an
│                             │                   X.509 certificate. This may result in an exception that
│                             │                   terminates the
│                             │                   application program.
│                             │                   Note that basic certificate chain validation (signatures,
│                             │                   dates, ...) is not
│                             │                   affected, the denial of service can occur only when the
│                             │                   application also
│                             │                   specifies an expected DNS name, Email address or IP address.
│                             │                   TLS servers rarely solicit client certificates, and even when
│                             │                    they do, they
│                             │                   generally don't perform a name check against a reference
│                             │                   identifier (expected
│                             │                   identity), but rather extract the presented identity after
│                             │                   checking the
│                             │                   certificate chain.  So TLS servers are generally not affected
│                             │                    and the severity
│                             │                   of the issue is Moderate.
│                             │                   The FIPS modules in 3.3, 3.2, 3.1 and 3.0 are not affected by
│                             │                    this issue. 
│                             ├ Severity        : MEDIUM 
│                             ├ CweIDs           ─ [0]: CWE-843 
│                             ├ VendorSeverity   ╭ redhat: 2 
│                             │                  ╰ ubuntu: 2 
│                             ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/
│                             │                           │           A:H 
│                             │                           ╰ V3Score : 5.9 
│                             ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-6119 
│                             │                  ├ [1]: https://github.com/openssl/openssl/commit/05f360d9e849a
│                             │                  │      1b277db628f1f13083a7f8dd04f 
│                             │                  ├ [2]: https://github.com/openssl/openssl/commit/06d1dc3fa96a2
│                             │                  │      ba5a3e22735a033012aadc9f0d6 
│                             │                  ├ [3]: https://github.com/openssl/openssl/commit/621f3729831b0
│                             │                  │      5ee828a3203eddb621d014ff2b2 
│                             │                  ├ [4]: https://github.com/openssl/openssl/commit/7dfcee2cd2a63
│                             │                  │      b2c64b9b4b0850be64cb695b0a0 
│                             │                  ├ [5]: https://github.com/openssl/openssl/security/advisories/
│                             │                  │      GHSA-5qrj-vq78-58fj 
│                             │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2024-6119 
│                             │                  ├ [7]: https://openssl-library.org/news/secadv/20240903.txt 
│                             │                  ├ [8]: https://ubuntu.com/security/notices/USN-6986-1 
│                             │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2024-6119 
│                             ├ PublishedDate   : 2024-09-03T16:15:07.177Z 
│                             ╰ LastModifiedDate: 2024-09-03T21:35:12.987Z 
╰ [1] ╭ Target: Java 
      ├ Class : lang-pkgs 
      ╰ Type  : jar 
````
