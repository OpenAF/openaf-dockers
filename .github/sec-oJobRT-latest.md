````yaml
─ [0] ╭ Target         : openaf/ojobrt:latest (alpine 3.18.4) 
      ├ Class          : os-pkgs 
      ├ Type           : alpine 
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2023-5363 
                        │     ├ PkgID           : libcrypto3@3.1.3-r0 
                        │     ├ PkgName         : libcrypto3 
                        │     ├ InstalledVersion: 3.1.3-r0 
                        │     ├ FixedVersion    : 3.1.4-r0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:791cca6985cdf78b89e5b206f5a85cf663b79ff3
                        │     │                  │         f95c141dd49fb58406c23bc6 
                        │     │                  ╰ DiffID: sha256:2b08f2e3dfe5cfd156997c6b14306ec4f9ad230f
                        │     │                            3be7440f851e9b9e9b546f80 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-5363 
                        │     ├ DataSource       ╭ ID  : alpine 
                        │     │                  ├ Name: Alpine Secdb 
                        │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
                        │     ├ Title           : Issue summary: A bug has been identified in the
                        │     │                   processing of key and  ... 
                        │     ├ Description     : A bug has been identified in the processing of key and
                        │     │                   initialisation vector (IV) lengths. This can lead to
                        │     │                   potential truncation or overruns during the initialisation of
                        │     │                    some symmetric ciphers. 
                        │     ├ Severity        : MEDIUM 
                        │     ╰ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
                        │                        │      -2023-5363 
                        │                        ├ [1]: https://ubuntu.com/security/notices/USN-6450-1 
                        │                        ╰ [2]: https://www.openssl.org/news/secadv/20231024.txt 
                        ├ [1] ╭ VulnerabilityID : CVE-2023-5363 
                        │     ├ PkgID           : libssl3@3.1.3-r0 
                        │     ├ PkgName         : libssl3 
                        │     ├ InstalledVersion: 3.1.3-r0 
                        │     ├ FixedVersion    : 3.1.4-r0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:791cca6985cdf78b89e5b206f5a85cf663b79ff3
                        │     │                  │         f95c141dd49fb58406c23bc6 
                        │     │                  ╰ DiffID: sha256:2b08f2e3dfe5cfd156997c6b14306ec4f9ad230f
                        │     │                            3be7440f851e9b9e9b546f80 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-5363 
                        │     ├ DataSource       ╭ ID  : alpine 
                        │     │                  ├ Name: Alpine Secdb 
                        │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
                        │     ├ Title           : Issue summary: A bug has been identified in the
                        │     │                   processing of key and  ... 
                        │     ├ Description     : A bug has been identified in the processing of key and
                        │     │                   initialisation vector (IV) lengths. This can lead to
                        │     │                   potential truncation or overruns during the initialisation of
                        │     │                    some symmetric ciphers. 
                        │     ├ Severity        : MEDIUM 
                        │     ╰ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
                        │                        │      -2023-5363 
                        │                        ├ [1]: https://ubuntu.com/security/notices/USN-6450-1 
                        │                        ╰ [2]: https://www.openssl.org/news/secadv/20231024.txt 
                        ╰ [2] ╭ VulnerabilityID : CVE-2023-5363 
                              ├ PkgID           : openssl@3.1.3-r0 
                              ├ PkgName         : openssl 
                              ├ InstalledVersion: 3.1.3-r0 
                              ├ FixedVersion    : 3.1.4-r0 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:791cca6985cdf78b89e5b206f5a85cf663b79ff3
                              │                  │         f95c141dd49fb58406c23bc6 
                              │                  ╰ DiffID: sha256:2b08f2e3dfe5cfd156997c6b14306ec4f9ad230f
                              │                            3be7440f851e9b9e9b546f80 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-5363 
                              ├ DataSource       ╭ ID  : alpine 
                              │                  ├ Name: Alpine Secdb 
                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
                              ├ Title           : Issue summary: A bug has been identified in the
                              │                   processing of key and  ... 
                              ├ Description     : A bug has been identified in the processing of key and
                              │                   initialisation vector (IV) lengths. This can lead to
                              │                   potential truncation or overruns during the initialisation of
                              │                    some symmetric ciphers. 
                              ├ Severity        : MEDIUM 
                              ╰ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
                                                 │      -2023-5363 
                                                 ├ [1]: https://ubuntu.com/security/notices/USN-6450-1 
                                                 ╰ [2]: https://www.openssl.org/news/secadv/20231024.txt 
````
