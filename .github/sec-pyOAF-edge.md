````yaml
╭ [0] ╭ Target         : openaf/pyoaf:edge (alpine 3.21.3) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2025-31498 
│                       │     ├ PkgID           : c-ares@1.34.3-r0 
│                       │     ├ PkgName         : c-ares 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/c-ares@1.34.3-r0?arch=x86_64&distro=3.2
│                       │     │                  │       1.3 
│                       │     │                  ╰ UID : 3bac544df48402b7 
│                       │     ├ InstalledVersion: 1.34.3-r0 
│                       │     ├ FixedVersion    : 1.34.5-r0 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4d
│                       │     │                  │         7814ea39226035ebf8e 
│                       │     │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b71
│                       │     │                            85ab555262cb80cc579 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-31498 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : c-ares: c-ares has a use-after-free in read_answers() 
│                       │     ├ Description     : c-ares is an asynchronous resolver library. From 1.32.3
│                       │     │                   through 1.34.4, there is a use-after-free in read_answers()
│                       │     │                   when process_answer() may re-enqueue a query either due to a
│                       │     │                   DNS Cookie Failure or when the upstream server does not
│                       │     │                   properly support EDNS, or possibly on TCP queries if the
│                       │     │                   remote closed the connection immediately after a response. If
│                       │     │                    there was an issue trying to put that new transaction on the
│                       │     │                    wire, it would close the connection handle, but
│                       │     │                   read_answers() was still expecting the connection handle to
│                       │     │                   be available to possibly dequeue other responses. In theory a
│                       │     │                    remote attacker might be able to trigger this by flooding
│                       │     │                   the target with ICMP UNREACHABLE packets if they also control
│                       │     │                    the upstream nameserver and can return a result with one of
│                       │     │                   those conditions, this has been untested. Otherwise only a
│                       │     │                   local attacker might be able to change system behavior to
│                       │     │                   make send()/write() return a failure condition. This
│                       │     │                   vulnerability is fixed in 1.34.5. 
│                       │     ├ Severity        : HIGH 
│                       │     ├ CweIDs           ─ [0]: CWE-416 
│                       │     ├ VendorSeverity   ╭ redhat: 3 
│                       │     │                  ╰ ubuntu: 2 
│                       │     ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/
│                       │     │                           │           A:H 
│                       │     │                           ╰ V3Score : 7 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2025/04/08/3 
│                       │     │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2025-31498 
│                       │     │                  ├ [2]: https://github.com/c-ares/c-ares/commit/29d38719112639d
│                       │     │                  │      8c0ba910254a3dd4f482ea2d1 
│                       │     │                  ├ [3]: https://github.com/c-ares/c-ares/pull/821 
│                       │     │                  ├ [4]: https://github.com/c-ares/c-ares/security/advisories/GH
│                       │     │                  │      SA-6hxc-62jh-p29v 
│                       │     │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2025-31498 
│                       │     │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2025-31498 
│                       │     ├ PublishedDate   : 2025-04-08T14:15:35.293Z 
│                       │     ╰ LastModifiedDate: 2025-04-08T15:15:50.31Z 
│                       ├ [1] ╭ VulnerabilityID : CVE-2025-31344 
│                       │     ├ PkgID           : giflib@5.2.2-r0 
│                       │     ├ PkgName         : giflib 
│                       │     ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/giflib@5.2.2-r0?arch=x86_64&distro=3.21.3 
│                       │     │                  ╰ UID : da32343cd3d1a4d8 
│                       │     ├ InstalledVersion: 5.2.2-r0 
│                       │     ├ FixedVersion    : 5.2.2-r1 
│                       │     ├ Status          : fixed 
│                       │     ├ Layer            ╭ Digest: sha256:1e5ff339c8114bc27d24c7ac92a1d1071255c746cdc4d
│                       │     │                  │         7814ea39226035ebf8e 
│                       │     │                  ╰ DiffID: sha256:071b9ab46a73306317e4fa55fb52334a4b6d9588a4b71
│                       │     │                            85ab555262cb80cc579 
│                       │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-31344 
│                       │     ├ DataSource       ╭ ID  : alpine 
│                       │     │                  ├ Name: Alpine Secdb 
│                       │     │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │     ├ Title           : Heap-based Buffer Overflow vulnerability in openEuler giflib
│                       │     │                   on Linux. ... 
│                       │     ├ Description     : Heap-based Buffer Overflow vulnerability in openEuler giflib
│                       │     │                   on Linux. This vulnerability is associated with program files
│                       │     │                    gif2rgb.C.
│                       │     │                   
│                       │     │                   This issue affects giflib: through 5.2.2. 
│                       │     ├ Severity        : UNKNOWN 
│                       │     ├ CweIDs           ─ [0]: CWE-122 
│                       │     ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2025/04/07/3 
│                       │     │                  ├ [1]: http://www.openwall.com/lists/oss-security/2025/04/07/4 
│                       │     │                  ├ [2]: http://www.openwall.com/lists/oss-security/2025/04/07/5 
│                       │     │                  ├ [3]: http://www.openwall.com/lists/oss-security/2025/04/07/6 
│                       │     │                  ├ [4]: http://www.openwall.com/lists/oss-security/2025/04/08/1 
│                       │     │                  ├ [5]: http://www.openwall.com/lists/oss-security/2025/04/09/5 
│                       │     │                  ├ [6]: http://www.openwall.com/lists/oss-security/2025/04/09/7 
│                       │     │                  ├ [7]: http://www.openwall.com/lists/oss-security/2025/04/10/1 
│                       │     │                  ├ [8]: https://gitee.com/src-openeuler/giflib/pulls/54 
│                       │     │                  ╰ [9]: https://www.openeuler.org/zh/security/security-bulletin
│                       │     │                         s/detail/?id=openEuler-SA-2025-1292 
│                       │     ├ PublishedDate   : 2025-04-14T08:15:13.973Z 
│                       │     ╰ LastModifiedDate: 2025-04-14T08:15:13.973Z 
│                       ╰ [2] ╭ VulnerabilityID : CVE-2025-31115 
│                             ├ PkgID           : xz-libs@5.6.3-r0 
│                             ├ PkgName         : xz-libs 
│                             ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/xz-libs@5.6.3-r0?arch=x86_64&distro=3.2
│                             │                  │       1.3 
│                             │                  ╰ UID : 6a1b930ba614c87c 
│                             ├ InstalledVersion: 5.6.3-r0 
│                             ├ FixedVersion    : 5.6.3-r1 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:4c4700dde23c51097d326a561f2def2e2afcb03cfd32a
│                             │                  │         f2fecb1758597ec9408 
│                             │                  ╰ DiffID: sha256:be756c12e9dbd56e6ea2e38174c811ced9c0c95d3241f
│                             │                            c7b86e44c11b16ec73a 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-31115 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Title           : xz: XZ has a heap-use-after-free bug in threaded .xz decoder 
│                             ├ Description     : XZ Utils provide a general-purpose data-compression library
│                             │                   plus command-line tools. In XZ Utils 5.3.3alpha to 5.8.0, the
│                             │                    multithreaded .xz decoder in liblzma has a bug where invalid
│                             │                    input can at least result in a crash. The effects include
│                             │                   heap use after free and writing to an address based on the
│                             │                   null pointer plus an offset. Applications and libraries that
│                             │                   use the lzma_stream_decoder_mt function are affected. The bug
│                             │                    has been fixed in XZ Utils 5.8.1, and the fix has been
│                             │                   committed to the v5.4, v5.6, v5.8, and master branches in the
│                             │                    xz Git repository. No new release packages will be made from
│                             │                    the old stable branches, but a standalone patch is available
│                             │                    that applies to all affected releases. 
│                             ├ Severity        : HIGH 
│                             ├ CweIDs           ╭ [0]: CWE-366 
│                             │                  ├ [1]: CWE-416 
│                             │                  ├ [2]: CWE-476 
│                             │                  ╰ [3]: CWE-826 
│                             ├ VendorSeverity   ╭ photon: 3 
│                             │                  ├ redhat: 3 
│                             │                  ╰ ubuntu: 2 
│                             ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/
│                             │                           │           A:H 
│                             │                           ╰ V3Score : 7.5 
│                             ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2025/04/03/1 
│                             │                  ├ [1]: http://www.openwall.com/lists/oss-security/2025/04/03/2 
│                             │                  ├ [2]: http://www.openwall.com/lists/oss-security/2025/04/03/3 
│                             │                  ├ [3]: https://access.redhat.com/security/cve/CVE-2025-31115 
│                             │                  ├ [4]: https://github.com/tukaani-project/xz/commit/d5a2ffe41b
│                             │                  │      b77b918a8c96084885d4dbe4bf6480 
│                             │                  ├ [5]: https://github.com/tukaani-project/xz/security/advisori
│                             │                  │      es/GHSA-6cc8-p5mm-29w2 
│                             │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2025-31115 
│                             │                  ├ [7]: https://tukaani.org/xz/xz-cve-2025-31115.patch 
│                             │                  ├ [8]: https://ubuntu.com/security/notices/USN-7414-1 
│                             │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2025-31115 
│                             ├ PublishedDate   : 2025-04-03T17:15:30.54Z 
│                             ╰ LastModifiedDate: 2025-04-07T14:18:34.453Z 
╰ [1] ╭ Target: Java 
      ├ Class : lang-pkgs 
      ╰ Type  : jar 
````
