```yaml
╭ [0] ╭ Target         : openaf/oaf:edge (alpine 3.24.2) 
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
│                             ├ Layer            ╭ Digest: sha256:2f4109d25c1ef289802d8161e8285bdd152b4f85cdf36
│                             │                  │         62b39af29eb303770fe 
│                             │                  ╰ DiffID: sha256:9382625169b6cbd96cf4869c282a2e77d99b741263fd5
│                             │                            b503fabf2e92a662278 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-85091 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Fingerprint     : sha256:19094c1f4c299c582a0687f8cdcabb7704323e30f13f12f4609aa9
│                             │                   b5368e8652 
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
│                             ├ PublishedDate   : 2026-09-03T13:06:20.573Z 
│                             ╰ LastModifiedDate: 2026-09-09T20:41:07.123Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages 
```
