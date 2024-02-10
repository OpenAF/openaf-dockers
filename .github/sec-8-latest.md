````yaml
─ [0] ╭ Target         : openaf/oaf:8-latest (alpine 3.19.1) 
      ├ Class          : os-pkgs 
      ├ Type           : alpine 
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2023-52425 
                        │     ├ PkgID           : libexpat@2.5.0-r2 
                        │     ├ PkgName         : libexpat 
                        │     ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/libexpat@2.5.0-r2?arch=x86_64&dist
                        │     │                          ro=3.19.1 
                        │     ├ InstalledVersion: 2.5.0-r2 
                        │     ├ FixedVersion    : 2.6.0-r0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:eb557ca81f844eb7817ca4a5e6ad44457f891f49
                        │     │                  │         ba0fda1fcfd12ccbc73c7924 
                        │     │                  ╰ DiffID: sha256:9572f497331bdd56ac7239e05957c582544c469b
                        │     │                            e57d6c6dbab5dda188acf71d 
                        │     ├ SeveritySource  : nvd 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-52425 
                        │     ├ DataSource       ╭ ID  : alpine 
                        │     │                  ├ Name: Alpine Secdb 
                        │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
                        │     ├ Title           : expat: parsing large tokens can trigger a denial of service 
                        │     ├ Description     : libexpat through 2.5.0 allows a denial of service
                        │     │                   (resource consumption) because many full reparsings are
                        │     │                   required in the case of a large token for which multiple
                        │     │                   buffer fills are needed. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs           ─ [0]: CWE-400 
                        │     ├ VendorSeverity   ╭ nvd   : 3 
                        │     │                  ╰ redhat: 2 
                        │     ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N
                        │     │                  │        │           /I:N/A:H 
                        │     │                  │        ╰ V3Score : 7.5 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N
                        │     │                           │           /I:N/A:L 
                        │     │                           ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-52425 
                        │     │                  ├ [1]: https://github.com/libexpat/libexpat/pull/789 
                        │     │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-52425 
                        │     │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2023-52425 
                        │     ├ PublishedDate   : 2024-02-04T20:15:46.063Z 
                        │     ╰ LastModifiedDate: 2024-02-09T02:03:16.3Z 
                        ╰ [1] ╭ VulnerabilityID : CVE-2023-52426 
                              ├ PkgID           : libexpat@2.5.0-r2 
                              ├ PkgName         : libexpat 
                              ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/libexpat@2.5.0-r2?arch=x86_64&dist
                              │                          ro=3.19.1 
                              ├ InstalledVersion: 2.5.0-r2 
                              ├ FixedVersion    : 2.6.0-r0 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:eb557ca81f844eb7817ca4a5e6ad44457f891f49
                              │                  │         ba0fda1fcfd12ccbc73c7924 
                              │                  ╰ DiffID: sha256:9572f497331bdd56ac7239e05957c582544c469b
                              │                            e57d6c6dbab5dda188acf71d 
                              ├ SeveritySource  : nvd 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-52426 
                              ├ DataSource       ╭ ID  : alpine 
                              │                  ├ Name: Alpine Secdb 
                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
                              ├ Title           : expat: recursive XML entity expansion vulnerability 
                              ├ Description     : libexpat through 2.5.0 allows recursive XML Entity
                              │                   Expansion if XML_DTD is undefined at compile time. 
                              ├ Severity        : MEDIUM 
                              ├ CweIDs           ─ [0]: CWE-776 
                              ├ VendorSeverity   ╭ nvd   : 2 
                              │                  ├ redhat: 2 
                              │                  ╰ ubuntu: 2 
                              ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N
                              │                  │        │           /I:N/A:H 
                              │                  │        ╰ V3Score : 5.5 
                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N
                              │                           │           /I:N/A:L 
                              │                           ╰ V3Score : 5.3 
                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-52426 
                              │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
                              │                  │      -2023-52426 
                              │                  ├ [2]: https://cwe.mitre.org/data/definitions/776.html 
                              │                  ├ [3]: https://github.com/libexpat/libexpat/commit/0f075e
                              │                  │      c8ecb5e43f8fdca5182f8cca4703da0404 
                              │                  ├ [4]: https://github.com/libexpat/libexpat/pull/777 
                              │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-52426 
                              │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-52426 
                              ├ PublishedDate   : 2024-02-04T20:15:46.12Z 
                              ╰ LastModifiedDate: 2024-02-09T02:02:39.8Z 
````
