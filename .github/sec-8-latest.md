````yaml
─ [0] ╭ Target         : openaf/oaf:8-latest (alpine 3.19.1) 
      ├ Class          : os-pkgs 
      ├ Type           : alpine 
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2023-42366 
                        │     ├ PkgID           : busybox@1.36.1-r15 
                        │     ├ PkgName         : busybox 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/busybox@1.36.1-r15?arch=x86_64&dis
                        │     │                  │       tro=3.19.1 
                        │     │                  ╰ UID : a71bca140ff5726b 
                        │     ├ InstalledVersion: 1.36.1-r15 
                        │     ├ FixedVersion    : 1.36.1-r16 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:1a5c171498f0a7a1af3d9d425fb8b0fa5f86ef78
                        │     │                  │         d21beb9ee484c322159d7dd9 
                        │     │                  ╰ DiffID: sha256:a459a7ba198ccd018ca94a925f446cb738e00953
                        │     │                            e3497cef1939bb021ee94d7d 
                        │     ├ SeveritySource  : nvd 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-42366 
                        │     ├ DataSource       ╭ ID  : alpine 
                        │     │                  ├ Name: Alpine Secdb 
                        │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
                        │     ├ Title           : busybox: A heap-buffer-overflow 
                        │     ├ Description     : A heap-buffer-overflow was discovered in BusyBox
                        │     │                   v.1.36.1 in the next_token function at awk.c:1159. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-787 
                        │     ├ VendorSeverity   ╭ nvd   : 2 
                        │     │                  ├ redhat: 2 
                        │     │                  ╰ ubuntu: 2 
                        │     ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N
                        │     │                  │        │           /I:N/A:H 
                        │     │                  │        ╰ V3Score : 5.5 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H
                        │     │                           │           /I:N/A:H 
                        │     │                           ╰ V3Score : 7.1 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-42366 
                        │     │                  ├ [1]: https://bugs.busybox.net/show_bug.cgi?id=15874 
                        │     │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-42366 
                        │     │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2023-42366 
                        │     ├ PublishedDate   : 2023-11-27T23:15:07.42Z 
                        │     ╰ LastModifiedDate: 2023-11-30T05:08:23.197Z 
                        ├ [1] ╭ VulnerabilityID : CVE-2023-42366 
                        │     ├ PkgID           : busybox-binsh@1.36.1-r15 
                        │     ├ PkgName         : busybox-binsh 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/busybox-binsh@1.36.1-r15?arch=x86_
                        │     │                  │       64&distro=3.19.1 
                        │     │                  ╰ UID : 3c2acc699fbc7b01 
                        │     ├ InstalledVersion: 1.36.1-r15 
                        │     ├ FixedVersion    : 1.36.1-r16 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:1a5c171498f0a7a1af3d9d425fb8b0fa5f86ef78
                        │     │                  │         d21beb9ee484c322159d7dd9 
                        │     │                  ╰ DiffID: sha256:a459a7ba198ccd018ca94a925f446cb738e00953
                        │     │                            e3497cef1939bb021ee94d7d 
                        │     ├ SeveritySource  : nvd 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-42366 
                        │     ├ DataSource       ╭ ID  : alpine 
                        │     │                  ├ Name: Alpine Secdb 
                        │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
                        │     ├ Title           : busybox: A heap-buffer-overflow 
                        │     ├ Description     : A heap-buffer-overflow was discovered in BusyBox
                        │     │                   v.1.36.1 in the next_token function at awk.c:1159. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-787 
                        │     ├ VendorSeverity   ╭ nvd   : 2 
                        │     │                  ├ redhat: 2 
                        │     │                  ╰ ubuntu: 2 
                        │     ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N
                        │     │                  │        │           /I:N/A:H 
                        │     │                  │        ╰ V3Score : 5.5 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H
                        │     │                           │           /I:N/A:H 
                        │     │                           ╰ V3Score : 7.1 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-42366 
                        │     │                  ├ [1]: https://bugs.busybox.net/show_bug.cgi?id=15874 
                        │     │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-42366 
                        │     │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2023-42366 
                        │     ├ PublishedDate   : 2023-11-27T23:15:07.42Z 
                        │     ╰ LastModifiedDate: 2023-11-30T05:08:23.197Z 
                        ╰ [2] ╭ VulnerabilityID : CVE-2023-42366 
                              ├ PkgID           : ssl_client@1.36.1-r15 
                              ├ PkgName         : ssl_client 
                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/ssl_client@1.36.1-r15?arch=x86_64&
                              │                  │       distro=3.19.1 
                              │                  ╰ UID : 3a57d387f26109e5 
                              ├ InstalledVersion: 1.36.1-r15 
                              ├ FixedVersion    : 1.36.1-r16 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:1a5c171498f0a7a1af3d9d425fb8b0fa5f86ef78
                              │                  │         d21beb9ee484c322159d7dd9 
                              │                  ╰ DiffID: sha256:a459a7ba198ccd018ca94a925f446cb738e00953
                              │                            e3497cef1939bb021ee94d7d 
                              ├ SeveritySource  : nvd 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-42366 
                              ├ DataSource       ╭ ID  : alpine 
                              │                  ├ Name: Alpine Secdb 
                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
                              ├ Title           : busybox: A heap-buffer-overflow 
                              ├ Description     : A heap-buffer-overflow was discovered in BusyBox
                              │                   v.1.36.1 in the next_token function at awk.c:1159. 
                              ├ Severity        : MEDIUM 
                              ├ CweIDs           ─ [0]: CWE-787 
                              ├ VendorSeverity   ╭ nvd   : 2 
                              │                  ├ redhat: 2 
                              │                  ╰ ubuntu: 2 
                              ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N
                              │                  │        │           /I:N/A:H 
                              │                  │        ╰ V3Score : 5.5 
                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H
                              │                           │           /I:N/A:H 
                              │                           ╰ V3Score : 7.1 
                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-42366 
                              │                  ├ [1]: https://bugs.busybox.net/show_bug.cgi?id=15874 
                              │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-42366 
                              │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2023-42366 
                              ├ PublishedDate   : 2023-11-27T23:15:07.42Z 
                              ╰ LastModifiedDate: 2023-11-30T05:08:23.197Z 
````
