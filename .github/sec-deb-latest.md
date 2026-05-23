```yaml
╭ [0] ╭ Target         : openaf/oaf:deb (ubuntu 25.10) 
│     ├ Class          : os-pkgs 
│     ├ Type           : ubuntu 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]   ╭ VulnerabilityID : CVE-2026-27456 
│                       │       ├ PkgID           : bsdutils@1:2.41-4ubuntu4.2 
│                       │       ├ PkgName         : bsdutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/bsdutils@2.41-4ubuntu4.2?arch=amd64&d
│                       │       │                  │       istro=ubuntu-25.10&epoch=1 
│                       │       │                  ╰ UID : 411fc06346b75c80 
│                       │       ├ InstalledVersion: 1:2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:68fdb863021eacee3ef1e9bb571a84b0ef2997d0c5624dc8c85a
│                       │       │                   18cbe01e82dd 
│                       │       ├ Title           : util-linux: TOCTOU in the mount program when setting up
│                       │       │                   loop devices 
│                       │       ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │       │                    to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │       │                   vulnerability has been identified in the SUID binary
│                       │       │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │       │                   setting up loop devices, validates the source file path
│                       │       │                   with user privileges via fork() + setuid() + realpath(),
│                       │       │                   but subsequently re-canonicalizes and opens it with root
│                       │       │                   privileges (euid=0) without verifying that the path has not
│                       │       │                    been replaced between both operations. Neither O_NOFOLLOW,
│                       │       │                    nor inode comparison, nor post-open fstat() are employed.
│                       │       │                   This allows a local unprivileged user to replace the source
│                       │       │                    file with a symlink pointing to any root-owned file or
│                       │       │                   device during the race window, causing the SUID binary to
│                       │       │                   open and mount it as root. Exploitation requires an
│                       │       │                   /etc/fstab entry with user,loop options whose path points
│                       │       │                   to a directory where the attacker has write permission, and
│                       │       │                    that /usr/bin/mount has the SUID bit set (the default
│                       │       │                   configuration on virtually all Linux distributions). The
│                       │       │                   impact is unauthorized read access to root-protected files
│                       │       │                   and block devices, including backup images, disk volumes,
│                       │       │                   and any file containing a valid filesystem. This issue has
│                       │       │                   been patched in version 2.41.4. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-59 
│                       │       │                  ├ [1]: CWE-269 
│                       │       │                  ╰ [2]: CWE-367 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ julia : 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 4.7 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 4.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │       │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e390
│                       │       │                  │      467b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │       │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag
│                       │       │                  │      /v2.41.4 
│                       │       │                  ├ [3]: https://github.com/util-linux/util-linux/security/adv
│                       │       │                  │      isories/GHSA-qq4x-vfq4-9h9g 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │       ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │       ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [1]   ╭ VulnerabilityID : CVE-2026-3184 
│                       │       ├ PkgID           : bsdutils@1:2.41-4ubuntu4.2 
│                       │       ├ PkgName         : bsdutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/bsdutils@2.41-4ubuntu4.2?arch=amd64&d
│                       │       │                  │       istro=ubuntu-25.10&epoch=1 
│                       │       │                  ╰ UID : 411fc06346b75c80 
│                       │       ├ InstalledVersion: 1:2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:d23ddeb6297633c14e74a801554d5146218fd27c1250b2fd0064
│                       │       │                   8ea19a67b958 
│                       │       ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │       │                   improper hostname canonicalization 
│                       │       ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │       │                   canonicalization in the `login(1)` utility, when invoked
│                       │       │                   with the `-h` option, can modify the supplied remote
│                       │       │                   hostname before setting `PAM_RHOST`. A remote attacker
│                       │       │                   could exploit this by providing a specially crafted
│                       │       │                   hostname, potentially bypassing host-based Pluggable
│                       │       │                   Authentication Modules (PAM) access control rules that rely
│                       │       │                    on fully qualified domain names. This could lead to
│                       │       │                   unauthorized access. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-289 
│                       │       ├ VendorSeverity   ╭ azure : 1 
│                       │       │                  ├ nvd   : 2 
│                       │       │                  ├ redhat: 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                  │        │           L/A:N 
│                       │       │                  │        ╰ V3Score : 5.3 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 3.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │       │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │       ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │       ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [2]   ╭ VulnerabilityID : CVE-2026-5545 
│                       │       ├ PkgID           : curl@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : curl 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.14.1-2ubuntu1.2?arch=amd64&dis
│                       │       │                  │       tro=ubuntu-25.10 
│                       │       │                  ╰ UID : 528931dd8c8372ba 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5545 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:8bc8e83961db161e0375eaf64c58192b0d6af1a01a18bc6eb6e2
│                       │       │                   8fadc7e29f76 
│                       │       ├ Title           : curl: libcurl: Authentication bypass due to incorrect HTTP
│                       │       │                   Negotiate connection reuse 
│                       │       ├ Description     : libcurl might in some circumstances reuse the wrong
│                       │       │                   connection when asked to
│                       │       │                   do an authenticated HTTP(S) request after a
│                       │       │                   Negotiate-authenticated one, when
│                       │       │                   both use the same host.
│                       │       │                   
│                       │       │                   libcurl features a pool of recent connections so that
│                       │       │                   subsequent requests can
│                       │       │                   reuse an existing connection to avoid overhead.
│                       │       │                   When reusing a connection a range of criteria must be met.
│                       │       │                   Due to a logical
│                       │       │                   error in the code, a request that was issued by an
│                       │       │                   application could
│                       │       │                   wrongfully reuse an existing connection to the same server
│                       │       │                   that was
│                       │       │                   authenticated using different credentials.
│                       │       │                   An application that first uses Negotiate authentication to
│                       │       │                   a server with
│                       │       │                   `user1:password1` and then does another operation to the
│                       │       │                   same server asking
│                       │       │                   for any authentication method but for `user2:password2`
│                       │       │                   (while the previous
│                       │       │                   connection is still alive) - the second request gets
│                       │       │                   confused and wrongly
│                       │       │                   reuses the same connection and sends the new request over
│                       │       │                   that connection
│                       │       │                   thinking it uses a mix of user1's and user2's credentials
│                       │       │                   when it is in fact
│                       │       │                   still using the connection authenticated for user1... 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-613 
│                       │       ├ VendorSeverity   ╭ nvd   : 2 
│                       │       │                  ├ photon: 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:
│                       │       │                  │        │           H/A:N 
│                       │       │                  │        ╰ V3Score : 6.5 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:
│                       │       │                           │           H/A:N 
│                       │       │                           ╰ V3Score : 6.5 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-5545 
│                       │       │                  ├ [1]: https://curl.se/docs/CVE-2026-5545.html 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-5545.json 
│                       │       │                  ├ [3]: https://hackerone.com/reports/3642555 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-5545 
│                       │       │                  ├ [5]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-5545 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:56.19Z 
│                       │       ╰ LastModifiedDate: 2026-05-13T19:31:07.633Z 
│                       ├ [3]   ╭ VulnerabilityID : CVE-2026-6253 
│                       │       ├ PkgID           : curl@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : curl 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.14.1-2ubuntu1.2?arch=amd64&dis
│                       │       │                  │       tro=ubuntu-25.10 
│                       │       │                  ╰ UID : 528931dd8c8372ba 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6253 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:07b6aa889b14471a33297feeb6d9e6555a3519f3111ed33e86e2
│                       │       │                   c6b1dcd8881e 
│                       │       ├ Title           : curl: curl: Proxy credential disclosure via redirects to
│                       │       │                   unauthenticated proxies 
│                       │       ├ Description     : curl might erroneously pass on credentials for a first
│                       │       │                   proxy to a second
│                       │       │                   proxy.
│                       │       │                   
│                       │       │                   This can happen when the following conditions are true:
│                       │       │                   1. curl is setup to use specific different proxies for
│                       │       │                   different URL schemes
│                       │       │                   2. the first proxy needs credentials
│                       │       │                   3. the second proxy uses no credentials
│                       │       │                   4. while using the first proxy (using say `http://`), curl
│                       │       │                   is asked to follow
│                       │       │                      a redirect to a URL using another scheme (say
│                       │       │                   `https://`), accessed using a
│                       │       │                      second, different, proxy 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-522 
│                       │       ├ VendorSeverity   ╭ photon: 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 5.3 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/29
│                       │       │                  │      /11 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-6253 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-6253.html 
│                       │       │                  ├ [3]: https://curl.se/docs/CVE-2026-6253.json 
│                       │       │                  ├ [4]: https://hackerone.com/reports/3669637 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-6253 
│                       │       │                  ├ [6]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-6253 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:56.57Z 
│                       │       ╰ LastModifiedDate: 2026-05-14T13:40:53.19Z 
│                       ├ [4]   ╭ VulnerabilityID : CVE-2026-6429 
│                       │       ├ PkgID           : curl@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : curl 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.14.1-2ubuntu1.2?arch=amd64&dis
│                       │       │                  │       tro=ubuntu-25.10 
│                       │       │                  ╰ UID : 528931dd8c8372ba 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6429 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:c830f57952786648f2459ccfbd0e42d4c185a4fa51796acbcaba
│                       │       │                   1087392d9c1f 
│                       │       ├ Title           : curl: libcurl: Credential leak via reused proxy connection
│                       │       │                   during HTTP redirects 
│                       │       ├ Description     : When asked to both use a `.netrc` file for credentials and
│                       │       │                   to follow HTTP
│                       │       │                   redirects, libcurl could leak the password used for the
│                       │       │                   first host to the
│                       │       │                   followed-to host under certain circumstances. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ VendorSeverity   ╭ photon: 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 6.5 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-6429 
│                       │       │                  ├ [1]: https://curl.se/docs/CVE-2026-6429.html 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-6429.json 
│                       │       │                  ├ [3]: https://hackerone.com/reports/3677759 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-6429 
│                       │       │                  ├ [5]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-6429 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:56.93Z 
│                       │       ╰ LastModifiedDate: 2026-05-14T14:18:02.24Z 
│                       ├ [5]   ╭ VulnerabilityID : CVE-2026-7168 
│                       │       ├ PkgID           : curl@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : curl 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.14.1-2ubuntu1.2?arch=amd64&dis
│                       │       │                  │       tro=ubuntu-25.10 
│                       │       │                  ╰ UID : 528931dd8c8372ba 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-7168 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:691eaee2d990ab2a28c87944ecac0bdbe5613472f1f2d480a5df
│                       │       │                   1305d394fe31 
│                       │       ├ Title           : curl: libcurl: Information disclosure via incorrect
│                       │       │                   Proxy-Authorization header reuse 
│                       │       ├ Description     : Successfully using libcurl to do a transfer over a specific
│                       │       │                    HTTP proxy
│                       │       │                   (`proxyA`) with **Digest** authentication and then changing
│                       │       │                    the proxy host to
│                       │       │                   a second one (`proxyB`) for a second transfer, reusing the
│                       │       │                   same handle, makes
│                       │       │                   libcurl wrongly pass on the `Proxy-Authorization:` header
│                       │       │                   field meant for
│                       │       │                   `proxyA`, to `proxyB`. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-294 
│                       │       ├ VendorSeverity   ╭ nvd   : 2 
│                       │       │                  ├ photon: 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 5.3 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 5.3 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/29
│                       │       │                  │      /14 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-7168 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-7168.html 
│                       │       │                  ├ [3]: https://curl.se/docs/CVE-2026-7168.json 
│                       │       │                  ├ [4]: https://hackerone.com/reports/3697719 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-7168 
│                       │       │                  ├ [6]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-7168 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:57.2Z 
│                       │       ╰ LastModifiedDate: 2026-05-14T14:12:48.457Z 
│                       ├ [6]   ╭ VulnerabilityID : CVE-2026-4873 
│                       │       ├ PkgID           : curl@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : curl 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.14.1-2ubuntu1.2?arch=amd64&dis
│                       │       │                  │       tro=ubuntu-25.10 
│                       │       │                  ╰ UID : 528931dd8c8372ba 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4873 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:2c3fee5694fbbc6866ce8b53ae0265c78e8a9295d4a50a1f0996
│                       │       │                   235511d28e28 
│                       │       ├ Title           : curl: curl: Information disclosure due to incorrect TLS
│                       │       │                   connection reuse 
│                       │       ├ Description     : A vulnerability exists where a connection requiring TLS
│                       │       │                   incorrectly reuses an
│                       │       │                   existing unencrypted connection from the same connection
│                       │       │                   pool. If an initial
│                       │       │                   transfer is made in clear-text (via IMAP, SMTP, or POP3), a
│                       │       │                    subsequent request
│                       │       │                   to that same host bypasses the TLS requirement and instead
│                       │       │                   transmit data
│                       │       │                   unencrypted. 
│                       │       ├ Severity        : LOW 
│                       │       ├ CweIDs           ╭ [0]: CWE-295 
│                       │       │                  ╰ [1]: CWE-319 
│                       │       ├ VendorSeverity   ╭ photon: 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 1 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 5.3 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/29/7 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-4873 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-4873.html 
│                       │       │                  ├ [3]: https://curl.se/docs/CVE-2026-4873.json 
│                       │       │                  ├ [4]: https://hackerone.com/reports/3621851 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-4873 
│                       │       │                  ├ [6]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-4873 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:55.893Z 
│                       │       ╰ LastModifiedDate: 2026-05-14T13:45:11.407Z 
│                       ├ [7]   ╭ VulnerabilityID : CVE-2026-5773 
│                       │       ├ PkgID           : curl@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : curl 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.14.1-2ubuntu1.2?arch=amd64&dis
│                       │       │                  │       tro=ubuntu-25.10 
│                       │       │                  ╰ UID : 528931dd8c8372ba 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5773 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:e66db9845c3ea0750a92bedbec12263354567781124db45d0ef6
│                       │       │                   83cd519a13d3 
│                       │       ├ Title           : curl: libcurl: Wrong file transfer due to incorrect SMB
│                       │       │                   connection reuse 
│                       │       ├ Description     : libcurl might in some circumstances reuse the wrong
│                       │       │                   connection for SMB(S)
│                       │       │                   transfers.
│                       │       │                   
│                       │       │                   libcurl features a pool of recent connections so that
│                       │       │                   subsequent requests can
│                       │       │                   reuse an existing connection to avoid overhead.
│                       │       │                   When reusing a connection a range of criteria must be met.
│                       │       │                   Due to a logical
│                       │       │                   error in the code, a network transfer operation that was
│                       │       │                   requested by an
│                       │       │                   application could wrongfully reuse an existing SMB
│                       │       │                   connection to the same
│                       │       │                   server that was using a different 'share' than the new
│                       │       │                   subsequent transfer
│                       │       │                   should.
│                       │       │                   This could in unlucky situations lead to the download of
│                       │       │                   the wrong file or the
│                       │       │                   upload of a file to the wrong place. When this happens, the
│                       │       │                    same credentials
│                       │       │                   are used and the server name is the same. 
│                       │       ├ Severity        : LOW 
│                       │       ├ CweIDs           ─ [0]: CWE-918 
│                       │       ├ VendorSeverity   ╭ nvd   : 3 
│                       │       │                  ├ photon: 3 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 1 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 7.5 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 6.5 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/29/9 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-5773 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-5773.html 
│                       │       │                  ├ [3]: https://curl.se/docs/CVE-2026-5773.json 
│                       │       │                  ├ [4]: https://hackerone.com/reports/3650689 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-5773 
│                       │       │                  ├ [6]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-5773 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:56.307Z 
│                       │       ╰ LastModifiedDate: 2026-05-13T19:13:14.097Z 
│                       ├ [8]   ╭ VulnerabilityID : CVE-2026-6276 
│                       │       ├ PkgID           : curl@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : curl 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.14.1-2ubuntu1.2?arch=amd64&dis
│                       │       │                  │       tro=ubuntu-25.10 
│                       │       │                  ╰ UID : 528931dd8c8372ba 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6276 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:2e38f1d1eb77b79aecd5270074c9bb4a635f929e63871254af03
│                       │       │                   a3c72d3d06ad 
│                       │       ├ Title           : curl: libcurl: Information disclosure due to cookie leak
│                       │       │                   when reusing connections with custom Host headers 
│                       │       ├ Description     : Using libcurl, when a custom `Host:` header is first set
│                       │       │                   for an HTTP request
│                       │       │                   and a second request is subsequently done using the same
│                       │       │                   *easy handle* but
│                       │       │                   without the custom `Host:` header set, the second request
│                       │       │                   would use stale
│                       │       │                   information and pass on cookies meant for the first host in
│                       │       │                    the second
│                       │       │                   request. Leak them. 
│                       │       ├ Severity        : LOW 
│                       │       ├ CweIDs           ─ [0]: CWE-319 
│                       │       ├ VendorSeverity   ╭ nvd   : 3 
│                       │       │                  ├ photon: 3 
│                       │       │                  ├ redhat: 1 
│                       │       │                  ╰ ubuntu: 1 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                  │        │           N/A:H 
│                       │       │                  │        ╰ V3Score : 7.5 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 3.7 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/29
│                       │       │                  │      /13 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-6276 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-6276.html 
│                       │       │                  ├ [3]: https://curl.se/docs/CVE-2026-6276.json 
│                       │       │                  ├ [4]: https://hackerone.com/reports/3671818 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-6276 
│                       │       │                  ├ [6]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-6276 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:56.8Z 
│                       │       ╰ LastModifiedDate: 2026-05-14T14:21:06.997Z 
│                       ├ [9]   ╭ VulnerabilityID : CVE-2026-2219 
│                       │       ├ PkgID           : dpkg@1.22.21ubuntu3.1 
│                       │       ├ PkgName         : dpkg 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/dpkg@1.22.21ubuntu3.1?arch=amd64&dist
│                       │       │                  │       ro=ubuntu-25.10 
│                       │       │                  ╰ UID : 441b18c6d9fcf5d3 
│                       │       ├ InstalledVersion: 1.22.21ubuntu3.1 
│                       │       ├ FixedVersion    : 1.22.21ubuntu3.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-2219 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:9044119541c4b23c39caeded47bf3372ae3ea9ddac3e2519bc11
│                       │       │                   10d0128bae9f 
│                       │       ├ Title           : It was discovered that dpkg-deb (a component of dpkg, the
│                       │       │                   Debian packa ... 
│                       │       ├ Description     : It was discovered that dpkg-deb (a component of dpkg, the
│                       │       │                   Debian package management system) does not properly
│                       │       │                   validate the end of the data stream when uncompressing a
│                       │       │                   zstd-compressed .deb archive, which may result in denial of
│                       │       │                    service (infinite loop spinning the CPU). 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-835 
│                       │       ├ VendorSeverity   ─ ubuntu: 2 
│                       │       ├ References       ╭ [0]: https://bugs.debian.org/1129722 
│                       │       │                  ├ [1]: https://git.dpkg.org/cgit/dpkg/dpkg.git/commit/?id=66
│                       │       │                  │      10297a62c0780dd0e80b0e302ef64fdcc9d313 
│                       │       │                  ├ [2]: https://ubuntu.com/security/notices/USN-8249-1 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-2219 
│                       │       ├ PublishedDate   : 2026-03-07T09:16:07.823Z 
│                       │       ╰ LastModifiedDate: 2026-03-09T15:15:57.87Z 
│                       ├ [10]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │       ├ PkgID           : libblkid1@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : libblkid1 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libblkid1@2.41-4ubuntu4.2?arch=amd64&
│                       │       │                  │       distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ddaca4141760dfcf 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:24ac7a58d476df18769656a1074c7ebce8ca9322f2da47d2a782
│                       │       │                   f559d960f5e4 
│                       │       ├ Title           : util-linux: TOCTOU in the mount program when setting up
│                       │       │                   loop devices 
│                       │       ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │       │                    to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │       │                   vulnerability has been identified in the SUID binary
│                       │       │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │       │                   setting up loop devices, validates the source file path
│                       │       │                   with user privileges via fork() + setuid() + realpath(),
│                       │       │                   but subsequently re-canonicalizes and opens it with root
│                       │       │                   privileges (euid=0) without verifying that the path has not
│                       │       │                    been replaced between both operations. Neither O_NOFOLLOW,
│                       │       │                    nor inode comparison, nor post-open fstat() are employed.
│                       │       │                   This allows a local unprivileged user to replace the source
│                       │       │                    file with a symlink pointing to any root-owned file or
│                       │       │                   device during the race window, causing the SUID binary to
│                       │       │                   open and mount it as root. Exploitation requires an
│                       │       │                   /etc/fstab entry with user,loop options whose path points
│                       │       │                   to a directory where the attacker has write permission, and
│                       │       │                    that /usr/bin/mount has the SUID bit set (the default
│                       │       │                   configuration on virtually all Linux distributions). The
│                       │       │                   impact is unauthorized read access to root-protected files
│                       │       │                   and block devices, including backup images, disk volumes,
│                       │       │                   and any file containing a valid filesystem. This issue has
│                       │       │                   been patched in version 2.41.4. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-59 
│                       │       │                  ├ [1]: CWE-269 
│                       │       │                  ╰ [2]: CWE-367 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ julia : 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 4.7 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 4.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │       │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e390
│                       │       │                  │      467b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │       │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag
│                       │       │                  │      /v2.41.4 
│                       │       │                  ├ [3]: https://github.com/util-linux/util-linux/security/adv
│                       │       │                  │      isories/GHSA-qq4x-vfq4-9h9g 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │       ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │       ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [11]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │       ├ PkgID           : libblkid1@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : libblkid1 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libblkid1@2.41-4ubuntu4.2?arch=amd64&
│                       │       │                  │       distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ddaca4141760dfcf 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:61b073fa3ce207b80b95a9c7dec38995057b601cff778ef26d56
│                       │       │                   fccf3beb4626 
│                       │       ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │       │                   improper hostname canonicalization 
│                       │       ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │       │                   canonicalization in the `login(1)` utility, when invoked
│                       │       │                   with the `-h` option, can modify the supplied remote
│                       │       │                   hostname before setting `PAM_RHOST`. A remote attacker
│                       │       │                   could exploit this by providing a specially crafted
│                       │       │                   hostname, potentially bypassing host-based Pluggable
│                       │       │                   Authentication Modules (PAM) access control rules that rely
│                       │       │                    on fully qualified domain names. This could lead to
│                       │       │                   unauthorized access. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-289 
│                       │       ├ VendorSeverity   ╭ azure : 1 
│                       │       │                  ├ nvd   : 2 
│                       │       │                  ├ redhat: 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                  │        │           L/A:N 
│                       │       │                  │        ╰ V3Score : 5.3 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 3.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │       │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │       ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │       ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [12]  ╭ VulnerabilityID : CVE-2026-4046 
│                       │       ├ PkgID           : libc-bin@2.42-0ubuntu3.1 
│                       │       ├ PkgName         : libc-bin 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.42-0ubuntu3.1?arch=amd64&d
│                       │       │                  │       istro=ubuntu-25.10 
│                       │       │                  ╰ UID : 32f722fad25bcb3d 
│                       │       ├ InstalledVersion: 2.42-0ubuntu3.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4046 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:8fa6c12af86d5be459d78f3969e6ef9fd54fc301321cc274853c
│                       │       │                   7399eab9e066 
│                       │       ├ Title           : glibc: glibc: Denial of Service via iconv() function with
│                       │       │                   specific character sets 
│                       │       ├ Description     : The iconv() function in the GNU C Library versions 2.43 and
│                       │       │                    earlier may crash due to an assertion failure when
│                       │       │                   converting inputs from the IBM1390 or IBM1399 character
│                       │       │                   sets, which may be used to remotely crash an application.
│                       │       │                   
│                       │       │                   This vulnerability can be trivially mitigated by removing
│                       │       │                   the IBM1390 and IBM1399 character sets from systems that do
│                       │       │                    not need them. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-617 
│                       │       ├ VendorSeverity   ╭ amazon: 3 
│                       │       │                  ├ azure : 3 
│                       │       │                  ├ photon: 3 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           N/A:L 
│                       │       │                           ╰ V3Score : 5.3 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-4046 
│                       │       │                  ├ [1]: https://inbox.sourceware.org/libc-announce/76814edf-c
│                       │       │                  │      f7f-47ec-979d-2dce0a2c76bf@gotplt.org/T/#u 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-4046 
│                       │       │                  ├ [3]: https://packages.fedoraproject.org/pkgs/glibc/glibc-g
│                       │       │                  │      conv-extra/ 
│                       │       │                  ├ [4]: https://sourceware.org/bugzilla/show_bug.cgi?id=33980 
│                       │       │                  ├ [5]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │       │                  │      f=advisories/GLIBC-SA-2026-0007 
│                       │       │                  ├ [6]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │       │                  │      f=advisories/GLIBC-SA-2026-0007;hb=HEAD 
│                       │       │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-4046 
│                       │       ├ PublishedDate   : 2026-03-30T18:16:19.573Z 
│                       │       ╰ LastModifiedDate: 2026-04-20T22:16:23.623Z 
│                       ├ [13]  ╭ VulnerabilityID : CVE-2026-4437 
│                       │       ├ PkgID           : libc-bin@2.42-0ubuntu3.1 
│                       │       ├ PkgName         : libc-bin 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.42-0ubuntu3.1?arch=amd64&d
│                       │       │                  │       istro=ubuntu-25.10 
│                       │       │                  ╰ UID : 32f722fad25bcb3d 
│                       │       ├ InstalledVersion: 2.42-0ubuntu3.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4437 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:0730d851ed5c54473fd70d48e2f3f9fd47f2411c3a74061e830d
│                       │       │                   edd18ec3634e 
│                       │       ├ Title           : glibc: glibc: Incorrect DNS response parsing via crafted
│                       │       │                   DNS server response 
│                       │       ├ Description     : Calling gethostbyaddr or gethostbyaddr_r with a configured
│                       │       │                   nsswitch.conf that specifies the library's DNS backend in
│                       │       │                   the GNU C Library version 2.34 to version 2.43 could, with
│                       │       │                   a crafted response from the configured DNS server, result
│                       │       │                   in a violation of the DNS specification that causes the
│                       │       │                   application to treat a non-answer section of the DNS
│                       │       │                   response as a valid answer. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-125 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ photon: 3 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           L/A:L 
│                       │       │                           ╰ V3Score : 6.5 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-4437 
│                       │       │                  ├ [1]: https://nvd.nist.gov/vuln/detail/CVE-2026-4437 
│                       │       │                  ├ [2]: https://sourceware.org/bugzilla/show_bug.cgi?id=34014 
│                       │       │                  ├ [3]: https://www.cve.org/CVERecord?id=CVE-2026-4437 
│                       │       │                  ╰ [4]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │       │                         3/2 
│                       │       ├ PublishedDate   : 2026-03-20T20:16:49.477Z 
│                       │       ╰ LastModifiedDate: 2026-04-07T18:41:36.647Z 
│                       ├ [14]  ╭ VulnerabilityID : CVE-2026-4438 
│                       │       ├ PkgID           : libc-bin@2.42-0ubuntu3.1 
│                       │       ├ PkgName         : libc-bin 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.42-0ubuntu3.1?arch=amd64&d
│                       │       │                  │       istro=ubuntu-25.10 
│                       │       │                  ╰ UID : 32f722fad25bcb3d 
│                       │       ├ InstalledVersion: 2.42-0ubuntu3.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4438 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:3fd217f7a7131b15c95274c3bf8e83b6ffa739c97dcf920ae2f6
│                       │       │                   6cdef42dfe2b 
│                       │       ├ Title           : glibc: glibc: Invalid DNS hostname returned via
│                       │       │                   gethostbyaddr functions 
│                       │       ├ Description     : Calling gethostbyaddr or gethostbyaddr_r with a configured
│                       │       │                   nsswitch.conf that specifies the library's DNS backend in
│                       │       │                   the GNU C library version 2.34 to version 2.43 could result
│                       │       │                    in an invalid DNS hostname being returned to the caller in
│                       │       │                    violation of the DNS specification. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-20 
│                       │       │                  ╰ [1]: CWE-88 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ photon: 2 
│                       │       │                  ├ redhat: 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 4 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-4438 
│                       │       │                  ├ [1]: https://nvd.nist.gov/vuln/detail/CVE-2026-4438 
│                       │       │                  ├ [2]: https://sourceware.org/bugzilla/show_bug.cgi?id=34015 
│                       │       │                  ├ [3]: https://www.cve.org/CVERecord?id=CVE-2026-4438 
│                       │       │                  ╰ [4]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │       │                         3/2 
│                       │       ├ PublishedDate   : 2026-03-20T20:16:49.623Z 
│                       │       ╰ LastModifiedDate: 2026-04-07T18:40:02.177Z 
│                       ├ [15]  ╭ VulnerabilityID : CVE-2026-4046 
│                       │       ├ PkgID           : libc6@2.42-0ubuntu3.1 
│                       │       ├ PkgName         : libc6 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.42-0ubuntu3.1?arch=amd64&dist
│                       │       │                  │       ro=ubuntu-25.10 
│                       │       │                  ╰ UID : 67fff5c1ddc17a00 
│                       │       ├ InstalledVersion: 2.42-0ubuntu3.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4046 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:b8e7e2f3590216821796f54a199ed108b1b78a2e551922692d1c
│                       │       │                   e6dc20a5d176 
│                       │       ├ Title           : glibc: glibc: Denial of Service via iconv() function with
│                       │       │                   specific character sets 
│                       │       ├ Description     : The iconv() function in the GNU C Library versions 2.43 and
│                       │       │                    earlier may crash due to an assertion failure when
│                       │       │                   converting inputs from the IBM1390 or IBM1399 character
│                       │       │                   sets, which may be used to remotely crash an application.
│                       │       │                   
│                       │       │                   This vulnerability can be trivially mitigated by removing
│                       │       │                   the IBM1390 and IBM1399 character sets from systems that do
│                       │       │                    not need them. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-617 
│                       │       ├ VendorSeverity   ╭ amazon: 3 
│                       │       │                  ├ azure : 3 
│                       │       │                  ├ photon: 3 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           N/A:L 
│                       │       │                           ╰ V3Score : 5.3 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-4046 
│                       │       │                  ├ [1]: https://inbox.sourceware.org/libc-announce/76814edf-c
│                       │       │                  │      f7f-47ec-979d-2dce0a2c76bf@gotplt.org/T/#u 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-4046 
│                       │       │                  ├ [3]: https://packages.fedoraproject.org/pkgs/glibc/glibc-g
│                       │       │                  │      conv-extra/ 
│                       │       │                  ├ [4]: https://sourceware.org/bugzilla/show_bug.cgi?id=33980 
│                       │       │                  ├ [5]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │       │                  │      f=advisories/GLIBC-SA-2026-0007 
│                       │       │                  ├ [6]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │       │                  │      f=advisories/GLIBC-SA-2026-0007;hb=HEAD 
│                       │       │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-4046 
│                       │       ├ PublishedDate   : 2026-03-30T18:16:19.573Z 
│                       │       ╰ LastModifiedDate: 2026-04-20T22:16:23.623Z 
│                       ├ [16]  ╭ VulnerabilityID : CVE-2026-4437 
│                       │       ├ PkgID           : libc6@2.42-0ubuntu3.1 
│                       │       ├ PkgName         : libc6 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.42-0ubuntu3.1?arch=amd64&dist
│                       │       │                  │       ro=ubuntu-25.10 
│                       │       │                  ╰ UID : 67fff5c1ddc17a00 
│                       │       ├ InstalledVersion: 2.42-0ubuntu3.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4437 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:ee1151334af7a4dfaae3ba3e1073263c449295d4c1f09adac430
│                       │       │                   50e6a090cabb 
│                       │       ├ Title           : glibc: glibc: Incorrect DNS response parsing via crafted
│                       │       │                   DNS server response 
│                       │       ├ Description     : Calling gethostbyaddr or gethostbyaddr_r with a configured
│                       │       │                   nsswitch.conf that specifies the library's DNS backend in
│                       │       │                   the GNU C Library version 2.34 to version 2.43 could, with
│                       │       │                   a crafted response from the configured DNS server, result
│                       │       │                   in a violation of the DNS specification that causes the
│                       │       │                   application to treat a non-answer section of the DNS
│                       │       │                   response as a valid answer. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-125 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ photon: 3 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           L/A:L 
│                       │       │                           ╰ V3Score : 6.5 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-4437 
│                       │       │                  ├ [1]: https://nvd.nist.gov/vuln/detail/CVE-2026-4437 
│                       │       │                  ├ [2]: https://sourceware.org/bugzilla/show_bug.cgi?id=34014 
│                       │       │                  ├ [3]: https://www.cve.org/CVERecord?id=CVE-2026-4437 
│                       │       │                  ╰ [4]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │       │                         3/2 
│                       │       ├ PublishedDate   : 2026-03-20T20:16:49.477Z 
│                       │       ╰ LastModifiedDate: 2026-04-07T18:41:36.647Z 
│                       ├ [17]  ╭ VulnerabilityID : CVE-2026-4438 
│                       │       ├ PkgID           : libc6@2.42-0ubuntu3.1 
│                       │       ├ PkgName         : libc6 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.42-0ubuntu3.1?arch=amd64&dist
│                       │       │                  │       ro=ubuntu-25.10 
│                       │       │                  ╰ UID : 67fff5c1ddc17a00 
│                       │       ├ InstalledVersion: 2.42-0ubuntu3.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4438 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:cb07760bb1e61c6f73f23b4677b2e01c59ae313225b685a9948f
│                       │       │                   0e5bcd2b6175 
│                       │       ├ Title           : glibc: glibc: Invalid DNS hostname returned via
│                       │       │                   gethostbyaddr functions 
│                       │       ├ Description     : Calling gethostbyaddr or gethostbyaddr_r with a configured
│                       │       │                   nsswitch.conf that specifies the library's DNS backend in
│                       │       │                   the GNU C library version 2.34 to version 2.43 could result
│                       │       │                    in an invalid DNS hostname being returned to the caller in
│                       │       │                    violation of the DNS specification. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-20 
│                       │       │                  ╰ [1]: CWE-88 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ photon: 2 
│                       │       │                  ├ redhat: 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 4 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-4438 
│                       │       │                  ├ [1]: https://nvd.nist.gov/vuln/detail/CVE-2026-4438 
│                       │       │                  ├ [2]: https://sourceware.org/bugzilla/show_bug.cgi?id=34015 
│                       │       │                  ├ [3]: https://www.cve.org/CVERecord?id=CVE-2026-4438 
│                       │       │                  ╰ [4]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │       │                         3/2 
│                       │       ├ PublishedDate   : 2026-03-20T20:16:49.623Z 
│                       │       ╰ LastModifiedDate: 2026-04-07T18:40:02.177Z 
│                       ├ [18]  ╭ VulnerabilityID : CVE-2026-5545 
│                       │       ├ PkgID           : libcurl4t64@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : libcurl4t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.14.1-2ubuntu1.2?arch=am
│                       │       │                  │       d64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 7f081f5df30ce970 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5545 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:35e8b30a96591020109f0c5127aae62d1eec71da16df2f70be5a
│                       │       │                   5bec60a169c7 
│                       │       ├ Title           : curl: libcurl: Authentication bypass due to incorrect HTTP
│                       │       │                   Negotiate connection reuse 
│                       │       ├ Description     : libcurl might in some circumstances reuse the wrong
│                       │       │                   connection when asked to
│                       │       │                   do an authenticated HTTP(S) request after a
│                       │       │                   Negotiate-authenticated one, when
│                       │       │                   both use the same host.
│                       │       │                   
│                       │       │                   libcurl features a pool of recent connections so that
│                       │       │                   subsequent requests can
│                       │       │                   reuse an existing connection to avoid overhead.
│                       │       │                   When reusing a connection a range of criteria must be met.
│                       │       │                   Due to a logical
│                       │       │                   error in the code, a request that was issued by an
│                       │       │                   application could
│                       │       │                   wrongfully reuse an existing connection to the same server
│                       │       │                   that was
│                       │       │                   authenticated using different credentials.
│                       │       │                   An application that first uses Negotiate authentication to
│                       │       │                   a server with
│                       │       │                   `user1:password1` and then does another operation to the
│                       │       │                   same server asking
│                       │       │                   for any authentication method but for `user2:password2`
│                       │       │                   (while the previous
│                       │       │                   connection is still alive) - the second request gets
│                       │       │                   confused and wrongly
│                       │       │                   reuses the same connection and sends the new request over
│                       │       │                   that connection
│                       │       │                   thinking it uses a mix of user1's and user2's credentials
│                       │       │                   when it is in fact
│                       │       │                   still using the connection authenticated for user1... 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-613 
│                       │       ├ VendorSeverity   ╭ nvd   : 2 
│                       │       │                  ├ photon: 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:
│                       │       │                  │        │           H/A:N 
│                       │       │                  │        ╰ V3Score : 6.5 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:
│                       │       │                           │           H/A:N 
│                       │       │                           ╰ V3Score : 6.5 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-5545 
│                       │       │                  ├ [1]: https://curl.se/docs/CVE-2026-5545.html 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-5545.json 
│                       │       │                  ├ [3]: https://hackerone.com/reports/3642555 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-5545 
│                       │       │                  ├ [5]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-5545 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:56.19Z 
│                       │       ╰ LastModifiedDate: 2026-05-13T19:31:07.633Z 
│                       ├ [19]  ╭ VulnerabilityID : CVE-2026-6253 
│                       │       ├ PkgID           : libcurl4t64@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : libcurl4t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.14.1-2ubuntu1.2?arch=am
│                       │       │                  │       d64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 7f081f5df30ce970 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6253 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:bd1ba27ffc16d9212beb9df7940c94e8e9718ebf72de35583c12
│                       │       │                   05d4cd040822 
│                       │       ├ Title           : curl: curl: Proxy credential disclosure via redirects to
│                       │       │                   unauthenticated proxies 
│                       │       ├ Description     : curl might erroneously pass on credentials for a first
│                       │       │                   proxy to a second
│                       │       │                   proxy.
│                       │       │                   
│                       │       │                   This can happen when the following conditions are true:
│                       │       │                   1. curl is setup to use specific different proxies for
│                       │       │                   different URL schemes
│                       │       │                   2. the first proxy needs credentials
│                       │       │                   3. the second proxy uses no credentials
│                       │       │                   4. while using the first proxy (using say `http://`), curl
│                       │       │                   is asked to follow
│                       │       │                      a redirect to a URL using another scheme (say
│                       │       │                   `https://`), accessed using a
│                       │       │                      second, different, proxy 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-522 
│                       │       ├ VendorSeverity   ╭ photon: 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 5.3 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/29
│                       │       │                  │      /11 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-6253 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-6253.html 
│                       │       │                  ├ [3]: https://curl.se/docs/CVE-2026-6253.json 
│                       │       │                  ├ [4]: https://hackerone.com/reports/3669637 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-6253 
│                       │       │                  ├ [6]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-6253 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:56.57Z 
│                       │       ╰ LastModifiedDate: 2026-05-14T13:40:53.19Z 
│                       ├ [20]  ╭ VulnerabilityID : CVE-2026-6429 
│                       │       ├ PkgID           : libcurl4t64@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : libcurl4t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.14.1-2ubuntu1.2?arch=am
│                       │       │                  │       d64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 7f081f5df30ce970 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6429 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:163a9fc857de97c8c9298538a414d5ec98a0396c3d72ec20ba39
│                       │       │                   a25b1a297a56 
│                       │       ├ Title           : curl: libcurl: Credential leak via reused proxy connection
│                       │       │                   during HTTP redirects 
│                       │       ├ Description     : When asked to both use a `.netrc` file for credentials and
│                       │       │                   to follow HTTP
│                       │       │                   redirects, libcurl could leak the password used for the
│                       │       │                   first host to the
│                       │       │                   followed-to host under certain circumstances. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ VendorSeverity   ╭ photon: 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 6.5 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-6429 
│                       │       │                  ├ [1]: https://curl.se/docs/CVE-2026-6429.html 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-6429.json 
│                       │       │                  ├ [3]: https://hackerone.com/reports/3677759 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-6429 
│                       │       │                  ├ [5]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-6429 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:56.93Z 
│                       │       ╰ LastModifiedDate: 2026-05-14T14:18:02.24Z 
│                       ├ [21]  ╭ VulnerabilityID : CVE-2026-7168 
│                       │       ├ PkgID           : libcurl4t64@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : libcurl4t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.14.1-2ubuntu1.2?arch=am
│                       │       │                  │       d64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 7f081f5df30ce970 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-7168 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:d9e0c481024fb677d8bf235997439d3a4fc68f7bc5c5fd63d4e6
│                       │       │                   2070aa7c53a4 
│                       │       ├ Title           : curl: libcurl: Information disclosure via incorrect
│                       │       │                   Proxy-Authorization header reuse 
│                       │       ├ Description     : Successfully using libcurl to do a transfer over a specific
│                       │       │                    HTTP proxy
│                       │       │                   (`proxyA`) with **Digest** authentication and then changing
│                       │       │                    the proxy host to
│                       │       │                   a second one (`proxyB`) for a second transfer, reusing the
│                       │       │                   same handle, makes
│                       │       │                   libcurl wrongly pass on the `Proxy-Authorization:` header
│                       │       │                   field meant for
│                       │       │                   `proxyA`, to `proxyB`. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-294 
│                       │       ├ VendorSeverity   ╭ nvd   : 2 
│                       │       │                  ├ photon: 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 5.3 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 5.3 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/29
│                       │       │                  │      /14 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-7168 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-7168.html 
│                       │       │                  ├ [3]: https://curl.se/docs/CVE-2026-7168.json 
│                       │       │                  ├ [4]: https://hackerone.com/reports/3697719 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-7168 
│                       │       │                  ├ [6]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-7168 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:57.2Z 
│                       │       ╰ LastModifiedDate: 2026-05-14T14:12:48.457Z 
│                       ├ [22]  ╭ VulnerabilityID : CVE-2026-4873 
│                       │       ├ PkgID           : libcurl4t64@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : libcurl4t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.14.1-2ubuntu1.2?arch=am
│                       │       │                  │       d64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 7f081f5df30ce970 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4873 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:2154ed7a490e890b8e1713430400888d6d52087cb46915ec3ad9
│                       │       │                   1da6b564ec1e 
│                       │       ├ Title           : curl: curl: Information disclosure due to incorrect TLS
│                       │       │                   connection reuse 
│                       │       ├ Description     : A vulnerability exists where a connection requiring TLS
│                       │       │                   incorrectly reuses an
│                       │       │                   existing unencrypted connection from the same connection
│                       │       │                   pool. If an initial
│                       │       │                   transfer is made in clear-text (via IMAP, SMTP, or POP3), a
│                       │       │                    subsequent request
│                       │       │                   to that same host bypasses the TLS requirement and instead
│                       │       │                   transmit data
│                       │       │                   unencrypted. 
│                       │       ├ Severity        : LOW 
│                       │       ├ CweIDs           ╭ [0]: CWE-295 
│                       │       │                  ╰ [1]: CWE-319 
│                       │       ├ VendorSeverity   ╭ photon: 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 1 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 5.3 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/29/7 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-4873 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-4873.html 
│                       │       │                  ├ [3]: https://curl.se/docs/CVE-2026-4873.json 
│                       │       │                  ├ [4]: https://hackerone.com/reports/3621851 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-4873 
│                       │       │                  ├ [6]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-4873 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:55.893Z 
│                       │       ╰ LastModifiedDate: 2026-05-14T13:45:11.407Z 
│                       ├ [23]  ╭ VulnerabilityID : CVE-2026-5773 
│                       │       ├ PkgID           : libcurl4t64@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : libcurl4t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.14.1-2ubuntu1.2?arch=am
│                       │       │                  │       d64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 7f081f5df30ce970 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5773 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:80fe2a8ed04610081a84a6c39d63f0c1638ec5fe397f12cb4521
│                       │       │                   1433373c3bc7 
│                       │       ├ Title           : curl: libcurl: Wrong file transfer due to incorrect SMB
│                       │       │                   connection reuse 
│                       │       ├ Description     : libcurl might in some circumstances reuse the wrong
│                       │       │                   connection for SMB(S)
│                       │       │                   transfers.
│                       │       │                   
│                       │       │                   libcurl features a pool of recent connections so that
│                       │       │                   subsequent requests can
│                       │       │                   reuse an existing connection to avoid overhead.
│                       │       │                   When reusing a connection a range of criteria must be met.
│                       │       │                   Due to a logical
│                       │       │                   error in the code, a network transfer operation that was
│                       │       │                   requested by an
│                       │       │                   application could wrongfully reuse an existing SMB
│                       │       │                   connection to the same
│                       │       │                   server that was using a different 'share' than the new
│                       │       │                   subsequent transfer
│                       │       │                   should.
│                       │       │                   This could in unlucky situations lead to the download of
│                       │       │                   the wrong file or the
│                       │       │                   upload of a file to the wrong place. When this happens, the
│                       │       │                    same credentials
│                       │       │                   are used and the server name is the same. 
│                       │       ├ Severity        : LOW 
│                       │       ├ CweIDs           ─ [0]: CWE-918 
│                       │       ├ VendorSeverity   ╭ nvd   : 3 
│                       │       │                  ├ photon: 3 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 1 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 7.5 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 6.5 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/29/9 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-5773 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-5773.html 
│                       │       │                  ├ [3]: https://curl.se/docs/CVE-2026-5773.json 
│                       │       │                  ├ [4]: https://hackerone.com/reports/3650689 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-5773 
│                       │       │                  ├ [6]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-5773 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:56.307Z 
│                       │       ╰ LastModifiedDate: 2026-05-13T19:13:14.097Z 
│                       ├ [24]  ╭ VulnerabilityID : CVE-2026-6276 
│                       │       ├ PkgID           : libcurl4t64@8.14.1-2ubuntu1.2 
│                       │       ├ PkgName         : libcurl4t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.14.1-2ubuntu1.2?arch=am
│                       │       │                  │       d64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 7f081f5df30ce970 
│                       │       ├ InstalledVersion: 8.14.1-2ubuntu1.2 
│                       │       ├ FixedVersion    : 8.14.1-2ubuntu1.3 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6276 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:45265707283ac424373f34bd79f19c5b31f6b9b492ea7ff53287
│                       │       │                   3bfb433ef4e4 
│                       │       ├ Title           : curl: libcurl: Information disclosure due to cookie leak
│                       │       │                   when reusing connections with custom Host headers 
│                       │       ├ Description     : Using libcurl, when a custom `Host:` header is first set
│                       │       │                   for an HTTP request
│                       │       │                   and a second request is subsequently done using the same
│                       │       │                   *easy handle* but
│                       │       │                   without the custom `Host:` header set, the second request
│                       │       │                   would use stale
│                       │       │                   information and pass on cookies meant for the first host in
│                       │       │                    the second
│                       │       │                   request. Leak them. 
│                       │       ├ Severity        : LOW 
│                       │       ├ CweIDs           ─ [0]: CWE-319 
│                       │       ├ VendorSeverity   ╭ nvd   : 3 
│                       │       │                  ├ photon: 3 
│                       │       │                  ├ redhat: 1 
│                       │       │                  ╰ ubuntu: 1 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                  │        │           N/A:H 
│                       │       │                  │        ╰ V3Score : 7.5 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 3.7 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/29
│                       │       │                  │      /13 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-6276 
│                       │       │                  ├ [2]: https://curl.se/docs/CVE-2026-6276.html 
│                       │       │                  ├ [3]: https://curl.se/docs/CVE-2026-6276.json 
│                       │       │                  ├ [4]: https://hackerone.com/reports/3671818 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-6276 
│                       │       │                  ├ [6]: https://ubuntu.com/security/notices/USN-8227-1 
│                       │       │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-6276 
│                       │       ├ PublishedDate   : 2026-05-13T13:01:56.8Z 
│                       │       ╰ LastModifiedDate: 2026-05-14T14:21:06.997Z 
│                       ├ [25]  ╭ VulnerabilityID : CVE-2024-2236 
│                       │       ├ PkgID           : libgcrypt20@1.11.0-7build1 
│                       │       ├ PkgName         : libgcrypt20 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgcrypt20@1.11.0-7build1?arch=amd64
│                       │       │                  │       &distro=ubuntu-25.10 
│                       │       │                  ╰ UID : dacd70a6a90042e1 
│                       │       ├ InstalledVersion: 1.11.0-7build1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-2236 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:f669e45f0ca1b8b437cae25ed8a9cbf8b1a1a2ebd7d9559dee4c
│                       │       │                   1c06b59da96f 
│                       │       ├ Title           : libgcrypt: vulnerable to Marvin Attack 
│                       │       ├ Description     : A timing-based side-channel flaw was found in libgcrypt's
│                       │       │                   RSA implementation. This issue may allow a remote attacker
│                       │       │                   to initiate a Bleichenbacher-style attack, which can lead
│                       │       │                   to the decryption of RSA ciphertexts. 
│                       │       ├ Severity        : LOW 
│                       │       ├ CweIDs           ─ [0]: CWE-385 
│                       │       ├ VendorSeverity   ╭ alma       : 2 
│                       │       │                  ├ amazon     : 2 
│                       │       │                  ├ oracle-oval: 2 
│                       │       │                  ├ redhat     : 2 
│                       │       │                  ├ rocky      : 2 
│                       │       │                  ╰ ubuntu     : 1 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 5.9 
│                       │       ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9404 
│                       │       │                  ├ [1] : https://access.redhat.com/errata/RHSA-2025:3530 
│                       │       │                  ├ [2] : https://access.redhat.com/errata/RHSA-2025:3534 
│                       │       │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2024-2236 
│                       │       │                  ├ [4] : https://bugzilla.redhat.com/2245218 
│                       │       │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2245218 
│                       │       │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2268268 
│                       │       │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2
│                       │       │                  │       024-2236 
│                       │       │                  ├ [8] : https://dev.gnupg.org/T7136 
│                       │       │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-9404.html 
│                       │       │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:9404 
│                       │       │                  ├ [11]: https://github.com/tomato42/marvin-toolkit/tree/mast
│                       │       │                  │       er/example/libgcrypt 
│                       │       │                  ├ [12]: https://gitlab.com/redhat-crypto/libgcrypt/libgcrypt
│                       │       │                  │       -mirror/-/merge_requests/17 
│                       │       │                  ├ [13]: https://linux.oracle.com/cve/CVE-2024-2236.html 
│                       │       │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2024-9404.html 
│                       │       │                  ├ [15]: https://lists.gnupg.org/pipermail/gcrypt-devel/2024-
│                       │       │                  │       March/005607.html 
│                       │       │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2024-2236 
│                       │       │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-2236 
│                       │       ├ PublishedDate   : 2024-03-06T22:15:57.977Z 
│                       │       ╰ LastModifiedDate: 2026-04-15T00:35:42.02Z 
│                       ├ [26]  ╭ VulnerabilityID : CVE-2026-33845 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-33845 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:76936a3b592ea0600222a85398e922d10f5759ed8df0a8b519c6
│                       │       │                   50c58a626ac5 
│                       │       ├ Title           : gnutls: GnuTLS: Denial of Service via DTLS zero-length
│                       │       │                   fragment 
│                       │       ├ Description     : A flaw in GnuTLS DTLS handshake parsing allows malformed
│                       │       │                   fragments with zero length and non-zero offset, leading to
│                       │       │                   an integer underflow during reassembly and resulting in an
│                       │       │                   out-of-bounds read. This issue is remotely exploitable and
│                       │       │                   may cause information disclosure or denial of service. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-191 
│                       │       ├ VendorSeverity   ╭ azure : 3 
│                       │       │                  ├ nvd   : 4 
│                       │       │                  ├ photon: 4 
│                       │       │                  ├ redhat: 3 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │       │                  │        │           N/A:H 
│                       │       │                  │        ╰ V3Score : 9.1 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           N/A:H 
│                       │       │                           ╰ V3Score : 7.5 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:13274 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-33845 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2450624 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-33845 
│                       │       │                  ├ [4]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │       │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2026-33845 
│                       │       │                  ╰ [6]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │       │                         26-04-29-3 
│                       │       ├ PublishedDate   : 2026-04-30T18:16:28.003Z 
│                       │       ╰ LastModifiedDate: 2026-05-05T03:03:19.247Z 
│                       ├ [27]  ╭ VulnerabilityID : CVE-2026-33846 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-33846 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:d12f57df22069ee2c62f6273f8c9ece214ffdb1a2ebc902f659c
│                       │       │                   8f26e4a2cf72 
│                       │       ├ Title           : gnutls: GnuTLS: Denial of Service via heap buffer overflow
│                       │       │                   in DTLS handshake fragment reassembly 
│                       │       ├ Description     : A heap buffer overflow vulnerability exists in the DTLS
│                       │       │                   handshake fragment reassembly logic of GnuTLS. The issue
│                       │       │                   arises in merge_handshake_packet() where incoming handshake
│                       │       │                    fragments are matched and merged based solely on handshake
│                       │       │                    type, without validating that the message_length field
│                       │       │                   remains consistent across all fragments of the same logical
│                       │       │                    message. An attacker can exploit this by sending crafted
│                       │       │                   DTLS fragments with conflicting message_length values,
│                       │       │                   causing the implementation to allocate a buffer based on a
│                       │       │                   smaller initial fragment and subsequently write beyond its
│                       │       │                   bounds using larger, inconsistent fragments. Because the
│                       │       │                   merge operation does not enforce proper bounds checking
│                       │       │                   against the allocated buffer size, this results in an
│                       │       │                   out-of-bounds write on the heap. The vulnerability is
│                       │       │                   remotely exploitable without authentication via the DTLS
│                       │       │                   handshake path and can lead to application crashes or
│                       │       │                   potential memory corruption. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-130 
│                       │       ├ VendorSeverity   ╭ redhat: 3 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           N/A:H 
│                       │       │                           ╰ V3Score : 7.5 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:13274 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-33846 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2450625 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-33846 
│                       │       │                  ├ [4]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │       │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2026-33846 
│                       │       │                  ╰ [6]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │       │                         26-04-29-1 
│                       │       ├ PublishedDate   : 2026-05-04T10:15:59.69Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T15:22:52.85Z 
│                       ├ [28]  ╭ VulnerabilityID : CVE-2026-3832 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3832 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:3eaa8ee6d6e47428d495b9fe4ffc3fa01ab92e968222a199e3ca
│                       │       │                   8a876580ab43 
│                       │       ├ Title           : gnutls: gnutls: Security bypass allows acceptance of
│                       │       │                   revoked server certificates via crafted OCSP response 
│                       │       ├ Description     : A flaw was found in gnutls. A remote attacker could exploit
│                       │       │                    this vulnerability by presenting a specially crafted
│                       │       │                   Online Certificate Status Protocol (OCSP) response during a
│                       │       │                    TLS handshake. Due to a logic error in how gnutls
│                       │       │                   processes multi-record OCSP responses, a client with OCSP
│                       │       │                   verification enabled may incorrectly accept a revoked
│                       │       │                   server certificate, potentially leading to a compromise of
│                       │       │                   trust. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-179 
│                       │       ├ VendorSeverity   ╭ redhat: 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 3.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:13274 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3832 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2445762 
│                       │       │                  ├ [3]: https://gitlab.com/gnutls/gnutls/-/issues/1801 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-3832 
│                       │       │                  ├ [5]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │       │                  ├ [6]: https://www.cve.org/CVERecord?id=CVE-2026-3832 
│                       │       │                  ╰ [7]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │       │                         26-04-29-12 
│                       │       ├ PublishedDate   : 2026-04-30T18:16:30.433Z 
│                       │       ╰ LastModifiedDate: 2026-05-11T19:15:57.277Z 
│                       ├ [29]  ╭ VulnerabilityID : CVE-2026-3833 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3833 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:c35f264071bd8474f46f2ea2f7e853230373982ae8748d440c63
│                       │       │                   ffd89e74d0f4 
│                       │       ├ Title           : gnutls: GnuTLS: Policy bypass due to case-sensitive
│                       │       │                   nameConstraints comparison 
│                       │       ├ Description     : A flaw was found in gnutls. This vulnerability occurs
│                       │       │                   because gnutls performs case-sensitive comparisons of
│                       │       │                   `nameConstraints` labels, specifically for `dNSName` (DNS)
│                       │       │                   or `rfc822Name` (email) constraints within
│                       │       │                   `excludedSubtrees` or `permittedSubtrees`. A remote
│                       │       │                   attacker can exploit this by crafting a leaf certificate
│                       │       │                   with casing differences in the Subject Alternative Name
│                       │       │                   (SAN), leading to a policy bypass where a certificate that
│                       │       │                   should be rejected is instead accepted. This could result
│                       │       │                   in unauthorized access or information disclosure. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-178 
│                       │       ├ VendorSeverity   ╭ nvd   : 3 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:
│                       │       │                  │        │           H/A:N 
│                       │       │                  │        ╰ V3Score : 7.4 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 6.5 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:13274 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3833 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2445763 
│                       │       │                  ├ [3]: https://gitlab.com/gnutls/gnutls/-/issues/1803 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-3833 
│                       │       │                  ├ [5]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │       │                  ├ [6]: https://www.cve.org/CVERecord?id=CVE-2026-3833 
│                       │       │                  ╰ [7]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │       │                         26-04-29-5 
│                       │       ├ PublishedDate   : 2026-04-30T18:16:30.577Z 
│                       │       ╰ LastModifiedDate: 2026-05-07T02:09:04.47Z 
│                       ├ [30]  ╭ VulnerabilityID : CVE-2026-42009 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42009 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:928fa710cc0b82853e22c6466211fdb8b5abd66f0fbfe3ba74d8
│                       │       │                   c9e2eda8da4f 
│                       │       ├ Title           : gnutls: gnutls: Denial of Service via DTLS packet
│                       │       │                   reordering vulnerability 
│                       │       ├ Description     : A flaw was found in gnutls. A remote attacker could exploit
│                       │       │                    an issue in the Datagram Transport Layer Security (DTLS)
│                       │       │                   packet reordering logic. The comparator function,
│                       │       │                   responsible for ordering DTLS packets by sequence numbers,
│                       │       │                   did not correctly handle packets with duplicate sequence
│                       │       │                   numbers. This could lead to unstable packet ordering or
│                       │       │                   undefined behavior, resulting in a denial of service. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-475 
│                       │       ├ VendorSeverity   ╭ redhat: 3 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           N/A:H 
│                       │       │                           ╰ V3Score : 7.5 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-42009 
│                       │       │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2467279 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-42009 
│                       │       │                  ├ [3]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │       │                  ├ [4]: https://www.cve.org/CVERecord?id=CVE-2026-42009 
│                       │       │                  ╰ [5]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │       │                         26-04-29-2 
│                       │       ├ PublishedDate   : 2026-05-18T13:16:32.707Z 
│                       │       ╰ LastModifiedDate: 2026-05-18T19:32:38.777Z 
│                       ├ [31]  ╭ VulnerabilityID : CVE-2026-42010 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42010 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:25934617a7def0cc33189767dbc0292964076d37ffeafc773f60
│                       │       │                   1b1d6d5df00a 
│                       │       ├ Title           : gnutls: gnutls: Authentication Bypass via NUL Character in
│                       │       │                   Username 
│                       │       ├ Description     : A flaw was found in gnutls. Servers configured with RSA-PSK
│                       │       │                    (Rivest–Shamir–Adleman – Pre-Shared Key) wrongfully
│                       │       │                   matched usernames containing a NUL character with truncated
│                       │       │                    usernames. A remote attacker could exploit this by sending
│                       │       │                    a specially crafted username, leading to an authentication
│                       │       │                    bypass. This vulnerability allows an attacker to gain
│                       │       │                   unauthorized access by circumventing the authentication
│                       │       │                   process. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-626 
│                       │       ├ VendorSeverity   ╭ nvd   : 4 
│                       │       │                  ├ photon: 4 
│                       │       │                  ├ redhat: 3 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:
│                       │       │                  │        │           H/A:H 
│                       │       │                  │        ╰ V3Score : 9.8 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 7.1 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:13274 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-42010 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2467289 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-42010 
│                       │       │                  ├ [4]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │       │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2026-42010 
│                       │       │                  ╰ [6]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │       │                         26-04-29-4 
│                       │       ├ PublishedDate   : 2026-05-07T12:16:17.977Z 
│                       │       ╰ LastModifiedDate: 2026-05-14T23:16:36.52Z 
│                       ├ [32]  ╭ VulnerabilityID : CVE-2026-42011 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42011 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:4fc69ff2ea709d60fb0aaa47a524bd17744fd82bb34a50f5d9b6
│                       │       │                   2f17f7962171 
│                       │       ├ Title           : gnutls: gnutls: Security bypass due to incorrect name
│                       │       │                   constraint handling 
│                       │       ├ Description     : A flaw was found in gnutls. This vulnerability occurs
│                       │       │                   because permitted name constraints were incorrectly ignored
│                       │       │                    when previous Certificate Authorities (CAs) only had
│                       │       │                   excluded name constraints. A remote attacker could exploit
│                       │       │                   this to bypass critical name constraint checks during
│                       │       │                   certificate validation. This bypass could lead to the
│                       │       │                   acceptance of invalid certificates, potentially enabling
│                       │       │                   spoofing or man-in-the-middle attacks against affected
│                       │       │                   systems. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-295 
│                       │       ├ VendorSeverity   ╭ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:
│                       │       │                           │           H/A:N 
│                       │       │                           ╰ V3Score : 7.4 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:13274 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-42011 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2467437 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-42011 
│                       │       │                  ├ [4]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │       │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2026-42011 
│                       │       │                  ╰ [6]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │       │                         26-04-29-6 
│                       │       ├ PublishedDate   : 2026-05-07T15:16:09.76Z 
│                       │       ╰ LastModifiedDate: 2026-05-14T23:16:36.667Z 
│                       ├ [33]  ╭ VulnerabilityID : CVE-2026-42012 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42012 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:ecd7e682f47768da3b982e39ca694a67cc1520c855a3c7997d6c
│                       │       │                   68da4e4340d5 
│                       │       ├ Description     : Certificates containing URI or SRV Subject Alternative
│                       │       │                   Names would fall back to checking DNS hostnames against
│                       │       │                   Common Name, allowing potential misuse of such certificates
│                       │       │                    beyond their original purpose. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ VendorSeverity   ─ ubuntu: 2 
│                       │       ╰ References       ╭ [0]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │                          ├ [1]: https://www.cve.org/CVERecord?id=CVE-2026-42012 
│                       │                          ╰ [2]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │                                 26-04-29-7 
│                       ├ [34]  ╭ VulnerabilityID : CVE-2026-42013 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42013 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:ce277070799382be74684266cc1fd2d5177176daf70c14b09410
│                       │       │                   854bf378a862 
│                       │       ├ Description     : Validation of certificates with oversized Subject
│                       │       │                   Alternative Names would fall back to checking DNS hostnames
│                       │       │                    against Common Name. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ VendorSeverity   ─ ubuntu: 2 
│                       │       ╰ References       ╭ [0]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │                          ├ [1]: https://www.cve.org/CVERecord?id=CVE-2026-42013 
│                       │                          ╰ [2]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │                                 26-04-29-8 
│                       ├ [35]  ╭ VulnerabilityID : CVE-2026-42014 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42014 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:73bd4585135b12e1f14412ebcdd8b13289950af5f481db96120e
│                       │       │                   7a8a4d0dc5bd 
│                       │       ├ Description     : Changing the Security Officer PIN with
│                       │       │                   gnutls_pkcs11_token_set_pin() with oldpin == NULL for a
│                       │       │                   token lacking a protected authentication path led to a
│                       │       │                   use-after-free. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ VendorSeverity   ─ ubuntu: 2 
│                       │       ╰ References       ╭ [0]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │                          ├ [1]: https://www.cve.org/CVERecord?id=CVE-2026-42014 
│                       │                          ╰ [2]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │                                 26-04-29-9 
│                       ├ [36]  ╭ VulnerabilityID : CVE-2026-42015 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42015 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:5572013d7d0e694a286f11c414d0b54528948ae2cd178146c2af
│                       │       │                   1258b5b896f4 
│                       │       ├ Description     : Appending to a PKCS#12 bag that already contained 32
│                       │       │                   elements could write past the bag's internal array. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ VendorSeverity   ─ ubuntu: 2 
│                       │       ╰ References       ╭ [0]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │                          ├ [1]: https://www.cve.org/CVERecord?id=CVE-2026-42015 
│                       │                          ╰ [2]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │                                 26-04-29-11 
│                       ├ [37]  ╭ VulnerabilityID : CVE-2026-5260 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5260 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:60f2da284236cd2b5c2b446a49b21e50d79180f287e97a34e8ef
│                       │       │                   4f4f763f4dc8 
│                       │       ├ Description     : For a server using an RSA key backed by a PKCS#11 token, a
│                       │       │                   client sending an extremely short premaster secret during
│                       │       │                   an RSA key exchange could trigger a short heap overread. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ VendorSeverity   ─ ubuntu: 2 
│                       │       ╰ References       ╭ [0]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │                          ├ [1]: https://www.cve.org/CVERecord?id=CVE-2026-5260 
│                       │                          ╰ [2]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │                                 26-04-29-10 
│                       ├ [38]  ╭ VulnerabilityID : CVE-2026-5419 
│                       │       ├ PkgID           : libgnutls30t64@3.8.9-3ubuntu2.1 
│                       │       ├ PkgName         : libgnutls30t64 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-3ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 13fce675b9880961 
│                       │       ├ InstalledVersion: 3.8.9-3ubuntu2.1 
│                       │       ├ FixedVersion    : 3.8.9-3ubuntu2.2 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5419 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:56e4cdfc880c17544a381170a48a425739022093b712489f1307
│                       │       │                   df51568eb1d2 
│                       │       ├ Description     : The PKCS#7 padding check performed during decryption was
│                       │       │                   not constant-time, potentially leaking information about
│                       │       │                   the padding bytes through timing differences. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ VendorSeverity   ─ ubuntu: 2 
│                       │       ╰ References       ╭ [0]: https://ubuntu.com/security/notices/USN-8284-1 
│                       │                          ├ [1]: https://www.cve.org/CVERecord?id=CVE-2026-5419 
│                       │                          ╰ [2]: https://www.gnutls.org/security-new.html#GNUTLS-SA-20
│                       │                                 26-04-29-13 
│                       ├ [39]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │       ├ PkgID           : liblastlog2-2@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : liblastlog2-2 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/liblastlog2-2@2.41-4ubuntu4.2?arch=am
│                       │       │                  │       d64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 6aa63af50fb78d18 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:74c47b7c3869830e0a6bbc4999214a80f4abaf430809d1b5d55e
│                       │       │                   a4aa3622cd7f 
│                       │       ├ Title           : util-linux: TOCTOU in the mount program when setting up
│                       │       │                   loop devices 
│                       │       ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │       │                    to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │       │                   vulnerability has been identified in the SUID binary
│                       │       │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │       │                   setting up loop devices, validates the source file path
│                       │       │                   with user privileges via fork() + setuid() + realpath(),
│                       │       │                   but subsequently re-canonicalizes and opens it with root
│                       │       │                   privileges (euid=0) without verifying that the path has not
│                       │       │                    been replaced between both operations. Neither O_NOFOLLOW,
│                       │       │                    nor inode comparison, nor post-open fstat() are employed.
│                       │       │                   This allows a local unprivileged user to replace the source
│                       │       │                    file with a symlink pointing to any root-owned file or
│                       │       │                   device during the race window, causing the SUID binary to
│                       │       │                   open and mount it as root. Exploitation requires an
│                       │       │                   /etc/fstab entry with user,loop options whose path points
│                       │       │                   to a directory where the attacker has write permission, and
│                       │       │                    that /usr/bin/mount has the SUID bit set (the default
│                       │       │                   configuration on virtually all Linux distributions). The
│                       │       │                   impact is unauthorized read access to root-protected files
│                       │       │                   and block devices, including backup images, disk volumes,
│                       │       │                   and any file containing a valid filesystem. This issue has
│                       │       │                   been patched in version 2.41.4. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-59 
│                       │       │                  ├ [1]: CWE-269 
│                       │       │                  ╰ [2]: CWE-367 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ julia : 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 4.7 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 4.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │       │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e390
│                       │       │                  │      467b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │       │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag
│                       │       │                  │      /v2.41.4 
│                       │       │                  ├ [3]: https://github.com/util-linux/util-linux/security/adv
│                       │       │                  │      isories/GHSA-qq4x-vfq4-9h9g 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │       ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │       ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [40]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │       ├ PkgID           : liblastlog2-2@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : liblastlog2-2 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/liblastlog2-2@2.41-4ubuntu4.2?arch=am
│                       │       │                  │       d64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 6aa63af50fb78d18 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:2072fefc309e7787315de57d5d4d70b9dd1adad94f5a2dde3b3a
│                       │       │                   ebc24f828d68 
│                       │       ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │       │                   improper hostname canonicalization 
│                       │       ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │       │                   canonicalization in the `login(1)` utility, when invoked
│                       │       │                   with the `-h` option, can modify the supplied remote
│                       │       │                   hostname before setting `PAM_RHOST`. A remote attacker
│                       │       │                   could exploit this by providing a specially crafted
│                       │       │                   hostname, potentially bypassing host-based Pluggable
│                       │       │                   Authentication Modules (PAM) access control rules that rely
│                       │       │                    on fully qualified domain names. This could lead to
│                       │       │                   unauthorized access. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-289 
│                       │       ├ VendorSeverity   ╭ azure : 1 
│                       │       │                  ├ nvd   : 2 
│                       │       │                  ├ redhat: 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                  │        │           L/A:N 
│                       │       │                  │        ╰ V3Score : 5.3 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 3.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │       │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │       ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │       ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [41]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │       ├ PkgID           : libmount1@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : libmount1 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libmount1@2.41-4ubuntu4.2?arch=amd64&
│                       │       │                  │       distro=ubuntu-25.10 
│                       │       │                  ╰ UID : e278fd35c2ddbe27 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:02c3f1520f1e1ceca92c128f5c51072cd031390a93c9362fbada
│                       │       │                   296d4d802114 
│                       │       ├ Title           : util-linux: TOCTOU in the mount program when setting up
│                       │       │                   loop devices 
│                       │       ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │       │                    to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │       │                   vulnerability has been identified in the SUID binary
│                       │       │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │       │                   setting up loop devices, validates the source file path
│                       │       │                   with user privileges via fork() + setuid() + realpath(),
│                       │       │                   but subsequently re-canonicalizes and opens it with root
│                       │       │                   privileges (euid=0) without verifying that the path has not
│                       │       │                    been replaced between both operations. Neither O_NOFOLLOW,
│                       │       │                    nor inode comparison, nor post-open fstat() are employed.
│                       │       │                   This allows a local unprivileged user to replace the source
│                       │       │                    file with a symlink pointing to any root-owned file or
│                       │       │                   device during the race window, causing the SUID binary to
│                       │       │                   open and mount it as root. Exploitation requires an
│                       │       │                   /etc/fstab entry with user,loop options whose path points
│                       │       │                   to a directory where the attacker has write permission, and
│                       │       │                    that /usr/bin/mount has the SUID bit set (the default
│                       │       │                   configuration on virtually all Linux distributions). The
│                       │       │                   impact is unauthorized read access to root-protected files
│                       │       │                   and block devices, including backup images, disk volumes,
│                       │       │                   and any file containing a valid filesystem. This issue has
│                       │       │                   been patched in version 2.41.4. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-59 
│                       │       │                  ├ [1]: CWE-269 
│                       │       │                  ╰ [2]: CWE-367 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ julia : 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 4.7 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 4.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │       │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e390
│                       │       │                  │      467b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │       │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag
│                       │       │                  │      /v2.41.4 
│                       │       │                  ├ [3]: https://github.com/util-linux/util-linux/security/adv
│                       │       │                  │      isories/GHSA-qq4x-vfq4-9h9g 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │       ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │       ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [42]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │       ├ PkgID           : libmount1@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : libmount1 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libmount1@2.41-4ubuntu4.2?arch=amd64&
│                       │       │                  │       distro=ubuntu-25.10 
│                       │       │                  ╰ UID : e278fd35c2ddbe27 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:a6129a9b98383b510cd5e341fe16a304cf8494c50d12d1e8a2f3
│                       │       │                   011244603e80 
│                       │       ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │       │                   improper hostname canonicalization 
│                       │       ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │       │                   canonicalization in the `login(1)` utility, when invoked
│                       │       │                   with the `-h` option, can modify the supplied remote
│                       │       │                   hostname before setting `PAM_RHOST`. A remote attacker
│                       │       │                   could exploit this by providing a specially crafted
│                       │       │                   hostname, potentially bypassing host-based Pluggable
│                       │       │                   Authentication Modules (PAM) access control rules that rely
│                       │       │                    on fully qualified domain names. This could lead to
│                       │       │                   unauthorized access. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-289 
│                       │       ├ VendorSeverity   ╭ azure : 1 
│                       │       │                  ├ nvd   : 2 
│                       │       │                  ├ redhat: 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                  │        │           L/A:N 
│                       │       │                  │        ╰ V3Score : 5.3 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 3.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │       │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │       ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │       ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [43]  ╭ VulnerabilityID : CVE-2026-27135 
│                       │       ├ PkgID           : libnghttp2-14@1.64.0-1.1ubuntu1 
│                       │       ├ PkgName         : libnghttp2-14 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libnghttp2-14@1.64.0-1.1ubuntu1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 3a556f16d7c485b0 
│                       │       ├ InstalledVersion: 1.64.0-1.1ubuntu1 
│                       │       ├ FixedVersion    : 1.64.0-1.1ubuntu1.1 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27135 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:8f05830c3a5418bdb591518eb8e368880a99e81256d1db5dd0c6
│                       │       │                   3fa199a0623f 
│                       │       ├ Title           : nghttp2: nghttp2: Denial of Service via malformed HTTP/2
│                       │       │                   frames after session termination 
│                       │       ├ Description     : nghttp2 is an implementation of the Hypertext Transfer
│                       │       │                   Protocol version 2 in C. Prior to version 1.68.1, the
│                       │       │                   nghttp2 library stops reading the incoming data when user
│                       │       │                   facing public API `nghttp2_session_terminate_session` or
│                       │       │                   `nghttp2_session_terminate_session2` is called by the
│                       │       │                   application. They might be called internally by the library
│                       │       │                    when it detects the situation that is subject to
│                       │       │                   connection error. Due to the missing internal state
│                       │       │                   validation, the library keeps reading the rest of the data
│                       │       │                   after one of those APIs is called. Then receiving a
│                       │       │                   malformed frame that causes FRAME_SIZE_ERROR causes
│                       │       │                   assertion failure. nghttp2 v1.68.1 adds missing state
│                       │       │                   validation to avoid assertion failure. No known workarounds
│                       │       │                    are available. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-617 
│                       │       ├ VendorSeverity   ╭ alma       : 3 
│                       │       │                  ├ amazon     : 3 
│                       │       │                  ├ azure      : 3 
│                       │       │                  ├ cbl-mariner: 3 
│                       │       │                  ├ oracle-oval: 3 
│                       │       │                  ├ photon     : 3 
│                       │       │                  ├ redhat     : 3 
│                       │       │                  ├ rocky      : 3 
│                       │       │                  ╰ ubuntu     : 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           N/A:H 
│                       │       │                           ╰ V3Score : 7.5 
│                       │       ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2026/03/2
│                       │       │                  │       0/3 
│                       │       │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:7896 
│                       │       │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2026-27135 
│                       │       │                  ├ [3] : https://bugzilla.redhat.com/2441268 
│                       │       │                  ├ [4] : https://bugzilla.redhat.com/2442922 
│                       │       │                  ├ [5] : https://bugzilla.redhat.com/2448754 
│                       │       │                  ├ [6] : https://bugzilla.redhat.com/2453151 
│                       │       │                  ├ [7] : https://bugzilla.redhat.com/show_bug.cgi?id=2448754 
│                       │       │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2
│                       │       │                  │       026-27135 
│                       │       │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2026-7896.html 
│                       │       │                  ├ [10]: https://errata.rockylinux.org/RLSA-2026:7667 
│                       │       │                  ├ [11]: https://github.com/nghttp2/nghttp2/commit/5c7df8fa81
│                       │       │                  │       5ac1004d9ecb9d1f7595c4d37f46e1 
│                       │       │                  ├ [12]: https://github.com/nghttp2/nghttp2/security/advisori
│                       │       │                  │       es/GHSA-6933-cjhr-5qg6 
│                       │       │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-27135.html 
│                       │       │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-8339.html 
│                       │       │                  ├ [15]: https://lists.debian.org/debian-lts-announce/2026/05
│                       │       │                  │       /msg00025.html 
│                       │       │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2026-27135 
│                       │       │                  ├ [17]: https://ubuntu.com/security/notices/USN-8233-1 
│                       │       │                  ├ [18]: https://ubuntu.com/security/notices/USN-8233-2 
│                       │       │                  ╰ [19]: https://www.cve.org/CVERecord?id=CVE-2026-27135 
│                       │       ├ PublishedDate   : 2026-03-18T18:16:26.723Z 
│                       │       ╰ LastModifiedDate: 2026-05-13T22:16:42.337Z 
│                       ├ [44]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │       ├ PkgID           : libsmartcols1@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : libsmartcols1 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsmartcols1@2.41-4ubuntu4.2?arch=am
│                       │       │                  │       d64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 5caf4ed7c33e8ba9 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:d5414be1cfa74f6127a7fa9e330a0802b64bc55bcd1ef460383f
│                       │       │                   db4631b0ab49 
│                       │       ├ Title           : util-linux: TOCTOU in the mount program when setting up
│                       │       │                   loop devices 
│                       │       ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │       │                    to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │       │                   vulnerability has been identified in the SUID binary
│                       │       │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │       │                   setting up loop devices, validates the source file path
│                       │       │                   with user privileges via fork() + setuid() + realpath(),
│                       │       │                   but subsequently re-canonicalizes and opens it with root
│                       │       │                   privileges (euid=0) without verifying that the path has not
│                       │       │                    been replaced between both operations. Neither O_NOFOLLOW,
│                       │       │                    nor inode comparison, nor post-open fstat() are employed.
│                       │       │                   This allows a local unprivileged user to replace the source
│                       │       │                    file with a symlink pointing to any root-owned file or
│                       │       │                   device during the race window, causing the SUID binary to
│                       │       │                   open and mount it as root. Exploitation requires an
│                       │       │                   /etc/fstab entry with user,loop options whose path points
│                       │       │                   to a directory where the attacker has write permission, and
│                       │       │                    that /usr/bin/mount has the SUID bit set (the default
│                       │       │                   configuration on virtually all Linux distributions). The
│                       │       │                   impact is unauthorized read access to root-protected files
│                       │       │                   and block devices, including backup images, disk volumes,
│                       │       │                   and any file containing a valid filesystem. This issue has
│                       │       │                   been patched in version 2.41.4. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-59 
│                       │       │                  ├ [1]: CWE-269 
│                       │       │                  ╰ [2]: CWE-367 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ julia : 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 4.7 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 4.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │       │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e390
│                       │       │                  │      467b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │       │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag
│                       │       │                  │      /v2.41.4 
│                       │       │                  ├ [3]: https://github.com/util-linux/util-linux/security/adv
│                       │       │                  │      isories/GHSA-qq4x-vfq4-9h9g 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │       ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │       ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [45]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │       ├ PkgID           : libsmartcols1@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : libsmartcols1 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsmartcols1@2.41-4ubuntu4.2?arch=am
│                       │       │                  │       d64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 5caf4ed7c33e8ba9 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:7ec2175d1c50559ffc16373d5781400bddc8d194bb9f3f2b0f65
│                       │       │                   9c76d02a945f 
│                       │       ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │       │                   improper hostname canonicalization 
│                       │       ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │       │                   canonicalization in the `login(1)` utility, when invoked
│                       │       │                   with the `-h` option, can modify the supplied remote
│                       │       │                   hostname before setting `PAM_RHOST`. A remote attacker
│                       │       │                   could exploit this by providing a specially crafted
│                       │       │                   hostname, potentially bypassing host-based Pluggable
│                       │       │                   Authentication Modules (PAM) access control rules that rely
│                       │       │                    on fully qualified domain names. This could lead to
│                       │       │                   unauthorized access. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-289 
│                       │       ├ VendorSeverity   ╭ azure : 1 
│                       │       │                  ├ nvd   : 2 
│                       │       │                  ├ redhat: 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                  │        │           L/A:N 
│                       │       │                  │        ╰ V3Score : 5.3 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 3.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │       │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │       ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │       ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [46]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │       ├ PkgID           : libuuid1@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : libuuid1 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libuuid1@2.41-4ubuntu4.2?arch=amd64&d
│                       │       │                  │       istro=ubuntu-25.10 
│                       │       │                  ╰ UID : 23db7c315eddf1f4 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:02e902ba32ba5e9f8751a5889f50745942d061ac5cf315d50204
│                       │       │                   79533e0d6123 
│                       │       ├ Title           : util-linux: TOCTOU in the mount program when setting up
│                       │       │                   loop devices 
│                       │       ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │       │                    to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │       │                   vulnerability has been identified in the SUID binary
│                       │       │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │       │                   setting up loop devices, validates the source file path
│                       │       │                   with user privileges via fork() + setuid() + realpath(),
│                       │       │                   but subsequently re-canonicalizes and opens it with root
│                       │       │                   privileges (euid=0) without verifying that the path has not
│                       │       │                    been replaced between both operations. Neither O_NOFOLLOW,
│                       │       │                    nor inode comparison, nor post-open fstat() are employed.
│                       │       │                   This allows a local unprivileged user to replace the source
│                       │       │                    file with a symlink pointing to any root-owned file or
│                       │       │                   device during the race window, causing the SUID binary to
│                       │       │                   open and mount it as root. Exploitation requires an
│                       │       │                   /etc/fstab entry with user,loop options whose path points
│                       │       │                   to a directory where the attacker has write permission, and
│                       │       │                    that /usr/bin/mount has the SUID bit set (the default
│                       │       │                   configuration on virtually all Linux distributions). The
│                       │       │                   impact is unauthorized read access to root-protected files
│                       │       │                   and block devices, including backup images, disk volumes,
│                       │       │                   and any file containing a valid filesystem. This issue has
│                       │       │                   been patched in version 2.41.4. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-59 
│                       │       │                  ├ [1]: CWE-269 
│                       │       │                  ╰ [2]: CWE-367 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ julia : 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 4.7 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 4.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │       │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e390
│                       │       │                  │      467b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │       │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag
│                       │       │                  │      /v2.41.4 
│                       │       │                  ├ [3]: https://github.com/util-linux/util-linux/security/adv
│                       │       │                  │      isories/GHSA-qq4x-vfq4-9h9g 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │       ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │       ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [47]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │       ├ PkgID           : libuuid1@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : libuuid1 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libuuid1@2.41-4ubuntu4.2?arch=amd64&d
│                       │       │                  │       istro=ubuntu-25.10 
│                       │       │                  ╰ UID : 23db7c315eddf1f4 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:bea0df3c507b341ebcad4551001f4189cff68fac454107cdcd58
│                       │       │                   7836def29b32 
│                       │       ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │       │                   improper hostname canonicalization 
│                       │       ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │       │                   canonicalization in the `login(1)` utility, when invoked
│                       │       │                   with the `-h` option, can modify the supplied remote
│                       │       │                   hostname before setting `PAM_RHOST`. A remote attacker
│                       │       │                   could exploit this by providing a specially crafted
│                       │       │                   hostname, potentially bypassing host-based Pluggable
│                       │       │                   Authentication Modules (PAM) access control rules that rely
│                       │       │                    on fully qualified domain names. This could lead to
│                       │       │                   unauthorized access. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-289 
│                       │       ├ VendorSeverity   ╭ azure : 1 
│                       │       │                  ├ nvd   : 2 
│                       │       │                  ├ redhat: 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                  │        │           L/A:N 
│                       │       │                  │        ╰ V3Score : 5.3 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 3.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │       │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │       ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │       ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [48]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │       ├ PkgID           : login@1:4.16.0-2+really2.41-4ubuntu4.2 
│                       │       ├ PkgName         : login 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login@4.16.0-2%2Breally2.41-4ubuntu4.
│                       │       │                  │       2?arch=amd64&distro=ubuntu-25.10&epoch=1 
│                       │       │                  ╰ UID : 7a0cd09a7bc5697e 
│                       │       ├ InstalledVersion: 1:4.16.0-2+really2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:c4f89be24d8e469e177cca14be8d573722297aa5f1d4fb3bf5e6
│                       │       │                   893b2ad7947c 
│                       │       ├ Title           : util-linux: TOCTOU in the mount program when setting up
│                       │       │                   loop devices 
│                       │       ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │       │                    to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │       │                   vulnerability has been identified in the SUID binary
│                       │       │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │       │                   setting up loop devices, validates the source file path
│                       │       │                   with user privileges via fork() + setuid() + realpath(),
│                       │       │                   but subsequently re-canonicalizes and opens it with root
│                       │       │                   privileges (euid=0) without verifying that the path has not
│                       │       │                    been replaced between both operations. Neither O_NOFOLLOW,
│                       │       │                    nor inode comparison, nor post-open fstat() are employed.
│                       │       │                   This allows a local unprivileged user to replace the source
│                       │       │                    file with a symlink pointing to any root-owned file or
│                       │       │                   device during the race window, causing the SUID binary to
│                       │       │                   open and mount it as root. Exploitation requires an
│                       │       │                   /etc/fstab entry with user,loop options whose path points
│                       │       │                   to a directory where the attacker has write permission, and
│                       │       │                    that /usr/bin/mount has the SUID bit set (the default
│                       │       │                   configuration on virtually all Linux distributions). The
│                       │       │                   impact is unauthorized read access to root-protected files
│                       │       │                   and block devices, including backup images, disk volumes,
│                       │       │                   and any file containing a valid filesystem. This issue has
│                       │       │                   been patched in version 2.41.4. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-59 
│                       │       │                  ├ [1]: CWE-269 
│                       │       │                  ╰ [2]: CWE-367 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ julia : 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 4.7 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 4.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │       │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e390
│                       │       │                  │      467b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │       │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag
│                       │       │                  │      /v2.41.4 
│                       │       │                  ├ [3]: https://github.com/util-linux/util-linux/security/adv
│                       │       │                  │      isories/GHSA-qq4x-vfq4-9h9g 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │       ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │       ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [49]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │       ├ PkgID           : login@1:4.16.0-2+really2.41-4ubuntu4.2 
│                       │       ├ PkgName         : login 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login@4.16.0-2%2Breally2.41-4ubuntu4.
│                       │       │                  │       2?arch=amd64&distro=ubuntu-25.10&epoch=1 
│                       │       │                  ╰ UID : 7a0cd09a7bc5697e 
│                       │       ├ InstalledVersion: 1:4.16.0-2+really2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:3c6008ba428eae4458d2b80dd9547451de6de309437b39b65298
│                       │       │                   997e20ec7c8b 
│                       │       ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │       │                   improper hostname canonicalization 
│                       │       ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │       │                   canonicalization in the `login(1)` utility, when invoked
│                       │       │                   with the `-h` option, can modify the supplied remote
│                       │       │                   hostname before setting `PAM_RHOST`. A remote attacker
│                       │       │                   could exploit this by providing a specially crafted
│                       │       │                   hostname, potentially bypassing host-based Pluggable
│                       │       │                   Authentication Modules (PAM) access control rules that rely
│                       │       │                    on fully qualified domain names. This could lead to
│                       │       │                   unauthorized access. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-289 
│                       │       ├ VendorSeverity   ╭ azure : 1 
│                       │       │                  ├ nvd   : 2 
│                       │       │                  ├ redhat: 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                  │        │           L/A:N 
│                       │       │                  │        ╰ V3Score : 5.3 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 3.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │       │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │       ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │       ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [50]  ╭ VulnerabilityID : CVE-2024-56433 
│                       │       ├ PkgID           : login.defs@1:4.17.4-2ubuntu2 
│                       │       ├ PkgName         : login.defs 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login.defs@4.17.4-2ubuntu2?arch=all&d
│                       │       │                  │       istro=ubuntu-25.10&epoch=1 
│                       │       │                  ╰ UID : 685157e74dbd875c 
│                       │       ├ InstalledVersion: 1:4.17.4-2ubuntu2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:fd244330f08e39e3bede1ede5ef197df062d61456d8c2f9cd3b3
│                       │       │                   028a5534ef19 
│                       │       ├ Title           : shadow-utils: Default subordinate ID configuration in
│                       │       │                   /etc/login.defs could lead to compromise 
│                       │       ├ Description     : shadow-utils (aka shadow) 4.4 through 4.17.0 establishes a
│                       │       │                   default /etc/subuid behavior (e.g., uid 100000 through
│                       │       │                   165535 for the first user account) that can realistically
│                       │       │                   conflict with the uids of users defined on locally
│                       │       │                   administered networks, potentially leading to account
│                       │       │                   takeover, e.g., by leveraging newuidmap for access to an
│                       │       │                   NFS home directory (or same-host resources in the case of
│                       │       │                   remote logins by these local network users). NOTE: it may
│                       │       │                   also be argued that system administrators should not have
│                       │       │                   assigned uids, within local networks, that are within the
│                       │       │                   range that can occur in /etc/subuid. 
│                       │       ├ Severity        : LOW 
│                       │       ├ CweIDs           ─ [0]: CWE-1188 
│                       │       ├ VendorSeverity   ╭ alma       : 1 
│                       │       │                  ├ azure      : 1 
│                       │       │                  ├ oracle-oval: 1 
│                       │       │                  ├ redhat     : 1 
│                       │       │                  ├ rocky      : 1 
│                       │       │                  ╰ ubuntu     : 1 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 3.6 
│                       │       ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:20559 
│                       │       │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-56433 
│                       │       │                  ├ [2] : https://bugzilla.redhat.com/2334165 
│                       │       │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2334165 
│                       │       │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2
│                       │       │                  │       024-56433 
│                       │       │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2025-20559.html 
│                       │       │                  ├ [6] : https://errata.rockylinux.org/RLSA-2025:20145 
│                       │       │                  ├ [7] : https://github.com/shadow-maint/shadow/blob/e2512d57
│                       │       │                  │       41d4a44bdd81a8c2d0029b6222728cf0/etc/login.defs#L238
│                       │       │                  │       -L241 
│                       │       │                  ├ [8] : https://github.com/shadow-maint/shadow/issues/1157 
│                       │       │                  ├ [9] : https://github.com/shadow-maint/shadow/releases/tag/
│                       │       │                  │       4.4 
│                       │       │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-56433.html 
│                       │       │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2025-20559-0.html 
│                       │       │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-56433 
│                       │       │                  ╰ [13]: https://www.cve.org/CVERecord?id=CVE-2024-56433 
│                       │       ├ PublishedDate   : 2024-12-26T09:15:07.267Z 
│                       │       ╰ LastModifiedDate: 2026-04-15T00:35:42.02Z 
│                       ├ [51]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │       ├ PkgID           : mount@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : mount 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/mount@2.41-4ubuntu4.2?arch=amd64&dist
│                       │       │                  │       ro=ubuntu-25.10 
│                       │       │                  ╰ UID : f2821a9fde7aa805 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:9561b2dcdb55f4520350331d54082aebb117b1010a0b2950d142
│                       │       │                   e257651eba8c 
│                       │       ├ Title           : util-linux: TOCTOU in the mount program when setting up
│                       │       │                   loop devices 
│                       │       ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │       │                    to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │       │                   vulnerability has been identified in the SUID binary
│                       │       │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │       │                   setting up loop devices, validates the source file path
│                       │       │                   with user privileges via fork() + setuid() + realpath(),
│                       │       │                   but subsequently re-canonicalizes and opens it with root
│                       │       │                   privileges (euid=0) without verifying that the path has not
│                       │       │                    been replaced between both operations. Neither O_NOFOLLOW,
│                       │       │                    nor inode comparison, nor post-open fstat() are employed.
│                       │       │                   This allows a local unprivileged user to replace the source
│                       │       │                    file with a symlink pointing to any root-owned file or
│                       │       │                   device during the race window, causing the SUID binary to
│                       │       │                   open and mount it as root. Exploitation requires an
│                       │       │                   /etc/fstab entry with user,loop options whose path points
│                       │       │                   to a directory where the attacker has write permission, and
│                       │       │                    that /usr/bin/mount has the SUID bit set (the default
│                       │       │                   configuration on virtually all Linux distributions). The
│                       │       │                   impact is unauthorized read access to root-protected files
│                       │       │                   and block devices, including backup images, disk volumes,
│                       │       │                   and any file containing a valid filesystem. This issue has
│                       │       │                   been patched in version 2.41.4. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-59 
│                       │       │                  ├ [1]: CWE-269 
│                       │       │                  ╰ [2]: CWE-367 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ julia : 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 4.7 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 4.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │       │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e390
│                       │       │                  │      467b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │       │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag
│                       │       │                  │      /v2.41.4 
│                       │       │                  ├ [3]: https://github.com/util-linux/util-linux/security/adv
│                       │       │                  │      isories/GHSA-qq4x-vfq4-9h9g 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │       ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │       ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [52]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │       ├ PkgID           : mount@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : mount 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/mount@2.41-4ubuntu4.2?arch=amd64&dist
│                       │       │                  │       ro=ubuntu-25.10 
│                       │       │                  ╰ UID : f2821a9fde7aa805 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:aa27241d950ec21f743d167a622eb4a1bf22b9251b49ede40904
│                       │       │                   2bd0f9afb190 
│                       │       ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │       │                   improper hostname canonicalization 
│                       │       ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │       │                   canonicalization in the `login(1)` utility, when invoked
│                       │       │                   with the `-h` option, can modify the supplied remote
│                       │       │                   hostname before setting `PAM_RHOST`. A remote attacker
│                       │       │                   could exploit this by providing a specially crafted
│                       │       │                   hostname, potentially bypassing host-based Pluggable
│                       │       │                   Authentication Modules (PAM) access control rules that rely
│                       │       │                    on fully qualified domain names. This could lead to
│                       │       │                   unauthorized access. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-289 
│                       │       ├ VendorSeverity   ╭ azure : 1 
│                       │       │                  ├ nvd   : 2 
│                       │       │                  ├ redhat: 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │       │                  │        │           L/A:N 
│                       │       │                  │        ╰ V3Score : 5.3 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 3.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │       │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │       │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │       │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │       ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │       ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [53]  ╭ VulnerabilityID : CVE-2024-56433 
│                       │       ├ PkgID           : passwd@1:4.17.4-2ubuntu2 
│                       │       ├ PkgName         : passwd 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/passwd@4.17.4-2ubuntu2?arch=amd64&dis
│                       │       │                  │       tro=ubuntu-25.10&epoch=1 
│                       │       │                  ╰ UID : 2d87ef360f209a3f 
│                       │       ├ InstalledVersion: 1:4.17.4-2ubuntu2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:780778e14725257474609c3782560034c851e14c03f907a322ab
│                       │       │                   956803e69ff6 
│                       │       ├ Title           : shadow-utils: Default subordinate ID configuration in
│                       │       │                   /etc/login.defs could lead to compromise 
│                       │       ├ Description     : shadow-utils (aka shadow) 4.4 through 4.17.0 establishes a
│                       │       │                   default /etc/subuid behavior (e.g., uid 100000 through
│                       │       │                   165535 for the first user account) that can realistically
│                       │       │                   conflict with the uids of users defined on locally
│                       │       │                   administered networks, potentially leading to account
│                       │       │                   takeover, e.g., by leveraging newuidmap for access to an
│                       │       │                   NFS home directory (or same-host resources in the case of
│                       │       │                   remote logins by these local network users). NOTE: it may
│                       │       │                   also be argued that system administrators should not have
│                       │       │                   assigned uids, within local networks, that are within the
│                       │       │                   range that can occur in /etc/subuid. 
│                       │       ├ Severity        : LOW 
│                       │       ├ CweIDs           ─ [0]: CWE-1188 
│                       │       ├ VendorSeverity   ╭ alma       : 1 
│                       │       │                  ├ azure      : 1 
│                       │       │                  ├ oracle-oval: 1 
│                       │       │                  ├ redhat     : 1 
│                       │       │                  ├ rocky      : 1 
│                       │       │                  ╰ ubuntu     : 1 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:
│                       │       │                           │           L/A:N 
│                       │       │                           ╰ V3Score : 3.6 
│                       │       ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:20559 
│                       │       │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-56433 
│                       │       │                  ├ [2] : https://bugzilla.redhat.com/2334165 
│                       │       │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2334165 
│                       │       │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2
│                       │       │                  │       024-56433 
│                       │       │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2025-20559.html 
│                       │       │                  ├ [6] : https://errata.rockylinux.org/RLSA-2025:20145 
│                       │       │                  ├ [7] : https://github.com/shadow-maint/shadow/blob/e2512d57
│                       │       │                  │       41d4a44bdd81a8c2d0029b6222728cf0/etc/login.defs#L238
│                       │       │                  │       -L241 
│                       │       │                  ├ [8] : https://github.com/shadow-maint/shadow/issues/1157 
│                       │       │                  ├ [9] : https://github.com/shadow-maint/shadow/releases/tag/
│                       │       │                  │       4.4 
│                       │       │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-56433.html 
│                       │       │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2025-20559-0.html 
│                       │       │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-56433 
│                       │       │                  ╰ [13]: https://www.cve.org/CVERecord?id=CVE-2024-56433 
│                       │       ├ PublishedDate   : 2024-12-26T09:15:07.267Z 
│                       │       ╰ LastModifiedDate: 2026-04-15T00:35:42.02Z 
│                       ├ [54]  ╭ VulnerabilityID : CVE-2026-35338 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35338 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:69fb0277de26e1eecea9de925386a5cba8694556dc6dfaa90919
│                       │       │                   d3d6a84ad3c9 
│                       │       ├ Title           : A vulnerability in the chmod utility of uutils coreutils
│                       │       │                   allows users  ... 
│                       │       ├ Description     : A vulnerability in the chmod utility of uutils coreutils
│                       │       │                   allows users to bypass the --preserve-root safety
│                       │       │                   mechanism. The implementation only validates if the target
│                       │       │                   path is literally / and does not canonicalize the path. An
│                       │       │                   attacker or accidental user can use path variants such as
│                       │       │                   /../ or symbolic links to execute destructive recursive
│                       │       │                   operations (e.g., chmod -R 000) on the entire root
│                       │       │                   filesystem, leading to system-wide permission loss and
│                       │       │                   potential complete system breakdown. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-22 
│                       │       ├ VendorSeverity   ╭ ghsa  : 3 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 7.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/413055b378
│                       │       │                  │      fa6fe2299c5e5f538c8e6e841ab810 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/10033 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.6.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35338 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35338 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:35.583Z 
│                       │       ╰ LastModifiedDate: 2026-04-27T12:28:50.307Z 
│                       ├ [55]  ╭ VulnerabilityID : CVE-2026-35339 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35339 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:f7fcc421334f21b5d6c6380e83e2a1380a6f03ff621404370082
│                       │       │                   e9fa2e60b011 
│                       │       ├ Title           : The recursive mode (-R) of the chmod utility in uutils
│                       │       │                   coreutils incor ... 
│                       │       ├ Description     : The recursive mode (-R) of the chmod utility in uutils
│                       │       │                   coreutils incorrectly handles exit codes when processing
│                       │       │                   multiple files. The final return value is determined solely
│                       │       │                    by the success or failure of the last file processed. This
│                       │       │                    allows the command to return an exit code of 0 (success)
│                       │       │                   even if errors were encountered on previous files, such as
│                       │       │                   'Operation not permitted'. Scripts relying on these exit
│                       │       │                   codes may proceed under a false sense of success while
│                       │       │                   sensitive files remain with restrictive or incorrect
│                       │       │                   permissions. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-253 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:H/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 5.5 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/abd581f62e
│                       │       │                  │      97d0b147306ac40eac13af71c6fbba 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/9793 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.6.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35339 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35339 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:35.767Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T20:14:43.883Z 
│                       ├ [56]  ╭ VulnerabilityID : CVE-2026-35340 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35340 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:f67802a0e4c8e6a0b522b7e8004f7d0934f9a399b90b43332f3f
│                       │       │                   62dd6882b40f 
│                       │       ├ Title           : A flaw in the ChownExecutor used by uutils coreutils chown
│                       │       │                   and chgrp c ... 
│                       │       ├ Description     : A flaw in the ChownExecutor used by uutils coreutils chown
│                       │       │                   and chgrp causes the utilities to return an incorrect exit
│                       │       │                   code during recursive operations. The final exit code is
│                       │       │                   determined only by the last file processed. If the last
│                       │       │                   operation succeeds, the command returns 0 even if earlier
│                       │       │                   ownership or group changes failed due to permission errors.
│                       │       │                    This can lead to security misconfigurations where
│                       │       │                   administrative scripts incorrectly assume that ownership
│                       │       │                   has been successfully transferred across a directory
│                       │       │                   tree. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-253 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:H/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 5.5 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/ebc08af9c3
│                       │       │                  │      4138f474b32ea0ef34bed3b086a3ed 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/10035 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.6.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35340 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35340 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:35.923Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T20:12:01.5Z 
│                       ├ [57]  ╭ VulnerabilityID : CVE-2026-35341 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35341 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:4bc3a1b5a92056c1aab3bc2e11672f9c9afccc49ac2c095a92ab
│                       │       │                   4d15e5a0e1e4 
│                       │       ├ Title           : A vulnerability in uutils coreutils mkfifo allows for the
│                       │       │                   unauthorized ... 
│                       │       ├ Description     : A vulnerability in uutils coreutils mkfifo allows for the
│                       │       │                   unauthorized modification of permissions on existing files.
│                       │       │                    When mkfifo fails to create a FIFO because a file already
│                       │       │                   exists at the target path, it fails to terminate the
│                       │       │                   operation for that path and continues to execute a
│                       │       │                   follow-up set_permissions call. This results in the
│                       │       │                   existing file's permissions being changed to the default
│                       │       │                   mode (often 644 after umask), potentially exposing
│                       │       │                   sensitive files such as SSH private keys to other users on
│                       │       │                   the system. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-732 
│                       │       ├ VendorSeverity   ╭ ghsa  : 3 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 7.1 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/10020 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35341 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35341 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:36.06Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T19:05:55.067Z 
│                       ├ [58]  ╭ VulnerabilityID : CVE-2026-35342 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35342 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:64be6736f04ff480e9ed93d92275f4b33cf56e7a404ab33e991c
│                       │       │                   a64e772da2ec 
│                       │       ├ Title           : The mktemp utility in uutils coreutils fails to properly
│                       │       │                   handle an emp ... 
│                       │       ├ Description     : The mktemp utility in uutils coreutils fails to properly
│                       │       │                   handle an empty TMPDIR environment variable. Unlike GNU
│                       │       │                   mktemp, which falls back to /tmp when TMPDIR is an empty
│                       │       │                   string, the uutils implementation treats the empty string
│                       │       │                   as a valid path. This causes temporary files to be created
│                       │       │                   in the current working directory (CWD) instead of the
│                       │       │                   intended secure temporary directory. If the CWD is more
│                       │       │                   permissive or accessible to other users than /tmp, it may
│                       │       │                   lead to unintended information disclosure or unauthorized
│                       │       │                   access to temporary data. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-377 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 3.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/eb25ec328b
│                       │       │                  │      226d8fbbaa4058bf9187165bf06d51 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/10566 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.6.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35342 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35342 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:36.217Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T20:11:32.34Z 
│                       ├ [59]  ╭ VulnerabilityID : CVE-2026-35343 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35343 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:c96264682f8605427a0a4896967ee2f184c98f8bd9b2dd954618
│                       │       │                   2fa33d7509a9 
│                       │       ├ Title           : The cut utility in uutils coreutils incorrectly handles the
│                       │       │                    -s (only-d ... 
│                       │       ├ Description     : The cut utility in uutils coreutils incorrectly handles the
│                       │       │                    -s (only-delimited) option when a newline character is
│                       │       │                   specified as the delimiter. The implementation fails to
│                       │       │                   verify the only_delimited flag in the
│                       │       │                   cut_fields_newline_char_delim function, causing the utility
│                       │       │                    to print non-delimited lines that should have been
│                       │       │                   suppressed. This can lead to unexpected data being passed
│                       │       │                   to downstream scripts that rely on strict output
│                       │       │                   filtering. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-670 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 3.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/9bbb58b746
│                       │       │                  │      c41802278b0cba738eebbf21517cf7 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/11143 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.7.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35343 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35343 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:36.357Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T20:10:47.587Z 
│                       ├ [60]  ╭ VulnerabilityID : CVE-2026-35344 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35344 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:3a7d3c161d9d6da82a11789ebaf3b428996c7c01474788e26a8f
│                       │       │                   8ad5e21f94d3 
│                       │       ├ Title           : The dd utility in uutils coreutils suppresses errors during
│                       │       │                    file trunc ... 
│                       │       ├ Description     : The dd utility in uutils coreutils suppresses errors during
│                       │       │                    file truncation operations by unconditionally calling
│                       │       │                   Result::ok() on truncation attempts. While intended to
│                       │       │                   mimic GNU behavior for special files like /dev/null, the
│                       │       │                   uutils implementation also hides failures on regular files
│                       │       │                   and directories caused by full disks or read-only file
│                       │       │                   systems. This can lead to silent data corruption in backup
│                       │       │                   or migration scripts, as the utility may report a
│                       │       │                   successful operation even when the destination file
│                       │       │                   contains old or garbage data. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-252 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 3.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/9745 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35344 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35344 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:36.49Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T20:09:48.593Z 
│                       ├ [61]  ╭ VulnerabilityID : CVE-2026-35345 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35345 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:10c4e34cd3182f711f5a18308b7544cb12572a3f03e34d5669e2
│                       │       │                   6310c7ac6af9 
│                       │       ├ Title           : A vulnerability in the tail utility of uutils coreutils
│                       │       │                   allows for the ... 
│                       │       ├ Description     : A vulnerability in the tail utility of uutils coreutils
│                       │       │                   allows for the exfiltration of sensitive file contents when
│                       │       │                    using the --follow=name option. Unlike GNU tail, the
│                       │       │                   uutils implementation continues to monitor a path after it
│                       │       │                   has been replaced by a symbolic link, subsequently
│                       │       │                   outputting the contents of the link's target. In
│                       │       │                   environments where a privileged user (e.g., root) monitors
│                       │       │                   a log directory, a local attacker with write access to that
│                       │       │                    directory can replace a log file with a symlink to a
│                       │       │                   sensitive system file (such as /etc/shadow), causing tail
│                       │       │                   to disclose the contents of the sensitive file. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-59 
│                       │       │                  ╰ [1]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:L/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 5.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/10328 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35345 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35345 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:36.627Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T20:04:25.093Z 
│                       ├ [62]  ╭ VulnerabilityID : CVE-2026-35346 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35346 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:2f155a5bd4043c2a05902a8b0b7ec47a962084517be169ae7844
│                       │       │                   9fedfad4e7e7 
│                       │       ├ Title           : The comm utility in uutils coreutils silently corrupts data
│                       │       │                    by perform ... 
│                       │       ├ Description     : The comm utility in uutils coreutils silently corrupts data
│                       │       │                    by performing lossy UTF-8 conversion on all output lines.
│                       │       │                   The implementation uses String::from_utf8_lossy(), which
│                       │       │                   replaces invalid UTF-8 byte sequences with the Unicode
│                       │       │                   replacement character (U+FFFD). This behavior differs from
│                       │       │                   GNU comm, which processes raw bytes and preserves the
│                       │       │                   original input. This results in corrupted output when the
│                       │       │                   utility is used to compare binary files or files using
│                       │       │                   non-UTF-8 legacy encodings. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-176 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 3.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/b9372e509e
│                       │       │                  │      a9b278fe13763237067a261bb8c946 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/issues/10192 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/pull/10206 
│                       │       │                  ├ [4]: https://github.com/uutils/coreutils/releases/tag/0.6.0 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-35346 
│                       │       │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-35346 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:36.76Z 
│                       │       ╰ LastModifiedDate: 2026-04-27T12:28:38.493Z 
│                       ├ [63]  ╭ VulnerabilityID : CVE-2026-35347 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35347 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:ba2526d713049c3fdeafc3acfb99dba77e9cdb50c4f5e1786085
│                       │       │                   535334b45700 
│                       │       ├ Title           : The comm utility in uutils coreutils incorrectly consumes
│                       │       │                   data from no ... 
│                       │       ├ Description     : The comm utility in uutils coreutils incorrectly consumes
│                       │       │                   data from non-regular file inputs before performing
│                       │       │                   comparison operations. The are_files_identical function
│                       │       │                   opens and reads from both input paths to compare content
│                       │       │                   without first verifying if the paths refer to regular
│                       │       │                   files. If an input path is a FIFO or a pipe, this pre-read
│                       │       │                   operation drains the stream, leading to silent data loss
│                       │       │                   before the actual comparison logic is executed.
│                       │       │                   Additionally, the utility may hang indefinitely if it
│                       │       │                   attempts to pre-read from infinite streams like
│                       │       │                   /dev/zero. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-20 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/
│                       │       │                         │           A:L 
│                       │       │                         ╰ V3Score : 4.4 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/75f45e87e5
│                       │       │                  │      2ed95840494963ab9a28651165d56e 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/9545 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.6.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35347 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35347 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:36.903Z 
│                       │       ╰ LastModifiedDate: 2026-04-27T12:28:23.273Z 
│                       ├ [64]  ╭ VulnerabilityID : CVE-2026-35348 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35348 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:9f6f48dc9c0063c85f468c1160eb1d10e5fada03924bc76c2844
│                       │       │                   af5d6fdd2b67 
│                       │       ├ Title           : The sort utility in uutils coreutils is vulnerable to a
│                       │       │                   process panic  ... 
│                       │       ├ Description     : The sort utility in uutils coreutils is vulnerable to a
│                       │       │                   process panic when using the --files0-from option with
│                       │       │                   inputs containing non-UTF-8 filenames. The implementation
│                       │       │                   enforces UTF-8 encoding and utilizes expect(), causing an
│                       │       │                   immediate crash when encountering valid but non-UTF-8
│                       │       │                   paths. This diverges from GNU sort, which treats filenames
│                       │       │                   as raw bytes. A local attacker can exploit this to crash
│                       │       │                   the utility and disrupt automated pipelines. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-248 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 5.5 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/9696 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35348 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35348 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:37.04Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T18:57:20.927Z 
│                       ├ [65]  ╭ VulnerabilityID : CVE-2026-35349 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35349 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:ad6db28e5feaf1e1817915bf766582a398e5e36ae4f483382603
│                       │       │                   6d196fff01b7 
│                       │       ├ Title           : A vulnerability in the rm utility of uutils coreutils
│                       │       │                   allows a bypass  ... 
│                       │       ├ Description     : A vulnerability in the rm utility of uutils coreutils
│                       │       │                   allows a bypass of the --preserve-root protection. The
│                       │       │                   implementation uses a path-string check rather than
│                       │       │                   comparing device and inode numbers to identify the root
│                       │       │                   directory. An attacker or accidental user can bypass this
│                       │       │                   safeguard by using a symbolic link that resolves to the
│                       │       │                   root directory (e.g., /tmp/rootlink -> /), potentially
│                       │       │                   leading to the unintended recursive deletion of the entire
│                       │       │                   root filesystem. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-59 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ├ nvd   : 3 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:H/
│                       │       │                  │      │           A:H 
│                       │       │                  │      ╰ V3Score : 6.7 
│                       │       │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:H/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 7.7 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/5e5968cdbc
│                       │       │                  │      6618acd6c2402a8a98b503f278835e 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/9706 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.7.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35349 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35349 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:37.19Z 
│                       │       ╰ LastModifiedDate: 2026-04-27T12:28:17.903Z 
│                       ├ [66]  ╭ VulnerabilityID : CVE-2026-35350 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35350 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:b50925cc660e4025e32255a0a9bd7d6d8addc103cfdece233b69
│                       │       │                   06917cbfddcc 
│                       │       ├ Title           : The cp utility in uutils coreutils fails to properly handle
│                       │       │                    setuid and ... 
│                       │       ├ Description     : The cp utility in uutils coreutils fails to properly handle
│                       │       │                    setuid and setgid bits when ownership preservation fails.
│                       │       │                   When copying with the -p (preserve) flag, the utility
│                       │       │                   applies the source mode bits even if the chown operation is
│                       │       │                    unsuccessful. This can result in a user-owned copy
│                       │       │                   retaining original privileged bits, creating unexpected
│                       │       │                   privileged executables that violate local security
│                       │       │                   policies. This differs from GNU cp, which clears these bits
│                       │       │                    when ownership cannot be preserved. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-281 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:H/
│                       │       │                         │           A:L 
│                       │       │                         ╰ V3Score : 6.6 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/9750 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35350 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35350 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:37.327Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T19:04:01.207Z 
│                       ├ [67]  ╭ VulnerabilityID : CVE-2026-35351 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35351 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:f3d93c00f0616b03346e2b71f80e1731fac85279980c380d21ef
│                       │       │                   a90a036fa281 
│                       │       ├ Title           : The mv utility in uutils coreutils fails to preserve file
│                       │       │                   ownership du ... 
│                       │       ├ Description     : The mv utility in uutils coreutils fails to preserve file
│                       │       │                   ownership during moves across different filesystem
│                       │       │                   boundaries. The utility falls back to a copy-and-delete
│                       │       │                   routine that creates the destination file using the
│                       │       │                   caller's UID/GID rather than the source's metadata. This
│                       │       │                   flaw breaks backups and migrations, causing files moved by
│                       │       │                   a privileged user (e.g., root) to become root-owned
│                       │       │                   unexpectedly, which can lead to information disclosure or
│                       │       │                   restricted access for the intended owners. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-281 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/
│                       │       │                         │           A:L 
│                       │       │                         ╰ V3Score : 4.2 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/9714 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/11706 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-35351 
│                       │       │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-35351 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:37.457Z 
│                       │       ╰ LastModifiedDate: 2026-04-27T12:28:10.22Z 
│                       ├ [68]  ╭ VulnerabilityID : CVE-2026-35352 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35352 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:47f4f303025a813554eadaad0584c0c959c69eaf07a117978db4
│                       │       │                   db266937cd02 
│                       │       ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) race condition
│                       │       │                   exists in the m ... 
│                       │       ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) race condition
│                       │       │                   exists in the mkfifo utility of uutils coreutils. The
│                       │       │                   utility creates a FIFO and then performs a path-based chmod
│                       │       │                    to set permissions. A local attacker with write access to
│                       │       │                   the parent directory can swap the newly created FIFO for a
│                       │       │                   symbolic link between these two operations. This redirects
│                       │       │                   the chmod call to an arbitrary file, potentially enabling
│                       │       │                   privilege escalation if the utility is run with elevated
│                       │       │                   privileges. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 3 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 7 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/05/04/4 
│                       │       │                  ├ [1]: http://www.openwall.com/lists/oss-security/2026/05/04/5 
│                       │       │                  ├ [2]: http://www.openwall.com/lists/oss-security/2026/05/04/6 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [4]: https://github.com/uutils/coreutils/issues/10020 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-35352 
│                       │       │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-35352 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:37.597Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T18:16:28.37Z 
│                       ├ [69]  ╭ VulnerabilityID : CVE-2026-35353 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35353 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:69b822bf11d861ef28df4166490977bbd9aa758c84f115f5408e
│                       │       │                   35bedba719e7 
│                       │       ├ Title           : The mkdir utility in uutils coreutils incorrectly applies
│                       │       │                   permissions  ... 
│                       │       ├ Description     : The mkdir utility in uutils coreutils incorrectly applies
│                       │       │                   permissions when using the -m flag by creating a directory
│                       │       │                   with umask-derived permissions (typically 0755) before
│                       │       │                   subsequently changing them to the requested mode via a
│                       │       │                   separate chmod system call. In multi-user environments,
│                       │       │                   this introduces a brief window where a directory intended
│                       │       │                   to be private is accessible to other users, potentially
│                       │       │                   leading to unauthorized data access. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 3.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/037b9583bc
│                       │       │                  │      03d814e8516df54ebcda6f681fe1f8 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/10036 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.6.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35353 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35353 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:37.723Z 
│                       │       ╰ LastModifiedDate: 2026-04-27T12:27:39.04Z 
│                       ├ [70]  ╭ VulnerabilityID : CVE-2026-35354 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35354 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:b530dce577a25d400c50d0ec9510385ed14b86b8ae4d151016a3
│                       │       │                   cb3c8e2844f0 
│                       │       ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability
│                       │       │                   exists in the mv ... 
│                       │       ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability
│                       │       │                   exists in the mv utility of uutils coreutils during
│                       │       │                   cross-device moves. The extended attribute (xattr)
│                       │       │                   preservation logic uses multiple path-based system calls
│                       │       │                   that perform fresh path-to-inode lookups for each
│                       │       │                   operation. A local attacker with write access to the
│                       │       │                   directory can exploit this race to swap files between
│                       │       │                   calls, causing the destination file to receive an
│                       │       │                   inconsistent mix of security xattrs, such as SELinux labels
│                       │       │                    or file capabilities. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 4.7 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/10014 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35354 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35354 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:37.867Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T19:04:08.917Z 
│                       ├ [71]  ╭ VulnerabilityID : CVE-2026-35355 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35355 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:879d330d329e93edf2dab6efc59ed2517fbdbcb772d5dc0066ca
│                       │       │                   7215b98c0d5e 
│                       │       ├ Title           : The install utility in uutils coreutils is vulnerable to a
│                       │       │                   Time-of-Che ... 
│                       │       ├ Description     : The install utility in uutils coreutils is vulnerable to a
│                       │       │                   Time-of-Check to Time-of-Use (TOCTOU) race condition during
│                       │       │                    file installation. The implementation unlinks an existing
│                       │       │                   destination file and then recreates it using a path-based
│                       │       │                   operation without the O_EXCL flag. A local attacker can
│                       │       │                   exploit the window between the unlink and the subsequent
│                       │       │                   creation to swap the path with a symbolic link, allowing
│                       │       │                   them to redirect privileged writes to overwrite arbitrary
│                       │       │                   system files. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 6.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/b5bbabc18a
│                       │       │                  │      1121908848d836f869a4e98eb63886 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/10067 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.6.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35355 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35355 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:37.993Z 
│                       │       ╰ LastModifiedDate: 2026-04-27T12:27:34.007Z 
│                       ├ [72]  ╭ VulnerabilityID : CVE-2026-35356 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35356 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:28b4474afd7d95f62ca23c429b83158a235fe6dbf959d2d7e1b7
│                       │       │                   8f814fb99934 
│                       │       ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability
│                       │       │                   exists in the in ... 
│                       │       ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability
│                       │       │                   exists in the install utility of uutils coreutils when
│                       │       │                   using the -D flag. The command creates parent directories
│                       │       │                   and subsequently performs a second path resolution to
│                       │       │                   create the target file, neither of which is anchored to a
│                       │       │                   directory file descriptor. An attacker with concurrent
│                       │       │                   write access can replace a path component with a symbolic
│                       │       │                   link between these operations, redirecting the privileged
│                       │       │                   write to an arbitrary file system location. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 6.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/0c41299975
│                       │       │                  │      f3c1e21cf5ca968d42cad55ceb42a1 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/10140 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.7.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35356 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35356 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:38.13Z 
│                       │       ╰ LastModifiedDate: 2026-04-27T12:27:28.787Z 
│                       ├ [73]  ╭ VulnerabilityID : CVE-2026-35357 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35357 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:def78dfb122c43f4a34d47e47939ed8f04541660a8055d1d5f04
│                       │       │                   139c6905a9c9 
│                       │       ├ Title           : The cp utility in uutils coreutils is vulnerable to an
│                       │       │                   information dis ... 
│                       │       ├ Description     : The cp utility in uutils coreutils is vulnerable to an
│                       │       │                   information disclosure race condition. Destination files
│                       │       │                   are initially created with umask-derived permissions (e.g.,
│                       │       │                    0644) before being restricted to their final mode (e.g.,
│                       │       │                   0600) later in the process. A local attacker can race to
│                       │       │                   open the file during this window; once obtained, the file
│                       │       │                   descriptor remains valid and readable even after the
│                       │       │                   permissions are tightened, exposing sensitive or private
│                       │       │                   file contents. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 4.7 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/10011 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35357 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35357 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:38.267Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T19:02:53.557Z 
│                       ├ [74]  ╭ VulnerabilityID : CVE-2026-35358 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35358 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:afa86e80989821307920858276ac4c106cefcb1e1b64553351f8
│                       │       │                   c744f491d91c 
│                       │       ├ Title           : The cp utility in uutils coreutils, when performing
│                       │       │                   recursive copies ( ... 
│                       │       ├ Description     : The cp utility in uutils coreutils, when performing
│                       │       │                   recursive copies (-R), incorrectly treats character and
│                       │       │                   block device nodes as stream sources rather than preserving
│                       │       │                    them. Because the implementation reads bytes into regular
│                       │       │                   files at the destination instead of using mknod, device
│                       │       │                   semantics are destroyed (e.g., /dev/null becomes a regular
│                       │       │                   file). This behavior can lead to runtime denial of service
│                       │       │                   through disk exhaustion or process hangs when reading from
│                       │       │                   unbounded device nodes. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-706 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ├ nvd   : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/
│                       │       │                  │      │           A:L 
│                       │       │                  │      ╰ V3Score : 4.4 
│                       │       │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 5.5 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/e6a3bb596f
│                       │       │                  │      149628ba973eec3d099f3bb69f2464 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/issues/9746 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/pull/11163 
│                       │       │                  ├ [4]: https://github.com/uutils/coreutils/releases/tag/0.7.0 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-35358 
│                       │       │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-35358 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:38.393Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T19:03:00.59Z 
│                       ├ [75]  ╭ VulnerabilityID : CVE-2026-35359 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35359 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:bf4e6291a17faf9af8c4065a43e7d30561de4d7fde826d09bc07
│                       │       │                   0cadcf0a7331 
│                       │       ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability in
│                       │       │                   the cp utilit ... 
│                       │       ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability in
│                       │       │                   the cp utility of uutils coreutils allows an attacker to
│                       │       │                   bypass no-dereference intent. The utility checks if a
│                       │       │                   source path is a symbolic link using path-based metadata
│                       │       │                   but subsequently opens it without the O_NOFOLLOW flag. An
│                       │       │                   attacker with concurrent write access can swap a regular
│                       │       │                   file for a symbolic link during this window, causing a
│                       │       │                   privileged cp process to copy the contents of arbitrary
│                       │       │                   sensitive files into a destination controlled by the
│                       │       │                   attacker. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-59 
│                       │       │                  ╰ [1]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 4.7 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/10017 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35359 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35359 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:38.537Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T19:02:25.72Z 
│                       ├ [76]  ╭ VulnerabilityID : CVE-2026-35360 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35360 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:00607b9187164b50fed309c743005e5739589b9ebeb7099124d3
│                       │       │                   8a7e8d2e1bd3 
│                       │       ├ Title           : The touch utility in uutils coreutils is vulnerable to a
│                       │       │                   Time-of-Check ... 
│                       │       ├ Description     : The touch utility in uutils coreutils is vulnerable to a
│                       │       │                   Time-of-Check to Time-of-Use (TOCTOU) race condition during
│                       │       │                    file creation. When the utility identifies a missing path,
│                       │       │                    it later attempts creation using File::create(), which
│                       │       │                   internally uses O_TRUNC. An attacker can exploit this
│                       │       │                   window to create a file or swap a symlink at the target
│                       │       │                   path, causing touch to truncate an existing file and
│                       │       │                   leading to permanent data loss. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 6.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/10019 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35360 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35360 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:38.673Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T19:02:11.56Z 
│                       ├ [77]  ╭ VulnerabilityID : CVE-2026-35361 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35361 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:49953a8fcc5a4cfce0c63ce4d23c697219a181211a9a2d641540
│                       │       │                   1681787a532f 
│                       │       ├ Title           : The mknod utility in uutils coreutils fails to handle
│                       │       │                   security labels  ... 
│                       │       ├ Description     : The mknod utility in uutils coreutils fails to handle
│                       │       │                   security labels atomically by creating device nodes before
│                       │       │                   setting the SELinux context. If labeling fails, the utility
│                       │       │                    attempts cleanup using std::fs::remove_dir, which cannot
│                       │       │                   remove device nodes or FIFOs. This leaves mislabeled nodes
│                       │       │                   behind with incorrect default contexts, potentially
│                       │       │                   allowing unauthorized access to device nodes that should
│                       │       │                   have been restricted by mandatory access controls. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-281 
│                       │       │                  ╰ [1]: CWE-459 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ├ nvd   : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/
│                       │       │                  │      │           A:N 
│                       │       │                  │      ╰ V3Score : 3.4 
│                       │       │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 4.4 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/42b2ad83cd
│                       │       │                  │      cf6e959ecb378c5040c60d9c64becf 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/10582 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.6.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35361 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35361 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:38.827Z 
│                       │       ╰ LastModifiedDate: 2026-04-27T12:27:20.527Z 
│                       ├ [78]  ╭ VulnerabilityID : CVE-2026-35362 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35362 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:cf55121f47682794b29f85d62a34bf13c2c709296a14adbdf750
│                       │       │                   0c70be8d6024 
│                       │       ├ Title           : The safe_traversal module in uutils coreutils, which
│                       │       │                   provides protecti ... 
│                       │       ├ Description     : The safe_traversal module in uutils coreutils, which
│                       │       │                   provides protection against Time-of-Check to Time-of-Use
│                       │       │                   (TOCTOU) symlink races using file-descriptor-relative
│                       │       │                   syscalls, is incorrectly limited to Linux targets. On other
│                       │       │                    Unix-like systems such as macOS and FreeBSD, the utility
│                       │       │                   fails to utilize these protections, leaving directory
│                       │       │                   traversal operations vulnerable to symlink race
│                       │       │                   conditions. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 3.6 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/30239e69a3
│                       │       │                  │      28e76d2377f2a0bc02fbde61c34280 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/9792 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.6.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35362 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35362 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:38.96Z 
│                       │       ╰ LastModifiedDate: 2026-04-27T12:26:40.533Z 
│                       ├ [79]  ╭ VulnerabilityID : CVE-2026-35363 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35363 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:afcd22f2d26b63841daec8f4434b8935abe5f49acdc20638c6c1
│                       │       │                   ac7437eb583a 
│                       │       ├ Title           : A vulnerability in the rm utility of uutils coreutils
│                       │       │                   allows the bypas ... 
│                       │       ├ Description     : A vulnerability in the rm utility of uutils coreutils
│                       │       │                   allows the bypass of safeguard mechanisms intended to
│                       │       │                   protect the current directory. While the utility correctly
│                       │       │                   refuses to delete . or .., it fails to recognize equivalent
│                       │       │                    paths with trailing slashes, such as ./ or .///. An
│                       │       │                   accidental or malicious execution of rm -rf ./ results in
│                       │       │                   the silent recursive deletion of all contents within the
│                       │       │                   current directory. The command further obscures the data
│                       │       │                   loss by reporting a misleading 'Invalid input' error, which
│                       │       │                    may cause users to miss the critical window for data
│                       │       │                   recovery. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-22 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:N/I:H/
│                       │       │                         │           A:L 
│                       │       │                         ╰ V3Score : 5.6 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/9749 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35363 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35363 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:39.12Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T19:02:00.463Z 
│                       ├ [80]  ╭ VulnerabilityID : CVE-2026-35364 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35364 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:d6db58367fb10b4f7046d71e876fcd4782b531fecb3acaacd105
│                       │       │                   c3bc0e20265b 
│                       │       ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) race condition
│                       │       │                   exists in the m ... 
│                       │       ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) race condition
│                       │       │                   exists in the mv utility of uutils coreutils during
│                       │       │                   cross-device operations. The utility removes the
│                       │       │                   destination path before recreating it through a copy
│                       │       │                   operation. A local attacker with write access to the
│                       │       │                   destination directory can exploit this window to replace
│                       │       │                   the destination with a symbolic link. The subsequent
│                       │       │                   privileged move operation will follow the symlink, allowing
│                       │       │                    the attacker to redirect the write and overwrite an
│                       │       │                   arbitrary target file with contents from the source. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 6.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/10015 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35364 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35364 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:39.737Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T19:19:11.777Z 
│                       ├ [81]  ╭ VulnerabilityID : CVE-2026-35365 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35365 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:666ab6f206b906a9ece2980b32a7dc16b7dc538cb6493582393c
│                       │       │                   2ea2bfad2ea6 
│                       │       ├ Title           : The mv utility in uutils coreutils improperly handles
│                       │       │                   directory trees  ... 
│                       │       ├ Description     : The mv utility in uutils coreutils improperly handles
│                       │       │                   directory trees containing symbolic links during moves
│                       │       │                   across filesystem boundaries. Instead of preserving
│                       │       │                   symlinks, the implementation expands them, copying the
│                       │       │                   linked targets as real files or directories at the
│                       │       │                   destination. This can lead to resource exhaustion (disk
│                       │       │                   space or time) if symlinks point to large external
│                       │       │                   directories, unexpected duplication of sensitive data into
│                       │       │                   unintended locations, or infinite recursion and repeated
│                       │       │                   copying in the presence of symlink loops. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-59 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:H/
│                       │       │                         │           A:L 
│                       │       │                         ╰ V3Score : 6.6 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/9654e4abaf
│                       │       │                  │      24449ef2279e9a16963edb5c8b8fef 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/10546 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.7.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35365 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35365 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:39.9Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T18:53:45.707Z 
│                       ├ [82]  ╭ VulnerabilityID : CVE-2026-35366 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35366 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:226bda86d80e2294dde5dcd19b3385c6190d1d6ee831a12e0e17
│                       │       │                   fb24a793b490 
│                       │       ├ Title           : The printenv utility in uutils coreutils fails to display
│                       │       │                   environment  ... 
│                       │       ├ Description     : The printenv utility in uutils coreutils fails to display
│                       │       │                   environment variables containing invalid UTF-8 byte
│                       │       │                   sequences. While POSIX permits arbitrary bytes in
│                       │       │                   environment strings, the uutils implementation silently
│                       │       │                   skips these entries rather than printing the raw bytes.
│                       │       │                   This vulnerability allows malicious environment variables
│                       │       │                   (e.g., adversarial LD_PRELOAD values) to evade inspection
│                       │       │                   by administrators or security auditing tools, potentially
│                       │       │                   allowing library injection or other environment-based
│                       │       │                   attacks to go undetected. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-754 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 4.4 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/0bfbbc00c7
│                       │       │                  │      895c0fb6ea94987b4aab99e3d7ee52 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/issues/9701 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/pull/9728 
│                       │       │                  ├ [4]: https://github.com/uutils/coreutils/releases/tag/0.6.0 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-35366 
│                       │       │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-35366 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:40.167Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T18:52:42.39Z 
│                       ├ [83]  ╭ VulnerabilityID : CVE-2026-35367 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35367 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:bfac0eb0fb43049ffaa6c44ba162e5097334bd24a21c1bcb5459
│                       │       │                   94741746b880 
│                       │       ├ Title           : The nohup utility in uutils coreutils creates its default
│                       │       │                   output file, ... 
│                       │       ├ Description     : The nohup utility in uutils coreutils creates its default
│                       │       │                   output file, nohup.out, without specifying explicit
│                       │       │                   restricted permissions. This causes the file to inherit
│                       │       │                   umask-based permissions, typically resulting in a
│                       │       │                   world-readable file (0644). In multi-user environments,
│                       │       │                   this allows any user on the system to read the captured
│                       │       │                   stdout/stderr output of a command, potentially exposing
│                       │       │                   sensitive information. This behavior diverges from GNU
│                       │       │                   coreutils, which creates nohup.out with owner-only (0600)
│                       │       │                   permissions. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-732 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 3.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/10021 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35367 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35367 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:40.423Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T19:19:05.067Z 
│                       ├ [84]  ╭ VulnerabilityID : CVE-2026-35368 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35368 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:7bf4ce6057c777eb985bb9a75b24c5a40c9de482dcdedee4c4bc
│                       │       │                   96dfe6f1aeea 
│                       │       ├ Title           : A vulnerability exists in the chroot utility of uutils
│                       │       │                   coreutils when  ... 
│                       │       ├ Description     : A vulnerability exists in the chroot utility of uutils
│                       │       │                   coreutils when using the --userspec option. The utility
│                       │       │                   resolves the user specification via getpwnam() after
│                       │       │                   entering the chroot but before dropping root privileges. On
│                       │       │                    glibc-based systems, this can trigger the Name Service
│                       │       │                   Switch (NSS) to load shared libraries (e.g., libnss_*.so.2)
│                       │       │                    from the new root directory. If the NEWROOT is writable by
│                       │       │                    an attacker, they can inject a malicious NSS module to
│                       │       │                   execute arbitrary code as root, facilitating a full
│                       │       │                   container escape or privilege escalation. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-426 
│                       │       ├ VendorSeverity   ╭ ghsa  : 3 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 7.9 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/10327 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35368 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35368 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:40.56Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T19:18:55.67Z 
│                       ├ [85]  ╭ VulnerabilityID : CVE-2026-35369 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35369 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:9305eba644ce12edef46f1b717783f53a9077a763357b5f092e4
│                       │       │                   0c15385cb007 
│                       │       ├ Title           : An argument parsing error in the kill utility of uutils
│                       │       │                   coreutils inco ... 
│                       │       ├ Description     : An argument parsing error in the kill utility of uutils
│                       │       │                   coreutils incorrectly interprets kill -1 as a request to
│                       │       │                   send the default signal (SIGTERM) to PID -1. Sending a
│                       │       │                   signal to PID -1 causes the kernel to terminate all
│                       │       │                   processes visible to the caller, potentially leading to a
│                       │       │                   system crash or massive process termination. This differs
│                       │       │                   from GNU coreutils, which correctly recognizes -1 as a
│                       │       │                   signal number in this context and would instead report a
│                       │       │                   missing PID argument. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-20 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 5.5 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/2d3aebce67
│                       │       │                  │      12841bc08b9b94e9078be50a25fc10 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/9700 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.6.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35369 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35369 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:40.687Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T18:50:23.537Z 
│                       ├ [86]  ╭ VulnerabilityID : CVE-2026-35370 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35370 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:0cf3be45a2c7f22b185b67112f7e6326e0f2a7f8b12524e0da7f
│                       │       │                   93d1649eec83 
│                       │       ├ Title           : The id utility in uutils coreutils miscalculates the
│                       │       │                   groups= section o ... 
│                       │       ├ Description     : The id utility in uutils coreutils miscalculates the
│                       │       │                   groups= section of its output. The implementation uses a
│                       │       │                   user's real GID instead of their effective GID to compute
│                       │       │                   the group list, leading to potentially divergent output
│                       │       │                   compared to GNU coreutils. Because many scripts and
│                       │       │                   automated processes rely on the output of id to make
│                       │       │                   security-critical access-control or permission decisions,
│                       │       │                   this discrepancy can lead to unauthorized access or
│                       │       │                   security misconfigurations. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-863 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 4.4 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/10006 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35370 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35370 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:40.833Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T20:02:44.33Z 
│                       ├ [87]  ╭ VulnerabilityID : CVE-2026-35371 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35371 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:dac76e20b1970f90df902653b96478622850c1c28e01258fe8a6
│                       │       │                   bed590f78c6e 
│                       │       ├ Title           : The id utility in uutils coreutils exhibits incorrect
│                       │       │                   behavior in its  ... 
│                       │       ├ Description     : The id utility in uutils coreutils exhibits incorrect
│                       │       │                   behavior in its "pretty print" output when the real UID and
│                       │       │                    effective UID differ. The implementation incorrectly uses
│                       │       │                   the effective GID instead of the effective UID when
│                       │       │                   performing a name lookup for the effective user. This
│                       │       │                   results in misleading diagnostic output that can cause
│                       │       │                   automated scripts or system administrators to make
│                       │       │                   incorrect decisions regarding file permissions or access
│                       │       │                   control. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-451 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 3.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/issues/10006 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35371 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35371 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:40.987Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T20:02:06.183Z 
│                       ├ [88]  ╭ VulnerabilityID : CVE-2026-35372 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35372 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:edd36aa896857ef942d5008daf8792b13cb5f08d5cb384026808
│                       │       │                   02e72cf6c7f9 
│                       │       ├ Title           : A logic error in the ln utility of uutils coreutils allows
│                       │       │                   the utility ... 
│                       │       ├ Description     : A logic error in the ln utility of uutils coreutils allows
│                       │       │                   the utility to dereference a symbolic link target even when
│                       │       │                    the --no-dereference (or -n) flag is explicitly provided.
│                       │       │                   The implementation previously only honored the
│                       │       │                   "no-dereference" intent if the --force (overwrite) mode was
│                       │       │                    also enabled. This flaw causes ln to follow a symbolic
│                       │       │                   link that points to a directory and create new links inside
│                       │       │                    that target directory instead of treating the symbolic
│                       │       │                   link itself as the destination. In environments where a
│                       │       │                   privileged user or system script uses ln -n to update a
│                       │       │                   symlink, a local attacker could manipulate existing
│                       │       │                   symbolic links to redirect file creation into sensitive
│                       │       │                   directories, potentially leading to unauthorized file
│                       │       │                   creation or system misconfiguration. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-61 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:N/I:H/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 5 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/394c4b17f2
│                       │       │                  │      f382b4be9f54389bcb79028de02f39 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/11253 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.8.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35372 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35372 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:41.85Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T18:49:46.51Z 
│                       ├ [89]  ╭ VulnerabilityID : CVE-2026-35373 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35373 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:206d6f6c6bd49d94f8a5980a918ac44029696678d63ed4e4bb0d
│                       │       │                   9800e11be14f 
│                       │       ├ Title           : A logic error in the ln utility of uutils coreutils causes
│                       │       │                   the program ... 
│                       │       ├ Description     : A logic error in the ln utility of uutils coreutils causes
│                       │       │                   the program to reject source paths containing non-UTF-8
│                       │       │                   filename bytes when using target-directory forms (e.g., ln
│                       │       │                   SOURCE... DIRECTORY). While GNU ln treats filenames as raw
│                       │       │                   bytes and creates the links correctly, the uutils
│                       │       │                   implementation enforces UTF-8 encoding, resulting in a
│                       │       │                   failure to stat the file and a non-zero exit code. In
│                       │       │                   environments where automated scripts or system tasks
│                       │       │                   process valid but non-UTF-8 filenames common on Unix
│                       │       │                   filesystems, this divergence causes the utility to fail,
│                       │       │                   leading to a local denial of service for those specific
│                       │       │                   operations. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-176 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ├ nvd   : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/
│                       │       │                  │      │           A:L 
│                       │       │                  │      ╰ V3Score : 3.3 
│                       │       │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 5.5 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/pull/11403 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35373 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35373 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:41.997Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T20:01:25.93Z 
│                       ├ [90]  ╭ VulnerabilityID : CVE-2026-35374 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35374 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:1477c2567ec3a7f894eda2d684452663f699fc64f597a5440412
│                       │       │                   aa2533fb0887 
│                       │       ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability
│                       │       │                   exists in the sp ... 
│                       │       ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability
│                       │       │                   exists in the split utility of uutils coreutils. The
│                       │       │                   program attempts to prevent data loss by checking for
│                       │       │                   identity between input and output files using their file
│                       │       │                   paths before initiating the split operation. However, the
│                       │       │                   utility subsequently opens the output file with truncation
│                       │       │                   after this path-based validation is complete. A local
│                       │       │                   attacker with write access to the directory can exploit
│                       │       │                   this race window by manipulating mutable path components
│                       │       │                   (e.g., swapping a path with a symbolic link). This can
│                       │       │                   cause split to truncate and write to an unintended target
│                       │       │                   file, potentially including the input file itself or other
│                       │       │                   sensitive files accessible to the process, leading to
│                       │       │                   permanent data loss. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/
│                       │       │                         │           A:H 
│                       │       │                         ╰ V3Score : 6.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/pull/11401 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35374 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35374 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:42.127Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T19:22:14.457Z 
│                       ├ [91]  ╭ VulnerabilityID : CVE-2026-35375 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35375 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:185d3be26e5875e7b01b84537efae753d4136c07dc47e7f0b540
│                       │       │                   749761c7cc30 
│                       │       ├ Title           : A logic error in the split utility of uutils coreutils
│                       │       │                   causes the corr ... 
│                       │       ├ Description     : A logic error in the split utility of uutils coreutils
│                       │       │                   causes the corruption of output filenames when provided
│                       │       │                   with non-UTF-8 prefix or suffix inputs. The implementation
│                       │       │                   utilizes to_string_lossy() when constructing chunk
│                       │       │                   filenames, which automatically rewrites invalid byte
│                       │       │                   sequences into the UTF-8 replacement character (U+FFFD).
│                       │       │                   This behavior diverges from GNU split, which preserves raw
│                       │       │                   pathname bytes intact. In environments utilizing non-UTF-8
│                       │       │                   encodings, this vulnerability leads to the creation of
│                       │       │                   files with incorrect names, potentially causing filename
│                       │       │                   collisions, broken automation, or the misdirection of
│                       │       │                   output data. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-176 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 3.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/d2b9550fe8
│                       │       │                  │      21a9a10bf0cec057509211357363f1 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/11397 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.8.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35375 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35375 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:42.293Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T19:13:37.293Z 
│                       ├ [92]  ╭ VulnerabilityID : CVE-2026-35376 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35376 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:d5c87dc6da8c831836ae068bece6ac166422c71e242024f674a7
│                       │       │                   9fb1230738b8 
│                       │       ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability
│                       │       │                   exists in the ch ... 
│                       │       ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability
│                       │       │                   exists in the chcon utility of uutils coreutils during
│                       │       │                   recursive operations. The implementation resolves recursive
│                       │       │                    targets using a fresh path lookup (via fts_accpath) rather
│                       │       │                    than binding the traversal and label application to the
│                       │       │                   specific directory state encountered during traversal.
│                       │       │                   Because these operations are not anchored to file
│                       │       │                   descriptors, a local attacker with write access to a
│                       │       │                   directory tree can exploit timing-sensitive rename or
│                       │       │                   symbolic link races to redirect a privileged recursive
│                       │       │                   relabeling operation to unintended files or directories.
│                       │       │                   This vulnerability breaks the hardening expectations for
│                       │       │                   SELinux administration workflows and can lead to the
│                       │       │                   unauthorized modification of security labels on sensitive
│                       │       │                   system objects. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-367 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ├ nvd   : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L/
│                       │       │                  │      │           A:L 
│                       │       │                  │      ╰ V3Score : 4.5 
│                       │       │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:H/
│                       │       │                         │           A:L 
│                       │       │                         ╰ V3Score : 5.8 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/pull/11402 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/releases/tag/0.8.0 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-35376 
│                       │       │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-35376 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:42.43Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T19:06:31.93Z 
│                       ├ [93]  ╭ VulnerabilityID : CVE-2026-35377 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35377 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:e7ddccf6255a9adf5fca15b6f7aaea79db39baf4d4cf1af82984
│                       │       │                   68f22ca21b25 
│                       │       ├ Title           : A logic error in the env utility of uutils coreutils causes
│                       │       │                    a failure  ... 
│                       │       ├ Description     : A logic error in the env utility of uutils coreutils causes
│                       │       │                    a failure to correctly parse command-line arguments when
│                       │       │                   utilizing the -S (split-string) option. In GNU env,
│                       │       │                   backslashes within single quotes are treated literally
│                       │       │                   (with the exceptions of \\ and \'). However, the uutils
│                       │       │                   implementation incorrectly attempts to validate these
│                       │       │                   sequences, resulting in an "invalid sequence" error and an
│                       │       │                   immediate process termination with an exit status of 125
│                       │       │                   when encountering valid but unrecognized sequences like \a
│                       │       │                   or \x. This divergence from GNU behavior breaks
│                       │       │                   compatibility for automated scripts and administrative
│                       │       │                   workflows that rely on standard split-string semantics,
│                       │       │                   leading to a local denial of service for those
│                       │       │                   operations. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-20 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/
│                       │       │                         │           A:L 
│                       │       │                         ╰ V3Score : 3.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/pull/11512 
│                       │       │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35377 
│                       │       │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35377 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:42.577Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T19:06:46.293Z 
│                       ├ [94]  ╭ VulnerabilityID : CVE-2026-35378 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35378 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:f275fd2f6a0a23e1ab65aca8976b7d3870f8be9f132667a5d481
│                       │       │                   5236ff2e60d3 
│                       │       ├ Title           : A logic error in the expr utility of uutils coreutils
│                       │       │                   causes the progr ... 
│                       │       ├ Description     : A logic error in the expr utility of uutils coreutils
│                       │       │                   causes the program to evaluate parenthesized subexpressions
│                       │       │                    during the parsing phase rather than at the execution
│                       │       │                   phase. This implementation flaw prevents the utility from
│                       │       │                   performing proper short-circuiting for logical OR (|) and
│                       │       │                   AND (&) operations. As a result, arithmetic errors (such as
│                       │       │                    division by zero) occurring within "dead" branches,
│                       │       │                   branches that should be ignored due to short-circuiting,
│                       │       │                   are raised as fatal errors. This divergence from GNU expr
│                       │       │                   behavior can cause guarded expressions within shell scripts
│                       │       │                    to fail with hard errors instead of returning expected
│                       │       │                   boolean results, leading to premature script termination
│                       │       │                   and breaking GNU-compatible shell control flow. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-768 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/
│                       │       │                         │           A:L 
│                       │       │                         ╰ V3Score : 3.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/76b2f7877f
│                       │       │                  │      558f3bfa78e3d4f49f022460f509b7 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/11395 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.8.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35378 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35378 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:42.73Z 
│                       │       ╰ LastModifiedDate: 2026-05-04T18:48:36.02Z 
│                       ├ [95]  ╭ VulnerabilityID : CVE-2026-35379 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35379 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:3eaa109a6054bc698f853e6581bc8c28d1f07cee194e396102a4
│                       │       │                   027e1d333530 
│                       │       ├ Title           : A logic error in the tr utility of uutils coreutils causes
│                       │       │                   the program ... 
│                       │       ├ Description     : A logic error in the tr utility of uutils coreutils causes
│                       │       │                   the program to incorrectly define the [:graph:] and
│                       │       │                   [:print:] character classes. The implementation mistakenly
│                       │       │                   includes the ASCII space character (0x20) in the [:graph:]
│                       │       │                   class and excludes it from the [:print:] class, effectively
│                       │       │                    reversing the standard behavior established by POSIX and
│                       │       │                   GNU coreutils. This vulnerability leads to unintended data
│                       │       │                   modification or loss when the utility is used in automated
│                       │       │                   scripts or data-cleaning pipelines that rely on standard
│                       │       │                   character class semantics. For example, a command executed
│                       │       │                   to delete all graphical characters while intending to
│                       │       │                   preserve whitespace will incorrectly delete all ASCII
│                       │       │                   spaces, potentially resulting in data corruption or logic
│                       │       │                   failures in downstream processing. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-684 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 3.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/358063f336
│                       │       │                  │      7cb23a1e5db314cfdbfeb607749b3d 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/11405 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.8.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35379 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35379 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:42.887Z 
│                       │       ╰ LastModifiedDate: 2026-04-29T15:59:08.45Z 
│                       ├ [96]  ╭ VulnerabilityID : CVE-2026-35380 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35380 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:46c869223d090a175c02a54ec6538eeeeae7a5bca65834eb5dd0
│                       │       │                   1cc258394b20 
│                       │       ├ Title           : A logic error in the cut utility of uutils coreutils causes
│                       │       │                    the progra ... 
│                       │       ├ Description     : A logic error in the cut utility of uutils coreutils causes
│                       │       │                    the program to incorrectly interpret the literal two-byte
│                       │       │                   string '' (two single quotes) as an empty delimiter. The
│                       │       │                   implementation mistakenly maps this string to the NUL
│                       │       │                   character for both the -d (delimiter) and
│                       │       │                   --output-delimiter options. This vulnerability can lead to
│                       │       │                   silent data corruption or logic errors in automated scripts
│                       │       │                    and data pipelines that process strings containing these
│                       │       │                   characters, as the utility may unintentionally split or
│                       │       │                   join data on NUL bytes rather than the intended literal
│                       │       │                   characters. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-20 
│                       │       ├ VendorSeverity   ╭ ghsa  : 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:H/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 5.5 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/593f5b191e
│                       │       │                  │      8b9c87e4292955999c2d0b5cbcce69 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/11399 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.8.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35380 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35380 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:43.047Z 
│                       │       ╰ LastModifiedDate: 2026-04-29T15:57:19.427Z 
│                       ├ [97]  ╭ VulnerabilityID : CVE-2026-35381 
│                       │       ├ PkgID           : rust-coreutils@0.2.2-0ubuntu2.1 
│                       │       ├ PkgName         : rust-coreutils 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.2.2-0ubuntu2.1?arch=
│                       │       │                  │       amd64&distro=ubuntu-25.10 
│                       │       │                  ╰ UID : ebefeb85901fc403 
│                       │       ├ InstalledVersion: 0.2.2-0ubuntu2.1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35381 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:5bc1830eb632b2d415866b1873dc8c4d4ba81d0698b24caa06c3
│                       │       │                   86966fc60a5d 
│                       │       ├ Title           : A logic error in the cut utility of uutils coreutils causes
│                       │       │                    the utilit ... 
│                       │       ├ Description     : A logic error in the cut utility of uutils coreutils causes
│                       │       │                    the utility to ignore the -s (only-delimited) flag when
│                       │       │                   using the -z (null-terminated) and -d '' (empty delimiter)
│                       │       │                   options together. The implementation incorrectly routes
│                       │       │                   this specific combination through a specialized
│                       │       │                   newline-delimiter code path that fails to check the record
│                       │       │                   suppression status. Consequently, uutils cut emits the
│                       │       │                   entire record plus a NUL byte instead of suppressing it.
│                       │       │                   This divergence from GNU coreutils behavior creates a data
│                       │       │                   integrity risk for automated pipelines that rely on cut -s
│                       │       │                   to filter out undelimited data. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-684 
│                       │       ├ VendorSeverity   ╭ ghsa  : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/
│                       │       │                         │           A:N 
│                       │       │                         ╰ V3Score : 3.3 
│                       │       ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │       │                  ├ [1]: https://github.com/uutils/coreutils/commit/483f13e918
│                       │       │                  │      30c468262aa1e010e753d6ae99c898 
│                       │       │                  ├ [2]: https://github.com/uutils/coreutils/pull/11394 
│                       │       │                  ├ [3]: https://github.com/uutils/coreutils/releases/tag/0.8.0 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35381 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35381 
│                       │       ├ PublishedDate   : 2026-04-22T17:16:43.2Z 
│                       │       ╰ LastModifiedDate: 2026-04-24T19:19:34.493Z 
│                       ├ [98]  ╭ VulnerabilityID : CVE-2026-5958 
│                       │       ├ PkgID           : sed@4.9-2build2 
│                       │       ├ PkgName         : sed 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/sed@4.9-2build2?arch=amd64&distro=ubu
│                       │       │                  │       ntu-25.10 
│                       │       │                  ╰ UID : 5c933b8e9aa12e84 
│                       │       ├ InstalledVersion: 4.9-2build2 
│                       │       ├ FixedVersion    : 4.9-2ubuntu0.25.10.1 
│                       │       ├ Status          : fixed 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5958 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:55efe5398b4ee97ecd5d68e34f9ecdccbb258fb50fb113005308
│                       │       │                   a8a17b9744c4 
│                       │       ├ Title           : When sed is invoked with both -i (in-place edit) and
│                       │       │                   --follow-symlinks ... 
│                       │       ├ Description     : When sed is invoked with both -i (in-place edit) and
│                       │       │                   --follow-symlinks, the function open_next_file() performs
│                       │       │                   two separate, non-atomic filesystem operations on the same
│                       │       │                   path: 
│                       │       │                   1. resolves symlink to its target and stores the resolved
│                       │       │                   path for determining when output is written,
│                       │       │                   2. opens the original symlink path (not the resolved one)
│                       │       │                   to read the file. 
│                       │       │                   Between these two calls there is a race window. If an
│                       │       │                   attacker atomically replaces the symlink with a different
│                       │       │                   target during that window, sed will: read content from the
│                       │       │                   new (attacker-chosen) symlink target and write the
│                       │       │                   processed result to the path recorded in step 1. This can
│                       │       │                   lead to arbitrary file overwrite with attacker-controlled
│                       │       │                   content in the context of the sed process.
│                       │       │                   
│                       │       │                   This issue was fixed in version 4.10. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-367 
│                       │       ├ VendorSeverity   ╭ azure : 1 
│                       │       │                  ├ julia : 1 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ─ julia ╭ V40Vector: CVSS:4.0/AV:L/AC:L/AT:P/PR:N/UI:N/VC:N/
│                       │       │                          │            VI:L/VA:N/SC:N/SI:N/SA:N 
│                       │       │                          ╰ V40Score : 2.1 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/05/13/1 
│                       │       │                  ├ [1]: https://cert.pl/en/posts/2026/04/CVE-2026-5958 
│                       │       │                  ├ [2]: https://github.com/advisories/GHSA-9r7w-j29g-xqx8 
│                       │       │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-5958 
│                       │       │                  ├ [4]: https://ubuntu.com/security/notices/USN-8229-1 
│                       │       │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2026-5958 
│                       │       │                  ├ [6]: https://www.gnu.org/software/sed 
│                       │       │                  ╰ [7]: https://www.gnu.org/software/sed/ 
│                       │       ├ PublishedDate   : 2026-04-20T12:16:08.433Z 
│                       │       ╰ LastModifiedDate: 2026-05-19T15:17:37.183Z 
│                       ├ [99]  ╭ VulnerabilityID : CVE-2025-45582 
│                       │       ├ PkgID           : tar@1.35+dfsg-3.1build1 
│                       │       ├ PkgName         : tar 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-3.1build1?arch=amd64&
│                       │       │                  │       distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 41081f85f98b9d6a 
│                       │       ├ InstalledVersion: 1.35+dfsg-3.1build1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-45582 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:6d25895d2ecd58fa126c50008957d4df533af342484c82eaadb3
│                       │       │                   dfb437a77267 
│                       │       ├ Title           : tar: Tar path traversal 
│                       │       ├ Description     : GNU Tar through 1.35 allows file overwrite via directory
│                       │       │                   traversal in crafted TAR archives, with a certain two-step
│                       │       │                   process. First, the victim must extract an archive that
│                       │       │                   contains a ../ symlink to a critical directory. Second, the
│                       │       │                    victim must extract an archive that contains a critical
│                       │       │                   file, specified via a relative pathname that begins with
│                       │       │                   the symlink name and ends with that critical file's name.
│                       │       │                   Here, the extraction follows the symlink and overwrites the
│                       │       │                    critical file. This bypasses the protection mechanism of
│                       │       │                   "Member name contains '..'" that would occur for a single
│                       │       │                   TAR archive that attempted to specify the critical file via
│                       │       │                    a ../ approach. For example, the first archive can contain
│                       │       │                    "x -> ../../../../../home/victim/.ssh" and the second
│                       │       │                   archive can contain x/authorized_keys. This can affect
│                       │       │                   server applications that automatically extract any number
│                       │       │                   of user-supplied TAR archives, and were relying on the
│                       │       │                   blocking of traversal. This can also affect software
│                       │       │                   installation processes in which "tar xf" is run more than
│                       │       │                   once (e.g., when installing a package can automatically
│                       │       │                   install two dependencies that are set up as untrusted
│                       │       │                   tarballs instead of official packages). NOTE: the official
│                       │       │                   GNU Tar manual has an otherwise-empty directory for each
│                       │       │                   "tar xf" in its Security Rules of Thumb; however,
│                       │       │                   third-party advice leads users to run "tar xf" more than
│                       │       │                   once into the same directory. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-24 
│                       │       ├ VendorSeverity   ╭ alma       : 2 
│                       │       │                  ├ oracle-oval: 2 
│                       │       │                  ├ redhat     : 2 
│                       │       │                  ├ rocky      : 2 
│                       │       │                  ╰ ubuntu     : 2 
│                       │       ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:
│                       │       │                           │           L/A:L 
│                       │       │                           ╰ V3Score : 5.6 
│                       │       ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2025/11/0
│                       │       │                  │       1/6 
│                       │       │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:0067 
│                       │       │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2025-45582 
│                       │       │                  ├ [3] : https://bugzilla.redhat.com/2379592 
│                       │       │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2379592 
│                       │       │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2
│                       │       │                  │       025-45582 
│                       │       │                  ├ [6] : https://errata.almalinux.org/9/ALSA-2026-0067.html 
│                       │       │                  ├ [7] : https://errata.rockylinux.org/RLSA-2026:0002 
│                       │       │                  ├ [8] : https://github.com/i900008/vulndb/blob/main/Gnu_tar_
│                       │       │                  │       vuln.md 
│                       │       │                  ├ [9] : https://linux.oracle.com/cve/CVE-2025-45582.html 
│                       │       │                  ├ [10]: https://linux.oracle.com/errata/ELSA-2026-0067.html 
│                       │       │                  ├ [11]: https://lists.gnu.org/archive/html/bug-tar/2025-08/m
│                       │       │                  │       sg00012.html 
│                       │       │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2025-45582 
│                       │       │                  ├ [13]: https://www.cve.org/CVERecord?id=CVE-2025-45582 
│                       │       │                  ├ [14]: https://www.gnu.org/software/tar/ 
│                       │       │                  ├ [15]: https://www.gnu.org/software/tar/manual/html_node/In
│                       │       │                  │       tegrity.html 
│                       │       │                  ├ [16]: https://www.gnu.org/software/tar/manual/html_node/In
│                       │       │                  │       tegrity.html#Integrity 
│                       │       │                  ╰ [17]: https://www.gnu.org/software/tar/manual/html_node/Se
│                       │       │                          curity-rules-of-thumb.html 
│                       │       ├ PublishedDate   : 2025-07-11T17:15:37.183Z 
│                       │       ╰ LastModifiedDate: 2025-11-02T01:15:32.307Z 
│                       ├ [100] ╭ VulnerabilityID : CVE-2026-5704 
│                       │       ├ PkgID           : tar@1.35+dfsg-3.1build1 
│                       │       ├ PkgName         : tar 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-3.1build1?arch=amd64&
│                       │       │                  │       distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 41081f85f98b9d6a 
│                       │       ├ InstalledVersion: 1.35+dfsg-3.1build1 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5704 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:743cef1a56bf8fdcfa25995838a8450e1e404cf3cfb99a15b9d5
│                       │       │                   3b480b03febb 
│                       │       ├ Title           : tar: tar: Hidden file injection via crafted archives 
│                       │       ├ Description     : A flaw was found in tar. A remote attacker could exploit
│                       │       │                   this vulnerability by crafting a malicious archive, leading
│                       │       │                    to hidden file injection with fully attacker-controlled
│                       │       │                   content. This bypasses pre-extraction inspection
│                       │       │                   mechanisms, potentially allowing an attacker to introduce
│                       │       │                   malicious files onto a system without detection. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ─ [0]: CWE-434 
│                       │       ├ VendorSeverity   ╭ nvd   : 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:
│                       │       │                  │        │           H/A:N 
│                       │       │                  │        ╰ V3Score : 5.5 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:N/I:
│                       │       │                           │           H/A:N 
│                       │       │                           ╰ V3Score : 5 
│                       │       ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/04/11
│                       │       │                  │      /10 
│                       │       │                  ├ [1]: http://www.openwall.com/lists/oss-security/2026/04/11
│                       │       │                  │      /11 
│                       │       │                  ├ [2]: http://www.openwall.com/lists/oss-security/2026/04/12/2 
│                       │       │                  ├ [3]: https://access.redhat.com/security/cve/CVE-2026-5704 
│                       │       │                  ├ [4]: https://bugzilla.redhat.com/show_bug.cgi?id=2455360 
│                       │       │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-5704 
│                       │       │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-5704 
│                       │       ├ PublishedDate   : 2026-04-06T16:16:42.14Z 
│                       │       ╰ LastModifiedDate: 2026-04-22T20:08:59.92Z 
│                       ├ [101] ╭ VulnerabilityID : CVE-2026-27456 
│                       │       ├ PkgID           : util-linux@2.41-4ubuntu4.2 
│                       │       ├ PkgName         : util-linux 
│                       │       ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/util-linux@2.41-4ubuntu4.2?arch=amd64
│                       │       │                  │       &distro=ubuntu-25.10 
│                       │       │                  ╰ UID : 4a5ea37c462ea4f5 
│                       │       ├ InstalledVersion: 2.41-4ubuntu4.2 
│                       │       ├ Status          : affected 
│                       │       ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                       │       │                  │         12ec388229d22e8ac9a98 
│                       │       │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                       │       │                            fd6f4501c5392df91067f 
│                       │       ├ SeveritySource  : ubuntu 
│                       │       ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │       ├ DataSource       ╭ ID  : ubuntu 
│                       │       │                  ├ Name: Ubuntu CVE Tracker 
│                       │       │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │       ├ Fingerprint     : sha256:8154ace83a4619f8a2d1f28a17a7cd15328fd13951ba98fea43f
│                       │       │                   e58eded1ef0d 
│                       │       ├ Title           : util-linux: TOCTOU in the mount program when setting up
│                       │       │                   loop devices 
│                       │       ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │       │                    to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │       │                   vulnerability has been identified in the SUID binary
│                       │       │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │       │                   setting up loop devices, validates the source file path
│                       │       │                   with user privileges via fork() + setuid() + realpath(),
│                       │       │                   but subsequently re-canonicalizes and opens it with root
│                       │       │                   privileges (euid=0) without verifying that the path has not
│                       │       │                    been replaced between both operations. Neither O_NOFOLLOW,
│                       │       │                    nor inode comparison, nor post-open fstat() are employed.
│                       │       │                   This allows a local unprivileged user to replace the source
│                       │       │                    file with a symlink pointing to any root-owned file or
│                       │       │                   device during the race window, causing the SUID binary to
│                       │       │                   open and mount it as root. Exploitation requires an
│                       │       │                   /etc/fstab entry with user,loop options whose path points
│                       │       │                   to a directory where the attacker has write permission, and
│                       │       │                    that /usr/bin/mount has the SUID bit set (the default
│                       │       │                   configuration on virtually all Linux distributions). The
│                       │       │                   impact is unauthorized read access to root-protected files
│                       │       │                   and block devices, including backup images, disk volumes,
│                       │       │                   and any file containing a valid filesystem. This issue has
│                       │       │                   been patched in version 2.41.4. 
│                       │       ├ Severity        : MEDIUM 
│                       │       ├ CweIDs           ╭ [0]: CWE-59 
│                       │       │                  ├ [1]: CWE-269 
│                       │       │                  ╰ [2]: CWE-367 
│                       │       ├ VendorSeverity   ╭ azure : 2 
│                       │       │                  ├ julia : 2 
│                       │       │                  ├ redhat: 2 
│                       │       │                  ╰ ubuntu: 2 
│                       │       ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                  │        │           N/A:N 
│                       │       │                  │        ╰ V3Score : 4.7 
│                       │       │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:
│                       │       │                           │           N/A:N 
│                       │       │                           ╰ V3Score : 4.7 
│                       │       ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │       │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e390
│                       │       │                  │      467b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │       │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag
│                       │       │                  │      /v2.41.4 
│                       │       │                  ├ [3]: https://github.com/util-linux/util-linux/security/adv
│                       │       │                  │      isories/GHSA-qq4x-vfq4-9h9g 
│                       │       │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │       │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │       ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │       ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ╰ [102] ╭ VulnerabilityID : CVE-2026-3184 
│                               ├ PkgID           : util-linux@2.41-4ubuntu4.2 
│                               ├ PkgName         : util-linux 
│                               ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/util-linux@2.41-4ubuntu4.2?arch=amd64
│                               │                  │       &distro=ubuntu-25.10 
│                               │                  ╰ UID : 4a5ea37c462ea4f5 
│                               ├ InstalledVersion: 2.41-4ubuntu4.2 
│                               ├ Status          : affected 
│                               ├ Layer            ╭ Digest: sha256:c8110fc70790ae3a54f0af9c87a727cec814938efc1
│                               │                  │         12ec388229d22e8ac9a98 
│                               │                  ╰ DiffID: sha256:d25184801990b1e08c3c14c33680a923e8193222064
│                               │                            fd6f4501c5392df91067f 
│                               ├ SeveritySource  : ubuntu 
│                               ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                               ├ DataSource       ╭ ID  : ubuntu 
│                               │                  ├ Name: Ubuntu CVE Tracker 
│                               │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                               ├ Fingerprint     : sha256:47f0f2aef9fbc2afa008d7ff4a498213c1fe39092fdd7e875dc8
│                               │                   1991a46d229b 
│                               ├ Title           : util-linux: util-linux: Access control bypass due to
│                               │                   improper hostname canonicalization 
│                               ├ Description     : A flaw was found in util-linux. Improper hostname
│                               │                   canonicalization in the `login(1)` utility, when invoked
│                               │                   with the `-h` option, can modify the supplied remote
│                               │                   hostname before setting `PAM_RHOST`. A remote attacker
│                               │                   could exploit this by providing a specially crafted
│                               │                   hostname, potentially bypassing host-based Pluggable
│                               │                   Authentication Modules (PAM) access control rules that rely
│                               │                    on fully qualified domain names. This could lead to
│                               │                   unauthorized access. 
│                               ├ Severity        : MEDIUM 
│                               ├ CweIDs           ─ [0]: CWE-289 
│                               ├ VendorSeverity   ╭ azure : 1 
│                               │                  ├ nvd   : 2 
│                               │                  ├ redhat: 1 
│                               │                  ╰ ubuntu: 2 
│                               ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                               │                  │        │           L/A:N 
│                               │                  │        ╰ V3Score : 5.3 
│                               │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                               │                           │           L/A:N 
│                               │                           ╰ V3Score : 3.7 
│                               ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                               │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                               │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                               │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                               │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                               ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                               ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages 
```
