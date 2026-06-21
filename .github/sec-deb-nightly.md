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
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0f8969e6b38700db39df880ecdb5abb8e191bac70764237539553
│                       │      │                   1afc69ca312 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : bsdutils@1:2.41.3-3ubuntu2 
│                       │      ├ PkgName         : bsdutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/bsdutils@2.41.3-3ubuntu2?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : 35a8976635e225e2 
│                       │      ├ InstalledVersion: 1:2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:eba5ccdfd15d397499a92db2a1d09f0bf7cb60507ef15b0bef916
│                       │      │                   8936310f0c8 
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
│                       │      ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : libblkid1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libblkid1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libblkid1@2.41.3-3ubuntu2?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : f63a0a78e3cac3a3 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3f3a64ae190d99e68f02c4d009d537489bb513e8debd5d87195ee
│                       │      │                   c4cc9238aef 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : libblkid1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libblkid1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libblkid1@2.41.3-3ubuntu2?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : f63a0a78e3cac3a3 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ae1cc9396300fdb9b9543306ed274d0451a75439a142d8b6f240a
│                       │      │                   324927a6d62 
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
│                       │      ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-4046 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : aa471766c29fe384 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4046 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:497404d7c9768fed4bbe3942b4e917064fe6b91679c76e2c07238
│                       │      │                   40c6312356c 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:20587 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-4046 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2453117 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2449777 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2449783 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2453117 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [9] : https://errata.almalinux.org/8/ALSA-2026-20587.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [11]: https://inbox.sourceware.org/libc-announce/76814edf-c
│                       │      │                  │       f7f-47ec-979d-2dce0a2c76bf@gotplt.org/T/#u 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2026-4046.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2026-50291.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2026-4046 
│                       │      │                  ├ [15]: https://packages.fedoraproject.org/pkgs/glibc/glibc-g
│                       │      │                  │       conv-extra/ 
│                       │      │                  ├ [16]: https://sourceware.org/bugzilla/show_bug.cgi?id=33980 
│                       │      │                  ├ [17]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │      │                  │       f=advisories/GLIBC-SA-2026-0007 
│                       │      │                  ├ [18]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │      │                  │       f=advisories/GLIBC-SA-2026-0007;hb=HEAD 
│                       │      │                  ╰ [19]: https://www.cve.org/CVERecord?id=CVE-2026-4046 
│                       │      ├ PublishedDate   : 2026-03-30T18:16:19.573Z 
│                       │      ╰ LastModifiedDate: 2026-04-20T22:16:23.623Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-4437 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : aa471766c29fe384 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4437 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3a052dd844d38f8cf730320c20cb8c7631aa6f100d6a08936368e
│                       │      │                   9dab4ab3b9c 
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
│                       │      ├ VendorSeverity   ╭ alma  : 2 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ photon: 3 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ├ rocky : 2 
│                       │      │                  ╰ ubuntu: 2 
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
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [10]: https://errata.almalinux.org/10/ALSA-2026-19061.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2026-4437 
│                       │      │                  ├ [13]: https://sourceware.org/bugzilla/show_bug.cgi?id=34014 
│                       │      │                  ├ [14]: https://www.cve.org/CVERecord?id=CVE-2026-4437 
│                       │      │                  ╰ [15]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │      │                          3/2 
│                       │      ├ PublishedDate   : 2026-03-20T20:16:49.477Z 
│                       │      ╰ LastModifiedDate: 2026-04-07T18:41:36.647Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-4438 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : aa471766c29fe384 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4438 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:3df4bfaef52f7176a7e60fa445d0119a887a707553891fec1763a
│                       │      │                   81ca1ba191f 
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
│                       │      ├ VendorSeverity   ╭ alma  : 2 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ├ rocky : 2 
│                       │      │                  ╰ ubuntu: 2 
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
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [10]: https://errata.almalinux.org/10/ALSA-2026-19061.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2026-4438 
│                       │      │                  ├ [13]: https://sourceware.org/bugzilla/show_bug.cgi?id=34015 
│                       │      │                  ├ [14]: https://www.cve.org/CVERecord?id=CVE-2026-4438 
│                       │      │                  ╰ [15]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │      │                          3/2 
│                       │      ├ PublishedDate   : 2026-03-20T20:16:49.623Z 
│                       │      ╰ LastModifiedDate: 2026-04-07T18:40:02.177Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-5435 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : aa471766c29fe384 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5435 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a4a48611569ef3a227abeee0ef9b5b863c598b437bea00cd911ee
│                       │      │                   a3470fc9760 
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
│                       │      │                  ├ [1]: https://inbox.sourceware.org/libc-alpha/cover.17775461
│                       │      │                  │      94.git.fweimer@redhat.com/ 
│                       │      │                  ├ [2]: https://inbox.sourceware.org/libc-announce/7a655d55-27
│                       │      │                  │      6f-41fe-b550-feb3ebb2ce91@redhat.com/T/#u 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-5435 
│                       │      │                  ├ [4]: https://sourceware.org/bugzilla/show_bug.cgi?id=34033 
│                       │      │                  ├ [5]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;f
│                       │      │                  │      =advisories/GLIBC-SA-2026-0011 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-5435 
│                       │      ├ PublishedDate   : 2026-04-28T13:19:22.29Z 
│                       │      ╰ LastModifiedDate: 2026-05-05T17:38:37.03Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-6238 
│                       │      ├ PkgID           : libc-bin@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.43-2ubuntu2?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04 
│                       │      │                  ╰ UID : aa471766c29fe384 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6238 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:65627b69a943563ecb000b80de5ccdca3dd9c1ca7dfbd26383f64
│                       │      │                   5da965b3acb 
│                       │      ├ Title           : glibc: glibc: Application crash or uninitialized memory read
│                       │      │                    via crafted DNS response 
│                       │      ├ Description     : The deprecated functions ns_printrrf, ns_printrr and
│                       │      │                   fp_nquery in the GNU C Library version 2.2 and newer fail to
│                       │      │                    validate the RDATA content against the RDATA length in a
│                       │      │                   DNS response when processing LOC, CERT, TKEY or TSIG
│                       │      │                   records, which may allow an attacker to craft a DNS
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
│                       │      │                  ├ [1]: https://inbox.sourceware.org/libc-alpha/cover.17775461
│                       │      │                  │      94.git.fweimer@redhat.com/ 
│                       │      │                  ├ [2]: https://inbox.sourceware.org/libc-announce/7a655d55-27
│                       │      │                  │      6f-41fe-b550-feb3ebb2ce91@redhat.com/T/#u 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-6238 
│                       │      │                  ├ [4]: https://sourceware.org/bugzilla/show_bug.cgi?id=34069 
│                       │      │                  ├ [5]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;f
│                       │      │                  │      =advisories/GLIBC-SA-2026-0012 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-6238 
│                       │      ├ PublishedDate   : 2026-04-28T19:37:47.523Z 
│                       │      ╰ LastModifiedDate: 2026-05-04T17:57:24.007Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-4046 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 229c678f3865c408 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4046 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e826264dc2e15240ae4aa5cb93e55c9732cdf4467384e93cb8464
│                       │      │                   056d7b550a5 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:20587 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-4046 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2453117 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2449777 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2449783 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2453117 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [9] : https://errata.almalinux.org/8/ALSA-2026-20587.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [11]: https://inbox.sourceware.org/libc-announce/76814edf-c
│                       │      │                  │       f7f-47ec-979d-2dce0a2c76bf@gotplt.org/T/#u 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2026-4046.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2026-50291.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2026-4046 
│                       │      │                  ├ [15]: https://packages.fedoraproject.org/pkgs/glibc/glibc-g
│                       │      │                  │       conv-extra/ 
│                       │      │                  ├ [16]: https://sourceware.org/bugzilla/show_bug.cgi?id=33980 
│                       │      │                  ├ [17]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │      │                  │       f=advisories/GLIBC-SA-2026-0007 
│                       │      │                  ├ [18]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │      │                  │       f=advisories/GLIBC-SA-2026-0007;hb=HEAD 
│                       │      │                  ╰ [19]: https://www.cve.org/CVERecord?id=CVE-2026-4046 
│                       │      ├ PublishedDate   : 2026-03-30T18:16:19.573Z 
│                       │      ╰ LastModifiedDate: 2026-04-20T22:16:23.623Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-4437 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 229c678f3865c408 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4437 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:1c8c86970004dc5bd6a165caa6733a141f58f33f001055cb04969
│                       │      │                   520ebe148c5 
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
│                       │      ├ VendorSeverity   ╭ alma  : 2 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ photon: 3 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ├ rocky : 2 
│                       │      │                  ╰ ubuntu: 2 
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
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [10]: https://errata.almalinux.org/10/ALSA-2026-19061.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2026-4437 
│                       │      │                  ├ [13]: https://sourceware.org/bugzilla/show_bug.cgi?id=34014 
│                       │      │                  ├ [14]: https://www.cve.org/CVERecord?id=CVE-2026-4437 
│                       │      │                  ╰ [15]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │      │                          3/2 
│                       │      ├ PublishedDate   : 2026-03-20T20:16:49.477Z 
│                       │      ╰ LastModifiedDate: 2026-04-07T18:41:36.647Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-4438 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 229c678f3865c408 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4438 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a7f9e4448636ecdbcaf4765b0a39b97915442413800b160444f95
│                       │      │                   a9800651242 
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
│                       │      ├ VendorSeverity   ╭ alma  : 2 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ├ rocky : 2 
│                       │      │                  ╰ ubuntu: 2 
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
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [10]: https://errata.almalinux.org/10/ALSA-2026-19061.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2026-4438 
│                       │      │                  ├ [13]: https://sourceware.org/bugzilla/show_bug.cgi?id=34015 
│                       │      │                  ├ [14]: https://www.cve.org/CVERecord?id=CVE-2026-4438 
│                       │      │                  ╰ [15]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │      │                          3/2 
│                       │      ├ PublishedDate   : 2026-03-20T20:16:49.623Z 
│                       │      ╰ LastModifiedDate: 2026-04-07T18:40:02.177Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-5435 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 229c678f3865c408 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5435 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:05ba4c6b21c3e5c58642ee1d5e142db592ffe6f5847f671dc119e
│                       │      │                   e36e2f908c1 
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
│                       │      │                  ├ [1]: https://inbox.sourceware.org/libc-alpha/cover.17775461
│                       │      │                  │      94.git.fweimer@redhat.com/ 
│                       │      │                  ├ [2]: https://inbox.sourceware.org/libc-announce/7a655d55-27
│                       │      │                  │      6f-41fe-b550-feb3ebb2ce91@redhat.com/T/#u 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-5435 
│                       │      │                  ├ [4]: https://sourceware.org/bugzilla/show_bug.cgi?id=34033 
│                       │      │                  ├ [5]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;f
│                       │      │                  │      =advisories/GLIBC-SA-2026-0011 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-5435 
│                       │      ├ PublishedDate   : 2026-04-28T13:19:22.29Z 
│                       │      ╰ LastModifiedDate: 2026-05-05T17:38:37.03Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-6238 
│                       │      ├ PkgID           : libc-gconv-modules-extra@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc-gconv-modules-extra 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-gconv-modules-extra@2.43-2ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 229c678f3865c408 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6238 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5e1fb4fdbe4c7f54ece994c27d450f2190b3168f0d3da2fa9869b
│                       │      │                   eb51b751a75 
│                       │      ├ Title           : glibc: glibc: Application crash or uninitialized memory read
│                       │      │                    via crafted DNS response 
│                       │      ├ Description     : The deprecated functions ns_printrrf, ns_printrr and
│                       │      │                   fp_nquery in the GNU C Library version 2.2 and newer fail to
│                       │      │                    validate the RDATA content against the RDATA length in a
│                       │      │                   DNS response when processing LOC, CERT, TKEY or TSIG
│                       │      │                   records, which may allow an attacker to craft a DNS
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
│                       │      │                  ├ [1]: https://inbox.sourceware.org/libc-alpha/cover.17775461
│                       │      │                  │      94.git.fweimer@redhat.com/ 
│                       │      │                  ├ [2]: https://inbox.sourceware.org/libc-announce/7a655d55-27
│                       │      │                  │      6f-41fe-b550-feb3ebb2ce91@redhat.com/T/#u 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-6238 
│                       │      │                  ├ [4]: https://sourceware.org/bugzilla/show_bug.cgi?id=34069 
│                       │      │                  ├ [5]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;f
│                       │      │                  │      =advisories/GLIBC-SA-2026-0012 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-6238 
│                       │      ├ PublishedDate   : 2026-04-28T19:37:47.523Z 
│                       │      ╰ LastModifiedDate: 2026-05-04T17:57:24.007Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-4046 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2?arch=amd64&distro=
│                       │      │                  │       ubuntu-26.04 
│                       │      │                  ╰ UID : a6167efe03e34488 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4046 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:541ba96851d56451de7f807191b3056a72214e8c46da30d169f25
│                       │      │                   8b1b6d62d92 
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
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2026:20587 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2026-4046 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2453117 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2449777 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2449783 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2453117 
│                       │      │                  ├ [6] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [9] : https://errata.almalinux.org/8/ALSA-2026-20587.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [11]: https://inbox.sourceware.org/libc-announce/76814edf-c
│                       │      │                  │       f7f-47ec-979d-2dce0a2c76bf@gotplt.org/T/#u 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2026-4046.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2026-50291.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2026-4046 
│                       │      │                  ├ [15]: https://packages.fedoraproject.org/pkgs/glibc/glibc-g
│                       │      │                  │       conv-extra/ 
│                       │      │                  ├ [16]: https://sourceware.org/bugzilla/show_bug.cgi?id=33980 
│                       │      │                  ├ [17]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │      │                  │       f=advisories/GLIBC-SA-2026-0007 
│                       │      │                  ├ [18]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;
│                       │      │                  │       f=advisories/GLIBC-SA-2026-0007;hb=HEAD 
│                       │      │                  ╰ [19]: https://www.cve.org/CVERecord?id=CVE-2026-4046 
│                       │      ├ PublishedDate   : 2026-03-30T18:16:19.573Z 
│                       │      ╰ LastModifiedDate: 2026-04-20T22:16:23.623Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-4437 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2?arch=amd64&distro=
│                       │      │                  │       ubuntu-26.04 
│                       │      │                  ╰ UID : a6167efe03e34488 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4437 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:8648ad670a957936d553d0994a1736e831a29494eab72254dc545
│                       │      │                   f19aa5edf31 
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
│                       │      ├ VendorSeverity   ╭ alma  : 2 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ photon: 3 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ├ rocky : 2 
│                       │      │                  ╰ ubuntu: 2 
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
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [10]: https://errata.almalinux.org/10/ALSA-2026-19061.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2026-4437 
│                       │      │                  ├ [13]: https://sourceware.org/bugzilla/show_bug.cgi?id=34014 
│                       │      │                  ├ [14]: https://www.cve.org/CVERecord?id=CVE-2026-4437 
│                       │      │                  ╰ [15]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │      │                          3/2 
│                       │      ├ PublishedDate   : 2026-03-20T20:16:49.477Z 
│                       │      ╰ LastModifiedDate: 2026-04-07T18:41:36.647Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-4438 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2?arch=amd64&distro=
│                       │      │                  │       ubuntu-26.04 
│                       │      │                  ╰ UID : a6167efe03e34488 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4438 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:08e62cdc12e1ebd6645e6fda15e2dc76afc19f4b5c1858f14548a
│                       │      │                   cb06690c60d 
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
│                       │      ├ VendorSeverity   ╭ alma  : 2 
│                       │      │                  ├ azure : 2 
│                       │      │                  ├ photon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ├ rocky : 2 
│                       │      │                  ╰ ubuntu: 2 
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
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4046 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4437 
│                       │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       26-4438 
│                       │      │                  ├ [10]: https://errata.almalinux.org/10/ALSA-2026-19061.html 
│                       │      │                  ├ [11]: https://errata.rockylinux.org/RLSA-2026:20597 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2026-4438 
│                       │      │                  ├ [13]: https://sourceware.org/bugzilla/show_bug.cgi?id=34015 
│                       │      │                  ├ [14]: https://www.cve.org/CVERecord?id=CVE-2026-4438 
│                       │      │                  ╰ [15]: https://www.openwall.com/lists/oss-security/2026/03/2
│                       │      │                          3/2 
│                       │      ├ PublishedDate   : 2026-03-20T20:16:49.623Z 
│                       │      ╰ LastModifiedDate: 2026-04-07T18:40:02.177Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2026-5435 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2?arch=amd64&distro=
│                       │      │                  │       ubuntu-26.04 
│                       │      │                  ╰ UID : a6167efe03e34488 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-5435 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0240d9e132ba604a6d5aeae06786be51a90e00df5ee13a9e060fb
│                       │      │                   fcd9e964d13 
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
│                       │      │                  ├ [1]: https://inbox.sourceware.org/libc-alpha/cover.17775461
│                       │      │                  │      94.git.fweimer@redhat.com/ 
│                       │      │                  ├ [2]: https://inbox.sourceware.org/libc-announce/7a655d55-27
│                       │      │                  │      6f-41fe-b550-feb3ebb2ce91@redhat.com/T/#u 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-5435 
│                       │      │                  ├ [4]: https://sourceware.org/bugzilla/show_bug.cgi?id=34033 
│                       │      │                  ├ [5]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;f
│                       │      │                  │      =advisories/GLIBC-SA-2026-0011 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-5435 
│                       │      ├ PublishedDate   : 2026-04-28T13:19:22.29Z 
│                       │      ╰ LastModifiedDate: 2026-05-05T17:38:37.03Z 
│                       ├ [18] ╭ VulnerabilityID : CVE-2026-6238 
│                       │      ├ PkgID           : libc6@2.43-2ubuntu2 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.43-2ubuntu2?arch=amd64&distro=
│                       │      │                  │       ubuntu-26.04 
│                       │      │                  ╰ UID : a6167efe03e34488 
│                       │      ├ InstalledVersion: 2.43-2ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-6238 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:2e40a9490188eea07f3a4fceca2dcc6457c7bf56e96997912517d
│                       │      │                   baf3da9402c 
│                       │      ├ Title           : glibc: glibc: Application crash or uninitialized memory read
│                       │      │                    via crafted DNS response 
│                       │      ├ Description     : The deprecated functions ns_printrrf, ns_printrr and
│                       │      │                   fp_nquery in the GNU C Library version 2.2 and newer fail to
│                       │      │                    validate the RDATA content against the RDATA length in a
│                       │      │                   DNS response when processing LOC, CERT, TKEY or TSIG
│                       │      │                   records, which may allow an attacker to craft a DNS
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
│                       │      │                  ├ [1]: https://inbox.sourceware.org/libc-alpha/cover.17775461
│                       │      │                  │      94.git.fweimer@redhat.com/ 
│                       │      │                  ├ [2]: https://inbox.sourceware.org/libc-announce/7a655d55-27
│                       │      │                  │      6f-41fe-b550-feb3ebb2ce91@redhat.com/T/#u 
│                       │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-6238 
│                       │      │                  ├ [4]: https://sourceware.org/bugzilla/show_bug.cgi?id=34069 
│                       │      │                  ├ [5]: https://sourceware.org/git/?p=glibc.git;a=blob_plain;f
│                       │      │                  │      =advisories/GLIBC-SA-2026-0012 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-6238 
│                       │      ├ PublishedDate   : 2026-04-28T19:37:47.523Z 
│                       │      ╰ LastModifiedDate: 2026-05-04T17:57:24.007Z 
│                       ├ [19] ╭ VulnerabilityID : CVE-2025-66382 
│                       │      ├ PkgID           : libexpat1@2.7.4-1 
│                       │      ├ PkgName         : libexpat1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libexpat1@2.7.4-1?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : c17b9d4b5a8b1286 
│                       │      ├ InstalledVersion: 2.7.4-1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-66382 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e3f3520330d3490a902ba6105f41757989ede4819288368273ed1
│                       │      │                   46ab1d57d7e 
│                       │      ├ Title           : libexpat: libexpat: Denial of service via crafted file
│                       │      │                   processing 
│                       │      ├ Description     : In libexpat through 2.7.3, a crafted file with an
│                       │      │                   approximate size of 2 MiB can lead to dozens of seconds of
│                       │      │                   processing time. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-407 
│                       │      ├ VendorSeverity   ╭ nvd   : 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N
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
│                       │      ╰ LastModifiedDate: 2026-06-02T14:16:37.12Z 
│                       ├ [20] ╭ VulnerabilityID : CVE-2024-2236 
│                       │      ├ PkgID           : libgcrypt20@1.12.0-2ubuntu0.1 
│                       │      ├ PkgName         : libgcrypt20 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgcrypt20@1.12.0-2ubuntu0.1?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : df31886cccfcce83 
│                       │      ├ InstalledVersion: 1.12.0-2ubuntu0.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-2236 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:edb858fca7e2298ebaa36791cf3dd3daa1cac2315d07a659953ba
│                       │      │                   8388f2c9865 
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
│                       │      ╰ LastModifiedDate: 2026-04-15T00:35:42.02Z 
│                       ├ [21] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : libmount1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libmount1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libmount1@2.41.3-3ubuntu2?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : ee0638a59a092c7e 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:c67383589e573ec2d44f294b9715f7742448595280851f839af94
│                       │      │                   bf3a73d3870 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [22] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : libmount1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libmount1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libmount1@2.41.3-3ubuntu2?arch=amd64&d
│                       │      │                  │       istro=ubuntu-26.04 
│                       │      │                  ╰ UID : ee0638a59a092c7e 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:01ebe7590984657fd001edd65e6dc0ca3ab7db4961c2c78073413
│                       │      │                   43869613395 
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
│                       │      ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [23] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : libsmartcols1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libsmartcols1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsmartcols1@2.41.3-3ubuntu2?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : ff5e7b67d2385233 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6b563c984ffc41bb8d188492927ea5be6ca54b7fc695fce1540bd
│                       │      │                   5aafec32245 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [24] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : libsmartcols1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libsmartcols1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsmartcols1@2.41.3-3ubuntu2?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : ff5e7b67d2385233 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e264bd584be64a4531caebefcc4fc0688a9322647f8d436fab6c2
│                       │      │                   ad66339f03e 
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
│                       │      ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [25] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libsystemd0@259.5-0ubuntu3 
│                       │      ├ PkgName         : libsystemd0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libsystemd0@259.5-0ubuntu3?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 68ed9dc5cf416dae 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:9dae19fb106339350cb1427a43702bef247adff943c93aaa93cae
│                       │      │                   bab7453e47f 
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
│                       │      ╰ LastModifiedDate: 2026-05-05T02:16:04.82Z 
│                       ├ [26] ╭ VulnerabilityID : CVE-2026-40228 
│                       │      ├ PkgID           : libudev1@259.5-0ubuntu3 
│                       │      ├ PkgName         : libudev1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libudev1@259.5-0ubuntu3?arch=amd64&dis
│                       │      │                  │       tro=ubuntu-26.04 
│                       │      │                  ╰ UID : 419f3d2219f938db 
│                       │      ├ InstalledVersion: 259.5-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-40228 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:51236bc11085514937064ce12ce8a15bbe05346181e31289c0806
│                       │      │                   4037aa3d873 
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
│                       │      ╰ LastModifiedDate: 2026-05-05T02:16:04.82Z 
│                       ├ [27] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : libuuid1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libuuid1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libuuid1@2.41.3-3ubuntu2?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04 
│                       │      │                  ╰ UID : 41d4afb2fde363cf 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:045d13737e7f9154d526faccc996c54a48a8fa6120822caa375c4
│                       │      │                   9a69b59bb01 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [28] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : libuuid1@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : libuuid1 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libuuid1@2.41.3-3ubuntu2?arch=amd64&di
│                       │      │                  │       stro=ubuntu-26.04 
│                       │      │                  ╰ UID : 41d4afb2fde363cf 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:156195b1fba99da0376a2947d1938e3130ff993c872f3a901e3e5
│                       │      │                   dd4a1fda38b 
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
│                       │      ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [29] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : login@1:4.16.0-2+really2.41.3-3ubuntu2 
│                       │      ├ PkgName         : login 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login@4.16.0-2%2Breally2.41.3-3ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : e1bfbadc9113c00a 
│                       │      ├ InstalledVersion: 1:4.16.0-2+really2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:15467772081ab8ed0db8ac36a5cd81dc22504d4961f73e4968dd4
│                       │      │                   e5b1bbc4dcb 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [30] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : login@1:4.16.0-2+really2.41.3-3ubuntu2 
│                       │      ├ PkgName         : login 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login@4.16.0-2%2Breally2.41.3-3ubuntu2
│                       │      │                  │       ?arch=amd64&distro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : e1bfbadc9113c00a 
│                       │      ├ InstalledVersion: 1:4.16.0-2+really2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:707c5e0b002a2bff2b26ad2c0b09c56e453d4cc2cad8e865e3a99
│                       │      │                   2ecb0b89b5d 
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
│                       │      ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [31] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : login.defs@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : login.defs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login.defs@4.17.4-2ubuntu3?arch=all&di
│                       │      │                  │       stro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : eaf648d5e4e975f7 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:032201a19bd0c798a927e5deb4bb804c6ab11ec6d61386036d2b8
│                       │      │                   a6cfcce4434 
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
│                       │      ╰ LastModifiedDate: 2026-04-15T00:35:42.02Z 
│                       ├ [32] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : mount@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : mount 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/mount@2.41.3-3ubuntu2?arch=amd64&distr
│                       │      │                  │       o=ubuntu-26.04 
│                       │      │                  ╰ UID : 98c6a5d7e9e110eb 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:32a89c92bdc3688d8499efd09bd5247652942dbf22153751ad70c
│                       │      │                   c3d7dda1707 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ├ [33] ╭ VulnerabilityID : CVE-2026-3184 
│                       │      ├ PkgID           : mount@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : mount 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/mount@2.41.3-3ubuntu2?arch=amd64&distr
│                       │      │                  │       o=ubuntu-26.04 
│                       │      │                  ╰ UID : 98c6a5d7e9e110eb 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:8a464a4850b60b32d53dc824f82e0a5c7b69ec6cdd92582bcf0ee
│                       │      │                   b8cd70d33e0 
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
│                       │      ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
│                       ├ [34] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : passwd@1:4.17.4-2ubuntu3 
│                       │      ├ PkgName         : passwd 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/passwd@4.17.4-2ubuntu3?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-26.04&epoch=1 
│                       │      │                  ╰ UID : e6ebfac85406f0d5 
│                       │      ├ InstalledVersion: 1:4.17.4-2ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5ceabda422cca71de413b0e70f0e3b0eb3d5bfc0f077db50d14d9
│                       │      │                   17ff3bb0160 
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
│                       │      ╰ LastModifiedDate: 2026-04-15T00:35:42.02Z 
│                       ├ [35] ╭ VulnerabilityID : CVE-2026-35341 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35341 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:060e7f6782651796de081e71dc0dead11d1ed37d08a0652630e14
│                       │      │                   99cc3b9fd1a 
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
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35341 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35341 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:36.06Z 
│                       │      ╰ LastModifiedDate: 2026-04-24T19:05:55.067Z 
│                       ├ [36] ╭ VulnerabilityID : CVE-2026-35344 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35344 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7188b9374265a9cb1483601eb8698ebc975346421cac6d44a7f8f
│                       │      │                   10e532b296b 
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
│                       │      ╰ LastModifiedDate: 2026-05-04T20:09:48.593Z 
│                       ├ [37] ╭ VulnerabilityID : CVE-2026-35345 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35345 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:38c2a202b878d330a8c66017803459b95950277cb2f19be7f02a2
│                       │      │                   9f4f4f73e6c 
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
│                       │      ╰ LastModifiedDate: 2026-05-04T20:04:25.093Z 
│                       ├ [38] ╭ VulnerabilityID : CVE-2026-35348 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35348 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7e1b9340022378558dff6eeb4e8a3fa0f0fe27d94abca960168b8
│                       │      │                   5211aa70e94 
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
│                       │      ╰ LastModifiedDate: 2026-04-24T18:57:20.927Z 
│                       ├ [39] ╭ VulnerabilityID : CVE-2026-35350 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35350 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:91218cd2d137ba4d6f880f1aca85dc095340c52831461f63c6b96
│                       │      │                   3f9131184b6 
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
│                       │      ╰ LastModifiedDate: 2026-04-24T19:04:01.207Z 
│                       ├ [40] ╭ VulnerabilityID : CVE-2026-35351 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35351 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:0884fe99014c8630a23554050484f6d6784ea3480402cf0eefbfe
│                       │      │                   195e5bb7f94 
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
│                       │      ╰ LastModifiedDate: 2026-04-27T12:28:10.22Z 
│                       ├ [41] ╭ VulnerabilityID : CVE-2026-35352 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35352 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:b01c130f077a55e75dd8ba75ef266012e99e0c162d2b9f226b8fb
│                       │      │                   da43fded0f6 
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
│                       │      ╰ LastModifiedDate: 2026-05-04T18:16:28.37Z 
│                       ├ [42] ╭ VulnerabilityID : CVE-2026-35354 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35354 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:91b96e500d8e9e8af841951f7c799927abc2eead4fdcf2cbf09b6
│                       │      │                   316f70bc50a 
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
│                       │      ╰ LastModifiedDate: 2026-04-24T19:04:08.917Z 
│                       ├ [43] ╭ VulnerabilityID : CVE-2026-35357 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35357 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:26b939c830f60cac64347362f57e66bd7f4b326eba0b1f26bb579
│                       │      │                   768ecea0229 
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
│                       │      ╰ LastModifiedDate: 2026-04-24T19:02:53.557Z 
│                       ├ [44] ╭ VulnerabilityID : CVE-2026-35359 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35359 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:e366376c9b2fd123da9508c3e14cc4cd11f5de84851e7dd2d5680
│                       │      │                   3c6f93c3575 
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
│                       │      ╰ LastModifiedDate: 2026-04-24T19:02:25.72Z 
│                       ├ [45] ╭ VulnerabilityID : CVE-2026-35360 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35360 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:a7328cd8ecc456a400d0c00c918f5a1aa81821009d46499d56179
│                       │      │                   31653dc6a5d 
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
│                       │      ╰ LastModifiedDate: 2026-04-24T19:02:11.56Z 
│                       ├ [46] ╭ VulnerabilityID : CVE-2026-35363 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35363 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5434d29bba78fe92c3ac9daa075d384fd7b7ec118d3934768e36a
│                       │      │                   b3cac329d98 
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
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35363 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35363 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:39.12Z 
│                       │      ╰ LastModifiedDate: 2026-04-24T19:02:00.463Z 
│                       ├ [47] ╭ VulnerabilityID : CVE-2026-35364 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35364 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:21775a081d98b21c41ac7d03847f4aba04e506d91f28deda69cf0
│                       │      │                   84835e7e4dc 
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
│                       │      ╰ LastModifiedDate: 2026-04-24T19:19:11.777Z 
│                       ├ [48] ╭ VulnerabilityID : CVE-2026-35367 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35367 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:51b70cfd5713d61b88889f1fba5ee1993f1056584c593d67cf5fc
│                       │      │                   ea63f4e4fbe 
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
│                       │      ╰ LastModifiedDate: 2026-04-24T19:19:05.067Z 
│                       ├ [49] ╭ VulnerabilityID : CVE-2026-35368 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35368 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:7cda7b6c77109ef15bc6301c8cb98acc50318cbd0173c197b3ff9
│                       │      │                   88a4aec619d 
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
│                       │      ╰ LastModifiedDate: 2026-04-24T19:18:55.67Z 
│                       ├ [50] ╭ VulnerabilityID : CVE-2026-35370 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35370 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:5747f080acdb5f535452217a0c441e6725168f6610bfafd4f4c97
│                       │      │                   97cdeb3aa38 
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
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35370 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35370 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.833Z 
│                       │      ╰ LastModifiedDate: 2026-05-04T20:02:44.33Z 
│                       ├ [51] ╭ VulnerabilityID : CVE-2026-35371 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35371 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:97408208ba8a855cc5644c925c8698eb133a201de4358bf736177
│                       │      │                   00a87dd21f2 
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
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35371 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35371 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:40.987Z 
│                       │      ╰ LastModifiedDate: 2026-05-04T20:02:06.183Z 
│                       ├ [52] ╭ VulnerabilityID : CVE-2026-35373 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35373 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:6ab2e7a30d828afca38fb12dcb76cf4876b0ed0ebd33a5fd454e7
│                       │      │                   78560c74ec7 
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
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2026-35373 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2026-35373 
│                       │      ├ PublishedDate   : 2026-04-22T17:16:41.997Z 
│                       │      ╰ LastModifiedDate: 2026-05-04T20:01:25.93Z 
│                       ├ [53] ╭ VulnerabilityID : CVE-2026-35374 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35374 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:26ad34df2139c618ca91dc432f9fbdb87c4bf0a053d6c558eeccd
│                       │      │                   32a7cf1b99f 
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
│                       │      ╰ LastModifiedDate: 2026-05-04T19:22:14.457Z 
│                       ├ [54] ╭ VulnerabilityID : CVE-2026-35377 
│                       │      ├ PkgID           : rust-coreutils@0.8.0-0ubuntu3 
│                       │      ├ PkgName         : rust-coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/rust-coreutils@0.8.0-0ubuntu3?arch=amd
│                       │      │                  │       64&distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 211a571db931b2ab 
│                       │      ├ InstalledVersion: 0.8.0-0ubuntu3 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-35377 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:ef684bb9386e216f634e10250c409017ab72bcca3c283db4f606c
│                       │      │                   62dec51efc3 
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
│                       │      ╰ LastModifiedDate: 2026-04-24T19:06:46.293Z 
│                       ├ [55] ╭ VulnerabilityID : CVE-2025-45582 
│                       │      ├ PkgID           : tar@1.35+dfsg-4 
│                       │      ├ PkgName         : tar 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-4?arch=amd64&distro=ub
│                       │      │                  │       untu-26.04 
│                       │      │                  ╰ UID : df8f3d12dd71b054 
│                       │      ├ InstalledVersion: 1.35+dfsg-4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-45582 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:9652ba9c66cba3b62e1c2ec6dcb8498f6d11fa833e19a5a00052c
│                       │      │                   af013dd4afc 
│                       │      ├ Title           : tar: Tar path traversal 
│                       │      ├ Description     : GNU Tar through 1.35 allows file overwrite via directory
│                       │      │                   traversal in crafted TAR archives, with a certain two-step
│                       │      │                   process. First, the victim must extract an archive that
│                       │      │                   contains a ../ symlink to a critical directory. Second, the
│                       │      │                   victim must extract an archive that contains a critical
│                       │      │                   file, specified via a relative pathname that begins with the
│                       │      │                    symlink name and ends with that critical file's name. Here,
│                       │      │                    the extraction follows the symlink and overwrites the
│                       │      │                   critical file. This bypasses the protection mechanism of
│                       │      │                   "Member name contains '..'" that would occur for a single
│                       │      │                   TAR archive that attempted to specify the critical file via
│                       │      │                   a ../ approach. For example, the first archive can contain
│                       │      │                   "x -> ../../../../../home/victim/.ssh" and the second
│                       │      │                   archive can contain x/authorized_keys. This can affect
│                       │      │                   server applications that automatically extract any number of
│                       │      │                    user-supplied TAR archives, and were relying on the
│                       │      │                   blocking of traversal. This can also affect software
│                       │      │                   installation processes in which "tar xf" is run more than
│                       │      │                   once (e.g., when installing a package can automatically
│                       │      │                   install two dependencies that are set up as untrusted
│                       │      │                   tarballs instead of official packages). NOTE: the official
│                       │      │                   GNU Tar manual has an otherwise-empty directory for each
│                       │      │                   "tar xf" in its Security Rules of Thumb; however,
│                       │      │                   third-party advice leads users to run "tar xf" more than
│                       │      │                   once into the same directory. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-24 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.6 
│                       │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2025/11/01/6 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2026:0067 
│                       │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2025-45582 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2379592 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2379592 
│                       │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-45582 
│                       │      │                  ├ [6] : https://errata.almalinux.org/9/ALSA-2026-0067.html 
│                       │      │                  ├ [7] : https://errata.rockylinux.org/RLSA-2026:0067 
│                       │      │                  ├ [8] : https://github.com/i900008/vulndb/blob/main/Gnu_tar_v
│                       │      │                  │       uln.md 
│                       │      │                  ├ [9] : https://linux.oracle.com/cve/CVE-2025-45582.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/errata/ELSA-2026-0067.html 
│                       │      │                  ├ [11]: https://lists.gnu.org/archive/html/bug-tar/2025-08/ms
│                       │      │                  │       g00012.html 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2025-45582 
│                       │      │                  ├ [13]: https://www.cve.org/CVERecord?id=CVE-2025-45582 
│                       │      │                  ├ [14]: https://www.gnu.org/software/tar/ 
│                       │      │                  ├ [15]: https://www.gnu.org/software/tar/manual/html_node/Int
│                       │      │                  │       egrity.html 
│                       │      │                  ├ [16]: https://www.gnu.org/software/tar/manual/html_node/Int
│                       │      │                  │       egrity.html#Integrity 
│                       │      │                  ╰ [17]: https://www.gnu.org/software/tar/manual/html_node/Sec
│                       │      │                          urity-rules-of-thumb.html 
│                       │      ├ PublishedDate   : 2025-07-11T17:15:37.183Z 
│                       │      ╰ LastModifiedDate: 2025-11-02T01:15:32.307Z 
│                       ├ [56] ╭ VulnerabilityID : CVE-2026-27456 
│                       │      ├ PkgID           : util-linux@2.41.3-3ubuntu2 
│                       │      ├ PkgName         : util-linux 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/util-linux@2.41.3-3ubuntu2?arch=amd64&
│                       │      │                  │       distro=ubuntu-26.04 
│                       │      │                  ╰ UID : 34e9503915630576 
│                       │      ├ InstalledVersion: 2.41.3-3ubuntu2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                       │      │                  │         7ad94da32273cd72fd6d 
│                       │      │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                       │      │                            7c0f07232e8fdd08b8c5 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27456 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Fingerprint     : sha256:05ac28bc91773629081203252227f0192108bb8df09d8df09c624
│                       │      │                   5b7d7bd3cb6 
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
│                       │      ├ VendorSeverity   ╭ azure : 2 
│                       │      │                  ├ julia : 2 
│                       │      │                  ├ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ╭ julia  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                  │        │           /A:N 
│                       │      │                  │        ╰ V3Score : 4.7 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-27456 
│                       │      │                  ├ [1]: https://github.com/util-linux/util-linux/commit/5e3904
│                       │      │                  │      67b26a3cf3fecc04e1a0d482dff3162fc4 
│                       │      │                  ├ [2]: https://github.com/util-linux/util-linux/releases/tag/
│                       │      │                  │      v2.41.4 
│                       │      │                  ├ [3]: https://github.com/util-linux/util-linux/security/advi
│                       │      │                  │      sories/GHSA-qq4x-vfq4-9h9g 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-27456 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2026-27456 
│                       │      ├ PublishedDate   : 2026-04-03T22:16:25.4Z 
│                       │      ╰ LastModifiedDate: 2026-04-22T16:08:55.1Z 
│                       ╰ [57] ╭ VulnerabilityID : CVE-2026-3184 
│                              ├ PkgID           : util-linux@2.41.3-3ubuntu2 
│                              ├ PkgName         : util-linux 
│                              ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/util-linux@2.41.3-3ubuntu2?arch=amd64&
│                              │                  │       distro=ubuntu-26.04 
│                              │                  ╰ UID : 34e9503915630576 
│                              ├ InstalledVersion: 2.41.3-3ubuntu2 
│                              ├ Status          : affected 
│                              ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f
│                              │                  │         7ad94da32273cd72fd6d 
│                              │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e36
│                              │                            7c0f07232e8fdd08b8c5 
│                              ├ SeveritySource  : ubuntu 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-3184 
│                              ├ DataSource       ╭ ID  : ubuntu 
│                              │                  ├ Name: Ubuntu CVE Tracker 
│                              │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                              ├ Fingerprint     : sha256:c1ff96b062fb1751a18e903da0e1884a41e5547315957a4a199cb
│                              │                   995c6ff486f 
│                              ├ Title           : util-linux: util-linux: Access control bypass due to
│                              │                   improper hostname canonicalization 
│                              ├ Description     : A flaw was found in util-linux. Improper hostname
│                              │                   canonicalization in the `login(1)` utility, when invoked
│                              │                   with the `-h` option, can modify the supplied remote
│                              │                   hostname before setting `PAM_RHOST`. A remote attacker could
│                              │                    exploit this by providing a specially crafted hostname,
│                              │                   potentially bypassing host-based Pluggable Authentication
│                              │                   Modules (PAM) access control rules that rely on fully
│                              │                   qualified domain names. This could lead to unauthorized
│                              │                   access. 
│                              ├ Severity        : MEDIUM 
│                              ├ CweIDs           ─ [0]: CWE-289 
│                              ├ VendorSeverity   ╭ azure : 1 
│                              │                  ├ nvd   : 2 
│                              │                  ├ photon: 2 
│                              │                  ├ redhat: 1 
│                              │                  ╰ ubuntu: 2 
│                              ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                              │                  │        │           /A:N 
│                              │                  │        ╰ V3Score : 5.3 
│                              │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                              │                           │           /A:N 
│                              │                           ╰ V3Score : 3.7 
│                              ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2026:7180 
│                              │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2026-3184 
│                              │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2442570 
│                              │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-3184 
│                              │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2026-3184 
│                              ├ PublishedDate   : 2026-04-03T19:17:23.377Z 
│                              ╰ LastModifiedDate: 2026-05-01T19:29:51.02Z 
├ [1] ╭ Target  : Java 
│     ├ Class   : lang-pkgs 
│     ├ Type    : jar 
│     ╰ Packages 
╰ [2] ╭ Target         : usr/bin/pebble 
      ├ Class          : lang-pkgs 
      ├ Type           : gobinary 
      ├ Packages        
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2026-42504 
                        │     ├ VendorIDs        ─ [0]: GO-2026-5038 
                        │     ├ PkgID           : stdlib@v1.26.3 
                        │     ├ PkgName         : stdlib 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.3 
                        │     │                  ╰ UID : 88b4097712908b9b 
                        │     ├ InstalledVersion: v1.26.3 
                        │     ├ FixedVersion    : 1.25.11, 1.26.4 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f7
                        │     │                  │         ad94da32273cd72fd6d 
                        │     │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e367
                        │     │                            c0f07232e8fdd08b8c5 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42504 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:2a7b49571c88f2c9190e3034ed722530629d0ef932a237b4e534e5
                        │     │                   3320ce3648 
                        │     ├ Title           : Decoding a maliciously-crafted MIME header containing many
                        │     │                   invalid enc ... 
                        │     ├ Description     : Decoding a maliciously-crafted MIME header containing many
                        │     │                   invalid encoded-words can consume excessive CPU. 
                        │     ├ Severity        : HIGH 
                        │     ├ CweIDs           ─ [0]: CWE-407 
                        │     ├ VendorSeverity   ─ bitnami: 3 
                        │     ├ CVSS             ─ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
                        │     │                            │           /A:H 
                        │     │                            ╰ V3Score : 7.5 
                        │     ├ References       ╭ [0]: https://go.dev/cl/774481 
                        │     │                  ├ [1]: https://go.dev/issue/79217 
                        │     │                  ├ [2]: https://groups.google.com/g/golang-announce/c/tKs3rmcBcKw 
                        │     │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-42504 
                        │     │                  ╰ [4]: https://pkg.go.dev/vuln/GO-2026-5038 
                        │     ├ PublishedDate   : 2026-06-02T23:16:37.927Z 
                        │     ╰ LastModifiedDate: 2026-06-04T16:15:50.143Z 
                        ├ [1] ╭ VulnerabilityID : CVE-2026-27145 
                        │     ├ VendorIDs        ─ [0]: GO-2026-5037 
                        │     ├ PkgID           : stdlib@v1.26.3 
                        │     ├ PkgName         : stdlib 
                        │     ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.3 
                        │     │                  ╰ UID : 88b4097712908b9b 
                        │     ├ InstalledVersion: v1.26.3 
                        │     ├ FixedVersion    : 1.25.11, 1.26.4 
                        │     ├ Status          : fixed 
                        │     ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f7
                        │     │                  │         ad94da32273cd72fd6d 
                        │     │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e367
                        │     │                            c0f07232e8fdd08b8c5 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-27145 
                        │     ├ DataSource       ╭ ID  : govulndb 
                        │     │                  ├ Name: The Go Vulnerability Database 
                        │     │                  ╰ URL : https://pkg.go.dev/vuln/ 
                        │     ├ Fingerprint     : sha256:c8cc20b5a803e83ae15d04d45c8bc330d8af9fa1ada7bb0cb0ac97
                        │     │                   0779798acc 
                        │     ├ Title           : *x509.Certificate).VerifyHostname previously called
                        │     │                   matchHostnames in ... 
                        │     ├ Description     : (*x509.Certificate).VerifyHostname previously called
                        │     │                   matchHostnames in a loop over all DNS Subject Alternative
                        │     │                   Name (SAN) entries. This caused strings.Split(host, ".") to
                        │     │                   execute repeatedly on the same input hostname. With a large
                        │     │                   DNS SAN list, verification costs scaled quadratically based
                        │     │                   on the number of SAN entries multiplied by the hostname's
                        │     │                   label count. Because x509.Verify validates hostnames before
                        │     │                   building the certificate chain, this overhead occurred even
                        │     │                   for untrusted certificates. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ VendorSeverity   ─ bitnami: 2 
                        │     ├ CVSS             ─ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
                        │     │                            │           /A:H 
                        │     │                            ╰ V3Score : 6.5 
                        │     ├ References       ╭ [0]: https://go.dev/cl/783621 
                        │     │                  ├ [1]: https://go.dev/issue/79694 
                        │     │                  ├ [2]: https://groups.google.com/g/golang-announce/c/tKs3rmcBcKw 
                        │     │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2026-27145 
                        │     │                  ╰ [4]: https://pkg.go.dev/vuln/GO-2026-5037 
                        │     ├ PublishedDate   : 2026-06-02T23:16:35.57Z 
                        │     ╰ LastModifiedDate: 2026-06-04T16:15:50.143Z 
                        ╰ [2] ╭ VulnerabilityID : CVE-2026-42507 
                              ├ VendorIDs        ─ [0]: GO-2026-5039 
                              ├ PkgID           : stdlib@v1.26.3 
                              ├ PkgName         : stdlib 
                              ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.26.3 
                              │                  ╰ UID : 88b4097712908b9b 
                              ├ InstalledVersion: v1.26.3 
                              ├ FixedVersion    : 1.25.11, 1.26.4 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:026d32611353f4951debac954cdda68bb9d4feaad37f7
                              │                  │         ad94da32273cd72fd6d 
                              │                  ╰ DiffID: sha256:97e4f5827d3834edf0fc859dab406f98343e2ece8e367
                              │                            c0f07232e8fdd08b8c5 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-42507 
                              ├ DataSource       ╭ ID  : govulndb 
                              │                  ├ Name: The Go Vulnerability Database 
                              │                  ╰ URL : https://pkg.go.dev/vuln/ 
                              ├ Fingerprint     : sha256:cd203ca79bdd720dff90fed05e4b7901d4ea3acae32f3fcf46ca4a
                              │                   ad8e587af0 
                              ├ Title           : net/textproto: golang: Golang net/textproto: Misleading error
                              │                    messages via input injection 
                              ├ Description     : When returning errors, functions in the net/textproto package
                              │                    would include its input as part of the error. This might
                              │                   allow an attacker to inject misleading content to errors that
                              │                    are printed or logged. 
                              ├ Severity        : MEDIUM 
                              ├ VendorSeverity   ╭ bitnami: 2 
                              │                  ╰ redhat : 2 
                              ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
                              │                  │         │           /A:N 
                              │                  │         ╰ V3Score : 5.3 
                              │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
                              │                            │           /A:N 
                              │                            ╰ V3Score : 5.3 
                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2026-42507 
                              │                  ├ [1]: https://go.dev/cl/777060 
                              │                  ├ [2]: https://go.dev/issue/79346 
                              │                  ├ [3]: https://groups.google.com/g/golang-announce/c/tKs3rmcBcKw 
                              │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2026-42507 
                              │                  ├ [5]: https://pkg.go.dev/vuln/GO-2026-5039 
                              │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2026-42507 
                              ├ PublishedDate   : 2026-06-02T23:16:38.027Z 
                              ╰ LastModifiedDate: 2026-06-04T16:15:50.143Z 
```
