````yaml
─ [0] ╭ Target         : openaf/ojobrt:nightly (alpine 3.18.5) 
      ├ Class          : os-pkgs 
      ├ Type           : alpine 
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2023-46218 
                        │     ├ PkgID           : curl@8.4.0-r0 
                        │     ├ PkgName         : curl 
                        │     ├ InstalledVersion: 8.4.0-r0 
                        │     ├ FixedVersion    : 8.5.0-r0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:f580fa1edf9e410a20ff85a1b90e0f2ba76abbc8
                        │     │                  │         b142fa9a372932c9465b3883 
                        │     │                  ╰ DiffID: sha256:afa01609e49a763affd33065e98405f5a337a89a
                        │     │                            dfec3392478900498870a498 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-46218 
                        │     ├ DataSource       ╭ ID  : alpine 
                        │     │                  ├ Name: Alpine Secdb 
                        │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
                        │     ├ Title           : curl: information disclosure by exploiting a mixed case flaw 
                        │     ├ Description     : This flaw allows a malicious HTTP server to set "super
                        │     │                   cookies" in curl that
                        │     │                   are then passed back to more origins than what is otherwise
                        │     │                   allowed or
                        │     │                   possible. This allows a site to set cookies that then would
                        │     │                   get sent to
                        │     │                   different and unrelated sites and domains.
                        │     │                   
                        │     │                   It could do this by exploiting a mixed case flaw in curl's
                        │     │                   function that
                        │     │                   verifies a given cookie domain against the Public Suffix List
                        │     │                    (PSL). For
                        │     │                   example a cookie could be set with `domain=co.UK` when the
                        │     │                   URL used a lower
                        │     │                   case hostname `curl.co.uk`, even though `co.uk` is listed as
                        │     │                   a PSL domain.
                        │     │                    
                        │     ├ Severity        : MEDIUM 
                        │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L
                        │     │                           │           /I:N/A:N 
                        │     │                           ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-46218 
                        │     │                  ├ [1]: https://curl.se/docs/CVE-2023-46218.html 
                        │     │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
                        │     │                  │      -2023-46218 
                        │     │                  ├ [3]: https://hackerone.com/reports/2212193 
                        │     │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-46218 
                        │     │                  ├ [5]: https://ubuntu.com/security/notices/USN-6535-1 
                        │     │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-46218 
                        │     ├ PublishedDate   : 2023-12-07T01:15:00Z 
                        │     ╰ LastModifiedDate: 2023-12-07T01:15:00Z 
                        ├ [1] ╭ VulnerabilityID : CVE-2023-46219 
                        │     ├ PkgID           : curl@8.4.0-r0 
                        │     ├ PkgName         : curl 
                        │     ├ InstalledVersion: 8.4.0-r0 
                        │     ├ FixedVersion    : 8.5.0-r0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:f580fa1edf9e410a20ff85a1b90e0f2ba76abbc8
                        │     │                  │         b142fa9a372932c9465b3883 
                        │     │                  ╰ DiffID: sha256:afa01609e49a763affd33065e98405f5a337a89a
                        │     │                            dfec3392478900498870a498 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-46219 
                        │     ├ DataSource       ╭ ID  : alpine 
                        │     │                  ├ Name: Alpine Secdb 
                        │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
                        │     ├ Title           : curl: excessively long file name may lead to unknown
                        │     │                   HSTS status 
                        │     ├ Description     : No description is available for this CVE. 
                        │     ├ Severity        : LOW 
                        │     ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-46219 
                        │                        ├ [1]: https://curl.se/docs/CVE-2023-46219.html 
                        │                        ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
                        │                        │      -2023-46219 
                        │                        ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-46219 
                        │                        ├ [4]: https://ubuntu.com/security/notices/USN-6535-1 
                        │                        ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-46219 
                        ├ [2] ╭ VulnerabilityID : CVE-2023-46218 
                        │     ├ PkgID           : libcurl@8.4.0-r0 
                        │     ├ PkgName         : libcurl 
                        │     ├ InstalledVersion: 8.4.0-r0 
                        │     ├ FixedVersion    : 8.5.0-r0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:f580fa1edf9e410a20ff85a1b90e0f2ba76abbc8
                        │     │                  │         b142fa9a372932c9465b3883 
                        │     │                  ╰ DiffID: sha256:afa01609e49a763affd33065e98405f5a337a89a
                        │     │                            dfec3392478900498870a498 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-46218 
                        │     ├ DataSource       ╭ ID  : alpine 
                        │     │                  ├ Name: Alpine Secdb 
                        │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
                        │     ├ Title           : curl: information disclosure by exploiting a mixed case flaw 
                        │     ├ Description     : This flaw allows a malicious HTTP server to set "super
                        │     │                   cookies" in curl that
                        │     │                   are then passed back to more origins than what is otherwise
                        │     │                   allowed or
                        │     │                   possible. This allows a site to set cookies that then would
                        │     │                   get sent to
                        │     │                   different and unrelated sites and domains.
                        │     │                   
                        │     │                   It could do this by exploiting a mixed case flaw in curl's
                        │     │                   function that
                        │     │                   verifies a given cookie domain against the Public Suffix List
                        │     │                    (PSL). For
                        │     │                   example a cookie could be set with `domain=co.UK` when the
                        │     │                   URL used a lower
                        │     │                   case hostname `curl.co.uk`, even though `co.uk` is listed as
                        │     │                   a PSL domain.
                        │     │                    
                        │     ├ Severity        : MEDIUM 
                        │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L
                        │     │                           │           /I:N/A:N 
                        │     │                           ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-46218 
                        │     │                  ├ [1]: https://curl.se/docs/CVE-2023-46218.html 
                        │     │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
                        │     │                  │      -2023-46218 
                        │     │                  ├ [3]: https://hackerone.com/reports/2212193 
                        │     │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-46218 
                        │     │                  ├ [5]: https://ubuntu.com/security/notices/USN-6535-1 
                        │     │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-46218 
                        │     ├ PublishedDate   : 2023-12-07T01:15:00Z 
                        │     ╰ LastModifiedDate: 2023-12-07T01:15:00Z 
                        ╰ [3] ╭ VulnerabilityID : CVE-2023-46219 
                              ├ PkgID           : libcurl@8.4.0-r0 
                              ├ PkgName         : libcurl 
                              ├ InstalledVersion: 8.4.0-r0 
                              ├ FixedVersion    : 8.5.0-r0 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:f580fa1edf9e410a20ff85a1b90e0f2ba76abbc8
                              │                  │         b142fa9a372932c9465b3883 
                              │                  ╰ DiffID: sha256:afa01609e49a763affd33065e98405f5a337a89a
                              │                            dfec3392478900498870a498 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-46219 
                              ├ DataSource       ╭ ID  : alpine 
                              │                  ├ Name: Alpine Secdb 
                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
                              ├ Title           : curl: excessively long file name may lead to unknown
                              │                   HSTS status 
                              ├ Description     : No description is available for this CVE. 
                              ├ Severity        : LOW 
                              ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-46219 
                                                 ├ [1]: https://curl.se/docs/CVE-2023-46219.html 
                                                 ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
                                                 │      -2023-46219 
                                                 ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-46219 
                                                 ├ [4]: https://ubuntu.com/security/notices/USN-6535-1 
                                                 ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-46219 
````
