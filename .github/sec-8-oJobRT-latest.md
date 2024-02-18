````yaml
─ [0] ╭ Target         : openaf/ojobrt:8-latest (alpine 3.19.1) 
      ├ Class          : os-pkgs 
      ├ Type           : alpine 
      ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2023-5388 
                              ├ PkgID           : nss@3.97-r0 
                              ├ PkgName         : nss 
                              ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/nss@3.97-r0?arch=x86_64&distro=3.19.1 
                              ├ InstalledVersion: 3.97-r0 
                              ├ FixedVersion    : 3.98-r0 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:f916f46100a81f864bcfdf9398ef0f599fd1ad74
                              │                  │         0cd20b9b2ca912087cbe232d 
                              │                  ╰ DiffID: sha256:099ff1e50695f1c847dedb5338ebdf7d32f5f02a
                              │                            2724403c2d76c172e8813704 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-5388 
                              ├ DataSource       ╭ ID  : alpine 
                              │                  ├ Name: Alpine Secdb 
                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
                              ├ Title           : nss: timing attack against RSA decryption 
                              ├ Description     : It was discovered that the numerical library used in NSS
                              │                    for RSA cryptography leaks information whether high order
                              │                   bits of the RSA decryption result are zero. This information
                              │                   can be used to mount a Bleichenbacher or Manger like attack
                              │                   against all RSA decryption operations. As the leak happens
                              │                   before any padding operations, it affects all padding modes:
                              │                   PKCS#1 v1.5, OAEP, and RSASVP. Both API level calls and TLS
                              │                   server operation are affected. 
                              ├ Severity        : MEDIUM 
                              ├ VendorSeverity   ╭ alma       : 2 
                              │                  ├ amazon     : 2 
                              │                  ├ oracle-oval: 2 
                              │                  ├ redhat     : 2 
                              │                  ├ rocky      : 2 
                              │                  ╰ ubuntu     : 2 
                              ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H
                              │                           │           /I:N/A:N 
                              │                           ╰ V3Score : 6.5 
                              ╰ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0108 
                                                 ├ [1] : https://access.redhat.com/security/cve/CVE-2023-5388 
                                                 ├ [2] : https://bugzilla.redhat.com/2243644 
                                                 ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2243644 
                                                 ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                                                 │       E-2023-5388 
                                                 ├ [5] : https://errata.almalinux.org/9/ALSA-2024-0108.html 
                                                 ├ [6] : https://errata.rockylinux.org/RLSA-2024:0105 
                                                 ├ [7] : https://linux.oracle.com/cve/CVE-2023-5388.html 
                                                 ├ [8] : https://linux.oracle.com/errata/ELSA-2024-0108.html 
                                                 ├ [9] : https://nvd.nist.gov/vuln/detail/CVE-2023-5388 
                                                 ├ [10]: https://people.redhat.com/~hkario/marvin/ 
                                                 ╰ [11]: https://www.cve.org/CVERecord?id=CVE-2023-5388 
````
