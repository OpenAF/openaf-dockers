````yaml
╭ [0] ╭ Target         : openaf/pyoaf:edge (alpine 3.21.3) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2025-31498 
│                       │      ├ PkgID           : c-ares@1.34.3-r0 
│                       │      ├ PkgName         : c-ares 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/c-ares@1.34.3-r0?arch=x86_64&distro=3.
│                       │      │                  │       21.3 
│                       │      │                  ╰ UID : 3bac544df48402b7 
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
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2025/04/08/3 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2025-31498 
│                       │      │                  ├ [2]: https://github.com/c-ares/c-ares/commit/29d38719112639
│                       │      │                  │      d8c0ba910254a3dd4f482ea2d1 
│                       │      │                  ├ [3]: https://github.com/c-ares/c-ares/pull/821 
│                       │      │                  ├ [4]: https://github.com/c-ares/c-ares/security/advisories/G
│                       │      │                  │      HSA-6hxc-62jh-p29v 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2025-31498 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2025-31498 
│                       │      ├ PublishedDate   : 2025-04-08T14:15:35.293Z 
│                       │      ╰ LastModifiedDate: 2025-04-08T15:15:50.31Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2025-31344 
│                       │      ├ PkgID           : giflib@5.2.2-r0 
│                       │      ├ PkgName         : giflib 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/giflib@5.2.2-r0?arch=x86_64&distro=3.2
│                       │      │                  │       1.3 
│                       │      │                  ╰ UID : da32343cd3d1a4d8 
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
│                       │      ├ VendorSeverity   ─ redhat: 2 
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
│                       │      │                  ╰ UID : b0c8f9b2170425c0 
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
│                       │      ├ VendorSeverity   ╭ oracle-oval: 2 
│                       │      │                  ╰ redhat     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-21587 
│                       │      │                  ├ [1]: https://linux.oracle.com/cve/CVE-2025-21587.html 
│                       │      │                  ├ [2]: https://linux.oracle.com/errata/ELSA-2025-3855.html 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2025-21587 
│                       │      │                  ├ [4]: https://www.cve.org/CVERecord?id=CVE-2025-21587 
│                       │      │                  ╰ [5]: https://www.oracle.com/security-alerts/cpuapr2025.html 
│                       │      ├ PublishedDate   : 2025-04-15T21:15:54.293Z 
│                       │      ╰ LastModifiedDate: 2025-04-16T16:15:29.73Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2025-23083 
│                       │      ├ PkgID           : openjdk21-jre@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.6_p7-r0?arch=x86_64
│                       │      │                  │       &distro=3.21.3 
│                       │      │                  ╰ UID : b0c8f9b2170425c0 
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
│                       │      │                  ╰ redhat     : 3 
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
│                       │      │                  ├ [6] : https://linux.oracle.com/cve/CVE-2025-23083.html 
│                       │      │                  ├ [7] : https://linux.oracle.com/errata/ELSA-2025-1613.html 
│                       │      │                  ├ [8] : https://nodejs.org/en/blog/vulnerability/january-2025
│                       │      │                  │       -security-releases 
│                       │      │                  ├ [9] : https://nvd.nist.gov/vuln/detail/CVE-2025-23083 
│                       │      │                  ├ [10]: https://security.netapp.com/advisory/ntap-20250228-00
│                       │      │                  │       08/ 
│                       │      │                  ╰ [11]: https://www.cve.org/CVERecord?id=CVE-2025-23083 
│                       │      ├ PublishedDate   : 2025-01-22T02:15:33.93Z 
│                       │      ╰ LastModifiedDate: 2025-02-28T13:15:28.213Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2025-30691 
│                       │      ├ PkgID           : openjdk21-jre@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.6_p7-r0?arch=x86_64
│                       │      │                  │       &distro=3.21.3 
│                       │      │                  ╰ UID : b0c8f9b2170425c0 
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
│                       │      ├ VendorSeverity   ╭ oracle-oval: 2 
│                       │      │                  ╰ redhat     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-30691 
│                       │      │                  ├ [1]: https://linux.oracle.com/cve/CVE-2025-30691.html 
│                       │      │                  ├ [2]: https://linux.oracle.com/errata/ELSA-2025-3855.html 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2025-30691 
│                       │      │                  ├ [4]: https://security.netapp.com/advisory/ntap-20250418-0004/ 
│                       │      │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2025-30691 
│                       │      │                  ╰ [6]: https://www.oracle.com/security-alerts/cpuapr2025.html 
│                       │      ├ PublishedDate   : 2025-04-15T21:15:58.36Z 
│                       │      ╰ LastModifiedDate: 2025-04-19T01:15:44.85Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2025-30698 
│                       │      ├ PkgID           : openjdk21-jre@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.6_p7-r0?arch=x86_64
│                       │      │                  │       &distro=3.21.3 
│                       │      │                  ╰ UID : b0c8f9b2170425c0 
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
│                       │      ├ VendorSeverity   ╭ oracle-oval: 2 
│                       │      │                  ╰ redhat     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.6 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-30698 
│                       │      │                  ├ [1]: https://linux.oracle.com/cve/CVE-2025-30698.html 
│                       │      │                  ├ [2]: https://linux.oracle.com/errata/ELSA-2025-3855.html 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2025-30698 
│                       │      │                  ├ [4]: https://www.cve.org/CVERecord?id=CVE-2025-30698 
│                       │      │                  ╰ [5]: https://www.oracle.com/security-alerts/cpuapr2025.html 
│                       │      ├ PublishedDate   : 2025-04-15T21:15:59.137Z 
│                       │      ╰ LastModifiedDate: 2025-04-16T16:15:33.397Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2025-21587 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.6_p7-r0?ar
│                       │      │                  │       ch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : 93561891ceb3fbef 
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
│                       │      ├ VendorSeverity   ╭ oracle-oval: 2 
│                       │      │                  ╰ redhat     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-21587 
│                       │      │                  ├ [1]: https://linux.oracle.com/cve/CVE-2025-21587.html 
│                       │      │                  ├ [2]: https://linux.oracle.com/errata/ELSA-2025-3855.html 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2025-21587 
│                       │      │                  ├ [4]: https://www.cve.org/CVERecord?id=CVE-2025-21587 
│                       │      │                  ╰ [5]: https://www.oracle.com/security-alerts/cpuapr2025.html 
│                       │      ├ PublishedDate   : 2025-04-15T21:15:54.293Z 
│                       │      ╰ LastModifiedDate: 2025-04-16T16:15:29.73Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2025-23083 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.6_p7-r0?ar
│                       │      │                  │       ch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : 93561891ceb3fbef 
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
│                       │      │                  ╰ redhat     : 3 
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
│                       │      │                  ├ [6] : https://linux.oracle.com/cve/CVE-2025-23083.html 
│                       │      │                  ├ [7] : https://linux.oracle.com/errata/ELSA-2025-1613.html 
│                       │      │                  ├ [8] : https://nodejs.org/en/blog/vulnerability/january-2025
│                       │      │                  │       -security-releases 
│                       │      │                  ├ [9] : https://nvd.nist.gov/vuln/detail/CVE-2025-23083 
│                       │      │                  ├ [10]: https://security.netapp.com/advisory/ntap-20250228-00
│                       │      │                  │       08/ 
│                       │      │                  ╰ [11]: https://www.cve.org/CVERecord?id=CVE-2025-23083 
│                       │      ├ PublishedDate   : 2025-01-22T02:15:33.93Z 
│                       │      ╰ LastModifiedDate: 2025-02-28T13:15:28.213Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2025-30691 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.6_p7-r0?ar
│                       │      │                  │       ch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : 93561891ceb3fbef 
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
│                       │      ├ VendorSeverity   ╭ oracle-oval: 2 
│                       │      │                  ╰ redhat     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-30691 
│                       │      │                  ├ [1]: https://linux.oracle.com/cve/CVE-2025-30691.html 
│                       │      │                  ├ [2]: https://linux.oracle.com/errata/ELSA-2025-3855.html 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2025-30691 
│                       │      │                  ├ [4]: https://security.netapp.com/advisory/ntap-20250418-0004/ 
│                       │      │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2025-30691 
│                       │      │                  ╰ [6]: https://www.oracle.com/security-alerts/cpuapr2025.html 
│                       │      ├ PublishedDate   : 2025-04-15T21:15:58.36Z 
│                       │      ╰ LastModifiedDate: 2025-04-19T01:15:44.85Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2025-30698 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.6_p7-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.6_p7-r0?ar
│                       │      │                  │       ch=x86_64&distro=3.21.3 
│                       │      │                  ╰ UID : 93561891ceb3fbef 
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
│                       │      ├ VendorSeverity   ╭ oracle-oval: 2 
│                       │      │                  ╰ redhat     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.6 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-30698 
│                       │      │                  ├ [1]: https://linux.oracle.com/cve/CVE-2025-30698.html 
│                       │      │                  ├ [2]: https://linux.oracle.com/errata/ELSA-2025-3855.html 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2025-30698 
│                       │      │                  ├ [4]: https://www.cve.org/CVERecord?id=CVE-2025-30698 
│                       │      │                  ╰ [5]: https://www.oracle.com/security-alerts/cpuapr2025.html 
│                       │      ├ PublishedDate   : 2025-04-15T21:15:59.137Z 
│                       │      ╰ LastModifiedDate: 2025-04-16T16:15:33.397Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2025-29087 
│                       │      ├ PkgID           : sqlite-libs@3.48.0-r0 
│                       │      ├ PkgName         : sqlite-libs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/sqlite-libs@3.48.0-r0?arch=x86_64&dist
│                       │      │                  │       ro=3.21.3 
│                       │      │                  ╰ UID : d3184f4c955c09b4 
│                       │      ├ InstalledVersion: 3.48.0-r0 
│                       │      ├ FixedVersion    : 3.48.0-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32
│                       │      │                  │         af2fecb1758597ec9408 
│                       │      │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241
│                       │      │                            fc7b86e44c11b16ec73a 
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
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-190 
│                       │      ├ VendorSeverity   ╭ bitnami: 1 
│                       │      │                  ├ redhat : 2 
│                       │      │                  ╰ ubuntu : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:C/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 3.2 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:H 
│                       │      │                            ╰ V3Score : 5.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-29087 
│                       │      │                  ├ [1]: https://gist.github.com/ylwango613/a44a29f1ef074fa783e
│                       │      │                  │      29f04a0afd62a 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2025-29087 
│                       │      │                  ├ [3]: https://sqlite.org/releaselog/3_49_1.html 
│                       │      │                  ├ [4]: https://www.cve.org/CVERecord?id=CVE-2025-29087 
│                       │      │                  ╰ [5]: https://www.sqlite.org/cves.html 
│                       │      ├ PublishedDate   : 2025-04-07T20:15:20.253Z 
│                       │      ╰ LastModifiedDate: 2025-04-15T16:16:06.233Z 
│                       ╰ [11] ╭ VulnerabilityID : CVE-2025-31115 
│                              ├ PkgID           : xz-libs@5.6.3-r0 
│                              ├ PkgName         : xz-libs 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/xz-libs@5.6.3-r0?arch=x86_64&distro=3.
│                              │                  │       21.3 
│                              │                  ╰ UID : 6a1b930ba614c87c 
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
│                              ├ VendorSeverity   ╭ photon: 3 
│                              │                  ├ redhat: 3 
│                              │                  ╰ ubuntu: 2 
│                              ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                              │                           │           /A:H 
│                              │                           ╰ V3Score : 7.5 
│                              ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2025/04/03/1 
│                              │                  ├ [1]: http://www.openwall.com/lists/oss-security/2025/04/03/2 
│                              │                  ├ [2]: http://www.openwall.com/lists/oss-security/2025/04/03/3 
│                              │                  ├ [3]: https://access.redhat.com/security/cve/CVE-2025-31115 
│                              │                  ├ [4]: https://github.com/tukaani-project/xz/commit/d5a2ffe41
│                              │                  │      bb77b918a8c96084885d4dbe4bf6480 
│                              │                  ├ [5]: https://github.com/tukaani-project/xz/security/advisor
│                              │                  │      ies/GHSA-6cc8-p5mm-29w2 
│                              │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2025-31115 
│                              │                  ├ [7]: https://tukaani.org/xz/xz-cve-2025-31115.patch 
│                              │                  ├ [8]: https://ubuntu.com/security/notices/USN-7414-1 
│                              │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2025-31115 
│                              ├ PublishedDate   : 2025-04-03T17:15:30.54Z 
│                              ╰ LastModifiedDate: 2025-04-07T14:18:34.453Z 
╰ [1] ╭ Target: Java 
      ├ Class : lang-pkgs 
      ╰ Type  : jar 
````
