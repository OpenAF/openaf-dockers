```yaml
╭ [0] ╭ Target         : openaf/pyoaf:edge (alpine 3.24.1) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-41254 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-41254 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:fcd6037121c90aa3895af25b0628c0af5d2e112785d0ad5595d14
│                       │      │                   66790c3a5ee 
│                       │      ├ Title           : Little CMS: lcms2: mm2/Little-CMS: Little CMS: Information
│                       │      │                   disclosure or denial of service via integer overflow in
│                       │      │                   CubeSize 
│                       │      ├ Description     : Little CMS (lcms2) through 2.18 has an integer overflow in
│                       │      │                   CubeSize in cmslut.c because the overflow check is performed
│                       │      │                    after the multiplication. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ╭ [0]: CWE-696 
│                       │      │                  ╰ [1]: CWE-190 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ julia      : 3 
│                       │      │                  ├ nvd        : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.5 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.1 
│                       │      ├ References       ╭ [0] : https://abhinavagarwal07.github.io/posts/lcms2-cubesi
│                       │      │                  │       ze-overflow/ 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2026-41254 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [20]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [29]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [30]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://github.com/mm2/Little-CMS/commit/da6110b1d14a
│                       │      │                  │       bc394633a388209abd5ebedd7ab0 
│                       │      │                  ├ [33]: https://github.com/mm2/Little-CMS/commit/e0641b1828d0
│                       │      │                  │       a1af5ecb1b11fe22f24fceefd4bc 
│                       │      │                  ├ [34]: https://github.com/mm2/Little-CMS/security/advisories
│                       │      │                  │       /GHSA-4xp6-rcgg-m9qq 
│                       │      │                  ├ [35]: https://linux.oracle.com/cve/CVE-2026-41254.html 
│                       │      │                  ├ [36]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [37]: https://lists.debian.org/debian-lts-announce/2026/05/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [38]: https://nvd.nist.gov/vuln/detail/CVE-2026-41254 
│                       │      │                  ├ [39]: https://ubuntu.com/security/notices/USN-8209-1 
│                       │      │                  ├ [40]: https://ubuntu.com/security/notices/USN-8209-2 
│                       │      │                  ├ [41]: https://www.cve.org/CVERecord?id=CVE-2026-41254 
│                       │      │                  ╰ [42]: https://www.openwall.com/lists/oss-security/2026/04/1
│                       │      │                          7/16 
│                       │      ├ PublishedDate   : 2026-04-18T07:16:10.807Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:46:23.47Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-47063 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47063 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:76c3c34f71ec437f06a67e5764d374d956d0e8943a736a7cf9c67
│                       │      │                   96c14a6c9bc 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance Jar handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Libraries).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u491, 8u491-perf, 11.0.31,
│                       │      │                   17.0.19, 21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK:
│                       │      │                   17.0.19 and  21.0.11; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.18. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   7.5 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-47063 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-47063.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-47063 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-47063 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:12.19Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:50:40.373Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-46917 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46917 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:aa184cddee2f9d72262165d9eb783c57c9867b91b2084a51b63cc
│                       │      │                   15a2d30f7d7 
│                       │      ├ Title           : openjdk: OpenJDK: Improve DTLS handshaking (Oracle CPU
│                       │      │                   2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Easily exploitable
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via TLS to compromise Oracle Java SE, Oracle GraalVM
│                       │      │                   for JDK, Oracle GraalVM Enterprise Edition.  Successful
│                       │      │                   attacks of this vulnerability can result in unauthorized
│                       │      │                   ability to cause a partial denial of service (partial DOS)
│                       │      │                   of Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition. Note: This vulnerability can only be
│                       │      │                   exploited by supplying data to APIs in the specified
│                       │      │                   Component without using Untrusted Java Web Start
│                       │      │                   applications or Untrusted Java applets, such as through a
│                       │      │                   web service. CVSS 3.1 Base Score 5.3 (Availability impacts).
│                       │      │                     CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-46917 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-46917.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-46917 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-46917 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:01.81Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:55:54.35Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-46968 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46968 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:f404bc514220de639d30da0a059b26e782de4d5d1500ecef8c7df
│                       │      │                   0e38e46f0fb 
│                       │      ├ Title           : openjdk: Enhance TLS certificate handling 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: JSSE). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u491, 8u491-perf, 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Difficult to exploit
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via TLS to compromise Oracle Java SE.  Successful
│                       │      │                   attacks of this vulnerability can result in  unauthorized
│                       │      │                   creation, deletion or modification access to critical data
│                       │      │                   or all Oracle Java SE accessible data. Note: This
│                       │      │                   vulnerability can only be exploited by supplying data to
│                       │      │                   APIs in the specified Component without using Untrusted Java
│                       │      │                    Web Start applications or Untrusted Java applets, such as
│                       │      │                   through a web service. CVSS 3.1 Base Score 5.9 (Integrity
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-46968 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-46968.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-46968 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-46968 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:02.76Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T15:27:29.943Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-47021 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47021 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8fa294d34aebdf720cb32becb8ca7b38bad8ebfb937e95311453e
│                       │      │                   7712ff266e9 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance XBM image support (Oracle CPU
│                       │      │                   2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Easily exploitable vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
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
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-47021 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-47021.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-47021 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-47021 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:07.67Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T13:42:33.4Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-47027 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47027 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:0d75b18cd023a33cc3f245397a87d6ddd56fb1812a35478a19294
│                       │      │                   2d5a6175458 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance Jar file processing (Oracle CPU
│                       │      │                   2026-07) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: Libraries). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u491, 8u491-perf, 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Easily exploitable
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via multiple protocols to compromise Oracle Java SE. 
│                       │      │                    Successful attacks of this vulnerability can result in
│                       │      │                   unauthorized ability to cause a partial denial of service
│                       │      │                   (partial DOS) of Oracle Java SE. Note: This vulnerability
│                       │      │                   can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   5.3 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-47027 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-47027.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-47027 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-47027 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:08.25Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:55:05.263Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-60147 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-60147 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:0ec704dd4318cbd2433d4517ce2287e0098cdc49f6f8000ef566e
│                       │      │                   73e936e5bec 
│                       │      ├ Title           : openjdk: OpenJDK: Improve certification checking (Oracle CPU
│                       │      │                    2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u491, 8u491-perf, 11.0.31,
│                       │      │                   17.0.19, 21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK:
│                       │      │                   17.0.19 and  21.0.11; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.18. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized update,
│                       │      │                   insert or delete access to some of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data as well as  unauthorized read access to a
│                       │      │                   subset of Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition accessible data. Note: This
│                       │      │                   vulnerability can be exploited by using APIs in the
│                       │      │                   specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 6.5 (Confidentiality and Integrity impacts). 
│                       │      │                    CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-60147 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-60147.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-60147 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-60147 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:15.407Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:49:46.977Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-47010 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47010 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:a34a954abf8c042f00548b3308068e007b6e8e1573824b688e609
│                       │      │                   90ccf733b8e 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance JPEG handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: ImageIO).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 3.7 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-47010 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-47010.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-47010 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-47010 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:06.497Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T15:13:21.283Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-47059 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47059 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:b5453870dd60a9dc7886266308e7ed1ba7f77f611834e267ea229
│                       │      │                   233ae4ad698 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance AWT ImagingLib (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. This vulnerability
│                       │      │                   does not apply to Java deployments, typically in servers,
│                       │      │                   that load and run only trusted code (e.g., code installed by
│                       │      │                    an administrator). CVSS 3.1 Base Score 3.7 (Availability
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-47059 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-47059.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-47059 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-47059 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:11.727Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:51:30.65Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-62574 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-62574 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e251e68000065806d90da308de4a022bad991bfcd2a902aaf8122
│                       │      │                   4ca1587d026 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Install).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u491, 11.0.31, 17.0.19, 21.0.11,
│                       │      │                   25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and 
│                       │      │                   21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18. Easily
│                       │      │                   exploitable vulnerability allows low privileged attacker
│                       │      │                   with logon to the infrastructure where Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   executes to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in takeover of Oracle Java
│                       │      │                   SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. CVSS 3.1 Base Score 7.8 (Confidentiality, Integrity
│                       │      │                    and Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H). 
│                       │      ├ Severity        : UNKNOWN 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ References       ─ [0]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:19:09.667Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:37:03.21Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-41254 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-41254 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:005869fdc4d5ffc14c1840075cd858f722529de836151482dca02
│                       │      │                   a867198cc81 
│                       │      ├ Title           : Little CMS: lcms2: mm2/Little-CMS: Little CMS: Information
│                       │      │                   disclosure or denial of service via integer overflow in
│                       │      │                   CubeSize 
│                       │      ├ Description     : Little CMS (lcms2) through 2.18 has an integer overflow in
│                       │      │                   CubeSize in cmslut.c because the overflow check is performed
│                       │      │                    after the multiplication. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ╭ [0]: CWE-696 
│                       │      │                  ╰ [1]: CWE-190 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ julia      : 3 
│                       │      │                  ├ nvd        : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.5 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.1 
│                       │      ├ References       ╭ [0] : https://abhinavagarwal07.github.io/posts/lcms2-cubesi
│                       │      │                  │       ze-overflow/ 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2026-41254 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [20]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [29]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [30]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://github.com/mm2/Little-CMS/commit/da6110b1d14a
│                       │      │                  │       bc394633a388209abd5ebedd7ab0 
│                       │      │                  ├ [33]: https://github.com/mm2/Little-CMS/commit/e0641b1828d0
│                       │      │                  │       a1af5ecb1b11fe22f24fceefd4bc 
│                       │      │                  ├ [34]: https://github.com/mm2/Little-CMS/security/advisories
│                       │      │                  │       /GHSA-4xp6-rcgg-m9qq 
│                       │      │                  ├ [35]: https://linux.oracle.com/cve/CVE-2026-41254.html 
│                       │      │                  ├ [36]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [37]: https://lists.debian.org/debian-lts-announce/2026/05/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [38]: https://nvd.nist.gov/vuln/detail/CVE-2026-41254 
│                       │      │                  ├ [39]: https://ubuntu.com/security/notices/USN-8209-1 
│                       │      │                  ├ [40]: https://ubuntu.com/security/notices/USN-8209-2 
│                       │      │                  ├ [41]: https://www.cve.org/CVERecord?id=CVE-2026-41254 
│                       │      │                  ╰ [42]: https://www.openwall.com/lists/oss-security/2026/04/1
│                       │      │                          7/16 
│                       │      ├ PublishedDate   : 2026-04-18T07:16:10.807Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:46:23.47Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-47063 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47063 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:ad69e8cfb07a69dd12301c265f76a755c00a5ace2c3ba976edca0
│                       │      │                   baf75b5c402 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance Jar handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Libraries).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u491, 8u491-perf, 11.0.31,
│                       │      │                   17.0.19, 21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK:
│                       │      │                   17.0.19 and  21.0.11; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.18. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   7.5 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-47063 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-47063.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-47063 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-47063 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:12.19Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:50:40.373Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-46917 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46917 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:a57cd7956c2b74dcaaab458d7fb92da06ad0154eb069334692845
│                       │      │                   46dba450a68 
│                       │      ├ Title           : openjdk: OpenJDK: Improve DTLS handshaking (Oracle CPU
│                       │      │                   2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Easily exploitable
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via TLS to compromise Oracle Java SE, Oracle GraalVM
│                       │      │                   for JDK, Oracle GraalVM Enterprise Edition.  Successful
│                       │      │                   attacks of this vulnerability can result in unauthorized
│                       │      │                   ability to cause a partial denial of service (partial DOS)
│                       │      │                   of Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition. Note: This vulnerability can only be
│                       │      │                   exploited by supplying data to APIs in the specified
│                       │      │                   Component without using Untrusted Java Web Start
│                       │      │                   applications or Untrusted Java applets, such as through a
│                       │      │                   web service. CVSS 3.1 Base Score 5.3 (Availability impacts).
│                       │      │                     CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-46917 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-46917.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-46917 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-46917 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:01.81Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:55:54.35Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-46968 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46968 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:070035c5e7c1cff33e93f708b7863e84677866de4a06b022b0678
│                       │      │                   67bff5e87c5 
│                       │      ├ Title           : openjdk: Enhance TLS certificate handling 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: JSSE). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u491, 8u491-perf, 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Difficult to exploit
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via TLS to compromise Oracle Java SE.  Successful
│                       │      │                   attacks of this vulnerability can result in  unauthorized
│                       │      │                   creation, deletion or modification access to critical data
│                       │      │                   or all Oracle Java SE accessible data. Note: This
│                       │      │                   vulnerability can only be exploited by supplying data to
│                       │      │                   APIs in the specified Component without using Untrusted Java
│                       │      │                    Web Start applications or Untrusted Java applets, such as
│                       │      │                   through a web service. CVSS 3.1 Base Score 5.9 (Integrity
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-46968 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-46968.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-46968 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-46968 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:02.76Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T15:27:29.943Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-47021 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47021 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:7b9e993041f75fb4b5a80cc1a6849c30c007fd80058331073521f
│                       │      │                   d9fb49e63c8 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance XBM image support (Oracle CPU
│                       │      │                   2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Easily exploitable vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
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
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-47021 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-47021.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-47021 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-47021 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:07.67Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T13:42:33.4Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-47027 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47027 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:42472727a0ec35c040ff67ac8c99275cc0608f979af6ca65a0fa5
│                       │      │                   1d457978f73 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance Jar file processing (Oracle CPU
│                       │      │                   2026-07) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: Libraries). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u491, 8u491-perf, 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Easily exploitable
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via multiple protocols to compromise Oracle Java SE. 
│                       │      │                    Successful attacks of this vulnerability can result in
│                       │      │                   unauthorized ability to cause a partial denial of service
│                       │      │                   (partial DOS) of Oracle Java SE. Note: This vulnerability
│                       │      │                   can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   5.3 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-47027 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-47027.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-47027 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-47027 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:08.25Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:55:05.263Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-60147 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-60147 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:a10379e050b893e65cbb9b1726cac164a96cd838e04f9a55c26e8
│                       │      │                   7a4e63777c9 
│                       │      ├ Title           : openjdk: OpenJDK: Improve certification checking (Oracle CPU
│                       │      │                    2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u491, 8u491-perf, 11.0.31,
│                       │      │                   17.0.19, 21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK:
│                       │      │                   17.0.19 and  21.0.11; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.18. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized update,
│                       │      │                   insert or delete access to some of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data as well as  unauthorized read access to a
│                       │      │                   subset of Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition accessible data. Note: This
│                       │      │                   vulnerability can be exploited by using APIs in the
│                       │      │                   specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 6.5 (Confidentiality and Integrity impacts). 
│                       │      │                    CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-60147 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-60147.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-60147 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-60147 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:15.407Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:49:46.977Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2026-47010 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47010 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:aa4191c4c43a15b9297ed776b692fcd7de2c7e7cc387667c7e044
│                       │      │                   f1f776324d5 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance JPEG handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: ImageIO).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 3.7 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-47010 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-47010.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-47010 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-47010 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:06.497Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T15:13:21.283Z 
│                       ├ [18] ╭ VulnerabilityID : CVE-2026-47059 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47059 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:3fddf854d643abe5888139582a82e5f514d4fc6a1869a7856863c
│                       │      │                   e6625493503 
│                       │      ├ Title           : openjdk: OpenJDK: Enhance AWT ImagingLib (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. This vulnerability
│                       │      │                   does not apply to Java deployments, typically in servers,
│                       │      │                   that load and run only trusted code (e.g., code installed by
│                       │      │                    an administrator). CVSS 3.1 Base Score 3.7 (Availability
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42895 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-47059 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2459420 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2502751 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2502782 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2502783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2502784 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2502791 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/2502792 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/2502793 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/2503636 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2459420 
│                       │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2502751 
│                       │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2502782 
│                       │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2502783 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2502784 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/show_bug.cgi?id=2502791 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2502792 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2502793 
│                       │      │                  ├ [19]: https://bugzilla.redhat.com/show_bug.cgi?id=2503636 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [29]: https://errata.almalinux.org/10/ALSA-2026-42895.html 
│                       │      │                  ├ [30]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2026-47059.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [33]: https://nvd.nist.gov/vuln/detail/CVE-2026-47059 
│                       │      │                  ├ [34]: https://www.cve.org/CVERecord?id=CVE-2026-47059 
│                       │      │                  ╰ [35]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:11.727Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:51:30.65Z 
│                       ╰ [19] ╭ VulnerabilityID : CVE-2026-62574 
│                              ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                              ├ PkgName         : openjdk21-jre-headless 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                              │                  │       arch=x86_64&distro=3.24.1 
│                              │                  ╰ UID : e50dcf6a51ec8089 
│                              ├ InstalledVersion: 21.0.11_p10-r0 
│                              ├ FixedVersion    : 21.0.12_p8-r0 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                              │                  │         4e4c9f62e347164a4006 
│                              │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                              │                            77bbbb6e1ea62d15f4ee 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-62574 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Fingerprint     : sha256:2db13eb11a35ce081d6e93b395da43c2d410f59aab4c926d672df
│                              │                   ce736447cfa 
│                              ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                              │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                              │                    (component: Install).  Supported versions that are affected
│                              │                    are Oracle Java SE: 8u491, 11.0.31, 17.0.19, 21.0.11,
│                              │                   25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and 
│                              │                   21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18. Easily
│                              │                   exploitable vulnerability allows low privileged attacker
│                              │                   with logon to the infrastructure where Oracle Java SE,
│                              │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                              │                   executes to compromise Oracle Java SE, Oracle GraalVM for
│                              │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                              │                   of this vulnerability can result in takeover of Oracle Java
│                              │                   SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                              │                   Edition. CVSS 3.1 Base Score 7.8 (Confidentiality, Integrity
│                              │                    and Availability impacts).  CVSS Vector:
│                              │                   (CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H). 
│                              ├ Severity        : UNKNOWN 
│                              ├ CweIDs           ─ [0]: CWE-284 
│                              ├ References       ─ [0]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                              ├ PublishedDate   : 2026-07-21T22:19:09.667Z 
│                              ╰ LastModifiedDate: 2026-08-03T18:37:03.21Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages 
```
