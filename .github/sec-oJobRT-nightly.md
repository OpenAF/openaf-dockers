````yaml
╭ [0] ╭ Target: openaf/ojobrt:nightly (alpine 3.18.2) 
│     ├ Class : os-pkgs 
│     ╰ Type  : alpine 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2023-2976 
                              ├ PkgName         : com.google.guava:guava 
                              ├ PkgPath         : openaf/S3/minio-8.5.4-all.jar 
                              ├ InstalledVersion: 32.0.0-jre 
                              ├ FixedVersion    : 32.0.1-android 
                              ├ Layer            ╭ Digest: sha256:750efa978f9ec6f51f84650cde61f9b394cd7938
                              │                  │         bcf9f38464741ca29a47dd3f 
                              │                  ╰ DiffID: sha256:4ef884542b51d715d7d9128e7fe8d12b6b799fd8
                              │                            7e344f6fed1f552cd3c487e5 
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
