````yaml
╭ [0] ╭ Target         : openaf/ojobrt:latest (alpine 3.20.3) 
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
│                       │     ├ Layer            ╭ Digest: sha256:7f1a743c3eff1a8fb23e0250c8d67501639585b0724f6
│                       │     │                  │         f87cd648aec418f9d81 
│                       │     │                  ╰ DiffID: sha256:35cfe830b7a1d7c58192780ef4b2970b8dd7c4dd95136
│                       │     │                            3097092522a7baf1631 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-11053 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : When asked to both use a `.netrc` file for credentials and to
│                       │     │                    follow H ... 
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
│                       │     ├ Severity        : UNKNOWN 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/12/11/1 
│                       │     │                  ├ [1]: https://curl.se/docs/CVE-2024-11053.html 
│                       │     │                  ├ [2]: https://curl.se/docs/CVE-2024-11053.json 
│                       │     │                  ╰ [3]: https://hackerone.com/reports/2829063 
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
│                             ├ Layer            ╭ Digest: sha256:7f1a743c3eff1a8fb23e0250c8d67501639585b0724f6
│                             │                  │         f87cd648aec418f9d81 
│                             │                  ╰ DiffID: sha256:35cfe830b7a1d7c58192780ef4b2970b8dd7c4dd95136
│                             │                            3097092522a7baf1631 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-11053 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Title           : When asked to both use a `.netrc` file for credentials and to
│                             │                    follow H ... 
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
│                             ├ Severity        : UNKNOWN 
│                             ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2024/12/11/1 
│                             │                  ├ [1]: https://curl.se/docs/CVE-2024-11053.html 
│                             │                  ├ [2]: https://curl.se/docs/CVE-2024-11053.json 
│                             │                  ╰ [3]: https://hackerone.com/reports/2829063 
│                             ├ PublishedDate   : 2024-12-11T08:15:05.307Z 
│                             ╰ LastModifiedDate: 2024-12-11T15:15:07.783Z 
╰ [1] ╭ Target: Java 
      ├ Class : lang-pkgs 
      ╰ Type  : jar 
````
