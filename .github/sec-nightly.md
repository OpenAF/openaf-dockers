````yaml
╭ [0] ╭ Target: openaf/oaf:nightly (alpine 3.19.1) 
│     ├ Class : os-pkgs 
│     ╰ Type  : alpine 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2024-31033 
                              ├ PkgName         : io.jsonwebtoken:jjwt-impl 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ PkgIdentifier    ─ PURL: pkg:maven/io.jsonwebtoken/jjwt-impl@0.12.5 
                              ├ InstalledVersion: 0.12.5 
                              ├ Status          : affected 
                              ├ Layer            ╭ Digest: sha256:d45fe311ce24b4729d90c5c835d60262dacd8b7d
                              │                  │         dd578eb3438e7b2dcff0fbc3 
                              │                  ╰ DiffID: sha256:e36199746d4bee05eb2115363e4b87495b549223
                              │                            3bd42f173b502cf7694b4c71 
                              ├ SeveritySource  : ghsa 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-31033 
                              ├ DataSource       ╭ ID  : ghsa 
                              │                  ├ Name: GitHub Security Advisory Maven 
                              │                  ╰ URL : https://github.com/advisories?query=type%3Areview
                              │                          ed+ecosystem%3Amaven 
                              ├ Title           : JJWT improperly generates signing keys 
                              ├ Description     : JJWT (aka Java JWT) through 0.12.5 ignores certain
                              │                   characters and thus a user might falsely conclude that they
                              │                   have a strong key. The impacted code is the setSigningKey()
                              │                   method within the DefaultJwtParser class and the signWith()
                              │                   method within the DefaultJwtBuilder class. 
                              ├ Severity        : MEDIUM 
                              ├ VendorSeverity   ─ ghsa: 2 
                              ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I
                              │                         │           :H/A:N 
                              │                         ╰ V3Score : 6.8 
                              ├ References       ╭ [0]: https://github.com/2308652512/JJWT_BUG 
                              │                  ├ [1]: https://github.com/jwtk/jjwt 
                              │                  ├ [2]: https://github.com/jwtk/jjwt/blob/26948610fbef81eb
                              │                  │      a867cbaad54b516d1874c70a/impl/src/main/java/io/jsonwebt
                              │                  │      oken/impl/DefaultJwtParserBuilder.java#L242 
                              │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2024-31033 
                              │                  ├ [4]: https://www.viralpatel.net/java-create-validate-jw
                              │                  │      t-token 
                              │                  ╰ [5]: https://www.viralpatel.net/java-create-validate-jw
                              │                         t-token/ 
                              ├ PublishedDate   : 2024-04-01T02:15:07.85Z 
                              ╰ LastModifiedDate: 2024-04-01T12:49:09.583Z 
````
