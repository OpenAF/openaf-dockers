```yaml
╭ [0] ╭ Target         : openaf/ojobrt:latest (alpine 3.24.2) 
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
│                             ├ Layer            ╭ Digest: sha256:e85b91e5ffae82a624a263daf6c87c4388dff94da3b92
│                             │                  │         987c1b84e30aad1d203 
│                             │                  ╰ DiffID: sha256:380ec2a6785f9c0bcc78850f973b9ed28d5cafec3255e
│                             │                            1f955ed3e7cc0cd087d 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-85091 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Fingerprint     : sha256:609f186d37bea4e75b21843e73e8eab27b54e7e6316e61260784c4
│                             │                   378e76eee7 
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
