````yaml
╭ [0] ╭ Target         : openaf/oaf:8-latest (alpine 3.19.1) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2023-5388 
│                             ├ PkgID           : nss@3.97-r0 
│                             ├ PkgName         : nss 
│                             ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/nss@3.97-r0?arch=x86_64&distro=3.19.1 
│                             ├ InstalledVersion: 3.97-r0 
│                             ├ FixedVersion    : 3.98-r0 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:c2bb7ac78b181c4b9b803a1ba69d054dd5a3ec28
│                             │                  │         80fcf08acd5ffa9bb0e24c55 
│                             │                  ╰ DiffID: sha256:b6685a6f4e5fc9c5ffee9d63b5f650ae32dc67bb
│                             │                            fd5e5742bc9f03d67745e59e 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-5388 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Title           : nss: timing attack against RSA decryption 
│                             ├ Description     : It was discovered that the numerical library used in NSS
│                             │                    for RSA cryptography leaks information whether high order
│                             │                   bits of the RSA decryption result are zero. This information
│                             │                   can be used to mount a Bleichenbacher or Manger like attack
│                             │                   against all RSA decryption operations. As the leak happens
│                             │                   before any padding operations, it affects all padding modes:
│                             │                   PKCS#1 v1.5, OAEP, and RSASVP. Both API level calls and TLS
│                             │                   server operation are affected. 
│                             ├ Severity        : MEDIUM 
│                             ├ VendorSeverity   ╭ alma       : 2 
│                             │                  ├ amazon     : 2 
│                             │                  ├ oracle-oval: 2 
│                             │                  ├ redhat     : 2 
│                             │                  ├ rocky      : 2 
│                             │                  ╰ ubuntu     : 2 
│                             ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H
│                             │                           │           /I:N/A:N 
│                             │                           ╰ V3Score : 6.5 
│                             ╰ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0105 
│                                                ├ [1] : https://access.redhat.com/security/cve/CVE-2023-5388 
│                                                ├ [2] : https://bugzilla.redhat.com/2243644 
│                                                ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2243644 
│                                                ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
│                                                │       E-2023-5388 
│                                                ├ [5] : https://errata.almalinux.org/8/ALSA-2024-0105.html 
│                                                ├ [6] : https://errata.rockylinux.org/RLSA-2024:0105 
│                                                ├ [7] : https://linux.oracle.com/cve/CVE-2023-5388.html 
│                                                ├ [8] : https://linux.oracle.com/errata/ELSA-2024-0108.html 
│                                                ├ [9] : https://nvd.nist.gov/vuln/detail/CVE-2023-5388 
│                                                ├ [10]: https://people.redhat.com/~hkario/marvin/ 
│                                                ╰ [11]: https://www.cve.org/CVERecord?id=CVE-2023-5388 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2024-25710 
                        │     ├ PkgName         : org.apache.commons:commons-compress 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ─ PURL: pkg:maven/org.apache.commons/commons-compress@1.25.0 
                        │     ├ InstalledVersion: 1.25.0 
                        │     ├ FixedVersion    : 1.26.0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:c2bb7ac78b181c4b9b803a1ba69d054dd5a3ec28
                        │     │                  │         80fcf08acd5ffa9bb0e24c55 
                        │     │                  ╰ DiffID: sha256:b6685a6f4e5fc9c5ffee9d63b5f650ae32dc67bb
                        │     │                            fd5e5742bc9f03d67745e59e 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-25710 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areview
                        │     │                          ed+ecosystem%3Amaven 
                        │     ├ Title           : commons-compress: Denial of service caused by an
                        │     │                   infinite loop for a corrupted DUMP file 
                        │     ├ Description     : Loop with Unreachable Exit Condition ('Infinite Loop')
                        │     │                   vulnerability in Apache Commons Compress.This issue affects
                        │     │                   Apache Commons Compress: from 1.3 through 1.25.0.
                        │     │                   
                        │     │                   Users are recommended to upgrade to version 1.26.0 which
                        │     │                   fixes the issue.
                        │     │                   
                        │     │                    
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs           ─ [0]: CWE-835 
                        │     ├ VendorSeverity   ╭ ghsa  : 3 
                        │     │                  ├ nvd   : 2 
                        │     │                  ╰ redhat: 3 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:C/C:H
                        │     │                  │        │           /I:H/A:H 
                        │     │                  │        ╰ V3Score : 8.1 
                        │     │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N
                        │     │                  │        │           /I:N/A:H 
                        │     │                  │        ╰ V3Score : 5.5 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:C/C:H
                        │     │                           │           /I:H/A:H 
                        │     │                           ╰ V3Score : 8.1 
                        │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/02/19/1 
                        │     │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2024-25710 
                        │     │                  ├ [2]: https://github.com/apache/commons-compress 
                        │     │                  ├ [3]: https://lists.apache.org/thread/cz8qkcwphy4cx8gltn
                        │     │                  │      932ln51cbtq6kf 
                        │     │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-25710 
                        │     │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2024-25710 
                        │     ├ PublishedDate   : 2024-02-19T09:15:37.943Z 
                        │     ╰ LastModifiedDate: 2024-02-22T15:24:45.24Z 
                        ╰ [1] ╭ VulnerabilityID : CVE-2024-26308 
                              ├ PkgName         : org.apache.commons:commons-compress 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ PkgIdentifier    ─ PURL: pkg:maven/org.apache.commons/commons-compress@1.25.0 
                              ├ InstalledVersion: 1.25.0 
                              ├ FixedVersion    : 1.26.0 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:c2bb7ac78b181c4b9b803a1ba69d054dd5a3ec28
                              │                  │         80fcf08acd5ffa9bb0e24c55 
                              │                  ╰ DiffID: sha256:b6685a6f4e5fc9c5ffee9d63b5f650ae32dc67bb
                              │                            fd5e5742bc9f03d67745e59e 
                              ├ SeveritySource  : ghsa 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26308 
                              ├ DataSource       ╭ ID  : ghsa 
                              │                  ├ Name: GitHub Security Advisory Maven 
                              │                  ╰ URL : https://github.com/advisories?query=type%3Areview
                              │                          ed+ecosystem%3Amaven 
                              ├ Title           : commons-compress: OutOfMemoryError unpacking broken
                              │                   Pack200 file 
                              ├ Description     : Allocation of Resources Without Limits or Throttling
                              │                   vulnerability in Apache Commons Compress.This issue affects
                              │                   Apache Commons Compress: from 1.21 before 1.26.
                              │                   
                              │                   Users are recommended to upgrade to version 1.26, which fixes
                              │                    the issue.
                              │                   
                              │                    
                              ├ Severity        : HIGH 
                              ├ CweIDs           ─ [0]: CWE-770 
                              ├ VendorSeverity   ╭ ghsa  : 3 
                              │                  ├ nvd   : 2 
                              │                  ╰ redhat: 2 
                              ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N
                              │                  │        │           /I:N/A:H 
                              │                  │        ╰ V3Score : 7.5 
                              │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N
                              │                  │        │           /I:N/A:H 
                              │                  │        ╰ V3Score : 5.5 
                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N
                              │                           │           /I:N/A:H 
                              │                           ╰ V3Score : 5.9 
                              ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/02/19/2 
                              │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2024-26308 
                              │                  ├ [2]: https://github.com/apache/commons-compress 
                              │                  ├ [3]: https://lists.apache.org/thread/ch5yo2d21p7vlqrhll
                              │                  │      9b17otbyq4npfg 
                              │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-26308 
                              │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2024-26308 
                              │                  ╰ [6]: https://www.openwall.com/lists/oss-security/2024/0
                              │                         2/19/2 
                              ├ PublishedDate   : 2024-02-19T09:15:38.277Z 
                              ╰ LastModifiedDate: 2024-02-22T15:21:36.213Z 
````
