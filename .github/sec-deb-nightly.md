````yaml
╭ [0] ╭ Target         : openaf/oaf:deb-nightly (ubuntu 25.04) 
│     ├ Class          : os-pkgs 
│     ├ Type           : ubuntu 
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2016-2781 
│                       │      ├ PkgID           : coreutils@9.5-1ubuntu1.25.04.2 
│                       │      ├ PkgName         : coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/coreutils@9.5-1ubuntu1.25.04.2?arch=am
│                       │      │                  │       d64&distro=ubuntu-25.04 
│                       │      │                  ╰ UID : fb90d22e49e1fb47 
│                       │      ├ InstalledVersion: 9.5-1ubuntu1.25.04.2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2016-2781 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : coreutils: Non-privileged session can escape to the parent
│                       │      │                   session in chroot 
│                       │      ├ Description     : chroot in GNU coreutils, when used with --userspec, allows
│                       │      │                   local users to escape to the parent session via a crafted
│                       │      │                   TIOCSTI ioctl call, which pushes characters to the
│                       │      │                   terminal's input buffer. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-20 
│                       │      ├ VendorSeverity   ╭ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:L/AC:L/Au:N/C:N/I:P/A:N 
│                       │      │                  │        ├ V3Vector: CVSS:3.0/AV:L/AC:L/PR:L/UI:N/S:C/C:N/I:H
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ├ V2Score : 2.1 
│                       │      │                  │        ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat ╭ V2Vector: AV:L/AC:H/Au:N/C:C/I:C/A:C 
│                       │      │                           ├ V3Vector: CVSS:3.0/AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ├ V2Score : 6.2 
│                       │      │                           ╰ V3Score : 8.6 
│                       │      ├ References       ╭ [0]: http://seclists.org/oss-sec/2016/q1/452 
│                       │      │                  ├ [1]: http://www.openwall.com/lists/oss-security/2016/02/28/2 
│                       │      │                  ├ [2]: http://www.openwall.com/lists/oss-security/2016/02/28/3 
│                       │      │                  ├ [3]: https://access.redhat.com/security/cve/CVE-2016-2781 
│                       │      │                  ├ [4]: https://lists.apache.org/thread.html/rf9fa47ab66495c78
│                       │      │                  │      bb4120b0754dd9531ca2ff0430f6685ac9b07772%40%3Cdev.mina
│                       │      │                  │      .apache.org%3E 
│                       │      │                  ├ [5]: https://lore.kernel.org/patchwork/patch/793178/ 
│                       │      │                  ├ [6]: https://mirrors.edge.kernel.org/pub/linux/utils/util-l
│                       │      │                  │      inux/v2.28/v2.28-ReleaseNotes 
│                       │      │                  ├ [7]: https://nvd.nist.gov/vuln/detail/CVE-2016-2781 
│                       │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2016-2781 
│                       │      ├ PublishedDate   : 2017-02-07T15:59:00.333Z 
│                       │      ╰ LastModifiedDate: 2025-06-09T16:15:25.013Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2025-10148 
│                       │      ├ PkgID           : curl@8.12.1-3ubuntu1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.12.1-3ubuntu1?arch=amd64&distro
│                       │      │                  │       =ubuntu-25.04 
│                       │      │                  ╰ UID : 6ea7a92c5821dca8 
│                       │      ├ InstalledVersion: 8.12.1-3ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-10148 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : curl: predictable WebSocket mask 
│                       │      ├ Description     : curl's websocket code did not update the 32 bit mask pattern
│                       │      │                    for each new
│                       │      │                    outgoing frame as the specification says. Instead it used a
│                       │      │                    fixed mask that
│                       │      │                   persisted and was used throughout the entire connection.
│                       │      │                   
│                       │      │                   A predictable mask pattern allows for a malicious server to
│                       │      │                   induce traffic
│                       │      │                   between the two communicating parties that could be
│                       │      │                   interpreted by an involved
│                       │      │                   proxy (configured or transparent) as genuine, real, HTTP
│                       │      │                   traffic with content
│                       │      │                   and thereby poison its cache. That cached poisoned content
│                       │      │                   could then be
│                       │      │                   served to all users of that proxy. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-10148 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2025-10148.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-10148.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3330839 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2025-10148 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2025-10148 
│                       │      ├ PublishedDate   : 2025-09-12T06:15:40.02Z 
│                       │      ╰ LastModifiedDate: 2025-09-15T15:21:42.937Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2025-9086 
│                       │      ├ PkgID           : curl@8.12.1-3ubuntu1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.12.1-3ubuntu1?arch=amd64&distro
│                       │      │                  │       =ubuntu-25.04 
│                       │      │                  ╰ UID : 6ea7a92c5821dca8 
│                       │      ├ InstalledVersion: 8.12.1-3ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-9086 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : curl: libcurl: Curl out of bounds read for cookie path 
│                       │      ├ Description     : 1. A cookie is set using the `secure` keyword for
│                       │      │                   `https://target`
│                       │      │                   2. curl is redirected to or otherwise made to speak with
│                       │      │                   `http://target` (same
│                       │      │                      hostname, but using clear text HTTP) using the same
│                       │      │                   cookie set
│                       │      │                   3. The same cookie name is set - but with just a slash as
│                       │      │                   path (`path='/'`).
│                       │      │                      Since this site is not secure, the cookie *should* just
│                       │      │                   be ignored.
│                       │      │                   4. A bug in the path comparison logic makes curl read
│                       │      │                   outside a heap buffer
│                       │      │                      boundary
│                       │      │                   
│                       │      │                   The bug either causes a crash or it potentially makes the
│                       │      │                   comparison come to
│                       │      │                   the wrong conclusion and lets the clear-text site override
│                       │      │                   the contents of the
│                       │      │                   secure cookie, contrary to expectations and depending on the
│                       │      │                    memory contents
│                       │      │                   immediately following the single-byte allocation that holds
│                       │      │                   the path.
│                       │      │                   The presumed and correct behavior would be to plainly ignore
│                       │      │                    the second set of
│                       │      │                   the cookie since it was already set as secure on a secure
│                       │      │                   host so overriding
│                       │      │                   it on an insecure host should not be okay. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-9086 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2025-9086.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-9086.json 
│                       │      │                  ├ [3]: https://github.com/curl/curl/commit/c6ae07c6a541e0e96d
│                       │      │                  │      0040afb6 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3294999 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2025-9086 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2025-9086 
│                       │      ├ PublishedDate   : 2025-09-12T06:15:44.1Z 
│                       │      ╰ LastModifiedDate: 2025-09-15T15:21:42.937Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2022-3219 
│                       │      ├ PkgID           : gpgv@2.4.4-2ubuntu23.1 
│                       │      ├ PkgName         : gpgv 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/gpgv@2.4.4-2ubuntu23.1?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-25.04 
│                       │      │                  ╰ UID : d2a702b753c09f0f 
│                       │      ├ InstalledVersion: 2.4.4-2ubuntu23.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-3219 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : gnupg: denial of service issue (resource consumption) using
│                       │      │                   compressed packets 
│                       │      ├ Description     : GnuPG can be made to spin on a relatively small input by
│                       │      │                   (for example) crafting a public key with thousands of
│                       │      │                   signatures attached, compressed down to just a few KB. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-787 
│                       │      ├ VendorSeverity   ╭ nvd   : 1 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:L 
│                       │      │                  │        ╰ V3Score : 3.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.2 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-3219 
│                       │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2127010 
│                       │      │                  ├ [2]: https://dev.gnupg.org/D556 
│                       │      │                  ├ [3]: https://dev.gnupg.org/T5993 
│                       │      │                  ├ [4]: https://marc.info/?l=oss-security&m=165696590211434&w=4 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2022-3219 
│                       │      │                  ├ [6]: https://security.netapp.com/advisory/ntap-20230324-0001/ 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2022-3219 
│                       │      ├ PublishedDate   : 2023-02-23T20:15:12.393Z 
│                       │      ╰ LastModifiedDate: 2025-03-12T21:15:38.207Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2025-10148 
│                       │      ├ PkgID           : libcurl4t64@8.12.1-3ubuntu1 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.12.1-3ubuntu1?arch=amd64
│                       │      │                  │       &distro=ubuntu-25.04 
│                       │      │                  ╰ UID : 5ce7d94c2b78c513 
│                       │      ├ InstalledVersion: 8.12.1-3ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-10148 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : curl: predictable WebSocket mask 
│                       │      ├ Description     : curl's websocket code did not update the 32 bit mask pattern
│                       │      │                    for each new
│                       │      │                    outgoing frame as the specification says. Instead it used a
│                       │      │                    fixed mask that
│                       │      │                   persisted and was used throughout the entire connection.
│                       │      │                   
│                       │      │                   A predictable mask pattern allows for a malicious server to
│                       │      │                   induce traffic
│                       │      │                   between the two communicating parties that could be
│                       │      │                   interpreted by an involved
│                       │      │                   proxy (configured or transparent) as genuine, real, HTTP
│                       │      │                   traffic with content
│                       │      │                   and thereby poison its cache. That cached poisoned content
│                       │      │                   could then be
│                       │      │                   served to all users of that proxy. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-10148 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2025-10148.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-10148.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3330839 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2025-10148 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2025-10148 
│                       │      ├ PublishedDate   : 2025-09-12T06:15:40.02Z 
│                       │      ╰ LastModifiedDate: 2025-09-15T15:21:42.937Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2025-9086 
│                       │      ├ PkgID           : libcurl4t64@8.12.1-3ubuntu1 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.12.1-3ubuntu1?arch=amd64
│                       │      │                  │       &distro=ubuntu-25.04 
│                       │      │                  ╰ UID : 5ce7d94c2b78c513 
│                       │      ├ InstalledVersion: 8.12.1-3ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-9086 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : curl: libcurl: Curl out of bounds read for cookie path 
│                       │      ├ Description     : 1. A cookie is set using the `secure` keyword for
│                       │      │                   `https://target`
│                       │      │                   2. curl is redirected to or otherwise made to speak with
│                       │      │                   `http://target` (same
│                       │      │                      hostname, but using clear text HTTP) using the same
│                       │      │                   cookie set
│                       │      │                   3. The same cookie name is set - but with just a slash as
│                       │      │                   path (`path='/'`).
│                       │      │                      Since this site is not secure, the cookie *should* just
│                       │      │                   be ignored.
│                       │      │                   4. A bug in the path comparison logic makes curl read
│                       │      │                   outside a heap buffer
│                       │      │                      boundary
│                       │      │                   
│                       │      │                   The bug either causes a crash or it potentially makes the
│                       │      │                   comparison come to
│                       │      │                   the wrong conclusion and lets the clear-text site override
│                       │      │                   the contents of the
│                       │      │                   secure cookie, contrary to expectations and depending on the
│                       │      │                    memory contents
│                       │      │                   immediately following the single-byte allocation that holds
│                       │      │                   the path.
│                       │      │                   The presumed and correct behavior would be to plainly ignore
│                       │      │                    the second set of
│                       │      │                   the cookie since it was already set as secure on a secure
│                       │      │                   host so overriding
│                       │      │                   it on an insecure host should not be okay. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-9086 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2025-9086.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-9086.json 
│                       │      │                  ├ [3]: https://github.com/curl/curl/commit/c6ae07c6a541e0e96d
│                       │      │                  │      0040afb6 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3294999 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2025-9086 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2025-9086 
│                       │      ├ PublishedDate   : 2025-09-12T06:15:44.1Z 
│                       │      ╰ LastModifiedDate: 2025-09-15T15:21:42.937Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2024-2236 
│                       │      ├ PkgID           : libgcrypt20@1.11.0-6ubuntu1 
│                       │      ├ PkgName         : libgcrypt20 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgcrypt20@1.11.0-6ubuntu1?arch=amd64
│                       │      │                  │       &distro=ubuntu-25.04 
│                       │      │                  ╰ UID : 5a0c5e86aadb6057 
│                       │      ├ InstalledVersion: 1.11.0-6ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-2236 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : libgcrypt: vulnerable to Marvin Attack 
│                       │      ├ Description     : A timing-based side-channel flaw was found in libgcrypt's
│                       │      │                   RSA implementation. This issue may allow a remote attacker
│                       │      │                   to initiate a Bleichenbacher-style attack, which can lead to
│                       │      │                    the decryption of RSA ciphertexts. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-208 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9404 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2025:3530 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2025:3534 
│                       │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2024-2236 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2245218 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2245218 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2268268 
│                       │      │                  ├ [7] : https://dev.gnupg.org/T7136 
│                       │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2024-9404.html 
│                       │      │                  ├ [9] : https://github.com/tomato42/marvin-toolkit/tree/maste
│                       │      │                  │       r/example/libgcrypt 
│                       │      │                  ├ [10]: https://gitlab.com/redhat-crypto/libgcrypt/libgcrypt-
│                       │      │                  │       mirror/-/merge_requests/17 
│                       │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2024-2236.html 
│                       │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2024-9404.html 
│                       │      │                  ├ [13]: https://lists.gnupg.org/pipermail/gcrypt-devel/2024-M
│                       │      │                  │       arch/005607.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2024-2236 
│                       │      │                  ╰ [15]: https://www.cve.org/CVERecord?id=CVE-2024-2236 
│                       │      ├ PublishedDate   : 2024-03-06T22:15:57.977Z 
│                       │      ╰ LastModifiedDate: 2025-04-02T17:15:37.79Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2025-8941 
│                       │      ├ PkgID           : libpam-modules@1.5.3-7ubuntu4.4 
│                       │      ├ PkgName         : libpam-modules 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam-modules@1.5.3-7ubuntu4.4?arch=a
│                       │      │                  │       md64&distro=ubuntu-25.04 
│                       │      │                  ╰ UID : c49554b6d433bfcd 
│                       │      ├ InstalledVersion: 1.5.3-7ubuntu4.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-8941 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : linux-pam: Incomplete fix for CVE-2025-6020 
│                       │      ├ Description     : A flaw was found in linux-pam. The pam_namespace module may
│                       │      │                   improperly handle user-controlled paths, allowing local
│                       │      │                   users to exploit symlink attacks and race conditions to
│                       │      │                   elevate their privileges to root. This CVE provides a
│                       │      │                   "complete" fix for CVE-2025-6020. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:14557 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2025:15099 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2025:15100 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2025:15101 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2025:15102 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2025:15103 
│                       │      │                  ├ [6] : https://access.redhat.com/errata/RHSA-2025:15104 
│                       │      │                  ├ [7] : https://access.redhat.com/errata/RHSA-2025:15105 
│                       │      │                  ├ [8] : https://access.redhat.com/errata/RHSA-2025:15106 
│                       │      │                  ├ [9] : https://access.redhat.com/errata/RHSA-2025:15107 
│                       │      │                  ├ [10]: https://access.redhat.com/errata/RHSA-2025:15709 
│                       │      │                  ├ [11]: https://access.redhat.com/errata/RHSA-2025:15827 
│                       │      │                  ├ [12]: https://access.redhat.com/errata/RHSA-2025:15828 
│                       │      │                  ├ [13]: https://access.redhat.com/errata/RHSA-2025:16524 
│                       │      │                  ├ [14]: https://access.redhat.com/security/cve/CVE-2025-8941 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/2372512 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/2388220 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2372512 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2388220 
│                       │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-6020 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-8941 
│                       │      │                  ├ [21]: https://errata.almalinux.org/9/ALSA-2025-15099.html 
│                       │      │                  ├ [22]: https://errata.rockylinux.org/RLSA-2025:14557 
│                       │      │                  ├ [23]: https://linux.oracle.com/cve/CVE-2025-8941.html 
│                       │      │                  ├ [24]: https://linux.oracle.com/errata/ELSA-2025-15099.html 
│                       │      │                  ├ [25]: https://nvd.nist.gov/vuln/detail/CVE-2025-8941 
│                       │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2025-8941 
│                       │      ├ PublishedDate   : 2025-08-13T15:15:41.873Z 
│                       │      ╰ LastModifiedDate: 2025-09-23T20:15:33.927Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2025-8941 
│                       │      ├ PkgID           : libpam-modules-bin@1.5.3-7ubuntu4.4 
│                       │      ├ PkgName         : libpam-modules-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam-modules-bin@1.5.3-7ubuntu4.4?ar
│                       │      │                  │       ch=amd64&distro=ubuntu-25.04 
│                       │      │                  ╰ UID : 5357e0bb8a1ff079 
│                       │      ├ InstalledVersion: 1.5.3-7ubuntu4.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-8941 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : linux-pam: Incomplete fix for CVE-2025-6020 
│                       │      ├ Description     : A flaw was found in linux-pam. The pam_namespace module may
│                       │      │                   improperly handle user-controlled paths, allowing local
│                       │      │                   users to exploit symlink attacks and race conditions to
│                       │      │                   elevate their privileges to root. This CVE provides a
│                       │      │                   "complete" fix for CVE-2025-6020. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:14557 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2025:15099 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2025:15100 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2025:15101 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2025:15102 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2025:15103 
│                       │      │                  ├ [6] : https://access.redhat.com/errata/RHSA-2025:15104 
│                       │      │                  ├ [7] : https://access.redhat.com/errata/RHSA-2025:15105 
│                       │      │                  ├ [8] : https://access.redhat.com/errata/RHSA-2025:15106 
│                       │      │                  ├ [9] : https://access.redhat.com/errata/RHSA-2025:15107 
│                       │      │                  ├ [10]: https://access.redhat.com/errata/RHSA-2025:15709 
│                       │      │                  ├ [11]: https://access.redhat.com/errata/RHSA-2025:15827 
│                       │      │                  ├ [12]: https://access.redhat.com/errata/RHSA-2025:15828 
│                       │      │                  ├ [13]: https://access.redhat.com/errata/RHSA-2025:16524 
│                       │      │                  ├ [14]: https://access.redhat.com/security/cve/CVE-2025-8941 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/2372512 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/2388220 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2372512 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2388220 
│                       │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-6020 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-8941 
│                       │      │                  ├ [21]: https://errata.almalinux.org/9/ALSA-2025-15099.html 
│                       │      │                  ├ [22]: https://errata.rockylinux.org/RLSA-2025:14557 
│                       │      │                  ├ [23]: https://linux.oracle.com/cve/CVE-2025-8941.html 
│                       │      │                  ├ [24]: https://linux.oracle.com/errata/ELSA-2025-15099.html 
│                       │      │                  ├ [25]: https://nvd.nist.gov/vuln/detail/CVE-2025-8941 
│                       │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2025-8941 
│                       │      ├ PublishedDate   : 2025-08-13T15:15:41.873Z 
│                       │      ╰ LastModifiedDate: 2025-09-23T20:15:33.927Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2025-8941 
│                       │      ├ PkgID           : libpam-runtime@1.5.3-7ubuntu4.4 
│                       │      ├ PkgName         : libpam-runtime 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam-runtime@1.5.3-7ubuntu4.4?arch=a
│                       │      │                  │       ll&distro=ubuntu-25.04 
│                       │      │                  ╰ UID : ff7c6fc616e7055b 
│                       │      ├ InstalledVersion: 1.5.3-7ubuntu4.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-8941 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : linux-pam: Incomplete fix for CVE-2025-6020 
│                       │      ├ Description     : A flaw was found in linux-pam. The pam_namespace module may
│                       │      │                   improperly handle user-controlled paths, allowing local
│                       │      │                   users to exploit symlink attacks and race conditions to
│                       │      │                   elevate their privileges to root. This CVE provides a
│                       │      │                   "complete" fix for CVE-2025-6020. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:14557 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2025:15099 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2025:15100 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2025:15101 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2025:15102 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2025:15103 
│                       │      │                  ├ [6] : https://access.redhat.com/errata/RHSA-2025:15104 
│                       │      │                  ├ [7] : https://access.redhat.com/errata/RHSA-2025:15105 
│                       │      │                  ├ [8] : https://access.redhat.com/errata/RHSA-2025:15106 
│                       │      │                  ├ [9] : https://access.redhat.com/errata/RHSA-2025:15107 
│                       │      │                  ├ [10]: https://access.redhat.com/errata/RHSA-2025:15709 
│                       │      │                  ├ [11]: https://access.redhat.com/errata/RHSA-2025:15827 
│                       │      │                  ├ [12]: https://access.redhat.com/errata/RHSA-2025:15828 
│                       │      │                  ├ [13]: https://access.redhat.com/errata/RHSA-2025:16524 
│                       │      │                  ├ [14]: https://access.redhat.com/security/cve/CVE-2025-8941 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/2372512 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/2388220 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2372512 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2388220 
│                       │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-6020 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-8941 
│                       │      │                  ├ [21]: https://errata.almalinux.org/9/ALSA-2025-15099.html 
│                       │      │                  ├ [22]: https://errata.rockylinux.org/RLSA-2025:14557 
│                       │      │                  ├ [23]: https://linux.oracle.com/cve/CVE-2025-8941.html 
│                       │      │                  ├ [24]: https://linux.oracle.com/errata/ELSA-2025-15099.html 
│                       │      │                  ├ [25]: https://nvd.nist.gov/vuln/detail/CVE-2025-8941 
│                       │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2025-8941 
│                       │      ├ PublishedDate   : 2025-08-13T15:15:41.873Z 
│                       │      ╰ LastModifiedDate: 2025-09-23T20:15:33.927Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2025-8941 
│                       │      ├ PkgID           : libpam0g@1.5.3-7ubuntu4.4 
│                       │      ├ PkgName         : libpam0g 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam0g@1.5.3-7ubuntu4.4?arch=amd64&d
│                       │      │                  │       istro=ubuntu-25.04 
│                       │      │                  ╰ UID : e7da9492a7d7e6e9 
│                       │      ├ InstalledVersion: 1.5.3-7ubuntu4.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-8941 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : linux-pam: Incomplete fix for CVE-2025-6020 
│                       │      ├ Description     : A flaw was found in linux-pam. The pam_namespace module may
│                       │      │                   improperly handle user-controlled paths, allowing local
│                       │      │                   users to exploit symlink attacks and race conditions to
│                       │      │                   elevate their privileges to root. This CVE provides a
│                       │      │                   "complete" fix for CVE-2025-6020. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:14557 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2025:15099 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2025:15100 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2025:15101 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2025:15102 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2025:15103 
│                       │      │                  ├ [6] : https://access.redhat.com/errata/RHSA-2025:15104 
│                       │      │                  ├ [7] : https://access.redhat.com/errata/RHSA-2025:15105 
│                       │      │                  ├ [8] : https://access.redhat.com/errata/RHSA-2025:15106 
│                       │      │                  ├ [9] : https://access.redhat.com/errata/RHSA-2025:15107 
│                       │      │                  ├ [10]: https://access.redhat.com/errata/RHSA-2025:15709 
│                       │      │                  ├ [11]: https://access.redhat.com/errata/RHSA-2025:15827 
│                       │      │                  ├ [12]: https://access.redhat.com/errata/RHSA-2025:15828 
│                       │      │                  ├ [13]: https://access.redhat.com/errata/RHSA-2025:16524 
│                       │      │                  ├ [14]: https://access.redhat.com/security/cve/CVE-2025-8941 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/2372512 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/2388220 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2372512 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2388220 
│                       │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-6020 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-8941 
│                       │      │                  ├ [21]: https://errata.almalinux.org/9/ALSA-2025-15099.html 
│                       │      │                  ├ [22]: https://errata.rockylinux.org/RLSA-2025:14557 
│                       │      │                  ├ [23]: https://linux.oracle.com/cve/CVE-2025-8941.html 
│                       │      │                  ├ [24]: https://linux.oracle.com/errata/ELSA-2025-15099.html 
│                       │      │                  ├ [25]: https://nvd.nist.gov/vuln/detail/CVE-2025-8941 
│                       │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2025-8941 
│                       │      ├ PublishedDate   : 2025-08-13T15:15:41.873Z 
│                       │      ╰ LastModifiedDate: 2025-09-23T20:15:33.927Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : login.defs@1:4.16.0-7ubuntu1 
│                       │      ├ PkgName         : login.defs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login.defs@4.16.0-7ubuntu1?arch=all&di
│                       │      │                  │       stro=ubuntu-25.04&epoch=1 
│                       │      │                  ╰ UID : 4016d70dedce9ad0 
│                       │      ├ InstalledVersion: 1:4.16.0-7ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : shadow-utils: Default subordinate ID configuration in
│                       │      │                   /etc/login.defs could lead to compromise 
│                       │      ├ Description     : shadow-utils (aka shadow) 4.4 through 4.17.0 establishes a
│                       │      │                   default /etc/subuid behavior (e.g., uid 100000 through
│                       │      │                   165535 for the first user account) that can realistically
│                       │      │                   conflict with the uids of users defined on locally
│                       │      │                   administered networks, potentially leading to account
│                       │      │                   takeover, e.g., by leveraging newuidmap for access to an NFS
│                       │      │                    home directory (or same-host resources in the case of
│                       │      │                   remote logins by these local network users). NOTE: it may
│                       │      │                   also be argued that system administrators should not have
│                       │      │                   assigned uids, within local networks, that are within the
│                       │      │                   range that can occur in /etc/subuid. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-1188 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.6 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-56433 
│                       │      │                  ├ [1]: https://github.com/shadow-maint/shadow/blob/e2512d5741
│                       │      │                  │      d4a44bdd81a8c2d0029b6222728cf0/etc/login.defs#L238-L24
│                       │      │                  │      1 
│                       │      │                  ├ [2]: https://github.com/shadow-maint/shadow/issues/1157 
│                       │      │                  ├ [3]: https://github.com/shadow-maint/shadow/releases/tag/4.4 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-56433 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2024-56433 
│                       │      ├ PublishedDate   : 2024-12-26T09:15:07.267Z 
│                       │      ╰ LastModifiedDate: 2024-12-26T09:15:07.267Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : passwd@1:4.16.0-7ubuntu1 
│                       │      ├ PkgName         : passwd 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/passwd@4.16.0-7ubuntu1?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-25.04&epoch=1 
│                       │      │                  ╰ UID : 3bc9adb4bf916fa 
│                       │      ├ InstalledVersion: 1:4.16.0-7ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                       │      │                  │         231a32f51a5a9c67df7c 
│                       │      │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                       │      │                            3e4377403b1cd0feb1b2 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : shadow-utils: Default subordinate ID configuration in
│                       │      │                   /etc/login.defs could lead to compromise 
│                       │      ├ Description     : shadow-utils (aka shadow) 4.4 through 4.17.0 establishes a
│                       │      │                   default /etc/subuid behavior (e.g., uid 100000 through
│                       │      │                   165535 for the first user account) that can realistically
│                       │      │                   conflict with the uids of users defined on locally
│                       │      │                   administered networks, potentially leading to account
│                       │      │                   takeover, e.g., by leveraging newuidmap for access to an NFS
│                       │      │                    home directory (or same-host resources in the case of
│                       │      │                   remote logins by these local network users). NOTE: it may
│                       │      │                   also be argued that system administrators should not have
│                       │      │                   assigned uids, within local networks, that are within the
│                       │      │                   range that can occur in /etc/subuid. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-1188 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.6 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-56433 
│                       │      │                  ├ [1]: https://github.com/shadow-maint/shadow/blob/e2512d5741
│                       │      │                  │      d4a44bdd81a8c2d0029b6222728cf0/etc/login.defs#L238-L24
│                       │      │                  │      1 
│                       │      │                  ├ [2]: https://github.com/shadow-maint/shadow/issues/1157 
│                       │      │                  ├ [3]: https://github.com/shadow-maint/shadow/releases/tag/4.4 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-56433 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2024-56433 
│                       │      ├ PublishedDate   : 2024-12-26T09:15:07.267Z 
│                       │      ╰ LastModifiedDate: 2024-12-26T09:15:07.267Z 
│                       ╰ [13] ╭ VulnerabilityID : CVE-2025-45582 
│                              ├ PkgID           : tar@1.35+dfsg-3.1 
│                              ├ PkgName         : tar 
│                              ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-3.1?arch=amd64&distro=
│                              │                  │       ubuntu-25.04 
│                              │                  ╰ UID : a03ee9a61d584e89 
│                              ├ InstalledVersion: 1.35+dfsg-3.1 
│                              ├ Status          : affected 
│                              ├ Layer            ╭ Digest: sha256:88267c28f04e9c2736e826e70fb2696ca6b0dca10d21
│                              │                  │         231a32f51a5a9c67df7c 
│                              │                  ╰ DiffID: sha256:41cfd3533f489ded44c523489c3f6415944371c0b5e2
│                              │                            3e4377403b1cd0feb1b2 
│                              ├ SeveritySource  : ubuntu 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-45582 
│                              ├ DataSource       ╭ ID  : ubuntu 
│                              │                  ├ Name: Ubuntu CVE Tracker 
│                              │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                              ├ Title           : tar: Tar path traversal 
│                              ├ Description     : GNU Tar through 1.35 allows file overwrite via directory
│                              │                   traversal in crafted TAR archives, with a certain two-step
│                              │                   process. First, the victim must extract an archive that
│                              │                   contains a ../ symlink to a critical directory. Second, the
│                              │                   victim must extract an archive that contains a critical
│                              │                   file, specified via a relative pathname that begins with the
│                              │                    symlink name and ends with that critical file's name. Here,
│                              │                    the extraction follows the symlink and overwrites the
│                              │                   critical file. This bypasses the protection mechanism of
│                              │                   "Member name contains '..'" that would occur for a single
│                              │                   TAR archive that attempted to specify the critical file via
│                              │                   a ../ approach. For example, the first archive can contain
│                              │                   "x -> ../../../../../home/victim/.ssh" and the second
│                              │                   archive can contain x/authorized_keys. This can affect
│                              │                   server applications that automatically extract any number of
│                              │                    user-supplied TAR archives, and were relying on the
│                              │                   blocking of traversal. This can also affect software
│                              │                   installation processes in which "tar xf" is run more than
│                              │                   once (e.g., when installing a package can automatically
│                              │                   install two dependencies that are set up as untrusted
│                              │                   tarballs instead of official packages). NOTE: the official
│                              │                   GNU Tar manual has an otherwise-empty directory for each
│                              │                   "tar xf" in its Security Rules of Thumb; however,
│                              │                   third-party advice leads users to run "tar xf" more than
│                              │                   once into the same directory. 
│                              ├ Severity        : MEDIUM 
│                              ├ CweIDs           ─ [0]: CWE-24 
│                              ├ VendorSeverity   ╭ redhat: 2 
│                              │                  ╰ ubuntu: 2 
│                              ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                              │                           │           /A:L 
│                              │                           ╰ V3Score : 5.6 
│                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-45582 
│                              │                  ├ [1]: https://github.com/i900008/vulndb/blob/main/Gnu_tar_vu
│                              │                  │      ln.md 
│                              │                  ├ [2]: https://lists.gnu.org/archive/html/bug-tar/2025-08/msg
│                              │                  │      00012.html 
│                              │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2025-45582 
│                              │                  ├ [4]: https://www.cve.org/CVERecord?id=CVE-2025-45582 
│                              │                  ├ [5]: https://www.gnu.org/software/tar/ 
│                              │                  ├ [6]: https://www.gnu.org/software/tar/manual/html_node/Inte
│                              │                  │      grity.html 
│                              │                  ├ [7]: https://www.gnu.org/software/tar/manual/html_node/Inte
│                              │                  │      grity.html#Integrity 
│                              │                  ╰ [8]: https://www.gnu.org/software/tar/manual/html_node/Secu
│                              │                         rity-rules-of-thumb.html 
│                              ├ PublishedDate   : 2025-07-11T17:15:37.183Z 
│                              ╰ LastModifiedDate: 2025-08-18T04:15:36.743Z 
╰ [1] ╭ Target: Java 
      ├ Class : lang-pkgs 
      ╰ Type  : jar 
````
