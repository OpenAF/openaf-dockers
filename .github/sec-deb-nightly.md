```yaml
╭ [0] ╭ Target         : openaf/oaf:deb-nightly (ubuntu 26.04) 
│     ├ Class          : os-pkgs 
│     ├ Type           : ubuntu 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : bsdutils@1:2.41.3-3ubuntu2 
│                       │      ├ PkgName         : bsdutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/bsdutils@2.41.3-3ubuntu2?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : 35a8976635e225e2 
│                       │      ├ InstalledVersion: 1:2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e357e7386b5c3d8fc16db0b9765f54f83fce07fe358ed89099a27
│                       │      │                   c1c2071032b 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-59 
│                       │      │                  ├ [1]: CWE-269 
│                       │      │                  ╰ [2]: CWE-367 
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026
│                       │      │                  │      -27456 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [2]: https://github.com/bottlerocket-os/bottlerocket-core-k
│                       │      │                  │      it/blob/develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.to
│                       │      │                  │      ml 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [4]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [5]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:27:11.017Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : bsdutils@1:2.41.3-3ubuntu2 
│                       │      ├ PkgName         : bsdutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/bsdutils@2.41.3-3ubuntu2?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : 35a8976635e225e2 
│                       │      ├ InstalledVersion: 1:2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:465f28b558a358fd712204aa6614591c8357bdbf59a2bd3149633
│                       │      │                   77353f40c14 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-289 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │      │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:43:10.203Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : libblkid1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libblkid1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libblkid1@2.41.3-3ubuntu2?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : f63a0a78e3cac3a3 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:9d9bd53738a0fc0889cc79b603f6408c863d00900f3bf29ccde82
│                       │      │                   6a71a6f2c3c 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-59 
│                       │      │                  ├ [1]: CWE-269 
│                       │      │                  ╰ [2]: CWE-367 
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026
│                       │      │                  │      -27456 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [2]: https://github.com/bottlerocket-os/bottlerocket-core-k
│                       │      │                  │      it/blob/develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.to
│                       │      │                  │      ml 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [4]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [5]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:27:11.017Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : libblkid1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libblkid1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libblkid1@2.41.3-3ubuntu2?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : f63a0a78e3cac3a3 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:aa62750c7c4273c7352ddc0511010344928d1847b7b13ff61b286
│                       │      │                   534e8cdb76a 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-289 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │      │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:43:10.203Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-4046 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : aa471766c29fe384 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4046 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:8dba4cec40c1acb640a52f43658da125fc8d9fbdd37dd016ec190
│                       │      │                   ed3b375bf61 
│                       │      ├ Title           : glibc: glibc: Denial of Service via iconv() function with
│                       │      │                   specific character sets 
│                       │      ├ Description     : The iconv() function in the GNU C Library versions 2.43 and
│                       │      │                   earlier may crash due to an assertion failure when
│                       │      │                   converting inputs from the IBM1390 or IBM1399 character
│                       │      │                   sets, which may be used to remotely crash an application.
│                       │      │                   
│                       │      │                   This vulnerability can be trivially mitigated by removing
│                       │      │                   the IBM1390 and IBM1399 character sets from systems that do
│                       │      │                   not need them. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-617 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:20594 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-4046 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2453117 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2449777 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2449783 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2453117 
│                       │      │                  ├ [6] : https://cert-portal.siemens.com/productcert/html/ssa-
│                       │      │                  │       082556.html 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [10]: https://errata.almalinux.org/10/ALSA-2026-20594.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [12]: https://inbox.sourceware.org/libc-announce/76814edf-c
│                       │      │                  │       f7f-47ec-979d-2dce0a2c76bf@gotplt.org/T/#u 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-4046.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-50291.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2026-4046 
│                       │      │                  ├ [16]: https://packages.fedoraproject.org/pkgs/glibc/glibc-g
│                       │      │                  │       conv-extra/ 
│                       │      │                  ├ [17]: https://sourceware.org/bugzilla/show_bug.cgi?id=33980 
│                       │      │                  ├ [18]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │      │                  │       f=advisories/GLIBC-SA-2026-0007 
│                       │      │                  ├ [19]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │      │                  │       f=advisories/GLIBC-SA-2026-0007;hb=HEAD 
│                       │      │                  ╰ [20]: https://www.cve.org/CVERecord?id=CVE-2026-4046 
│                       │      ├ PublishedDate   : 2026-03-30T18:16:19.573Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:57.707Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-4437 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : aa471766c29fe384 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4437 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c950901d8ef136318697bb4b1ef136f84ca504bba46c8377d02e3
│                       │      │                   8dfe509ab2b 
│                       │      ├ Title           : glibc: glibc: Incorrect DNS response parsing via crafted DNS
│                       │      │                    server response 
│                       │      ├ Description     : Calling gethostbyaddr or gethostbyaddr_r with a configured
│                       │      │                   nsswitch.conf that specifies the library's DNS backend in
│                       │      │                   the GNU C Library version 2.34 to version 2.43 could, with a
│                       │      │                    crafted response from the configured DNS server, result in
│                       │      │                   a violation of the DNS specification that causes the
│                       │      │                   application to treat a non-answer section of the DNS
│                       │      │                   response as a valid answer. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-125 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:19061 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-4437 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2449777 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2449783 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2449777 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2449783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2453117 
│                       │      │                  ├ [7] : https://cert-portal.siemens.com/productcert/html/ssa-
│                       │      │                  │       082556.html 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [11]: https://errata.almalinux.org/10/ALSA-2026-19061.html 
│                       │      │                  ├ [12]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-4437.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-500006.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2026-4437 
│                       │      │                  ├ [16]: https://sourceware.org/bugzilla/show_bug.cgi?id=34014 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2026-4437 
│                       │      │                  ╰ [18]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │      │                          3/2 
│                       │      ├ PublishedDate   : 2026-03-20T20:16:49.477Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:57.923Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-4438 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : aa471766c29fe384 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4438 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7ad5cd7754e7b0fedd5d7271a2959f512eff694d27c02dd2c3eea
│                       │      │                   fbc38a471e5 
│                       │      ├ Title           : glibc: glibc: Invalid DNS hostname returned via
│                       │      │                   gethostbyaddr functions 
│                       │      ├ Description     : Calling gethostbyaddr or gethostbyaddr_r with a configured
│                       │      │                   nsswitch.conf that specifies the library's DNS backend in
│                       │      │                   the GNU C library version 2.34 to version 2.43 could result
│                       │      │                   in an invalid DNS hostname being returned to the caller in
│                       │      │                   violation of the DNS specification. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-20 
│                       │      │                  ╰ [1]: CWE-88 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:19061 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-4438 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2449777 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2449783 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2449777 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2449783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2453117 
│                       │      │                  ├ [7] : https://cert-portal.siemens.com/productcert/html/ssa-
│                       │      │                  │       082556.html 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [11]: https://errata.almalinux.org/10/ALSA-2026-19061.html 
│                       │      │                  ├ [12]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-4438.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-500006.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2026-4438 
│                       │      │                  ├ [16]: https://sourceware.org/bugzilla/show_bug.cgi?id=34015 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2026-4438 
│                       │      │                  ╰ [18]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │      │                          3/2 
│                       │      ├ PublishedDate   : 2026-03-20T20:16:49.623Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:58.247Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-5435 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : aa471766c29fe384 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5435 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:80889285a6664057cb839d4b394f5ef641b14607aef7448ce7a75
│                       │      │                   45ea8a7c6f2 
│                       │      ├ Title           : glibc: glibc: Out-of-bounds write via TSIG record processing 
│                       │      ├ Description     : The deprecated functions ns_printrrf, ns_printrr and
│                       │      │                   fp_nquery in the GNU C Library version 2.2 and newer fail to
│                       │      │                    enforce the caller-supplied buffer length, and can result
│                       │      │                   in an out-of-bounds write when printing TSIG records. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-787 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-5435 
│                       │      │                  ├ [1]: https://cert-portal.siemens.com/productcert/html/ssa-0
│                       │      │                  │      82556.html 
│                       │      │                  ├ [2]: https://inbox.sourceware.org/libc-alpha/cover.17775461
│                       │      │                  │      94.git.fweimer@redhat.com/ 
│                       │      │                  ├ [3]: https://inbox.sourceware.org/libc-announce/7a655d55-27
│                       │      │                  │      6f-41fe-b550-feb3ebb2ce91@redhat.com/T/#u 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-5435 
│                       │      │                  ├ [5]: https://sourceware.org/bugzilla/show_bug.cgi?id=34033 
│                       │      │                  ├ [6]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;f
│                       │      │                  │      =advisories/GLIBC-SA-2026-0011 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-5435 
│                       │      ├ PublishedDate   : 2026-04-28T13:19:22.29Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:19:01.36Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-6238 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : aa471766c29fe384 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6238 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:2e6349d5737cff34da165cd4dfd464fe656bfd433bdae9e68d876
│                       │      │                   8a9c9866ad3 
│                       │      ├ Title           : glibc: glibc: Application crash or uninitialized memory read
│                       │      │                    via crafted DNS response 
│                       │      ├ Description     : The deprecated functions ns_printrrf, ns_printrr and
│                       │      │                   fp_nquery in the GNU C Library version 2.0.1 to version 2.43
│                       │      │                    fail to validate the RDATA content against the RDATA length
│                       │      │                    in a DNS response when processing A6, CERT, LOC, TKEY or
│                       │      │                   TSIG records, which may allow an attacker to craft a DNS
│                       │      │                   response, causing a target application to crash or read
│                       │      │                   uninitialized memory.
│                       │      │                   
│                       │      │                   These functions are for application debugging only and hence
│                       │      │                    not in the path of code executed by the DNS resolver. 
│                       │      │                   Further, they have been deprecated since version 2.34 and
│                       │      │                   should not be used by any new applications.  Applications
│                       │      │                   should consider porting away from these interfaces since
│                       │      │                   they may be removed in future versions. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-126 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-6238 
│                       │      │                  ├ [1]: https://cert-portal.siemens.com/productcert/html/ssa-0
│                       │      │                  │      82556.html 
│                       │      │                  ├ [2]: https://inbox.sourceware.org/libc-alpha/cover.17775461
│                       │      │                  │      94.git.fweimer@redhat.com/ 
│                       │      │                  ├ [3]: https://inbox.sourceware.org/libc-announce/7a655d55-27
│                       │      │                  │      6f-41fe-b550-feb3ebb2ce91@redhat.com/T/#u 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-6238 
│                       │      │                  ├ [5]: https://sourceware.org/bugzilla/show_bug.cgi?id=34069 
│                       │      │                  ├ [6]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;f
│                       │      │                  │      =advisories/GLIBC-SA-2026-0012 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-6238 
│                       │      ├ PublishedDate   : 2026-04-28T19:37:47.523Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:19:09.2Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-4046 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 229c678f3865c408 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4046 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:cb93400caf4fd29ce6c6b2f5fef4ed62bb3775b8854a30a2727b4
│                       │      │                   405d780bd2c 
│                       │      ├ Title           : glibc: glibc: Denial of Service via iconv() function with
│                       │      │                   specific character sets 
│                       │      ├ Description     : The iconv() function in the GNU C Library versions 2.43 and
│                       │      │                   earlier may crash due to an assertion failure when
│                       │      │                   converting inputs from the IBM1390 or IBM1399 character
│                       │      │                   sets, which may be used to remotely crash an application.
│                       │      │                   
│                       │      │                   This vulnerability can be trivially mitigated by removing
│                       │      │                   the IBM1390 and IBM1399 character sets from systems that do
│                       │      │                   not need them. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-617 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:20594 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-4046 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2453117 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2449777 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2449783 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2453117 
│                       │      │                  ├ [6] : https://cert-portal.siemens.com/productcert/html/ssa-
│                       │      │                  │       082556.html 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [10]: https://errata.almalinux.org/10/ALSA-2026-20594.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [12]: https://inbox.sourceware.org/libc-announce/76814edf-c
│                       │      │                  │       f7f-47ec-979d-2dce0a2c76bf@gotplt.org/T/#u 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-4046.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-50291.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2026-4046 
│                       │      │                  ├ [16]: https://packages.fedoraproject.org/pkgs/glibc/glibc-g
│                       │      │                  │       conv-extra/ 
│                       │      │                  ├ [17]: https://sourceware.org/bugzilla/show_bug.cgi?id=33980 
│                       │      │                  ├ [18]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │      │                  │       f=advisories/GLIBC-SA-2026-0007 
│                       │      │                  ├ [19]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │      │                  │       f=advisories/GLIBC-SA-2026-0007;hb=HEAD 
│                       │      │                  ╰ [20]: https://www.cve.org/CVERecord?id=CVE-2026-4046 
│                       │      ├ PublishedDate   : 2026-03-30T18:16:19.573Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:57.707Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-4437 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 229c678f3865c408 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4437 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:92132da3a7a7276a3bad49af2624e16718a26a1af30eb28ac3194
│                       │      │                   504570abf99 
│                       │      ├ Title           : glibc: glibc: Incorrect DNS response parsing via crafted DNS
│                       │      │                    server response 
│                       │      ├ Description     : Calling gethostbyaddr or gethostbyaddr_r with a configured
│                       │      │                   nsswitch.conf that specifies the library's DNS backend in
│                       │      │                   the GNU C Library version 2.34 to version 2.43 could, with a
│                       │      │                    crafted response from the configured DNS server, result in
│                       │      │                   a violation of the DNS specification that causes the
│                       │      │                   application to treat a non-answer section of the DNS
│                       │      │                   response as a valid answer. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-125 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:19061 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-4437 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2449777 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2449783 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2449777 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2449783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2453117 
│                       │      │                  ├ [7] : https://cert-portal.siemens.com/productcert/html/ssa-
│                       │      │                  │       082556.html 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [11]: https://errata.almalinux.org/10/ALSA-2026-19061.html 
│                       │      │                  ├ [12]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-4437.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-500006.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2026-4437 
│                       │      │                  ├ [16]: https://sourceware.org/bugzilla/show_bug.cgi?id=34014 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2026-4437 
│                       │      │                  ╰ [18]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │      │                          3/2 
│                       │      ├ PublishedDate   : 2026-03-20T20:16:49.477Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:57.923Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-4438 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 229c678f3865c408 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4438 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:65aa7fd216c4802a624d334edb9f0ed2f7ff0c6d692fc9f2a2ddb
│                       │      │                   b70708aa194 
│                       │      ├ Title           : glibc: glibc: Invalid DNS hostname returned via
│                       │      │                   gethostbyaddr functions 
│                       │      ├ Description     : Calling gethostbyaddr or gethostbyaddr_r with a configured
│                       │      │                   nsswitch.conf that specifies the library's DNS backend in
│                       │      │                   the GNU C library version 2.34 to version 2.43 could result
│                       │      │                   in an invalid DNS hostname being returned to the caller in
│                       │      │                   violation of the DNS specification. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-20 
│                       │      │                  ╰ [1]: CWE-88 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:19061 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-4438 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2449777 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2449783 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2449777 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2449783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2453117 
│                       │      │                  ├ [7] : https://cert-portal.siemens.com/productcert/html/ssa-
│                       │      │                  │       082556.html 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [11]: https://errata.almalinux.org/10/ALSA-2026-19061.html 
│                       │      │                  ├ [12]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-4438.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-500006.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2026-4438 
│                       │      │                  ├ [16]: https://sourceware.org/bugzilla/show_bug.cgi?id=34015 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2026-4438 
│                       │      │                  ╰ [18]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │      │                          3/2 
│                       │      ├ PublishedDate   : 2026-03-20T20:16:49.623Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:58.247Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-5435 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 229c678f3865c408 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5435 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:fbfa3ab2d3d5e2dffc69a9eda8955f047255a7754ec78598aedfb
│                       │      │                   dde0ff0bd14 
│                       │      ├ Title           : glibc: glibc: Out-of-bounds write via TSIG record processing 
│                       │      ├ Description     : The deprecated functions ns_printrrf, ns_printrr and
│                       │      │                   fp_nquery in the GNU C Library version 2.2 and newer fail to
│                       │      │                    enforce the caller-supplied buffer length, and can result
│                       │      │                   in an out-of-bounds write when printing TSIG records. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-787 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-5435 
│                       │      │                  ├ [1]: https://cert-portal.siemens.com/productcert/html/ssa-0
│                       │      │                  │      82556.html 
│                       │      │                  ├ [2]: https://inbox.sourceware.org/libc-alpha/cover.17775461
│                       │      │                  │      94.git.fweimer@redhat.com/ 
│                       │      │                  ├ [3]: https://inbox.sourceware.org/libc-announce/7a655d55-27
│                       │      │                  │      6f-41fe-b550-feb3ebb2ce91@redhat.com/T/#u 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-5435 
│                       │      │                  ├ [5]: https://sourceware.org/bugzilla/show_bug.cgi?id=34033 
│                       │      │                  ├ [6]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;f
│                       │      │                  │      =advisories/GLIBC-SA-2026-0011 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-5435 
│                       │      ├ PublishedDate   : 2026-04-28T13:19:22.29Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:19:01.36Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-6238 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 229c678f3865c408 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6238 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f7aea954607efd66fda666c5620c1c8a4b8b1878dc7687ae10139
│                       │      │                   d36568d0d48 
│                       │      ├ Title           : glibc: glibc: Application crash or uninitialized memory read
│                       │      │                    via crafted DNS response 
│                       │      ├ Description     : The deprecated functions ns_printrrf, ns_printrr and
│                       │      │                   fp_nquery in the GNU C Library version 2.0.1 to version 2.43
│                       │      │                    fail to validate the RDATA content against the RDATA length
│                       │      │                    in a DNS response when processing A6, CERT, LOC, TKEY or
│                       │      │                   TSIG records, which may allow an attacker to craft a DNS
│                       │      │                   response, causing a target application to crash or read
│                       │      │                   uninitialized memory.
│                       │      │                   
│                       │      │                   These functions are for application debugging only and hence
│                       │      │                    not in the path of code executed by the DNS resolver. 
│                       │      │                   Further, they have been deprecated since version 2.34 and
│                       │      │                   should not be used by any new applications.  Applications
│                       │      │                   should consider porting away from these interfaces since
│                       │      │                   they may be removed in future versions. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-126 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-6238 
│                       │      │                  ├ [1]: https://cert-portal.siemens.com/productcert/html/ssa-0
│                       │      │                  │      82556.html 
│                       │      │                  ├ [2]: https://inbox.sourceware.org/libc-alpha/cover.17775461
│                       │      │                  │      94.git.fweimer@redhat.com/ 
│                       │      │                  ├ [3]: https://inbox.sourceware.org/libc-announce/7a655d55-27
│                       │      │                  │      6f-41fe-b550-feb3ebb2ce91@redhat.com/T/#u 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-6238 
│                       │      │                  ├ [5]: https://sourceware.org/bugzilla/show_bug.cgi?id=34069 
│                       │      │                  ├ [6]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;f
│                       │      │                  │      =advisories/GLIBC-SA-2026-0012 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-6238 
│                       │      ├ PublishedDate   : 2026-04-28T19:37:47.523Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:19:09.2Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-4046 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2?arch=amd64&distro=
│                       │      │                  │       ubuntu-26.04 
│                       │      │                  ╰ UID : a6167efe03e34488 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4046 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:57cc3e817fbea5847fe82ae648da2b9f0fb00fbd403ca9797a6cd
│                       │      │                   8b8ceb5f849 
│                       │      ├ Title           : glibc: glibc: Denial of Service via iconv() function with
│                       │      │                   specific character sets 
│                       │      ├ Description     : The iconv() function in the GNU C Library versions 2.43 and
│                       │      │                   earlier may crash due to an assertion failure when
│                       │      │                   converting inputs from the IBM1390 or IBM1399 character
│                       │      │                   sets, which may be used to remotely crash an application.
│                       │      │                   
│                       │      │                   This vulnerability can be trivially mitigated by removing
│                       │      │                   the IBM1390 and IBM1399 character sets from systems that do
│                       │      │                   not need them. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-617 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:20594 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-4046 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2453117 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2449777 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2449783 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2453117 
│                       │      │                  ├ [6] : https://cert-portal.siemens.com/productcert/html/ssa-
│                       │      │                  │       082556.html 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [10]: https://errata.almalinux.org/10/ALSA-2026-20594.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [12]: https://inbox.sourceware.org/libc-announce/76814edf-c
│                       │      │                  │       f7f-47ec-979d-2dce0a2c76bf@gotplt.org/T/#u 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-4046.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-50291.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2026-4046 
│                       │      │                  ├ [16]: https://packages.fedoraproject.org/pkgs/glibc/glibc-g
│                       │      │                  │       conv-extra/ 
│                       │      │                  ├ [17]: https://sourceware.org/bugzilla/show_bug.cgi?id=33980 
│                       │      │                  ├ [18]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │      │                  │       f=advisories/GLIBC-SA-2026-0007 
│                       │      │                  ├ [19]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │      │                  │       f=advisories/GLIBC-SA-2026-0007;hb=HEAD 
│                       │      │                  ╰ [20]: https://www.cve.org/CVERecord?id=CVE-2026-4046 
│                       │      ├ PublishedDate   : 2026-03-30T18:16:19.573Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:57.707Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-4437 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2?arch=amd64&distro=
│                       │      │                  │       ubuntu-26.04 
│                       │      │                  ╰ UID : a6167efe03e34488 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4437 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0f3dba22c45c454f6d0f6d208c711909cce4e4096a1b587b804d7
│                       │      │                   8a6102487a4 
│                       │      ├ Title           : glibc: glibc: Incorrect DNS response parsing via crafted DNS
│                       │      │                    server response 
│                       │      ├ Description     : Calling gethostbyaddr or gethostbyaddr_r with a configured
│                       │      │                   nsswitch.conf that specifies the library's DNS backend in
│                       │      │                   the GNU C Library version 2.34 to version 2.43 could, with a
│                       │      │                    crafted response from the configured DNS server, result in
│                       │      │                   a violation of the DNS specification that causes the
│                       │      │                   application to treat a non-answer section of the DNS
│                       │      │                   response as a valid answer. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-125 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:19061 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-4437 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2449777 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2449783 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2449777 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2449783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2453117 
│                       │      │                  ├ [7] : https://cert-portal.siemens.com/productcert/html/ssa-
│                       │      │                  │       082556.html 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [11]: https://errata.almalinux.org/10/ALSA-2026-19061.html 
│                       │      │                  ├ [12]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-4437.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-500006.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2026-4437 
│                       │      │                  ├ [16]: https://sourceware.org/bugzilla/show_bug.cgi?id=34014 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2026-4437 
│                       │      │                  ╰ [18]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │      │                          3/2 
│                       │      ├ PublishedDate   : 2026-03-20T20:16:49.477Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:57.923Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-4438 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2?arch=amd64&distro=
│                       │      │                  │       ubuntu-26.04 
│                       │      │                  ╰ UID : a6167efe03e34488 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4438 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:221a3db93e7bff8acf6d181631f63f78bab21c3a3d54bbb039e79
│                       │      │                   9dc6ced9ffc 
│                       │      ├ Title           : glibc: glibc: Invalid DNS hostname returned via
│                       │      │                   gethostbyaddr functions 
│                       │      ├ Description     : Calling gethostbyaddr or gethostbyaddr_r with a configured
│                       │      │                   nsswitch.conf that specifies the library's DNS backend in
│                       │      │                   the GNU C library version 2.34 to version 2.43 could result
│                       │      │                   in an invalid DNS hostname being returned to the caller in
│                       │      │                   violation of the DNS specification. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-20 
│                       │      │                  ╰ [1]: CWE-88 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:19061 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-4438 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2449777 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2449783 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2449777 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2449783 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2453117 
│                       │      │                  ├ [7] : https://cert-portal.siemens.com/productcert/html/ssa-
│                       │      │                  │       082556.html 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [11]: https://errata.almalinux.org/10/ALSA-2026-19061.html 
│                       │      │                  ├ [12]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2026-4438.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2026-500006.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2026-4438 
│                       │      │                  ├ [16]: https://sourceware.org/bugzilla/show_bug.cgi?id=34015 
│                       │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2026-4438 
│                       │      │                  ╰ [18]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │      │                          3/2 
│                       │      ├ PublishedDate   : 2026-03-20T20:16:49.623Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:18:58.247Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2026-5435 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2?arch=amd64&distro=
│                       │      │                  │       ubuntu-26.04 
│                       │      │                  ╰ UID : a6167efe03e34488 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5435 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d59e96b1e357b86139f603ab43a4d89f4eff1d51c32005fb5cf25
│                       │      │                   856f1128b1e 
│                       │      ├ Title           : glibc: glibc: Out-of-bounds write via TSIG record processing 
│                       │      ├ Description     : The deprecated functions ns_printrrf, ns_printrr and
│                       │      │                   fp_nquery in the GNU C Library version 2.2 and newer fail to
│                       │      │                    enforce the caller-supplied buffer length, and can result
│                       │      │                   in an out-of-bounds write when printing TSIG records. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-787 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-5435 
│                       │      │                  ├ [1]: https://cert-portal.siemens.com/productcert/html/ssa-0
│                       │      │                  │      82556.html 
│                       │      │                  ├ [2]: https://inbox.sourceware.org/libc-alpha/cover.17775461
│                       │      │                  │      94.git.fweimer@redhat.com/ 
│                       │      │                  ├ [3]: https://inbox.sourceware.org/libc-announce/7a655d55-27
│                       │      │                  │      6f-41fe-b550-feb3ebb2ce91@redhat.com/T/#u 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-5435 
│                       │      │                  ├ [5]: https://sourceware.org/bugzilla/show_bug.cgi?id=34033 
│                       │      │                  ├ [6]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;f
│                       │      │                  │      =advisories/GLIBC-SA-2026-0011 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-5435 
│                       │      ├ PublishedDate   : 2026-04-28T13:19:22.29Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:19:01.36Z 
│                       ├ [18] ╭ VulnerabilityID : CVE-2026-6238 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2?arch=amd64&distro=
│                       │      │                  │       ubuntu-26.04 
│                       │      │                  ╰ UID : a6167efe03e34488 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6238 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f7fc24808a6d7e5d4b76dacbdb7f1cd63074d5845ef45a2a84311
│                       │      │                   c9f512519a4 
│                       │      ├ Title           : glibc: glibc: Application crash or uninitialized memory read
│                       │      │                    via crafted DNS response 
│                       │      ├ Description     : The deprecated functions ns_printrrf, ns_printrr and
│                       │      │                   fp_nquery in the GNU C Library version 2.0.1 to version 2.43
│                       │      │                    fail to validate the RDATA content against the RDATA length
│                       │      │                    in a DNS response when processing A6, CERT, LOC, TKEY or
│                       │      │                   TSIG records, which may allow an attacker to craft a DNS
│                       │      │                   response, causing a target application to crash or read
│                       │      │                   uninitialized memory.
│                       │      │                   
│                       │      │                   These functions are for application debugging only and hence
│                       │      │                    not in the path of code executed by the DNS resolver. 
│                       │      │                   Further, they have been deprecated since version 2.34 and
│                       │      │                   should not be used by any new applications.  Applications
│                       │      │                   should consider porting away from these interfaces since
│                       │      │                   they may be removed in future versions. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-126 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-6238 
│                       │      │                  ├ [1]: https://cert-portal.siemens.com/productcert/html/ssa-0
│                       │      │                  │      82556.html 
│                       │      │                  ├ [2]: https://inbox.sourceware.org/libc-alpha/cover.17775461
│                       │      │                  │      94.git.fweimer@redhat.com/ 
│                       │      │                  ├ [3]: https://inbox.sourceware.org/libc-announce/7a655d55-27
│                       │      │                  │      6f-41fe-b550-feb3ebb2ce91@redhat.com/T/#u 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-6238 
│                       │      │                  ├ [5]: https://sourceware.org/bugzilla/show_bug.cgi?id=34069 
│                       │      │                  ├ [6]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;f
│                       │      │                  │      =advisories/GLIBC-SA-2026-0012 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-6238 
│                       │      ├ PublishedDate   : 2026-04-28T19:37:47.523Z 
│                       │      ╰ LastModifiedDate: 2026-07-14T13:19:09.2Z 
│                       ├ [19] ╭ VulnerabilityID : CVE-2025-66382 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-66382 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e0ddc16b6cc9fdd3b16a027d4a5b2f0855a8ceeff62c87e43ac9c
│                       │      │                   65214197919 
│                       │      ├ Title           : libexpat: libexpat: Denial of service via crafted file
│                       │      │                   processing 
│                       │      ├ Description     : In libexpat through 2.7.3, a crafted file with an
│                       │      │                   approximate size of 2 MiB can lead to dozens of seconds of
│                       │      │                   processing time. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-407 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 2.9 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2025/12/02/1 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2025-66382 
│                       │      │                  ├ [2]: https://cert-portal.siemens.com/productcert/html/ssa-0
│                       │      │                  │      82556.html 
│                       │      │                  ├ [3]: https://cert-portal.siemens.com/productcert/html/ssa-2
│                       │      │                  │      53495.html 
│                       │      │                  ├ [4]: https://github.com/libexpat/libexpat/issues/1076 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2025-66382 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2025-66382 
│                       │      ├ PublishedDate   : 2025-11-28T07:15:57.9Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T09:56:45.24Z 
│                       ├ [20] ╭ VulnerabilityID : CVE-2024-2236 
│                       │      ├ PkgID           : libgcrypt20@1.12.0-2ubuntu1 
│                       │      ├ PkgName         : libgcrypt20 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgcrypt20@1.12.0-2ubuntu1?arch=amd64
│                       │      │                  │       &distro=ubuntu-26.04 
│                       │      │                  ╰ UID : c975856993003ac6 
│                       │      ├ InstalledVersion: 1.12.0-2ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-2236 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a62042b7a956ea74a517ec5e382fc133ec62bc2e6cfdf5bed9a2e
│                       │      │                   54c459db97f 
│                       │      ├ Title           : libgcrypt: vulnerable to Marvin Attack 
│                       │      ├ Description     : A timing-based side-channel flaw was found in libgcrypt's
│                       │      │                   RSA implementation. This issue may allow a remote attacker
│                       │      │                   to initiate a Bleichenbacher-style attack, which can lead to
│                       │      │                    the decryption of RSA ciphertexts. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-385 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
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
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-2236 
│                       │      │                  ├ [8] : https://dev.gnupg.org/T7136 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-9404.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:9404 
│                       │      │                  ├ [11]: https://github.com/tomato42/marvin-toolkit/tree/maste
│                       │      │                  │       r/example/libgcrypt 
│                       │      │                  ├ [12]: https://gitlab.com/redhat-crypto/libgcrypt/libgcrypt-
│                       │      │                  │       mirror/-/merge_requests/17 
│                       │      │                  ├ [13]: https://linux.oracle.com/cve/CVE-2024-2236.html 
│                       │      │                  ├ [14]: https://linux.oracle.com/errata/ELSA-2024-9404.html 
│                       │      │                  ├ [15]: https://lists.gnupg.org/pipermail/gcrypt-devel/2024-M
│                       │      │                  │       arch/005607.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2024-2236 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-2236 
│                       │      ├ PublishedDate   : 2024-03-06T22:15:57.977Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T07:24:06.083Z 
│                       ├ [21] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : libmount1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libmount1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libmount1@2.41.3-3ubuntu2?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : ee0638a59a092c7e 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ad05f52d166bb121496db94661608825dac3d7c3449484756ff39
│                       │      │                   85a70a699c4 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-59 
│                       │      │                  ├ [1]: CWE-269 
│                       │      │                  ╰ [2]: CWE-367 
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026
│                       │      │                  │      -27456 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [2]: https://github.com/bottlerocket-os/bottlerocket-core-k
│                       │      │                  │      it/blob/develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.to
│                       │      │                  │      ml 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [4]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [5]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:27:11.017Z 
│                       ├ [22] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : libmount1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libmount1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libmount1@2.41.3-3ubuntu2?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : ee0638a59a092c7e 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:73e2c1173824ea908821c65bf1cd72fbc3f1fe3aee4dee5130623
│                       │      │                   8b35f89e8d3 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-289 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │      │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:43:10.203Z 
│                       ├ [23] ╭ VulnerabilityID : CVE-2026-13757 
│                       │      ├ PkgID           : libp11-kit0@0.26.2-2 
│                       │      ├ PkgName         : libp11-kit0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libp11-kit0@0.26.2-2?arch=amd64&distro
│                       │      │                  │       =ubuntu-26.04 
│                       │      │                  ╰ UID : f30da36e7f9e8d5a 
│                       │      ├ InstalledVersion: 0.26.2-2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-13757 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:181b87e1c7207e2836a93b828477f695ede4dbd29a18215a74681
│                       │      │                   9ad627567a0 
│                       │      ├ Title           : p11-kit: Stack exhaustion via unbounded recursion in RPC
│                       │      │                   attribute parsing 
│                       │      ├ Description     : A flaw was found in p11-kit. The RPC message attribute
│                       │      │                   parsing functions p11_rpc_message_get_attribute() and
│                       │      │                   p11_rpc_message_get_attribute_array_value() form a
│                       │      │                   mutually-recursive call chain with no recursion depth limit
│                       │      │                   when processing nested CKA_WRAP_TEMPLATE,
│                       │      │                   CKA_UNWRAP_TEMPLATE, and CKA_DERIVE_TEMPLATE attributes. An
│                       │      │                   unauthenticated attacker with local access to the p11-kit
│                       │      │                   RPC Unix domain socket can send a specially crafted request
│                       │      │                   with deeply nested template attributes, causing stack
│                       │      │                   exhaustion and crashing the p11-kit server process and its
│                       │      │                   dependent services. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-674 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.2 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:37469 
│                       │      │                  ├ [1]: https://access.redhat.com/errata/RHSA-2026:38342 
│                       │      │                  ├ [2]: https://access.redhat.com/security/cve/CVE-2026-13757 
│                       │      │                  ├ [3]: https://bugzilla.redhat.com/show_bug.cgi?id=2494556 
│                       │      │                  ├ [4]: https://github.com/advisories/GHSA-p2wm-69qx-x25w 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-13757 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-13757 
│                       │      ├ PublishedDate   : 2026-06-29T19:16:40.907Z 
│                       │      ╰ LastModifiedDate: 2026-07-13T06:16:24.863Z 
│                       ├ [24] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : libsmartcols1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libsmartcols1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsmartcols1@2.41.3-3ubuntu2?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : ff5e7b67d2385233 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:99f7f6dea88e2c04435881838176400cbebcae5dbfc30eeda52a4
│                       │      │                   505274a4fce 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-59 
│                       │      │                  ├ [1]: CWE-269 
│                       │      │                  ╰ [2]: CWE-367 
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026
│                       │      │                  │      -27456 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [2]: https://github.com/bottlerocket-os/bottlerocket-core-k
│                       │      │                  │      it/blob/develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.to
│                       │      │                  │      ml 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [4]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [5]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:27:11.017Z 
│                       ├ [25] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : libsmartcols1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libsmartcols1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsmartcols1@2.41.3-3ubuntu2?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : ff5e7b67d2385233 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d7926327a7b8952512957f441f49c8fe69c8d59acb9ed64244ff8
│                       │      │                   d0b76ada2bc 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-289 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │      │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:43:10.203Z 
│                       ├ [26] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libsystemd0@259.5-0ubuntu3 
│                       │      ├ PkgName         : libsystemd0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsystemd0@259.5-0ubuntu3?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 68ed9dc5cf416dae 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b244e02d457b6cdeefa3df92f23e06e30bcd2c54571b4e0134e37
│                       │      │                   ceaa2f4f1bc 
│                       │      ├ Title           : systemd: systemd-journald: Unintended output to user
│                       │      │                   terminals via logger command 
│                       │      ├ Description     : In systemd 259, systemd-journald can send ANSI escape
│                       │      │                   sequences to the terminals of arbitrary users when a "logger
│                       │      │                    -p emerg" command is executed, if ForwardToWall=yes is
│                       │      │                   set. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-669 
│                       │      ├ VendorSeverity   ╭ nvd   : 1 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 3.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 2.9 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/05/05/1 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-40228 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-40228 
│                       │      │                  ├ [3]: https://www.cve.org/CVERecord?id=CVE-2026-40228 
│                       │      │                  ╰ [4]: https://www.openwall.com/lists/oss-security/2026/04/08/1 
│                       │      ├ PublishedDate   : 2026-04-10T16:16:33.753Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:44:53.31Z 
│                       ├ [27] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libudev1@259.5-0ubuntu3 
│                       │      ├ PkgName         : libudev1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libudev1@259.5-0ubuntu3?arch=amd64&dis
│                       │      │                  │       tro=ubuntu-26.04 
│                       │      │                  ╰ UID : 419f3d2219f938db 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d21a90d1253e67c90f674e86047b385fb4da2d5ee01d7a2542e5c
│                       │      │                   10c131bb591 
│                       │      ├ Title           : systemd: systemd-journald: Unintended output to user
│                       │      │                   terminals via logger command 
│                       │      ├ Description     : In systemd 259, systemd-journald can send ANSI escape
│                       │      │                   sequences to the terminals of arbitrary users when a "logger
│                       │      │                    -p emerg" command is executed, if ForwardToWall=yes is
│                       │      │                   set. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-669 
│                       │      ├ VendorSeverity   ╭ nvd   : 1 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 3.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 2.9 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/05/05/1 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-40228 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-40228 
│                       │      │                  ├ [3]: https://www.cve.org/CVERecord?id=CVE-2026-40228 
│                       │      │                  ╰ [4]: https://www.openwall.com/lists/oss-security/2026/04/08/1 
│                       │      ├ PublishedDate   : 2026-04-10T16:16:33.753Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:44:53.31Z 
│                       ├ [28] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : libuuid1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libuuid1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libuuid1@2.41.3-3ubuntu2?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04 
│                       │      │                  ╰ UID : 41d4afb2fde363cf 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ef4be7a3172965a6abfbd719fa984d2ced265c00d3d24e4cefba7
│                       │      │                   ab0faeb5da2 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-59 
│                       │      │                  ├ [1]: CWE-269 
│                       │      │                  ╰ [2]: CWE-367 
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026
│                       │      │                  │      -27456 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [2]: https://github.com/bottlerocket-os/bottlerocket-core-k
│                       │      │                  │      it/blob/develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.to
│                       │      │                  │      ml 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [4]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [5]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:27:11.017Z 
│                       ├ [29] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : libuuid1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libuuid1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libuuid1@2.41.3-3ubuntu2?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04 
│                       │      │                  ╰ UID : 41d4afb2fde363cf 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6f5261ee7c68050665f9fe52c383cb81d0db57a8bdee2e8991374
│                       │      │                   71b8b6c8749 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-289 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │      │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:43:10.203Z 
│                       ├ [30] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : login@1:4.16.0-2+really2.41.3-3ubuntu2 
│                       │      ├ PkgName         : login 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login@4.16.0-2%2Breally2.41.3-3ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : e1bfbadc9113c00a 
│                       │      ├ InstalledVersion: 1:4.16.0-2+really2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b576f43a4c37d22ef44dee359a3599f65bfdd901012331d89853d
│                       │      │                   80aba0228dd 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-59 
│                       │      │                  ├ [1]: CWE-269 
│                       │      │                  ╰ [2]: CWE-367 
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026
│                       │      │                  │      -27456 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [2]: https://github.com/bottlerocket-os/bottlerocket-core-k
│                       │      │                  │      it/blob/develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.to
│                       │      │                  │      ml 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [4]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [5]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:27:11.017Z 
│                       ├ [31] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : login@1:4.16.0-2+really2.41.3-3ubuntu2 
│                       │      ├ PkgName         : login 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login@4.16.0-2%2Breally2.41.3-3ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : e1bfbadc9113c00a 
│                       │      ├ InstalledVersion: 1:4.16.0-2+really2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5edf2eaa962979fbc6d1011a8794e07bc0a278ff4c6009b930768
│                       │      │                   35d33ead6a3 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-289 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │      │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:43:10.203Z 
│                       ├ [32] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : login.defs@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : login.defs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login.defs@4.17.4-2ubuntu3?arch=all&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : eaf648d5e4e975f7 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e2d1b05d31e44ff4c449bcfbdef768aba47d667660a6d2f3bf4b6
│                       │      │                   1706b21ceb8 
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
│                       │      ├ VendorSeverity   ╭ alma       : 1 
│                       │      │                  ├ azure      : 1 
│                       │      │                  ├ oracle-oval: 1 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:20559 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-56433 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2334165 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2334165 
│                       │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-56433 
│                       │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2025-20559.html 
│                       │      │                  ├ [6] : https://errata.rockylinux.org/RLSA-2025:20559 
│                       │      │                  ├ [7] : https://github.com/shadow-maint/shadow/blob/e2512d574
│                       │      │                  │       1d4a44bdd81a8c2d0029b6222728cf0/etc/login.defs#L238-L
│                       │      │                  │       241 
│                       │      │                  ├ [8] : https://github.com/shadow-maint/shadow/issues/1157 
│                       │      │                  ├ [9] : https://github.com/shadow-maint/shadow/releases/tag/4.4 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-56433.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2025-20559-0.html 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-56433 
│                       │      │                  ╰ [13]: https://www.cve.org/CVERecord?id=CVE-2024-56433 
│                       │      ├ PublishedDate   : 2024-12-26T09:15:07.267Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T08:12:10.903Z 
│                       ├ [33] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : mount@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : mount 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/mount@2.41.3-3ubuntu2?arch=amd64&distr
│                       │      │                  │       o=ubuntu-26.04 
│                       │      │                  ╰ UID : 98c6a5d7e9e110eb 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:544174290d4f73986b9ab759eda031d81e1ff8c4074bcbd9a9f8e
│                       │      │                   f241a92a7c4 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-59 
│                       │      │                  ├ [1]: CWE-269 
│                       │      │                  ╰ [2]: CWE-367 
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026
│                       │      │                  │      -27456 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [2]: https://github.com/bottlerocket-os/bottlerocket-core-k
│                       │      │                  │      it/blob/develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.to
│                       │      │                  │      ml 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [4]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [5]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:27:11.017Z 
│                       ├ [34] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : mount@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : mount 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/mount@2.41.3-3ubuntu2?arch=amd64&distr
│                       │      │                  │       o=ubuntu-26.04 
│                       │      │                  ╰ UID : 98c6a5d7e9e110eb 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:75f831bb424935f54e34f3ee2d0086204998f2e4725f35ebbbbd7
│                       │      │                   d1ed5a468d2 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-289 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │      │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:43:10.203Z 
│                       ├ [35] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : passwd@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : passwd 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/passwd@4.17.4-2ubuntu3?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : e6ebfac85406f0d5 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7757a0ddc07114c05796c2b72bb43d1e887bc04b0680daf21a03b
│                       │      │                   a2e76d9685b 
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
│                       │      ├ VendorSeverity   ╭ alma       : 1 
│                       │      │                  ├ azure      : 1 
│                       │      │                  ├ oracle-oval: 1 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.6 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:20559 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-56433 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2334165 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2334165 
│                       │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-56433 
│                       │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2025-20559.html 
│                       │      │                  ├ [6] : https://errata.rockylinux.org/RLSA-2025:20559 
│                       │      │                  ├ [7] : https://github.com/shadow-maint/shadow/blob/e2512d574
│                       │      │                  │       1d4a44bdd81a8c2d0029b6222728cf0/etc/login.defs#L238-L
│                       │      │                  │       241 
│                       │      │                  ├ [8] : https://github.com/shadow-maint/shadow/issues/1157 
│                       │      │                  ├ [9] : https://github.com/shadow-maint/shadow/releases/tag/4.4 
│                       │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2024-56433.html 
│                       │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2025-20559-0.html 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-56433 
│                       │      │                  ╰ [13]: https://www.cve.org/CVERecord?id=CVE-2024-56433 
│                       │      ├ PublishedDate   : 2024-12-26T09:15:07.267Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T08:12:10.903Z 
│                       ├ [36] ╭ VulnerabilityID : CVE-2026-35341 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35341 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f986a7220c086fd09492b3ed0e56089a3781ff65b5be17cc22d3b
│                       │      │                   524580df083 
│                       │      ├ Title           : A vulnerability in uutils coreutils mkfifo allows for the
│                       │      │                   unauthorized ... 
│                       │      ├ Description     : A vulnerability in uutils coreutils mkfifo allows for the
│                       │      │                   unauthorized modification of permissions on existing files.
│                       │      │                   When mkfifo fails to create a FIFO because a file already
│                       │      │                   exists at the target path, it fails to terminate the
│                       │      │                   operation for that path and continues to execute a follow-up
│                       │      │                    set_permissions call. This results in the existing file's
│                       │      │                   permissions being changed to the default mode (often 644
│                       │      │                   after umask), potentially exposing sensitive files such as
│                       │      │                   SSH private keys to other users on the system. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-732 
│                       │      ├ VendorSeverity   ╭ ghsa  : 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N 
│                       │      │                         ╰ V3Score : 7.1 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/10020 
│                       │      │                  ├ [2]: https://github.com/uutils/coreutils/pull/10376 
│                       │      │                  ├ [3]: https://github.com/uutils/coreutils/security/advisorie
│                       │      │                  │      s/GHSA-pmf6-rcx4-v53v 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-35341 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-35341 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:36.06Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:25.5Z 
│                       ├ [37] ╭ VulnerabilityID : CVE-2026-35344 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35344 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5ec578735c56acbe182d2651820380c500e81ba5d751fd8d88412
│                       │      │                   bed9ae14a72 
│                       │      ├ Title           : The dd utility in uutils coreutils suppresses errors during
│                       │      │                   file trunc ... 
│                       │      ├ Description     : The dd utility in uutils coreutils suppresses errors during
│                       │      │                   file truncation operations by unconditionally calling
│                       │      │                   Result::ok() on truncation attempts. While intended to mimic
│                       │      │                    GNU behavior for special files like /dev/null, the uutils
│                       │      │                   implementation also hides failures on regular files and
│                       │      │                   directories caused by full disks or read-only file systems.
│                       │      │                   This can lead to silent data corruption in backup or
│                       │      │                   migration scripts, as the utility may report a successful
│                       │      │                   operation even when the destination file contains old or
│                       │      │                   garbage data. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-252 
│                       │      ├ VendorSeverity   ╭ ghsa  : 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N 
│                       │      │                         ╰ V3Score : 3.3 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/9745 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35344 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35344 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:36.49Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:25.833Z 
│                       ├ [38] ╭ VulnerabilityID : CVE-2026-35345 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35345 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e8bdd7f926d09824f3f509fe9665d38e177ead7d4cb3f22d41c9e
│                       │      │                   aa1ea2191b4 
│                       │      ├ Title           : A vulnerability in the tail utility of uutils coreutils
│                       │      │                   allows for the ... 
│                       │      ├ Description     : A vulnerability in the tail utility of uutils coreutils
│                       │      │                   allows for the exfiltration of sensitive file contents when
│                       │      │                   using the --follow=name option. Unlike GNU tail, the uutils
│                       │      │                   implementation continues to monitor a path after it has been
│                       │      │                    replaced by a symbolic link, subsequently outputting the
│                       │      │                   contents of the link's target. In environments where a
│                       │      │                   privileged user (e.g., root) monitors a log directory, a
│                       │      │                   local attacker with write access to that directory can
│                       │      │                   replace a log file with a symlink to a sensitive system file
│                       │      │                    (such as /etc/shadow), causing tail to disclose the
│                       │      │                   contents of the sensitive file. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-59 
│                       │      │                  ╰ [1]: CWE-367 
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:L/A:N 
│                       │      │                         ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/10328 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35345 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35345 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:36.627Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:25.943Z 
│                       ├ [39] ╭ VulnerabilityID : CVE-2026-35348 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35348 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:68d378b34661d40ec21d95296df1d6c85928334727c70ec543b91
│                       │      │                   99f58d666d7 
│                       │      ├ Title           : The sort utility in uutils coreutils is vulnerable to a
│                       │      │                   process panic  ... 
│                       │      ├ Description     : The sort utility in uutils coreutils is vulnerable to a
│                       │      │                   process panic when using the --files0-from option with
│                       │      │                   inputs containing non-UTF-8 filenames. The implementation
│                       │      │                   enforces UTF-8 encoding and utilizes expect(), causing an
│                       │      │                   immediate crash when encountering valid but non-UTF-8 paths.
│                       │      │                    This diverges from GNU sort, which treats filenames as raw
│                       │      │                   bytes. A local attacker can exploit this to crash the
│                       │      │                   utility and disrupt automated pipelines. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-248 
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H 
│                       │      │                         ╰ V3Score : 5.5 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/9696 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35348 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35348 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.04Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.27Z 
│                       ├ [40] ╭ VulnerabilityID : CVE-2026-35350 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35350 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:302fd440eb6347ae5def879b786a6aea79b0ce7edd6a9dcb71525
│                       │      │                   68709212970 
│                       │      ├ Title           : The cp utility in uutils coreutils fails to properly handle
│                       │      │                   setuid and ... 
│                       │      ├ Description     : The cp utility in uutils coreutils fails to properly handle
│                       │      │                   setuid and setgid bits when ownership preservation fails.
│                       │      │                   When copying with the -p (preserve) flag, the utility
│                       │      │                   applies the source mode bits even if the chown operation is
│                       │      │                   unsuccessful. This can result in a user-owned copy retaining
│                       │      │                    original privileged bits, creating unexpected privileged
│                       │      │                   executables that violate local security policies. This
│                       │      │                   differs from GNU cp, which clears these bits when ownership
│                       │      │                   cannot be preserved. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-281 
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:H/A:L 
│                       │      │                         ╰ V3Score : 6.6 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/9750 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35350 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35350 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.327Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.48Z 
│                       ├ [41] ╭ VulnerabilityID : CVE-2026-35351 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35351 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:1b9fd51c89599ca71138c594664b523ade9a47141878180b7b506
│                       │      │                   b7193998e44 
│                       │      ├ Title           : The mv utility in uutils coreutils fails to preserve file
│                       │      │                   ownership du ... 
│                       │      ├ Description     : The mv utility in uutils coreutils fails to preserve file
│                       │      │                   ownership during moves across different filesystem
│                       │      │                   boundaries. The utility falls back to a copy-and-delete
│                       │      │                   routine that creates the destination file using the caller's
│                       │      │                    UID/GID rather than the source's metadata. This flaw breaks
│                       │      │                    backups and migrations, causing files moved by a privileged
│                       │      │                    user (e.g., root) to become root-owned unexpectedly, which
│                       │      │                   can lead to information disclosure or restricted access for
│                       │      │                   the intended owners. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-281 
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L 
│                       │      │                         ╰ V3Score : 4.2 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/9714 
│                       │      │                  ├ [2]: https://github.com/uutils/coreutils/pull/11706 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-35351 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-35351 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.457Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.587Z 
│                       ├ [42] ╭ VulnerabilityID : CVE-2026-35352 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35352 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:f50a136d4d50d89723abf3e6b209bbf5279ede69467c96d17dbf8
│                       │      │                   1b6d40c5f5f 
│                       │      ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) race condition
│                       │      │                   exists in the m ... 
│                       │      ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) race condition
│                       │      │                   exists in the mkfifo utility of uutils coreutils. The
│                       │      │                   utility creates a FIFO and then performs a path-based chmod
│                       │      │                   to set permissions. A local attacker with write access to
│                       │      │                   the parent directory can swap the newly created FIFO for a
│                       │      │                   symbolic link between these two operations. This redirects
│                       │      │                   the chmod call to an arbitrary file, potentially enabling
│                       │      │                   privilege escalation if the utility is run with elevated
│                       │      │                   privileges. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-367 
│                       │      ├ VendorSeverity   ╭ ghsa  : 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H 
│                       │      │                         ╰ V3Score : 7 
│                       │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2026/05/04/4 
│                       │      │                  ├ [1]: http://www.openwall.com/lists/oss-security/2026/05/04/5 
│                       │      │                  ├ [2]: http://www.openwall.com/lists/oss-security/2026/05/04/6 
│                       │      │                  ├ [3]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [4]: https://github.com/uutils/coreutils/issues/10020 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2026-35352 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-35352 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.597Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.69Z 
│                       ├ [43] ╭ VulnerabilityID : CVE-2026-35354 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35354 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c0bb18e5f73c685ea024c0a03cd8c4136fc081cf434db878e1ce1
│                       │      │                   02870f2789b 
│                       │      ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability exists
│                       │      │                    in the mv ... 
│                       │      ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability exists
│                       │      │                    in the mv utility of uutils coreutils during cross-device
│                       │      │                   moves. The extended attribute (xattr) preservation logic
│                       │      │                   uses multiple path-based system calls that perform fresh
│                       │      │                   path-to-inode lookups for each operation. A local attacker
│                       │      │                   with write access to the directory can exploit this race to
│                       │      │                   swap files between calls, causing the destination file to
│                       │      │                   receive an inconsistent mix of security xattrs, such as
│                       │      │                   SELinux labels or file capabilities. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-367 
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/A:N 
│                       │      │                         ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/10014 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35354 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35354 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:37.867Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:26.907Z 
│                       ├ [44] ╭ VulnerabilityID : CVE-2026-35357 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35357 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e6d31872d6fb789b72835245bb8062c8e16e46aeda3616668121c
│                       │      │                   3fe09d8ce44 
│                       │      ├ Title           : The cp utility in uutils coreutils is vulnerable to an
│                       │      │                   information dis ... 
│                       │      ├ Description     : The cp utility in uutils coreutils is vulnerable to an
│                       │      │                   information disclosure race condition. Destination files are
│                       │      │                    initially created with umask-derived permissions (e.g.,
│                       │      │                   0644) before being restricted to their final mode (e.g.,
│                       │      │                   0600) later in the process. A local attacker can race to
│                       │      │                   open the file during this window; once obtained, the file
│                       │      │                   descriptor remains valid and readable even after the
│                       │      │                   permissions are tightened, exposing sensitive or private
│                       │      │                   file contents. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-367 
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N 
│                       │      │                         ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/10011 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35357 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35357 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:38.267Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.223Z 
│                       ├ [45] ╭ VulnerabilityID : CVE-2026-35359 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35359 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c13f551d4da7e9185d450a2dcb86deacf421707933dc4c378a720
│                       │      │                   6f53567cc25 
│                       │      ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability in the
│                       │      │                    cp utilit ... 
│                       │      ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability in the
│                       │      │                    cp utility of uutils coreutils allows an attacker to bypass
│                       │      │                    no-dereference intent. The utility checks if a source path
│                       │      │                   is a symbolic link using path-based metadata but
│                       │      │                   subsequently opens it without the O_NOFOLLOW flag. An
│                       │      │                   attacker with concurrent write access can swap a regular
│                       │      │                   file for a symbolic link during this window, causing a
│                       │      │                   privileged cp process to copy the contents of arbitrary
│                       │      │                   sensitive files into a destination controlled by the
│                       │      │                   attacker. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-59 
│                       │      │                  ╰ [1]: CWE-367 
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N 
│                       │      │                         ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/10017 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35359 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35359 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:38.537Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.437Z 
│                       ├ [46] ╭ VulnerabilityID : CVE-2026-35360 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35360 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:bfa355fcfc6123896e99a09666e3a8550ebf15da9893b3ba8c681
│                       │      │                   b59bbd717cf 
│                       │      ├ Title           : The touch utility in uutils coreutils is vulnerable to a
│                       │      │                   Time-of-Check ... 
│                       │      ├ Description     : The touch utility in uutils coreutils is vulnerable to a
│                       │      │                   Time-of-Check to Time-of-Use (TOCTOU) race condition during
│                       │      │                   file creation. When the utility identifies a missing path,
│                       │      │                   it later attempts creation using File::create(), which
│                       │      │                   internally uses O_TRUNC. An attacker can exploit this window
│                       │      │                    to create a file or swap a symlink at the target path,
│                       │      │                   causing touch to truncate an existing file and leading to
│                       │      │                   permanent data loss. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-367 
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/A:H 
│                       │      │                         ╰ V3Score : 6.3 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/10019 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35360 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35360 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:38.673Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.543Z 
│                       ├ [47] ╭ VulnerabilityID : CVE-2026-35363 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35363 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6c2a8331de93bdb9919dc97019f2ff59f848b94e43bc287a117bb
│                       │      │                   2b384a9c499 
│                       │      ├ Title           : A vulnerability in the rm utility of uutils coreutils allows
│                       │      │                    the bypas ... 
│                       │      ├ Description     : A vulnerability in the rm utility of uutils coreutils allows
│                       │      │                    the bypass of safeguard mechanisms intended to protect the
│                       │      │                   current directory. While the utility correctly refuses to
│                       │      │                   delete . or .., it fails to recognize equivalent paths with
│                       │      │                   trailing slashes, such as ./ or .///. An accidental or
│                       │      │                   malicious execution of rm -rf ./ results in the silent
│                       │      │                   recursive deletion of all contents within the current
│                       │      │                   directory. The command further obscures the data loss by
│                       │      │                   reporting a misleading 'Invalid input' error, which may
│                       │      │                   cause users to miss the critical window for data recovery.[
│                       │      │                   m 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:N/I:H/A:L 
│                       │      │                         ╰ V3Score : 5.6 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/9749 
│                       │      │                  ├ [2]: https://github.com/uutils/coreutils/security/advisorie
│                       │      │                  │      s/GHSA-89p7-7cq3-hhr2 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-35363 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-35363 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:39.12Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.867Z 
│                       ├ [48] ╭ VulnerabilityID : CVE-2026-35364 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35364 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5b6799bbb7a5151ba66b7b8e6e012468254cbd9c115faa7384f5b
│                       │      │                   b0b1b401df2 
│                       │      ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) race condition
│                       │      │                   exists in the m ... 
│                       │      ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) race condition
│                       │      │                   exists in the mv utility of uutils coreutils during
│                       │      │                   cross-device operations. The utility removes the destination
│                       │      │                    path before recreating it through a copy operation. A local
│                       │      │                    attacker with write access to the destination directory can
│                       │      │                    exploit this window to replace the destination with a
│                       │      │                   symbolic link. The subsequent privileged move operation will
│                       │      │                    follow the symlink, allowing the attacker to redirect the
│                       │      │                   write and overwrite an arbitrary target file with contents
│                       │      │                   from the source. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-367 
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/A:H 
│                       │      │                         ╰ V3Score : 6.3 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/10015 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35364 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35364 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:39.737Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:27.97Z 
│                       ├ [49] ╭ VulnerabilityID : CVE-2026-35367 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35367 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6d5f742d826bbbb015e1dd24bd4c61517b917c64b1a7f979c297e
│                       │      │                   698b6b0c173 
│                       │      ├ Title           : The nohup utility in uutils coreutils creates its default
│                       │      │                   output file, ... 
│                       │      ├ Description     : The nohup utility in uutils coreutils creates its default
│                       │      │                   output file, nohup.out, without specifying explicit
│                       │      │                   restricted permissions. This causes the file to inherit
│                       │      │                   umask-based permissions, typically resulting in a
│                       │      │                   world-readable file (0644). In multi-user environments, this
│                       │      │                    allows any user on the system to read the captured
│                       │      │                   stdout/stderr output of a command, potentially exposing
│                       │      │                   sensitive information. This behavior diverges from GNU
│                       │      │                   coreutils, which creates nohup.out with owner-only (0600)
│                       │      │                   permissions. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-732 
│                       │      ├ VendorSeverity   ╭ ghsa  : 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N 
│                       │      │                         ╰ V3Score : 3.3 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/10021 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35367 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35367 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.423Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.297Z 
│                       ├ [50] ╭ VulnerabilityID : CVE-2026-35368 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35368 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b70f9849822c04d971adf304e4e958af7bf6884eb0c84567fff82
│                       │      │                   8d492cd1616 
│                       │      ├ Title           : A vulnerability exists in the chroot utility of uutils
│                       │      │                   coreutils when  ... 
│                       │      ├ Description     : A vulnerability exists in the chroot utility of uutils
│                       │      │                   coreutils when using the --userspec option. The utility
│                       │      │                   resolves the user specification via getpwnam() after
│                       │      │                   entering the chroot but before dropping root privileges. On
│                       │      │                   glibc-based systems, this can trigger the Name Service
│                       │      │                   Switch (NSS) to load shared libraries (e.g., libnss_*.so.2)
│                       │      │                   from the new root directory. If the NEWROOT is writable by
│                       │      │                   an attacker, they can inject a malicious NSS module to
│                       │      │                   execute arbitrary code as root, facilitating a full
│                       │      │                   container escape or privilege escalation. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-426 
│                       │      ├ VendorSeverity   ╭ ghsa  : 3 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H 
│                       │      │                         ╰ V3Score : 7.9 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/10327 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35368 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35368 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.56Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.4Z 
│                       ├ [51] ╭ VulnerabilityID : CVE-2026-35370 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35370 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:601121e1312d2ddb5298df6d9ae8b23bcfd44f9f327146eb05e9f
│                       │      │                   3a2adf356dc 
│                       │      ├ Title           : The id utility in uutils coreutils miscalculates the groups=
│                       │      │                    section o ... 
│                       │      ├ Description     : The id utility in uutils coreutils miscalculates the groups=
│                       │      │                    section of its output. The implementation uses a user's
│                       │      │                   real GID instead of their effective GID to compute the group
│                       │      │                    list, leading to potentially divergent output compared to
│                       │      │                   GNU coreutils. Because many scripts and automated processes
│                       │      │                   rely on the output of id to make security-critical
│                       │      │                   access-control or permission decisions, this discrepancy can
│                       │      │                    lead to unauthorized access or security
│                       │      │                   misconfigurations. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-863 
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N 
│                       │      │                         ╰ V3Score : 4.4 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/10006 
│                       │      │                  ├ [2]: https://github.com/uutils/coreutils/security/advisorie
│                       │      │                  │      s/GHSA-47c7-qrm7-mqw7 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-35370 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-35370 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.833Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.613Z 
│                       ├ [52] ╭ VulnerabilityID : CVE-2026-35371 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35371 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:36da2d1bc2c4fcc592c7f1ac446b4b5c97884c6c71b92be381ed0
│                       │      │                   d921506da7e 
│                       │      ├ Title           : The id utility in uutils coreutils exhibits incorrect
│                       │      │                   behavior in its  ... 
│                       │      ├ Description     : The id utility in uutils coreutils exhibits incorrect
│                       │      │                   behavior in its "pretty print" output when the real UID and
│                       │      │                   effective UID differ. The implementation incorrectly uses
│                       │      │                   the effective GID instead of the effective UID when
│                       │      │                   performing a name lookup for the effective user. This
│                       │      │                   results in misleading diagnostic output that can cause
│                       │      │                   automated scripts or system administrators to make incorrect
│                       │      │                    decisions regarding file permissions or access control. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-451 
│                       │      ├ VendorSeverity   ╭ ghsa  : 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N 
│                       │      │                         ╰ V3Score : 3.3 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/issues/10006 
│                       │      │                  ├ [2]: https://github.com/uutils/coreutils/security/advisorie
│                       │      │                  │      s/GHSA-xv5w-cw7x-72gj 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-35371 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-35371 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.987Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.723Z 
│                       ├ [53] ╭ VulnerabilityID : CVE-2026-35373 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35373 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:1f5b23050e798426c08a3ef130e4c941e190da687a2af959b5d27
│                       │      │                   76f88a2e80d 
│                       │      ├ Title           : A logic error in the ln utility of uutils coreutils causes
│                       │      │                   the program ... 
│                       │      ├ Description     : A logic error in the ln utility of uutils coreutils causes
│                       │      │                   the program to reject source paths containing non-UTF-8
│                       │      │                   filename bytes when using target-directory forms (e.g., ln
│                       │      │                   SOURCE... DIRECTORY). While GNU ln treats filenames as raw
│                       │      │                   bytes and creates the links correctly, the uutils
│                       │      │                   implementation enforces UTF-8 encoding, resulting in a
│                       │      │                   failure to stat the file and a non-zero exit code. In
│                       │      │                   environments where automated scripts or system tasks process
│                       │      │                    valid but non-UTF-8 filenames common on Unix filesystems,
│                       │      │                   this divergence causes the utility to fail, leading to a
│                       │      │                   local denial of service for those specific operations. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-176 
│                       │      ├ VendorSeverity   ╭ ghsa  : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L 
│                       │      │                  │      ╰ V3Score : 3.3 
│                       │      │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H 
│                       │      │                         ╰ V3Score : 5.5 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/pull/11403 
│                       │      │                  ├ [2]: https://github.com/uutils/coreutils/security/advisorie
│                       │      │                  │      s/GHSA-jcjr-rh8q-7xqf 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-35373 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-35373 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:41.997Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:28.933Z 
│                       ├ [54] ╭ VulnerabilityID : CVE-2026-35374 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3dc0c4825880f1f361bc2b577b7db15523084c635ae7a17d8244c
│                       │      │                   572ea7dc85f 
│                       │      ├ Title           : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability exists
│                       │      │                    in the sp ... 
│                       │      ├ Description     : A Time-of-Check to Time-of-Use (TOCTOU) vulnerability exists
│                       │      │                    in the split utility of uutils coreutils. The program
│                       │      │                   attempts to prevent data loss by checking for identity
│                       │      │                   between input and output files using their file paths before
│                       │      │                    initiating the split operation. However, the utility
│                       │      │                   subsequently opens the output file with truncation after
│                       │      │                   this path-based validation is complete. A local attacker
│                       │      │                   with write access to the directory can exploit this race
│                       │      │                   window by manipulating mutable path components (e.g.,
│                       │      │                   swapping a path with a symbolic link). This can cause split
│                       │      │                   to truncate and write to an unintended target file,
│                       │      │                   potentially including the input file itself or other
│                       │      │                   sensitive files accessible to the process, leading to
│                       │      │                   permanent data loss. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-367 
│                       │      ├ VendorSeverity   ╭ ghsa  : 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/A:H 
│                       │      │                         ╰ V3Score : 6.3 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/pull/11401 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35374 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35374 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:42.127Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:29.04Z 
│                       ├ [55] ╭ VulnerabilityID : CVE-2026-35377 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35377 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:aee8d1366d7dffcb672688f17c0706f71e8b7bbd7028219afaf33
│                       │      │                   6502878fafc 
│                       │      ├ Title           : A logic error in the env utility of uutils coreutils causes
│                       │      │                   a failure  ... 
│                       │      ├ Description     : A logic error in the env utility of uutils coreutils causes
│                       │      │                   a failure to correctly parse command-line arguments when
│                       │      │                   utilizing the -S (split-string) option. In GNU env,
│                       │      │                   backslashes within single quotes are treated literally (with
│                       │      │                    the exceptions of \\ and \'). However, the uutils
│                       │      │                   implementation incorrectly attempts to validate these
│                       │      │                   sequences, resulting in an "invalid sequence" error and an
│                       │      │                   immediate process termination with an exit status of 125
│                       │      │                   when encountering valid but unrecognized sequences like \a
│                       │      │                   or \x. This divergence from GNU behavior breaks
│                       │      │                   compatibility for automated scripts and administrative
│                       │      │                   workflows that rely on standard split-string semantics,
│                       │      │                   leading to a local denial of service for those operations.[
│                       │      │                   m 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-20 
│                       │      ├ VendorSeverity   ╭ ghsa  : 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L 
│                       │      │                         ╰ V3Score : 3.3 
│                       │      ├ References       ╭ [0]: https://github.com/uutils/coreutils 
│                       │      │                  ├ [1]: https://github.com/uutils/coreutils/pull/11512 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35377 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35377 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:42.577Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:40:29.357Z 
│                       ├ [56] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : util-linux@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : util-linux 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/util-linux@2.41.3-3ubuntu2?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 34e9503915630576 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:db245656ac882bca7c7c507b15010c3864848c65e81769079e0e7
│                       │      │                   12f71fe7782 
│                       │      ├ Title           : util-linux: TOCTOU in the mount program when setting up loop
│                       │      │                    devices 
│                       │      ├ Description     : util-linux is a random collection of Linux utilities. Prior
│                       │      │                   to version 2.41.4, a TOCTOU (Time-of-Check-Time-of-Use)
│                       │      │                   vulnerability has been identified in the SUID binary
│                       │      │                   /usr/bin/mount from util-linux. The mount binary, when
│                       │      │                   setting up loop devices, validates the source file path with
│                       │      │                    user privileges via fork() + setuid() + realpath(), but
│                       │      │                   subsequently re-canonicalizes and opens it with root
│                       │      │                   privileges (euid=0) without verifying that the path has not
│                       │      │                   been replaced between both operations. Neither O_NOFOLLOW,
│                       │      │                   nor inode comparison, nor post-open fstat() are employed.
│                       │      │                   This allows a local unprivileged user to replace the source
│                       │      │                   file with a symlink pointing to any root-owned file or
│                       │      │                   device during the race window, causing the SUID binary to
│                       │      │                   open and mount it as root. Exploitation requires an
│                       │      │                   /etc/fstab entry with user,loop options whose path points to
│                       │      │                    a directory where the attacker has write permission, and
│                       │      │                   that /usr/bin/mount has the SUID bit set (the default
│                       │      │                   configuration on virtually all Linux distributions). The
│                       │      │                   impact is unauthorized read access to root-protected files
│                       │      │                   and block devices, including backup images, disk volumes,
│                       │      │                   and any file containing a valid filesystem. This issue has
│                       │      │                   been patched in version 2.41.4. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ╭ [0]: CWE-59 
│                       │      │                  ├ [1]: CWE-269 
│                       │      │                  ╰ [2]: CWE-367 
│                       │      ├ VendorSeverity   ╭ azure       : 2 
│                       │      │                  ├ bottlerocket: 2 
│                       │      │                  ├ julia       : 2 
│                       │      │                  ├ redhat      : 2 
│                       │      │                  ╰ ubuntu      : 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026
│                       │      │                  │      -27456 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [2]: https://github.com/bottlerocket-os/bottlerocket-core-k
│                       │      │                  │      it/blob/develop/advisories/14.5.0/BRSA-jgcxwcxt3sxd.to
│                       │      │                  │      ml 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [4]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [5]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:27:11.017Z 
│                       ├ [57] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : util-linux@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : util-linux 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/util-linux@2.41.3-3ubuntu2?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 34e9503915630576 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                       │      │                  │         e5814b990e4a375056a9 
│                       │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                       │      │                            734c64e0c01604915e58 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:d61b1c3c787b1f3c978707c3b963d1b912d39f82d78a06d860b59
│                       │      │                   dc9d16f347b 
│                       │      ├ Title           : util-linux: util-linux: Access control bypass due to
│                       │      │                   improper hostname canonicalization 
│                       │      ├ Description     : A flaw was found in util-linux. Improper hostname
│                       │      │                   canonicalization in the `login(1)` utility, when invoked
│                       │      │                   with the `-h` option, can modify the supplied remote
│                       │      │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                       │      │                    exploit this by providing a specially crafted hostname,
│                       │      │                   potentially bypassing host-based Pluggable Authentication
│                       │      │                   Modules (PAM) access control rules that rely on fully
│                       │      │                   qualified domain names. This could lead to unauthorized
│                       │      │                   access. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-289 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ nvd   : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                       │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                       │      │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                       │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                       │      ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:43:10.203Z 
│                       ╰ [58] ╭ VulnerabilityID : CVE-2026-27171 
│                              ├ PkgID           : zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu3 
│                              ├ PkgName         : zlib1g 
│                              ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/zlib1g@1.3.dfsg%2Breally1.3.1-1ubuntu3
│                              │                  │       ?arch=amd64&distro=ubuntu-26.04&epoch=1 
│                              │                  ╰ UID : f9537564bd1f9cb2 
│                              ├ InstalledVersion: 1:1.3.dfsg+really1.3.1-1ubuntu3 
│                              ├ Status          : affected 
│                              ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
│                              │                  │         e5814b990e4a375056a9 
│                              │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
│                              │                            734c64e0c01604915e58 
│                              ├ SeveritySource  : ubuntu 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27171 
│                              ├ DataSource       ╭ ID  : ubuntu 
│                              │                  ├ Name: Ubuntu CVE Tracker 
│                              │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                              ├ Fingerprint     : sha256:7e56c2d5a20d2862d0e08818fda767de9b42dbd22a230e1d9eb55
│                              │                   287a911dae3 
│                              ├ Title           : zlib: zlib: Denial of Service via infinite loop in CRC32
│                              │                   combine functions 
│                              ├ Description     : zlib before 1.3.2 allows CPU consumption via crc32_combine64
│                              │                    and crc32_combine_gen64 because x2nmodp can do right shifts
│                              │                    within a loop that has no termination condition. 
│                              ├ Severity        : LOW 
│                              ├ CweIDs           ─ [0]: CWE-1284 
│                              ├ VendorSeverity   ╭ amazon     : 1 
│                              │                  ├ azure      : 1 
│                              │                  ├ cbl-mariner: 1 
│                              │                  ├ julia      : 2 
│                              │                  ├ nvd        : 2 
│                              │                  ├ photon     : 2 
│                              │                  ├ redhat     : 1 
│                              │                  ╰ ubuntu     : 1 
│                              ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                              │                  │        │           /A:H 
│                              │                  │        ╰ V3Score : 5.5 
│                              │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                              │                  │        │           /A:H 
│                              │                  │        ╰ V3Score : 5.5 
│                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                              │                           │           /A:L 
│                              │                           ╰ V3Score : 3.3 
│                              ├ References       ╭ [0] : https://7asecurity.com/blog/2026/02/zlib-7asecurity-a
│                              │                  │       udit 
│                              │                  ├ [1] : https://7asecurity.com/blog/2026/02/zlib-7asecurity-a
│                              │                  │       udit/ 
│                              │                  ├ [2] : https://7asecurity.com/reports/pentest-report-zlib-RC
│                              │                  │       1.1.pdf 
│                              │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2026-27171 
│                              │                  ├ [4] : https://github.com/advisories/GHSA-h858-mf2m-8jf4 
│                              │                  ├ [5] : https://github.com/madler/zlib/issues/904 
│                              │                  ├ [6] : https://github.com/madler/zlib/releases/tag/v1.3.2 
│                              │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2026-27171 
│                              │                  ├ [8] : https://ostif.org/zlib-audit-complete 
│                              │                  ├ [9] : https://ostif.org/zlib-audit-complete/ 
│                              │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2026-27171 
│                              ├ PublishedDate   : 2026-02-18T04:16:01.263Z 
│                              ╰ LastModifiedDate: 2026-06-17T10:26:47.357Z 
├ [1] ╭ Target         : Java 
│     ├ Class          : lang-pkgs 
│     ├ Type           : jar 
│     ├ Packages        
│     ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2026-54515 
│                             ├ VendorIDs        ─ [0]: GHSA-5jmj-h7xm-6q6v 
│                             ├ PkgName         : com.fasterxml.jackson.core:jackson-databind 
│                             ├ PkgPath         : openaf/openaf.jar 
│                             ├ PkgIdentifier    ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@
│                             │                  │       2.22.0 
│                             │                  ╰ UID : c3b2e55f064f8b6 
│                             ├ InstalledVersion: 2.22.0 
│                             ├ FixedVersion    : 3.1.4, 2.18.9, 2.21.5, 2.22.1 
│                             ├ Status          : fixed 
│                             ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73be
│                             │                  │         5814b990e4a375056a9 
│                             │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb4347
│                             │                            34c64e0c01604915e58 
│                             ├ SeveritySource  : ghsa 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-54515 
│                             ├ DataSource       ╭ ID  : ghsa 
│                             │                  ├ Name: GitHub Security Advisory Maven 
│                             │                  ╰ URL : https://github.com/advisories?query=type%3Areviewed+ec
│                             │                          osystem%3Amaven 
│                             ├ Fingerprint     : sha256:912633a66eed1fe94eae1a5fa7ecceaae02966f97cf299d1f6dd65
│                             │                   c926cb4b02 
│                             ├ Title           : jackson-databind: jackson-databind: Ignored properties can be
│                             │                    unexpectedly modified 
│                             ├ Description     : jackson-databind contains the general-purpose data-binding
│                             │                   functionality and tree-model for Jackson Data Processor. From
│                             │                    2.8.0 until 2.18.9, 2.21.5, and 3.1.4, in
│                             │                   BeanDeserializerBase.createContextual(), per-property
│                             │                   @JsonIgnoreProperties exclusions are applied by
│                             │                   _handleByNameInclusion(), producing a contextual deserializer
│                             │                    whose BeanPropertyMap has the ignored properties removed.
│                             │                   The subsequent per-property case-insensitivity block
│                             │                   (triggered by
│                             │                   @JsonFormat(ACCEPT_CASE_INSENSITIVE_PROPERTIES)) rebuilds
│                             │                   from this._beanProperties (the original, unfiltered map)
│                             │                   instead of contextual._beanProperties, then overwrites the
│                             │                   filtered map — restoring every property
│                             │                   _handleByNameInclusion had just removed. The ignored property
│                             │                    becomes writable again. This vulnerability is fixed in
│                             │                   2.18.9, 2.21.5, and 3.1.4. 
│                             ├ Severity        : MEDIUM 
│                             ├ CweIDs           ─ [0]: CWE-915 
│                             ├ VendorSeverity   ╭ amazon: 3 
│                             │                  ├ ghsa  : 2 
│                             │                  ╰ redhat: 2 
│                             ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/
│                             │                  │        │           A:N 
│                             │                  │        ╰ V3Score : 5.3 
│                             │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/
│                             │                           │           A:N 
│                             │                           ╰ V3Score : 5.3 
│                             ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-54515 
│                             │                  ├ [1]: https://github.com/FasterXML/jackson-databind 
│                             │                  ├ [2]: https://github.com/FasterXML/jackson-databind/commit/0e
│                             │                  │      1b0b211f7a53baa62ba2f4c9bd006c7bf4d5fa 
│                             │                  ├ [3]: https://github.com/FasterXML/jackson-databind/issues/5962 
│                             │                  ├ [4]: https://github.com/FasterXML/jackson-databind/issues/5964 
│                             │                  ├ [5]: https://github.com/FasterXML/jackson-databind/security/
│                             │                  │      advisories/GHSA-5jmj-h7xm-6q6v 
│                             │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2026-54515 
│                             │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2026-54515 
│                             ├ PublishedDate   : 2026-06-23T21:17:02.597Z 
│                             ╰ LastModifiedDate: 2026-06-29T13:38:59.057Z 
╰ [2] ╭ Target         : usr/bin/pebble 
      ├ Class          : lang-pkgs 
      ├ Type           : gobinary 
      ├ Packages        
      ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-25681 
                        │      ├ VendorIDs        ─ [0]: GO-2026-5029 
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.55.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                        │      │                  │         e5814b990e4a375056a9 
                        │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                        │      │                            734c64e0c01604915e58 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-25681 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:f6b1b27fa7dd9d90f636031e5bcc31945a32fe5f53d2890f41a4a
                        │      │                   2cecd4b19e6 
                        │      ├ Title           : golang.org/x/net/html: golang.org/x/net/html: Arbitrary code
                        │      │                    execution via Cross-Site Scripting 
                        │      ├ Description     : Parsing arbitrary HTML which is then rendered using Render
                        │      │                   can result in an unexpected HTML tree. This can be leveraged
                        │      │                    to execute XSS attacks in applications that attempt to
                        │      │                   sanitize input HTML before rendering. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs           ─ [0]: CWE-1021 
                        │      ├ VendorSeverity   ╭ alma       : 3 
                        │      │                  ├ amazon     : 3 
                        │      │                  ├ azure      : 2 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ redhat     : 3 
                        │      │                  ╰ rocky      : 3 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 8.1 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:34357 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-25681 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2466505 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2466507 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2467822 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2480756 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2480761 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2484207 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2480680 
                        │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2480681 
                        │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2480685 
                        │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2480688 
                        │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2480757 
                        │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2480761 
                        │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2493620 
                        │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-25681 
                        │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-27136 
                        │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-39829 
                        │      │                  ├ [18]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-39832 
                        │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-39835 
                        │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-42508 
                        │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-57231 
                        │      │                  ├ [22]: https://errata.almalinux.org/10/ALSA-2026-34357.html 
                        │      │                  ├ [23]: https://errata.rockylinux.org/RLSA-2026:37123 
                        │      │                  ├ [24]: https://go.dev/cl/781703 
                        │      │                  ├ [25]: https://go.dev/issue/79574 
                        │      │                  ├ [26]: https://groups.google.com/g/golang-announce/c/iI-mYSI
                        │      │                  │       0lu8 
                        │      │                  ├ [27]: https://linux.oracle.com/cve/CVE-2026-25681.html 
                        │      │                  ├ [28]: https://linux.oracle.com/errata/ELSA-2026-37123.html 
                        │      │                  ├ [29]: https://nvd.nist.gov/vuln/detail/CVE-2026-25681 
                        │      │                  ├ [30]: https://pkg.go.dev/vuln/GO-2026-5029 
                        │      │                  ╰ [31]: https://www.cve.org/CVERecord?id=CVE-2026-25681 
                        │      ├ PublishedDate   : 2026-05-22T16:16:19.863Z 
                        │      ╰ LastModifiedDate: 2026-06-17T10:25:03.343Z 
                        ├ [1]  ╭ VulnerabilityID : CVE-2026-27136 
                        │      ├ VendorIDs        ─ [0]: GO-2026-5030 
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.55.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                        │      │                  │         e5814b990e4a375056a9 
                        │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                        │      │                            734c64e0c01604915e58 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27136 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:2ae082c6b578fe2dbe7a444d3e32256ec6b99af46d4377d6ed9ae
                        │      │                   2884da7c030 
                        │      ├ Title           : golang.org/x/net/html: golang: golang.org/x/net/html:
                        │      │                   Cross-Site Scripting via HTML parsing bypass 
                        │      ├ Description     : Parsing arbitrary HTML which is then rendered using Render
                        │      │                   can result in an unexpected HTML tree. This can be leveraged
                        │      │                    to execute XSS attacks in applications that attempt to
                        │      │                   sanitize input HTML before rendering. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs           ─ [0]: CWE-1021 
                        │      ├ VendorSeverity   ╭ alma       : 3 
                        │      │                  ├ amazon     : 3 
                        │      │                  ├ azure      : 2 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ redhat     : 3 
                        │      │                  ╰ rocky      : 3 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 8.1 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:37123 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-27136 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2480680 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2480681 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2480685 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2480688 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2480757 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2480761 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/2493620 
                        │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2480680 
                        │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2480681 
                        │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2480685 
                        │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2480688 
                        │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2480757 
                        │      │                  ├ [14]: https://bugzilla.redhat.com/show_bug.cgi?id=2480761 
                        │      │                  ├ [15]: https://bugzilla.redhat.com/show_bug.cgi?id=2493620 
                        │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-25681 
                        │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-27136 
                        │      │                  ├ [18]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-39829 
                        │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-39832 
                        │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-39835 
                        │      │                  ├ [21]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-42508 
                        │      │                  ├ [22]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-57231 
                        │      │                  ├ [23]: https://errata.almalinux.org/9/ALSA-2026-37123.html 
                        │      │                  ├ [24]: https://errata.rockylinux.org/RLSA-2026:37123 
                        │      │                  ├ [25]: https://go.dev/cl/781685 
                        │      │                  ├ [26]: https://go.dev/issue/79575 
                        │      │                  ├ [27]: https://groups.google.com/g/golang-announce/c/iI-mYSI
                        │      │                  │       0lu8 
                        │      │                  ├ [28]: https://linux.oracle.com/cve/CVE-2026-27136.html 
                        │      │                  ├ [29]: https://linux.oracle.com/errata/ELSA-2026-37123.html 
                        │      │                  ├ [30]: https://nvd.nist.gov/vuln/detail/CVE-2026-27136 
                        │      │                  ├ [31]: https://pkg.go.dev/vuln/GO-2026-5030 
                        │      │                  ╰ [32]: https://www.cve.org/CVERecord?id=CVE-2026-27136 
                        │      ├ PublishedDate   : 2026-05-22T16:16:20.087Z 
                        │      ╰ LastModifiedDate: 2026-06-17T10:26:43.803Z 
                        ├ [2]  ╭ VulnerabilityID : CVE-2026-33814 
                        │      ├ VendorIDs        ─ [0]: GO-2026-4918 
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.53.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                        │      │                  │         e5814b990e4a375056a9 
                        │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                        │      │                            734c64e0c01604915e58 
                        │      ├ SeveritySource  : nvd 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-33814 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:0b2be82e95ff1729ddbce261a005aa955079e9b80945557c091b7
                        │      │                   55363968a69 
                        │      ├ Title           : net/http/internal/http2: golang: golang.org/x/net: Go
                        │      │                   HTTP/2: Denial of Service via malformed
                        │      │                   SETTINGS_MAX_FRAME_SIZE frame 
                        │      ├ Description     : When processing HTTP/2 SETTINGS frames, transport will enter
                        │      │                    an infinite loop of writing CONTINUATION frames if it
                        │      │                   receives a SETTINGS_MAX_FRAME_SIZE with a value of 0. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs           ╭ [0]: CWE-835 
                        │      │                  ╰ [1]: CWE-606 
                        │      ├ VendorSeverity   ╭ amazon     : 3 
                        │      │                  ├ azure      : 2 
                        │      │                  ├ bitnami    : 3 
                        │      │                  ├ nvd        : 3 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ photon     : 3 
                        │      │                  ├ redhat     : 3 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ├ nvd     ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                  │         │           N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
                        │      │                            │           N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:23262 
                        │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:23264 
                        │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2026:33120 
                        │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2026:33123 
                        │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2026:33142 
                        │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2026:33150 
                        │      │                  ├ [6] : https://access.redhat.com/errata/RHSA-2026:34342 
                        │      │                  ├ [7] : https://access.redhat.com/errata/RHSA-2026:37387 
                        │      │                  ├ [8] : https://access.redhat.com/security/cve/CVE-2026-33814 
                        │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2467815 
                        │      │                  ├ [10]: https://github.com/golang/go/issues/78476 
                        │      │                  ├ [11]: https://go-review.googlesource.com/c/go/+/761581 
                        │      │                  ├ [12]: https://go-review.googlesource.com/c/net/+/761640 
                        │      │                  ├ [13]: https://go.dev/cl/761581 
                        │      │                  ├ [14]: https://go.dev/cl/761640 
                        │      │                  ├ [15]: https://go.dev/issue/78476 
                        │      │                  ├ [16]: https://groups.google.com/g/golang-announce/c/qcCIEXs
                        │      │                  │       o47M 
                        │      │                  ├ [17]: https://linux.oracle.com/cve/CVE-2026-33814.html 
                        │      │                  ├ [18]: https://linux.oracle.com/errata/ELSA-2026-22121.html 
                        │      │                  ├ [19]: https://nvd.nist.gov/vuln/detail/CVE-2026-33814 
                        │      │                  ├ [20]: https://pkg.go.dev/vuln/GO-2026-4918 
                        │      │                  ├ [21]: https://security.access.redhat.com/data/csaf/v2/vex/2
                        │      │                  │       026/cve-2026-33814.json 
                        │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-8430-1 
                        │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-8471-1 
                        │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-8472-1 
                        │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-8473-1 
                        │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2026-33814 
                        │      ├ PublishedDate   : 2026-05-07T20:16:42.88Z 
                        │      ╰ LastModifiedDate: 2026-07-20T12:18:43.933Z 
                        ├ [3]  ╭ VulnerabilityID : CVE-2026-39821 
                        │      ├ VendorIDs        ─ [0]: GO-2026-5026 
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.55.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                        │      │                  │         e5814b990e4a375056a9 
                        │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                        │      │                            734c64e0c01604915e58 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-39821 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:ff36c9f8a7d7cdf483a19aeb75f409cb0523507c3b5845132a028
                        │      │                   55c3c75d473 
                        │      ├ Title           : golang.org/x/net/idna: golang: net/http:
                        │      │                   golang.org/x/net/idna: Privilege escalation via incorrect
                        │      │                   Punycode label processing 
                        │      ├ Description     : The ToASCII and ToUnicode functions incorrectly accept
                        │      │                   Punycode-encoded labels that decode to an ASCII-only label.
                        │      │                   For example, ToUnicode("xn--example-.com") incorrectly
                        │      │                   returns the name "example.com" rather than an error. This
                        │      │                   behavior can lead to privilege escalation in programs using
                        │      │                   the idna package. For example, a program which performs
                        │      │                   privilege checks on the ASCII hostname may reject
                        │      │                   "example.com" but permit "xn--example-.com". If that program
                        │      │                    subsequently converts the ASCII hostname to Unicode, it
                        │      │                   will inadvertently permits access to the Unicode name
                        │      │                   "example.com". 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs           ─ [0]: CWE-1289 
                        │      ├ VendorSeverity   ╭ alma       : 3 
                        │      │                  ├ amazon     : 3 
                        │      │                  ├ azure      : 4 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ redhat     : 3 
                        │      │                  ├ rocky      : 3 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 8.2 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:23262 
                        │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:23264 
                        │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2026:26546 
                        │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2026:26547 
                        │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2026:30650 
                        │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2026:30651 
                        │      │                  ├ [6] : https://access.redhat.com/errata/RHSA-2026:30853 
                        │      │                  ├ [7] : https://access.redhat.com/errata/RHSA-2026:30854 
                        │      │                  ├ [8] : https://access.redhat.com/errata/RHSA-2026:30855 
                        │      │                  ├ [9] : https://access.redhat.com/errata/RHSA-2026:33155 
                        │      │                  ├ [10]: https://access.redhat.com/errata/RHSA-2026:33160 
                        │      │                  ├ [11]: https://access.redhat.com/errata/RHSA-2026:33163 
                        │      │                  ├ [12]: https://access.redhat.com/errata/RHSA-2026:33173 
                        │      │                  ├ [13]: https://access.redhat.com/errata/RHSA-2026:33183 
                        │      │                  ├ [14]: https://access.redhat.com/errata/RHSA-2026:33524 
                        │      │                  ├ [15]: https://access.redhat.com/errata/RHSA-2026:33531 
                        │      │                  ├ [16]: https://access.redhat.com/errata/RHSA-2026:34342 
                        │      │                  ├ [17]: https://access.redhat.com/errata/RHSA-2026:34357 
                        │      │                  ├ [18]: https://access.redhat.com/errata/RHSA-2026:34359 
                        │      │                  ├ [19]: https://access.redhat.com/errata/RHSA-2026:34364 
                        │      │                  ├ [20]: https://access.redhat.com/errata/RHSA-2026:34789 
                        │      │                  ├ [21]: https://access.redhat.com/errata/RHSA-2026:35826 
                        │      │                  ├ [22]: https://access.redhat.com/errata/RHSA-2026:35827 
                        │      │                  ├ [23]: https://access.redhat.com/errata/RHSA-2026:35828 
                        │      │                  ├ [24]: https://access.redhat.com/errata/RHSA-2026:35829 
                        │      │                  ├ [25]: https://access.redhat.com/errata/RHSA-2026:35830 
                        │      │                  ├ [26]: https://access.redhat.com/errata/RHSA-2026:35831 
                        │      │                  ├ [27]: https://access.redhat.com/errata/RHSA-2026:35993 
                        │      │                  ├ [28]: https://access.redhat.com/errata/RHSA-2026:35994 
                        │      │                  ├ [29]: https://access.redhat.com/errata/RHSA-2026:36105 
                        │      │                  ├ [30]: https://access.redhat.com/errata/RHSA-2026:36167 
                        │      │                  ├ [31]: https://access.redhat.com/errata/RHSA-2026:36207 
                        │      │                  ├ [32]: https://access.redhat.com/errata/RHSA-2026:36648 
                        │      │                  ├ [33]: https://access.redhat.com/errata/RHSA-2026:36651 
                        │      │                  ├ [34]: https://access.redhat.com/errata/RHSA-2026:36796 
                        │      │                  ├ [35]: https://access.redhat.com/errata/RHSA-2026:36797 
                        │      │                  ├ [36]: https://access.redhat.com/errata/RHSA-2026:36808 
                        │      │                  ├ [37]: https://access.redhat.com/errata/RHSA-2026:36820 
                        │      │                  ├ [38]: https://access.redhat.com/errata/RHSA-2026:36883 
                        │      │                  ├ [39]: https://access.redhat.com/errata/RHSA-2026:37387 
                        │      │                  ├ [40]: https://access.redhat.com/errata/RHSA-2026:37435 
                        │      │                  ├ [41]: https://access.redhat.com/errata/RHSA-2026:37436 
                        │      │                  ├ [42]: https://access.redhat.com/errata/RHSA-2026:38995 
                        │      │                  ├ [43]: https://access.redhat.com/errata/RHSA-2026:39005 
                        │      │                  ├ [44]: https://access.redhat.com/errata/RHSA-2026:39573 
                        │      │                  ├ [45]: https://access.redhat.com/errata/RHSA-2026:39879 
                        │      │                  ├ [46]: https://access.redhat.com/errata/RHSA-2026:40118 
                        │      │                  ├ [47]: https://access.redhat.com/errata/RHSA-2026:40262 
                        │      │                  ├ [48]: https://access.redhat.com/errata/RHSA-2026:40945 
                        │      │                  ├ [49]: https://access.redhat.com/errata/RHSA-2026:41019 
                        │      │                  ├ [50]: https://access.redhat.com/errata/RHSA-2026:41030 
                        │      │                  ├ [51]: https://access.redhat.com/errata/RHSA-2026:41031 
                        │      │                  ├ [52]: https://access.redhat.com/errata/RHSA-2026:41036 
                        │      │                  ├ [53]: https://access.redhat.com/errata/RHSA-2026:41055 
                        │      │                  ├ [54]: https://access.redhat.com/errata/RHSA-2026:41066 
                        │      │                  ├ [55]: https://access.redhat.com/errata/RHSA-2026:41930 
                        │      │                  ├ [56]: https://access.redhat.com/security/cve/CVE-2026-39821 
                        │      │                  ├ [57]: https://bugzilla.redhat.com/2480756 
                        │      │                  ├ [58]: https://bugzilla.redhat.com/show_bug.cgi?id=2480756 
                        │      │                  ├ [59]: https://bugzilla.redhat.com/show_bug.cgi?id=2498152 
                        │      │                  ├ [60]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-39821 
                        │      │                  ├ [61]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-39822 
                        │      │                  ├ [62]: https://errata.almalinux.org/10/ALSA-2026-37436.html 
                        │      │                  ├ [63]: https://errata.rockylinux.org/RLSA-2026:37435 
                        │      │                  ├ [64]: https://github.com/golang/go/issues/78760 
                        │      │                  ├ [65]: https://go.dev/cl/767220 
                        │      │                  ├ [66]: https://go.dev/issue/78760 
                        │      │                  ├ [67]: https://groups.google.com/g/golang-announce/c/iI-mYSI
                        │      │                  │       0lu8 
                        │      │                  ├ [68]: https://linux.oracle.com/cve/CVE-2026-39821.html 
                        │      │                  ├ [69]: https://linux.oracle.com/errata/ELSA-2026-38995.html 
                        │      │                  ├ [70]: https://nvd.nist.gov/vuln/detail/CVE-2026-39821 
                        │      │                  ├ [71]: https://pkg.go.dev/vuln/GO-2026-5026 
                        │      │                  ├ [72]: https://security.access.redhat.com/data/csaf/v2/vex/2
                        │      │                  │       026/cve-2026-39821.json 
                        │      │                  ├ [73]: https://ubuntu.com/security/notices/USN-8416-1 
                        │      │                  ╰ [74]: https://www.cve.org/CVERecord?id=CVE-2026-39821 
                        │      ├ PublishedDate   : 2026-05-22T16:16:20.41Z 
                        │      ╰ LastModifiedDate: 2026-07-20T12:18:53.62Z 
                        ├ [4]  ╭ VulnerabilityID : CVE-2025-47911 
                        │      ├ VendorIDs        ─ [0]: GO-2026-4440 
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.45.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                        │      │                  │         e5814b990e4a375056a9 
                        │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                        │      │                            734c64e0c01604915e58 
                        │      ├ SeveritySource  : nvd 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-47911 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:6eccf98d61c85ac5aa31c6a56f9a15fa0923c320b71a95cf077f4
                        │      │                   10013368488 
                        │      ├ Title           : golang.org/x/net/html: Quadratic parsing complexity in
                        │      │                   golang.org/x/net/html 
                        │      ├ Description     : The html.Parse function in golang.org/x/net/html has
                        │      │                   quadratic parsing complexity when processing certain inputs,
                        │      │                    which can lead to denial of service (DoS) if an attacker
                        │      │                   provides specially crafted HTML content. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ VendorSeverity   ╭ amazon     : 2 
                        │      │                  ├ azure      : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                  │        │           /A:L 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                           │           /A:L 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2025-47911 
                        │      │                  ├ [1] : https://github.com/golang/go/issues/75682 
                        │      │                  ├ [2] : https://github.com/golang/vulndb/issues/4440 
                        │      │                  ├ [3] : https://go.dev/cl/709876 
                        │      │                  ├ [4] : https://groups.google.com/g/golang-announce/c/jnQcOYp
                        │      │                  │       iR2c 
                        │      │                  ├ [5] : https://nvd.nist.gov/vuln/detail/CVE-2025-47911 
                        │      │                  ├ [6] : https://pkg.go.dev/vuln/GO-2026-4440 
                        │      │                  ├ [7] : https://ubuntu.com/security/notices/USN-8089-1 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-8089-2 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-8089-3 
                        │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2025-47911 
                        │      ├ PublishedDate   : 2026-02-05T18:16:09.893Z 
                        │      ╰ LastModifiedDate: 2026-06-17T09:28:50.07Z 
                        ├ [5]  ╭ VulnerabilityID : CVE-2025-58190 
                        │      ├ VendorIDs        ─ [0]: GO-2026-4441 
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.45.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                        │      │                  │         e5814b990e4a375056a9 
                        │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                        │      │                            734c64e0c01604915e58 
                        │      ├ SeveritySource  : nvd 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-58190 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:feebea63a8429f73742e60064527a3c9c32efbf8a45a7821fb29d
                        │      │                   a6663fa7a67 
                        │      ├ Title           : golang.org/x/net/html: Infinite parsing loop in
                        │      │                   golang.org/x/net 
                        │      ├ Description     : The html.Parse function in golang.org/x/net/html has an
                        │      │                   infinite parsing loop when processing certain inputs, which
                        │      │                   can lead to denial of service (DoS) if an attacker provides
                        │      │                   specially crafted HTML content. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-835 
                        │      ├ VendorSeverity   ╭ amazon     : 2 
                        │      │                  ├ azure      : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │      │                  │        │           /A:L 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N
                        │      │                           │           /A:L 
                        │      │                           ╰ V3Score : 4.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2025-58190 
                        │      │                  ├ [1] : https://github.com/golang/go/issues/70179 
                        │      │                  ├ [2] : https://github.com/golang/vulndb/issues/4441 
                        │      │                  ├ [3] : https://go.dev/cl/709875 
                        │      │                  ├ [4] : https://groups.google.com/g/golang-announce/c/jnQcOYp
                        │      │                  │       iR2c 
                        │      │                  ├ [5] : https://nvd.nist.gov/vuln/detail/CVE-2025-58190 
                        │      │                  ├ [6] : https://pkg.go.dev/vuln/GO-2026-4441 
                        │      │                  ├ [7] : https://ubuntu.com/security/notices/USN-8089-1 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-8089-2 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-8089-3 
                        │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2025-58190 
                        │      ├ PublishedDate   : 2026-02-05T18:16:10.027Z 
                        │      ╰ LastModifiedDate: 2026-06-17T09:44:02.557Z 
                        ├ [6]  ╭ VulnerabilityID : CVE-2026-25680 
                        │      ├ VendorIDs        ─ [0]: GO-2026-5028 
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.55.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                        │      │                  │         e5814b990e4a375056a9 
                        │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                        │      │                            734c64e0c01604915e58 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-25680 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:a00a8b6e438202de731ab73b9a3da98295e147921e5af11a147f9
                        │      │                   7e8bb3f3bd7 
                        │      ├ Title           : golang.org/x/net/html: golang.org/x/net/html: Denial of
                        │      │                   Service due to excessive HTML parsing 
                        │      ├ Description     : Parsing arbitrary HTML can consume excessive CPU time,
                        │      │                   possibly leading to denial of service. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-400 
                        │      ├ VendorSeverity   ╭ amazon: 3 
                        │      │                  ├ azure : 2 
                        │      │                  ╰ redhat: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N
                        │      │                           │           /A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-25680 
                        │      │                  ├ [1]: https://go.dev/cl/781702 
                        │      │                  ├ [2]: https://go.dev/issue/79573 
                        │      │                  ├ [3]: https://groups.google.com/g/golang-announce/c/iI-mYSI0
                        │      │                  │      lu8 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-25680 
                        │      │                  ├ [5]: https://pkg.go.dev/vuln/GO-2026-5028 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-25680 
                        │      ├ PublishedDate   : 2026-05-22T16:16:19.753Z 
                        │      ╰ LastModifiedDate: 2026-06-17T10:25:03.14Z 
                        ├ [7]  ╭ VulnerabilityID : CVE-2026-42502 
                        │      ├ VendorIDs        ─ [0]: GO-2026-5027 
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.55.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                        │      │                  │         e5814b990e4a375056a9 
                        │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                        │      │                            734c64e0c01604915e58 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42502 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:0cd6bb7870796f6f3f8eee6bb4d3e56e36e4f877dd1a831a3a905
                        │      │                   75a26545099 
                        │      ├ Title           : golang.org/x/net/html: golang: golang.org/x/net/html:
                        │      │                   Cross-Site Scripting via unexpected HTML tree rendering 
                        │      ├ Description     : Parsing arbitrary HTML which is then rendered using Render
                        │      │                   can result in an unexpected HTML tree. This can be leveraged
                        │      │                    to execute XSS attacks in applications that attempt to
                        │      │                   sanitize input HTML before rendering. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-1021 
                        │      ├ VendorSeverity   ╭ amazon: 3 
                        │      │                  ├ azure : 2 
                        │      │                  ╰ redhat: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 6.1 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-42502 
                        │      │                  ├ [1]: https://go.dev/cl/781701 
                        │      │                  ├ [2]: https://go.dev/issue/79572 
                        │      │                  ├ [3]: https://groups.google.com/g/golang-announce/c/iI-mYSI0
                        │      │                  │      lu8 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-42502 
                        │      │                  ├ [5]: https://pkg.go.dev/vuln/GO-2026-5027 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-42502 
                        │      ├ PublishedDate   : 2026-05-22T16:16:20.587Z 
                        │      ╰ LastModifiedDate: 2026-06-17T10:47:56.593Z 
                        ├ [8]  ╭ VulnerabilityID : CVE-2026-42506 
                        │      ├ VendorIDs        ─ [0]: GO-2026-5025 
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.55.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                        │      │                  │         e5814b990e4a375056a9 
                        │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                        │      │                            734c64e0c01604915e58 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42506 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:a640cc5480971f363f477fc6fbe61279c60d54bc3bb71b01a1b11
                        │      │                   8444c79f627 
                        │      ├ Title           : golang.org/x/net/html: golang.org/x/net/html: Cross-Site
                        │      │                   Scripting (XSS) via arbitrary HTML parsing 
                        │      ├ Description     : Parsing arbitrary HTML which is then rendered using Render
                        │      │                   can result in an unexpected HTML tree. This can be leveraged
                        │      │                    to execute XSS attacks in applications that attempt to
                        │      │                   sanitize input HTML before rendering. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-79 
                        │      ├ VendorSeverity   ╭ amazon: 3 
                        │      │                  ├ azure : 2 
                        │      │                  ╰ redhat: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L
                        │      │                           │           /A:N 
                        │      │                           ╰ V3Score : 5.4 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-42506 
                        │      │                  ├ [1]: https://go.dev/cl/781700 
                        │      │                  ├ [2]: https://go.dev/issue/79571 
                        │      │                  ├ [3]: https://groups.google.com/g/golang-announce/c/iI-mYSI0
                        │      │                  │      lu8 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-42506 
                        │      │                  ├ [5]: https://pkg.go.dev/vuln/GO-2026-5025 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-42506 
                        │      ├ PublishedDate   : 2026-05-22T16:16:20.803Z 
                        │      ╰ LastModifiedDate: 2026-06-17T10:47:56.993Z 
                        ├ [9]  ╭ VulnerabilityID : CVE-2026-46600 
                        │      ├ VendorIDs        ─ [0]: GO-2026-5942 
                        │      ├ PkgID           : golang.org/x/net@v0.40.0 
                        │      ├ PkgName         : golang.org/x/net 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/net@v0.40.0 
                        │      │                  ╰ UID : b8870a94f706b324 
                        │      ├ InstalledVersion: v0.40.0 
                        │      ├ FixedVersion    : 0.56.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                        │      │                  │         e5814b990e4a375056a9 
                        │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                        │      │                            734c64e0c01604915e58 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46600 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:7aeea3578927aab48584aa44b362895c3f3d0a9238e1fa75aa85a
                        │      │                   04bc09acb06 
                        │      ├ Title           : Parsing an invalid SVCB or HTTPS RR can panic in
                        │      │                   golang.org/x/net/dns/dnsmessage 
                        │      ├ Description     : Parsing an invalid SVCB or HTTPS RR can panic when the size
                        │      │                   of a parameter value overflows the message buffer. 
                        │      ├ Severity        : UNKNOWN 
                        │      ╰ References       ╭ [0]: https://go.dev/cl/786345 
                        │                         ├ [1]: https://go.dev/issue/79795 
                        │                         ╰ [2]: https://pkg.go.dev/vuln/GO-2026-5942 
                        ├ [10] ╭ VulnerabilityID : CVE-2026-39824 
                        │      ├ VendorIDs        ─ [0]: GO-2026-5024 
                        │      ├ PkgID           : golang.org/x/sys@v0.33.0 
                        │      ├ PkgName         : golang.org/x/sys 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/golang.org/x/sys@v0.33.0 
                        │      │                  ╰ UID : a350d4cc028089d4 
                        │      ├ InstalledVersion: v0.33.0 
                        │      ├ FixedVersion    : 0.44.0 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                        │      │                  │         e5814b990e4a375056a9 
                        │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                        │      │                            734c64e0c01604915e58 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-39824 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:15d46b374a478d9fd6e9b59feb618e63bc557491fa39e538a2cb2
                        │      │                   b187dd765dc 
                        │      ├ Title           : Invoking integer overflow in NewNTUnicodeString in
                        │      │                   golang.org/x/sys/windows 
                        │      ├ Description     : NewNTUnicodeString does not check for string length
                        │      │                   overflow. When provided with a string that overflows the
                        │      │                   maximum size of a NTUnicodeString (a 16-bit number of
                        │      │                   bytes), it returns a truncated string rather than an
                        │      │                   error. 
                        │      ├ Severity        : UNKNOWN 
                        │      ├ CweIDs           ─ [0]: CWE-190 
                        │      ├ References       ╭ [0]: https://go.dev/cl/770080 
                        │      │                  ├ [1]: https://go.dev/issue/78916 
                        │      │                  ├ [2]: https://groups.google.com/g/golang-announce/c/6MMI8Lj-
                        │      │                  │      Atg 
                        │      │                  ╰ [3]: https://pkg.go.dev/vuln/GO-2026-5024 
                        │      ├ PublishedDate   : 2026-05-22T20:16:33.057Z 
                        │      ╰ LastModifiedDate: 2026-06-17T10:42:38.62Z 
                        ├ [11] ╭ VulnerabilityID : CVE-2026-39822 
                        │      ├ VendorIDs        ─ [0]: GO-2026-4970 
                        │      ├ PkgID           : stdlib@v1.26.4 
                        │      ├ PkgName         : stdlib 
                        │      ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.4 
                        │      │                  ╰ UID : 364846ec8fe81bdc 
                        │      ├ InstalledVersion: v1.26.4 
                        │      ├ FixedVersion    : 1.25.12, 1.26.5, 1.27.0-rc.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                        │      │                  │         e5814b990e4a375056a9 
                        │      │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                        │      │                            734c64e0c01604915e58 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-39822 
                        │      ├ DataSource       ╭ ID  : govulndb 
                        │      │                  ├ Name: The Go Vulnerability Database 
                        │      │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │      ├ Fingerprint     : sha256:9347f0dc5989b7bbd341cbbf41999738881e39e22497b0bf0db91
                        │      │                   eb1a99a8265 
                        │      ├ Title           : os: golang: Go os.Root: Symlink following vulnerability
                        │      │                   allows directory traversal 
                        │      ├ Description     : On Unix systems, opening a file in an os.Root improperly
                        │      │                   follows symlinks to locations outside of the Root when the
                        │      │                   final path component of the a path is a symbolic link and
                        │      │                   the path ends in /. For example, 'root.Open("symlink/")'
                        │      │                   will open "symlink" even when "symlink" is a symbolic link
                        │      │                   pointing outside of the root. 
                        │      ├ Severity        : HIGH 
                        │      ├ CweIDs           ─ [0]: CWE-61 
                        │      ├ VendorSeverity   ╭ alma       : 3 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ bitnami    : 3 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ redhat     : 3 
                        │      │                  ╰ rocky      : 3 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:
                        │      │                  │         │           H/A:H 
                        │      │                  │         ╰ V3Score : 7.8 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:
                        │      │                            │           H/A:H 
                        │      │                            ╰ V3Score : 7.8 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:38495 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-39822 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2498152 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2498152 
                        │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
                        │      │                  │       26-39822 
                        │      │                  ├ [5] : https://errata.almalinux.org/10/ALSA-2026-38495.html 
                        │      │                  ├ [6] : https://errata.rockylinux.org/RLSA-2026:38878 
                        │      │                  ├ [7] : https://go.dev/cl/797880 
                        │      │                  ├ [8] : https://go.dev/issue/79005 
                        │      │                  ├ [9] : https://groups.google.com/g/golang-announce/c/OrmQE_Y
                        │      │                  │       p5Sc 
                        │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2026-39822.html 
                        │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2026-38995.html 
                        │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2026-39822 
                        │      │                  ├ [13]: https://pkg.go.dev/vuln/GO-2026-4970 
                        │      │                  ╰ [14]: https://www.cve.org/CVERecord?id=CVE-2026-39822 
                        │      ├ PublishedDate   : 2026-07-08T17:17:21.31Z 
                        │      ╰ LastModifiedDate: 2026-07-13T14:54:26.317Z 
                        ╰ [12] ╭ VulnerabilityID : CVE-2026-42505 
                               ├ VendorIDs        ─ [0]: GO-2026-5856 
                               ├ PkgID           : stdlib@v1.26.4 
                               ├ PkgName         : stdlib 
                               ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.4 
                               │                  ╰ UID : 364846ec8fe81bdc 
                               ├ InstalledVersion: v1.26.4 
                               ├ FixedVersion    : 1.25.12, 1.26.5, 1.27.0-rc.2 
                               ├ Status          : fixed 
                               ├ Layer            ╭ Digest: sha256:e999bc889c1855050f868b28fd7724842d3f1d07f73b
                               │                  │         e5814b990e4a375056a9 
                               │                  ╰ DiffID: sha256:7af2eea91467c3c50bea91da8ebbbdab8c16e85bb434
                               │                            734c64e0c01604915e58 
                               ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42505 
                               ├ DataSource       ╭ ID  : govulndb 
                               │                  ├ Name: The Go Vulnerability Database 
                               │                  ╰ URL : https://pkg.go.dev/vuln/ 
                               ├ Fingerprint     : sha256:d33f5bb94710a1c3f34c3cb59020f87cac4591a1c63495e81f483
                               │                   8673c74c288 
                               ├ Title           : crypto/tls: golang: Go crypto/tls: Information disclosure in
                               │                    Encrypted Client Hello 
                               ├ Description     : Handshakes which used Encrypted Client Hello could be
                               │                   de-anonymized by a passive network observer due to a
                               │                   disclosure of pre-shared key identities in the unencrypted
                               │                   client hello. 
                               ├ Severity        : MEDIUM 
                               ├ CweIDs           ─ [0]: CWE-201 
                               ├ VendorSeverity   ╭ amazon : 2 
                               │                  ├ bitnami: 2 
                               │                  ╰ redhat : 2 
                               ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
                               │                  │         │           N/A:N 
                               │                  │         ╰ V3Score : 5.3 
                               │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
                               │                            │           N/A:N 
                               │                            ╰ V3Score : 5.3 
                               ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-42505 
                               │                  ├ [1]: https://go.dev/cl/775960 
                               │                  ├ [2]: https://go.dev/issue/79282 
                               │                  ├ [3]: https://groups.google.com/g/golang-announce/c/OrmQE_Yp
                               │                  │      5Sc 
                               │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-42505 
                               │                  ├ [5]: https://pkg.go.dev/vuln/GO-2026-5856 
                               │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-42505 
                               ├ PublishedDate   : 2026-07-08T17:17:21.497Z 
                               ╰ LastModifiedDate: 2026-07-13T17:05:36.303Z 
```
