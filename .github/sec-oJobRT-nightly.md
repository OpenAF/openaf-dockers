```yaml
╭ [0] ╭ Target         : openaf/ojobrt:nightly (alpine 3.24.2) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2026-85091 
│                             ├ PkgID           : zlib@1.3.2-r0 
│                             ├ PkgName         : zlib 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/zlib@1.3.2-r0?arch=x86_64&distro=3.24.2 
│                             │                  ╰ UID : e37054a2982d6c16 
│                             ├ InstalledVersion: 1.3.2-r0 
│                             ├ FixedVersion    : 1.3.2-r1 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:2e6b2d3623bce1d3aa7ec1fbc1839e6fd7444a017854d
│                             │                  │         39ef3fcb78c6d98c598 
│                             │                  ╰ DiffID: sha256:d9f4f8e92ff2954e9e92ecd1d1044d60ebd69e50c6d2d
│                             │                            48a8c284890b17120d4 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-85091 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Fingerprint     : sha256:769b13749ac6feabe46214a0a40955ac21a884a1a8570b2496f185
│                             │                   b5c822da93 
│                             ├ Title           : zlib versions 1.3.1.2 through 1.3.2 contain a heap buffer
│                             │                   overflow vul ... 
│                             ├ Description     : zlib versions 1.3.1.2 through 1.3.2 contain a heap buffer
│                             │                   overflow vulnerability in the gz_vacate() function when
│                             │                   processing non-blocking gzwrite() operations with stale
│                             │                   external buffer pointers. Attackers can trigger the overflow
│                             │                   by calling gzprintf() or gzvprintf() after a write stall,
│                             │                   causing an unchecked memmove() to write beyond the internal
│                             │                   input buffer boundary. 
│                             ├ Severity        : MEDIUM 
│                             ├ CweIDs                  
│                             │                  ───────
│                             │                  CWE-787
│                             │                  
│                             ├ VendorSeverity   ─ ubuntu: 2 
│                             ├ References                                                                     
│                             │                  ──────────────────────────────────────────────────────────────
│                             │                  https://gist.github.com/thesmartshadow/e0b9481792afb7c31e86fee
│                             │                  1ff084490                                                     
│                             │                  https://github.com/madler/zlib                                
│                             │                                                                                
│                             │                  https://github.com/madler/zlib/blob/v1.3.2/gzwrite.c#L393     
│                             │                                                                                
│                             │                  https://www.cve.org/CVERecord?id=CVE-2026-85091               
│                             │                                                                                
│                             │                  https://www.vulncheck.com/advisories/zlib-1.3.1.2-through-1.3.
│                             │                  2-heap-buffer-overflow-via-gz-vacate                          
│                             │                  
│                             ├ PublishedDate   : 2026-09-03T13:06:20.573Z 
│                             ╰ LastModifiedDate: 2026-09-09T20:41:07.123Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages 
```
