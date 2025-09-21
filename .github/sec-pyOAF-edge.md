````yaml
╭ [0] ╭ Target         : openaf/pyoaf:edge (alpine 3.21.3) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2025-31498 
│                       │      ├ PkgID           : c-ares@1.34.3-r0 
│                       │      ├ PkgName         : c-ares 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/c-ares@1.34.3-r0?arch=x86_64&distro=3.
│                       │      │                  │       21.3 
│                       │      │                  ╰ UID : a88ae4812afe4ac7 
│                       │      ├ InstalledVersion: 1.34.3-r0 
│                       │      ├ FixedVersion    : 1.34.5-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-31498 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : c-ares: c-ares has a use-after-free in read_answers() 
│                       │      ├ Description     : c-ares is an asynchronous resolver library. From 1.32.3
│                       │      │                   through 1.34.4, there is a use-after-free in read_answers()
│                       │      │                   when process_answer() may re-enqueue a query either due to a
│                       │      │                    DNS Cookie Failure or when the upstream server does not
│                       │      │                   properly support EDNS, or possibly on TCP queries if the
│                       │      │                   remote closed the connection immediately after a response.
│                       │      │                   If there was an issue trying to put that new transaction on
│                       │      │                   the wire, it would close the connection handle, but
│                       │      │                   read_answers() was still expecting the connection handle to
│                       │      │                   be available to possibly dequeue other responses. In theory
│                       │      │                   a remote attacker might be able to trigger this by flooding
│                       │      │                   the target with ICMP UNREACHABLE packets if they also
│                       │      │                   control the upstream nameserver and can return a result with
│                       │      │                    one of those conditions, this has been untested. Otherwise
│                       │      │                   only a local attacker might be able to change system
│                       │      │                   behavior to make send()/write() return a failure condition.
│                       │      │                   This vulnerability is fixed in 1.34.5. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-416 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2025/04/08/3 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2025:7433 
│                       │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2025-31498 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2358271 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2359553 
│                       │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2025-7433.html 
│                       │      │                  ├ [6] : https://github.com/c-ares/c-ares/commit/29d3871911263
│                       │      │                  │       9d8c0ba910254a3dd4f482ea2d1 
│                       │      │                  ├ [7] : https://github.com/c-ares/c-ares/pull/821 
│                       │      │                  ├ [8] : https://github.com/c-ares/c-ares/security/advisories/
│                       │      │                  │       GHSA-6hxc-62jh-p29v 
│                       │      │                  ├ [9] : https://linux.oracle.com/cve/CVE-2025-31498.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/errata/ELSA-2025-7502.html 
│                       │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2025-31498 
│                       │      │                  ├ [12]: https://ubuntu.com/security/notices/USN-7477-1 
│                       │      │                  ╰ [13]: https://www.cve.org/CVERecord?id=CVE-2025-31498 
│                       │      ├ PublishedDate   : 2025-04-08T14:15:35.293Z 
│                       │      ╰ LastModifiedDate: 2025-04-08T15:15:50.31Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2025-31344 
│                       │      ├ PkgID           : giflib@5.2.2-r0 
│                       │      ├ PkgName         : giflib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/giflib@5.2.2-r0?arch=x86_64&distro=3.2
│                       │      │                  │       1.3 
│                       │      │                  ╰ UID : 1faefcccad6c3f6 
│                       │      ├ InstalledVersion: 5.2.2-r0 
│                       │      ├ FixedVersion    : 5.2.2-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-31344 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : giflib: The giflib open-source component has a buffer
│                       │      │                   overflow vulnerability 
│                       │      ├ Description     : Heap-based Buffer Overflow vulnerability in openEuler giflib
│                       │      │                    on Linux. This vulnerability is associated with program
│                       │      │                   files gif2rgb.C.
│                       │      │                   
│                       │      │                   This issue affects giflib: through 5.2.2. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-122 
│                       │      ├ VendorSeverity   ╭ azure      : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ╰ redhat     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2025/04/07/3 
│                       │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2025/04/07/4 
│                       │      │                  ├ [2] : http://www.openwall.com/lists/oss-security/2025/04/07/5 
│                       │      │                  ├ [3] : http://www.openwall.com/lists/oss-security/2025/04/07/6 
│                       │      │                  ├ [4] : http://www.openwall.com/lists/oss-security/2025/04/08/1 
│                       │      │                  ├ [5] : http://www.openwall.com/lists/oss-security/2025/04/09/5 
│                       │      │                  ├ [6] : http://www.openwall.com/lists/oss-security/2025/04/09/7 
│                       │      │                  ├ [7] : http://www.openwall.com/lists/oss-security/2025/04/10/1 
│                       │      │                  ├ [8] : https://access.redhat.com/security/cve/CVE-2025-31344 
│                       │      │                  ├ [9] : https://gitee.com/src-openeuler/giflib/pulls/54 
│                       │      │                  ├ [10]: https://nvd.nist.gov/vuln/detail/CVE-2025-31344 
│                       │      │                  ├ [11]: https://www.cve.org/CVERecord?id=CVE-2025-31344 
│                       │      │                  ╰ [12]: https://www.openeuler.org/zh/security/security-bullet
│                       │      │                          ins/detail/?id=openEuler-SA-2025-1292 
│                       │      ├ PublishedDate   : 2025-04-14T08:15:13.973Z 
│                       │      ╰ LastModifiedDate: 2025-04-15T18:39:27.967Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2025-21587 
│                       │      ├ PkgID           : openjdk21-jre@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.6_p7-r0?arch=x86_64
│                       │      │                  │       &distro=3.21.3 
│                       │      │                  ╰ UID : 2080461f382c7dae 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.7_p6-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-21587 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Better TLS connection support (Oracle CPU 2025-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE:8u441, 8u441-perf, 11.0.26, 17.0.14,
│                       │      │                   21.0.6, 24; Oracle GraalVM for JDK:17.0.14, 21.0.6, 24;
│                       │      │                   Oracle GraalVM Enterprise Edition:20.3.17 and  21.3.13.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized creation, deletion
│                       │      │                    or modification access to critical data or all Oracle Java
│                       │      │                   SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data as well as  unauthorized access to
│                       │      │                   critical data or complete access to all Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability can be exploited
│                       │      │                   by using APIs in the specified Component, e.g., through a
│                       │      │                   web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:3855 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-21587 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2359693 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2359694 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2359695 
│                       │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-21587 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30691 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30698 
│                       │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2025-3855.html 
│                       │      │                  ├ [9] : https://errata.rockylinux.org/RLSA-2025:3855 
│                       │      │                  ├ [10]: https://github.com/openjdk/jdk11u/commit/2adb01e8c5fb
│                       │      │                  │       cc3dfa9f82df3deccb3a1705bf13 (jdk-11.0.27-ga) 
│                       │      │                  ├ [11]: https://github.com/openjdk/jdk17u/commit/73aa304234f2
│                       │      │                  │       ec17abbb640b7f2d0503cf1bfc91 (jdk-17.0.15-ga) 
│                       │      │                  ├ [12]: https://github.com/openjdk/jdk21u/commit/d5c94adf69ba
│                       │      │                  │       20f5652453729620c4f1c8e4860e (jdk-21.0.7-ga) 
│                       │      │                  ├ [13]: https://github.com/openjdk/jdk8u/commit/3cdd3081565d8
│                       │      │                  │       90801a27a1f9ac8bc53e5711ce6 (jdk8u452-b08) 
│                       │      │                  ├ [14]: https://linux.oracle.com/cve/CVE-2025-21587.html 
│                       │      │                  ├ [15]: https://linux.oracle.com/errata/ELSA-2025-7508.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2025-21587 
│                       │      │                  ├ [17]: https://openjdk.org/groups/vulnerability/advisories/2
│                       │      │                  │       025-04-15 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-7480-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7481-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7482-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-7483-1 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7484-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7531-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7533-1 
│                       │      │                  ├ [25]: https://www.cve.org/CVERecord?id=CVE-2025-21587 
│                       │      │                  ╰ [26]: https://www.oracle.com/security-alerts/cpuapr2025.html 
│                       │      ├ PublishedDate   : 2025-04-15T21:15:54.293Z 
│                       │      ╰ LastModifiedDate: 2025-04-29T20:03:13.79Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2025-23083 
│                       │      ├ PkgID           : openjdk21-jre@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.6_p7-r0?arch=x86_64
│                       │      │                  │       &distro=3.21.3 
│                       │      │                  ╰ UID : 2080461f382c7dae 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.7_p6-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-23083 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : nodejs: Node.js Worker Thread Exposure via Diagnostics Channel 
│                       │      ├ Description     : With the aid of the diagnostics_channel utility, an event
│                       │      │                   can be hooked into whenever a worker thread is created. This
│                       │      │                    is not limited only to workers but also exposes internal
│                       │      │                   workers, where an instance of them can be fetched, and its
│                       │      │                   constructor can be grabbed and reinstated for malicious
│                       │      │                   usage. 
│                       │      │                   
│                       │      │                   This vulnerability affects Permission Model users
│                       │      │                   (--permission) on Node.js v20, v22, and v23. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.0/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 7.7 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.0/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 7.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:1613 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-23083 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2339176 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2339392 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2342618 
│                       │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2025-1613.html 
│                       │      │                  ├ [6] : https://github.com/nodejs/node/commit/51938f023aac90d
│                       │      │                  │       c1dc0bc1f743501788613210e 
│                       │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2025-23083.html 
│                       │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2025-1613.html 
│                       │      │                  ├ [9] : https://nodejs.org/en/blog/vulnerability/january-2025
│                       │      │                  │       -security-releases 
│                       │      │                  ├ [10]: https://nodejs.org/en/blog/vulnerability/january-2025
│                       │      │                  │       -security-releases#worker-permission-bypass-via-inter
│                       │      │                  │       nalworker-leak-in-diagnostics-cve-2025-23083---high 
│                       │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2025-23083 
│                       │      │                  ├ [12]: https://security.netapp.com/advisory/ntap-20250228-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [13]: https://www.cve.org/CVERecord?id=CVE-2025-23083 
│                       │      │                  ├ [14]: https://www.vicarius.io/vsociety/posts/cve-2025-23083
│                       │      │                  │       -detect-nodejs-vulnerability 
│                       │      │                  ╰ [15]: https://www.vicarius.io/vsociety/posts/cve-2025-23083
│                       │      │                          -mitigate-nodejs-vulnerability 
│                       │      ├ PublishedDate   : 2025-01-22T02:15:33.93Z 
│                       │      ╰ LastModifiedDate: 2025-07-22T16:15:26.76Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2025-30749 
│                       │      ├ PkgID           : openjdk21-jre@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.6_p7-r0?arch=x86_64
│                       │      │                  │       &distro=3.21.3 
│                       │      │                  ╰ UID : 2080461f382c7dae 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.8_p9-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-30749 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Better Glyph drawing (Oracle CPU 2025-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u451, 8u451-perf, 11.0.27, 17.0.15, 21.0.7,
│                       │      │                    24.0.1; Oracle GraalVM for JDK: 17.0.15, 21.0.7 and 
│                       │      │                   24.0.1; Oracle GraalVM Enterprise Edition: 21.3.14.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in takeover of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. This vulnerability
│                       │      │                   does not apply to Java deployments, typically in servers,
│                       │      │                   that load and run only trusted code (e.g., code installed by
│                       │      │                    an administrator). CVSS 3.1 Base Score 8.1
│                       │      │                   (Confidentiality, Integrity and Availability impacts).  CVSS
│                       │      │                    Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 8.1 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10873 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-30749 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2376783 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2376784 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2376785 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2379031 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30749 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30754 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50059 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50106 
│                       │      │                  ├ [10]: https://errata.almalinux.org/9/ALSA-2025-10873.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2025:10867 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2025-30749.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2025-10873.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2025-30749 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-7667-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7668-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-7669-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-7672-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7673-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7674-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-7690-1 
│                       │      │                  ├ [22]: https://www.cve.org/CVERecord?id=CVE-2025-30749 
│                       │      │                  ├ [23]: https://www.oracle.com/security-alerts/cpujul2025.html 
│                       │      │                  ╰ [24]: https://www.oracle.com/security-alerts/cpujul2025.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2025-07-15T20:15:29.313Z 
│                       │      ╰ LastModifiedDate: 2025-08-04T21:05:34.533Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2025-50059 
│                       │      ├ PkgID           : openjdk21-jre@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.6_p7-r0?arch=x86_64
│                       │      │                  │       &distro=3.21.3 
│                       │      │                  ╰ UID : 2080461f382c7dae 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.8_p9-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-50059 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Improve HTTP client header handling (Oracle CPU
│                       │      │                   2025-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Networking).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u451-perf, 11.0.27, 17.0.15,
│                       │      │                   21.0.7, 24.0.1; Oracle GraalVM for JDK: 17.0.15, 21.0.7 and 
│                       │      │                    24.0.1; Oracle GraalVM Enterprise Edition: 21.3.14. Easily
│                       │      │                   exploitable vulnerability allows unauthenticated attacker
│                       │      │                   with network access via multiple protocols to compromise
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition.  While the vulnerability is in Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition, attacks may significantly impact additional
│                       │      │                   products (scope change).  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized access to critical
│                       │      │                    data or complete access to all Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability applies to Java
│                       │      │                   deployments, typically in clients running sandboxed Java Web
│                       │      │                    Start applications or sandboxed Java applets, that load and
│                       │      │                    run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. This
│                       │      │                   vulnerability does not apply to Java deployments, typically
│                       │      │                   in servers, that load and run only trusted code (e.g., code
│                       │      │                   installed by an administrator). CVSS 3.1 Base Score 8.6
│                       │      │                   (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 8.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10873 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-50059 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2376783 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2376784 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2376785 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2379031 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30749 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30754 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50059 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50106 
│                       │      │                  ├ [10]: https://errata.almalinux.org/9/ALSA-2025-10873.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2025:10867 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2025-50059.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2025-10873.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2025-50059 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-7668-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7669-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-7672-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-7673-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7674-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7690-1 
│                       │      │                  ├ [21]: https://www.cve.org/CVERecord?id=CVE-2025-50059 
│                       │      │                  ├ [22]: https://www.oracle.com/security-alerts/cpujul2025.html 
│                       │      │                  ╰ [23]: https://www.oracle.com/security-alerts/cpujul2025.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2025-07-15T20:15:40.367Z 
│                       │      ╰ LastModifiedDate: 2025-08-04T21:17:16.467Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2025-50106 
│                       │      ├ PkgID           : openjdk21-jre@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.6_p7-r0?arch=x86_64
│                       │      │                  │       &distro=3.21.3 
│                       │      │                  ╰ UID : 2080461f382c7dae 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.8_p9-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-50106 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Glyph out-of-memory access and crash (Oracle CPU
│                       │      │                   2025-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u451, 8u451-perf, 11.0.27, 17.0.15, 21.0.7,
│                       │      │                    24.0.1; Oracle GraalVM for JDK: 17.0.15, 21.0.7 and 
│                       │      │                   24.0.1; Oracle GraalVM Enterprise Edition: 21.3.14.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in takeover of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 8.1 (Confidentiality, Integrity and
│                       │      │                   Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 8.1 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10873 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-50106 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2376783 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2376784 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2376785 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2379031 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30749 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30754 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50059 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50106 
│                       │      │                  ├ [10]: https://errata.almalinux.org/9/ALSA-2025-10873.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2025:10867 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2025-50106.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2025-10873.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2025-50106 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-7667-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7668-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-7669-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-7672-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7673-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7674-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-7690-1 
│                       │      │                  ├ [22]: https://www.cve.org/CVERecord?id=CVE-2025-50106 
│                       │      │                  ├ [23]: https://www.oracle.com/security-alerts/cpujul2025.html 
│                       │      │                  ╰ [24]: https://www.oracle.com/security-alerts/cpujul2025.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2025-07-15T20:15:47.013Z 
│                       │      ╰ LastModifiedDate: 2025-08-04T21:20:26.203Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2025-30691 
│                       │      ├ PkgID           : openjdk21-jre@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.6_p7-r0?arch=x86_64
│                       │      │                  │       &distro=3.21.3 
│                       │      │                  ╰ UID : 2080461f382c7dae 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.7_p6-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-30691 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Improve compiler transformations (Oracle CPU 2025-04) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: Compiler). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   21.0.6, 24; Oracle GraalVM for JDK: 21.0.6 and  24.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE accessible data as
│                       │      │                   well as  unauthorized read access to a subset of Oracle Java
│                       │      │                    SE accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 4.8
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:3855 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-30691 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2359693 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2359694 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2359695 
│                       │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-21587 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30691 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30698 
│                       │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2025-3855.html 
│                       │      │                  ├ [9] : https://errata.rockylinux.org/RLSA-2025:3855 
│                       │      │                  ├ [10]: https://github.com/openjdk/jdk11u/commit/2b70822671cf
│                       │      │                  │       5f9b37956949421e7c77da082c8e (jdk-11.0.27-ga) 
│                       │      │                  ├ [11]: https://github.com/openjdk/jdk17u/commit/5b0a5f436fb9
│                       │      │                  │       817d679f64302b37543bf160d43d (jdk-17.0.15-ga) 
│                       │      │                  ├ [12]: https://github.com/openjdk/jdk21u/commit/11067d7e975c
│                       │      │                  │       e71bedbfdd314519ec9ff689a7e7 (jdk-21.0.7-ga) 
│                       │      │                  ├ [13]: https://github.com/openjdk/jdk8u/commit/949c6ffc54efa
│                       │      │                  │       a92d6559a3e7897432b95e99253 (jdk8u452-b08) 
│                       │      │                  ├ [14]: https://linux.oracle.com/cve/CVE-2025-30691.html 
│                       │      │                  ├ [15]: https://linux.oracle.com/errata/ELSA-2025-7508.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2025-30691 
│                       │      │                  ├ [17]: https://openjdk.org/groups/vulnerability/advisories/2
│                       │      │                  │       025-04-15 
│                       │      │                  ├ [18]: https://security.netapp.com/advisory/ntap-20250418-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7480-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7481-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-7482-1 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7483-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7484-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7531-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7533-1 
│                       │      │                  ├ [26]: https://www.cve.org/CVERecord?id=CVE-2025-30691 
│                       │      │                  ╰ [27]: https://www.oracle.com/security-alerts/cpuapr2025.html 
│                       │      ├ PublishedDate   : 2025-04-15T21:15:58.36Z 
│                       │      ╰ LastModifiedDate: 2025-04-19T01:15:44.85Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2025-30698 
│                       │      ├ PkgID           : openjdk21-jre@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.6_p7-r0?arch=x86_64
│                       │      │                  │       &distro=3.21.3 
│                       │      │                  ╰ UID : 2080461f382c7dae 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.7_p6-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-30698 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Enhance Buffered Image handling (Oracle CPU 2025-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u441, 8u441-perf, 11.0.26, 17.0.14, 21.0.6,
│                       │      │                    24; Oracle GraalVM for JDK: 17.0.14, 21.0.6, 24; Oracle
│                       │      │                   GraalVM Enterprise Edition: 20.3.17 and  21.3.13. Difficult
│                       │      │                   to exploit vulnerability allows unauthenticated attacker
│                       │      │                   with network access via multiple protocols to compromise
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data as
│                       │      │                   well as  unauthorized read access to a subset of Oracle Java
│                       │      │                    SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data and unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. This vulnerability
│                       │      │                   does not apply to Java deployments, typically in servers,
│                       │      │                   that load and run only trusted code (e.g., code installed by
│                       │      │                    an administrator). CVSS 3.1 Base Score 5.6
│                       │      │                   (Confidentiality, Integrity and Availability impacts).  CVSS
│                       │      │                    Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:3855 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-30698 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2359693 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2359694 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2359695 
│                       │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-21587 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30691 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30698 
│                       │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2025-3855.html 
│                       │      │                  ├ [9] : https://errata.rockylinux.org/RLSA-2025:3855 
│                       │      │                  ├ [10]: https://github.com/openjdk/jdk11u/commit/ea1389c97182
│                       │      │                  │       7876134a6d1d3ab2934681e9f3d6 (jdk-11.0.27-ga) 
│                       │      │                  ├ [11]: https://github.com/openjdk/jdk17u/commit/0a89eb258833
│                       │      │                  │       4226531e8e25ac340eabbc00bd6d (jdk-17.0.15-ga) 
│                       │      │                  ├ [12]: https://github.com/openjdk/jdk21u/commit/3048e287d8ea
│                       │      │                  │       7d5e0d19d9188eb4212801ebf2a2 (jdk-21.0.7-ga) 
│                       │      │                  ├ [13]: https://github.com/openjdk/jdk8u/commit/68d10daabaf9c
│                       │      │                  │       939a5d2e665994c6d348f38cfd5 (jdk8u452-b08) 
│                       │      │                  ├ [14]: https://linux.oracle.com/cve/CVE-2025-30698.html 
│                       │      │                  ├ [15]: https://linux.oracle.com/errata/ELSA-2025-7508.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2025-30698 
│                       │      │                  ├ [17]: https://openjdk.org/groups/vulnerability/advisories/2
│                       │      │                  │       025-04-15 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-7480-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7481-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7482-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-7483-1 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7484-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7531-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7533-1 
│                       │      │                  ├ [25]: https://www.cve.org/CVERecord?id=CVE-2025-30698 
│                       │      │                  ╰ [26]: https://www.oracle.com/security-alerts/cpuapr2025.html 
│                       │      ├ PublishedDate   : 2025-04-15T21:15:59.137Z 
│                       │      ╰ LastModifiedDate: 2025-04-29T20:03:21.7Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2025-30754 
│                       │      ├ PkgID           : openjdk21-jre@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.6_p7-r0?arch=x86_64
│                       │      │                  │       &distro=3.21.3 
│                       │      │                  ╰ UID : 2080461f382c7dae 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.8_p9-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-30754 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Enhance TLS protocol support (Oracle CPU 2025-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 8u451, 8u451-perf, 11.0.27, 17.0.15,
│                       │      │                   21.0.7, 24.0.1; Oracle GraalVM for JDK: 17.0.15, 21.0.7 and 
│                       │      │                    24.0.1; Oracle GraalVM Enterprise Edition: 21.3.14.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via TLS to compromise Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition.  Successful attacks of this vulnerability can
│                       │      │                   result in  unauthorized update, insert or delete access to
│                       │      │                   some of Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition accessible data as well as 
│                       │      │                   unauthorized read access to a subset of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability applies to Java
│                       │      │                   deployments, typically in clients running sandboxed Java Web
│                       │      │                    Start applications or sandboxed Java applets, that load and
│                       │      │                    run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. This
│                       │      │                   vulnerability does not apply to Java deployments, typically
│                       │      │                   in servers, that load and run only trusted code (e.g., code
│                       │      │                   installed by an administrator). CVSS 3.1 Base Score 4.8
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10873 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-30754 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2376783 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2376784 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2376785 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2379031 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30749 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30754 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50059 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50106 
│                       │      │                  ├ [10]: https://errata.almalinux.org/9/ALSA-2025-10873.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2025:10867 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2025-30754.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2025-10873.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2025-30754 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-7667-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7668-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-7669-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-7672-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7673-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7674-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-7690-1 
│                       │      │                  ├ [22]: https://www.cve.org/CVERecord?id=CVE-2025-30754 
│                       │      │                  ├ [23]: https://www.oracle.com/security-alerts/cpujul2025.html 
│                       │      │                  ╰ [24]: https://www.oracle.com/security-alerts/cpujul2025.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2025-07-15T20:15:29.973Z 
│                       │      ╰ LastModifiedDate: 2025-08-04T21:16:20.84Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2025-21587 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.6_p7-r0?ar
│                       │      │                  │       ch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : d2e38af626fba367 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.7_p6-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-21587 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Better TLS connection support (Oracle CPU 2025-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE:8u441, 8u441-perf, 11.0.26, 17.0.14,
│                       │      │                   21.0.6, 24; Oracle GraalVM for JDK:17.0.14, 21.0.6, 24;
│                       │      │                   Oracle GraalVM Enterprise Edition:20.3.17 and  21.3.13.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized creation, deletion
│                       │      │                    or modification access to critical data or all Oracle Java
│                       │      │                   SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data as well as  unauthorized access to
│                       │      │                   critical data or complete access to all Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability can be exploited
│                       │      │                   by using APIs in the specified Component, e.g., through a
│                       │      │                   web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:3855 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-21587 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2359693 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2359694 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2359695 
│                       │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-21587 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30691 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30698 
│                       │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2025-3855.html 
│                       │      │                  ├ [9] : https://errata.rockylinux.org/RLSA-2025:3855 
│                       │      │                  ├ [10]: https://github.com/openjdk/jdk11u/commit/2adb01e8c5fb
│                       │      │                  │       cc3dfa9f82df3deccb3a1705bf13 (jdk-11.0.27-ga) 
│                       │      │                  ├ [11]: https://github.com/openjdk/jdk17u/commit/73aa304234f2
│                       │      │                  │       ec17abbb640b7f2d0503cf1bfc91 (jdk-17.0.15-ga) 
│                       │      │                  ├ [12]: https://github.com/openjdk/jdk21u/commit/d5c94adf69ba
│                       │      │                  │       20f5652453729620c4f1c8e4860e (jdk-21.0.7-ga) 
│                       │      │                  ├ [13]: https://github.com/openjdk/jdk8u/commit/3cdd3081565d8
│                       │      │                  │       90801a27a1f9ac8bc53e5711ce6 (jdk8u452-b08) 
│                       │      │                  ├ [14]: https://linux.oracle.com/cve/CVE-2025-21587.html 
│                       │      │                  ├ [15]: https://linux.oracle.com/errata/ELSA-2025-7508.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2025-21587 
│                       │      │                  ├ [17]: https://openjdk.org/groups/vulnerability/advisories/2
│                       │      │                  │       025-04-15 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-7480-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7481-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7482-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-7483-1 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7484-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7531-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7533-1 
│                       │      │                  ├ [25]: https://www.cve.org/CVERecord?id=CVE-2025-21587 
│                       │      │                  ╰ [26]: https://www.oracle.com/security-alerts/cpuapr2025.html 
│                       │      ├ PublishedDate   : 2025-04-15T21:15:54.293Z 
│                       │      ╰ LastModifiedDate: 2025-04-29T20:03:13.79Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2025-23083 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.6_p7-r0?ar
│                       │      │                  │       ch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : d2e38af626fba367 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.7_p6-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-23083 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : nodejs: Node.js Worker Thread Exposure via Diagnostics Channel 
│                       │      ├ Description     : With the aid of the diagnostics_channel utility, an event
│                       │      │                   can be hooked into whenever a worker thread is created. This
│                       │      │                    is not limited only to workers but also exposes internal
│                       │      │                   workers, where an instance of them can be fetched, and its
│                       │      │                   constructor can be grabbed and reinstated for malicious
│                       │      │                   usage. 
│                       │      │                   
│                       │      │                   This vulnerability affects Permission Model users
│                       │      │                   (--permission) on Node.js v20, v22, and v23. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.0/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 7.7 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.0/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 7.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:1613 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-23083 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2339176 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2339392 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2342618 
│                       │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2025-1613.html 
│                       │      │                  ├ [6] : https://github.com/nodejs/node/commit/51938f023aac90d
│                       │      │                  │       c1dc0bc1f743501788613210e 
│                       │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2025-23083.html 
│                       │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2025-1613.html 
│                       │      │                  ├ [9] : https://nodejs.org/en/blog/vulnerability/january-2025
│                       │      │                  │       -security-releases 
│                       │      │                  ├ [10]: https://nodejs.org/en/blog/vulnerability/january-2025
│                       │      │                  │       -security-releases#worker-permission-bypass-via-inter
│                       │      │                  │       nalworker-leak-in-diagnostics-cve-2025-23083---high 
│                       │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2025-23083 
│                       │      │                  ├ [12]: https://security.netapp.com/advisory/ntap-20250228-00
│                       │      │                  │       08/ 
│                       │      │                  ├ [13]: https://www.cve.org/CVERecord?id=CVE-2025-23083 
│                       │      │                  ├ [14]: https://www.vicarius.io/vsociety/posts/cve-2025-23083
│                       │      │                  │       -detect-nodejs-vulnerability 
│                       │      │                  ╰ [15]: https://www.vicarius.io/vsociety/posts/cve-2025-23083
│                       │      │                          -mitigate-nodejs-vulnerability 
│                       │      ├ PublishedDate   : 2025-01-22T02:15:33.93Z 
│                       │      ╰ LastModifiedDate: 2025-07-22T16:15:26.76Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2025-30749 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.6_p7-r0?ar
│                       │      │                  │       ch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : d2e38af626fba367 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.8_p9-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-30749 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Better Glyph drawing (Oracle CPU 2025-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u451, 8u451-perf, 11.0.27, 17.0.15, 21.0.7,
│                       │      │                    24.0.1; Oracle GraalVM for JDK: 17.0.15, 21.0.7 and 
│                       │      │                   24.0.1; Oracle GraalVM Enterprise Edition: 21.3.14.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in takeover of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. This vulnerability
│                       │      │                   does not apply to Java deployments, typically in servers,
│                       │      │                   that load and run only trusted code (e.g., code installed by
│                       │      │                    an administrator). CVSS 3.1 Base Score 8.1
│                       │      │                   (Confidentiality, Integrity and Availability impacts).  CVSS
│                       │      │                    Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 8.1 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10873 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-30749 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2376783 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2376784 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2376785 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2379031 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30749 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30754 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50059 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50106 
│                       │      │                  ├ [10]: https://errata.almalinux.org/9/ALSA-2025-10873.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2025:10867 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2025-30749.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2025-10873.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2025-30749 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-7667-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7668-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-7669-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-7672-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7673-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7674-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-7690-1 
│                       │      │                  ├ [22]: https://www.cve.org/CVERecord?id=CVE-2025-30749 
│                       │      │                  ├ [23]: https://www.oracle.com/security-alerts/cpujul2025.html 
│                       │      │                  ╰ [24]: https://www.oracle.com/security-alerts/cpujul2025.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2025-07-15T20:15:29.313Z 
│                       │      ╰ LastModifiedDate: 2025-08-04T21:05:34.533Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2025-50059 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.6_p7-r0?ar
│                       │      │                  │       ch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : d2e38af626fba367 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.8_p9-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-50059 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Improve HTTP client header handling (Oracle CPU
│                       │      │                   2025-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Networking).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u451-perf, 11.0.27, 17.0.15,
│                       │      │                   21.0.7, 24.0.1; Oracle GraalVM for JDK: 17.0.15, 21.0.7 and 
│                       │      │                    24.0.1; Oracle GraalVM Enterprise Edition: 21.3.14. Easily
│                       │      │                   exploitable vulnerability allows unauthenticated attacker
│                       │      │                   with network access via multiple protocols to compromise
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition.  While the vulnerability is in Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition, attacks may significantly impact additional
│                       │      │                   products (scope change).  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized access to critical
│                       │      │                    data or complete access to all Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability applies to Java
│                       │      │                   deployments, typically in clients running sandboxed Java Web
│                       │      │                    Start applications or sandboxed Java applets, that load and
│                       │      │                    run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. This
│                       │      │                   vulnerability does not apply to Java deployments, typically
│                       │      │                   in servers, that load and run only trusted code (e.g., code
│                       │      │                   installed by an administrator). CVSS 3.1 Base Score 8.6
│                       │      │                   (Confidentiality impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 8.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10873 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-50059 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2376783 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2376784 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2376785 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2379031 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30749 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30754 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50059 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50106 
│                       │      │                  ├ [10]: https://errata.almalinux.org/9/ALSA-2025-10873.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2025:10867 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2025-50059.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2025-10873.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2025-50059 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-7668-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7669-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-7672-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-7673-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7674-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7690-1 
│                       │      │                  ├ [21]: https://www.cve.org/CVERecord?id=CVE-2025-50059 
│                       │      │                  ├ [22]: https://www.oracle.com/security-alerts/cpujul2025.html 
│                       │      │                  ╰ [23]: https://www.oracle.com/security-alerts/cpujul2025.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2025-07-15T20:15:40.367Z 
│                       │      ╰ LastModifiedDate: 2025-08-04T21:17:16.467Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2025-50106 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.6_p7-r0?ar
│                       │      │                  │       ch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : d2e38af626fba367 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.8_p9-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-50106 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Glyph out-of-memory access and crash (Oracle CPU
│                       │      │                   2025-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u451, 8u451-perf, 11.0.27, 17.0.15, 21.0.7,
│                       │      │                    24.0.1; Oracle GraalVM for JDK: 17.0.15, 21.0.7 and 
│                       │      │                   24.0.1; Oracle GraalVM Enterprise Edition: 21.3.14.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in takeover of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 8.1 (Confidentiality, Integrity and
│                       │      │                   Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 8.1 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10873 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-50106 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2376783 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2376784 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2376785 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2379031 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30749 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30754 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50059 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50106 
│                       │      │                  ├ [10]: https://errata.almalinux.org/9/ALSA-2025-10873.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2025:10867 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2025-50106.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2025-10873.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2025-50106 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-7667-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7668-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-7669-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-7672-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7673-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7674-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-7690-1 
│                       │      │                  ├ [22]: https://www.cve.org/CVERecord?id=CVE-2025-50106 
│                       │      │                  ├ [23]: https://www.oracle.com/security-alerts/cpujul2025.html 
│                       │      │                  ╰ [24]: https://www.oracle.com/security-alerts/cpujul2025.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2025-07-15T20:15:47.013Z 
│                       │      ╰ LastModifiedDate: 2025-08-04T21:20:26.203Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2025-30691 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.6_p7-r0?ar
│                       │      │                  │       ch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : d2e38af626fba367 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.7_p6-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-30691 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Improve compiler transformations (Oracle CPU 2025-04) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: Compiler). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   21.0.6, 24; Oracle GraalVM for JDK: 21.0.6 and  24.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE accessible data as
│                       │      │                   well as  unauthorized read access to a subset of Oracle Java
│                       │      │                    SE accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 4.8
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:3855 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-30691 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2359693 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2359694 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2359695 
│                       │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-21587 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30691 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30698 
│                       │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2025-3855.html 
│                       │      │                  ├ [9] : https://errata.rockylinux.org/RLSA-2025:3855 
│                       │      │                  ├ [10]: https://github.com/openjdk/jdk11u/commit/2b70822671cf
│                       │      │                  │       5f9b37956949421e7c77da082c8e (jdk-11.0.27-ga) 
│                       │      │                  ├ [11]: https://github.com/openjdk/jdk17u/commit/5b0a5f436fb9
│                       │      │                  │       817d679f64302b37543bf160d43d (jdk-17.0.15-ga) 
│                       │      │                  ├ [12]: https://github.com/openjdk/jdk21u/commit/11067d7e975c
│                       │      │                  │       e71bedbfdd314519ec9ff689a7e7 (jdk-21.0.7-ga) 
│                       │      │                  ├ [13]: https://github.com/openjdk/jdk8u/commit/949c6ffc54efa
│                       │      │                  │       a92d6559a3e7897432b95e99253 (jdk8u452-b08) 
│                       │      │                  ├ [14]: https://linux.oracle.com/cve/CVE-2025-30691.html 
│                       │      │                  ├ [15]: https://linux.oracle.com/errata/ELSA-2025-7508.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2025-30691 
│                       │      │                  ├ [17]: https://openjdk.org/groups/vulnerability/advisories/2
│                       │      │                  │       025-04-15 
│                       │      │                  ├ [18]: https://security.netapp.com/advisory/ntap-20250418-00
│                       │      │                  │       04/ 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7480-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7481-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-7482-1 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7483-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7484-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7531-1 
│                       │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-7533-1 
│                       │      │                  ├ [26]: https://www.cve.org/CVERecord?id=CVE-2025-30691 
│                       │      │                  ╰ [27]: https://www.oracle.com/security-alerts/cpuapr2025.html 
│                       │      ├ PublishedDate   : 2025-04-15T21:15:58.36Z 
│                       │      ╰ LastModifiedDate: 2025-04-19T01:15:44.85Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2025-30698 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.6_p7-r0?ar
│                       │      │                  │       ch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : d2e38af626fba367 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.7_p6-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-30698 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Enhance Buffered Image handling (Oracle CPU 2025-04) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u441, 8u441-perf, 11.0.26, 17.0.14, 21.0.6,
│                       │      │                    24; Oracle GraalVM for JDK: 17.0.14, 21.0.6, 24; Oracle
│                       │      │                   GraalVM Enterprise Edition: 20.3.17 and  21.3.13. Difficult
│                       │      │                   to exploit vulnerability allows unauthenticated attacker
│                       │      │                   with network access via multiple protocols to compromise
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data as
│                       │      │                   well as  unauthorized read access to a subset of Oracle Java
│                       │      │                    SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data and unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. This vulnerability
│                       │      │                   does not apply to Java deployments, typically in servers,
│                       │      │                   that load and run only trusted code (e.g., code installed by
│                       │      │                    an administrator). CVSS 3.1 Base Score 5.6
│                       │      │                   (Confidentiality, Integrity and Availability impacts).  CVSS
│                       │      │                    Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:3855 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-30698 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2359693 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2359694 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2359695 
│                       │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-21587 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30691 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30698 
│                       │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2025-3855.html 
│                       │      │                  ├ [9] : https://errata.rockylinux.org/RLSA-2025:3855 
│                       │      │                  ├ [10]: https://github.com/openjdk/jdk11u/commit/ea1389c97182
│                       │      │                  │       7876134a6d1d3ab2934681e9f3d6 (jdk-11.0.27-ga) 
│                       │      │                  ├ [11]: https://github.com/openjdk/jdk17u/commit/0a89eb258833
│                       │      │                  │       4226531e8e25ac340eabbc00bd6d (jdk-17.0.15-ga) 
│                       │      │                  ├ [12]: https://github.com/openjdk/jdk21u/commit/3048e287d8ea
│                       │      │                  │       7d5e0d19d9188eb4212801ebf2a2 (jdk-21.0.7-ga) 
│                       │      │                  ├ [13]: https://github.com/openjdk/jdk8u/commit/68d10daabaf9c
│                       │      │                  │       939a5d2e665994c6d348f38cfd5 (jdk8u452-b08) 
│                       │      │                  ├ [14]: https://linux.oracle.com/cve/CVE-2025-30698.html 
│                       │      │                  ├ [15]: https://linux.oracle.com/errata/ELSA-2025-7508.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2025-30698 
│                       │      │                  ├ [17]: https://openjdk.org/groups/vulnerability/advisories/2
│                       │      │                  │       025-04-15 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-7480-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7481-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7482-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-7483-1 
│                       │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-7484-1 
│                       │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-7531-1 
│                       │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-7533-1 
│                       │      │                  ├ [25]: https://www.cve.org/CVERecord?id=CVE-2025-30698 
│                       │      │                  ╰ [26]: https://www.oracle.com/security-alerts/cpuapr2025.html 
│                       │      ├ PublishedDate   : 2025-04-15T21:15:59.137Z 
│                       │      ╰ LastModifiedDate: 2025-04-29T20:03:21.7Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2025-30754 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.6_p7-r0?ar
│                       │      │                  │       ch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : d2e38af626fba367 
│                       │      ├ InstalledVersion: 21.0.6_p7-r0 
│                       │      ├ FixedVersion    : 21.0.8_p9-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-30754 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : openjdk: Enhance TLS protocol support (Oracle CPU 2025-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 8u451, 8u451-perf, 11.0.27, 17.0.15,
│                       │      │                   21.0.7, 24.0.1; Oracle GraalVM for JDK: 17.0.15, 21.0.7 and 
│                       │      │                    24.0.1; Oracle GraalVM Enterprise Edition: 21.3.14.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via TLS to compromise Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition.  Successful attacks of this vulnerability can
│                       │      │                   result in  unauthorized update, insert or delete access to
│                       │      │                   some of Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition accessible data as well as 
│                       │      │                   unauthorized read access to a subset of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data. Note: This vulnerability applies to Java
│                       │      │                   deployments, typically in clients running sandboxed Java Web
│                       │      │                    Start applications or sandboxed Java applets, that load and
│                       │      │                    run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. This
│                       │      │                   vulnerability does not apply to Java deployments, typically
│                       │      │                   in servers, that load and run only trusted code (e.g., code
│                       │      │                   installed by an administrator). CVSS 3.1 Base Score 4.8
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10873 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-30754 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=2376783 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2376784 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2376785 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2379031 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30749 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-30754 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50059 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-50106 
│                       │      │                  ├ [10]: https://errata.almalinux.org/9/ALSA-2025-10873.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2025:10867 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2025-30754.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2025-10873.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2025-30754 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-7667-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7668-1 
│                       │      │                  ├ [17]: https://ubuntu.com/security/notices/USN-7669-1 
│                       │      │                  ├ [18]: https://ubuntu.com/security/notices/USN-7672-1 
│                       │      │                  ├ [19]: https://ubuntu.com/security/notices/USN-7673-1 
│                       │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-7674-1 
│                       │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-7690-1 
│                       │      │                  ├ [22]: https://www.cve.org/CVERecord?id=CVE-2025-30754 
│                       │      │                  ├ [23]: https://www.oracle.com/security-alerts/cpujul2025.html 
│                       │      │                  ╰ [24]: https://www.oracle.com/security-alerts/cpujul2025.htm
│                       │      │                          l#AppendixJAVA 
│                       │      ├ PublishedDate   : 2025-07-15T20:15:29.973Z 
│                       │      ╰ LastModifiedDate: 2025-08-04T21:16:20.84Z 
│                       ├ [18] ╭ VulnerabilityID : CVE-2024-12718 
│                       │      ├ PkgID           : pyc@3.12.9-r0 
│                       │      ├ PkgName         : pyc 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/pyc@3.12.9-r0?arch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : 41758a8c4cd5d746 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-12718 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: Bypass extraction filter to modify file
│                       │      │                   metadata outside extraction directory 
│                       │      ├ Description     : Allows modifying some file metadata (e.g. last modified)
│                       │      │                   with filter="data" or file permissions (chmod) with
│                       │      │                   filter="tar" of files outside the extraction directory.
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information. Only Python versions
│                       │      │                   3.12 or later are affected by these vulnerabilities, earlier
│                       │      │                    versions don't include the extraction filter feature.
│                       │      │                   
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           L/A:N 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:
│                       │      │                            │           H/A:L 
│                       │      │                            ╰ V3Score : 7.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-12718 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/127987 
│                       │      │                  ├ [30]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [31]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2024-12718.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [34]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [35]: https://nvd.nist.gov/vuln/detail/CVE-2024-12718 
│                       │      │                  ├ [36]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [37]: https://www.cve.org/CVERecord?id=CVE-2024-12718 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.183Z 
│                       │      ╰ LastModifiedDate: 2025-07-24T16:15:29.157Z 
│                       ├ [19] ╭ VulnerabilityID : CVE-2025-4138 
│                       │      ├ PkgID           : pyc@3.12.9-r0 
│                       │      ├ PkgName         : pyc 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/pyc@3.12.9-r0?arch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : 41758a8c4cd5d746 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4138 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: Bypassing extraction filter to create
│                       │      │                   symlinks to arbitrary targets outside extraction directory 
│                       │      ├ Description     : Allows the extraction filter to be ignored, allowing symlink
│                       │      │                    targets to point outside the destination directory, and the
│                       │      │                    modification of some file metadata.
│                       │      │                   
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information.
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                  │         │           N/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                            │           N/A:N 
│                       │      │                            ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-4138 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [30]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2025-4138.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [33]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2025-4138 
│                       │      │                  ├ [35]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [36]: https://www.cve.org/CVERecord?id=CVE-2025-4138 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.377Z 
│                       │      ╰ LastModifiedDate: 2025-06-05T14:15:32.767Z 
│                       ├ [20] ╭ VulnerabilityID : CVE-2025-4330 
│                       │      ├ PkgID           : pyc@3.12.9-r0 
│                       │      ├ PkgName         : pyc 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/pyc@3.12.9-r0?arch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : 41758a8c4cd5d746 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4330 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: Extraction filter bypass for linking
│                       │      │                   outside extraction directory 
│                       │      ├ Description     : Allows the extraction filter to be ignored, allowing symlink
│                       │      │                    targets to point outside the destination directory, and the
│                       │      │                    modification of some file metadata.
│                       │      │                   
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information.
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 7.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-4330 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [30]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2025-4330.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [33]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2025-4330 
│                       │      │                  ├ [35]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [36]: https://www.cve.org/CVERecord?id=CVE-2025-4330 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.503Z 
│                       │      ╰ LastModifiedDate: 2025-06-05T14:15:32.91Z 
│                       ├ [21] ╭ VulnerabilityID : CVE-2025-4517 
│                       │      ├ PkgID           : pyc@3.12.9-r0 
│                       │      ├ PkgName         : pyc 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/pyc@3.12.9-r0?arch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : 41758a8c4cd5d746 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4517 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : python: cpython: Arbitrary writes via tarfile realpath
│                       │      │                   overflow 
│                       │      ├ Description     : Allows arbitrary filesystem writes outside the extraction
│                       │      │                   directory during extraction with filter="data".
│                       │      │                   
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information.
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ bitnami    : 4 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 4 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                  │         │           H/A:L 
│                       │      │                  │         ╰ V3Score : 9.4 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:
│                       │      │                            │           H/A:L 
│                       │      │                            ╰ V3Score : 7.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-4517 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [30]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2025-4517.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [33]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2025-4517 
│                       │      │                  ├ [35]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [36]: https://www.cve.org/CVERecord?id=CVE-2025-4517 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.837Z 
│                       │      ╰ LastModifiedDate: 2025-06-05T14:15:33.05Z 
│                       ├ [22] ╭ VulnerabilityID : CVE-2025-4516 
│                       │      ├ PkgID           : pyc@3.12.9-r0 
│                       │      ├ PkgName         : pyc 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/pyc@3.12.9-r0?arch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : 41758a8c4cd5d746 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.10-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4516 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: CPython DecodeError Handling Vulnerability 
│                       │      ├ Description     : There is an issue in CPython when using
│                       │      │                   `bytes.decode("unicode_escape", error="ignore|replace")`. If
│                       │      │                    you are not using the "unicode_escape" encoding or an error
│                       │      │                    handler your usage is not affected. To work-around this
│                       │      │                   issue you may stop using the error= handler and instead wrap
│                       │      │                    the bytes.decode() call in a try-except catching the
│                       │      │                   DecodeError. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-416 
│                       │      ├ VendorSeverity   ╭ amazon     : 3 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.1 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2025/05/16/4 
│                       │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2025/05/19/1 
│                       │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2025-4516 
│                       │      │                  ├ [3] : https://github.com/python/cpython/commit/4398b788ffc1
│                       │      │                  │       f954a2c552da285477d42a571292 
│                       │      │                  ├ [4] : https://github.com/python/cpython/commit/564664867829
│                       │      │                  │       5a44aa82636c6e92826651baf33a 
│                       │      │                  ├ [5] : https://github.com/python/cpython/commit/6279eb8c076d
│                       │      │                  │       89d3739a6edb393e43c7929b429d 
│                       │      │                  ├ [6] : https://github.com/python/cpython/commit/69b4387f78f4
│                       │      │                  │       13e8c47572a85b3478c47eba8142 
│                       │      │                  ├ [7] : https://github.com/python/cpython/commit/73b3040f5924
│                       │      │                  │       36385007918887b7e2132aa8431f 
│                       │      │                  ├ [8] : https://github.com/python/cpython/commit/8d35fd1b3493
│                       │      │                  │       5221aff23a1ab69a429dd156be77 
│                       │      │                  ├ [9] : https://github.com/python/cpython/commit/9f69a58623bd
│                       │      │                  │       01349a18ba0c7a9cb1dad6a51e8e 
│                       │      │                  ├ [10]: https://github.com/python/cpython/commit/9f69a58623bd
│                       │      │                  │       01349a18ba0c7a9cb1dad6a51e8e (main) 
│                       │      │                  ├ [11]: https://github.com/python/cpython/commit/ab9893c40609
│                       │      │                  │       935e0d40a6d2a7307ea51aec598b 
│                       │      │                  ├ [12]: https://github.com/python/cpython/issues/133767 
│                       │      │                  ├ [13]: https://github.com/python/cpython/pull/129648 
│                       │      │                  ├ [14]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/L75IPBBTSCYEF56I2M4KIW353BB3AY74
│                       │      │                  │       / 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2025-4516 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7570-1 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2025-4516 
│                       │      ├ PublishedDate   : 2025-05-15T14:15:31.753Z 
│                       │      ╰ LastModifiedDate: 2025-06-03T14:15:49.697Z 
│                       ├ [23] ╭ VulnerabilityID : CVE-2024-12718 
│                       │      ├ PkgID           : python3@3.12.9-r0 
│                       │      ├ PkgName         : python3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3@3.12.9-r0?arch=x86_64&distro=3
│                       │      │                  │       .21.3 
│                       │      │                  ╰ UID : a21f36526a870334 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-12718 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: Bypass extraction filter to modify file
│                       │      │                   metadata outside extraction directory 
│                       │      ├ Description     : Allows modifying some file metadata (e.g. last modified)
│                       │      │                   with filter="data" or file permissions (chmod) with
│                       │      │                   filter="tar" of files outside the extraction directory.
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information. Only Python versions
│                       │      │                   3.12 or later are affected by these vulnerabilities, earlier
│                       │      │                    versions don't include the extraction filter feature.
│                       │      │                   
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           L/A:N 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:
│                       │      │                            │           H/A:L 
│                       │      │                            ╰ V3Score : 7.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-12718 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/127987 
│                       │      │                  ├ [30]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [31]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2024-12718.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [34]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [35]: https://nvd.nist.gov/vuln/detail/CVE-2024-12718 
│                       │      │                  ├ [36]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [37]: https://www.cve.org/CVERecord?id=CVE-2024-12718 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.183Z 
│                       │      ╰ LastModifiedDate: 2025-07-24T16:15:29.157Z 
│                       ├ [24] ╭ VulnerabilityID : CVE-2025-4138 
│                       │      ├ PkgID           : python3@3.12.9-r0 
│                       │      ├ PkgName         : python3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3@3.12.9-r0?arch=x86_64&distro=3
│                       │      │                  │       .21.3 
│                       │      │                  ╰ UID : a21f36526a870334 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4138 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: Bypassing extraction filter to create
│                       │      │                   symlinks to arbitrary targets outside extraction directory 
│                       │      ├ Description     : Allows the extraction filter to be ignored, allowing symlink
│                       │      │                    targets to point outside the destination directory, and the
│                       │      │                    modification of some file metadata.
│                       │      │                   
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information.
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                  │         │           N/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                            │           N/A:N 
│                       │      │                            ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-4138 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [30]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2025-4138.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [33]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2025-4138 
│                       │      │                  ├ [35]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [36]: https://www.cve.org/CVERecord?id=CVE-2025-4138 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.377Z 
│                       │      ╰ LastModifiedDate: 2025-06-05T14:15:32.767Z 
│                       ├ [25] ╭ VulnerabilityID : CVE-2025-4330 
│                       │      ├ PkgID           : python3@3.12.9-r0 
│                       │      ├ PkgName         : python3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3@3.12.9-r0?arch=x86_64&distro=3
│                       │      │                  │       .21.3 
│                       │      │                  ╰ UID : a21f36526a870334 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4330 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: Extraction filter bypass for linking
│                       │      │                   outside extraction directory 
│                       │      ├ Description     : Allows the extraction filter to be ignored, allowing symlink
│                       │      │                    targets to point outside the destination directory, and the
│                       │      │                    modification of some file metadata.
│                       │      │                   
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information.
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 7.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-4330 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [30]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2025-4330.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [33]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2025-4330 
│                       │      │                  ├ [35]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [36]: https://www.cve.org/CVERecord?id=CVE-2025-4330 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.503Z 
│                       │      ╰ LastModifiedDate: 2025-06-05T14:15:32.91Z 
│                       ├ [26] ╭ VulnerabilityID : CVE-2025-4517 
│                       │      ├ PkgID           : python3@3.12.9-r0 
│                       │      ├ PkgName         : python3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3@3.12.9-r0?arch=x86_64&distro=3
│                       │      │                  │       .21.3 
│                       │      │                  ╰ UID : a21f36526a870334 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4517 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : python: cpython: Arbitrary writes via tarfile realpath
│                       │      │                   overflow 
│                       │      ├ Description     : Allows arbitrary filesystem writes outside the extraction
│                       │      │                   directory during extraction with filter="data".
│                       │      │                   
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information.
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ bitnami    : 4 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 4 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                  │         │           H/A:L 
│                       │      │                  │         ╰ V3Score : 9.4 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:
│                       │      │                            │           H/A:L 
│                       │      │                            ╰ V3Score : 7.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-4517 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [30]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2025-4517.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [33]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2025-4517 
│                       │      │                  ├ [35]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [36]: https://www.cve.org/CVERecord?id=CVE-2025-4517 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.837Z 
│                       │      ╰ LastModifiedDate: 2025-06-05T14:15:33.05Z 
│                       ├ [27] ╭ VulnerabilityID : CVE-2025-4516 
│                       │      ├ PkgID           : python3@3.12.9-r0 
│                       │      ├ PkgName         : python3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3@3.12.9-r0?arch=x86_64&distro=3
│                       │      │                  │       .21.3 
│                       │      │                  ╰ UID : a21f36526a870334 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.10-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4516 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: CPython DecodeError Handling Vulnerability 
│                       │      ├ Description     : There is an issue in CPython when using
│                       │      │                   `bytes.decode("unicode_escape", error="ignore|replace")`. If
│                       │      │                    you are not using the "unicode_escape" encoding or an error
│                       │      │                    handler your usage is not affected. To work-around this
│                       │      │                   issue you may stop using the error= handler and instead wrap
│                       │      │                    the bytes.decode() call in a try-except catching the
│                       │      │                   DecodeError. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-416 
│                       │      ├ VendorSeverity   ╭ amazon     : 3 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.1 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2025/05/16/4 
│                       │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2025/05/19/1 
│                       │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2025-4516 
│                       │      │                  ├ [3] : https://github.com/python/cpython/commit/4398b788ffc1
│                       │      │                  │       f954a2c552da285477d42a571292 
│                       │      │                  ├ [4] : https://github.com/python/cpython/commit/564664867829
│                       │      │                  │       5a44aa82636c6e92826651baf33a 
│                       │      │                  ├ [5] : https://github.com/python/cpython/commit/6279eb8c076d
│                       │      │                  │       89d3739a6edb393e43c7929b429d 
│                       │      │                  ├ [6] : https://github.com/python/cpython/commit/69b4387f78f4
│                       │      │                  │       13e8c47572a85b3478c47eba8142 
│                       │      │                  ├ [7] : https://github.com/python/cpython/commit/73b3040f5924
│                       │      │                  │       36385007918887b7e2132aa8431f 
│                       │      │                  ├ [8] : https://github.com/python/cpython/commit/8d35fd1b3493
│                       │      │                  │       5221aff23a1ab69a429dd156be77 
│                       │      │                  ├ [9] : https://github.com/python/cpython/commit/9f69a58623bd
│                       │      │                  │       01349a18ba0c7a9cb1dad6a51e8e 
│                       │      │                  ├ [10]: https://github.com/python/cpython/commit/9f69a58623bd
│                       │      │                  │       01349a18ba0c7a9cb1dad6a51e8e (main) 
│                       │      │                  ├ [11]: https://github.com/python/cpython/commit/ab9893c40609
│                       │      │                  │       935e0d40a6d2a7307ea51aec598b 
│                       │      │                  ├ [12]: https://github.com/python/cpython/issues/133767 
│                       │      │                  ├ [13]: https://github.com/python/cpython/pull/129648 
│                       │      │                  ├ [14]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/L75IPBBTSCYEF56I2M4KIW353BB3AY74
│                       │      │                  │       / 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2025-4516 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7570-1 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2025-4516 
│                       │      ├ PublishedDate   : 2025-05-15T14:15:31.753Z 
│                       │      ╰ LastModifiedDate: 2025-06-03T14:15:49.697Z 
│                       ├ [28] ╭ VulnerabilityID : CVE-2024-12718 
│                       │      ├ PkgID           : python3-pyc@3.12.9-r0 
│                       │      ├ PkgName         : python3-pyc 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3-pyc@3.12.9-r0?arch=x86_64&dist
│                       │      │                  │       ro=3.21.3 
│                       │      │                  ╰ UID : 2bcc0db22fc4228 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-12718 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: Bypass extraction filter to modify file
│                       │      │                   metadata outside extraction directory 
│                       │      ├ Description     : Allows modifying some file metadata (e.g. last modified)
│                       │      │                   with filter="data" or file permissions (chmod) with
│                       │      │                   filter="tar" of files outside the extraction directory.
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information. Only Python versions
│                       │      │                   3.12 or later are affected by these vulnerabilities, earlier
│                       │      │                    versions don't include the extraction filter feature.
│                       │      │                   
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           L/A:N 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:
│                       │      │                            │           H/A:L 
│                       │      │                            ╰ V3Score : 7.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-12718 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/127987 
│                       │      │                  ├ [30]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [31]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2024-12718.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [34]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [35]: https://nvd.nist.gov/vuln/detail/CVE-2024-12718 
│                       │      │                  ├ [36]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [37]: https://www.cve.org/CVERecord?id=CVE-2024-12718 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.183Z 
│                       │      ╰ LastModifiedDate: 2025-07-24T16:15:29.157Z 
│                       ├ [29] ╭ VulnerabilityID : CVE-2025-4138 
│                       │      ├ PkgID           : python3-pyc@3.12.9-r0 
│                       │      ├ PkgName         : python3-pyc 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3-pyc@3.12.9-r0?arch=x86_64&dist
│                       │      │                  │       ro=3.21.3 
│                       │      │                  ╰ UID : 2bcc0db22fc4228 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4138 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: Bypassing extraction filter to create
│                       │      │                   symlinks to arbitrary targets outside extraction directory 
│                       │      ├ Description     : Allows the extraction filter to be ignored, allowing symlink
│                       │      │                    targets to point outside the destination directory, and the
│                       │      │                    modification of some file metadata.
│                       │      │                   
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information.
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                  │         │           N/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                            │           N/A:N 
│                       │      │                            ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-4138 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [30]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2025-4138.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [33]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2025-4138 
│                       │      │                  ├ [35]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [36]: https://www.cve.org/CVERecord?id=CVE-2025-4138 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.377Z 
│                       │      ╰ LastModifiedDate: 2025-06-05T14:15:32.767Z 
│                       ├ [30] ╭ VulnerabilityID : CVE-2025-4330 
│                       │      ├ PkgID           : python3-pyc@3.12.9-r0 
│                       │      ├ PkgName         : python3-pyc 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3-pyc@3.12.9-r0?arch=x86_64&dist
│                       │      │                  │       ro=3.21.3 
│                       │      │                  ╰ UID : 2bcc0db22fc4228 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4330 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: Extraction filter bypass for linking
│                       │      │                   outside extraction directory 
│                       │      ├ Description     : Allows the extraction filter to be ignored, allowing symlink
│                       │      │                    targets to point outside the destination directory, and the
│                       │      │                    modification of some file metadata.
│                       │      │                   
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information.
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 7.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-4330 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [30]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2025-4330.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [33]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2025-4330 
│                       │      │                  ├ [35]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [36]: https://www.cve.org/CVERecord?id=CVE-2025-4330 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.503Z 
│                       │      ╰ LastModifiedDate: 2025-06-05T14:15:32.91Z 
│                       ├ [31] ╭ VulnerabilityID : CVE-2025-4517 
│                       │      ├ PkgID           : python3-pyc@3.12.9-r0 
│                       │      ├ PkgName         : python3-pyc 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3-pyc@3.12.9-r0?arch=x86_64&dist
│                       │      │                  │       ro=3.21.3 
│                       │      │                  ╰ UID : 2bcc0db22fc4228 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4517 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : python: cpython: Arbitrary writes via tarfile realpath
│                       │      │                   overflow 
│                       │      ├ Description     : Allows arbitrary filesystem writes outside the extraction
│                       │      │                   directory during extraction with filter="data".
│                       │      │                   
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information.
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ bitnami    : 4 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 4 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                  │         │           H/A:L 
│                       │      │                  │         ╰ V3Score : 9.4 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:
│                       │      │                            │           H/A:L 
│                       │      │                            ╰ V3Score : 7.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-4517 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [30]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2025-4517.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [33]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2025-4517 
│                       │      │                  ├ [35]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [36]: https://www.cve.org/CVERecord?id=CVE-2025-4517 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.837Z 
│                       │      ╰ LastModifiedDate: 2025-06-05T14:15:33.05Z 
│                       ├ [32] ╭ VulnerabilityID : CVE-2025-4516 
│                       │      ├ PkgID           : python3-pyc@3.12.9-r0 
│                       │      ├ PkgName         : python3-pyc 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3-pyc@3.12.9-r0?arch=x86_64&dist
│                       │      │                  │       ro=3.21.3 
│                       │      │                  ╰ UID : 2bcc0db22fc4228 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.10-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4516 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: CPython DecodeError Handling Vulnerability 
│                       │      ├ Description     : There is an issue in CPython when using
│                       │      │                   `bytes.decode("unicode_escape", error="ignore|replace")`. If
│                       │      │                    you are not using the "unicode_escape" encoding or an error
│                       │      │                    handler your usage is not affected. To work-around this
│                       │      │                   issue you may stop using the error= handler and instead wrap
│                       │      │                    the bytes.decode() call in a try-except catching the
│                       │      │                   DecodeError. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-416 
│                       │      ├ VendorSeverity   ╭ amazon     : 3 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.1 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2025/05/16/4 
│                       │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2025/05/19/1 
│                       │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2025-4516 
│                       │      │                  ├ [3] : https://github.com/python/cpython/commit/4398b788ffc1
│                       │      │                  │       f954a2c552da285477d42a571292 
│                       │      │                  ├ [4] : https://github.com/python/cpython/commit/564664867829
│                       │      │                  │       5a44aa82636c6e92826651baf33a 
│                       │      │                  ├ [5] : https://github.com/python/cpython/commit/6279eb8c076d
│                       │      │                  │       89d3739a6edb393e43c7929b429d 
│                       │      │                  ├ [6] : https://github.com/python/cpython/commit/69b4387f78f4
│                       │      │                  │       13e8c47572a85b3478c47eba8142 
│                       │      │                  ├ [7] : https://github.com/python/cpython/commit/73b3040f5924
│                       │      │                  │       36385007918887b7e2132aa8431f 
│                       │      │                  ├ [8] : https://github.com/python/cpython/commit/8d35fd1b3493
│                       │      │                  │       5221aff23a1ab69a429dd156be77 
│                       │      │                  ├ [9] : https://github.com/python/cpython/commit/9f69a58623bd
│                       │      │                  │       01349a18ba0c7a9cb1dad6a51e8e 
│                       │      │                  ├ [10]: https://github.com/python/cpython/commit/9f69a58623bd
│                       │      │                  │       01349a18ba0c7a9cb1dad6a51e8e (main) 
│                       │      │                  ├ [11]: https://github.com/python/cpython/commit/ab9893c40609
│                       │      │                  │       935e0d40a6d2a7307ea51aec598b 
│                       │      │                  ├ [12]: https://github.com/python/cpython/issues/133767 
│                       │      │                  ├ [13]: https://github.com/python/cpython/pull/129648 
│                       │      │                  ├ [14]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/L75IPBBTSCYEF56I2M4KIW353BB3AY74
│                       │      │                  │       / 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2025-4516 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7570-1 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2025-4516 
│                       │      ├ PublishedDate   : 2025-05-15T14:15:31.753Z 
│                       │      ╰ LastModifiedDate: 2025-06-03T14:15:49.697Z 
│                       ├ [33] ╭ VulnerabilityID : CVE-2024-12718 
│                       │      ├ PkgID           : python3-pycache-pyc0@3.12.9-r0 
│                       │      ├ PkgName         : python3-pycache-pyc0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3-pycache-pyc0@3.12.9-r0?arch=x8
│                       │      │                  │       6_64&distro=3.21.3 
│                       │      │                  ╰ UID : bfb291a02ec4b24d 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-12718 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: Bypass extraction filter to modify file
│                       │      │                   metadata outside extraction directory 
│                       │      ├ Description     : Allows modifying some file metadata (e.g. last modified)
│                       │      │                   with filter="data" or file permissions (chmod) with
│                       │      │                   filter="tar" of files outside the extraction directory.
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information. Only Python versions
│                       │      │                   3.12 or later are affected by these vulnerabilities, earlier
│                       │      │                    versions don't include the extraction filter feature.
│                       │      │                   
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           L/A:N 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:
│                       │      │                            │           H/A:L 
│                       │      │                            ╰ V3Score : 7.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-12718 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/127987 
│                       │      │                  ├ [30]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [31]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [32]: https://linux.oracle.com/cve/CVE-2024-12718.html 
│                       │      │                  ├ [33]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [34]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [35]: https://nvd.nist.gov/vuln/detail/CVE-2024-12718 
│                       │      │                  ├ [36]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [37]: https://www.cve.org/CVERecord?id=CVE-2024-12718 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.183Z 
│                       │      ╰ LastModifiedDate: 2025-07-24T16:15:29.157Z 
│                       ├ [34] ╭ VulnerabilityID : CVE-2025-4138 
│                       │      ├ PkgID           : python3-pycache-pyc0@3.12.9-r0 
│                       │      ├ PkgName         : python3-pycache-pyc0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3-pycache-pyc0@3.12.9-r0?arch=x8
│                       │      │                  │       6_64&distro=3.21.3 
│                       │      │                  ╰ UID : bfb291a02ec4b24d 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4138 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: Bypassing extraction filter to create
│                       │      │                   symlinks to arbitrary targets outside extraction directory 
│                       │      ├ Description     : Allows the extraction filter to be ignored, allowing symlink
│                       │      │                    targets to point outside the destination directory, and the
│                       │      │                    modification of some file metadata.
│                       │      │                   
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information.
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                  │         │           N/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                            │           N/A:N 
│                       │      │                            ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-4138 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [30]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2025-4138.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [33]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2025-4138 
│                       │      │                  ├ [35]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [36]: https://www.cve.org/CVERecord?id=CVE-2025-4138 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.377Z 
│                       │      ╰ LastModifiedDate: 2025-06-05T14:15:32.767Z 
│                       ├ [35] ╭ VulnerabilityID : CVE-2025-4330 
│                       │      ├ PkgID           : python3-pycache-pyc0@3.12.9-r0 
│                       │      ├ PkgName         : python3-pycache-pyc0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3-pycache-pyc0@3.12.9-r0?arch=x8
│                       │      │                  │       6_64&distro=3.21.3 
│                       │      │                  ╰ UID : bfb291a02ec4b24d 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4330 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: Extraction filter bypass for linking
│                       │      │                   outside extraction directory 
│                       │      ├ Description     : Allows the extraction filter to be ignored, allowing symlink
│                       │      │                    targets to point outside the destination directory, and the
│                       │      │                    modification of some file metadata.
│                       │      │                   
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information.
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 7.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-4330 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [30]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2025-4330.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [33]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2025-4330 
│                       │      │                  ├ [35]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [36]: https://www.cve.org/CVERecord?id=CVE-2025-4330 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.503Z 
│                       │      ╰ LastModifiedDate: 2025-06-05T14:15:32.91Z 
│                       ├ [36] ╭ VulnerabilityID : CVE-2025-4517 
│                       │      ├ PkgID           : python3-pycache-pyc0@3.12.9-r0 
│                       │      ├ PkgName         : python3-pycache-pyc0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3-pycache-pyc0@3.12.9-r0?arch=x8
│                       │      │                  │       6_64&distro=3.21.3 
│                       │      │                  ╰ UID : bfb291a02ec4b24d 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.11-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4517 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : python: cpython: Arbitrary writes via tarfile realpath
│                       │      │                   overflow 
│                       │      ├ Description     : Allows arbitrary filesystem writes outside the extraction
│                       │      │                   directory during extraction with filter="data".
│                       │      │                   
│                       │      │                   You are affected by this vulnerability if using the tarfile
│                       │      │                   module to extract untrusted tar archives using
│                       │      │                   TarFile.extractall() or TarFile.extract() using the filter=
│                       │      │                   parameter with a value of "data" or "tar". See the tarfile 
│                       │      │                   extraction filters documentation
│                       │      │                   https://docs.python.org/3/library/tarfile.html#tarfile-extra
│                       │      │                   ction-filter  for more information.
│                       │      │                   Note that for Python 3.14 or later the default value of
│                       │      │                   filter= changed from "no filtering" to `"data", so if you
│                       │      │                   are relying on this new default behavior then your usage is
│                       │      │                   also affected.
│                       │      │                   Note that none of these vulnerabilities significantly affect
│                       │      │                    the installation of source distributions which are tar
│                       │      │                   archives as source distributions already allow arbitrary
│                       │      │                   code execution during the build process. However when
│                       │      │                   evaluating source distributions it's important to avoid
│                       │      │                   installing source distributions with suspicious links. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ bitnami    : 4 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 4 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │      │                  │         │           H/A:L 
│                       │      │                  │         ╰ V3Score : 9.4 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:
│                       │      │                            │           H/A:L 
│                       │      │                            ╰ V3Score : 7.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:10189 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-4517 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2370010 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2370013 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2370014 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2370016 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/2372426 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2370010 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2370013 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2370014 
│                       │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2370016 
│                       │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2372426 
│                       │      │                  ├ [12]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-12718 
│                       │      │                  ├ [13]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4138 
│                       │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4330 
│                       │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4435 
│                       │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-4517 
│                       │      │                  ├ [17]: https://errata.almalinux.org/9/ALSA-2025-10189.html 
│                       │      │                  ├ [18]: https://errata.rockylinux.org/RLSA-2025:10031 
│                       │      │                  ├ [19]: https://gist.github.com/sethmlarson/52398e33eff261329
│                       │      │                  │       a0180ac1d54f42f 
│                       │      │                  ├ [20]: https://github.com/python/cpython/commit/19de092debb3
│                       │      │                  │       d7e832e5672cc2f7b788d35951da 
│                       │      │                  ├ [21]: https://github.com/python/cpython/commit/28463dba112a
│                       │      │                  │       f719df1e8b0391c46787ad756dd9 
│                       │      │                  ├ [22]: https://github.com/python/cpython/commit/3612d8f51741
│                       │      │                  │       b11f36f8fb0494d79086bac9390a 
│                       │      │                  ├ [23]: https://github.com/python/cpython/commit/4633f3f497b1
│                       │      │                  │       ff70e4a35b6fe2c907cbe2d4cb2e 
│                       │      │                  ├ [24]: https://github.com/python/cpython/commit/98016f7c92aa
│                       │      │                  │       4c1232c68bac1ed6646db31782ec 
│                       │      │                  ├ [25]: https://github.com/python/cpython/commit/9c1110ef6652
│                       │      │                  │       687d7c55f590f909720eddde965a 
│                       │      │                  ├ [26]: https://github.com/python/cpython/commit/9e0ac76d96cf
│                       │      │                  │       80b49055f6d6b9a6763fb9215c2a 
│                       │      │                  ├ [27]: https://github.com/python/cpython/commit/aa9eb5f757ce
│                       │      │                  │       ff461e6e996f12c89e5d9b583b01 
│                       │      │                  ├ [28]: https://github.com/python/cpython/commit/dd8f187d0746
│                       │      │                  │       da151e0025c51680979ac5b4cfb1 
│                       │      │                  ├ [29]: https://github.com/python/cpython/issues/135034 
│                       │      │                  ├ [30]: https://github.com/python/cpython/pull/135037 
│                       │      │                  ├ [31]: https://linux.oracle.com/cve/CVE-2025-4517.html 
│                       │      │                  ├ [32]: https://linux.oracle.com/errata/ELSA-2025-10189.html 
│                       │      │                  ├ [33]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG
│                       │      │                  │       / 
│                       │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2025-4517 
│                       │      │                  ├ [35]: https://ubuntu.com/security/notices/USN-7583-1 
│                       │      │                  ╰ [36]: https://www.cve.org/CVERecord?id=CVE-2025-4517 
│                       │      ├ PublishedDate   : 2025-06-03T13:15:20.837Z 
│                       │      ╰ LastModifiedDate: 2025-06-05T14:15:33.05Z 
│                       ├ [37] ╭ VulnerabilityID : CVE-2025-4516 
│                       │      ├ PkgID           : python3-pycache-pyc0@3.12.9-r0 
│                       │      ├ PkgName         : python3-pycache-pyc0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/python3-pycache-pyc0@3.12.9-r0?arch=x8
│                       │      │                  │       6_64&distro=3.21.3 
│                       │      │                  ╰ UID : bfb291a02ec4b24d 
│                       │      ├ InstalledVersion: 3.12.9-r0 
│                       │      ├ FixedVersion    : 3.12.10-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-4516 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : cpython: python: CPython DecodeError Handling Vulnerability 
│                       │      ├ Description     : There is an issue in CPython when using
│                       │      │                   `bytes.decode("unicode_escape", error="ignore|replace")`. If
│                       │      │                    you are not using the "unicode_escape" encoding or an error
│                       │      │                    handler your usage is not affected. To work-around this
│                       │      │                   issue you may stop using the error= handler and instead wrap
│                       │      │                    the bytes.decode() call in a try-except catching the
│                       │      │                   DecodeError. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-416 
│                       │      ├ VendorSeverity   ╭ amazon     : 3 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.1 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2025/05/16/4 
│                       │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2025/05/19/1 
│                       │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2025-4516 
│                       │      │                  ├ [3] : https://github.com/python/cpython/commit/4398b788ffc1
│                       │      │                  │       f954a2c552da285477d42a571292 
│                       │      │                  ├ [4] : https://github.com/python/cpython/commit/564664867829
│                       │      │                  │       5a44aa82636c6e92826651baf33a 
│                       │      │                  ├ [5] : https://github.com/python/cpython/commit/6279eb8c076d
│                       │      │                  │       89d3739a6edb393e43c7929b429d 
│                       │      │                  ├ [6] : https://github.com/python/cpython/commit/69b4387f78f4
│                       │      │                  │       13e8c47572a85b3478c47eba8142 
│                       │      │                  ├ [7] : https://github.com/python/cpython/commit/73b3040f5924
│                       │      │                  │       36385007918887b7e2132aa8431f 
│                       │      │                  ├ [8] : https://github.com/python/cpython/commit/8d35fd1b3493
│                       │      │                  │       5221aff23a1ab69a429dd156be77 
│                       │      │                  ├ [9] : https://github.com/python/cpython/commit/9f69a58623bd
│                       │      │                  │       01349a18ba0c7a9cb1dad6a51e8e 
│                       │      │                  ├ [10]: https://github.com/python/cpython/commit/9f69a58623bd
│                       │      │                  │       01349a18ba0c7a9cb1dad6a51e8e (main) 
│                       │      │                  ├ [11]: https://github.com/python/cpython/commit/ab9893c40609
│                       │      │                  │       935e0d40a6d2a7307ea51aec598b 
│                       │      │                  ├ [12]: https://github.com/python/cpython/issues/133767 
│                       │      │                  ├ [13]: https://github.com/python/cpython/pull/129648 
│                       │      │                  ├ [14]: https://mail.python.org/archives/list/security-announ
│                       │      │                  │       ce@python.org/thread/L75IPBBTSCYEF56I2M4KIW353BB3AY74
│                       │      │                  │       / 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2025-4516 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7570-1 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2025-4516 
│                       │      ├ PublishedDate   : 2025-05-15T14:15:31.753Z 
│                       │      ╰ LastModifiedDate: 2025-06-03T14:15:49.697Z 
│                       ├ [38] ╭ VulnerabilityID : CVE-2025-3277 
│                       │      ├ PkgID           : sqlite-libs@3.48.0-r0 
│                       │      ├ PkgName         : sqlite-libs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/sqlite-libs@3.48.0-r0?arch=x86_64&dist
│                       │      │                  │       ro=3.21.3 
│                       │      │                  ╰ UID : 22e66f5245d24208 
│                       │      ├ InstalledVersion: 3.48.0-r0 
│                       │      ├ FixedVersion    : 3.48.0-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-3277 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : SQLite: integer overflow in SQLite 
│                       │      ├ Description     : An integer overflow can be triggered in SQLite’s
│                       │      │                   `concat_ws()` function. The resulting, truncated integer is
│                       │      │                   then used to allocate a buffer. When SQLite then writes the
│                       │      │                   resulting string to the buffer, it uses the original,
│                       │      │                   untruncated size and thus a wild Heap Buffer overflow of
│                       │      │                   size ~4GB can be triggered. This can result in arbitrary
│                       │      │                   code execution. 
│                       │      ├ Severity        : CRITICAL 
│                       │      ├ CweIDs           ╭ [0]: CWE-122 
│                       │      │                  ╰ [1]: CWE-190 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ nvd        : 4 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 9.8 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 7.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:7433 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-3277 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2358271 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2359553 
│                       │      │                  ├ [4] : https://errata.almalinux.org/9/ALSA-2025-7433.html 
│                       │      │                  ├ [5] : https://linux.oracle.com/cve/CVE-2025-3277.html 
│                       │      │                  ├ [6] : https://linux.oracle.com/errata/ELSA-2025-7517.html 
│                       │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2025-3277 
│                       │      │                  ├ [8] : https://sqlite.org/src/info/498e3f1cf57f164f 
│                       │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-7528-1 
│                       │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2025-3277 
│                       │      ├ PublishedDate   : 2025-04-14T17:15:27.297Z 
│                       │      ╰ LastModifiedDate: 2025-08-18T21:28:16.38Z 
│                       ├ [39] ╭ VulnerabilityID : CVE-2025-6965 
│                       │      ├ PkgID           : sqlite-libs@3.48.0-r0 
│                       │      ├ PkgName         : sqlite-libs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/sqlite-libs@3.48.0-r0?arch=x86_64&dist
│                       │      │                  │       ro=3.21.3 
│                       │      │                  ╰ UID : 22e66f5245d24208 
│                       │      ├ InstalledVersion: 3.48.0-r0 
│                       │      ├ FixedVersion    : 3.48.0-r3 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-6965 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : sqlite: Integer Truncation in SQLite 
│                       │      ├ Description     : There exists a vulnerability in SQLite versions before
│                       │      │                   3.50.2 where the number of aggregate terms could exceed the
│                       │      │                   number of columns available. This could lead to a memory
│                       │      │                   corruption issue. We recommend upgrading to version 3.50.2
│                       │      │                   or above. 
│                       │      ├ Severity        : CRITICAL 
│                       │      ├ CweIDs           ─ [0]: CWE-197 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ nvd        : 4 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 4 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 9.8 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:L/I:H
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 7.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:11992 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-6965 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2380149 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2380149 
│                       │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-6965 
│                       │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2025-11992.html 
│                       │      │                  ├ [6] : https://errata.rockylinux.org/RLSA-2025:12010 
│                       │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2025-6965.html 
│                       │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2025-14101.html 
│                       │      │                  ├ [9] : https://nvd.nist.gov/vuln/detail/CVE-2025-6965 
│                       │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-7676-1 
│                       │      │                  ├ [11]: https://ubuntu.com/security/notices/USN-7679-1 
│                       │      │                  ├ [12]: https://www.cve.org/CVERecord?id=CVE-2025-6965 
│                       │      │                  ╰ [13]: https://www.sqlite.org/src/info/5508b56fd24016c13981e
│                       │      │                          c280ecdd833007c9d8dd595edb295b984c2b487b5c8 
│                       │      ├ PublishedDate   : 2025-07-15T14:15:31.08Z 
│                       │      ╰ LastModifiedDate: 2025-07-22T17:06:21.51Z 
│                       ├ [40] ╭ VulnerabilityID : CVE-2025-29087 
│                       │      ├ PkgID           : sqlite-libs@3.48.0-r0 
│                       │      ├ PkgName         : sqlite-libs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/sqlite-libs@3.48.0-r0?arch=x86_64&dist
│                       │      │                  │       ro=3.21.3 
│                       │      │                  ╰ UID : 22e66f5245d24208 
│                       │      ├ InstalledVersion: 3.48.0-r0 
│                       │      ├ FixedVersion    : 3.48.0-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-29087 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : sqlite: Integer Overflow in SQLite concat_ws Function 
│                       │      ├ Description     : In SQLite 3.44.0 through 3.49.0 before 3.49.1, the
│                       │      │                   concat_ws() SQL function can cause memory to be written
│                       │      │                   beyond the end of a malloc-allocated buffer. If the
│                       │      │                   separator argument is attacker-controlled and has a large
│                       │      │                   string (e.g., 2MB or more), an integer overflow occurs in
│                       │      │                   calculating the size of the result buffer, and thus malloc
│                       │      │                   may not allocate enough memory. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-190 
│                       │      ├ VendorSeverity   ╭ bitnami: 3 
│                       │      │                  ├ nvd    : 3 
│                       │      │                  ├ redhat : 2 
│                       │      │                  ╰ ubuntu : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ├ nvd     ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:H 
│                       │      │                            ╰ V3Score : 5.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-29087 
│                       │      │                  ├ [1]: https://gist.github.com/ylwango613/a44a29f1ef074fa783e
│                       │      │                  │      29f04a0afd62a 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2025-29087 
│                       │      │                  ├ [3]: https://sqlite.org/releaselog/3_49_1.html 
│                       │      │                  ├ [4]: https://ubuntu.com/security/notices/USN-7528-1 
│                       │      │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2025-29087 
│                       │      │                  ╰ [6]: https://www.sqlite.org/cves.html 
│                       │      ├ PublishedDate   : 2025-04-07T20:15:20.253Z 
│                       │      ╰ LastModifiedDate: 2025-04-30T12:43:22.31Z 
│                       ├ [41] ╭ VulnerabilityID : CVE-2025-29088 
│                       │      ├ PkgID           : sqlite-libs@3.48.0-r0 
│                       │      ├ PkgName         : sqlite-libs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/sqlite-libs@3.48.0-r0?arch=x86_64&dist
│                       │      │                  │       ro=3.21.3 
│                       │      │                  ╰ UID : 22e66f5245d24208 
│                       │      ├ InstalledVersion: 3.48.0-r0 
│                       │      ├ FixedVersion    : 3.48.0-r4 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-29088 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : sqlite: Denial of Service in SQLite 
│                       │      ├ Description     : In SQLite 3.49.0 before 3.49.1, certain argument values to
│                       │      │                   sqlite3_db_config (in the C-language API) can cause a denial
│                       │      │                    of service (application crash). An sz*nBig multiplication
│                       │      │                   is not cast to a 64-bit integer, and consequently some
│                       │      │                   memory allocations may be incorrect. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-190 
│                       │      ├ VendorSeverity   ╭ amazon : 3 
│                       │      │                  ├ bitnami: 2 
│                       │      │                  ├ photon : 2 
│                       │      │                  ├ redhat : 2 
│                       │      │                  ╰ ubuntu : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:C/C:L/I:
│                       │      │                  │         │           L/A:L 
│                       │      │                  │         ╰ V3Score : 5.6 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:H 
│                       │      │                            ╰ V3Score : 5.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-29088 
│                       │      │                  ├ [1]: https://gist.github.com/ylwango613/d3883fb9f6ba8a78086
│                       │      │                  │      356779ce88248 
│                       │      │                  ├ [2]: https://github.com/sqlite/sqlite/commit/56d2fd008b1081
│                       │      │                  │      09f489339f5fd55212bb50afd4 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2025-29088 
│                       │      │                  ├ [4]: https://sqlite.org/forum/forumpost/48f365daec 
│                       │      │                  ├ [5]: https://sqlite.org/releaselog/3_49_1.html 
│                       │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-7528-1 
│                       │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-7679-1 
│                       │      │                  ├ [8]: https://www.cve.org/CVERecord?id=CVE-2025-29088 
│                       │      │                  ╰ [9]: https://www.sqlite.org/cves.html 
│                       │      ├ PublishedDate   : 2025-04-10T14:15:27.163Z 
│                       │      ╰ LastModifiedDate: 2025-08-26T20:15:39.47Z 
│                       ├ [42] ╭ VulnerabilityID : CVE-2025-32462 
│                       │      ├ PkgID           : sudo@1.9.16_p2-r0 
│                       │      ├ PkgName         : sudo 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/sudo@1.9.16_p2-r0?arch=x86_64&distro=3
│                       │      │                  │       .21.3 
│                       │      │                  ╰ UID : de403b0ae5749724 
│                       │      ├ InstalledVersion: 1.9.16_p2-r0 
│                       │      ├ FixedVersion    : 1.9.17_p1-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-32462 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : sudo: LPE via host option 
│                       │      ├ Description     : Sudo before 1.9.17p1, when used with a sudoers file that
│                       │      │                   specifies a host that is neither the current host nor ALL,
│                       │      │                   allows listed users to execute commands on unintended
│                       │      │                   machines. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-863 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 1 
│                       │      │                  ├ cbl-mariner: 1 
│                       │      │                  ├ nvd        : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 3 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 8.8 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:9978 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-32462 
│                       │      │                  ├ [2] : https://access.redhat.com/security/cve/cve-2025-32462 
│                       │      │                  ├ [3] : https://bugs.gentoo.org/show_bug.cgi?id=CVE-2025-32462 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2374692 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2374692 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-32462 
│                       │      │                  ├ [7] : https://errata.almalinux.org/9/ALSA-2025-9978.html 
│                       │      │                  ├ [8] : https://errata.rockylinux.org/RLSA-2025:10110 
│                       │      │                  ├ [9] : https://explore.alas.aws.amazon.com/CVE-2025-32462.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2025-32462.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2025-9978.html 
│                       │      │                  ├ [12]: https://lists.debian.org/debian-security-announce/202
│                       │      │                  │       5/msg00118.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2025-32462 
│                       │      │                  ├ [14]: https://security-tracker.debian.org/tracker/CVE-2025-
│                       │      │                  │       32462 
│                       │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-7604-1 
│                       │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-7604-2 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2025-32462 
│                       │      │                  ├ [18]: https://www.openwall.com/lists/oss-security/2025/06/3
│                       │      │                  │       0/2 
│                       │      │                  ├ [19]: https://www.secpod.com/blog/sudo-lpe-vulnerabilities-
│                       │      │                  │       resolved-what-you-need-to-know-about-cve-2025-32462-a
│                       │      │                  │       nd-cve-2025-32463/ 
│                       │      │                  ├ [20]: https://www.stratascale.com/vulnerability-alert-CVE-2
│                       │      │                  │       025-32462-sudo-host 
│                       │      │                  ├ [21]: https://www.sudo.ws/releases/changelog/ 
│                       │      │                  ├ [22]: https://www.sudo.ws/security/advisories/ 
│                       │      │                  ├ [23]: https://www.sudo.ws/security/advisories/host_any/ 
│                       │      │                  ╰ [24]: https://www.suse.com/security/cve/CVE-2025-32462.html 
│                       │      ├ PublishedDate   : 2025-06-30T21:15:30.08Z 
│                       │      ╰ LastModifiedDate: 2025-07-25T15:15:26.497Z 
│                       ├ [43] ╭ VulnerabilityID : CVE-2025-32463 
│                       │      ├ PkgID           : sudo@1.9.16_p2-r0 
│                       │      ├ PkgName         : sudo 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/sudo@1.9.16_p2-r0?arch=x86_64&distro=3
│                       │      │                  │       .21.3 
│                       │      │                  ╰ UID : de403b0ae5749724 
│                       │      ├ InstalledVersion: 1.9.16_p2-r0 
│                       │      ├ FixedVersion    : 1.9.17_p1-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4
│                       │      │                  │         d7814ea39226035ebf8e 
│                       │      │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b7
│                       │      │                            185ab555262cb80cc579 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-32463 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Title           : sudo: LPE via chroot option 
│                       │      ├ Description     : Sudo before 1.9.17p1 allows local users to obtain root
│                       │      │                   access because /etc/nsswitch.conf from a user-controlled
│                       │      │                   directory is used with the --chroot option. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs           ─ [0]: CWE-829 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 4 
│                       │      │                  ├ cbl-mariner: 4 
│                       │      │                  ├ nvd        : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ ubuntu     : 3 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 7.8 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:11537 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2025-32463 
│                       │      │                  ├ [2] : https://access.redhat.com/security/cve/cve-2025-32463 
│                       │      │                  ├ [3] : https://bugs.gentoo.org/show_bug.cgi?id=CVE-2025-32463 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2374692 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/2374693 
│                       │      │                  ├ [6] : https://errata.almalinux.org/10/ALSA-2025-11537.html 
│                       │      │                  ├ [7] : https://explore.alas.aws.amazon.com/CVE-2025-32463.html 
│                       │      │                  ├ [8] : https://iototsecnews.jp/2025/07/01/linux-sudo-chroot-
│                       │      │                  │       vulnerability-enables-hackers-to-elevate-privileges-t
│                       │      │                  │       o-root/ 
│                       │      │                  ├ [9] : https://linux.oracle.com/cve/CVE-2025-32463.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/errata/ELSA-2025-11537.html 
│                       │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2025-32463 
│                       │      │                  ├ [12]: https://security-tracker.debian.org/tracker/CVE-2025-
│                       │      │                  │       32463 
│                       │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-7604-1 
│                       │      │                  ├ [14]: https://www.cve.org/CVERecord?id=CVE-2025-32463 
│                       │      │                  ├ [15]: https://www.openwall.com/lists/oss-security/2025/06/3
│                       │      │                  │       0/3 
│                       │      │                  ├ [16]: https://www.secpod.com/blog/sudo-lpe-vulnerabilities-
│                       │      │                  │       resolved-what-you-need-to-know-about-cve-2025-32462-a
│                       │      │                  │       nd-cve-2025-32463/ 
│                       │      │                  ├ [17]: https://www.stratascale.com/vulnerability-alert-CVE-2
│                       │      │                  │       025-32463-sudo-chroot 
│                       │      │                  ├ [18]: https://www.sudo.ws/releases/changelog/ 
│                       │      │                  ├ [19]: https://www.sudo.ws/security/advisories/ 
│                       │      │                  ├ [20]: https://www.sudo.ws/security/advisories/chroot_bug/ 
│                       │      │                  ├ [21]: https://www.suse.com/security/cve/CVE-2025-32463.html 
│                       │      │                  ├ [22]: https://www.suse.com/support/update/announcement/2025
│                       │      │                  │       /suse-su-202502177-1/ 
│                       │      │                  ├ [23]: https://www.vicarius.io/vsociety/posts/cve-2025-32463
│                       │      │                  │       -detect-sudo-vulnerability 
│                       │      │                  ╰ [24]: https://www.vicarius.io/vsociety/posts/cve-2025-32463
│                       │      │                          -mitigate-sudo-vulnerability 
│                       │      ├ PublishedDate   : 2025-06-30T21:15:30.257Z 
│                       │      ╰ LastModifiedDate: 2025-07-22T15:15:26.15Z 
│                       ╰ [44] ╭ VulnerabilityID : CVE-2025-31115 
│                              ├ PkgID           : xz-libs@5.6.3-r0 
│                              ├ PkgName         : xz-libs 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/xz-libs@5.6.3-r0?arch=x86_64&distro=3.
│                              │                  │       21.3 
│                              │                  ╰ UID : a317bf50660bd742 
│                              ├ InstalledVersion: 5.6.3-r0 
│                              ├ FixedVersion    : 5.6.3-r1 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                              │                  │         af2fecb1758597ec9408 
│                              │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                              │                            fc7b86e44c11b16ec73a 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-31115 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Title           : xz: XZ has a heap-use-after-free bug in threaded .xz decoder 
│                              ├ Description     : XZ Utils provide a general-purpose data-compression library
│                              │                   plus command-line tools. In XZ Utils 5.3.3alpha to 5.8.0,
│                              │                   the multithreaded .xz decoder in liblzma has a bug where
│                              │                   invalid input can at least result in a crash. The effects
│                              │                   include heap use after free and writing to an address based
│                              │                   on the null pointer plus an offset. Applications and
│                              │                   libraries that use the lzma_stream_decoder_mt function are
│                              │                   affected. The bug has been fixed in XZ Utils 5.8.1, and the
│                              │                   fix has been committed to the v5.4, v5.6, v5.8, and master
│                              │                   branches in the xz Git repository. No new release packages
│                              │                   will be made from the old stable branches, but a standalone
│                              │                   patch is available that applies to all affected releases. 
│                              ├ Severity        : HIGH 
│                              ├ CweIDs           ╭ [0]: CWE-366 
│                              │                  ├ [1]: CWE-416 
│                              │                  ├ [2]: CWE-476 
│                              │                  ╰ [3]: CWE-826 
│                              ├ VendorSeverity   ╭ alma       : 3 
│                              │                  ├ azure      : 3 
│                              │                  ├ oracle-oval: 3 
│                              │                  ├ photon     : 3 
│                              │                  ├ redhat     : 3 
│                              │                  ╰ ubuntu     : 2 
│                              ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                              │                           │           /A:H 
│                              │                           ╰ V3Score : 7.5 
│                              ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2025/04/03/1 
│                              │                  ├ [1] : http://www.openwall.com/lists/oss-security/2025/04/03/2 
│                              │                  ├ [2] : http://www.openwall.com/lists/oss-security/2025/04/03/3 
│                              │                  ├ [3] : https://access.redhat.com/errata/RHSA-2025:7524 
│                              │                  ├ [4] : https://access.redhat.com/security/cve/CVE-2025-31115 
│                              │                  ├ [5] : https://bugzilla.redhat.com/2357249 
│                              │                  ├ [6] : https://errata.almalinux.org/10/ALSA-2025-7524.html 
│                              │                  ├ [7] : https://github.com/tukaani-project/xz/commit/d5a2ffe4
│                              │                  │       1bb77b918a8c96084885d4dbe4bf6480 
│                              │                  ├ [8] : https://github.com/tukaani-project/xz/security/adviso
│                              │                  │       ries/GHSA-6cc8-p5mm-29w2 
│                              │                  ├ [9] : https://linux.oracle.com/cve/CVE-2025-31115.html 
│                              │                  ├ [10]: https://linux.oracle.com/errata/ELSA-2025-7524.html 
│                              │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2025-31115 
│                              │                  ├ [12]: https://tukaani.org/xz/xz-cve-2025-31115.patch 
│                              │                  ├ [13]: https://ubuntu.com/security/notices/USN-7414-1 
│                              │                  ╰ [14]: https://www.cve.org/CVERecord?id=CVE-2025-31115 
│                              ├ PublishedDate   : 2025-04-03T17:15:30.54Z 
│                              ╰ LastModifiedDate: 2025-04-07T14:18:34.453Z 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2025-48924 
                              ├ PkgName         : org.apache.commons:commons-lang3 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ PkgIdentifier    ╭ PURL: pkg:maven/org.apache.commons/commons-lang3@3.17.0 
                              │                  ╰ UID : 36abc6aa3ef9156f 
                              ├ InstalledVersion: 3.17.0 
                              ├ FixedVersion    : 3.18.0 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4d
                              │                  │         7814ea39226035ebf8e 
                              │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b71
                              │                            85ab555262cb80cc579 
                              ├ SeveritySource  : ghsa 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-48924 
                              ├ DataSource       ╭ ID  : ghsa 
                              │                  ├ Name: GitHub Security Advisory Maven 
                              │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
                              │                          osystem%3Amaven 
                              ├ Title           : commons-lang/commons-lang: org.apache.commons/commons-lang3:
                              │                   Uncontrolled Recursion vulnerability in Apache Commons Lang 
                              ├ Description     : Uncontrolled Recursion vulnerability in Apache Commons Lang.
                              │                   
                              │                   This issue affects Apache Commons Lang: Starting with
                              │                   commons-lang:commons-lang 2.0 to 2.6, and, from
                              │                   org.apache.commons:commons-lang3 3.0 before 3.18.0.
                              │                   The methods ClassUtils.getClass(...) can throw
                              │                   StackOverflowError on very long inputs. Because an Error is
                              │                   usually not handled by applications and libraries, a 
                              │                   StackOverflowError could cause an application to stop.
                              │                   Users are recommended to upgrade to version 3.18.0, which
                              │                   fixes the issue. 
                              ├ Severity        : MEDIUM 
                              ├ CweIDs           ─ [0]: CWE-674 
                              ├ VendorSeverity   ╭ amazon: 1 
                              │                  ├ azure : 2 
                              │                  ├ ghsa  : 2 
                              │                  ╰ redhat: 1 
                              ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/
                              │                  │        │           A:N 
                              │                  │        ╰ V3Score : 6.5 
                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/
                              │                           │           A:L 
                              │                           ╰ V3Score : 3.7 
                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-48924 
                              │                  ├ [1]: https://github.com/apache/commons-lang 
                              │                  ├ [2]: https://github.com/apache/commons-lang/commit/b424803ab
                              │                  │      db2bec818e4fbcb251ce031c22aca53 
                              │                  ├ [3]: https://lists.apache.org/thread/bgv0lpswokgol11tloxnjfz
                              │                  │      dl7yrc1g1 
                              │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2025-48924 
                              │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2025-48924 
                              ├ PublishedDate   : 2025-07-11T15:15:24.347Z 
                              ╰ LastModifiedDate: 2025-07-28T13:45:38.647Z 
````
