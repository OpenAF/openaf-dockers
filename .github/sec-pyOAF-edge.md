```yaml
╭ [0] ╭ Target         : openaf/pyoaf:edge (alpine 3.24.1) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2026-2100 
│                       │     ├ PkgID           : p11-kit@0.25.5-r2 
│                       │     ├ PkgName         : p11-kit 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/p11-kit@0.25.5-r2?arch=x86_64&distro=3.
│                       │     │                  │       24.1 
│                       │     │                  ╰ UID : 9d018f0737ae08a7 
│                       │     ├ InstalledVersion: 0.25.5-r2 
│                       │     ├ FixedVersion    : 0.26.2-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
│                       │     │                  │         427b17582323a475421 
│                       │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
│                       │     │                            13c7ec0494711fcad72 
│                       │     ├ SeveritySource  : nvd 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-2100 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Fingerprint     : sha256:dc9f02b37f36fda9ae2fc85cc2084f699835ba135465c90206da06
│                       │     │                   84ccd0f0c1 
│                       │     ├ Title           : p11-kit: NULL dereference via C_DeriveKey with specific NULL
│                       │     │                   parameters 
│                       │     ├ Description     : A flaw was found in p11-kit. A remote attacker could exploit
│                       │     │                   this vulnerability by calling the C_DeriveKey function on a
│                       │     │                   remote token with specific IBM kyber or IBM btc derive
│                       │     │                   mechanism parameters set to NULL. This could lead to the
│                       │     │                   RPC-client attempting to return an uninitialized value,
│                       │     │                   potentially resulting in a NULL dereference or undefined
│                       │     │                   behavior. This issue may cause an application level denial of
│                       │     │                    service or other unpredictable system states. 
│                       │     ├ Severity        : HIGH 
│                       │     ├ CweIDs           ─ [0]: CWE-824 
│                       │     ├ VendorSeverity   ╭ alma       : 2 
│                       │     │                  ├ nvd        : 3 
│                       │     │                  ├ oracle-oval: 2 
│                       │     │                  ├ redhat     : 2 
│                       │     │                  ╰ rocky      : 2 
│                       │     ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/
│                       │     │                  │        │           A:H 
│                       │     │                  │        ╰ V3Score : 7.5 
│                       │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/
│                       │     │                           │           A:L 
│                       │     │                           ╰ V3Score : 5.3 
│                       │     ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:18143 
│                       │     │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:18599 
│                       │     │                  ├ [2] : https://access.redhat.com/errata/RHSA-2026:21275 
│                       │     │                  ├ [3] : https://access.redhat.com/errata/RHSA-2026:22634 
│                       │     │                  ├ [4] : https://access.redhat.com/errata/RHSA-2026:27998 
│                       │     │                  ├ [5] : https://access.redhat.com/errata/RHSA-2026:7065 
│                       │     │                  ├ [6] : https://access.redhat.com/security/cve/CVE-2026-2100 
│                       │     │                  ├ [7] : https://bugzilla.redhat.com/2437308 
│                       │     │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2437308 
│                       │     │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-202
│                       │     │                  │       6-2100 
│                       │     │                  ├ [10]: https://errata.almalinux.org/9/ALSA-2026-18599.html 
│                       │     │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:18599 
│                       │     │                  ├ [12]: https://github.com/p11-glue/p11-kit/pull/740 
│                       │     │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-2100.html 
│                       │     │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-18599.html 
│                       │     │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2026-2100 
│                       │     │                  ╰ [16]: https://www.cve.org/CVERecord?id=CVE-2026-2100 
│                       │     ├ PublishedDate   : 2026-03-26T21:17:04.247Z 
│                       │     ╰ LastModifiedDate: 2026-06-22T20:16:28.86Z 
│                       ╰ [1] ╭ VulnerabilityID : CVE-2026-2100 
│                             ├ PkgID           : p11-kit-trust@0.25.5-r2 
│                             ├ PkgName         : p11-kit-trust 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/p11-kit-trust@0.25.5-r2?arch=x86_64&dis
│                             │                  │       tro=3.24.1 
│                             │                  ╰ UID : 40951c87f9e2103c 
│                             ├ InstalledVersion: 0.25.5-r2 
│                             ├ FixedVersion    : 0.26.2-r0 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
│                             │                  │         427b17582323a475421 
│                             │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
│                             │                            13c7ec0494711fcad72 
│                             ├ SeveritySource  : nvd 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-2100 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Fingerprint     : sha256:1219de7b7022ffbe37ab5ae0159c52e0cd67b521f533eb6ee8f7e7
│                             │                   20ef8a4171 
│                             ├ Title           : p11-kit: NULL dereference via C_DeriveKey with specific NULL
│                             │                   parameters 
│                             ├ Description     : A flaw was found in p11-kit. A remote attacker could exploit
│                             │                   this vulnerability by calling the C_DeriveKey function on a
│                             │                   remote token with specific IBM kyber or IBM btc derive
│                             │                   mechanism parameters set to NULL. This could lead to the
│                             │                   RPC-client attempting to return an uninitialized value,
│                             │                   potentially resulting in a NULL dereference or undefined
│                             │                   behavior. This issue may cause an application level denial of
│                             │                    service or other unpredictable system states. 
│                             ├ Severity        : HIGH 
│                             ├ CweIDs           ─ [0]: CWE-824 
│                             ├ VendorSeverity   ╭ alma       : 2 
│                             │                  ├ nvd        : 3 
│                             │                  ├ oracle-oval: 2 
│                             │                  ├ redhat     : 2 
│                             │                  ╰ rocky      : 2 
│                             ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/
│                             │                  │        │           A:H 
│                             │                  │        ╰ V3Score : 7.5 
│                             │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/
│                             │                           │           A:L 
│                             │                           ╰ V3Score : 5.3 
│                             ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:18143 
│                             │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:18599 
│                             │                  ├ [2] : https://access.redhat.com/errata/RHSA-2026:21275 
│                             │                  ├ [3] : https://access.redhat.com/errata/RHSA-2026:22634 
│                             │                  ├ [4] : https://access.redhat.com/errata/RHSA-2026:27998 
│                             │                  ├ [5] : https://access.redhat.com/errata/RHSA-2026:7065 
│                             │                  ├ [6] : https://access.redhat.com/security/cve/CVE-2026-2100 
│                             │                  ├ [7] : https://bugzilla.redhat.com/2437308 
│                             │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2437308 
│                             │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-202
│                             │                  │       6-2100 
│                             │                  ├ [10]: https://errata.almalinux.org/9/ALSA-2026-18599.html 
│                             │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:18599 
│                             │                  ├ [12]: https://github.com/p11-glue/p11-kit/pull/740 
│                             │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-2100.html 
│                             │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-18599.html 
│                             │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2026-2100 
│                             │                  ╰ [16]: https://www.cve.org/CVERecord?id=CVE-2026-2100 
│                             ├ PublishedDate   : 2026-03-26T21:17:04.247Z 
│                             ╰ LastModifiedDate: 2026-06-22T20:16:28.86Z 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ├ Packages        
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2026-54512 
                        │     ├ VendorIDs        ─ [0]: GHSA-j3rv-43j4-c7qm 
                        │     ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                        │     │                  │       2.21.1 
                        │     │                  ╰ UID : f5a07e107dd30f70 
                        │     ├ InstalledVersion: 2.21.1 
                        │     ├ FixedVersion    : 2.18.8, 3.1.4, 2.21.4 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                        │     │                  │         427b17582323a475421 
                        │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                        │     │                            13c7ec0494711fcad72 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54512 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:6c9609cceeea13c0f3b8c5fe4b2047a6260adc7a023aa06879bc94
                        │     │                   21fc10a6c8 
                        │     ├ Title           : jackson-databind contains the general-purpose data-binding
                        │     │                   functionali ... 
                        │     ├ Description     : jackson-databind contains the general-purpose data-binding
                        │     │                   functionality and tree-model for Jackson Data Processor. From
                        │     │                    2.10.0 until 2.18.8, 2.21.4, and 3.1.4, jackson-databind's
                        │     │                   PolymorphicTypeValidator (PTV) is the primary safety
                        │     │                   mechanism guarding polymorphic deserialization. When
                        │     │                   polymorphic typing is enabled and a type identifier contains
                        │     │                   generic parameters (i.e. the type ID string contains <),
                        │     │                   DatabindContext._resolveAndValidateGeneric() validates only
                        │     │                   the raw container class name (the substring before <) against
                        │     │                    the configured PTV. If the container type is approved, the
                        │     │                   method parses the full canonical type string via
                        │     │                   TypeFactory.constructFromCanonical() and returns the fully
                        │     │                   parameterized type without ever validating the nested type
                        │     │                   arguments against the PTV. The nested type arguments are then
                        │     │                    resolved, instantiated, and populated as beans during
                        │     │                   deserialization. An attacker who controls the type ID can
                        │     │                   therefore place a denied class as a generic type parameter of
                        │     │                    an allowed container — for example
                        │     │                   java.util.ArrayList<com.evil.Gadget> when only
                        │     │                   java.util.ArrayList is allow-listed. The container passes the
                        │     │                    PTV check; com.evil.Gadget is loaded via Class.forName(name,
                        │     │                    true, loader), instantiated, and its properties are set from
                        │     │                    attacker-controlled JSON. This completely bypasses an
                        │     │                   explicitly configured PTV allow-list. This vulnerability is
                        │     │                   fixed in 2.18.8, 2.21.4, and 3.1.4. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs           ╭ [0]: CWE-184 
                        │     │                  ╰ [1]: CWE-502 
                        │     ├ VendorSeverity   ─ ghsa: 3 
                        │     ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H 
                        │     │                         ╰ V3Score : 8.1 
                        │     ├ References       ╭ [0]: https://github.com/FasterXML/jackson-databind 
                        │     │                  ├ [1]: https://github.com/FasterXML/jackson-databind/commit/43
                        │     │                  │      4d6c511de7fdd9872f29157aafb6162d12d8d5 
                        │     │                  ├ [2]: https://github.com/FasterXML/jackson-databind/issues/5988 
                        │     │                  ╰ [3]: https://github.com/FasterXML/jackson-databind/security/
                        │     │                         advisories/GHSA-j3rv-43j4-c7qm 
                        │     ├ PublishedDate   : 2026-06-23T21:17:02.203Z 
                        │     ╰ LastModifiedDate: 2026-06-27T21:01:36.47Z 
                        ├ [1] ╭ VulnerabilityID : CVE-2026-54513 
                        │     ├ VendorIDs        ─ [0]: GHSA-rmj7-2vxq-3g9f 
                        │     ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                        │     │                  │       2.21.1 
                        │     │                  ╰ UID : f5a07e107dd30f70 
                        │     ├ InstalledVersion: 2.21.1 
                        │     ├ FixedVersion    : 2.18.8, 2.21.4, 3.1.4 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                        │     │                  │         427b17582323a475421 
                        │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                        │     │                            13c7ec0494711fcad72 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54513 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:431328ce54c81c37d3bbf63addd9ea14cb44af52a5a17424c5821b
                        │     │                   5f95bbb641 
                        │     ├ Title           : jackson-databind: Jackson-databind: Security bypass allows
                        │     │                   arbitrary code execution 
                        │     ├ Description     : jackson-databind contains the general-purpose data-binding
                        │     │                   functionality and tree-model for Jackson Data Processor. From
                        │     │                    2.10.0 until 2.18.8, 2.21.4, and 3.1.4,
                        │     │                   BasicPolymorphicTypeValidator.Builder.allowIfSubTypeIsArray()
                        │     │                    allowlists any array type based only on clazz.isArray(),
                        │     │                   without validating the array's component (element) type
                        │     │                   against the configured allowlist. A PTV built with
                        │     │                   allowIfSubTypeIsArray() plus an explicit concrete-type
                        │     │                   allowlist therefore still permits EvilType[] even though
                        │     │                   EvilType is not allowlisted. When Jackson deserializes the
                        │     │                   elements and no per-element type IDs are present, it
                        │     │                   instantiates the component type directly with no further PTV
                        │     │                   check, bypassing the allowlist. This vulnerability is fixed
                        │     │                   in 2.18.8, 2.21.4, and 3.1.4. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs           ─ [0]: CWE-184 
                        │     ├ VendorSeverity   ╭ ghsa  : 3 
                        │     │                  ╰ redhat: 3 
                        │     ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/
                        │     │                  │        │           A:H 
                        │     │                  │        ╰ V3Score : 8.1 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/
                        │     │                           │           A:H 
                        │     │                           ╰ V3Score : 8.1 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-54513 
                        │     │                  ├ [1]: https://github.com/FasterXML/jackson-databind 
                        │     │                  ├ [2]: https://github.com/FasterXML/jackson-databind/commit/01
                        │     │                  │      d1692c8d0ed03e51a0e3c4f8a9e6908e4931e5 
                        │     │                  ├ [3]: https://github.com/FasterXML/jackson-databind/commit/24
                        │     │                  │      529da29fdf46ff94ca38de9ebf31cd188f5e8e 
                        │     │                  ├ [4]: https://github.com/FasterXML/jackson-databind/issues/5981 
                        │     │                  ├ [5]: https://github.com/FasterXML/jackson-databind/issues/5983 
                        │     │                  ├ [6]: https://github.com/FasterXML/jackson-databind/pull/5984 
                        │     │                  ├ [7]: https://github.com/FasterXML/jackson-databind/security/
                        │     │                  │      advisories/GHSA-rmj7-2vxq-3g9f 
                        │     │                  ├ [8]: https://nvd.nist.gov/vuln/detail/CVE-2026-54513 
                        │     │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2026-54513 
                        │     ├ PublishedDate   : 2026-06-23T21:17:02.333Z 
                        │     ╰ LastModifiedDate: 2026-06-27T21:00:19.3Z 
                        ├ [2] ╭ VulnerabilityID : CVE-2026-54514 
                        │     ├ VendorIDs        ─ [0]: GHSA-hgj6-7826-r7m5 
                        │     ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                        │     │                  │       2.21.1 
                        │     │                  ╰ UID : f5a07e107dd30f70 
                        │     ├ InstalledVersion: 2.21.1 
                        │     ├ FixedVersion    : 2.18.8, 2.21.4, 3.1.4 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                        │     │                  │         427b17582323a475421 
                        │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                        │     │                            13c7ec0494711fcad72 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54514 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:8a2714b918a9c3e5ef8c4b7d24e3b892b5ff1378c48d4cac072972
                        │     │                   546699da4d 
                        │     ├ Title           : jackson-databind contains the general-purpose data-binding
                        │     │                   functionali ... 
                        │     ├ Description     : jackson-databind contains the general-purpose data-binding
                        │     │                   functionality and tree-model for Jackson Data Processor. From
                        │     │                    2.0.0 until 2.18.8, 2.21.4, and 3.1.4,
                        │     │                   JDKFromStringDeserializer constructed InetSocketAddress with
                        │     │                   new InetSocketAddress(host, port), which performs eager DNS
                        │     │                   name resolution for hostname inputs at deserialization time.
                        │     │                   An application that binds untrusted JSON into a type
                        │     │                   containing an InetSocketAddress field issues an
                        │     │                   attacker-chosen DNS query during readValue, before any
                        │     │                   application-level validation or connect logic. The fix uses
                        │     │                   InetSocketAddress.createUnresolved(host, port), deferring DNS
                        │     │                    to an explicit connect. This vulnerability is fixed in
                        │     │                   2.18.8, 2.21.4, and 3.1.4. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-918 
                        │     ├ VendorSeverity   ─ ghsa: 2 
                        │     ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N 
                        │     │                         ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://github.com/FasterXML/jackson-databind 
                        │     │                  ├ [1]: https://github.com/FasterXML/jackson-databind/commit/1f
                        │     │                  │      5a1037b1e9e05920e755cb35f198bcd46667e4 
                        │     │                  ├ [2]: https://github.com/FasterXML/jackson-databind/pull/5951 
                        │     │                  ╰ [3]: https://github.com/FasterXML/jackson-databind/security/
                        │     │                         advisories/GHSA-hgj6-7826-r7m5 
                        │     ├ PublishedDate   : 2026-06-23T21:17:02.467Z 
                        │     ╰ LastModifiedDate: 2026-06-27T20:55:09.61Z 
                        ├ [3] ╭ VulnerabilityID : CVE-2026-54515 
                        │     ├ VendorIDs        ─ [0]: GHSA-5jmj-h7xm-6q6v 
                        │     ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                        │     │                  │       2.21.1 
                        │     │                  ╰ UID : f5a07e107dd30f70 
                        │     ├ InstalledVersion: 2.21.1 
                        │     ├ FixedVersion    : 3.1.4, 2.18.9, 2.21.5 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                        │     │                  │         427b17582323a475421 
                        │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                        │     │                            13c7ec0494711fcad72 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54515 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:4e769cf6e7c6187379254e1c67b64adb5f302dc80fa2e05e9e069d
                        │     │                   6d99e55ca0 
                        │     ├ Title           : jackson-databind contains the general-purpose data-binding
                        │     │                   functionali ... 
                        │     ├ Description     : jackson-databind contains the general-purpose data-binding
                        │     │                   functionality and tree-model for Jackson Data Processor. From
                        │     │                    2.8.0 until 2.18.9, 2.21.5, and 3.1.4, in
                        │     │                   BeanDeserializerBase.createContextual(), per-property
                        │     │                   @JsonIgnoreProperties exclusions are applied by
                        │     │                   _handleByNameInclusion(), producing a contextual deserializer
                        │     │                    whose BeanPropertyMap has the ignored properties removed.
                        │     │                   The subsequent per-property case-insensitivity block
                        │     │                   (triggered by
                        │     │                   @JsonFormat(ACCEPT_CASE_INSENSITIVE_PROPERTIES)) rebuilds
                        │     │                   from this._beanProperties (the original, unfiltered map)
                        │     │                   instead of contextual._beanProperties, then overwrites the
                        │     │                   filtered map — restoring every property
                        │     │                   _handleByNameInclusion had just removed. The ignored property
                        │     │                    becomes writable again. This vulnerability is fixed in
                        │     │                   2.18.9, 2.21.5, and 3.1.4. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-915 
                        │     ├ VendorSeverity   ─ ghsa: 2 
                        │     ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │     │                         ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://github.com/FasterXML/jackson-databind 
                        │     │                  ├ [1]: https://github.com/FasterXML/jackson-databind/commit/0e
                        │     │                  │      1b0b211f7a53baa62ba2f4c9bd006c7bf4d5fa 
                        │     │                  ├ [2]: https://github.com/FasterXML/jackson-databind/issues/5962 
                        │     │                  ├ [3]: https://github.com/FasterXML/jackson-databind/issues/5964 
                        │     │                  ╰ [4]: https://github.com/FasterXML/jackson-databind/security/
                        │     │                         advisories/GHSA-5jmj-h7xm-6q6v 
                        │     ├ PublishedDate   : 2026-06-23T21:17:02.597Z 
                        │     ╰ LastModifiedDate: 2026-06-25T16:14:14.483Z 
                        ├ [4] ╭ VulnerabilityID : CVE-2026-54516 
                        │     ├ VendorIDs        ─ [0]: GHSA-9fxm-vc8v-hj55 
                        │     ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                        │     │                  │       2.21.1 
                        │     │                  ╰ UID : f5a07e107dd30f70 
                        │     ├ InstalledVersion: 2.21.1 
                        │     ├ FixedVersion    : 2.21.4, 3.1.4 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                        │     │                  │         427b17582323a475421 
                        │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                        │     │                            13c7ec0494711fcad72 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54516 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:4a519ec7cd6307df0fe35c102caadb11182fa447faab4238843c68
                        │     │                   34b010af5d 
                        │     ├ Title           : jackson-databind contains the general-purpose data-binding
                        │     │                   functionali ... 
                        │     ├ Description     : jackson-databind contains the general-purpose data-binding
                        │     │                   functionality and tree-model for Jackson Data Processor. From
                        │     │                    2.21.0 until 2.21.4 and 3.1.4,
                        │     │                   POJOPropertiesCollector._renameProperties() allows a property
                        │     │                    with @JsonProperty("renamed") on the getter and @JsonIgnore
                        │     │                   on the setter to be renamed rather than dropped. With
                        │     │                   MapperFeature.INFER_PROPERTY_MUTATORS enabled (default), the
                        │     │                   private backing field is retained; during deserialization
                        │     │                   BeanDeserializerFactory.addBeanProps() sees hasField()==true,
                        │     │                    builds a FieldProperty, and makes the backing field
                        │     │                   writable. An attacker supplying the renamed JSON key writes
                        │     │                   the backing field directly, bypassing the @JsonIgnore on the
                        │     │                   setter. This vulnerability is fixed in 3.1.4. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-915 
                        │     ├ VendorSeverity   ─ ghsa: 2 
                        │     ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │     │                         ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://github.com/FasterXML/jackson-databind 
                        │     │                  ├ [1]: https://github.com/FasterXML/jackson-databind/commit/c3
                        │     │                  │      d56dd25d52319828147c5b9aeabf2d485c250a 
                        │     │                  ├ [2]: https://github.com/FasterXML/jackson-databind/commit/e8
                        │     │                  │      8cb17006b6af4883b973058f0bb6486e5074af 
                        │     │                  ├ [3]: https://github.com/FasterXML/jackson-databind/pull/5967 
                        │     │                  ├ [4]: https://github.com/FasterXML/jackson-databind/pull/5968 
                        │     │                  ╰ [5]: https://github.com/FasterXML/jackson-databind/security/
                        │     │                         advisories/GHSA-9fxm-vc8v-hj55 
                        │     ├ PublishedDate   : 2026-06-23T21:17:02.723Z 
                        │     ╰ LastModifiedDate: 2026-06-27T20:52:12.103Z 
                        ├ [5] ╭ VulnerabilityID : CVE-2026-54517 
                        │     ├ VendorIDs        ─ [0]: GHSA-5hh8-q8hv-fr38 
                        │     ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                        │     │                  │       2.21.1 
                        │     │                  ╰ UID : f5a07e107dd30f70 
                        │     ├ InstalledVersion: 2.21.1 
                        │     ├ FixedVersion    : 2.21.4, 3.1.4 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                        │     │                  │         427b17582323a475421 
                        │     │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                        │     │                            13c7ec0494711fcad72 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54517 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:5bb7321a7424d2edcebb60d956e35e976db6f02b4974792a9d0910
                        │     │                   d0ed23f54e 
                        │     ├ Title           : jackson-databind contains the general-purpose data-binding
                        │     │                   functionali ... 
                        │     ├ Description     : jackson-databind contains the general-purpose data-binding
                        │     │                   functionality and tree-model for Jackson Data Processor. From
                        │     │                    2.21.0 until 2.21.4 and 3.1.4, in
                        │     │                   BeanDeserializer._deserializeUsingPropertyBased, the
                        │     │                   active-view (@JsonView) filter was applied only to creator
                        │     │                   properties; the regular property-buffering branch performed
                        │     │                   no prop.visibleInView(activeView) check. A change making
                        │     │                   SetterlessProperty.isMerging() return true routed setterless
                        │     │                   Collection/Map properties through this unguarded path, so a
                        │     │                   setterless collection annotated with a restricted @JsonView
                        │     │                   is populated from attacker JSON even when the active view
                        │     │                   excludes it. This vulnerability is fixed in 2.21.4 and
                        │     │                   3.1.4. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-863 
                        │     ├ VendorSeverity   ─ ghsa: 2 
                        │     ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │     │                         ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://github.com/FasterXML/jackson-databind 
                        │     │                  ├ [1]: https://github.com/FasterXML/jackson-databind/commit/5b
                        │     │                  │      f23edb4221f7dd2ec8e71ff6d26c61640f261d 
                        │     │                  ├ [2]: https://github.com/FasterXML/jackson-databind/commit/94
                        │     │                  │      c5d215b3af1505098c686405d9641f041a9962 
                        │     │                  ├ [3]: https://github.com/FasterXML/jackson-databind/pull/5969 
                        │     │                  ├ [4]: https://github.com/FasterXML/jackson-databind/pull/5970 
                        │     │                  ╰ [5]: https://github.com/FasterXML/jackson-databind/security/
                        │     │                         advisories/GHSA-5hh8-q8hv-fr38 
                        │     ├ PublishedDate   : 2026-06-23T21:17:02.853Z 
                        │     ╰ LastModifiedDate: 2026-06-27T20:51:09.987Z 
                        ╰ [6] ╭ VulnerabilityID : CVE-2026-54518 
                              ├ VendorIDs        ─ [0]: GHSA-rcqc-6cw3-h962 
                              ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
                              │                  │       2.21.1 
                              │                  ╰ UID : f5a07e107dd30f70 
                              ├ InstalledVersion: 2.21.1 
                              ├ FixedVersion    : 2.21.4 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:2c70bd0476047a0dea3edb077b8c2b77a9c3b9c088349
                              │                  │         427b17582323a475421 
                              │                  ╰ DiffID: sha256:f34cf3d2e26c1259e7e35018ba3bd2483ae339f54d25d
                              │                            13c7ec0494711fcad72 
                              ├ SeveritySource  : ghsa 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54518 
                              ├ DataSource       ╭ ID  : ghsa 
                              │                  ├ Name: GitHub Security Advisory Maven 
                              │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                              │                          osystem%3Amaven 
                              ├ Fingerprint     : sha256:90b5e865f81d486cdde61b3c3185f0a9892bd0ab98ae3c49144bf3
                              │                   8875939424 
                              ├ Title           : jackson-databind contains the general-purpose data-binding
                              │                   functionali ... 
                              ├ Description     : jackson-databind contains the general-purpose data-binding
                              │                   functionality and tree-model for Jackson Data Processor. From
                              │                    2.21.0 until 2.21.4 and 3.1.4,
                              │                   UnwrappedPropertyHandler.processUnwrappedCreatorProperties()
                              │                   replays buffered JSON into creator parameters but never
                              │                   consults prop.visibleInView(activeView). The normal
                              │                   property-based creator path gates creator properties on the
                              │                   active view, but this unwrapped-creator replay path bypasses
                              │                   that check, so a constructor parameter annotated with both
                              │                   @JsonView(AdminView.class) and @JsonUnwrapped is populated
                              │                   from attacker JSON even when a more restrictive view is
                              │                   active. This vulnerability is fixed in 2.21.4 and 3.1.4. 
                              ├ Severity        : MEDIUM 
                              ├ CweIDs           ─ [0]: CWE-863 
                              ├ VendorSeverity   ─ ghsa: 2 
                              ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N 
                              │                         ╰ V3Score : 6.5 
                              ├ References       ╭ [0]: https://github.com/FasterXML/jackson-databind 
                              │                  ├ [1]: https://github.com/FasterXML/jackson-databind/commit/72
                              │                  │      1fa07ebbd4aab4a659a1a68940878315c3e341 
                              │                  ├ [2]: https://github.com/FasterXML/jackson-databind/commit/d6
                              │                  │      33bc038f200c1397c07f1a2b46f58e72c91eea 
                              │                  ├ [3]: https://github.com/FasterXML/jackson-databind/pull/5971 
                              │                  ├ [4]: https://github.com/FasterXML/jackson-databind/pull/5973 
                              │                  ╰ [5]: https://github.com/FasterXML/jackson-databind/security/
                              │                         advisories/GHSA-rcqc-6cw3-h962 
                              ├ PublishedDate   : 2026-06-23T22:16:32.073Z 
                              ╰ LastModifiedDate: 2026-06-27T20:49:30.977Z 
```
