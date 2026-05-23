```yaml
╭ [0] ╭ Target         : openaf/pyoaf:edge (alpine 3.23.4) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-40930 
│                       │      ├ PkgID           : libpng@1.6.57-r0 
│                       │      ├ PkgName         : libpng 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libpng@1.6.57-r0?arch=x86_64&distro=3.
│                       │      │                  │       23.4 
│                       │      │                  ╰ UID : a1a14f8b116541c1 
│                       │      ├ InstalledVersion: 1.6.57-r0 
│                       │      ├ FixedVersion    : 1.6.58-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40930 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:4ace03d8ab33da8d0257b3ccb605add4585494e8d3c251af9b618
│                       │      │                   7736b02d4d1 
│                       │      ╰ Severity        : UNKNOWN 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-22016 
│                       │      ├ PkgID           : openjdk21-jre@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.10_p7-r0?arch=x86_6
│                       │      │                  │       4&distro=3.23.4 
│                       │      │                  ╰ UID : 7775cc54b6be71ba 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22016 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:3c62c9f7f8e06032dde3e7f288c4cb270fa9a96dd9b587a6387a8
│                       │      │                   12bea11ed01 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance Path Factories Redux (Oracle CPU
│                       │      │                   2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JAXP).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 8u481, 8u481-b50, 8u481-perf, 11.0.30,
│                       │      │                   17.0.18, 21.0.10, 25.0.2, 26; Oracle GraalVM for JDK:
│                       │      │                   17.0.18 and  21.0.10; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.17. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized access to
│                       │      │                   critical data or complete access to all Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability can be exploited
│                       │      │                   by using APIs in the specified Component, e.g., through a
│                       │      │                   web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 7.5
│                       │      │                   (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ╭ [0]: CWE-200 
│                       │      │                  ╰ [1]: CWE-502 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                  │         │           N/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                            │           N/A:N 
│                       │      │                            ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-22016 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-22016.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-22016 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-22016 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:28.47Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:16:20.87Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-34282 
│                       │      ├ PkgID           : openjdk21-jre@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.10_p7-r0?arch=x86_6
│                       │      │                  │       4&distro=3.23.4 
│                       │      │                  ╰ UID : 7775cc54b6be71ba 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-34282 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:f5a84eec983ea7bf59138f1ba25b577a2d7824441cbe9f2e4b718
│                       │      │                   33f16d24646 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance TLS connection handling (Oracle
│                       │      │                   CPU 2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Networking).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u481-perf, 11.0.30, 17.0.18,
│                       │      │                   21.0.10, 25.0.2, 26; Oracle GraalVM for JDK: 17.0.18 and 
│                       │      │                   21.0.10; Oracle GraalVM Enterprise Edition: 21.3.17. Easily
│                       │      │                   exploitable vulnerability allows unauthenticated attacker
│                       │      │                   with network access via multiple protocols to compromise
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   hang or frequently repeatable crash (complete DOS) of Oracle
│                       │      │                    Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability can be exploited by using
│                       │      │                   APIs in the specified Component, e.g., through a web service
│                       │      │                    which supplies data to the APIs. This vulnerability also
│                       │      │                   applies to Java deployments, typically in clients running
│                       │      │                   sandboxed Java Web Start applications or sandboxed Java
│                       │      │                   applets, that load and run untrusted code (e.g., code that
│                       │      │                   comes from the internet) and rely on the Java sandbox for
│                       │      │                   security. CVSS 3.1 Base Score 7.5 (Availability impacts). 
│                       │      │                   CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-400 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:H 
│                       │      │                            ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-34282 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-34282.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-34282 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-34282 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:32.643Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:20:14.86Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-22013 
│                       │      ├ PkgID           : openjdk21-jre@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.10_p7-r0?arch=x86_6
│                       │      │                  │       4&distro=3.23.4 
│                       │      │                  ╰ UID : 7775cc54b6be71ba 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22013 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:98e55f4083bb6a2a969992e50a40e1b6f55acd04155c0b6526958
│                       │      │                   a11b116af69 
│                       │      ├ Title           : openjdk: OpenJDK: Improve Kerberos credentialing (Oracle CPU
│                       │      │                    2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JGSS).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 8u481, 8u481-b50, 8u481-perf, 11.0.30,
│                       │      │                   17.0.18, 21.0.10, 25.0.2, 26; Oracle GraalVM for JDK:
│                       │      │                   17.0.18 and  21.0.10; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.17. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   require human interaction from a person other than the
│                       │      │                   attacker. Successful attacks of this vulnerability can
│                       │      │                   result in  unauthorized access to critical data or complete
│                       │      │                   access to all Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                    GraalVM Enterprise Edition accessible data. Note: This
│                       │      │                   vulnerability applies to Java deployments, typically in
│                       │      │                   clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. This vulnerability does not apply
│                       │      │                    to Java deployments, typically in servers, that load and
│                       │      │                   run only trusted code (e.g., code installed by an
│                       │      │                   administrator). CVSS 3.1 Base Score 5.3 (Confidentiality
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:N/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-693 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:
│                       │      │                  │         │           N/A:N 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:
│                       │      │                            │           N/A:N 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-22013 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-22013.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-22013 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-22013 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:27.923Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:15:33.847Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-22021 
│                       │      ├ PkgID           : openjdk21-jre@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.10_p7-r0?arch=x86_6
│                       │      │                  │       4&distro=3.23.4 
│                       │      │                  ╰ UID : 7775cc54b6be71ba 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22021 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:be516f6765bdbc183369ca3baad70d038f7d7072c2d31cec8d02d
│                       │      │                   5487ba22cbb 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance certificate chain validation
│                       │      │                   (Oracle CPU 2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 8u481, 8u481-b50, 8u481-perf, 11.0.30,
│                       │      │                   17.0.18, 21.0.10, 25.0.2, 26; Oracle GraalVM for JDK:
│                       │      │                   17.0.18 and  21.0.10; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.17. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via HTTPS to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 5.3 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-400 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-22021 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-22021.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-22021 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-22021 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:29.193Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:18:05.093Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-23865 
│                       │      ├ PkgID           : openjdk21-jre@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.10_p7-r0?arch=x86_6
│                       │      │                  │       4&distro=3.23.4 
│                       │      │                  ╰ UID : 7775cc54b6be71ba 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-23865 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:62a78a64b87b62e25b4b52c4870bdcd6aa003d9b6db831ed282ff
│                       │      │                   fb8f4089b91 
│                       │      ├ Title           : freetype: Freetype: Information disclosure or denial of
│                       │      │                   service via specially crafted font files 
│                       │      ├ Description     : An integer overflow in the tt_var_load_item_variation_store
│                       │      │                   function of the Freetype library in versions 2.13.2 and
│                       │      │                   2.13.3 may allow for an out of bounds read operation when
│                       │      │                   parsing HVAR/VVAR/MVAR tables in OpenType variable fonts.
│                       │      │                   This issue is fixed in version 2.14.2. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-125 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ julia      : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:
│                       │      │                  │         │           L/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ├ julia   ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:
│                       │      │                  │         │           L/A:L/E:U/RL:O/RC:C 
│                       │      │                  │         ╰ V3Score : 4.6 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:
│                       │      │                            │           L/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2026/03/03/8 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2026-23865 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [18]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [19]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [20]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [21]: https://github.com/advisories/GHSA-878v-mxg6-vj8f 
│                       │      │                  ├ [22]: https://gitlab.com/freetype/freetype/-/commit/fc85a25
│                       │      │                  │       5849229c024c8e65f536fe1875d84841c 
│                       │      │                  ├ [23]: https://linux.oracle.com/cve/CVE-2026-23865.html 
│                       │      │                  ├ [24]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [25]: https://nvd.nist.gov/vuln/detail/CVE-2026-23865 
│                       │      │                  ├ [26]: https://sourceforge.net/projects/freetype/files/freet
│                       │      │                  │       ype2/2.14.2 
│                       │      │                  ├ [27]: https://sourceforge.net/projects/freetype/files/freet
│                       │      │                  │       ype2/2.14.2/ 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-8086-1 
│                       │      │                  ├ [29]: https://www.cve.org/CVERecord?id=CVE-2026-23865 
│                       │      │                  ├ [30]: https://www.facebook.com/security/advisories/cve-2026
│                       │      │                  │       -23865 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-03-02T17:16:32.1Z 
│                       │      ╰ LastModifiedDate: 2026-05-01T17:41:13.433Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-22007 
│                       │      ├ PkgID           : openjdk21-jre@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.10_p7-r0?arch=x86_6
│                       │      │                  │       4&distro=3.23.4 
│                       │      │                  ╰ UID : 7775cc54b6be71ba 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22007 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:15c7a6486d9922bb2da5875db3cdfd7e4225ed505657cb2af76be
│                       │      │                   135114a8155 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance crypto algorithm support (Oracle
│                       │      │                   CPU 2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u481, 8u481-b50, 8u481-perf,
│                       │      │                   11.0.30, 17.0.18, 21.0.10, 25.0.2, 26; Oracle GraalVM for
│                       │      │                   JDK: 17.0.18 and  21.0.10; Oracle GraalVM Enterprise
│                       │      │                   Edition: 21.3.17. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with logon to the infrastructure
│                       │      │                   where Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                    Enterprise Edition executes to compromise Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized read access to a subset of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability can be exploited
│                       │      │                   by using APIs in the specified Component, e.g., through a
│                       │      │                   web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 2.9
│                       │      │                   (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-200 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:
│                       │      │                  │         │           N/A:N 
│                       │      │                  │         ╰ V3Score : 2.9 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:
│                       │      │                            │           N/A:N 
│                       │      │                            ╰ V3Score : 2.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-22007 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-22007.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-22007 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-22007 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:26.44Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:14:24.013Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-22018 
│                       │      ├ PkgID           : openjdk21-jre@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.10_p7-r0?arch=x86_6
│                       │      │                  │       4&distro=3.23.4 
│                       │      │                  ╰ UID : 7775cc54b6be71ba 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22018 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:5137f0d972b9b90516302f10d46a7e4c71af2506771686f6382e5
│                       │      │                   64c64ceb542 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance Zip file reading (Oracle CPU
│                       │      │                   2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Libraries).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u481, 8u481-b50, 8u481-perf,
│                       │      │                   11.0.30, 17.0.18, 21.0.10, 25.0.2, 26; Oracle GraalVM for
│                       │      │                   JDK: 17.0.18 and  21.0.10; Oracle GraalVM Enterprise
│                       │      │                   Edition: 21.3.17. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in unauthorized ability to
│                       │      │                   cause a partial denial of service (partial DOS) of Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability can be exploited by using
│                       │      │                   APIs in the specified Component, e.g., through a web service
│                       │      │                    which supplies data to the APIs. This vulnerability also
│                       │      │                   applies to Java deployments, typically in clients running
│                       │      │                   sandboxed Java Web Start applications or sandboxed Java
│                       │      │                   applets, that load and run untrusted code (e.g., code that
│                       │      │                   comes from the internet) and rely on the Java sandbox for
│                       │      │                   security. CVSS 3.1 Base Score 3.7 (Availability impacts). 
│                       │      │                   CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 3.7 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-22018 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-22018.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-22018 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-22018 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:28.833Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:17:18.483Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-34268 
│                       │      ├ PkgID           : openjdk21-jre@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.10_p7-r0?arch=x86_6
│                       │      │                  │       4&distro=3.23.4 
│                       │      │                  ╰ UID : 7775cc54b6be71ba 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-34268 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:28f0e466aef019a939284768b90e01be52d39a34d24341a57910c
│                       │      │                   f5a6c7b04ab 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance key generation (Oracle CPU 2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u481, 8u481-b50, 8u481-perf,
│                       │      │                   11.0.30, 17.0.18, 21.0.10, 25.0.2, 26; Oracle GraalVM for
│                       │      │                   JDK: 17.0.18 and  21.0.10; Oracle GraalVM Enterprise
│                       │      │                   Edition: 21.3.17. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with logon to the infrastructure
│                       │      │                   where Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                    Enterprise Edition executes to compromise Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized read access to a subset of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability can be exploited
│                       │      │                   by using APIs in the specified Component, e.g., through a
│                       │      │                   web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 2.9
│                       │      │                   (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-200 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:
│                       │      │                  │         │           N/A:N 
│                       │      │                  │         ╰ V3Score : 2.9 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:
│                       │      │                            │           N/A:N 
│                       │      │                            ╰ V3Score : 2.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-34268 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-34268.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-34268 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-34268 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:30.353Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:19:01.973Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-22016 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.10_p7-r0?a
│                       │      │                  │       rch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : ac9a6ccdba670539 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22016 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:6ebd478263f7d9cecb8263e9e2b5b1e91f05b1da3480053864a32
│                       │      │                   aa431690ca2 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance Path Factories Redux (Oracle CPU
│                       │      │                   2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JAXP).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 8u481, 8u481-b50, 8u481-perf, 11.0.30,
│                       │      │                   17.0.18, 21.0.10, 25.0.2, 26; Oracle GraalVM for JDK:
│                       │      │                   17.0.18 and  21.0.10; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.17. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized access to
│                       │      │                   critical data or complete access to all Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability can be exploited
│                       │      │                   by using APIs in the specified Component, e.g., through a
│                       │      │                   web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 7.5
│                       │      │                   (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ╭ [0]: CWE-200 
│                       │      │                  ╰ [1]: CWE-502 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                  │         │           N/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                            │           N/A:N 
│                       │      │                            ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-22016 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-22016.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-22016 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-22016 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:28.47Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:16:20.87Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-34282 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.10_p7-r0?a
│                       │      │                  │       rch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : ac9a6ccdba670539 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-34282 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:66a5003b7391662737424e51ac01d8e068e9dd886daf0e2831fbc
│                       │      │                   c2f14a1871c 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance TLS connection handling (Oracle
│                       │      │                   CPU 2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Networking).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u481-perf, 11.0.30, 17.0.18,
│                       │      │                   21.0.10, 25.0.2, 26; Oracle GraalVM for JDK: 17.0.18 and 
│                       │      │                   21.0.10; Oracle GraalVM Enterprise Edition: 21.3.17. Easily
│                       │      │                   exploitable vulnerability allows unauthenticated attacker
│                       │      │                   with network access via multiple protocols to compromise
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   hang or frequently repeatable crash (complete DOS) of Oracle
│                       │      │                    Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability can be exploited by using
│                       │      │                   APIs in the specified Component, e.g., through a web service
│                       │      │                    which supplies data to the APIs. This vulnerability also
│                       │      │                   applies to Java deployments, typically in clients running
│                       │      │                   sandboxed Java Web Start applications or sandboxed Java
│                       │      │                   applets, that load and run untrusted code (e.g., code that
│                       │      │                   comes from the internet) and rely on the Java sandbox for
│                       │      │                   security. CVSS 3.1 Base Score 7.5 (Availability impacts). 
│                       │      │                   CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-400 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:H 
│                       │      │                            ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-34282 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-34282.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-34282 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-34282 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:32.643Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:20:14.86Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-22013 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.10_p7-r0?a
│                       │      │                  │       rch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : ac9a6ccdba670539 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22013 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8d532bce5b2f93ec139001eb1cece086d508e3150599ac5e1feac
│                       │      │                   56bb1652507 
│                       │      ├ Title           : openjdk: OpenJDK: Improve Kerberos credentialing (Oracle CPU
│                       │      │                    2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JGSS).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 8u481, 8u481-b50, 8u481-perf, 11.0.30,
│                       │      │                   17.0.18, 21.0.10, 25.0.2, 26; Oracle GraalVM for JDK:
│                       │      │                   17.0.18 and  21.0.10; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.17. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   require human interaction from a person other than the
│                       │      │                   attacker. Successful attacks of this vulnerability can
│                       │      │                   result in  unauthorized access to critical data or complete
│                       │      │                   access to all Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                    GraalVM Enterprise Edition accessible data. Note: This
│                       │      │                   vulnerability applies to Java deployments, typically in
│                       │      │                   clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. This vulnerability does not apply
│                       │      │                    to Java deployments, typically in servers, that load and
│                       │      │                   run only trusted code (e.g., code installed by an
│                       │      │                   administrator). CVSS 3.1 Base Score 5.3 (Confidentiality
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:N/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-693 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:
│                       │      │                  │         │           N/A:N 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:
│                       │      │                            │           N/A:N 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-22013 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-22013.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-22013 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-22013 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:27.923Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:15:33.847Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-22021 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.10_p7-r0?a
│                       │      │                  │       rch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : ac9a6ccdba670539 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22021 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:291cc24ff19a4cc6b3b6fc794fbc1a03eddd17763963f41932978
│                       │      │                   2531dd9bcb4 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance certificate chain validation
│                       │      │                   (Oracle CPU 2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 8u481, 8u481-b50, 8u481-perf, 11.0.30,
│                       │      │                   17.0.18, 21.0.10, 25.0.2, 26; Oracle GraalVM for JDK:
│                       │      │                   17.0.18 and  21.0.10; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.17. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via HTTPS to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 5.3 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-400 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-22021 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-22021.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-22021 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-22021 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:29.193Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:18:05.093Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-23865 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.10_p7-r0?a
│                       │      │                  │       rch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : ac9a6ccdba670539 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-23865 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:feb9e8509e0603aaabd106bfe66c298759fbcbcdd96f97ccf6390
│                       │      │                   0ec3e19c73a 
│                       │      ├ Title           : freetype: Freetype: Information disclosure or denial of
│                       │      │                   service via specially crafted font files 
│                       │      ├ Description     : An integer overflow in the tt_var_load_item_variation_store
│                       │      │                   function of the Freetype library in versions 2.13.2 and
│                       │      │                   2.13.3 may allow for an out of bounds read operation when
│                       │      │                   parsing HVAR/VVAR/MVAR tables in OpenType variable fonts.
│                       │      │                   This issue is fixed in version 2.14.2. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-125 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ julia      : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:
│                       │      │                  │         │           L/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ├ julia   ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:
│                       │      │                  │         │           L/A:L/E:U/RL:O/RC:C 
│                       │      │                  │         ╰ V3Score : 4.6 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:
│                       │      │                            │           L/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2026/03/03/8 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2026-23865 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [18]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [19]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [20]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [21]: https://github.com/advisories/GHSA-878v-mxg6-vj8f 
│                       │      │                  ├ [22]: https://gitlab.com/freetype/freetype/-/commit/fc85a25
│                       │      │                  │       5849229c024c8e65f536fe1875d84841c 
│                       │      │                  ├ [23]: https://linux.oracle.com/cve/CVE-2026-23865.html 
│                       │      │                  ├ [24]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [25]: https://nvd.nist.gov/vuln/detail/CVE-2026-23865 
│                       │      │                  ├ [26]: https://sourceforge.net/projects/freetype/files/freet
│                       │      │                  │       ype2/2.14.2 
│                       │      │                  ├ [27]: https://sourceforge.net/projects/freetype/files/freet
│                       │      │                  │       ype2/2.14.2/ 
│                       │      │                  ├ [28]: https://ubuntu.com/security/notices/USN-8086-1 
│                       │      │                  ├ [29]: https://www.cve.org/CVERecord?id=CVE-2026-23865 
│                       │      │                  ├ [30]: https://www.facebook.com/security/advisories/cve-2026
│                       │      │                  │       -23865 
│                       │      │                  ╰ [31]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-03-02T17:16:32.1Z 
│                       │      ╰ LastModifiedDate: 2026-05-01T17:41:13.433Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-22007 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.10_p7-r0?a
│                       │      │                  │       rch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : ac9a6ccdba670539 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22007 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:80dfdeedd7b2e79270505bd4ee75dcb6e74aadc5692decfcbea35
│                       │      │                   00dfd7bb4e2 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance crypto algorithm support (Oracle
│                       │      │                   CPU 2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u481, 8u481-b50, 8u481-perf,
│                       │      │                   11.0.30, 17.0.18, 21.0.10, 25.0.2, 26; Oracle GraalVM for
│                       │      │                   JDK: 17.0.18 and  21.0.10; Oracle GraalVM Enterprise
│                       │      │                   Edition: 21.3.17. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with logon to the infrastructure
│                       │      │                   where Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                    Enterprise Edition executes to compromise Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized read access to a subset of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability can be exploited
│                       │      │                   by using APIs in the specified Component, e.g., through a
│                       │      │                   web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 2.9
│                       │      │                   (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-200 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:
│                       │      │                  │         │           N/A:N 
│                       │      │                  │         ╰ V3Score : 2.9 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:
│                       │      │                            │           N/A:N 
│                       │      │                            ╰ V3Score : 2.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-22007 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-22007.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-22007 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-22007 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:26.44Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:14:24.013Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-22018 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.10_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.10_p7-r0?a
│                       │      │                  │       rch=x86_64&distro=3.23.4 
│                       │      │                  ╰ UID : ac9a6ccdba670539 
│                       │      ├ InstalledVersion: 21.0.10_p7-r0 
│                       │      ├ FixedVersion    : 21.0.11_p10-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                       │      │                  │         dcee783029a1e52067bb 
│                       │      │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                       │      │                            f9415ddf41f5a2533835 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22018 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e7a5fcd9eb0fd94d07e7a1ecbe6e56edbdee0b13761f882fb9aa0
│                       │      │                   52c513d4ea3 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance Zip file reading (Oracle CPU
│                       │      │                   2026-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Libraries).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u481, 8u481-b50, 8u481-perf,
│                       │      │                   11.0.30, 17.0.18, 21.0.10, 25.0.2, 26; Oracle GraalVM for
│                       │      │                   JDK: 17.0.18 and  21.0.10; Oracle GraalVM Enterprise
│                       │      │                   Edition: 21.3.17. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in unauthorized ability to
│                       │      │                   cause a partial denial of service (partial DOS) of Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. Note: This vulnerability can be exploited by using
│                       │      │                   APIs in the specified Component, e.g., through a web service
│                       │      │                    which supplies data to the APIs. This vulnerability also
│                       │      │                   applies to Java deployments, typically in clients running
│                       │      │                   sandboxed Java Web Start applications or sandboxed Java
│                       │      │                   applets, that load and run untrusted code (e.g., code that
│                       │      │                   comes from the internet) and rely on the Java sandbox for
│                       │      │                   security. CVSS 3.1 Base Score 3.7 (Availability impacts). 
│                       │      │                   CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 3.7 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-22018 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22007 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22013 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22016 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22018 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-22021 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-23865 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34268 
│                       │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-34282 
│                       │      │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                       │      │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                       │      │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-22018.html 
│                       │      │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                       │      │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-22018 
│                       │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-22018 
│                       │      │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                       │      │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2026-04-21T21:16:28.833Z 
│                       │      ╰ LastModifiedDate: 2026-04-27T12:17:18.483Z 
│                       ╰ [16] ╭ VulnerabilityID : CVE-2026-34268 
│                              ├ PkgID           : openjdk21-jre-headless@21.0.10_p7-r0 
│                              ├ PkgName         : openjdk21-jre-headless 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.10_p7-r0?a
│                              │                  │       rch=x86_64&distro=3.23.4 
│                              │                  ╰ UID : ac9a6ccdba670539 
│                              ├ InstalledVersion: 21.0.10_p7-r0 
│                              ├ FixedVersion    : 21.0.11_p10-r0 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:85d81298fb3243b0f0e90c0f2ddf0caa2d4f7a4b1de4
│                              │                  │         dcee783029a1e52067bb 
│                              │                  ╰ DiffID: sha256:bbd7047cee0551d66c4ccb8b24a2d008daa0ae516dc8
│                              │                            f9415ddf41f5a2533835 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-34268 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Fingerprint     : sha256:fe7e424886cdb9617443d1b3699616b532f55f59e2f5964b5c5f3
│                              │                   fffae3e8a99 
│                              ├ Title           : openjdk: OpenJDK: Enhance key generation (Oracle CPU 2026-04) 
│                              ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                              │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                              │                    (component: Security).  Supported versions that are
│                              │                   affected are Oracle Java SE: 8u481, 8u481-b50, 8u481-perf,
│                              │                   11.0.30, 17.0.18, 21.0.10, 25.0.2, 26; Oracle GraalVM for
│                              │                   JDK: 17.0.18 and  21.0.10; Oracle GraalVM Enterprise
│                              │                   Edition: 21.3.17. Difficult to exploit vulnerability allows
│                              │                   unauthenticated attacker with logon to the infrastructure
│                              │                   where Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                              │                    Enterprise Edition executes to compromise Oracle Java SE,
│                              │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                              │                   Successful attacks of this vulnerability can result in 
│                              │                   unauthorized read access to a subset of Oracle Java SE,
│                              │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                              │                   accessible data. Note: This vulnerability can be exploited
│                              │                   by using APIs in the specified Component, e.g., through a
│                              │                   web service which supplies data to the APIs. This
│                              │                   vulnerability also applies to Java deployments, typically in
│                              │                    clients running sandboxed Java Web Start applications or
│                              │                   sandboxed Java applets, that load and run untrusted code
│                              │                   (e.g., code that comes from the internet) and rely on the
│                              │                   Java sandbox for security. CVSS 3.1 Base Score 2.9
│                              │                   (Confidentiality impacts).  CVSS Vector:
│                              │                   (CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N). 
│                              ├ Severity        : LOW 
│                              ├ CweIDs           ─ [0]: CWE-200 
│                              ├ VendorSeverity   ╭ alma       : 3 
│                              │                  ├ amazon     : 3 
│                              │                  ├ bitnami    : 1 
│                              │                  ├ oracle-oval: 3 
│                              │                  ├ redhat     : 1 
│                              │                  ╰ rocky      : 3 
│                              ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:
│                              │                  │         │           N/A:N 
│                              │                  │         ╰ V3Score : 2.9 
│                              │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:L/I:
│                              │                            │           N/A:N 
│                              │                            ╰ V3Score : 2.9 
│                              ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9693 
│                              │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-34268 
│                              │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2443891 
│                              │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2460038 
│                              │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2460039 
│                              │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2460040 
│                              │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2460041 
│                              │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2460042 
│                              │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2460043 
│                              │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2460044 
│                              │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                              │                  │       26-22007 
│                              │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                              │                  │       26-22013 
│                              │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                              │                  │       26-22016 
│                              │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                              │                  │       26-22018 
│                              │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                              │                  │       26-22021 
│                              │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                              │                  │       26-23865 
│                              │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                              │                  │       26-34268 
│                              │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                              │                  │       26-34282 
│                              │                  ├ [18]: https://errata.almalinux.org/9/ALSA-2026-9693.html 
│                              │                  ├ [19]: https://errata.rockylinux.org/RLSA-2026:9689 
│                              │                  ├ [20]: https://linux.oracle.com/cve/CVE-2026-34268.html 
│                              │                  ├ [21]: https://linux.oracle.com/errata/ELSA-2026-9693.html 
│                              │                  ├ [22]: https://nvd.nist.gov/vuln/detail/CVE-2026-34268 
│                              │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2026-34268 
│                              │                  ├ [24]: https://www.oracle.com/security-alerts/cpuapr2026.html 
│                              │                  ╰ [25]: https://www.oracle.com/security-alerts/cpuapr2026.htm
│                              │                          l#AppendixJAVA 
│                              ├ PublishedDate   : 2026-04-21T21:16:30.353Z 
│                              ╰ LastModifiedDate: 2026-04-27T12:19:01.973Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages 
```
