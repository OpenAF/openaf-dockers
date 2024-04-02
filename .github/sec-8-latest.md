````yaml
╭ [0] ╭ Target         : openaf/oaf:8-latest (alpine 3.19.1) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2024-25629 
│                       │      ├ PkgID           : c-ares@1.24.0-r1 
│                       │      ├ PkgName         : c-ares 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/c-ares@1.24.0-r1?arch=x86_64&dist
│                       │      │                          ro=3.19.1 
│                       │      ├ InstalledVersion: 1.24.0-r1 
│                       │      ├ FixedVersion    : 1.27.0-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-25629 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : c-ares: Out of bounds read in ares__read_line() 
│                       │      ├ Description     : c-ares is a C library for asynchronous DNS requests.
│                       │      │                   `ares__read_line()` is used to parse local configuration
│                       │      │                   files such as `/etc/resolv.conf`, `/etc/nsswitch.conf`, the
│                       │      │                   `HOSTALIASES` file, and if using a c-ares version prior to
│                       │      │                   1.27.0, the `/etc/hosts` file. If any of these configuration
│                       │      │                    files has an embedded `NULL` character as the first
│                       │      │                   character in a new line, it can lead to attempting to read
│                       │      │                   memory prior to the start of the given buffer which may
│                       │      │                   result in a crash. This issue is fixed in c-ares 1.27.0. No
│                       │      │                   known workarounds exist. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-127 
│                       │      ├ VendorSeverity   ╭ amazon: 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:
│                       │      │                           │           N/I:N/A:H 
│                       │      │                           ╰ V3Score : 4.4 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-25629 
│                       │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
│                       │      │                  │      E-2024-25629 
│                       │      │                  ├ [2]: https://github.com/c-ares/c-ares/commit/a804c04dd
│                       │      │                  │      c8245fc8adf0e92368709639125e183 
│                       │      │                  ├ [3]: https://github.com/c-ares/c-ares/security/advisor
│                       │      │                  │      ies/GHSA-mg26-v6qh-x48q 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-25629 
│                       │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-6676-1 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2024-25629 
│                       │      ├ PublishedDate   : 2024-02-23T15:15:09.237Z 
│                       │      ╰ LastModifiedDate: 2024-02-23T16:14:43.447Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2024-20918 
│                       │      ├ PkgID           : openjdk8-jre@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre@8.392.08-r1?arch=x86
│                       │      │                          _64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20918 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: array out-of-bounds access due to missing
│                       │      │                   range check in C1 compiler (8314468) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Hotspot).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data as well as  unauthorized
│                       │      │                   access to critical data or complete access to all Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           H/I:H/A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20918 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20918 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20918.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
│                       │      │                  │       4/01/msg00023.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-20918 
│                       │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202402
│                       │      │                  │       01-0002/ 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [19]: https://www.cve.org/CVERecord?id=CVE-2024-20918 
│                       │      │                  ├ [20]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [21]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-01-16T22:15:39.51Z 
│                       │      ╰ LastModifiedDate: 2024-02-15T03:18:09.407Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2024-20952 
│                       │      ├ PkgID           : openjdk8-jre@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre@8.392.08-r1?arch=x86
│                       │      │                          _64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20952 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: RSA padding issue and timing side-channel
│                       │      │                   attack against TLS (8317547) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data as well as  unauthorized
│                       │      │                   access to critical data or complete access to all Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability applies to
│                       │      │                    Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. This
│                       │      │                   vulnerability does not apply to Java deployments, typically
│                       │      │                   in servers, that load and run only trusted code (e.g., code
│                       │      │                   installed by an administrator). CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           H/I:H/A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20952 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20952 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20952.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
│                       │      │                  │       4/01/msg00023.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-20952 
│                       │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202402
│                       │      │                  │       01-0002/ 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [19]: https://www.cve.org/CVERecord?id=CVE-2024-20952 
│                       │      │                  ├ [20]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [21]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-01-16T22:15:42.477Z 
│                       │      ╰ LastModifiedDate: 2024-02-15T03:18:31.14Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2024-20919 
│                       │      ├ PkgID           : openjdk8-jre@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre@8.392.08-r1?arch=x86
│                       │      │                          _64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20919 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: JVM class file verifier flaw allows unverified
│                       │      │                    bytecode execution (8314295) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Hotspot).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can only be exploited by supplying data to APIs in the
│                       │      │                   specified Component without using Untrusted Java Web Start
│                       │      │                   applications or Untrusted Java applets, such as through a
│                       │      │                   web service. CVSS 3.1 Base Score 5.9 (Integrity impacts). 
│                       │      │                   CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           N/I:H/A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20919 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20919 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20919.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-20919 
│                       │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-20919 
│                       │      │                  ├ [18]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [19]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-02-17T02:15:46.77Z 
│                       │      ╰ LastModifiedDate: 2024-02-20T19:51:05.51Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2024-20921 
│                       │      ├ PkgID           : openjdk8-jre@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre@8.392.08-r1?arch=x86
│                       │      │                          _64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20921 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: range check loop optimization issue (8314307) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Hotspot).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows
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
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 5.9
│                       │      │                   (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           H/I:N/A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20921 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20921 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20921.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-20921 
│                       │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-20921 
│                       │      │                  ├ [18]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [19]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-02-17T02:15:46.937Z 
│                       │      ╰ LastModifiedDate: 2024-02-20T19:51:05.51Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2024-20926 
│                       │      ├ PkgID           : openjdk8-jre@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre@8.392.08-r1?arch=x86
│                       │      │                          _64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20926 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: arbitrary Java code execution in Nashorn (8314284) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Scripting).  Supported versions that are
│                       │      │                    affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21;
│                       │      │                   Oracle GraalVM for JDK: 17.0.9; Oracle GraalVM Enterprise
│                       │      │                   Edition: 20.3.12, 21.3.8 and  22.3.4. Difficult to exploit
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via multiple protocols to compromise Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized access to critical data or complete access to
│                       │      │                   all Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   5.9 (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           H/I:N/A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0266 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20926 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257850 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20926 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0266.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20926.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0266.html 
│                       │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
│                       │      │                  │       4/01/msg00023.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-20926 
│                       │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202402
│                       │      │                  │       01-0002/ 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-20926 
│                       │      │                  ├ [18]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [19]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-01-16T22:15:40.207Z 
│                       │      ╰ LastModifiedDate: 2024-02-02T17:35:48.843Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2024-20945 
│                       │      ├ PkgID           : openjdk8-jre@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre@8.392.08-r1?arch=x86
│                       │      │                          _64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20945 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: logging of digital signature private keys (8316976) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows low
│                       │      │                   privileged attacker with logon to the infrastructure where
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition executes to compromise Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized access to critical data or complete access to
│                       │      │                   all Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   4.7 (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:
│                       │      │                           │           H/I:N/A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20945 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20945 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20945.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-20945 
│                       │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-20945 
│                       │      │                  ├ [18]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [19]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-02-17T02:15:48.88Z 
│                       │      ╰ LastModifiedDate: 2024-02-20T19:51:05.51Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2024-20918 
│                       │      ├ PkgID           : openjdk8-jre-base@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre-base@8.392.08-r1?arc
│                       │      │                          h=x86_64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20918 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: array out-of-bounds access due to missing
│                       │      │                   range check in C1 compiler (8314468) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Hotspot).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data as well as  unauthorized
│                       │      │                   access to critical data or complete access to all Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           H/I:H/A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20918 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20918 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20918.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
│                       │      │                  │       4/01/msg00023.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-20918 
│                       │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202402
│                       │      │                  │       01-0002/ 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [19]: https://www.cve.org/CVERecord?id=CVE-2024-20918 
│                       │      │                  ├ [20]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [21]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-01-16T22:15:39.51Z 
│                       │      ╰ LastModifiedDate: 2024-02-15T03:18:09.407Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2024-20952 
│                       │      ├ PkgID           : openjdk8-jre-base@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre-base@8.392.08-r1?arc
│                       │      │                          h=x86_64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20952 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: RSA padding issue and timing side-channel
│                       │      │                   attack against TLS (8317547) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data as well as  unauthorized
│                       │      │                   access to critical data or complete access to all Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability applies to
│                       │      │                    Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. This
│                       │      │                   vulnerability does not apply to Java deployments, typically
│                       │      │                   in servers, that load and run only trusted code (e.g., code
│                       │      │                   installed by an administrator). CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           H/I:H/A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20952 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20952 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20952.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
│                       │      │                  │       4/01/msg00023.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-20952 
│                       │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202402
│                       │      │                  │       01-0002/ 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [19]: https://www.cve.org/CVERecord?id=CVE-2024-20952 
│                       │      │                  ├ [20]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [21]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-01-16T22:15:42.477Z 
│                       │      ╰ LastModifiedDate: 2024-02-15T03:18:31.14Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2024-20919 
│                       │      ├ PkgID           : openjdk8-jre-base@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre-base@8.392.08-r1?arc
│                       │      │                          h=x86_64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20919 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: JVM class file verifier flaw allows unverified
│                       │      │                    bytecode execution (8314295) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Hotspot).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can only be exploited by supplying data to APIs in the
│                       │      │                   specified Component without using Untrusted Java Web Start
│                       │      │                   applications or Untrusted Java applets, such as through a
│                       │      │                   web service. CVSS 3.1 Base Score 5.9 (Integrity impacts). 
│                       │      │                   CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           N/I:H/A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20919 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20919 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20919.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-20919 
│                       │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-20919 
│                       │      │                  ├ [18]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [19]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-02-17T02:15:46.77Z 
│                       │      ╰ LastModifiedDate: 2024-02-20T19:51:05.51Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2024-20921 
│                       │      ├ PkgID           : openjdk8-jre-base@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre-base@8.392.08-r1?arc
│                       │      │                          h=x86_64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20921 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: range check loop optimization issue (8314307) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Hotspot).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows
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
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 5.9
│                       │      │                   (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           H/I:N/A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20921 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20921 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20921.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-20921 
│                       │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-20921 
│                       │      │                  ├ [18]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [19]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-02-17T02:15:46.937Z 
│                       │      ╰ LastModifiedDate: 2024-02-20T19:51:05.51Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2024-20926 
│                       │      ├ PkgID           : openjdk8-jre-base@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre-base@8.392.08-r1?arc
│                       │      │                          h=x86_64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20926 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: arbitrary Java code execution in Nashorn (8314284) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Scripting).  Supported versions that are
│                       │      │                    affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21;
│                       │      │                   Oracle GraalVM for JDK: 17.0.9; Oracle GraalVM Enterprise
│                       │      │                   Edition: 20.3.12, 21.3.8 and  22.3.4. Difficult to exploit
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via multiple protocols to compromise Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized access to critical data or complete access to
│                       │      │                   all Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   5.9 (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           H/I:N/A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0266 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20926 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257850 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20926 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0266.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20926.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0266.html 
│                       │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
│                       │      │                  │       4/01/msg00023.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-20926 
│                       │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202402
│                       │      │                  │       01-0002/ 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-20926 
│                       │      │                  ├ [18]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [19]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-01-16T22:15:40.207Z 
│                       │      ╰ LastModifiedDate: 2024-02-02T17:35:48.843Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2024-20945 
│                       │      ├ PkgID           : openjdk8-jre-base@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre-base 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre-base@8.392.08-r1?arc
│                       │      │                          h=x86_64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20945 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: logging of digital signature private keys (8316976) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows low
│                       │      │                   privileged attacker with logon to the infrastructure where
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition executes to compromise Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized access to critical data or complete access to
│                       │      │                   all Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   4.7 (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:
│                       │      │                           │           H/I:N/A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20945 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20945 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20945.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-20945 
│                       │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-20945 
│                       │      │                  ├ [18]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [19]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-02-17T02:15:48.88Z 
│                       │      ╰ LastModifiedDate: 2024-02-20T19:51:05.51Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2024-20918 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.392.08-r1?arch
│                       │      │                          =x86_64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20918 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: array out-of-bounds access due to missing
│                       │      │                   range check in C1 compiler (8314468) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Hotspot).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data as well as  unauthorized
│                       │      │                   access to critical data or complete access to all Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           H/I:H/A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20918 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20918 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20918.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
│                       │      │                  │       4/01/msg00023.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-20918 
│                       │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202402
│                       │      │                  │       01-0002/ 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [19]: https://www.cve.org/CVERecord?id=CVE-2024-20918 
│                       │      │                  ├ [20]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [21]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-01-16T22:15:39.51Z 
│                       │      ╰ LastModifiedDate: 2024-02-15T03:18:09.407Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2024-20952 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.392.08-r1?arch
│                       │      │                          =x86_64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20952 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: RSA padding issue and timing side-channel
│                       │      │                   attack against TLS (8317547) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data as well as  unauthorized
│                       │      │                   access to critical data or complete access to all Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability applies to
│                       │      │                    Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. This
│                       │      │                   vulnerability does not apply to Java deployments, typically
│                       │      │                   in servers, that load and run only trusted code (e.g., code
│                       │      │                   installed by an administrator). CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           H/I:H/A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20952 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20952 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20952.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
│                       │      │                  │       4/01/msg00023.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-20952 
│                       │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202402
│                       │      │                  │       01-0002/ 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [19]: https://www.cve.org/CVERecord?id=CVE-2024-20952 
│                       │      │                  ├ [20]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [21]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-01-16T22:15:42.477Z 
│                       │      ╰ LastModifiedDate: 2024-02-15T03:18:31.14Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2024-20919 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.392.08-r1?arch
│                       │      │                          =x86_64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20919 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: JVM class file verifier flaw allows unverified
│                       │      │                    bytecode execution (8314295) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Hotspot).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can only be exploited by supplying data to APIs in the
│                       │      │                   specified Component without using Untrusted Java Web Start
│                       │      │                   applications or Untrusted Java applets, such as through a
│                       │      │                   web service. CVSS 3.1 Base Score 5.9 (Integrity impacts). 
│                       │      │                   CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           N/I:H/A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20919 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20919 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20919.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-20919 
│                       │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-20919 
│                       │      │                  ├ [18]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [19]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-02-17T02:15:46.77Z 
│                       │      ╰ LastModifiedDate: 2024-02-20T19:51:05.51Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2024-20921 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.392.08-r1?arch
│                       │      │                          =x86_64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20921 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: range check loop optimization issue (8314307) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Hotspot).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                       │      │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                       │      │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                       │      │                   22.3.4. Difficult to exploit vulnerability allows
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
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 5.9
│                       │      │                   (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           H/I:N/A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20921 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20921 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20921.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-20921 
│                       │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6661-1 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6662-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-20921 
│                       │      │                  ├ [18]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [19]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-02-17T02:15:46.937Z 
│                       │      ╰ LastModifiedDate: 2024-02-20T19:51:05.51Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2024-20926 
│                       │      ├ PkgID           : openjdk8-jre-lib@8.392.08-r1 
│                       │      ├ PkgName         : openjdk8-jre-lib 
│                       │      ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.392.08-r1?arch
│                       │      │                          =x86_64&distro=3.19.1 
│                       │      ├ InstalledVersion: 8.392.08-r1 
│                       │      ├ FixedVersion    : 8.402.06-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                       │      │                  │         72c2033bd2f960470c478ec64 
│                       │      │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                       │      │                            7431737375dd9905f5165a736 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20926 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : OpenJDK: arbitrary Java code execution in Nashorn (8314284) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                       │      │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                       │      │                   Java SE (component: Scripting).  Supported versions that are
│                       │      │                    affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21;
│                       │      │                   Oracle GraalVM for JDK: 17.0.9; Oracle GraalVM Enterprise
│                       │      │                   Edition: 20.3.12, 21.3.8 and  22.3.4. Difficult to exploit
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via multiple protocols to compromise Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized access to critical data or complete access to
│                       │      │                   all Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   5.9 (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
│                       │      │                           │           H/I:N/A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0266 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20926 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2257728 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2257837 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2257850 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                       │      │                  │       VE-2024-20926 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0266.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20926.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0266.html 
│                       │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
│                       │      │                  │       4/01/msg00023.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-20926 
│                       │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202402
│                       │      │                  │       01-0002/ 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6660-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6696-1 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-20926 
│                       │      │                  ├ [18]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                  │       4.html 
│                       │      │                  ╰ [19]: https://www.oracle.com/security-alerts/cpujan202
│                       │      │                          4.html#AppendixJAVA 
│                       │      ├ PublishedDate   : 2024-01-16T22:15:40.207Z 
│                       │      ╰ LastModifiedDate: 2024-02-02T17:35:48.843Z 
│                       ╰ [18] ╭ VulnerabilityID : CVE-2024-20945 
│                              ├ PkgID           : openjdk8-jre-lib@8.392.08-r1 
│                              ├ PkgName         : openjdk8-jre-lib 
│                              ├ PkgIdentifier    ─ PURL: pkg:apk/alpine/openjdk8-jre-lib@8.392.08-r1?arch
│                              │                          =x86_64&distro=3.19.1 
│                              ├ InstalledVersion: 8.392.08-r1 
│                              ├ FixedVersion    : 8.402.06-r0 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d2
│                              │                  │         72c2033bd2f960470c478ec64 
│                              │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c979
│                              │                            7431737375dd9905f5165a736 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-20945 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Title           : OpenJDK: logging of digital signature private keys (8316976) 
│                              ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for
│                              │                    JDK, Oracle GraalVM Enterprise Edition product of Oracle
│                              │                   Java SE (component: Security).  Supported versions that are
│                              │                   affected are Oracle Java SE: 8u391, 8u391-perf, 11.0.21,
│                              │                   17.0.9, 21.0.1; Oracle GraalVM for JDK: 17.0.9, 21.0.1;
│                              │                   Oracle GraalVM Enterprise Edition: 20.3.12, 21.3.8 and 
│                              │                   22.3.4. Difficult to exploit vulnerability allows low
│                              │                   privileged attacker with logon to the infrastructure where
│                              │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                              │                   Enterprise Edition executes to compromise Oracle Java SE,
│                              │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                              │                   Successful attacks of this vulnerability can result in 
│                              │                   unauthorized access to critical data or complete access to
│                              │                   all Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                              │                   Enterprise Edition accessible data. Note: This vulnerability
│                              │                    can be exploited by using APIs in the specified Component,
│                              │                   e.g., through a web service which supplies data to the APIs.
│                              │                    This vulnerability also applies to Java deployments,
│                              │                   typically in clients running sandboxed Java Web Start
│                              │                   applications or sandboxed Java applets, that load and run
│                              │                   untrusted code (e.g., code that comes from the internet) and
│                              │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                              │                   4.7 (Confidentiality impacts).  CVSS Vector:
│                              │                   (CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N). 
│                              ├ Severity        : MEDIUM 
│                              ├ VendorSeverity   ╭ alma       : 3 
│                              │                  ├ amazon     : 3 
│                              │                  ├ oracle-oval: 3 
│                              │                  ├ redhat     : 2 
│                              │                  ╰ ubuntu     : 2 
│                              ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:
│                              │                           │           H/I:N/A:N 
│                              │                           ╰ V3Score : 4.7 
│                              ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:0267 
│                              │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-20945 
│                              │                  ├ [2] : https://bugzilla.redhat.com/2257720 
│                              │                  ├ [3] : https://bugzilla.redhat.com/2257728 
│                              │                  ├ [4] : https://bugzilla.redhat.com/2257837 
│                              │                  ├ [5] : https://bugzilla.redhat.com/2257853 
│                              │                  ├ [6] : https://bugzilla.redhat.com/2257859 
│                              │                  ├ [7] : https://bugzilla.redhat.com/2257874 
│                              │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
│                              │                  │       VE-2024-20945 
│                              │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-0267.html 
│                              │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-20945.html 
│                              │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0267.html 
│                              │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-20945 
│                              │                  ├ [13]: https://ubuntu.com/security/notices/USN-6660-1 
│                              │                  ├ [14]: https://ubuntu.com/security/notices/USN-6661-1 
│                              │                  ├ [15]: https://ubuntu.com/security/notices/USN-6662-1 
│                              │                  ├ [16]: https://ubuntu.com/security/notices/USN-6696-1 
│                              │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2024-20945 
│                              │                  ├ [18]: https://www.oracle.com/security-alerts/cpujan202
│                              │                  │       4.html 
│                              │                  ╰ [19]: https://www.oracle.com/security-alerts/cpujan202
│                              │                          4.html#AppendixJAVA 
│                              ├ PublishedDate   : 2024-02-17T02:15:48.88Z 
│                              ╰ LastModifiedDate: 2024-02-20T19:51:05.51Z 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2024-31033 
                              ├ PkgName         : io.jsonwebtoken:jjwt-impl 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ PkgIdentifier    ─ PURL: pkg:maven/io.jsonwebtoken/jjwt-impl@0.12.5 
                              ├ InstalledVersion: 0.12.5 
                              ├ Status          : affected 
                              ├ Layer            ╭ Digest: sha256:604414ded2530e1bdd4d78f5a447f422d0ec7d27
                              │                  │         2c2033bd2f960470c478ec64 
                              │                  ╰ DiffID: sha256:ebd52dbab23b79a601f35d7b3509191dcd5c9797
                              │                            431737375dd9905f5165a736 
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
