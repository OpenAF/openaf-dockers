```yaml
╭ [0] ╭ Target  : openaf/ojobrt:edge (alpine 3.24.2) 
│     ├ Class   : os-pkgs 
│     ├ Type    : alpine 
│     ╰ Packages 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ├ Packages        
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2026-8763 
                        │     ├ VendorIDs                           
                        │     │                  ───────────────────
                        │     │                  GHSA-9pwp-9qqc-pr26
                        │     │                  
                        │     ├ PkgName         : org.bouncycastle:bcprov-jdk18on 
                        │     ├ PkgPath         : openaf/S3/bcprov-jdk18on-1.84.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/org.bouncycastle/bcprov-jdk18on@1.84 
                        │     │                  ╰ UID : aa9cc21dd2336977 
                        │     ├ InstalledVersion: 1.84 
                        │     ├ FixedVersion    : 1.85 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:edb5451f925c852a90c29538fc3120d92e151b8ea351c
                        │     │                  │         9a8dd63f941e3a8fe11 
                        │     │                  ╰ DiffID: sha256:d06ec56fba58e112e5ea7c25bd5688e649ffda420c9a4
                        │     │                            5fb305be0d8a4232eb4 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-8763 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:78831cb2e27933fa830198e6b2f3c397a33d750a21171b83ff6482
                        │     │                   2f5ad18c1e 
                        │     ├ Title           : org.bouncycastle/bcprov-jdk15on:
                        │     │                   org.bouncycastle/bcpkix-jdk15on: Bouncy Castle for Java: Name
                        │     │                    Constraints bypass via trailing dot in rfc822Name and URI 
                        │     ├ Description     : In Bouncy Castle for Java before 1.85, Name Constraints
                        │     │                   bypass via trailing dot in rfc822Name and URI. This issue
                        │     │                   also affects Bouncy Castle for Java LTS before 2.73.12, and
                        │     │                   Bouncy Castle for Java FIPS (BC-FJA) before bc-fips 1.0.2.7
                        │     │                   (1.0.X series), 2.0.2 (2.0.X series) and 2.1.3 (2.1.X
                        │     │                   series). 
                        │     ├ Severity        : CRITICAL 
                        │     ├ CweIDs                  
                        │     │                  ───────
                        │     │                  CWE-295
                        │     │                  
                        │     ├ VendorSeverity   ╭ amazon: 3 
                        │     │                  ├ ghsa  : 4 
                        │     │                  ├ nvd   : 4 
                        │     │                  ╰ redhat: 3 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector : CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H
                        │     │                  │        │            /A:N 
                        │     │                  │        ├ V40Vector: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/V
                        │     │                  │        │            I:H/VA:N/SC:N/SI:N/SA:N/U:Amber 
                        │     │                  │        ├ V3Score  : 9.1 
                        │     │                  │        ╰ V40Score : 9.3 
                        │     │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/
                        │     │                  │        │           A:N 
                        │     │                  │        ╰ V3Score : 9.1 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/
                        │     │                           │           A:N 
                        │     │                           ╰ V3Score : 7.4 
                        │     ├ References                                                                     
                        │     │                  ──────────────────────────────────────────────────────────────
                        │     │                  https://access.redhat.com/security/cve/CVE-2026-8763          
                        │     │                  https://github.com/bcgit/bc-java                              
                        │     │                  https://github.com/bcgit/bc-java/commit/2c28b253a44681fbbc5625
                        │     │                  61eab6ad383d2ae558                                            
                        │     │                  https://github.com/bcgit/bc-java/releases/tag/r1rv85v2        
                        │     │                                                                                
                        │     │                  https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9
                        │     │                  08763                                                         
                        │     │                  https://github.com/bcgit/bc-java/wiki/CVE-2026-8763           
                        │     │                                                                                
                        │     │                  https://nvd.nist.gov/vuln/detail/CVE-2026-8763                
                        │     │                                                                                
                        │     │                  https://www.cve.org/CVERecord?id=CVE-2026-8763                
                        │     │                                                                                
                        │     │                  
                        │     ├ PublishedDate   : 2026-08-03T01:16:45.807Z 
                        │     ╰ LastModifiedDate: 2026-09-02T14:28:48.94Z 
                        ╰ [1] ╭ VulnerabilityID : CVE-2026-13506 
                              ├ VendorIDs                           
                              │                  ───────────────────
                              │                  GHSA-qp49-qgx5-5m26
                              │                  
                              ├ PkgName         : org.bouncycastle:bcprov-jdk18on 
                              ├ PkgPath         : openaf/S3/bcprov-jdk18on-1.84.jar 
                              ├ PkgIdentifier    ╭ PURL: pkg:maven/org.bouncycastle/bcprov-jdk18on@1.84 
                              │                  ╰ UID : aa9cc21dd2336977 
                              ├ InstalledVersion: 1.84 
                              ├ FixedVersion    : 1.85 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:edb5451f925c852a90c29538fc3120d92e151b8ea351c
                              │                  │         9a8dd63f941e3a8fe11 
                              │                  ╰ DiffID: sha256:d06ec56fba58e112e5ea7c25bd5688e649ffda420c9a4
                              │                            5fb305be0d8a4232eb4 
                              ├ SeveritySource  : ghsa 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13506 
                              ├ DataSource       ╭ ID  : ghsa 
                              │                  ├ Name: GitHub Security Advisory Maven 
                              │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                              │                          osystem%3Amaven 
                              ├ Fingerprint     : sha256:30ed9afdda784481d3ba21b65f495ea5821e674068a4df4d63040b
                              │                   944546c76f 
                              ├ Title           : bouncycastle: Bouncy Castle for Java: Denial of Service via
                              │                   lazy ASN.1 sequence processing 
                              ├ Description     : In Bouncy Castle for Java before 1.85, Lazy ASN.1 sequence
                              │                   forcing resets nesting-depth guard. This issue also affects
                              │                   Bouncy Castle for Java LTS before 2.73.12, and Bouncy Castle
                              │                   for Java FIPS (BC-FJA) before bc-fips 1.0.2.7 (1.0.X series),
                              │                    2.0.2 (2.0.X series) and 2.1.3 (2.1.X series). 
                              ├ Severity        : HIGH 
                              ├ CweIDs                  
                              │                  ───────
                              │                  CWE-674
                              │                  
                              ├ VendorSeverity   ╭ amazon: 3 
                              │                  ├ ghsa  : 3 
                              │                  ├ nvd   : 3 
                              │                  ╰ redhat: 3 
                              ├ CVSS             ╭ ghsa   ╭ V3Vector : CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                              │                  │        │            /A:H 
                              │                  │        ├ V40Vector: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/V
                              │                  │        │            I:N/VA:H/SC:N/SI:N/SA:N/U:Amber 
                              │                  │        ├ V3Score  : 7.5 
                              │                  │        ╰ V40Score : 8.7 
                              │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/
                              │                  │        │           A:H 
                              │                  │        ╰ V3Score : 7.5 
                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/
                              │                           │           A:H 
                              │                           ╰ V3Score : 7.5 
                              ├ References                                                                     
                              │                  ──────────────────────────────────────────────────────────────
                              │                  https://access.redhat.com/security/cve/CVE-2026-13506         
                              │                  https://github.com/bcgit/bc-java                              
                              │                  https://github.com/bcgit/bc-java/commit/77454da9b3dcaaa2991412
                              │                  d1c3c1a6e1a338ff84                                            
                              │                  https://github.com/bcgit/bc-java/wiki/CVE-2026-13506          
                              │                                                                                
                              │                  https://nvd.nist.gov/vuln/detail/CVE-2026-13506               
                              │                                                                                
                              │                  https://www.cve.org/CVERecord?id=CVE-2026-13506               
                              │                                                                                
                              │                  
                              ├ PublishedDate   : 2026-08-03T04:16:39.957Z 
                              ╰ LastModifiedDate: 2026-08-28T16:41:22.84Z 
```
