````yaml
╭ [0] ╭ Target         : openaf/ojobrt:latest (alpine 3.18.2) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2023-2975 
│                       │     ├ PkgID           : libcrypto3@3.1.1-r1 
│                       │     ├ PkgName         : libcrypto3 
│                       │     ├ InstalledVersion: 3.1.1-r1 
│                       │     ├ FixedVersion    : 3.1.1-r2 
│                       │     ├ Layer            ╭ Digest: sha256:bf23025c8f3462c0fdfb016726540bc5b079196b
│                       │     │                  │         96da37a386e2e8900eda93d3 
│                       │     │                  ╰ DiffID: sha256:180263b367fde05414b5b1c1838508fee4c10e67
│                       │     │                            6d52f28955948bf7ee5bdbe9 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2975 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : Issue summary: The AES-SIV cipher implementation
│                       │     │                   contains a bug that c ... 
│                       │     ├ Description     : Issue summary: The AES-SIV cipher implementation
│                       │     │                   contains a bug that causes
│                       │     │                   it to ignore empty associated data entries which are
│                       │     │                   unauthenticated as
│                       │     │                   a consequence.
│                       │     │                   
│                       │     │                   Impact summary: Applications that use the AES-SIV algorithm
│                       │     │                   and want to
│                       │     │                   authenticate empty data entries as associated data can be
│                       │     │                   mislead by removing
│                       │     │                   adding or reordering such empty entries as these are ignored
│                       │     │                   by the OpenSSL
│                       │     │                   implementation. We are currently unaware of any such
│                       │     │                   applications.
│                       │     │                   
│                       │     │                   The AES-SIV algorithm allows for authentication of multiple
│                       │     │                   associated
│                       │     │                   data entries along with the encryption. To authenticate empty
│                       │     │                    data the
│                       │     │                   application has to call EVP_EncryptUpdate() (or
│                       │     │                   EVP_CipherUpdate()) with
│                       │     │                   NULL pointer as the output buffer and 0 as the input buffer
│                       │     │                   length.
│                       │     │                   The AES-SIV implementation in OpenSSL just returns success
│                       │     │                   for such a call
│                       │     │                   instead of performing the associated data authentication
│                       │     │                   operation.
│                       │     │                   The empty data thus will not be authenticated.
│                       │     │                   
│                       │     │                   As this issue does not affect non-empty associated data
│                       │     │                   authentication and
│                       │     │                   we expect it to be rare for an application to use empty
│                       │     │                   associated data
│                       │     │                   entries this is qualified as Low severity issue. 
│                       │     ├ Severity        : LOW 
│                       │     ├ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
│                       │     │                  │      -2023-2975 
│                       │     │                  ├ [1]: https://git.openssl.org/gitweb/?p=openssl.git;a=co
│                       │     │                  │      mmitdiff;h=00e2f5eea29994d19293ec4e8c8775ba73678598
│                       │     │                  │      [m 
│                       │     │                  ├ [2]: https://git.openssl.org/gitweb/?p=openssl.git;a=co
│                       │     │                  │      mmitdiff;h=6a83f0c958811f07e0d11dfc6b5a6a98edfd5bdc
│                       │     │                  │      [m 
│                       │     │                  ╰ [3]: https://www.openssl.org/news/secadv/20230714.txt 
│                       │     ├ PublishedDate   : 2023-07-14T12:15:00Z 
│                       │     ╰ LastModifiedDate: 2023-07-14T12:47:00Z 
│                       ├ [1] ╭ VulnerabilityID : CVE-2023-2975 
│                       │     ├ PkgID           : libssl3@3.1.1-r1 
│                       │     ├ PkgName         : libssl3 
│                       │     ├ InstalledVersion: 3.1.1-r1 
│                       │     ├ FixedVersion    : 3.1.1-r2 
│                       │     ├ Layer            ╭ Digest: sha256:bf23025c8f3462c0fdfb016726540bc5b079196b
│                       │     │                  │         96da37a386e2e8900eda93d3 
│                       │     │                  ╰ DiffID: sha256:180263b367fde05414b5b1c1838508fee4c10e67
│                       │     │                            6d52f28955948bf7ee5bdbe9 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2975 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : Issue summary: The AES-SIV cipher implementation
│                       │     │                   contains a bug that c ... 
│                       │     ├ Description     : Issue summary: The AES-SIV cipher implementation
│                       │     │                   contains a bug that causes
│                       │     │                   it to ignore empty associated data entries which are
│                       │     │                   unauthenticated as
│                       │     │                   a consequence.
│                       │     │                   
│                       │     │                   Impact summary: Applications that use the AES-SIV algorithm
│                       │     │                   and want to
│                       │     │                   authenticate empty data entries as associated data can be
│                       │     │                   mislead by removing
│                       │     │                   adding or reordering such empty entries as these are ignored
│                       │     │                   by the OpenSSL
│                       │     │                   implementation. We are currently unaware of any such
│                       │     │                   applications.
│                       │     │                   
│                       │     │                   The AES-SIV algorithm allows for authentication of multiple
│                       │     │                   associated
│                       │     │                   data entries along with the encryption. To authenticate empty
│                       │     │                    data the
│                       │     │                   application has to call EVP_EncryptUpdate() (or
│                       │     │                   EVP_CipherUpdate()) with
│                       │     │                   NULL pointer as the output buffer and 0 as the input buffer
│                       │     │                   length.
│                       │     │                   The AES-SIV implementation in OpenSSL just returns success
│                       │     │                   for such a call
│                       │     │                   instead of performing the associated data authentication
│                       │     │                   operation.
│                       │     │                   The empty data thus will not be authenticated.
│                       │     │                   
│                       │     │                   As this issue does not affect non-empty associated data
│                       │     │                   authentication and
│                       │     │                   we expect it to be rare for an application to use empty
│                       │     │                   associated data
│                       │     │                   entries this is qualified as Low severity issue. 
│                       │     ├ Severity        : LOW 
│                       │     ├ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
│                       │     │                  │      -2023-2975 
│                       │     │                  ├ [1]: https://git.openssl.org/gitweb/?p=openssl.git;a=co
│                       │     │                  │      mmitdiff;h=00e2f5eea29994d19293ec4e8c8775ba73678598
│                       │     │                  │      [m 
│                       │     │                  ├ [2]: https://git.openssl.org/gitweb/?p=openssl.git;a=co
│                       │     │                  │      mmitdiff;h=6a83f0c958811f07e0d11dfc6b5a6a98edfd5bdc
│                       │     │                  │      [m 
│                       │     │                  ╰ [3]: https://www.openssl.org/news/secadv/20230714.txt 
│                       │     ├ PublishedDate   : 2023-07-14T12:15:00Z 
│                       │     ╰ LastModifiedDate: 2023-07-14T12:47:00Z 
│                       ╰ [2] ╭ VulnerabilityID : CVE-2023-2975 
│                             ├ PkgID           : openssl@3.1.1-r1 
│                             ├ PkgName         : openssl 
│                             ├ InstalledVersion: 3.1.1-r1 
│                             ├ FixedVersion    : 3.1.1-r2 
│                             ├ Layer            ╭ Digest: sha256:bf23025c8f3462c0fdfb016726540bc5b079196b
│                             │                  │         96da37a386e2e8900eda93d3 
│                             │                  ╰ DiffID: sha256:180263b367fde05414b5b1c1838508fee4c10e67
│                             │                            6d52f28955948bf7ee5bdbe9 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2975 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Title           : Issue summary: The AES-SIV cipher implementation
│                             │                   contains a bug that c ... 
│                             ├ Description     : Issue summary: The AES-SIV cipher implementation
│                             │                   contains a bug that causes
│                             │                   it to ignore empty associated data entries which are
│                             │                   unauthenticated as
│                             │                   a consequence.
│                             │                   
│                             │                   Impact summary: Applications that use the AES-SIV algorithm
│                             │                   and want to
│                             │                   authenticate empty data entries as associated data can be
│                             │                   mislead by removing
│                             │                   adding or reordering such empty entries as these are ignored
│                             │                   by the OpenSSL
│                             │                   implementation. We are currently unaware of any such
│                             │                   applications.
│                             │                   
│                             │                   The AES-SIV algorithm allows for authentication of multiple
│                             │                   associated
│                             │                   data entries along with the encryption. To authenticate empty
│                             │                    data the
│                             │                   application has to call EVP_EncryptUpdate() (or
│                             │                   EVP_CipherUpdate()) with
│                             │                   NULL pointer as the output buffer and 0 as the input buffer
│                             │                   length.
│                             │                   The AES-SIV implementation in OpenSSL just returns success
│                             │                   for such a call
│                             │                   instead of performing the associated data authentication
│                             │                   operation.
│                             │                   The empty data thus will not be authenticated.
│                             │                   
│                             │                   As this issue does not affect non-empty associated data
│                             │                   authentication and
│                             │                   we expect it to be rare for an application to use empty
│                             │                   associated data
│                             │                   entries this is qualified as Low severity issue. 
│                             ├ Severity        : LOW 
│                             ├ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
│                             │                  │      -2023-2975 
│                             │                  ├ [1]: https://git.openssl.org/gitweb/?p=openssl.git;a=co
│                             │                  │      mmitdiff;h=00e2f5eea29994d19293ec4e8c8775ba73678598
│                             │                  │      [m 
│                             │                  ├ [2]: https://git.openssl.org/gitweb/?p=openssl.git;a=co
│                             │                  │      mmitdiff;h=6a83f0c958811f07e0d11dfc6b5a6a98edfd5bdc
│                             │                  │      [m 
│                             │                  ╰ [3]: https://www.openssl.org/news/secadv/20230714.txt 
│                             ├ PublishedDate   : 2023-07-14T12:15:00Z 
│                             ╰ LastModifiedDate: 2023-07-14T12:47:00Z 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2023-2976 
                              ├ PkgName         : com.google.guava:guava 
                              ├ PkgPath         : openaf/S3/minio-8.5.4-all.jar 
                              ├ InstalledVersion: 32.0.0-jre 
                              ├ FixedVersion    : 32.0.1-android 
                              ├ Layer            ╭ Digest: sha256:2400cad7dc4658c3ee4dacb314d47956b3194cc2
                              │                  │         11efd2624e7ec2b5222f6783 
                              │                  ╰ DiffID: sha256:dd6c4bd4131a82e2eaa047e6dd28540d70b3460c
                              │                            4ec1f02b3cb3249851783478 
                              ├ SeveritySource  : nvd 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2976 
                              ├ DataSource       ╭ ID  : glad 
                              │                  ├ Name: GitLab Advisory Database Community 
                              │                  ╰ URL : https://gitlab.com/gitlab-org/advisories-community 
                              ├ Title           : insecure temporary directory creation 
                              ├ Description     : Use of Java's default temporary directory for file
                              │                   creation in `FileBackedOutputStream` in Google Guava versions
                              │                    1.0 to 31.1 on Unix systems and Android Ice Cream Sandwich
                              │                   allows other users and apps on the machine with access to the
                              │                    default Java temporary directory to be able to access the
                              │                   files created by the class.
                              │                   
                              │                   Even though the security vulnerability is fixed in version
                              │                   32.0.0, we recommend using version 32.0.1 as version 32.0.0
                              │                   breaks some functionality under Windows.
                              │                   
                              │                    
                              ├ Severity        : HIGH 
                              ├ CweIDs           ─ [0]: CWE-552 
                              ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H
                              │                  │        │           /I:N/A:N 
                              │                  │        ╰ V3Score : 5.5 
                              │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H
                              │                  │        │           /I:H/A:N 
                              │                  │        ╰ V3Score : 7.1 
                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L
                              │                           │           /I:L/A:N 
                              │                           ╰ V3Score : 4.4 
                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-2976 
                              │                  ├ [1]: https://github.com/advisories/GHSA-7g45-4rm6-3mm3 
                              │                  ├ [2]: https://github.com/google/guava/commit/feb83a1c8fd
                              │                  │      2e7670b244d5afd23cba5aca43284 
                              │                  ├ [3]: https://github.com/google/guava/issues/2575 
                              │                  ├ [4]: https://github.com/google/guava/issues/6532 
                              │                  ├ [5]: https://github.com/google/guava/releases/tag/v32.0.0 
                              │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-2976 
                              │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2023-2976 
                              ├ PublishedDate   : 2023-06-14T18:15:00Z 
                              ╰ LastModifiedDate: 2023-06-29T18:22:00Z 
````
