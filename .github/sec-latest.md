````yaml
╭ [0] ╭ Target         : openaf/oaf:latest (alpine 3.21.2) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2025-26519 
│                       │     ├ PkgID           : musl@1.2.5-r8 
│                       │     ├ PkgName         : musl 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/musl@1.2.5-r8?arch=x86_64&distro=3.21.2 
│                       │     │                  ╰ UID : 936f1fd92822db90 
│                       │     ├ InstalledVersion: 1.2.5-r8 
│                       │     ├ FixedVersion    : 1.2.5-r9 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:4c29462c245646c85a8ec3b3348417bc60cdd5bbf5297
│                       │     │                  │         f8e1a486928d6269397 
│                       │     │                  ╰ DiffID: sha256:7a96a656c8398a9e0d4890b0e5a9c37934d70fc2d7b0a
│                       │     │                            04e0edf4bf252e7caef 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-26519 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : musl libc 0.9.13 through 1.2.5 before 1.2.6 has an
│                       │     │                   out-of-bounds write ... 
│                       │     ├ Description     : musl libc 0.9.13 through 1.2.5 before 1.2.6 has an
│                       │     │                   out-of-bounds write vulnerability when an attacker can
│                       │     │                   trigger iconv conversion of untrusted EUC-KR text to UTF-8. 
│                       │     ├ Severity        : UNKNOWN 
│                       │     ├ CweIDs           ─ [0]: CWE-787 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2025/02/13/2 
│                       │     │                  ├ [1]: http://www.openwall.com/lists/oss-security/2025/02/13/3 
│                       │     │                  ├ [2]: http://www.openwall.com/lists/oss-security/2025/02/13/4 
│                       │     │                  ├ [3]: http://www.openwall.com/lists/oss-security/2025/02/13/5 
│                       │     │                  ├ [4]: http://www.openwall.com/lists/oss-security/2025/02/14/5 
│                       │     │                  ├ [5]: http://www.openwall.com/lists/oss-security/2025/02/14/6 
│                       │     │                  ├ [6]: https://git.musl-libc.org/cgit/musl/commit/?id=c47ad25e
│                       │     │                  │      a3b484e10326f933e927c0bc8cded3da 
│                       │     │                  ├ [7]: https://git.musl-libc.org/cgit/musl/commit/?id=e5adcd97
│                       │     │                  │      b5196e29991b524237381a0202a60659 
│                       │     │                  ╰ [8]: https://www.openwall.com/lists/oss-security/2025/02/13/2 
│                       │     ├ PublishedDate   : 2025-02-14T04:15:09.05Z 
│                       │     ╰ LastModifiedDate: 2025-02-14T17:15:23.09Z 
│                       ╰ [1] ╭ VulnerabilityID : CVE-2025-26519 
│                             ├ PkgID           : musl-utils@1.2.5-r8 
│                             ├ PkgName         : musl-utils 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/musl-utils@1.2.5-r8?arch=x86_64&distro=
│                             │                  │       3.21.2 
│                             │                  ╰ UID : f25fd050ed07b9ad 
│                             ├ InstalledVersion: 1.2.5-r8 
│                             ├ FixedVersion    : 1.2.5-r9 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:4c29462c245646c85a8ec3b3348417bc60cdd5bbf5297
│                             │                  │         f8e1a486928d6269397 
│                             │                  ╰ DiffID: sha256:7a96a656c8398a9e0d4890b0e5a9c37934d70fc2d7b0a
│                             │                            04e0edf4bf252e7caef 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-26519 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Title           : musl libc 0.9.13 through 1.2.5 before 1.2.6 has an
│                             │                   out-of-bounds write ... 
│                             ├ Description     : musl libc 0.9.13 through 1.2.5 before 1.2.6 has an
│                             │                   out-of-bounds write vulnerability when an attacker can
│                             │                   trigger iconv conversion of untrusted EUC-KR text to UTF-8. 
│                             ├ Severity        : UNKNOWN 
│                             ├ CweIDs           ─ [0]: CWE-787 
│                             ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2025/02/13/2 
│                             │                  ├ [1]: http://www.openwall.com/lists/oss-security/2025/02/13/3 
│                             │                  ├ [2]: http://www.openwall.com/lists/oss-security/2025/02/13/4 
│                             │                  ├ [3]: http://www.openwall.com/lists/oss-security/2025/02/13/5 
│                             │                  ├ [4]: http://www.openwall.com/lists/oss-security/2025/02/14/5 
│                             │                  ├ [5]: http://www.openwall.com/lists/oss-security/2025/02/14/6 
│                             │                  ├ [6]: https://git.musl-libc.org/cgit/musl/commit/?id=c47ad25e
│                             │                  │      a3b484e10326f933e927c0bc8cded3da 
│                             │                  ├ [7]: https://git.musl-libc.org/cgit/musl/commit/?id=e5adcd97
│                             │                  │      b5196e29991b524237381a0202a60659 
│                             │                  ╰ [8]: https://www.openwall.com/lists/oss-security/2025/02/13/2 
│                             ├ PublishedDate   : 2025-02-14T04:15:09.05Z 
│                             ╰ LastModifiedDate: 2025-02-14T17:15:23.09Z 
╰ [1] ╭ Target: Java 
      ├ Class : lang-pkgs 
      ╰ Type  : jar 
````
