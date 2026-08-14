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
│                       │      ├ Fingerprint     : sha256:ee961e960c50b51ed51d459e45bce728b1e431895c39f6620b15f
│                       │      │                   1354b7111e7 
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
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [21]: https://creativecommons.org/licenses/by/4.0/ 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [29]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [30]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [31]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [32]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [33]: https://github.com/mm2/Little-CMS/commit/da6110b1d14a
│                       │      │                  │       bc394633a388209abd5ebedd7ab0 
│                       │      │                  ├ [34]: https://github.com/mm2/Little-CMS/commit/e0641b1828d0
│                       │      │                  │       a1af5ecb1b11fe22f24fceefd4bc 
│                       │      │                  ├ [35]: https://github.com/mm2/Little-CMS/security/advisories
│                       │      │                  │       /GHSA-4xp6-rcgg-m9qq 
│                       │      │                  ├ [36]: https://linux.oracle.com/cve/CVE-2026-41254.html 
│                       │      │                  ├ [37]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [38]: https://lists.debian.org/debian-lts-announce/2026/05/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [39]: https://nvd.nist.gov/vuln/detail/CVE-2026-41254 
│                       │      │                  ├ [40]: https://ubuntu.com/security/notices/USN-8209-1 
│                       │      │                  ├ [41]: https://ubuntu.com/security/notices/USN-8209-2 
│                       │      │                  ├ [42]: https://www.cve.org/CVERecord?id=CVE-2026-41254 
│                       │      │                  ╰ [43]: https://www.openwall.com/lists/oss-security/2026/04/1
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
│                       │      ├ Fingerprint     : sha256:8109b454cc304f9eb0a99bc03c117cb0f63f5ad7c9ebd9f203f58
│                       │      │                   39a3811f951 
│                       │      ├ Title           : openjdk: Enhance Jar handling (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-47063.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-47063 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-47063 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:e2aa7d80c327a4a897ac5974973b5f8c0782acc221ae36c520790
│                       │      │                   e21cc9e8e2f 
│                       │      ├ Title           : openjdk: Improve DTLS handshaking (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-46917.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-46917 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-46917 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:3d5af03da22b312b46c6db128f3bdb06d59b04e70c9de6b7365b5
│                       │      │                   1630f3e582e 
│                       │      ├ Title           : openjdk: Enhance TLS certificate handling (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-46968.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-46968 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-46968 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:38fb98ee017f5567290fb7e95a19bd1eb5a69339b0a03b171fe1a
│                       │      │                   8796474704a 
│                       │      ├ Title           : openjdk: Enhance XBM image support (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-47021.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-47021 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-47021 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:07.67Z 
│                       │      ╰ LastModifiedDate: 2026-08-12T20:17:44.44Z 
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
│                       │      ├ Fingerprint     : sha256:c6cfbc5a7353933e24f59e36343755c7fd8d37c222e2b3905cc72
│                       │      │                   ba65586d11c 
│                       │      ├ Title           : openjdk: Enhance Jar file processing (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-47027.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-47027 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-47027 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:61c7df8c81cf6b9c733c87ddadc3237a12363829e0d794b6647a0
│                       │      │                   3f2a99068c6 
│                       │      ├ Title           : openjdk: Improve certification checking (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-60147.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-60147 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-60147 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:43a14c642ce8d372fafd2b8a82a13b5c5bf6d5f7b03affff00bdc
│                       │      │                   9523fc03f2a 
│                       │      ├ Title           : openjdk: Enhance JPEG handling (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-47010.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-47010 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-47010 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:9a948083cd4116261006f72f1407cf81f30a06ea2b8d500942d5b
│                       │      │                   d694e2d1f81 
│                       │      ├ Title           : openjdk: Enhance AWT ImagingLib (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-47059.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-47059 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-47059 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:f66f199c7aa97f77dc8da779790ce0859a27c9f2a126138b044d2
│                       │      │                   e0643ad5b16 
│                       │      ├ Title           : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Orac ... 
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
│                       │      ├ Fingerprint     : sha256:6a0ddf1ac1943bca28b55151f418b990a69d041d6226377a0dd64
│                       │      │                   3104b8d81b4 
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
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [21]: https://creativecommons.org/licenses/by/4.0/ 
│                       │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-41254 
│                       │      │                  ├ [23]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46917 
│                       │      │                  ├ [24]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-46968 
│                       │      │                  ├ [25]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47010 
│                       │      │                  ├ [26]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47021 
│                       │      │                  ├ [27]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47027 
│                       │      │                  ├ [28]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47059 
│                       │      │                  ├ [29]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-47063 
│                       │      │                  ├ [30]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-60147 
│                       │      │                  ├ [31]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [32]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [33]: https://github.com/mm2/Little-CMS/commit/da6110b1d14a
│                       │      │                  │       bc394633a388209abd5ebedd7ab0 
│                       │      │                  ├ [34]: https://github.com/mm2/Little-CMS/commit/e0641b1828d0
│                       │      │                  │       a1af5ecb1b11fe22f24fceefd4bc 
│                       │      │                  ├ [35]: https://github.com/mm2/Little-CMS/security/advisories
│                       │      │                  │       /GHSA-4xp6-rcgg-m9qq 
│                       │      │                  ├ [36]: https://linux.oracle.com/cve/CVE-2026-41254.html 
│                       │      │                  ├ [37]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [38]: https://lists.debian.org/debian-lts-announce/2026/05/
│                       │      │                  │       msg00014.html 
│                       │      │                  ├ [39]: https://nvd.nist.gov/vuln/detail/CVE-2026-41254 
│                       │      │                  ├ [40]: https://ubuntu.com/security/notices/USN-8209-1 
│                       │      │                  ├ [41]: https://ubuntu.com/security/notices/USN-8209-2 
│                       │      │                  ├ [42]: https://www.cve.org/CVERecord?id=CVE-2026-41254 
│                       │      │                  ╰ [43]: https://www.openwall.com/lists/oss-security/2026/04/1
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
│                       │      ├ Fingerprint     : sha256:a36fda536e5bf5aa7ae31b267f61ce274cdd8a554a8b732290a6c
│                       │      │                   9425bb2dbd1 
│                       │      ├ Title           : openjdk: Enhance Jar handling (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-47063.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-47063 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-47063 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:d20e6d7da6bd1a3a02f2e748ec0b3432195c200190e0bc536d7ce
│                       │      │                   1f0901f143e 
│                       │      ├ Title           : openjdk: Improve DTLS handshaking (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-46917.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-46917 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-46917 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:e0d997fb9edba79927c98d31ebb9226a75392c636362005ff4ec9
│                       │      │                   4dd3d3a25cc 
│                       │      ├ Title           : openjdk: Enhance TLS certificate handling (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-46968.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-46968 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-46968 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:46aef7442d7b4737afe19ef129e82e96a30d7c23d3cf5425539ea
│                       │      │                   9a59e1f42dd 
│                       │      ├ Title           : openjdk: Enhance XBM image support (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-47021.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-47021 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-47021 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
│                       │      ├ PublishedDate   : 2026-07-21T22:17:07.67Z 
│                       │      ╰ LastModifiedDate: 2026-08-12T20:17:44.44Z 
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
│                       │      ├ Fingerprint     : sha256:922df3abf7d67a0a54d00cb6e9d00722a40e8f51d5fc739d40665
│                       │      │                   953d09bb767 
│                       │      ├ Title           : openjdk: Enhance Jar file processing (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-47027.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-47027 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-47027 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:5d95c628f47375c6376f3146e150691a4901f541fd105363e6523
│                       │      │                   652f8ddacde 
│                       │      ├ Title           : openjdk: Improve certification checking (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-60147.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-60147 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-60147 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:de8b3aa0c37961eb6b2d137b0c0486a2e99ac5252b6a4d5038d88
│                       │      │                   c1376ee8622 
│                       │      ├ Title           : openjdk: Enhance JPEG handling (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-47010.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-47010 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-47010 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                       │      ├ Fingerprint     : sha256:2c463e2db52c3ba73fdeccd6c69e2241e3696746f992beaa4b2d9
│                       │      │                   240709aa583 
│                       │      ├ Title           : openjdk: Enhance AWT ImagingLib (Oracle CPU 2026-07) 
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
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:42899 
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
│                       │      │                  ├ [20]: https://creativecommons.org/licenses/by/4.0/ 
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
│                       │      │                  ├ [30]: https://errata.almalinux.org/9/ALSA-2026-42899.html 
│                       │      │                  ├ [31]: https://errata.rockylinux.org/RLSA-2026:42899 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2026-47059.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2026-42899.html 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2026-47059 
│                       │      │                  ├ [35]: https://www.cve.org/CVERecord?id=CVE-2026-47059 
│                       │      │                  ╰ [36]: https://www.oracle.com/security-alerts/cpujul2026.html 
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
│                              ├ Fingerprint     : sha256:aacd4986430d3d2aac0f500dcadfdfa9fd94a5dcd913e98ebb500
│                              │                   480317eb1be 
│                              ├ Title           : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                              │                    Orac ... 
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
