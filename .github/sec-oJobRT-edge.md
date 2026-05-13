```yaml
╭ [0] ╭ Target         : openaf/ojobrt:edge (alpine 3.24.0_alpha20260127) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2026-40200 
│                       │     ├ PkgID           : musl@1.2.5-r21 
│                       │     ├ PkgName         : musl 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/musl@1.2.5-r21?arch=x86_64&distro=3.24.
│                       │     │                  │       0_alpha20260127 
│                       │     │                  ╰ UID : a7bafcf4eaef5646 
│                       │     ├ InstalledVersion: 1.2.5-r21 
│                       │     ├ FixedVersion    : 1.2.6-r2 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:4247bce4e6b0154252c90c5d6957b042408d9355ed35e
│                       │     │                  │         d19a18123bc1351925d 
│                       │     │                  ╰ DiffID: sha256:9ba501e4c5064718ae8f48934b6ef4f4f8382700276e9
│                       │     │                            9eb981123702b54ffa0 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40200 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Fingerprint     : sha256:d54ac7e9529e607e200d2edf0b4243d71bfafa6a07a9b2458b8aaf
│                       │     │                   ecf4f39a46 
│                       │     ├ Title           : musl: musl libc: Arbitrary code execution and denial of
│                       │     │                   service via stack-based memory corruption in qsort 
│                       │     ├ Description     : An issue was discovered in musl libc 0.7.10 through 1.2.6.
│                       │     │                   Stack-based memory corruption can occur during qsort of very
│                       │     │                   large arrays, due to incorrectly implemented double-word
│                       │     │                   primitives. The number of elements must exceed about seven
│                       │     │                   million, i.e., the 32nd Leonardo number on 32-bit platforms
│                       │     │                   (or the 64th Leonardo number on 64-bit platforms, which is
│                       │     │                   not practical). 
│                       │     ├ Severity        : HIGH 
│                       │     ├ CweIDs           ─ [0]: CWE-670 
│                       │     ├ VendorSeverity   ─ redhat: 3 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 7.8 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/10/13 
│                       │     │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-40200 
│                       │     │                  ├ [2]: https://musl.libc.org/releases.html 
│                       │     │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-40200 
│                       │     │                  ├ [4]: https://www.cve.org/CVERecord?id=CVE-2026-40200 
│                       │     │                  ╰ [5]: https://www.openwall.com/lists/oss-security/2026/04/10/13 
│                       │     ├ PublishedDate   : 2026-04-10T17:17:14.107Z 
│                       │     ╰ LastModifiedDate: 2026-04-27T19:18:46.69Z 
│                       ├ [1] ╭ VulnerabilityID : CVE-2026-6042 
│                       │     ├ PkgID           : musl@1.2.5-r21 
│                       │     ├ PkgName         : musl 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/musl@1.2.5-r21?arch=x86_64&distro=3.24.
│                       │     │                  │       0_alpha20260127 
│                       │     │                  ╰ UID : a7bafcf4eaef5646 
│                       │     ├ InstalledVersion: 1.2.5-r21 
│                       │     ├ FixedVersion    : 1.2.6-r1 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:4247bce4e6b0154252c90c5d6957b042408d9355ed35e
│                       │     │                  │         d19a18123bc1351925d 
│                       │     │                  ╰ DiffID: sha256:9ba501e4c5064718ae8f48934b6ef4f4f8382700276e9
│                       │     │                            9eb981123702b54ffa0 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6042 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Fingerprint     : sha256:798e38fd393d0bab20e2dd2962fcf7f3bd5594a3350c4d4adedd28
│                       │     │                   b997fee768 
│                       │     ├ Title           : musl libc: GB18030 4-byte Decoder: musl libc: Denial of
│                       │     │                   Service via inefficient algorithmic complexity in iconv 
│                       │     ├ Description     : A security flaw has been discovered in musl libc up to 1.2.6.
│                       │     │                    Affected is the function iconv of the file
│                       │     │                   src/locale/iconv.c of the component GB18030 4-byte Decoder.
│                       │     │                   Performing a manipulation results in inefficient algorithmic
│                       │     │                   complexity. The attack must be initiated from a local
│                       │     │                   position. To fix this issue, it is recommended to deploy a
│                       │     │                   patch. 
│                       │     ├ Severity        : MEDIUM 
│                       │     ├ CweIDs           ╭ [0]: CWE-404 
│                       │     │                  ╰ [1]: CWE-407 
│                       │     ├ VendorSeverity   ─ redhat: 2 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 5.5 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/09/19 
│                       │     │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-6042 
│                       │     │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-6042 
│                       │     │                  ├ [3]: https://vuldb.com/submit/796352 
│                       │     │                  ├ [4]: https://vuldb.com/vuln/356620 
│                       │     │                  ├ [5]: https://vuldb.com/vuln/356620/cti 
│                       │     │                  ├ [6]: https://www.cve.org/CVERecord?id=CVE-2026-6042 
│                       │     │                  ├ [7]: https://www.openwall.com/lists/oss-security/2026/04/02/10 
│                       │     │                  ╰ [8]: https://www.openwall.com/lists/oss-security/2026/04/03/2 
│                       │     ├ PublishedDate   : 2026-04-10T09:16:25.45Z 
│                       │     ╰ LastModifiedDate: 2026-04-24T18:01:13.913Z 
│                       ├ [2] ╭ VulnerabilityID : CVE-2026-40200 
│                       │     ├ PkgID           : musl-utils@1.2.5-r21 
│                       │     ├ PkgName         : musl-utils 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/musl-utils@1.2.5-r21?arch=x86_64&distro
│                       │     │                  │       =3.24.0_alpha20260127 
│                       │     │                  ╰ UID : 6f37302d99121f4f 
│                       │     ├ InstalledVersion: 1.2.5-r21 
│                       │     ├ FixedVersion    : 1.2.6-r2 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:4247bce4e6b0154252c90c5d6957b042408d9355ed35e
│                       │     │                  │         d19a18123bc1351925d 
│                       │     │                  ╰ DiffID: sha256:9ba501e4c5064718ae8f48934b6ef4f4f8382700276e9
│                       │     │                            9eb981123702b54ffa0 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40200 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Fingerprint     : sha256:f88ddcf2aeb4899024ea84ce02a5a456fa1013707809ef9a81f387
│                       │     │                   79235a8c36 
│                       │     ├ Title           : musl: musl libc: Arbitrary code execution and denial of
│                       │     │                   service via stack-based memory corruption in qsort 
│                       │     ├ Description     : An issue was discovered in musl libc 0.7.10 through 1.2.6.
│                       │     │                   Stack-based memory corruption can occur during qsort of very
│                       │     │                   large arrays, due to incorrectly implemented double-word
│                       │     │                   primitives. The number of elements must exceed about seven
│                       │     │                   million, i.e., the 32nd Leonardo number on 32-bit platforms
│                       │     │                   (or the 64th Leonardo number on 64-bit platforms, which is
│                       │     │                   not practical). 
│                       │     ├ Severity        : HIGH 
│                       │     ├ CweIDs           ─ [0]: CWE-670 
│                       │     ├ VendorSeverity   ─ redhat: 3 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 7.8 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/10/13 
│                       │     │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-40200 
│                       │     │                  ├ [2]: https://musl.libc.org/releases.html 
│                       │     │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-40200 
│                       │     │                  ├ [4]: https://www.cve.org/CVERecord?id=CVE-2026-40200 
│                       │     │                  ╰ [5]: https://www.openwall.com/lists/oss-security/2026/04/10/13 
│                       │     ├ PublishedDate   : 2026-04-10T17:17:14.107Z 
│                       │     ╰ LastModifiedDate: 2026-04-27T19:18:46.69Z 
│                       ├ [3] ╭ VulnerabilityID : CVE-2026-6042 
│                       │     ├ PkgID           : musl-utils@1.2.5-r21 
│                       │     ├ PkgName         : musl-utils 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/musl-utils@1.2.5-r21?arch=x86_64&distro
│                       │     │                  │       =3.24.0_alpha20260127 
│                       │     │                  ╰ UID : 6f37302d99121f4f 
│                       │     ├ InstalledVersion: 1.2.5-r21 
│                       │     ├ FixedVersion    : 1.2.6-r1 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:4247bce4e6b0154252c90c5d6957b042408d9355ed35e
│                       │     │                  │         d19a18123bc1351925d 
│                       │     │                  ╰ DiffID: sha256:9ba501e4c5064718ae8f48934b6ef4f4f8382700276e9
│                       │     │                            9eb981123702b54ffa0 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6042 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Fingerprint     : sha256:ebd956c138e554e804485a61056656bcadfa2ae42e5e6f830def87
│                       │     │                   bd81e7d3ff 
│                       │     ├ Title           : musl libc: GB18030 4-byte Decoder: musl libc: Denial of
│                       │     │                   Service via inefficient algorithmic complexity in iconv 
│                       │     ├ Description     : A security flaw has been discovered in musl libc up to 1.2.6.
│                       │     │                    Affected is the function iconv of the file
│                       │     │                   src/locale/iconv.c of the component GB18030 4-byte Decoder.
│                       │     │                   Performing a manipulation results in inefficient algorithmic
│                       │     │                   complexity. The attack must be initiated from a local
│                       │     │                   position. To fix this issue, it is recommended to deploy a
│                       │     │                   patch. 
│                       │     ├ Severity        : MEDIUM 
│                       │     ├ CweIDs           ╭ [0]: CWE-404 
│                       │     │                  ╰ [1]: CWE-407 
│                       │     ├ VendorSeverity   ─ redhat: 2 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 5.5 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/09/19 
│                       │     │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-6042 
│                       │     │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-6042 
│                       │     │                  ├ [3]: https://vuldb.com/submit/796352 
│                       │     │                  ├ [4]: https://vuldb.com/vuln/356620 
│                       │     │                  ├ [5]: https://vuldb.com/vuln/356620/cti 
│                       │     │                  ├ [6]: https://www.cve.org/CVERecord?id=CVE-2026-6042 
│                       │     │                  ├ [7]: https://www.openwall.com/lists/oss-security/2026/04/02/10 
│                       │     │                  ╰ [8]: https://www.openwall.com/lists/oss-security/2026/04/03/2 
│                       │     ├ PublishedDate   : 2026-04-10T09:16:25.45Z 
│                       │     ╰ LastModifiedDate: 2026-04-24T18:01:13.913Z 
│                       ├ [4] ╭ VulnerabilityID : CVE-2026-22184 
│                       │     ├ PkgID           : zlib@1.3.1-r2 
│                       │     ├ PkgName         : zlib 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/zlib@1.3.1-r2?arch=x86_64&distro=3.24.0
│                       │     │                  │       _alpha20260127 
│                       │     │                  ╰ UID : c6f558cca1be2488 
│                       │     ├ InstalledVersion: 1.3.1-r2 
│                       │     ├ FixedVersion    : 1.3.2-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:4247bce4e6b0154252c90c5d6957b042408d9355ed35e
│                       │     │                  │         d19a18123bc1351925d 
│                       │     │                  ╰ DiffID: sha256:9ba501e4c5064718ae8f48934b6ef4f4f8382700276e9
│                       │     │                            9eb981123702b54ffa0 
│                       │     ├ SeveritySource  : nvd 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22184 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Fingerprint     : sha256:d54e73eb7ba346f7c60315b9c46241294e36bf8f70c7ae0378f116
│                       │     │                   a21077a5e6 
│                       │     ├ Title           : zlib: zlib: Arbitrary code execution via buffer overflow in
│                       │     │                   untgz utility 
│                       │     ├ Description     : zlib versions up to and including 1.3.1.2 include a global
│                       │     │                   buffer overflow in the untgz utility located under
│                       │     │                   contrib/untgz. The vulnerability is limited to the standalone
│                       │     │                    demonstration utility and does not affect the core zlib
│                       │     │                   compression library. The flaw occurs when a user executes the
│                       │     │                    untgz command with an excessively long archive name supplied
│                       │     │                    via the command line, leading to an out-of-bounds write in a
│                       │     │                    fixed-size global buffer. 
│                       │     ├ Severity        : HIGH 
│                       │     ├ CweIDs           ─ [0]: CWE-787 
│                       │     ├ VendorSeverity   ╭ nvd   : 3 
│                       │     │                  ╰ redhat: 3 
│                       │     ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/
│                       │     │                  │        │           A:H 
│                       │     │                  │        ╰ V3Score : 7.8 
│                       │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 8.6 
│                       │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-22184 
│                       │     │                  ├ [1]: https://github.com/madler/zlib 
│                       │     │                  ├ [2]: https://github.com/madler/zlib/issues/1142 
│                       │     │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-22184 
│                       │     │                  ├ [4]: https://seclists.org/fulldisclosure/2026/Jan/3 
│                       │     │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2026-22184 
│                       │     │                  ├ [6]: https://www.vulncheck.com/advisories/zlib-untgz-global-
│                       │     │                  │      buffer-overflow-in-tgzfname 
│                       │     │                  ╰ [7]: https://zlib.net/ 
│                       │     ├ PublishedDate   : 2026-01-07T21:16:01.563Z 
│                       │     ╰ LastModifiedDate: 2026-03-18T16:26:31.14Z 
│                       ╰ [5] ╭ VulnerabilityID : CVE-2026-27171 
│                             ├ PkgID           : zlib@1.3.1-r2 
│                             ├ PkgName         : zlib 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/zlib@1.3.1-r2?arch=x86_64&distro=3.24.0
│                             │                  │       _alpha20260127 
│                             │                  ╰ UID : c6f558cca1be2488 
│                             ├ InstalledVersion: 1.3.1-r2 
│                             ├ FixedVersion    : 1.3.2-r0 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:4247bce4e6b0154252c90c5d6957b042408d9355ed35e
│                             │                  │         d19a18123bc1351925d 
│                             │                  ╰ DiffID: sha256:9ba501e4c5064718ae8f48934b6ef4f4f8382700276e9
│                             │                            9eb981123702b54ffa0 
│                             ├ SeveritySource  : nvd 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27171 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Fingerprint     : sha256:c993c74ea36dcad3b08328fa09cc60a08fd59600dc29a42e2a666d
│                             │                   95fdac9c7b 
│                             ├ Title           : zlib: zlib: Denial of Service via infinite loop in CRC32
│                             │                   combine functions 
│                             ├ Description     : zlib before 1.3.2 allows CPU consumption via crc32_combine64
│                             │                   and crc32_combine_gen64 because x2nmodp can do right shifts
│                             │                   within a loop that has no termination condition. 
│                             ├ Severity        : MEDIUM 
│                             ├ CweIDs           ─ [0]: CWE-1284 
│                             ├ VendorSeverity   ╭ amazon     : 1 
│                             │                  ├ azure      : 1 
│                             │                  ├ cbl-mariner: 1 
│                             │                  ├ julia      : 1 
│                             │                  ├ nvd        : 2 
│                             │                  ├ redhat     : 1 
│                             │                  ╰ ubuntu     : 1 
│                             ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:N/
│                             │                  │        │           A:L 
│                             │                  │        ╰ V3Score : 2.9 
│                             │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/
│                             │                  │        │           A:H 
│                             │                  │        ╰ V3Score : 5.5 
│                             │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/
│                             │                           │           A:L 
│                             │                           ╰ V3Score : 3.3 
│                             ├ References       ╭ [0] : https://7asecurity.com/blog/2026/02/zlib-7asecurity-au
│                             │                  │       dit 
│                             │                  ├ [1] : https://7asecurity.com/blog/2026/02/zlib-7asecurity-au
│                             │                  │       dit/ 
│                             │                  ├ [2] : https://7asecurity.com/reports/pentest-report-zlib-RC1
│                             │                  │       .1.pdf 
│                             │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2026-27171 
│                             │                  ├ [4] : https://github.com/advisories/GHSA-h858-mf2m-8jf4 
│                             │                  ├ [5] : https://github.com/madler/zlib/issues/904 
│                             │                  ├ [6] : https://github.com/madler/zlib/releases/tag/v1.3.2 
│                             │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2026-27171 
│                             │                  ├ [8] : https://ostif.org/zlib-audit-complete 
│                             │                  ├ [9] : https://ostif.org/zlib-audit-complete/ 
│                             │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2026-27171 
│                             ├ PublishedDate   : 2026-02-18T04:16:01.263Z 
│                             ╰ LastModifiedDate: 2026-03-25T21:27:04.603Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages 
```
