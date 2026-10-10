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
│                             ├ Layer            ╭ Digest: sha256:35f2b07504c95baed243b2bf77c583073e7946b25c63a
│                             │                  │         dc674d4a686fd79c383 
│                             │                  ╰ DiffID: sha256:c613de1466a0dfb1e1a8eb95449760c0fc3c8a8b2459f
│                             │                            b2f691109c3e7171c32 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-85091 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Fingerprint     : sha256:88532b21c067c61d1e760f13558ce583451a566a84e00ccd5e2ea2
│                             │                   ba3e94f4da 
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
