````yaml
─ [0] ╭ Target         : openaf/oaf:8-ubi (alpine 3.19.0) 
      ├ Class          : os-pkgs 
      ├ Type           : alpine 
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2024-0727 
                        │     ├ PkgID           : libcrypto3@3.1.4-r4 
                        │     ├ PkgName         : libcrypto3 
                        │     ├ InstalledVersion: 3.1.4-r4 
                        │     ├ FixedVersion    : 3.1.4-r5 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:7f65fb84733f6c174c62b569bb8f686b9a466570
                        │     │                  │         60fcac2144b36a19cd97d92f 
                        │     │                  ╰ DiffID: sha256:b7738828183f6af302b91a3e8cd49a0df0f10f72
                        │     │                            def3ef98f68580560dbc1bbd 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-0727 
                        │     ├ DataSource       ╭ ID  : alpine 
                        │     │                  ├ Name: Alpine Secdb 
                        │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
                        │     ├ Title           : openssl: denial of service via null dereference 
                        │     ├ Description     : A flaw was found in OpenSSL. The optional ContentInfo
                        │     │                   fields can be set to null, even if the "type" is a valid
                        │     │                   value, which can lead to a null dereference error that may
                        │     │                   cause a denial of service. 
                        │     ├ Severity        : LOW 
                        │     ├ VendorSeverity   ╭ redhat: 1 
                        │     │                  ╰ ubuntu: 1 
                        │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N
                        │     │                           │           /I:N/A:L 
                        │     │                           ╰ V3Score : 3.3 
                        │     ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-0727 
                        │                        ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
                        │                        │      -2024-0727 
                        │                        ├ [2]: https://github.com/openssl/openssl/pull/23362 
                        │                        ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2024-0727 
                        │                        ├ [4]: https://www.cve.org/CVERecord?id=CVE-2024-0727 
                        │                        ╰ [5]: https://www.openssl.org/news/secadv/20240125.txt 
                        ├ [1] ╭ VulnerabilityID : CVE-2024-0727 
                        │     ├ PkgID           : libssl3@3.1.4-r4 
                        │     ├ PkgName         : libssl3 
                        │     ├ InstalledVersion: 3.1.4-r4 
                        │     ├ FixedVersion    : 3.1.4-r5 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:7f65fb84733f6c174c62b569bb8f686b9a466570
                        │     │                  │         60fcac2144b36a19cd97d92f 
                        │     │                  ╰ DiffID: sha256:b7738828183f6af302b91a3e8cd49a0df0f10f72
                        │     │                            def3ef98f68580560dbc1bbd 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-0727 
                        │     ├ DataSource       ╭ ID  : alpine 
                        │     │                  ├ Name: Alpine Secdb 
                        │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
                        │     ├ Title           : openssl: denial of service via null dereference 
                        │     ├ Description     : A flaw was found in OpenSSL. The optional ContentInfo
                        │     │                   fields can be set to null, even if the "type" is a valid
                        │     │                   value, which can lead to a null dereference error that may
                        │     │                   cause a denial of service. 
                        │     ├ Severity        : LOW 
                        │     ├ VendorSeverity   ╭ redhat: 1 
                        │     │                  ╰ ubuntu: 1 
                        │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N
                        │     │                           │           /I:N/A:L 
                        │     │                           ╰ V3Score : 3.3 
                        │     ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-0727 
                        │                        ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
                        │                        │      -2024-0727 
                        │                        ├ [2]: https://github.com/openssl/openssl/pull/23362 
                        │                        ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2024-0727 
                        │                        ├ [4]: https://www.cve.org/CVERecord?id=CVE-2024-0727 
                        │                        ╰ [5]: https://www.openssl.org/news/secadv/20240125.txt 
                        ╰ [2] ╭ VulnerabilityID : CVE-2024-0727 
                              ├ PkgID           : openssl@3.1.4-r4 
                              ├ PkgName         : openssl 
                              ├ InstalledVersion: 3.1.4-r4 
                              ├ FixedVersion    : 3.1.4-r5 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:7f65fb84733f6c174c62b569bb8f686b9a466570
                              │                  │         60fcac2144b36a19cd97d92f 
                              │                  ╰ DiffID: sha256:b7738828183f6af302b91a3e8cd49a0df0f10f72
                              │                            def3ef98f68580560dbc1bbd 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-0727 
                              ├ DataSource       ╭ ID  : alpine 
                              │                  ├ Name: Alpine Secdb 
                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
                              ├ Title           : openssl: denial of service via null dereference 
                              ├ Description     : A flaw was found in OpenSSL. The optional ContentInfo
                              │                   fields can be set to null, even if the "type" is a valid
                              │                   value, which can lead to a null dereference error that may
                              │                   cause a denial of service. 
                              ├ Severity        : LOW 
                              ├ VendorSeverity   ╭ redhat: 1 
                              │                  ╰ ubuntu: 1 
                              ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N
                              │                           │           /I:N/A:L 
                              │                           ╰ V3Score : 3.3 
                              ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-0727 
                                                 ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
                                                 │      -2024-0727 
                                                 ├ [2]: https://github.com/openssl/openssl/pull/23362 
                                                 ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2024-0727 
                                                 ├ [4]: https://www.cve.org/CVERecord?id=CVE-2024-0727 
                                                 ╰ [5]: https://www.openssl.org/news/secadv/20240125.txt 
````
