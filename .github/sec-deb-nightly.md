```yaml
╭ [0] ╭ Target  : openaf/oaf:deb-nightly (debian forky/sid) 
│     ├ Class   : os-pkgs 
│     ├ Type    : debian 
│     ╰ Packages 
├ [1] ╭ Target  : Java 
│     ├ Class   : lang-pkgs 
│     ├ Type    : jar 
│     ╰ Packages 
╰ [2] ╭ Target         : usr/bin/pebble 
      ├ Class          : lang-pkgs 
      ├ Type           : gobinary 
      ├ Packages        
      ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2026-97054 
                              ├ VendorIDs                    
                              │                  ────────────
                              │                  GO-2026-6859
                              ├ PkgID           : stdlib@v1.27.3 
                              ├ PkgName         : stdlib 
                              ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.3 
                              │                  ╰ UID : e374b4c8f0056732 
                              ├ InstalledVersion: v1.27.3 
                              ├ FixedVersion    : 1.26.11, 1.27.4 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:29ff67b6a3d515b4323eedd52f4073e1ae2168a00a2c3
                              │                  │         d2953af5604a69efe07 
                              │                  ╰ DiffID: sha256:ee774d118b94968a5808a48392b8f06623719709142b5
                              │                            505dd591d69ddfec9fb 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97054 
                              ├ DataSource       ╭ ID  : govulndb 
                              │                  ├ Name: The Go Vulnerability Database 
                              │                  ╰ URL : https://pkg.go.dev/vuln/ 
                              ├ Fingerprint     : sha256:4c0f9b04fae9bac8f799b4ad6b37c5ce6a6266a183310849a54450
                              │                   167a62f2ea 
                              ├ Title           : For HTTP/1 servers, when MaxBytesReader's limit is exceeded,
                              │                   "Connecti ... 
                              ├ Description     : For HTTP/1 servers, when MaxBytesReader's limit is exceeded,
                              │                   "Connection: close" header is automatically set without
                              │                   synchronization, which might race with another header being
                              │                   set explicitly in the server handler. As a result, an HTTP/1
                              │                   server that utilizes MaxBytesReader or MaxBytesHandler can
                              │                   crash due to runtime panic if its handler reads the request
                              │                   body concurrently with writing the response header. 
                              ├ Severity        : UNKNOWN 
                              ├ References                                                                
                              │                  ─────────────────────────────────────────────────────────
                              │                  https://go.dev/cl/862185                                 
                              │                  https://go.dev/issue/82563                               
                              │                  https://groups.google.com/g/golang-announce/c/iY8TY0wWgbM
                              │                  https://pkg.go.dev/vuln/GO-2026-6859                     
                              ├ PublishedDate   : 2026-11-11T05:19:58.943Z 
                              ╰ LastModifiedDate: 2026-11-12T22:09:39.233Z 
```
