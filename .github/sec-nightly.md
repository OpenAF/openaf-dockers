````yaml
╭ [0] ╭ Target         : openaf/oaf:nightly (alpine 3.21.2) 
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
│                       │     ├ Layer            ╭ Digest: sha256:a199a5419b01e256684baeef17e0ca0a43e34b4e9d0dd
│                       │     │                  │         776b36c1f5af16249e3 
│                       │     │                  ╰ DiffID: sha256:a219b51eca5899fc49c33ae7583285fabdbd97cdb7672
│                       │     │                            ffa6a1a71df2527df2f 
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
│                             ├ Layer            ╭ Digest: sha256:a199a5419b01e256684baeef17e0ca0a43e34b4e9d0dd
│                             │                  │         776b36c1f5af16249e3 
│                             │                  ╰ DiffID: sha256:a219b51eca5899fc49c33ae7583285fabdbd97cdb7672
│                             │                            ffa6a1a71df2527df2f 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ╰ Severity        : UNKNOWN 
╰ [1] ╭ Target: Java 
      ├ Class : lang-pkgs 
      ╰ Type  : jar 
````
