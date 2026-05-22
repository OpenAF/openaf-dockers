```yaml
╭ [0] ╭ Target         : openaf/ojobrt:latest (alpine 3.23.4) 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40930 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:1362e6b5c95eef81151f3da04fdcec8de65586bfa6be3f3326962
│                       │      │                   92bb387493e 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22016 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:02b0c845875464a0cb2c59029e7e832dca42950e4b4ed998473a3
│                       │      │                   5ac9cb25abc 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-34282 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:2a89546361207fd467b4411664d370141d5379ca7e023022c1973
│                       │      │                   a938c33f06b 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22013 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8f6655057402fcaab19520fbedc7f8d56152fb89b91df655e4f1d
│                       │      │                   68fa5b6dc0d 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22021 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:5e52f16f69940691842a7e4718dcad0aaca890503c985b57c57ad
│                       │      │                   5ebb1518963 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-23865 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8b4413915d75268b96cfd48b375f0ab3f0cc5f9f03462a95f37cc
│                       │      │                   3c4cb66244d 
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
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [19]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22007 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:7f6d3514ee0bebcab1950acd1239aa8ed427f140c08b1d3a3e999
│                       │      │                   f44d9885202 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22018 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:753e167eae2d10f8d90c33fac8aa005e09615161bba1a579cb647
│                       │      │                   a4ea6cf6574 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-34268 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:94881365e6236b9e2aa2c9cb51b181271c4edf88f9e8563fb2fc4
│                       │      │                   33d365f9ae5 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22016 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:bcb9346ad32714e61ed6bc4c635b89dc12fad8e9cb24a52650b2a
│                       │      │                   8752a334af9 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-34282 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:465a760c65f585b7231cf0e7483bcf7569be8a82bb05a256b1725
│                       │      │                   57823752bf6 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22013 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:9ffb7cb3b65df02d097fea825405a5701690c9c931338da9bbf29
│                       │      │                   d888f227a4a 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22021 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e2686bf1371824e7c64e968787cc1205192507dfced8d198301d5
│                       │      │                   d1996295b0f 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-23865 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:2c7191cce1804b9e9e989a7225bc8e89e0c4413daf5618b67b447
│                       │      │                   354b7e08db1 
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
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [19]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22007 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8bf630d1a038241be60ea0c3dad47ef208e280e9a50b4024d9e8c
│                       │      │                   7edcb727b3c 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                       │      ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                       │      │                  │         ee30a5bf7d341c2b6100 
│                       │      │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                       │      │                            321c5536a30de88f45ce 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-22018 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:f8fbd00a587a62c6008962b25aae8676fd90f8b06719982729412
│                       │      │                   60204a1ce7c 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                       │      │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
│                              ├ Layer            ╭ Digest: sha256:0bfa2b35aa673dea8712cbdc25e211e81776cfb7b110
│                              │                  │         ee30a5bf7d341c2b6100 
│                              │                  ╰ DiffID: sha256:c06a9fa4447f95970767bb294272a759df82f34bc7a9
│                              │                            321c5536a30de88f45ce 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-34268 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Fingerprint     : sha256:279a2422cd0a8556d0fd3904adebb4be27b05ee76d83b96206393
│                              │                   bd9c00deec7 
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
│                              ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:9689 
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
│                              │                  ├ [18]: https://errata.almalinux.org/8/ALSA-2026-9689.html 
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
