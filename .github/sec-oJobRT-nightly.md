````yaml
╭ [0] ╭ Target: openaf/ojobrt:nightly (alpine 3.19.1) 
│     ├ Class : os-pkgs 
│     ╰ Type  : alpine 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2024-25710 
                        │     ├ PkgName         : org.apache.commons:commons-compress 
                        │     ├ PkgPath         : openaf/S3/commons-compress-1.24.0.jar 
                        │     ├ PkgIdentifier    ─ PURL: pkg:maven/org.apache.commons/commons-compress@1.24.0 
                        │     ├ InstalledVersion: 1.24.0 
                        │     ├ FixedVersion    : 1.26.0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:cc08e10fab97e446ba90dcae20d7b964589b0e28
                        │     │                  │         a383f435e6f6bf5f15fef541 
                        │     │                  ╰ DiffID: sha256:74bdae1b6e96e931301dad962da19e591887e3fe
                        │     │                            9cd050d8bf9eb0310a001a5f 
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
                        ├ [1] ╭ VulnerabilityID : CVE-2024-26308 
                        │     ├ PkgName         : org.apache.commons:commons-compress 
                        │     ├ PkgPath         : openaf/S3/commons-compress-1.24.0.jar 
                        │     ├ PkgIdentifier    ─ PURL: pkg:maven/org.apache.commons/commons-compress@1.24.0 
                        │     ├ InstalledVersion: 1.24.0 
                        │     ├ FixedVersion    : 1.26.0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:cc08e10fab97e446ba90dcae20d7b964589b0e28
                        │     │                  │         a383f435e6f6bf5f15fef541 
                        │     │                  ╰ DiffID: sha256:74bdae1b6e96e931301dad962da19e591887e3fe
                        │     │                            9cd050d8bf9eb0310a001a5f 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26308 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areview
                        │     │                          ed+ecosystem%3Amaven 
                        │     ├ Title           : commons-compress: OutOfMemoryError unpacking broken
                        │     │                   Pack200 file 
                        │     ├ Description     : Allocation of Resources Without Limits or Throttling
                        │     │                   vulnerability in Apache Commons Compress.This issue affects
                        │     │                   Apache Commons Compress: from 1.21 before 1.26.
                        │     │                   
                        │     │                   Users are recommended to upgrade to version 1.26, which fixes
                        │     │                    the issue.
                        │     │                   
                        │     │                    
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs           ─ [0]: CWE-770 
                        │     ├ VendorSeverity   ╭ ghsa  : 3 
                        │     │                  ├ nvd   : 2 
                        │     │                  ╰ redhat: 2 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N
                        │     │                  │        │           /I:N/A:H 
                        │     │                  │        ╰ V3Score : 7.5 
                        │     │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N
                        │     │                  │        │           /I:N/A:H 
                        │     │                  │        ╰ V3Score : 5.5 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N
                        │     │                           │           /I:N/A:H 
                        │     │                           ╰ V3Score : 5.9 
                        │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/02/19/2 
                        │     │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2024-26308 
                        │     │                  ├ [2]: https://github.com/apache/commons-compress 
                        │     │                  ├ [3]: https://lists.apache.org/thread/ch5yo2d21p7vlqrhll
                        │     │                  │      9b17otbyq4npfg 
                        │     │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-26308 
                        │     │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2024-26308 
                        │     │                  ╰ [6]: https://www.openwall.com/lists/oss-security/2024/0
                        │     │                         2/19/2 
                        │     ├ PublishedDate   : 2024-02-19T09:15:38.277Z 
                        │     ╰ LastModifiedDate: 2024-02-22T15:21:36.213Z 
                        ├ [2] ╭ VulnerabilityID : CVE-2024-25710 
                        │     ├ PkgName         : org.apache.commons:commons-compress 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ─ PURL: pkg:maven/org.apache.commons/commons-compress@1.25.0 
                        │     ├ InstalledVersion: 1.25.0 
                        │     ├ FixedVersion    : 1.26.0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:1729ecdd85283d74320556eb48eb0b05e131c18e
                        │     │                  │         5a8af3acc4f090f9435e3eb0 
                        │     │                  ╰ DiffID: sha256:a6f6568c03845781f0e283500e303e32332d917f
                        │     │                            20e29941310ba5b93a8cdea6 
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
                        ╰ [3] ╭ VulnerabilityID : CVE-2024-26308 
                              ├ PkgName         : org.apache.commons:commons-compress 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ PkgIdentifier    ─ PURL: pkg:maven/org.apache.commons/commons-compress@1.25.0 
                              ├ InstalledVersion: 1.25.0 
                              ├ FixedVersion    : 1.26.0 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:1729ecdd85283d74320556eb48eb0b05e131c18e
                              │                  │         5a8af3acc4f090f9435e3eb0 
                              │                  ╰ DiffID: sha256:a6f6568c03845781f0e283500e303e32332d917f
                              │                            20e29941310ba5b93a8cdea6 
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
