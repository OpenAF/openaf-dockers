````yaml
╭ [0] ╭ Target         : openaf/ojobrt:latest (alpine 3.21.2) 
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
│                       │     ├ Layer            ╭ Digest: sha256:e1b4dd4fa06a3e0625d025e2c05fe60f2275f9a8d5492
│                       │     │                  │         7f9f06c26c76cec3135 
│                       │     │                  ╰ DiffID: sha256:ea38678eb747a96dd074e5e7f3d1e2cb4bcfc03a3ca4b
│                       │     │                            89609eca1dbb5bf8c8e 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ╰ Severity        : UNKNOWN 
│                       ╰ [1] ╭ VulnerabilityID : CVE-2025-26519 
│                             ├ PkgID           : musl-utils@1.2.5-r8 
│                             ├ PkgName         : musl-utils 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/musl-utils@1.2.5-r8?arch=x86_64&distro=
│                             │                  │       3.21.2 
│                             │                  ╰ UID : f25fd050ed07b9ad 
│                             ├ InstalledVersion: 1.2.5-r8 
│                             ├ FixedVersion    : 1.2.5-r9 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:e1b4dd4fa06a3e0625d025e2c05fe60f2275f9a8d5492
│                             │                  │         7f9f06c26c76cec3135 
│                             │                  ╰ DiffID: sha256:ea38678eb747a96dd074e5e7f3d1e2cb4bcfc03a3ca4b
│                             │                            89609eca1dbb5bf8c8e 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ╰ Severity        : UNKNOWN 
╰ [1] ╭ Target: Java 
      ├ Class : lang-pkgs 
      ╰ Type  : jar 
````
