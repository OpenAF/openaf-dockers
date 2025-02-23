````yaml
╭ [0] ╭ Target         : openaf/oaf:deb-nightly (ubuntu 24.04) 
│     ├ Class          : os-pkgs 
│     ├ Type           : ubuntu 
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2016-2781 
│                       │      ├ PkgID           : coreutils@9.4-3ubuntu6 
│                       │      ├ PkgName         : coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/coreutils@9.4-3ubuntu6?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-24.04 
│                       │      │                  ╰ UID : 91b2a8258892ebb 
│                       │      ├ InstalledVersion: 9.4-3ubuntu6 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
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
│                       │      ╰ LastModifiedDate: 2024-11-21T02:48:47.593Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2025-0167 
│                       │      ├ PkgID           : curl@8.5.0-2ubuntu10.6 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.5.0-2ubuntu10.6?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-24.04 
│                       │      │                  ╰ UID : 71fd8292b7daf34e 
│                       │      ├ InstalledVersion: 8.5.0-2ubuntu10.6 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-0167 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : When asked to use a `.netrc` file for credentials **and** to
│                       │      │                    follow HT ... 
│                       │      ├ Description     : When asked to use a `.netrc` file for credentials **and** to
│                       │      │                    follow HTTP
│                       │      │                   redirects, curl could leak the password used for the first
│                       │      │                   host to the
│                       │      │                   followed-to host under certain circumstances.
│                       │      │                   
│                       │      │                   This flaw only manifests itself if the netrc file has a
│                       │      │                   `default` entry that
│                       │      │                   omits both login and password. A rare circumstance. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ├ References       ╭ [0]: https://curl.se/docs/CVE-2025-0167.html 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2025-0167.json 
│                       │      │                  ├ [2]: https://hackerone.com/reports/2917232 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2025-0167 
│                       │      ├ PublishedDate   : 2025-02-05T10:15:22.71Z 
│                       │      ╰ LastModifiedDate: 2025-02-06T15:15:16.967Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2022-3219 
│                       │      ├ PkgID           : gpgv@2.4.4-2ubuntu17 
│                       │      ├ PkgName         : gpgv 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/gpgv@2.4.4-2ubuntu17?arch=amd64&distro
│                       │      │                  │       =ubuntu-24.04 
│                       │      │                  ╰ UID : 7861d55200da292b 
│                       │      ├ InstalledVersion: 2.4.4-2ubuntu17 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
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
│                       │      ╰ LastModifiedDate: 2024-11-21T07:19:04.727Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2024-26462 
│                       │      ├ PkgID           : krb5-locales@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : krb5-locales 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/krb5-locales@1.20.1-6ubuntu2.4?arch=al
│                       │      │                  │       l&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 43c311d1fad01dcc 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26462 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/kdc/ndr.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak
│                       │      │                   vulnerability in /krb5/src/kdc/ndr.c. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-401 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26462 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [6] : https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_3.md 
│                       │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2024-26462.html 
│                       │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [9] : https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [10]: https://nvd.nist.gov/vuln/detail/CVE-2024-26462 
│                       │      │                  ├ [11]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       12/ 
│                       │      │                  ╰ [12]: https://www.cve.org/CVERecord?id=CVE-2024-26462 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.857Z 
│                       │      ╰ LastModifiedDate: 2025-02-14T17:29:03.303Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2024-26458 
│                       │      ├ PkgID           : krb5-locales@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : krb5-locales 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/krb5-locales@1.20.1-6ubuntu2.4?arch=al
│                       │      │                  │       l&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 43c311d1fad01dcc 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26458 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak in
│                       │      │                   /krb5/src/lib/rpc/pmap_rmt.c. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26458 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2266731 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2266740 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26458 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26461 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:3268 
│                       │      │                  ├ [11]: https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_1.md 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2024-26458.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [14]: https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2024-26458 
│                       │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       10/ 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-26458 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.78Z 
│                       │      ╰ LastModifiedDate: 2024-12-06T21:15:06.28Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2024-26461 
│                       │      ├ PkgID           : krb5-locales@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : krb5-locales 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/krb5-locales@1.20.1-6ubuntu2.4?arch=al
│                       │      │                  │       l&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 43c311d1fad01dcc 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26461 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak
│                       │      │                   vulnerability in /krb5/src/lib/gssapi/krb5/k5sealv3.c. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26461 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2266731 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2266740 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26458 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26461 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:3268 
│                       │      │                  ├ [11]: https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_2.md 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2024-26461.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [14]: https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2024-26461 
│                       │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       11/ 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-26461 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.82Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T09:02:26.477Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2016-20013 
│                       │      ├ PkgID           : libc-bin@2.39-0ubuntu8.4 
│                       │      ├ PkgName         : libc-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc-bin@2.39-0ubuntu8.4?arch=amd64&di
│                       │      │                  │       stro=ubuntu-24.04 
│                       │      │                  ╰ UID : 939838306fc8a34c 
│                       │      ├ InstalledVersion: 2.39-0ubuntu8.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2016-20013 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Description     : sha256crypt and sha512crypt through 0.6 allow attackers to
│                       │      │                   cause a denial of service (CPU consumption) because the
│                       │      │                   algorithm's runtime is proportional to the square of the
│                       │      │                   length of the password. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ nvd   : 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ nvd ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:N/A:P 
│                       │      │                        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
│                       │      │                        ├ V2Score : 5 
│                       │      │                        ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://akkadia.org/drepper/SHA-crypt.txt 
│                       │      │                  ├ [1]: https://pthree.org/2018/05/23/do-not-use-sha256crypt-s
│                       │      │                  │      ha512crypt-theyre-dangerous/ 
│                       │      │                  ├ [2]: https://twitter.com/solardiz/status/795601240151457793 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2016-20013 
│                       │      ├ PublishedDate   : 2022-02-19T05:15:09.413Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T02:47:33.427Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2016-20013 
│                       │      ├ PkgID           : libc6@2.39-0ubuntu8.4 
│                       │      ├ PkgName         : libc6 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libc6@2.39-0ubuntu8.4?arch=amd64&distr
│                       │      │                  │       o=ubuntu-24.04 
│                       │      │                  ╰ UID : 59b78719802dd37a 
│                       │      ├ InstalledVersion: 2.39-0ubuntu8.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2016-20013 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Description     : sha256crypt and sha512crypt through 0.6 allow attackers to
│                       │      │                   cause a denial of service (CPU consumption) because the
│                       │      │                   algorithm's runtime is proportional to the square of the
│                       │      │                   length of the password. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ nvd   : 3 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ nvd ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:N/A:P 
│                       │      │                        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
│                       │      │                        ├ V2Score : 5 
│                       │      │                        ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0]: https://akkadia.org/drepper/SHA-crypt.txt 
│                       │      │                  ├ [1]: https://pthree.org/2018/05/23/do-not-use-sha256crypt-s
│                       │      │                  │      ha512crypt-theyre-dangerous/ 
│                       │      │                  ├ [2]: https://twitter.com/solardiz/status/795601240151457793 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2016-20013 
│                       │      ├ PublishedDate   : 2022-02-19T05:15:09.413Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T02:47:33.427Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2025-1390 
│                       │      ├ PkgID           : libcap2@1:2.66-5ubuntu2.1 
│                       │      ├ PkgName         : libcap2 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcap2@2.66-5ubuntu2.1?arch=amd64&dis
│                       │      │                  │       tro=ubuntu-24.04&epoch=1 
│                       │      │                  ╰ UID : 4c75c706fa9a02ae 
│                       │      ├ InstalledVersion: 1:2.66-5ubuntu2.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-1390 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : libcap: pam_cap: Fix potential configuration parsing error 
│                       │      ├ Description     : The PAM module pam_cap.so of libcap configuration supports
│                       │      │                   group names starting with “@”, during actual parsing,
│                       │      │                   configurations not starting with “@” are incorrectly
│                       │      │                   recognized as group names. This may result in nonintended
│                       │      │                   users being granted an inherited capability set, potentially
│                       │      │                    leading to security risks. Attackers can exploit this
│                       │      │                   vulnerability to achieve local privilege escalation on
│                       │      │                   systems where /etc/security/capability.conf is used to
│                       │      │                   configure user inherited privileges by constructing specific
│                       │      │                    usernames. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-284 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 6.1 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-1390 
│                       │      │                  ├ [1]: https://bugzilla.openanolis.cn/show_bug.cgi?id=18804 
│                       │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2025-1390 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2025-1390 
│                       │      ├ PublishedDate   : 2025-02-18T03:15:10.447Z 
│                       │      ╰ LastModifiedDate: 2025-02-18T03:15:10.447Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2025-0167 
│                       │      ├ PkgID           : libcurl4t64@8.5.0-2ubuntu10.6 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.5.0-2ubuntu10.6?arch=amd
│                       │      │                  │       64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 1affc7d07a525f4a 
│                       │      ├ InstalledVersion: 8.5.0-2ubuntu10.6 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-0167 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : When asked to use a `.netrc` file for credentials **and** to
│                       │      │                    follow HT ... 
│                       │      ├ Description     : When asked to use a `.netrc` file for credentials **and** to
│                       │      │                    follow HTTP
│                       │      │                   redirects, curl could leak the password used for the first
│                       │      │                   host to the
│                       │      │                   followed-to host under certain circumstances.
│                       │      │                   
│                       │      │                   This flaw only manifests itself if the netrc file has a
│                       │      │                   `default` entry that
│                       │      │                   omits both login and password. A rare circumstance. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ─ ubuntu: 1 
│                       │      ├ References       ╭ [0]: https://curl.se/docs/CVE-2025-0167.html 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2025-0167.json 
│                       │      │                  ├ [2]: https://hackerone.com/reports/2917232 
│                       │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2025-0167 
│                       │      ├ PublishedDate   : 2025-02-05T10:15:22.71Z 
│                       │      ╰ LastModifiedDate: 2025-02-06T15:15:16.967Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2024-2236 
│                       │      ├ PkgID           : libgcrypt20@1.10.3-2build1 
│                       │      ├ PkgName         : libgcrypt20 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgcrypt20@1.10.3-2build1?arch=amd64&
│                       │      │                  │       distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 75ea201b0aeb3715 
│                       │      ├ InstalledVersion: 1.10.3-2build1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
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
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-2236 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2245218 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/show_bug.cgi?id=2245218 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2268268 
│                       │      │                  ├ [5] : https://dev.gnupg.org/T7136 
│                       │      │                  ├ [6] : https://errata.almalinux.org/9/ALSA-2024-9404.html 
│                       │      │                  ├ [7] : https://github.com/tomato42/marvin-toolkit/tree/maste
│                       │      │                  │       r/example/libgcrypt 
│                       │      │                  ├ [8] : https://gitlab.com/redhat-crypto/libgcrypt/libgcrypt-
│                       │      │                  │       mirror/-/merge_requests/17 
│                       │      │                  ├ [9] : https://linux.oracle.com/cve/CVE-2024-2236.html 
│                       │      │                  ├ [10]: https://linux.oracle.com/errata/ELSA-2024-9404.html 
│                       │      │                  ├ [11]: https://lists.gnupg.org/pipermail/gcrypt-devel/2024-M
│                       │      │                  │       arch/005607.html 
│                       │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2024-2236 
│                       │      │                  ╰ [13]: https://www.cve.org/CVERecord?id=CVE-2024-2236 
│                       │      ├ PublishedDate   : 2024-03-06T22:15:57.977Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T09:09:19.41Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2024-26462 
│                       │      ├ PkgID           : libgssapi-krb5-2@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : libgssapi-krb5-2 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgssapi-krb5-2@1.20.1-6ubuntu2.4?arc
│                       │      │                  │       h=amd64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 998709db5c1b91a5 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26462 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/kdc/ndr.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak
│                       │      │                   vulnerability in /krb5/src/kdc/ndr.c. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-401 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26462 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [6] : https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_3.md 
│                       │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2024-26462.html 
│                       │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [9] : https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [10]: https://nvd.nist.gov/vuln/detail/CVE-2024-26462 
│                       │      │                  ├ [11]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       12/ 
│                       │      │                  ╰ [12]: https://www.cve.org/CVERecord?id=CVE-2024-26462 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.857Z 
│                       │      ╰ LastModifiedDate: 2025-02-14T17:29:03.303Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2024-26458 
│                       │      ├ PkgID           : libgssapi-krb5-2@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : libgssapi-krb5-2 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgssapi-krb5-2@1.20.1-6ubuntu2.4?arc
│                       │      │                  │       h=amd64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 998709db5c1b91a5 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26458 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak in
│                       │      │                   /krb5/src/lib/rpc/pmap_rmt.c. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26458 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2266731 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2266740 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26458 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26461 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:3268 
│                       │      │                  ├ [11]: https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_1.md 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2024-26458.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [14]: https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2024-26458 
│                       │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       10/ 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-26458 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.78Z 
│                       │      ╰ LastModifiedDate: 2024-12-06T21:15:06.28Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2024-26461 
│                       │      ├ PkgID           : libgssapi-krb5-2@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : libgssapi-krb5-2 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgssapi-krb5-2@1.20.1-6ubuntu2.4?arc
│                       │      │                  │       h=amd64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 998709db5c1b91a5 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26461 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak
│                       │      │                   vulnerability in /krb5/src/lib/gssapi/krb5/k5sealv3.c. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26461 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2266731 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2266740 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26458 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26461 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:3268 
│                       │      │                  ├ [11]: https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_2.md 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2024-26461.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [14]: https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2024-26461 
│                       │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       11/ 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-26461 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.82Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T09:02:26.477Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2024-26462 
│                       │      ├ PkgID           : libk5crypto3@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : libk5crypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libk5crypto3@1.20.1-6ubuntu2.4?arch=am
│                       │      │                  │       d64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : c0875c431e2fddd0 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26462 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/kdc/ndr.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak
│                       │      │                   vulnerability in /krb5/src/kdc/ndr.c. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-401 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26462 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [6] : https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_3.md 
│                       │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2024-26462.html 
│                       │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [9] : https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [10]: https://nvd.nist.gov/vuln/detail/CVE-2024-26462 
│                       │      │                  ├ [11]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       12/ 
│                       │      │                  ╰ [12]: https://www.cve.org/CVERecord?id=CVE-2024-26462 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.857Z 
│                       │      ╰ LastModifiedDate: 2025-02-14T17:29:03.303Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2024-26458 
│                       │      ├ PkgID           : libk5crypto3@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : libk5crypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libk5crypto3@1.20.1-6ubuntu2.4?arch=am
│                       │      │                  │       d64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : c0875c431e2fddd0 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26458 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak in
│                       │      │                   /krb5/src/lib/rpc/pmap_rmt.c. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26458 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2266731 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2266740 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26458 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26461 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:3268 
│                       │      │                  ├ [11]: https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_1.md 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2024-26458.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [14]: https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2024-26458 
│                       │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       10/ 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-26458 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.78Z 
│                       │      ╰ LastModifiedDate: 2024-12-06T21:15:06.28Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2024-26461 
│                       │      ├ PkgID           : libk5crypto3@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : libk5crypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libk5crypto3@1.20.1-6ubuntu2.4?arch=am
│                       │      │                  │       d64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : c0875c431e2fddd0 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26461 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak
│                       │      │                   vulnerability in /krb5/src/lib/gssapi/krb5/k5sealv3.c. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26461 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2266731 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2266740 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26458 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26461 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:3268 
│                       │      │                  ├ [11]: https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_2.md 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2024-26461.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [14]: https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2024-26461 
│                       │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       11/ 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-26461 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.82Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T09:02:26.477Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2024-26462 
│                       │      ├ PkgID           : libkrb5-3@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : libkrb5-3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libkrb5-3@1.20.1-6ubuntu2.4?arch=amd64
│                       │      │                  │       &distro=ubuntu-24.04 
│                       │      │                  ╰ UID : d65342dbe27c8452 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26462 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/kdc/ndr.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak
│                       │      │                   vulnerability in /krb5/src/kdc/ndr.c. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-401 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26462 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [6] : https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_3.md 
│                       │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2024-26462.html 
│                       │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [9] : https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [10]: https://nvd.nist.gov/vuln/detail/CVE-2024-26462 
│                       │      │                  ├ [11]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       12/ 
│                       │      │                  ╰ [12]: https://www.cve.org/CVERecord?id=CVE-2024-26462 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.857Z 
│                       │      ╰ LastModifiedDate: 2025-02-14T17:29:03.303Z 
│                       ├ [18] ╭ VulnerabilityID : CVE-2024-26458 
│                       │      ├ PkgID           : libkrb5-3@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : libkrb5-3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libkrb5-3@1.20.1-6ubuntu2.4?arch=amd64
│                       │      │                  │       &distro=ubuntu-24.04 
│                       │      │                  ╰ UID : d65342dbe27c8452 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26458 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak in
│                       │      │                   /krb5/src/lib/rpc/pmap_rmt.c. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26458 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2266731 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2266740 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26458 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26461 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:3268 
│                       │      │                  ├ [11]: https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_1.md 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2024-26458.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [14]: https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2024-26458 
│                       │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       10/ 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-26458 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.78Z 
│                       │      ╰ LastModifiedDate: 2024-12-06T21:15:06.28Z 
│                       ├ [19] ╭ VulnerabilityID : CVE-2024-26461 
│                       │      ├ PkgID           : libkrb5-3@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : libkrb5-3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libkrb5-3@1.20.1-6ubuntu2.4?arch=amd64
│                       │      │                  │       &distro=ubuntu-24.04 
│                       │      │                  ╰ UID : d65342dbe27c8452 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26461 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak
│                       │      │                   vulnerability in /krb5/src/lib/gssapi/krb5/k5sealv3.c. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26461 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2266731 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2266740 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26458 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26461 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:3268 
│                       │      │                  ├ [11]: https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_2.md 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2024-26461.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [14]: https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2024-26461 
│                       │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       11/ 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-26461 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.82Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T09:02:26.477Z 
│                       ├ [20] ╭ VulnerabilityID : CVE-2024-26462 
│                       │      ├ PkgID           : libkrb5support0@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : libkrb5support0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libkrb5support0@1.20.1-6ubuntu2.4?arch
│                       │      │                  │       =amd64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 217834966d60c9a8 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26462 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/kdc/ndr.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak
│                       │      │                   vulnerability in /krb5/src/kdc/ndr.c. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-401 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ nvd        : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N
│                       │      │                  │        │           /A:H 
│                       │      │                  │        ╰ V3Score : 5.5 
│                       │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.5 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26462 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [6] : https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_3.md 
│                       │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2024-26462.html 
│                       │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [9] : https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [10]: https://nvd.nist.gov/vuln/detail/CVE-2024-26462 
│                       │      │                  ├ [11]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       12/ 
│                       │      │                  ╰ [12]: https://www.cve.org/CVERecord?id=CVE-2024-26462 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.857Z 
│                       │      ╰ LastModifiedDate: 2025-02-14T17:29:03.303Z 
│                       ├ [21] ╭ VulnerabilityID : CVE-2024-26458 
│                       │      ├ PkgID           : libkrb5support0@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : libkrb5support0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libkrb5support0@1.20.1-6ubuntu2.4?arch
│                       │      │                  │       =amd64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 217834966d60c9a8 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26458 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/lib/rpc/pmap_rmt.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak in
│                       │      │                   /krb5/src/lib/rpc/pmap_rmt.c. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ cbl-mariner: 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26458 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2266731 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2266740 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26458 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26461 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:3268 
│                       │      │                  ├ [11]: https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_1.md 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2024-26458.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [14]: https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2024-26458 
│                       │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       10/ 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-26458 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.78Z 
│                       │      ╰ LastModifiedDate: 2024-12-06T21:15:06.28Z 
│                       ├ [22] ╭ VulnerabilityID : CVE-2024-26461 
│                       │      ├ PkgID           : libkrb5support0@1.20.1-6ubuntu2.4 
│                       │      ├ PkgName         : libkrb5support0 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libkrb5support0@1.20.1-6ubuntu2.4?arch
│                       │      │                  │       =amd64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 217834966d60c9a8 
│                       │      ├ InstalledVersion: 1.20.1-6ubuntu2.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-26461 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : krb5: Memory leak at /krb5/src/lib/gssapi/krb5/k5sealv3.c 
│                       │      ├ Description     : Kerberos 5 (aka krb5) 1.21.2 contains a memory leak
│                       │      │                   vulnerability in /krb5/src/lib/gssapi/krb5/k5sealv3.c. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-770 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ cbl-mariner: 3 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ photon     : 2 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ├ rocky      : 1 
│                       │      │                  ╰ ubuntu     : 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:9331 
│                       │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2024-26461 
│                       │      │                  ├ [2] : https://bugzilla.redhat.com/2266731 
│                       │      │                  ├ [3] : https://bugzilla.redhat.com/2266740 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2266742 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2266731 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2266740 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26458 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-26461 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-9331.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:3268 
│                       │      │                  ├ [11]: https://github.com/LuMingYinDetect/krb5_defects/blob/
│                       │      │                  │       main/krb5_detect_2.md 
│                       │      │                  ├ [12]: https://linux.oracle.com/cve/CVE-2024-26461.html 
│                       │      │                  ├ [13]: https://linux.oracle.com/errata/ELSA-2024-9331.html 
│                       │      │                  ├ [14]: https://mailman.mit.edu/pipermail/kerberos/2024-March
│                       │      │                  │       /023095.html 
│                       │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2024-26461 
│                       │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-20240415-00
│                       │      │                  │       11/ 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-26461 
│                       │      ├ PublishedDate   : 2024-02-29T01:44:18.82Z 
│                       │      ╰ LastModifiedDate: 2024-11-21T09:02:26.477Z 
│                       ├ [23] ╭ VulnerabilityID : CVE-2024-10041 
│                       │      ├ PkgID           : libpam-modules@1.5.3-5ubuntu5.1 
│                       │      ├ PkgName         : libpam-modules 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam-modules@1.5.3-5ubuntu5.1?arch=a
│                       │      │                  │       md64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : f821171cc4f544ed 
│                       │      ├ InstalledVersion: 1.5.3-5ubuntu5.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-10041 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : pam: libpam: Libpam vulnerable to read hashed password 
│                       │      ├ Description     : A vulnerability was found in PAM. The secret information is
│                       │      │                   stored in memory, where the attacker can trigger the victim
│                       │      │                   program to execute by sending characters to its standard
│                       │      │                   input (stdin). As this occurs, the attacker can train the
│                       │      │                   branch predictor to execute an ROP chain speculatively. This
│                       │      │                    flaw could result in leaked passwords, such as those found
│                       │      │                   in /etc/shadow while performing authentications. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-922 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:10379 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2024:11250 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2024:9941 
│                       │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2024-10041 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2319212 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2319212 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2324291 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10041 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10963 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-11250.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:10379 
│                       │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2024-10041.html 
│                       │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2024-11250.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-10041 
│                       │      │                  ╰ [14]: https://www.cve.org/CVERecord?id=CVE-2024-10041 
│                       │      ├ PublishedDate   : 2024-10-23T14:15:03.97Z 
│                       │      ╰ LastModifiedDate: 2024-12-18T10:15:05.85Z 
│                       ├ [24] ╭ VulnerabilityID : CVE-2024-10963 
│                       │      ├ PkgID           : libpam-modules@1.5.3-5ubuntu5.1 
│                       │      ├ PkgName         : libpam-modules 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam-modules@1.5.3-5ubuntu5.1?arch=a
│                       │      │                  │       md64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : f821171cc4f544ed 
│                       │      ├ InstalledVersion: 1.5.3-5ubuntu5.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-10963 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : pam: Improper Hostname Interpretation in pam_access Leads to
│                       │      │                    Access Control Bypass 
│                       │      ├ Description     : A flaw was found in pam_access, where certain rules in its
│                       │      │                   configuration file are mistakenly treated as hostnames. This
│                       │      │                    vulnerability allows attackers to trick the system by
│                       │      │                   pretending to be a trusted hostname, gaining unauthorized
│                       │      │                   access. This issue poses a risk for systems that rely on
│                       │      │                   this feature to control who can access certain services or
│                       │      │                   terminals. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-287 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:10232 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2024:10244 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2024:10379 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2024:10518 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2024:10528 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2024:10852 
│                       │      │                  ├ [6] : https://access.redhat.com/security/cve/CVE-2024-10963 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2324291 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2319212 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2324291 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10041 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10963 
│                       │      │                  ├ [12]: https://errata.almalinux.org/9/ALSA-2024-10244.html 
│                       │      │                  ├ [13]: https://errata.rockylinux.org/RLSA-2024:10379 
│                       │      │                  ├ [14]: https://linux.oracle.com/cve/CVE-2024-10963.html 
│                       │      │                  ├ [15]: https://linux.oracle.com/errata/ELSA-2024-10379.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2024-10963 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-10963 
│                       │      ├ PublishedDate   : 2024-11-07T16:15:17.15Z 
│                       │      ╰ LastModifiedDate: 2025-02-06T06:15:29.24Z 
│                       ├ [25] ╭ VulnerabilityID : CVE-2024-10041 
│                       │      ├ PkgID           : libpam-modules-bin@1.5.3-5ubuntu5.1 
│                       │      ├ PkgName         : libpam-modules-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam-modules-bin@1.5.3-5ubuntu5.1?ar
│                       │      │                  │       ch=amd64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 7c7ccd55f96c6f56 
│                       │      ├ InstalledVersion: 1.5.3-5ubuntu5.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-10041 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : pam: libpam: Libpam vulnerable to read hashed password 
│                       │      ├ Description     : A vulnerability was found in PAM. The secret information is
│                       │      │                   stored in memory, where the attacker can trigger the victim
│                       │      │                   program to execute by sending characters to its standard
│                       │      │                   input (stdin). As this occurs, the attacker can train the
│                       │      │                   branch predictor to execute an ROP chain speculatively. This
│                       │      │                    flaw could result in leaked passwords, such as those found
│                       │      │                   in /etc/shadow while performing authentications. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-922 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:10379 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2024:11250 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2024:9941 
│                       │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2024-10041 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2319212 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2319212 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2324291 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10041 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10963 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-11250.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:10379 
│                       │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2024-10041.html 
│                       │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2024-11250.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-10041 
│                       │      │                  ╰ [14]: https://www.cve.org/CVERecord?id=CVE-2024-10041 
│                       │      ├ PublishedDate   : 2024-10-23T14:15:03.97Z 
│                       │      ╰ LastModifiedDate: 2024-12-18T10:15:05.85Z 
│                       ├ [26] ╭ VulnerabilityID : CVE-2024-10963 
│                       │      ├ PkgID           : libpam-modules-bin@1.5.3-5ubuntu5.1 
│                       │      ├ PkgName         : libpam-modules-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam-modules-bin@1.5.3-5ubuntu5.1?ar
│                       │      │                  │       ch=amd64&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : 7c7ccd55f96c6f56 
│                       │      ├ InstalledVersion: 1.5.3-5ubuntu5.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-10963 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : pam: Improper Hostname Interpretation in pam_access Leads to
│                       │      │                    Access Control Bypass 
│                       │      ├ Description     : A flaw was found in pam_access, where certain rules in its
│                       │      │                   configuration file are mistakenly treated as hostnames. This
│                       │      │                    vulnerability allows attackers to trick the system by
│                       │      │                   pretending to be a trusted hostname, gaining unauthorized
│                       │      │                   access. This issue poses a risk for systems that rely on
│                       │      │                   this feature to control who can access certain services or
│                       │      │                   terminals. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-287 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:10232 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2024:10244 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2024:10379 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2024:10518 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2024:10528 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2024:10852 
│                       │      │                  ├ [6] : https://access.redhat.com/security/cve/CVE-2024-10963 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2324291 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2319212 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2324291 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10041 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10963 
│                       │      │                  ├ [12]: https://errata.almalinux.org/9/ALSA-2024-10244.html 
│                       │      │                  ├ [13]: https://errata.rockylinux.org/RLSA-2024:10379 
│                       │      │                  ├ [14]: https://linux.oracle.com/cve/CVE-2024-10963.html 
│                       │      │                  ├ [15]: https://linux.oracle.com/errata/ELSA-2024-10379.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2024-10963 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-10963 
│                       │      ├ PublishedDate   : 2024-11-07T16:15:17.15Z 
│                       │      ╰ LastModifiedDate: 2025-02-06T06:15:29.24Z 
│                       ├ [27] ╭ VulnerabilityID : CVE-2024-10041 
│                       │      ├ PkgID           : libpam-runtime@1.5.3-5ubuntu5.1 
│                       │      ├ PkgName         : libpam-runtime 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam-runtime@1.5.3-5ubuntu5.1?arch=a
│                       │      │                  │       ll&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : f94ce0c2a9328057 
│                       │      ├ InstalledVersion: 1.5.3-5ubuntu5.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-10041 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : pam: libpam: Libpam vulnerable to read hashed password 
│                       │      ├ Description     : A vulnerability was found in PAM. The secret information is
│                       │      │                   stored in memory, where the attacker can trigger the victim
│                       │      │                   program to execute by sending characters to its standard
│                       │      │                   input (stdin). As this occurs, the attacker can train the
│                       │      │                   branch predictor to execute an ROP chain speculatively. This
│                       │      │                    flaw could result in leaked passwords, such as those found
│                       │      │                   in /etc/shadow while performing authentications. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-922 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:10379 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2024:11250 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2024:9941 
│                       │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2024-10041 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2319212 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2319212 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2324291 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10041 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10963 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-11250.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:10379 
│                       │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2024-10041.html 
│                       │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2024-11250.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-10041 
│                       │      │                  ╰ [14]: https://www.cve.org/CVERecord?id=CVE-2024-10041 
│                       │      ├ PublishedDate   : 2024-10-23T14:15:03.97Z 
│                       │      ╰ LastModifiedDate: 2024-12-18T10:15:05.85Z 
│                       ├ [28] ╭ VulnerabilityID : CVE-2024-10963 
│                       │      ├ PkgID           : libpam-runtime@1.5.3-5ubuntu5.1 
│                       │      ├ PkgName         : libpam-runtime 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam-runtime@1.5.3-5ubuntu5.1?arch=a
│                       │      │                  │       ll&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : f94ce0c2a9328057 
│                       │      ├ InstalledVersion: 1.5.3-5ubuntu5.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-10963 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : pam: Improper Hostname Interpretation in pam_access Leads to
│                       │      │                    Access Control Bypass 
│                       │      ├ Description     : A flaw was found in pam_access, where certain rules in its
│                       │      │                   configuration file are mistakenly treated as hostnames. This
│                       │      │                    vulnerability allows attackers to trick the system by
│                       │      │                   pretending to be a trusted hostname, gaining unauthorized
│                       │      │                   access. This issue poses a risk for systems that rely on
│                       │      │                   this feature to control who can access certain services or
│                       │      │                   terminals. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-287 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:10232 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2024:10244 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2024:10379 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2024:10518 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2024:10528 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2024:10852 
│                       │      │                  ├ [6] : https://access.redhat.com/security/cve/CVE-2024-10963 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2324291 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2319212 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2324291 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10041 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10963 
│                       │      │                  ├ [12]: https://errata.almalinux.org/9/ALSA-2024-10244.html 
│                       │      │                  ├ [13]: https://errata.rockylinux.org/RLSA-2024:10379 
│                       │      │                  ├ [14]: https://linux.oracle.com/cve/CVE-2024-10963.html 
│                       │      │                  ├ [15]: https://linux.oracle.com/errata/ELSA-2024-10379.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2024-10963 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-10963 
│                       │      ├ PublishedDate   : 2024-11-07T16:15:17.15Z 
│                       │      ╰ LastModifiedDate: 2025-02-06T06:15:29.24Z 
│                       ├ [29] ╭ VulnerabilityID : CVE-2024-10041 
│                       │      ├ PkgID           : libpam0g@1.5.3-5ubuntu5.1 
│                       │      ├ PkgName         : libpam0g 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam0g@1.5.3-5ubuntu5.1?arch=amd64&d
│                       │      │                  │       istro=ubuntu-24.04 
│                       │      │                  ╰ UID : 7a311da79b48e0e1 
│                       │      ├ InstalledVersion: 1.5.3-5ubuntu5.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-10041 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : pam: libpam: Libpam vulnerable to read hashed password 
│                       │      ├ Description     : A vulnerability was found in PAM. The secret information is
│                       │      │                   stored in memory, where the attacker can trigger the victim
│                       │      │                   program to execute by sending characters to its standard
│                       │      │                   input (stdin). As this occurs, the attacker can train the
│                       │      │                   branch predictor to execute an ROP chain speculatively. This
│                       │      │                    flaw could result in leaked passwords, such as those found
│                       │      │                   in /etc/shadow while performing authentications. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-922 
│                       │      ├ VendorSeverity   ╭ alma       : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ oracle-oval: 2 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.7 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:10379 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2024:11250 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2024:9941 
│                       │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2024-10041 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2319212 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2319212 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2324291 
│                       │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10041 
│                       │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10963 
│                       │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2024-11250.html 
│                       │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2024:10379 
│                       │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2024-10041.html 
│                       │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2024-11250.html 
│                       │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-10041 
│                       │      │                  ╰ [14]: https://www.cve.org/CVERecord?id=CVE-2024-10041 
│                       │      ├ PublishedDate   : 2024-10-23T14:15:03.97Z 
│                       │      ╰ LastModifiedDate: 2024-12-18T10:15:05.85Z 
│                       ├ [30] ╭ VulnerabilityID : CVE-2024-10963 
│                       │      ├ PkgID           : libpam0g@1.5.3-5ubuntu5.1 
│                       │      ├ PkgName         : libpam0g 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam0g@1.5.3-5ubuntu5.1?arch=amd64&d
│                       │      │                  │       istro=ubuntu-24.04 
│                       │      │                  ╰ UID : 7a311da79b48e0e1 
│                       │      ├ InstalledVersion: 1.5.3-5ubuntu5.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-10963 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : pam: Improper Hostname Interpretation in pam_access Leads to
│                       │      │                    Access Control Bypass 
│                       │      ├ Description     : A flaw was found in pam_access, where certain rules in its
│                       │      │                   configuration file are mistakenly treated as hostnames. This
│                       │      │                    vulnerability allows attackers to trick the system by
│                       │      │                   pretending to be a trusted hostname, gaining unauthorized
│                       │      │                   access. This issue poses a risk for systems that rely on
│                       │      │                   this feature to control who can access certain services or
│                       │      │                   terminals. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-287 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ azure      : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2024:10232 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2024:10244 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2024:10379 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2024:10518 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2024:10528 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2024:10852 
│                       │      │                  ├ [6] : https://access.redhat.com/security/cve/CVE-2024-10963 
│                       │      │                  ├ [7] : https://bugzilla.redhat.com/2324291 
│                       │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=2319212 
│                       │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2324291 
│                       │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10041 
│                       │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       24-10963 
│                       │      │                  ├ [12]: https://errata.almalinux.org/9/ALSA-2024-10244.html 
│                       │      │                  ├ [13]: https://errata.rockylinux.org/RLSA-2024:10379 
│                       │      │                  ├ [14]: https://linux.oracle.com/cve/CVE-2024-10963.html 
│                       │      │                  ├ [15]: https://linux.oracle.com/errata/ELSA-2024-10379.html 
│                       │      │                  ├ [16]: https://nvd.nist.gov/vuln/detail/CVE-2024-10963 
│                       │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2024-10963 
│                       │      ├ PublishedDate   : 2024-11-07T16:15:17.15Z 
│                       │      ╰ LastModifiedDate: 2025-02-06T06:15:29.24Z 
│                       ├ [31] ╭ VulnerabilityID : CVE-2024-41996 
│                       │      ├ PkgID           : libssl3t64@3.0.13-0ubuntu3.5 
│                       │      ├ PkgName         : libssl3t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libssl3t64@3.0.13-0ubuntu3.5?arch=amd6
│                       │      │                  │       4&distro=ubuntu-24.04 
│                       │      │                  ╰ UID : f7dd30a98cc0b1a 
│                       │      ├ InstalledVersion: 3.0.13-0ubuntu3.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-41996 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : openssl: remote attackers (from the client side) to trigger
│                       │      │                   unnecessarily expensive server-side DHE
│                       │      │                   modular-exponentiation calculations 
│                       │      ├ Description     : Validating the order of the public keys in the
│                       │      │                   Diffie-Hellman Key Agreement Protocol, when an approved safe
│                       │      │                    prime is used, allows remote attackers (from the client
│                       │      │                   side) to trigger unnecessarily expensive server-side DHE
│                       │      │                   modular-exponentiation calculations. The client may cause
│                       │      │                   asymmetric resource consumption. The basic attack scenario
│                       │      │                   is that the client must claim that it can only communicate
│                       │      │                   with DHE, and the server must be configured to allow DHE and
│                       │      │                    validate the order of the public key. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-295 
│                       │      ├ VendorSeverity   ╭ amazon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-41996 
│                       │      │                  ├ [1]: https://dheatattack.gitlab.io/details/ 
│                       │      │                  ├ [2]: https://dheatattack.gitlab.io/faq/ 
│                       │      │                  ├ [3]: https://gist.github.com/c0r0n3r/abccc14d4d96c0442f3a77
│                       │      │                  │      fa5ca255d1 
│                       │      │                  ├ [4]: https://github.com/openssl/openssl/issues/17374 
│                       │      │                  ├ [5]: https://github.com/openssl/openssl/pull/25088 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2024-41996 
│                       │      │                  ├ [7]: https://openssl-library.org/post/2022-10-21-tls-groups
│                       │      │                  │      -configuration/ 
│                       │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2024-41996 
│                       │      ├ PublishedDate   : 2024-08-26T06:15:04.603Z 
│                       │      ╰ LastModifiedDate: 2024-08-26T16:35:11.247Z 
│                       ├ [32] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : login@1:4.13+dfsg1-4ubuntu3.2 
│                       │      ├ PkgName         : login 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login@4.13%2Bdfsg1-4ubuntu3.2?arch=amd
│                       │      │                  │       64&distro=ubuntu-24.04&epoch=1 
│                       │      │                  ╰ UID : 92b953859fb749c3 
│                       │      ├ InstalledVersion: 1:4.13+dfsg1-4ubuntu3.2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
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
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-1188 
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
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
│                       ├ [33] ╭ VulnerabilityID : CVE-2024-41996 
│                       │      ├ PkgID           : openssl@3.0.13-0ubuntu3.5 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/openssl@3.0.13-0ubuntu3.5?arch=amd64&d
│                       │      │                  │       istro=ubuntu-24.04 
│                       │      │                  ╰ UID : 9833b0131d231716 
│                       │      ├ InstalledVersion: 3.0.13-0ubuntu3.5 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                       │      │                  │         220400b097eb335db1a4 
│                       │      │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                       │      │                            127e7fb08290e1be7343 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-41996 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : openssl: remote attackers (from the client side) to trigger
│                       │      │                   unnecessarily expensive server-side DHE
│                       │      │                   modular-exponentiation calculations 
│                       │      ├ Description     : Validating the order of the public keys in the
│                       │      │                   Diffie-Hellman Key Agreement Protocol, when an approved safe
│                       │      │                    prime is used, allows remote attackers (from the client
│                       │      │                   side) to trigger unnecessarily expensive server-side DHE
│                       │      │                   modular-exponentiation calculations. The client may cause
│                       │      │                   asymmetric resource consumption. The basic attack scenario
│                       │      │                   is that the client must claim that it can only communicate
│                       │      │                   with DHE, and the server must be configured to allow DHE and
│                       │      │                    validate the order of the public key. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-295 
│                       │      ├ VendorSeverity   ╭ amazon: 2 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-41996 
│                       │      │                  ├ [1]: https://dheatattack.gitlab.io/details/ 
│                       │      │                  ├ [2]: https://dheatattack.gitlab.io/faq/ 
│                       │      │                  ├ [3]: https://gist.github.com/c0r0n3r/abccc14d4d96c0442f3a77
│                       │      │                  │      fa5ca255d1 
│                       │      │                  ├ [4]: https://github.com/openssl/openssl/issues/17374 
│                       │      │                  ├ [5]: https://github.com/openssl/openssl/pull/25088 
│                       │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2024-41996 
│                       │      │                  ├ [7]: https://openssl-library.org/post/2022-10-21-tls-groups
│                       │      │                  │      -configuration/ 
│                       │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2024-41996 
│                       │      ├ PublishedDate   : 2024-08-26T06:15:04.603Z 
│                       │      ╰ LastModifiedDate: 2024-08-26T16:35:11.247Z 
│                       ╰ [34] ╭ VulnerabilityID : CVE-2024-56433 
│                              ├ PkgID           : passwd@1:4.13+dfsg1-4ubuntu3.2 
│                              ├ PkgName         : passwd 
│                              ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/passwd@4.13%2Bdfsg1-4ubuntu3.2?arch=am
│                              │                  │       d64&distro=ubuntu-24.04&epoch=1 
│                              │                  ╰ UID : d910a4981892feb8 
│                              ├ InstalledVersion: 1:4.13+dfsg1-4ubuntu3.2 
│                              ├ Status          : affected 
│                              ├ Layer            ╭ Digest: sha256:0948f6495456a3718d4db1958e1defc9367a3f0e71cb
│                              │                  │         220400b097eb335db1a4 
│                              │                  ╰ DiffID: sha256:8290a1203a998f6232d6e4e1b2a3f43a1add8119c058
│                              │                            127e7fb08290e1be7343 
│                              ├ SeveritySource  : ubuntu 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-56433 
│                              ├ DataSource       ╭ ID  : ubuntu 
│                              │                  ├ Name: Ubuntu CVE Tracker 
│                              │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                              ├ Title           : shadow-utils: Default subordinate ID configuration in
│                              │                   /etc/login.defs could lead to compromise 
│                              ├ Description     : shadow-utils (aka shadow) 4.4 through 4.17.0 establishes a
│                              │                   default /etc/subuid behavior (e.g., uid 100000 through
│                              │                   165535 for the first user account) that can realistically
│                              │                   conflict with the uids of users defined on locally
│                              │                   administered networks, potentially leading to account
│                              │                   takeover, e.g., by leveraging newuidmap for access to an NFS
│                              │                    home directory (or same-host resources in the case of
│                              │                   remote logins by these local network users). NOTE: it may
│                              │                   also be argued that system administrators should not have
│                              │                   assigned uids, within local networks, that are within the
│                              │                   range that can occur in /etc/subuid. 
│                              ├ Severity        : MEDIUM 
│                              ├ CweIDs           ─ [0]: CWE-1188 
│                              ├ VendorSeverity   ╭ redhat: 1 
│                              │                  ╰ ubuntu: 2 
│                              ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L
│                              │                           │           /A:N 
│                              │                           ╰ V3Score : 3.6 
│                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-56433 
│                              │                  ├ [1]: https://github.com/shadow-maint/shadow/blob/e2512d5741
│                              │                  │      d4a44bdd81a8c2d0029b6222728cf0/etc/login.defs#L238-L24
│                              │                  │      1 
│                              │                  ├ [2]: https://github.com/shadow-maint/shadow/issues/1157 
│                              │                  ├ [3]: https://github.com/shadow-maint/shadow/releases/tag/4.4 
│                              │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2024-56433 
│                              │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2024-56433 
│                              ├ PublishedDate   : 2024-12-26T09:15:07.267Z 
│                              ╰ LastModifiedDate: 2024-12-26T09:15:07.267Z 
╰ [1] ╭ Target: Java 
      ├ Class : lang-pkgs 
      ╰ Type  : jar 
````
