```yaml
╭ [0] ╭ Target         : openaf/oaf:nightly (alpine 3.24.4) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2026-4738 
│                             ├ PkgID           : zlib@1.3.2-r1 
│                             ├ PkgName         : zlib 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/zlib@1.3.2-r1?arch=x86_64&distro=3.24.4 
│                             │                  ╰ UID : 926381dc853769fb 
│                             ├ InstalledVersion: 1.3.2-r1 
│                             ├ FixedVersion    : 1.4-r0 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:44b50618357470d407def1add288e7bff255634f0fa0b
│                             │                  │         8b82f665830fa991ffa 
│                             │                  ╰ DiffID: sha256:14c3566716adf8754d954085e3625f70d7de89fdd583f
│                             │                            88fee4f7c058dd74788 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4738 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Fingerprint     : sha256:e87ee8a8671086cbc0847dc63309e0bd9118a960f5fe058d8f7b57
│                             │                   b5da29d384 
│                             ├ Title           : Improper Restriction of Operations within the Bounds of a
│                             │                   Memory Buffe ... 
│                             ├ Description     : Improper Restriction of Operations within the Bounds of a
│                             │                   Memory Buffer vulnerability in OSGeo gdal
│                             │                   (frmts/zlib/contrib/infback9 modules). This vulnerability is
│                             │                   associated with program files inftree9.C‎.
│                             │                   
│                             │                   This issue affects gdal: before 3.11.0. 
│                             ├ Severity        : MEDIUM 
│                             ├ CweIDs                  
│                             │                  ───────
│                             │                  CWE-119
│                             ├ VendorSeverity   ╭ bitnami: 4 
│                             │                  ├ julia  : 4 
│                             │                  ╰ ubuntu : 2 
│                             ├ CVSS             ╭ bitnami ╭ V40Vector: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:P/VC:H/
│                             │                  │         │            VI:H/VA:H/SC:H/SI:H/SA:H/E:A/S:P/AU:Y/R
│                             │                  │         │            :U/V:C/RE:L/U:Amber 
│                             │                  │         ╰ V40Score : 9.4 
│                             │                  ╰ julia   ╭ V40Vector: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:P/VC:H/
│                             │                            │            VI:H/VA:H/SC:H/SI:H/SA:H/E:A/S:P/AU:Y/R
│                             │                            │            :U/V:C/RE:L/U:Amber 
│                             │                            ╰ V40Score : 9.4 
│                             ├ References                                                        
│                             │                  ─────────────────────────────────────────────────
│                             │                  https://github.com/OSGeo/gdal/pull/12244         
│                             │                  https://github.com/advisories/GHSA-hp6p-5qh5-w9fj
│                             │                  https://nvd.nist.gov/vuln/detail/CVE-2026-4738   
│                             │                  https://www.cve.org/CVERecord?id=CVE-2026-4738   
│                             ├ PublishedDate   : 2026-03-24T04:17:29Z 
│                             ╰ LastModifiedDate: 2026-06-17T10:57:09.03Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages 
```
