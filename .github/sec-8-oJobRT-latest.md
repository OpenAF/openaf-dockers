````yaml
─ [0] ╭ Target         : openaf/ojobrt:8-latest (alpine 3.19.1) 
      ├ Class          : os-pkgs 
      ├ Type           : alpine 
      ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2024-25629 
                              ├ PkgID           : c-ares@1.24.0-r1 
                              ├ PkgName         : c-ares 
                              ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/c-ares@1.24.0-r1?arch=x86_64&distr
                              │                          o=3.19.1 
                              ├ InstalledVersion: 1.24.0-r1 
                              ├ FixedVersion    : 1.27.0-r0 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:71065b1d23d35596d2e4ead3e2e7be256da9cc4e
                              │                  │         281ca79d98dc4bd59f9a9fad 
                              │                  ╰ DiffID: sha256:ed89bfe5b77d92e9a8d467234f2b01700f98409a
                              │                            78c694ed9481d699aed4c152 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-25629 
                              ├ DataSource       ╭ ID  : alpine 
                              │                  ├ Name: Alpine Secdb 
                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
                              ├ Title           : c-ares: Out of bounds read in ares__read_line() 
                              ├ Description     : c-ares is a C library for asynchronous DNS requests.
                              │                   `ares__read_line()` is used to parse local configuration
                              │                   files such as `/etc/resolv.conf`, `/etc/nsswitch.conf`, the
                              │                   `HOSTALIASES` file, and if using a c-ares version prior to
                              │                   1.27.0, the `/etc/hosts` file. If any of these configuration
                              │                   files has an embedded `NULL` character as the first character
                              │                    in a new line, it can lead to attempting to read memory
                              │                   prior to the start of the given buffer which may result in a
                              │                   crash. This issue is fixed in c-ares 1.27.0. No known
                              │                   workarounds exist. 
                              ├ Severity        : MEDIUM 
                              ├ CweIDs           ─ [0]: CWE-127 
                              ├ VendorSeverity   ╭ amazon: 2 
                              │                  ├ photon: 2 
                              │                  ├ redhat: 1 
                              │                  ╰ ubuntu: 2 
                              ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:N
                              │                           │           /I:N/A:H 
                              │                           ╰ V3Score : 4.4 
                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-25629 
                              │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE
                              │                  │      -2024-25629 
                              │                  ├ [2]: https://github.com/c-ares/c-ares/commit/a804c04ddc
                              │                  │      8245fc8adf0e92368709639125e183 
                              │                  ├ [3]: https://github.com/c-ares/c-ares/security/advisori
                              │                  │      es/GHSA-mg26-v6qh-x48q 
                              │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-25629 
                              │                  ├ [5]: https://ubuntu.com/security/notices/USN-6676-1 
                              │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2024-25629 
                              ├ PublishedDate   : 2024-02-23T15:15:09.237Z 
                              ╰ LastModifiedDate: 2024-02-23T16:14:43.447Z 
````
