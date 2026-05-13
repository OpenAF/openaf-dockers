```yaml
╭ [0] ╭ Target         : openaf/ojobrt:latest (alpine 3.23.4) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2026-41254 
│                       │     ├ PkgID           : lcms2@2.17-r0 
│                       │     ├ PkgName         : lcms2 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/lcms2@2.17-r0?arch=x86_64&distro=3.23.4 
│                       │     │                  ╰ UID : fab3e62e8c1a419a 
│                       │     ├ InstalledVersion: 2.17-r0 
│                       │     ├ FixedVersion    : 2.19-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:8638e40c547d34de5518259e895082ab99adca577c652
│                       │     │                  │         3a3d1ffdb5ff8d0791b 
│                       │     │                  ╰ DiffID: sha256:c1c6920541d3259ba2d76941c332ba5d6b5819ac31f9e
│                       │     │                            dd22bd374b86102706b 
│                       │     ├ SeveritySource  : nvd 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-41254 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Fingerprint     : sha256:dc600e8b8c9aae87402e47347e2717b52b12cfb0e70686254f8646
│                       │     │                   2817edca0d 
│                       │     ├ Title           : Little CMS: lcms2: mm2/Little-CMS: Little CMS: Information
│                       │     │                   disclosure or denial of service via integer overflow in
│                       │     │                   CubeSize 
│                       │     ├ Description     : Little CMS (lcms2) through 2.18 has an integer overflow in
│                       │     │                   CubeSize in cmslut.c because the overflow check is performed
│                       │     │                   after the multiplication. 
│                       │     ├ Severity        : HIGH 
│                       │     ├ CweIDs           ╭ [0]: CWE-696 
│                       │     │                  ╰ [1]: CWE-190 
│                       │     ├ VendorSeverity   ╭ azure : 2 
│                       │     │                  ├ nvd   : 3 
│                       │     │                  ├ redhat: 2 
│                       │     │                  ╰ ubuntu: 2 
│                       │     ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/
│                       │     │                  │        │           A:H 
│                       │     │                  │        ╰ V3Score : 7.5 
│                       │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 6.1 
│                       │     ├ References       ╭ [0]: https://abhinavagarwal07.github.io/posts/lcms2-cubesize
│                       │     │                  │      -overflow/ 
│                       │     │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-41254 
│                       │     │                  ├ [2]: https://github.com/mm2/Little-CMS/commit/da6110b1d14abc
│                       │     │                  │      394633a388209abd5ebedd7ab0 
│                       │     │                  ├ [3]: https://github.com/mm2/Little-CMS/commit/e0641b1828d0a1
│                       │     │                  │      af5ecb1b11fe22f24fceefd4bc 
│                       │     │                  ├ [4]: https://github.com/mm2/Little-CMS/security/advisories/G
│                       │     │                  │      HSA-4xp6-rcgg-m9qq 
│                       │     │                  ├ [5]: https://lists.debian.org/debian-lts-announce/2026/05/ms
│                       │     │                  │      g00014.html 
│                       │     │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-41254 
│                       │     │                  ├ [7]: https://ubuntu.com/security/notices/USN-8209-1 
│                       │     │                  ├ [8]: https://www.cve.org/CVERecord?id=CVE-2026-41254 
│                       │     │                  ╰ [9]: https://www.openwall.com/lists/oss-security/2026/04/17/16 
│                       │     ├ PublishedDate   : 2026-04-18T07:16:10.807Z 
│                       │     ╰ LastModifiedDate: 2026-05-07T18:16:19.3Z 
│                       ╰ [1] ╭ VulnerabilityID : CVE-2026-27135 
│                             ├ PkgID           : nghttp2-libs@1.68.0-r0 
│                             ├ PkgName         : nghttp2-libs 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/nghttp2-libs@1.68.0-r0?arch=x86_64&dist
│                             │                  │       ro=3.23.4 
│                             │                  ╰ UID : 74e42e23a979e950 
│                             ├ InstalledVersion: 1.68.0-r0 
│                             ├ FixedVersion    : 1.68.1 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:8638e40c547d34de5518259e895082ab99adca577c652
│                             │                  │         3a3d1ffdb5ff8d0791b 
│                             │                  ╰ DiffID: sha256:c1c6920541d3259ba2d76941c332ba5d6b5819ac31f9e
│                             │                            dd22bd374b86102706b 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27135 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Fingerprint     : sha256:ab4c2b2b163522cecea88db5eb082bf3f1073d127dad2c52a47a6c
│                             │                   0e5c8db160 
│                             ├ Title           : nghttp2: nghttp2: Denial of Service via malformed HTTP/2
│                             │                   frames after session termination 
│                             ├ Description     : nghttp2 is an implementation of the Hypertext Transfer
│                             │                   Protocol version 2 in C. Prior to version 1.68.1, the nghttp2
│                             │                    library stops reading the incoming data when user facing
│                             │                   public API `nghttp2_session_terminate_session` or
│                             │                   `nghttp2_session_terminate_session2` is called by the
│                             │                   application. They might be called internally by the library
│                             │                   when it detects the situation that is subject to connection
│                             │                   error. Due to the missing internal state validation, the
│                             │                   library keeps reading the rest of the data after one of those
│                             │                    APIs is called. Then receiving a malformed frame that causes
│                             │                    FRAME_SIZE_ERROR causes assertion failure. nghttp2 v1.68.1
│                             │                   adds missing state validation to avoid assertion failure. No
│                             │                   known workarounds are available. 
│                             ├ Severity        : HIGH 
│                             ├ CweIDs           ─ [0]: CWE-617 
│                             ├ VendorSeverity   ╭ alma       : 3 
│                             │                  ├ amazon     : 3 
│                             │                  ├ azure      : 3 
│                             │                  ├ cbl-mariner: 3 
│                             │                  ├ oracle-oval: 3 
│                             │                  ├ photon     : 3 
│                             │                  ├ redhat     : 3 
│                             │                  ├ rocky      : 3 
│                             │                  ╰ ubuntu     : 2 
│                             ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/
│                             │                           │           A:H 
│                             │                           ╰ V3Score : 7.5 
│                             ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2026/03/20/3 
│                             │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:7896 
│                             │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2026-27135 
│                             │                  ├ [3] : https://bugzilla.redhat.com/2441268 
│                             │                  ├ [4] : https://bugzilla.redhat.com/2442922 
│                             │                  ├ [5] : https://bugzilla.redhat.com/2448754 
│                             │                  ├ [6] : https://bugzilla.redhat.com/2453151 
│                             │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2448754 
│                             │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-202
│                             │                  │       6-27135 
│                             │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2026-7896.html 
│                             │                  ├ [10]: https://errata.rockylinux.org/RLSA-2026:7668 
│                             │                  ├ [11]: https://github.com/nghttp2/nghttp2/commit/5c7df8fa815a
│                             │                  │       c1004d9ecb9d1f7595c4d37f46e1 
│                             │                  ├ [12]: https://github.com/nghttp2/nghttp2/security/advisories
│                             │                  │       /GHSA-6933-cjhr-5qg6 
│                             │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-27135.html 
│                             │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-8339.html 
│                             │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2026-27135 
│                             │                  ├ [16]: https://ubuntu.com/security/notices/USN-8233-1 
│                             │                  ├ [17]: https://ubuntu.com/security/notices/USN-8233-2 
│                             │                  ╰ [18]: https://www.cve.org/CVERecord?id=CVE-2026-27135 
│                             ├ PublishedDate   : 2026-03-18T18:16:26.723Z 
│                             ╰ LastModifiedDate: 2026-03-23T17:51:17.017Z 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ├ Packages        
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2026-5598 
                        │     ├ VendorIDs        ─ [0]: GHSA-p93r-85wp-75v3 
                        │     ├ PkgName         : org.bouncycastle:bcprov-jdk18on 
                        │     ├ PkgPath         : openaf/S3/bcprov-jdk18on-1.82.jar 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:maven/org.bouncycastle/bcprov-jdk18on@1.82 
                        │     │                  ╰ UID : ba3bda42b1145eb2 
                        │     ├ InstalledVersion: 1.82 
                        │     ├ FixedVersion    : 1.84 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:f52bf5b96f8757349ed0b105b64c5f3827f7a9c7672de
                        │     │                  │         3ea0c787e6528fca34a 
                        │     │                  ╰ DiffID: sha256:c7e127c628ebf16cb5d765a28c888be2ebe3292c86090
                        │     │                            ac436e739bb1c7ea6d8 
                        │     ├ SeveritySource  : ghsa 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5598 
                        │     ├ DataSource       ╭ ID  : ghsa 
                        │     │                  ├ Name: GitHub Security Advisory Maven 
                        │     │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                        │     │                          osystem%3Amaven 
                        │     ├ Fingerprint     : sha256:56301bb8aeb72fec1a2cf8f0b3cf4545f4bbb65603ab9a2156af62
                        │     │                   704febb675 
                        │     ├ Title           : bouncycastle: BC-JAVA: private key leakage via non-constant
                        │     │                   time comparisons 
                        │     ├ Description     : Covert timing channel vulnerability in Legion of the Bouncy
                        │     │                   Castle Inc. BC-JAVA core on all (core modules). This
                        │     │                   vulnerability is associated with program files
                        │     │                   FrodoEngine.Java.
                        │     │                   
                        │     │                   This issue affects BC-JAVA: from 1.71 before 1.84. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs           ─ [0]: CWE-385 
                        │     ├ VendorSeverity   ╭ ghsa  : 3 
                        │     │                  ╰ redhat: 3 
                        │     ├ CVSS             ╭ ghsa   ╭ V40Vector: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/V
                        │     │                  │        │            I:H/VA:N/SC:H/SI:H/SA:N/E:U/S:P/AU:Y/U:R
                        │     │                  │        │            ed 
                        │     │                  │        ╰ V40Score : 8.9 
                        │     │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/
                        │     │                           │           A:N 
                        │     │                           ╰ V3Score : 7.5 
                        │     ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-5598 
                        │     │                  ├ [1]: https://github.com/bcgit/bc-java 
                        │     │                  ├ [2]: https://github.com/bcgit/bc-java/commit/8692e6b2b191fc4
                        │     │                  │      aafa32545c7a78bdb9bf110c5 
                        │     │                  ├ [3]: https://github.com/bcgit/bc-java/commit/94abbd56413dfda
                        │     │                  │      c651fd878bc60253871ef5e87 
                        │     │                  ├ [4]: https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%
                        │     │                  │      E2%80%905598 
                        │     │                  ├ [5]: https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%
                        │     │                  │      E2%80%905998 
                        │     │                  ├ [6]: https://github.com/bcgit/bc-java/wiki/CVE-2026-5598 
                        │     │                  ├ [7]: https://nvd.nist.gov/vuln/detail/CVE-2026-5598 
                        │     │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2026-5598 
                        │     ├ PublishedDate   : 2026-04-15T10:16:49.757Z 
                        │     ╰ LastModifiedDate: 2026-04-21T16:16:20.717Z 
                        ╰ [1] ╭ VulnerabilityID : CVE-2026-0636 
                              ├ VendorIDs        ─ [0]: GHSA-c3fc-8qff-9hwx 
                              ├ PkgName         : org.bouncycastle:bcprov-jdk18on 
                              ├ PkgPath         : openaf/S3/bcprov-jdk18on-1.82.jar 
                              ├ PkgIdentifier    ╭ PURL: pkg:maven/org.bouncycastle/bcprov-jdk18on@1.82 
                              │                  ╰ UID : ba3bda42b1145eb2 
                              ├ InstalledVersion: 1.82 
                              ├ FixedVersion    : 1.84 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:f52bf5b96f8757349ed0b105b64c5f3827f7a9c7672de
                              │                  │         3ea0c787e6528fca34a 
                              │                  ╰ DiffID: sha256:c7e127c628ebf16cb5d765a28c888be2ebe3292c86090
                              │                            ac436e739bb1c7ea6d8 
                              ├ SeveritySource  : ghsa 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-0636 
                              ├ DataSource       ╭ ID  : ghsa 
                              │                  ├ Name: GitHub Security Advisory Maven 
                              │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                              │                          osystem%3Amaven 
                              ├ Fingerprint     : sha256:d73fb6cb979aa781182cce6f52adfdb5c27ffd1d1718618c8117f9
                              │                   6e05bf9e39 
                              ├ Title           : bouncycastle: BC-JAVA: LDAP injection vulnerability in
                              │                   LDAPStoreHelper.java 
                              ├ Description     : Improper neutralization of special elements used in an LDAP
                              │                   query ('LDAP injection') vulnerability in Legion of the
                              │                   Bouncy Castle Inc. BC-JAVA bcprov on all (prov modules). This
                              │                    vulnerability is associated with program files
                              │                   LDAPStoreHelper.
                              │                   
                              │                   This issue affects BC-JAVA: from 1.74 before 1.84. 
                              ├ Severity        : MEDIUM 
                              ├ CweIDs           ─ [0]: CWE-90 
                              ├ VendorSeverity   ╭ ghsa  : 2 
                              │                  ╰ redhat: 3 
                              ├ CVSS             ╭ ghsa   ╭ V40Vector: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/V
                              │                  │        │            I:N/VA:N/SC:N/SI:N/SA:N/E:P/RE:M/U:Amber
                              │                  │        │             
                              │                  │        ╰ V40Score : 5.5 
                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/
                              │                           │           A:N 
                              │                           ╰ V3Score : 6.5 
                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-0636 
                              │                  ├ [1]: https://github.com/bcgit/bc-java 
                              │                  ├ [2]: https://github.com/bcgit/bc-java/commit/d20cdb8430e0922
                              │                  │      4114fec0179a71859929fcbde 
                              │                  ├ [3]: https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%
                              │                  │      E2%80%900636 
                              │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-0636 
                              │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-0636 
                              ├ PublishedDate   : 2026-04-15T10:16:38.413Z 
                              ╰ LastModifiedDate: 2026-04-17T15:38:09.243Z 
```
