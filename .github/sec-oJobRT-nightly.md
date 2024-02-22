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
                        │     ├ Layer            ╭ Digest: sha256:8e463f1faeb83eda91ec041cedd70a2dcf19a8f3
                        │     │                  │         a0f860976b9ea6d6c2c8a949 
                        │     │                  ╰ DiffID: sha256:43cd1b86afcb6fdd262b4bee3391160680a89711
                        │     │                            7f1ef9c12db1d891ac938edd 
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
                        │     │                  ╰ redhat: 3 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:C/C:H
                        │     │                  │        │           /I:H/A:H 
                        │     │                  │        ╰ V3Score : 8.1 
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
                        │     ╰ LastModifiedDate: 2024-02-20T19:50:53.96Z 
                        ├ [1] ╭ VulnerabilityID : CVE-2024-26308 
                        │     ├ PkgName         : org.apache.commons:commons-compress 
                        │     ├ PkgPath         : openaf/S3/commons-compress-1.24.0.jar 
                        │     ├ PkgIdentifier    ─ PURL: pkg:maven/org.apache.commons/commons-compress@1.24.0 
                        │     ├ InstalledVersion: 1.24.0 
                        │     ├ FixedVersion    : 1.26.0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:8e463f1faeb83eda91ec041cedd70a2dcf19a8f3
                        │     │                  │         a0f860976b9ea6d6c2c8a949 
                        │     │                  ╰ DiffID: sha256:43cd1b86afcb6fdd262b4bee3391160680a89711
                        │     │                            7f1ef9c12db1d891ac938edd 
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
                        │     │                  ╰ redhat: 2 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N
                        │     │                  │        │           /I:N/A:H 
                        │     │                  │        ╰ V3Score : 7.5 
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
                        │     ╰ LastModifiedDate: 2024-02-20T19:50:53.96Z 
                        ├ [2] ╭ VulnerabilityID : CVE-2024-25710 
                        │     ├ PkgName         : org.apache.commons:commons-compress 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ─ PURL: pkg:maven/org.apache.commons/commons-compress@1.25.0 
                        │     ├ InstalledVersion: 1.25.0 
                        │     ├ FixedVersion    : 1.26.0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2d885f3f1ba5d4b3559e93fdf249beaefcfb9b02
                        │     │                  │         21103bdb3c1dfd10819bb729 
                        │     │                  ╰ DiffID: sha256:f1398ad909898780c64a1718c9e9887c2d03613c
                        │     │                            9cc2bb4359049559386aa33e 
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
                        │     │                  ╰ redhat: 3 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:C/C:H
                        │     │                  │        │           /I:H/A:H 
                        │     │                  │        ╰ V3Score : 8.1 
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
                        │     ╰ LastModifiedDate: 2024-02-20T19:50:53.96Z 
                        ╰ [3] ╭ VulnerabilityID : CVE-2024-26308 
                              ├ PkgName         : org.apache.commons:commons-compress 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ PkgIdentifier    ─ PURL: pkg:maven/org.apache.commons/commons-compress@1.25.0 
                              ├ InstalledVersion: 1.25.0 
                              ├ FixedVersion    : 1.26.0 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:2d885f3f1ba5d4b3559e93fdf249beaefcfb9b02
                              │                  │         21103bdb3c1dfd10819bb729 
                              │                  ╰ DiffID: sha256:f1398ad909898780c64a1718c9e9887c2d03613c
                              │                            9cc2bb4359049559386aa33e 
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
                              │                  ╰ redhat: 2 
                              ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N
                              │                  │        │           /I:N/A:H 
                              │                  │        ╰ V3Score : 7.5 
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
                              ╰ LastModifiedDate: 2024-02-20T19:50:53.96Z 
````
