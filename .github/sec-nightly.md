````yaml
╭ [0] ╭ Target: openaf/oaf:nightly (alpine 3.20.2) 
│     ├ Class : os-pkgs 
│     ╰ Type  : alpine 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2024-25638 
                        │     ├ PkgName         : dnsjava:dnsjava 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/dnsjava/dnsjava@3.5.3 
                        │     │                  ╰ UID : fcd3d0c2bf50859 
                        │     ├ InstalledVersion: 3.5.3 
                        │     ├ FixedVersion    : 3.6.0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:de02d856ec020c12f8c53dbdf312424f6ea217f6
                        │     │                  │         0b21129a1073e64e3f18baa1 
                        │     │                  ╰ DiffID: sha256:375b33c487735b5990d3714861a1a00b564e67aa
                        │     │                            e186887c8e6f9f9c126a3e11 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-25638 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areview
                        │     │                          ed+ecosystem%3Amaven 
                        │     ├ Title           : dnsjava: Improper response validation allowing DNSSEC bypass 
                        │     ├ Description     : dnsjava is an implementation of DNS in Java. Records in
                        │     │                   DNS replies are not checked for their relevance to the query,
                        │     │                    allowing an attacker to respond with RRs from different
                        │     │                   zones. This vulnerability is fixed in 3.6.0. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs           ╭ [0]: CWE-345 
                        │     │                  ╰ [1]: CWE-349 
                        │     ├ VendorSeverity   ╭ ghsa  : 3 
                        │     │                  ╰ redhat: 3 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H
                        │     │                  │        │           /I:H/A:L 
                        │     │                  │        ╰ V3Score : 8.9 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H
                        │     │                           │           /I:H/A:L 
                        │     │                           ╰ V3Score : 8.9 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-25638 
                        │     │                  ├ [1]: https://github.com/dnsjava/dnsjava 
                        │     │                  ├ [2]: https://github.com/dnsjava/dnsjava/commit/bc51df1c
                        │     │                  │      455e6c9fb7cbd42fcb6d62d16047818d 
                        │     │                  ├ [3]: https://github.com/dnsjava/dnsjava/security/adviso
                        │     │                  │      ries/GHSA-cfxw-4h78-h7fw 
                        │     │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-25638 
                        │     │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2024-25638 
                        │     ├ PublishedDate   : 2024-07-22T14:15:04.593Z 
                        │     ╰ LastModifiedDate: 2024-07-22T14:15:04.593Z 
                        ├ [1] ╭ VulnerabilityID : GHSA-crjg-w57m-rqqf 
                        │     ├ PkgName         : dnsjava:dnsjava 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/dnsjava/dnsjava@3.5.3 
                        │     │                  ╰ UID : fcd3d0c2bf50859 
                        │     ├ InstalledVersion: 3.5.3 
                        │     ├ FixedVersion    : 3.6.0 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:de02d856ec020c12f8c53dbdf312424f6ea217f6
                        │     │                  │         0b21129a1073e64e3f18baa1 
                        │     │                  ╰ DiffID: sha256:375b33c487735b5990d3714861a1a00b564e67aa
                        │     │                            e186887c8e6f9f9c126a3e11 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://github.com/advisories/GHSA-crjg-w57m-rqqf 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areview
                        │     │                          ed+ecosystem%3Amaven 
                        │     ├ Title           : DNSJava vulnerable to KeyTrap - Denial-of-Service
                        │     │                   Algorithmic Complexity Attacks 
                        │     ├ Description     : ### Impact
                        │     │                   Users using the `ValidatingResolver` for DNSSEC validation
                        │     │                   can run into CPU exhaustion with specially crafted
                        │     │                   DNSSEC-signed zones.
                        │     │                   
                        │     │                   ### Patches
                        │     │                   Users should upgrade to dnsjava v3.6.0
                        │     │                   
                        │     │                   ### Workarounds
                        │     │                   Although not recommended, only using a non-validating
                        │     │                   resolver, will remove the vulnerability. 
                        │     │                   
                        │     │                   ### References
                        │     │                   https://www.athene-center.de/en/keytrap
                        │     │                    
                        │     ├ Severity        : MEDIUM 
                        │     ├ VendorSeverity   ─ ghsa: 2 
                        │     ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I
                        │     │                         │           :N/A:H 
                        │     │                         ╰ V3Score : 6.5 
                        │     ╰ References       ╭ [0]: https://github.com/dnsjava/dnsjava 
                        │                        ├ [1]: https://github.com/dnsjava/dnsjava/commit/07ac36a1
                        │                        │      1578cc1bce0cd8ddf2fe568f062aee78 
                        │                        ├ [2]: https://github.com/dnsjava/dnsjava/commit/3ddc45ce
                        │                        │      8cdb5c2274e10b7401416f497694e1cf 
                        │                        ╰ [3]: https://github.com/dnsjava/dnsjava/security/adviso
                        │                               ries/GHSA-crjg-w57m-rqqf 
                        ╰ [2] ╭ VulnerabilityID : GHSA-mmwx-rj87-vfgr 
                              ├ PkgName         : dnsjava:dnsjava 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ PkgIdentifier    ╭ PURL: pkg:maven/dnsjava/dnsjava@3.5.3 
                              │                  ╰ UID : fcd3d0c2bf50859 
                              ├ InstalledVersion: 3.5.3 
                              ├ FixedVersion    : 3.6.0 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:de02d856ec020c12f8c53dbdf312424f6ea217f6
                              │                  │         0b21129a1073e64e3f18baa1 
                              │                  ╰ DiffID: sha256:375b33c487735b5990d3714861a1a00b564e67aa
                              │                            e186887c8e6f9f9c126a3e11 
                              ├ SeveritySource  : ghsa 
                              ├ PrimaryURL      : https://github.com/advisories/GHSA-mmwx-rj87-vfgr 
                              ├ DataSource       ╭ ID  : ghsa 
                              │                  ├ Name: GitHub Security Advisory Maven 
                              │                  ╰ URL : https://github.com/advisories?query=type%3Areview
                              │                          ed+ecosystem%3Amaven 
                              ├ Title           : DNSJava affected by KeyTrap - NSEC3 closest encloser
                              │                   proof can exhaust CPU resources 
                              ├ Description     : ### Impact
                              │                   Users using the `ValidatingResolver` for DNSSEC validation
                              │                   can run into CPU exhaustion with specially crafted
                              │                   DNSSEC-signed zones.
                              │                   
                              │                   ### Patches
                              │                   Users should upgrade to dnsjava v3.6.0
                              │                   
                              │                   ### Workarounds
                              │                   Although not recommended, only using a non-validating
                              │                   resolver, will remove the vulnerability.
                              │                   
                              │                   ### References
                              │                   https://www.athene-center.de/en/keytrap
                              │                    
                              ├ Severity        : MEDIUM 
                              ├ VendorSeverity   ─ ghsa: 2 
                              ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I
                              │                         │           :N/A:H 
                              │                         ╰ V3Score : 6.5 
                              ╰ References       ╭ [0]: https://github.com/dnsjava/dnsjava 
                                                 ├ [1]: https://github.com/dnsjava/dnsjava/commit/711af79b
                                                 │      e3214f52daa5c846b95766dc0a075116 
                                                 ╰ [2]: https://github.com/dnsjava/dnsjava/security/adviso
                                                        ries/GHSA-mmwx-rj87-vfgr 
````
