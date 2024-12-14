````yaml
╭ [0] ╭ Target         : openaf/oaf:latest (alpine 3.20.3) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2024-11053 
│                       │     ├ PkgID           : curl@8.11.0-r2 
│                       │     ├ PkgName         : curl 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/curl@8.11.0-r2?arch=x86_64&distro=3.20.3 
│                       │     │                  ╰ UID : dba6d150ebf87de 
│                       │     ├ InstalledVersion: 8.11.0-r2 
│                       │     ├ FixedVersion    : 8.11.1-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:f87acdaa3f26a49f244227c8828f06bead07ba1b59451
│                       │     │                  │         90d922558b6d0e13dae 
│                       │     │                  ╰ DiffID: sha256:5e9933d01871b5b972b45e1ed09b195839a11087ba2f8
│                       │     │                            8e75ba45260e01a6e59 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-11053 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : curl: curl netrc password leak 
│                       │     ├ Description     : When asked to both use a `.netrc` file for credentials and to
│                       │     │                    follow HTTP
│                       │     │                   redirects, curl could leak the password used for the first
│                       │     │                   host to the
│                       │     │                   followed-to host under certain circumstances.
│                       │     │                   
│                       │     │                   This flaw only manifests itself if the netrc file has an
│                       │     │                   entry that matches
│                       │     │                   the redirect target hostname but the entry either omits just
│                       │     │                   the password or
│                       │     │                   omits both login and password. 
│                       │     ├ Severity        : MEDIUM 
│                       │     ├ VendorSeverity   ─ redhat: 1 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/
│                       │     │                           │           A:N 
│                       │     │                           ╰ V3Score : 5.9 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/12/11/1 
│                       │     │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2024-11053 
│                       │     │                  ├ [2]: https://curl.se/docs/CVE-2024-11053.html 
│                       │     │                  ├ [3]: https://curl.se/docs/CVE-2024-11053.json 
│                       │     │                  ├ [4]: https://hackerone.com/reports/2829063 
│                       │     │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2024-11053 
│                       │     │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2024-11053 
│                       │     ├ PublishedDate   : 2024-12-11T08:15:05.307Z 
│                       │     ╰ LastModifiedDate: 2024-12-11T15:15:07.783Z 
│                       ╰ [1] ╭ VulnerabilityID : CVE-2024-11053 
│                             ├ PkgID           : libcurl@8.11.0-r2 
│                             ├ PkgName         : libcurl 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcurl@8.11.0-r2?arch=x86_64&distro=3.
│                             │                  │       20.3 
│                             │                  ╰ UID : 79232d4bad6f26e 
│                             ├ InstalledVersion: 8.11.0-r2 
│                             ├ FixedVersion    : 8.11.1-r0 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:f87acdaa3f26a49f244227c8828f06bead07ba1b59451
│                             │                  │         90d922558b6d0e13dae 
│                             │                  ╰ DiffID: sha256:5e9933d01871b5b972b45e1ed09b195839a11087ba2f8
│                             │                            8e75ba45260e01a6e59 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-11053 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Title           : curl: curl netrc password leak 
│                             ├ Description     : When asked to both use a `.netrc` file for credentials and to
│                             │                    follow HTTP
│                             │                   redirects, curl could leak the password used for the first
│                             │                   host to the
│                             │                   followed-to host under certain circumstances.
│                             │                   
│                             │                   This flaw only manifests itself if the netrc file has an
│                             │                   entry that matches
│                             │                   the redirect target hostname but the entry either omits just
│                             │                   the password or
│                             │                   omits both login and password. 
│                             ├ Severity        : MEDIUM 
│                             ├ VendorSeverity   ─ redhat: 1 
│                             ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/
│                             │                           │           A:N 
│                             │                           ╰ V3Score : 5.9 
│                             ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/12/11/1 
│                             │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2024-11053 
│                             │                  ├ [2]: https://curl.se/docs/CVE-2024-11053.html 
│                             │                  ├ [3]: https://curl.se/docs/CVE-2024-11053.json 
│                             │                  ├ [4]: https://hackerone.com/reports/2829063 
│                             │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2024-11053 
│                             │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2024-11053 
│                             ├ PublishedDate   : 2024-12-11T08:15:05.307Z 
│                             ╰ LastModifiedDate: 2024-12-11T15:15:07.783Z 
╰ [1] ╭ Target: Java 
      ├ Class : lang-pkgs 
      ╰ Type  : jar 
````
