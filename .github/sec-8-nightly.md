````yaml
╭ [0] ╭ Target: openaf/oaf:8-nightly (alpine 3.19.1) 
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
                              ├ Layer            ╭ Digest: sha256:21f36e7c0938ed8bba753979c67e153b863a072c
                              │                  │         5100eb255a1a832caf3751e1 
                              │                  ╰ DiffID: sha256:047c5eed395b34f09b63bb3e3e332fe44a5dab94
                              │                            e7c39ccaea8833719c2a2f7e 
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
