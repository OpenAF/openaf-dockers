````yaml
─ [0] ╭ Target         : openaf/oaf:8-ubi (redhat 9.3) 
      ├ Class          : os-pkgs 
      ├ Type           : redhat 
      ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2023-38469 
                        │      ├ PkgID           : avahi-libs@0.8-15.el9.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-15.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-38469 
                        │      ├ Title           : avahi: Reachable assertion in avahi_dns_packet_append_record 
                        │      ├ Description     : A vulnerability was found in Avahi, where a reachable
                        │      │                   assertion exists in avahi_dns_packet_append_record. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-617 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ├ rocky      : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:7836 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-38469 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/1939614 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2191687 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2191690 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2191691 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2191692 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2191694 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=1939614 
                        │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2191687 
                        │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2191690 
                        │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2191691 
                        │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2191692 
                        │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2191694 
                        │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2021-3468 
                        │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38469 
                        │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38470 
                        │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38471 
                        │      │                  ├ [18]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38472 
                        │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38473 
                        │      │                  ├ [20]: https://errata.almalinux.org/8/ALSA-2023-7836.html 
                        │      │                  ├ [21]: https://errata.rockylinux.org/RLSA-2023:7836 
                        │      │                  ├ [22]: https://linux.oracle.com/cve/CVE-2023-38469.html 
                        │      │                  ├ [23]: https://linux.oracle.com/errata/ELSA-2023-7836.html 
                        │      │                  ├ [24]: https://nvd.nist.gov/vuln/detail/CVE-2023-38469 
                        │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6487-1 
                        │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2023-38469 
                        │      ├ PublishedDate   : 2023-11-02T15:15:08.167Z 
                        │      ╰ LastModifiedDate: 2023-11-09T19:58:53.293Z 
                        ├ [1]  ╭ VulnerabilityID : CVE-2023-38470 
                        │      ├ PkgID           : avahi-libs@0.8-15.el9.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-15.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-38470 
                        │      ├ Title           : avahi: Reachable assertion in avahi_escape_label 
                        │      ├ Description     : A vulnerability was found in Avahi. A reachable
                        │      │                   assertion exists in the avahi_escape_label() function. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-617 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ├ rocky      : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:7836 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-38470 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/1939614 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2191687 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2191690 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2191691 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2191692 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2191694 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=1939614 
                        │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2191687 
                        │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2191690 
                        │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2191691 
                        │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2191692 
                        │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2191694 
                        │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2021-3468 
                        │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38469 
                        │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38470 
                        │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38471 
                        │      │                  ├ [18]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38472 
                        │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38473 
                        │      │                  ├ [20]: https://errata.almalinux.org/8/ALSA-2023-7836.html 
                        │      │                  ├ [21]: https://errata.rockylinux.org/RLSA-2023:7836 
                        │      │                  ├ [22]: https://linux.oracle.com/cve/CVE-2023-38470.html 
                        │      │                  ├ [23]: https://linux.oracle.com/errata/ELSA-2023-7836.html 
                        │      │                  ├ [24]: https://nvd.nist.gov/vuln/detail/CVE-2023-38470 
                        │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6487-1 
                        │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2023-38470 
                        │      ├ PublishedDate   : 2023-11-02T15:15:08.237Z 
                        │      ╰ LastModifiedDate: 2023-11-09T19:58:39.71Z 
                        ├ [2]  ╭ VulnerabilityID : CVE-2023-38471 
                        │      ├ PkgID           : avahi-libs@0.8-15.el9.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-15.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-38471 
                        │      ├ Title           : avahi: Reachable assertion in dbus_set_host_name 
                        │      ├ Description     : A vulnerability was found in Avahi. A reachable
                        │      │                   assertion exists in the dbus_set_host_name function. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-617 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ├ rocky      : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:7836 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-38471 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/1939614 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2191687 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2191690 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2191691 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2191692 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2191694 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=1939614 
                        │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2191687 
                        │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2191690 
                        │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2191691 
                        │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2191692 
                        │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2191694 
                        │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2021-3468 
                        │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38469 
                        │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38470 
                        │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38471 
                        │      │                  ├ [18]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38472 
                        │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38473 
                        │      │                  ├ [20]: https://errata.almalinux.org/8/ALSA-2023-7836.html 
                        │      │                  ├ [21]: https://errata.rockylinux.org/RLSA-2023:7836 
                        │      │                  ├ [22]: https://linux.oracle.com/cve/CVE-2023-38471.html 
                        │      │                  ├ [23]: https://linux.oracle.com/errata/ELSA-2023-7836.html 
                        │      │                  ├ [24]: https://nvd.nist.gov/vuln/detail/CVE-2023-38471 
                        │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6487-1 
                        │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2023-38471 
                        │      ├ PublishedDate   : 2023-11-02T15:15:08.3Z 
                        │      ╰ LastModifiedDate: 2023-11-09T19:58:27.143Z 
                        ├ [3]  ╭ VulnerabilityID : CVE-2023-38472 
                        │      ├ PkgID           : avahi-libs@0.8-15.el9.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-15.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-38472 
                        │      ├ Title           : avahi: Reachable assertion in avahi_rdata_parse 
                        │      ├ Description     : A vulnerability was found in Avahi. A reachable
                        │      │                   assertion exists in the avahi_rdata_parse() function. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-617 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ├ rocky      : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:7836 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-38472 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/1939614 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2191687 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2191690 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2191691 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2191692 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2191694 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=1939614 
                        │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2191687 
                        │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2191690 
                        │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2191691 
                        │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2191692 
                        │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2191694 
                        │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2021-3468 
                        │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38469 
                        │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38470 
                        │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38471 
                        │      │                  ├ [18]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38472 
                        │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38473 
                        │      │                  ├ [20]: https://errata.almalinux.org/8/ALSA-2023-7836.html 
                        │      │                  ├ [21]: https://errata.rockylinux.org/RLSA-2023:7836 
                        │      │                  ├ [22]: https://linux.oracle.com/cve/CVE-2023-38472.html 
                        │      │                  ├ [23]: https://linux.oracle.com/errata/ELSA-2023-7836.html 
                        │      │                  ├ [24]: https://nvd.nist.gov/vuln/detail/CVE-2023-38472 
                        │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6487-1 
                        │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2023-38472 
                        │      ├ PublishedDate   : 2023-11-02T15:15:08.363Z 
                        │      ╰ LastModifiedDate: 2023-11-09T19:58:11.57Z 
                        ├ [4]  ╭ VulnerabilityID : CVE-2023-38473 
                        │      ├ PkgID           : avahi-libs@0.8-15.el9.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-15.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-38473 
                        │      ├ Title           : avahi: Reachable assertion in avahi_alternative_host_name 
                        │      ├ Description     : A vulnerability was found in Avahi. A reachable
                        │      │                   assertion exists in the avahi_alternative_host_name()
                        │      │                   function. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-617 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ├ rocky      : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:7836 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-38473 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/1939614 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2191687 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2191690 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2191691 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2191692 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2191694 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/show_bug.cgi?id=1939614 
                        │      │                  ├ [9] : https://bugzilla.redhat.com/show_bug.cgi?id=2191687 
                        │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2191690 
                        │      │                  ├ [11]: https://bugzilla.redhat.com/show_bug.cgi?id=2191691 
                        │      │                  ├ [12]: https://bugzilla.redhat.com/show_bug.cgi?id=2191692 
                        │      │                  ├ [13]: https://bugzilla.redhat.com/show_bug.cgi?id=2191694 
                        │      │                  ├ [14]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2021-3468 
                        │      │                  ├ [15]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38469 
                        │      │                  ├ [16]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38470 
                        │      │                  ├ [17]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38471 
                        │      │                  ├ [18]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38472 
                        │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-38473 
                        │      │                  ├ [20]: https://errata.almalinux.org/8/ALSA-2023-7836.html 
                        │      │                  ├ [21]: https://errata.rockylinux.org/RLSA-2023:7836 
                        │      │                  ├ [22]: https://linux.oracle.com/cve/CVE-2023-38473.html 
                        │      │                  ├ [23]: https://linux.oracle.com/errata/ELSA-2023-7836.html 
                        │      │                  ├ [24]: https://nvd.nist.gov/vuln/detail/CVE-2023-38473 
                        │      │                  ├ [25]: https://ubuntu.com/security/notices/USN-6487-1 
                        │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2023-38473 
                        │      ├ PublishedDate   : 2023-11-02T16:15:08.773Z 
                        │      ╰ LastModifiedDate: 2023-11-09T17:46:40.643Z 
                        ├ [5]  ╭ VulnerabilityID : CVE-2017-6519 
                        │      ├ PkgID           : avahi-libs@0.8-15.el9.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-15.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2017-6519 
                        │      ├ Title           : avahi: Multicast DNS responds to unicast queries
                        │      │                   outside of local network 
                        │      ├ Description     : avahi-daemon in Avahi through 0.6.32 and 0.7
                        │      │                   inadvertently responds to IPv6 unicast queries with source
                        │      │                   addresses that are not on-link, which allows remote
                        │      │                   attackers to cause a denial of service (traffic
                        │      │                   amplification) and may cause information leakage by
                        │      │                   obtaining potentially sensitive  information from the
                        │      │                   responding device via port-5353 UDP packets.  NOTE: this may
                        │      │                    overlap CVE-2015-2809. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-346 
                        │      ├ VendorSeverity   ╭ amazon     : 1 
                        │      │                  ├ cbl-mariner: 4 
                        │      │                  ├ nvd        : 4 
                        │      │                  ├ oracle-oval: 1 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:P/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:H 
                        │      │                  │        ├ V2Score : 6.4 
                        │      │                  │        ╰ V3Score : 9.1 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 5.8 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2017-6519 
                        │      │                  ├ [1] : https://bugzilla.redhat.com/show_bug.cgi?id=1426712 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2017-6519 
                        │      │                  ├ [3] : https://github.com/lathiat/avahi/issues/203 
                        │      │                  ├ [4] : https://github.com/lathiat/avahi/issues/203#issu
                        │      │                  │       ecomment-449536790 
                        │      │                  ├ [5] : https://linux.oracle.com/cve/CVE-2017-6519.html 
                        │      │                  ├ [6] : https://linux.oracle.com/errata/ELSA-2020-1176.html 
                        │      │                  ├ [7] : https://lists.apache.org/thread.html/r1b103833cb
                        │      │                  │       5bc8466e24ff0ecc5e75b45a705334ab6a444e64e840a0%40%3Ci
                        │      │                  │       ssues.bookkeeper.apache.org%3E 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2017-6519 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-3876-1 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-3876-2 
                        │      │                  ├ [11]: https://usn.ubuntu.com/3876-1/ 
                        │      │                  ├ [12]: https://usn.ubuntu.com/3876-2/ 
                        │      │                  ├ [13]: https://www.cve.org/CVERecord?id=CVE-2017-6519 
                        │      │                  ├ [14]: https://www.kb.cert.org/vuls/id/550620 
                        │      │                  ╰ [15]: https://www.secfu.net/advisories 
                        │      ├ PublishedDate   : 2017-05-01T01:59:00.297Z 
                        │      ╰ LastModifiedDate: 2023-11-07T02:49:56.39Z 
                        ├ [6]  ╭ VulnerabilityID : CVE-2023-37920 
                        │      ├ PkgID           : ca-certificates@2023.2.60_v7.0.306-90.1.el9_2.noarch 
                        │      ├ PkgName         : ca-certificates 
                        │      ├ InstalledVersion: 2023.2.60_v7.0.306-90.1.el9_2 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-37920 
                        │      ├ Title           : python-certifi: Removal of e-Tugra root certificate 
                        │      ├ Description     : Certifi is a curated collection of Root Certificates
                        │      │                   for validating the trustworthiness of SSL certificates while
                        │      │                    verifying the identity of TLS hosts. Certifi prior to
                        │      │                   version 2023.07.22 recognizes "e-Tugra" root certificates.
                        │      │                   e-Tugra's root certificates were subject to an investigation
                        │      │                    prompted by reporting of security issues in their systems.
                        │      │                   Certifi 2023.07.22 removes root certificates from "e-Tugra"
                        │      │                   from the root store. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-345 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 3 
                        │      │                  ├ ghsa       : 3 
                        │      │                  ├ nvd        : 4 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ photon     : 4 
                        │      │                  ╰ redhat     : 1 
                        │      ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:H/A:N 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 9.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:H/A:N 
                        │      │                           ╰ V3Score : 9.1 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:7753 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-37920 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2226586 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2242493 
                        │      │                  ├ [4] : https://errata.almalinux.org/9/ALSA-2023-7753.html 
                        │      │                  ├ [5] : https://github.com/certifi/python-certifi 
                        │      │                  ├ [6] : https://github.com/certifi/python-certifi/commit
                        │      │                  │       /8fb96ed81f71e7097ed11bc4d9b19afd7ea5c909 
                        │      │                  ├ [7] : https://github.com/certifi/python-certifi/securi
                        │      │                  │       ty/advisories/GHSA-xqr8-7jwr-rhp7 
                        │      │                  ├ [8] : https://github.com/pypa/advisory-database/tree/m
                        │      │                  │       ain/vulns/certifi/PYSEC-2023-135.yaml 
                        │      │                  ├ [9] : https://groups.google.com/a/mozilla.org/g/dev-se
                        │      │                  │       curity-policy/c/C-HrP1SEq1A 
                        │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2023-37920.html 
                        │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2024-0133.html 
                        │      │                  ├ [12]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/5EX6NG
                        │      │                  │       7WUFNUKGFHLM35KHHU3GAKXRTG/ 
                        │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2023-37920 
                        │      │                  ╰ [14]: https://www.cve.org/CVERecord?id=CVE-2023-37920 
                        │      ├ PublishedDate   : 2023-07-25T21:15:10.827Z 
                        │      ╰ LastModifiedDate: 2023-08-12T06:16:31.077Z 
                        ├ [7]  ╭ VulnerabilityID : CVE-2023-4504 
                        │      ├ PkgID           : cups-libs@2.3.3op2-21.el9.x86_64 
                        │      ├ PkgName         : cups-libs 
                        │      ├ InstalledVersion: 1:2.3.3op2-21.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-4504 
                        │      ├ Title           : cups, libppd: Postscript Parsing Heap Overflow 
                        │      ├ Description     : Due to failure in validating the length provided by an
                        │      │                   attacker-crafted PPD PostScript document, CUPS and libppd
                        │      │                   are susceptible to a heap-based buffer overflow and possibly
                        │      │                    code execution. This issue has been fixed in CUPS version
                        │      │                   2.4.7, released in September of 2023.
                        │      │                    
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ╭ [0]: CWE-787 
                        │      │                  ╰ [1]: CWE-122 
                        │      ├ VendorSeverity   ╭ amazon: 2 
                        │      │                  ├ nvd   : 3 
                        │      │                  ├ photon: 3 
                        │      │                  ├ redhat: 2 
                        │      │                  ╰ ubuntu: 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:U/C:
                        │      │                           │           H/I:H/A:H 
                        │      │                           ╰ V3Score : 7 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-4504 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-4504 
                        │      │                  ├ [2] : https://github.com/OpenPrinting/cups/releases/ta
                        │      │                  │       g/v2.4.7 
                        │      │                  ├ [3] : https://github.com/OpenPrinting/cups/security/ad
                        │      │                  │       visories/GHSA-pf5r-86w9-678h 
                        │      │                  ├ [4] : https://github.com/OpenPrinting/libppd/security/
                        │      │                  │       advisories/GHSA-4f65-6ph5-qwh6 
                        │      │                  ├ [5] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/09/msg00041.html 
                        │      │                  ├ [6] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/5WHEJI
                        │      │                  │       YMMAIXU2EC35MGTB5LGGO2FFJE/ 
                        │      │                  ├ [7] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/5WVS4I
                        │      │                  │       7JG3LISFPKTM6ADKJXXEPEEWBQ/ 
                        │      │                  ├ [8] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/AMYDKI
                        │      │                  │       E4PSJDEMC5OWNFCDMHFGLJ57XG/ 
                        │      │                  ├ [9] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/PXPVAD
                        │      │                  │       B56NMLJWG4IZ3OZBNJ2ZOLPQJ6/ 
                        │      │                  ├ [10]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/T2GSPQ
                        │      │                  │       AFK2Z6L57TRXEKZDF42K2EVBH7/ 
                        │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2023-4504 
                        │      │                  ├ [12]: https://takeonme.org/cves/CVE-2023-4504.html 
                        │      │                  ├ [13]: https://ubuntu.com/security/notices/USN-6391-1 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6391-2 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6392-1 
                        │      │                  ╰ [16]: https://www.cve.org/CVERecord?id=CVE-2023-4504 
                        │      ├ PublishedDate   : 2023-09-21T23:15:12.293Z 
                        │      ╰ LastModifiedDate: 2023-11-09T20:58:00.163Z 
                        ├ [8]  ╭ VulnerabilityID : CVE-2021-25317 
                        │      ├ PkgID           : cups-libs@2.3.3op2-21.el9.x86_64 
                        │      ├ PkgName         : cups-libs 
                        │      ├ InstalledVersion: 1:2.3.3op2-21.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-25317 
                        │      ├ Title           : cups: insecure permissions of /var/log/cups allows for
                        │      │                   symlink attacks 
                        │      ├ Description     : A Incorrect Default Permissions vulnerability in the
                        │      │                   packaging of cups of SUSE Linux Enterprise Server
                        │      │                   11-SP4-LTSS, SUSE Manager Server 4.0, SUSE OpenStack Cloud
                        │      │                   Crowbar 9; openSUSE Leap 15.2, Factory allows local
                        │      │                   attackers with control of the lp users to create files as
                        │      │                   root with 0644 permissions without the ability to set the
                        │      │                   content. This issue affects: SUSE Linux Enterprise Server
                        │      │                   11-SP4-LTSS cups versions prior to 1.3.9. SUSE Manager
                        │      │                   Server 4.0 cups versions prior to 2.2.7. SUSE OpenStack
                        │      │                   Cloud Crowbar 9 cups versions prior to 1.7.5. openSUSE Leap
                        │      │                   15.2 cups versions prior to 2.2.7. openSUSE Factory cups
                        │      │                   version 2.3.3op2-2.1 and prior versions. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-276 
                        │      ├ VendorSeverity   ╭ nvd   : 1 
                        │      │                  ╰ redhat: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:L/AC:L/Au:N/C:N/I:P/A:N 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:N 
                        │      │                  │        ├ V2Score : 2.1 
                        │      │                  │        ╰ V3Score : 3.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 2 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-25317 
                        │      │                  ├ [1]: https://bugzilla.suse.com/show_bug.cgi?id=1184161 
                        │      │                  ├ [2]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce%40lists.fedoraproject.org/message/GWPGZL
                        │      │                  │      T3U776Q5YPPSA6LGFWWBDWBVH3/ 
                        │      │                  ├ [3]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce%40lists.fedoraproject.org/message/H74BP7
                        │      │                  │      46O5NNVCBUTLLZYAFBPESFVECV/ 
                        │      │                  ├ [4]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce%40lists.fedoraproject.org/message/S37IDQ
                        │      │                  │      GHTORQ3Z6VRDQIGBYVOI27YG47/ 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2021-25317 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2021-25317 
                        │      ├ PublishedDate   : 2021-05-05T10:15:08.133Z 
                        │      ╰ LastModifiedDate: 2023-11-07T03:31:27.377Z 
                        ├ [9]  ╭ VulnerabilityID : CVE-2023-46218 
                        │      ├ PkgID           : curl-minimal@7.76.1-26.el9_3.2.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-26.el9_3.2 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-46218 
                        │      ├ Title           : curl: information disclosure by exploiting a mixed case flaw 
                        │      ├ Description     : This flaw allows a malicious HTTP server to set "super
                        │      │                   cookies" in curl that
                        │      │                   are then passed back to more origins than what is otherwise
                        │      │                   allowed or
                        │      │                   possible. This allows a site to set cookies that then would
                        │      │                   get sent to
                        │      │                   different and unrelated sites and domains.
                        │      │                   
                        │      │                   It could do this by exploiting a mixed case flaw in curl's
                        │      │                   function that
                        │      │                   verifies a given cookie domain against the Public Suffix
                        │      │                   List (PSL). For
                        │      │                   example a cookie could be set with `domain=co.UK` when the
                        │      │                   URL used a lower
                        │      │                   case hostname `curl.co.uk`, even though `co.uk` is listed as
                        │      │                    a PSL domain.
                        │      │                    
                        │      ├ Severity        : MEDIUM 
                        │      ├ VendorSeverity   ╭ amazon     : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           L/I:L/A:N 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           L/I:N/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-46218 
                        │      │                  ├ [1] : https://curl.se/docs/CVE-2023-46218.html 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-46218 
                        │      │                  ├ [3] : https://hackerone.com/reports/2212193 
                        │      │                  ├ [4] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/12/msg00015.html 
                        │      │                  ├ [5] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/3ZX3VW
                        │      │                  │       67N4ACRAPMV2QS2LVYGD7H2MVE/ 
                        │      │                  ├ [6] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/UOGXU2
                        │      │                  │       5FMMT2X6UUITQ7EZZYMJ42YWWD/ 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2023-46218 
                        │      │                  ├ [8] : https://security.netapp.com/advisory/ntap-202401
                        │      │                  │       25-0007/ 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-6535-1 
                        │      │                  ├ [10]: https://www.cve.org/CVERecord?id=CVE-2023-46218 
                        │      │                  ╰ [11]: https://www.debian.org/security/2023/dsa-5587 
                        │      ├ PublishedDate   : 2023-12-07T01:15:07.16Z 
                        │      ╰ LastModifiedDate: 2024-01-25T14:15:26.117Z 
                        ├ [10] ╭ VulnerabilityID : CVE-2022-48554 
                        │      ├ PkgID           : file-libs@5.39-14.el9.x86_64 
                        │      ├ PkgName         : file-libs 
                        │      ├ InstalledVersion: 5.39-14.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-48554 
                        │      ├ Title           : file: stack-based buffer over-read in file_copystr in
                        │      │                   funcs.c 
                        │      ├ Description     : File before 5.43 has an stack-based buffer over-read in
                        │      │                    file_copystr in funcs.c. NOTE: "File" is the name of an
                        │      │                   Open Source project. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-125 
                        │      ├ VendorSeverity   ╭ amazon: 1 
                        │      │                  ├ nvd   : 2 
                        │      │                  ├ redhat: 1 
                        │      │                  ╰ ubuntu: 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-48554 
                        │      │                  ├ [1]: https://bugs.astron.com/view.php?id=310 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2022-48554 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2022-48554 
                        │      │                  ├ [4]: https://security.netapp.com/advisory/ntap-2023111
                        │      │                  │      6-0002/ 
                        │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-6359-1 
                        │      │                  ├ [6]: https://www.cve.org/CVERecord?id=CVE-2022-48554 
                        │      │                  ╰ [7]: https://www.debian.org/security/2023/dsa-5489 
                        │      ├ PublishedDate   : 2023-08-22T19:16:31.757Z 
                        │      ╰ LastModifiedDate: 2023-12-27T22:04:16.397Z 
                        ├ [11] ╭ VulnerabilityID : CVE-2023-4156 
                        │      ├ PkgID           : gawk@5.1.0-6.el9.x86_64 
                        │      ├ PkgName         : gawk 
                        │      ├ InstalledVersion: 5.1.0-6.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-4156 
                        │      ├ Title           : gawk: heap out of bound read in builtin.c 
                        │      ├ Description     : A heap out-of-bounds read flaw was found in builtin.c
                        │      │                   in the gawk package. This issue may lead to a crash and
                        │      │                   could be used to read sensitive information. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-125 
                        │      ├ VendorSeverity   ╭ amazon     : 1 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 3 
                        │      │                  ├ photon     : 3 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           H/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.1 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           L/I:N/A:H 
                        │      │                           ╰ V3Score : 6.1 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-4156 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2215930 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-4156 
                        │      │                  ├ [3]: https://git.savannah.gnu.org/gitweb/?p=gawk.git;a
                        │      │                  │      =commitdiff;h=e709eb829448ce040087a3fc5481db6bfcaae212
                        │      │                  │       (gawk-5.2.0) 
                        │      │                  ├ [4]: https://mail.gnu.org/archive/html/bug-gawk/2022-0
                        │      │                  │      8/msg00000.html 
                        │      │                  ├ [5]: https://mail.gnu.org/archive/html/bug-gawk/2022-0
                        │      │                  │      8/msg00023.html 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-4156 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-6373-1 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-4156 
                        │      ├ PublishedDate   : 2023-09-25T18:15:11.013Z 
                        │      ╰ LastModifiedDate: 2023-11-07T04:22:11.937Z 
                        ├ [12] ╭ VulnerabilityID : CVE-2023-32636 
                        │      ├ PkgID           : glib2@2.68.4-11.el9.x86_64 
                        │      ├ PkgName         : glib2 
                        │      ├ InstalledVersion: 2.68.4-11.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-32636 
                        │      ├ Title           : glib: Timeout in fuzz_variant_text 
                        │      ├ Description     : A flaw was found in glib, where the gvariant
                        │      │                   deserialization code is vulnerable to a denial of service
                        │      │                   introduced by additional input validation added to resolve
                        │      │                   CVE-2023-29499. The offset table validation may be very
                        │      │                   slow. This bug does not affect any released version of glib
                        │      │                   but does affect glib distributors who followed the guidance
                        │      │                   of glib developers to backport the initial fix for
                        │      │                   CVE-2023-29499. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ╭ [0]: CWE-502 
                        │      │                  ╰ [1]: CWE-400 
                        │      ├ VendorSeverity   ╭ nvd   : 3 
                        │      │                  ├ photon: 3 
                        │      │                  ├ redhat: 1 
                        │      │                  ╰ ubuntu: 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-32636 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-32636 
                        │      │                  ├ [2]: https://discourse.gnome.org/t/multiple-fixes-for-
                        │      │                  │      gvariant-normalisation-issues-in-glib/12835 
                        │      │                  ├ [3]: https://gitlab.gnome.org/GNOME/glib/-/issues/2841 
                        │      │                  ├ [4]: https://https://discourse.gnome.org/t/multiple-fi
                        │      │                  │      xes-for-gvariant-normalisation-issues-in-glib/12835
                        │      │                  │       
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-32636 
                        │      │                  ├ [6]: https://security.netapp.com/advisory/ntap-2023111
                        │      │                  │      0-0002/ 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-6165-1 
                        │      │                  ├ [8]: https://ubuntu.com/security/notices/USN-6165-2 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-32636 
                        │      ├ PublishedDate   : 2023-09-14T20:15:09.653Z 
                        │      ╰ LastModifiedDate: 2024-01-12T22:09:56.247Z 
                        ├ [13] ╭ VulnerabilityID : CVE-2022-3219 
                        │      ├ PkgID           : gnupg2@2.3.3-4.el9.x86_64 
                        │      ├ PkgName         : gnupg2 
                        │      ├ InstalledVersion: 2.3.3-4.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-3219 
                        │      ├ Title           : denial of service issue (resource consumption) using
                        │      │                   compressed packets 
                        │      ├ Description     : GnuPG can be made to spin on a relatively small input
                        │      │                   by (for example) crafting a public key with thousands of
                        │      │                   signatures attached, compressed down to just a few KB. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-787 
                        │      ├ VendorSeverity   ╭ nvd   : 1 
                        │      │                  ├ redhat: 1 
                        │      │                  ╰ ubuntu: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:L 
                        │      │                  │        ╰ V3Score : 3.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-3219 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2127010 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2022-3219 
                        │      │                  ├ [3]: https://dev.gnupg.org/D556 
                        │      │                  ├ [4]: https://dev.gnupg.org/T5993 
                        │      │                  ├ [5]: https://marc.info/?l=oss-security&m=1656965902114
                        │      │                  │      34&w=4 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2022-3219 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-2023032
                        │      │                  │      4-0001/ 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2022-3219 
                        │      ├ PublishedDate   : 2023-02-23T20:15:12.393Z 
                        │      ╰ LastModifiedDate: 2023-05-26T16:31:34.07Z 
                        ├ [14] ╭ VulnerabilityID : CVE-2023-5981 
                        │      ├ VendorIDs        ─ [0]: RHSA-2024:0533 
                        │      ├ PkgID           : gnutls@3.7.6-23.el9.x86_64 
                        │      ├ PkgName         : gnutls 
                        │      ├ InstalledVersion: 3.7.6-23.el9 
                        │      ├ FixedVersion    : 3.7.6-23.el9_3.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-5981 
                        │      ├ Title           : gnutls: timing side-channel in the RSA-PSK authentication 
                        │      ├ Description     : A vulnerability was found that the response times to
                        │      │                   malformed ciphertexts in RSA-PSK ClientKeyExchange differ
                        │      │                   from response times of ciphertexts with correct PKCS#1 v1.5
                        │      │                   padding. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ├ rocky      : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2024/
                        │      │                  │       01/19/3 
                        │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2024:0155 
                        │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2024:0319 
                        │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2024:0399 
                        │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2024:0451 
                        │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2024:0533 
                        │      │                  ├ [6] : https://access.redhat.com/security/cve/CVE-2023-5981 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2248445 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/2258412 
                        │      │                  ├ [9] : https://bugzilla.redhat.com/2258544 
                        │      │                  ├ [10]: https://bugzilla.redhat.com/show_bug.cgi?id=2248445 
                        │      │                  ├ [11]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-5981 
                        │      │                  ├ [12]: https://errata.almalinux.org/9/ALSA-2024-0533.html 
                        │      │                  ├ [13]: https://errata.rockylinux.org/RLSA-2024:0155 
                        │      │                  ├ [14]: https://gnutls.org/security-new.html#GNUTLS-SA-2
                        │      │                  │       023-10-23 
                        │      │                  ├ [15]: https://linux.oracle.com/cve/CVE-2023-5981.html 
                        │      │                  ├ [16]: https://linux.oracle.com/errata/ELSA-2024-0155.html 
                        │      │                  ├ [17]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/GNXKVR
                        │      │                  │       5YNUEBNHAHM5GSYKBZX4W2HMN2/ 
                        │      │                  ├ [18]: https://lists.gnupg.org/pipermail/gnutls-help/20
                        │      │                  │       23-November/004837.html 
                        │      │                  ├ [19]: https://nvd.nist.gov/vuln/detail/CVE-2023-5981 
                        │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6499-1 
                        │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-6499-2 
                        │      │                  ╰ [22]: https://www.cve.org/CVERecord?id=CVE-2023-5981 
                        │      ├ PublishedDate   : 2023-11-28T12:15:07.04Z 
                        │      ╰ LastModifiedDate: 2024-01-29T16:15:08.063Z 
                        ├ [15] ╭ VulnerabilityID : CVE-2024-0553 
                        │      ├ VendorIDs        ─ [0]: RHSA-2024:0533 
                        │      ├ PkgID           : gnutls@3.7.6-23.el9.x86_64 
                        │      ├ PkgName         : gnutls 
                        │      ├ InstalledVersion: 3.7.6-23.el9 
                        │      ├ FixedVersion    : 3.7.6-23.el9_3.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-0553 
                        │      ├ Title           : gnutls: incomplete fix for CVE-2023-5981 
                        │      ├ Description     : A vulnerability was found in GnuTLS. The response times
                        │      │                    to malformed ciphertexts in RSA-PSK ClientKeyExchange
                        │      │                   differ from the response times of ciphertexts with correct
                        │      │                   PKCS#1 v1.5 padding. This issue may allow a remote attacker
                        │      │                   to perform a timing side-channel attack in the RSA-PSK key
                        │      │                   exchange, potentially leading to the leakage of sensitive
                        │      │                   data. CVE-2024-0553 is designated as an incomplete
                        │      │                   resolution for CVE-2023-5981. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ VendorSeverity   ╭ alma  : 2 
                        │      │                  ├ nvd   : 3 
                        │      │                  ├ redhat: 2 
                        │      │                  ╰ ubuntu: 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2024/
                        │      │                  │       01/19/3 
                        │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2024:0533 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2024-0553 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2248445 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2258412 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2258544 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2258412 
                        │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2024-0553 
                        │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2024-0533.html 
                        │      │                  ├ [9] : https://gitlab.com/gnutls/gnutls/-/issues/1522 
                        │      │                  ├ [10]: https://gnutls.org/security-new.html#GNUTLS-SA-2
                        │      │                  │       024-01-14 
                        │      │                  ├ [11]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/GNXKVR
                        │      │                  │       5YNUEBNHAHM5GSYKBZX4W2HMN2/ 
                        │      │                  ├ [12]: https://lists.gnupg.org/pipermail/gnutls-help/20
                        │      │                  │       24-January/004841.html 
                        │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-0553 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6593-1 
                        │      │                  ╰ [15]: https://www.cve.org/CVERecord?id=CVE-2024-0553 
                        │      ├ PublishedDate   : 2024-01-16T12:15:45.557Z 
                        │      ╰ LastModifiedDate: 2024-01-29T17:15:09.36Z 
                        ├ [16] ╭ VulnerabilityID : CVE-2024-0567 
                        │      ├ VendorIDs        ─ [0]: RHSA-2024:0533 
                        │      ├ PkgID           : gnutls@3.7.6-23.el9.x86_64 
                        │      ├ PkgName         : gnutls 
                        │      ├ InstalledVersion: 3.7.6-23.el9 
                        │      ├ FixedVersion    : 3.7.6-23.el9_3.3 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-0567 
                        │      ├ Title           : gnutls: rejects certificate chain with distributed trust 
                        │      ├ Description     : A vulnerability was found in GnuTLS, where a cockpit
                        │      │                   (which uses gnuTLS) rejects a certificate chain with
                        │      │                   distributed trust. This issue occurs when validating a
                        │      │                   certificate chain with cockpit-certificate-ensure. This flaw
                        │      │                    allows an unauthenticated, remote client or attacker to
                        │      │                   initiate a denial of service attack. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-347 
                        │      ├ VendorSeverity   ╭ alma  : 2 
                        │      │                  ├ nvd   : 3 
                        │      │                  ├ redhat: 2 
                        │      │                  ╰ ubuntu: 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2024/
                        │      │                  │       01/19/3 
                        │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2024:0533 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2024-0567 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2248445 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2258412 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2258544 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2258544 
                        │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2024-0567 
                        │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2024-0533.html 
                        │      │                  ├ [9] : https://gitlab.com/gnutls/gnutls/-/issues/1521 
                        │      │                  ├ [10]: https://gnutls.org/security-new.html#GNUTLS-SA-2
                        │      │                  │       024-01-09 
                        │      │                  ├ [11]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/GNXKVR
                        │      │                  │       5YNUEBNHAHM5GSYKBZX4W2HMN2/ 
                        │      │                  ├ [12]: https://lists.gnupg.org/pipermail/gnutls-help/20
                        │      │                  │       24-January/004841.html 
                        │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2024-0567 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6593-1 
                        │      │                  ╰ [15]: https://www.cve.org/CVERecord?id=CVE-2024-0567 
                        │      ├ PublishedDate   : 2024-01-16T14:15:48.527Z 
                        │      ╰ LastModifiedDate: 2024-01-29T16:15:08.18Z 
                        ├ [17] ╭ VulnerabilityID : CVE-2023-25193 
                        │      ├ PkgID           : harfbuzz@2.7.4-8.el9.x86_64 
                        │      ├ PkgName         : harfbuzz 
                        │      ├ InstalledVersion: 2.7.4-8.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-25193 
                        │      ├ Title           : harfbuzz: allows attackers to trigger O(n^2) growth via
                        │      │                    consecutive marks 
                        │      ├ Description     : hb-ot-layout-gsubgpos.hh in HarfBuzz through 6.0.0
                        │      │                   allows attackers to trigger O(n^2) growth via consecutive
                        │      │                   marks during the process of looking back for base glyphs
                        │      │                   when attaching marks. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-770 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ nvd        : 3 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ photon     : 3 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:4177 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-25193 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2167254 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2221626 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2221634 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2221642 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2221645 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2221647 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/2223207 
                        │      │                  ├ [9] : https://chromium.googlesource.com/chromium/src/+
                        │      │                  │       /e1f324aa681af54101c1f2d173d92adb80e37088/DEPS#361
                        │      │                  │        
                        │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-25193 
                        │      │                  ├ [11]: https://errata.almalinux.org/9/ALSA-2023-4177.html 
                        │      │                  ├ [12]: https://github.com/harfbuzz/harfbuzz/blob/2822b5
                        │      │                  │       89bc837fae6f66233e2cf2eef0f6ce8470/src/hb-ot-layout-g
                        │      │                  │       subgpos.hh 
                        │      │                  ├ [13]: https://github.com/harfbuzz/harfbuzz/commit/85be
                        │      │                  │       877925ddbf34f74a1229f3ca1716bb6170dc 
                        │      │                  ├ [14]: https://github.com/harfbuzz/harfbuzz/commit/85be
                        │      │                  │       877925ddbf34f74a1229f3ca1716bb6170dc (reverted) 
                        │      │                  ├ [15]: https://linux.oracle.com/cve/CVE-2023-25193.html 
                        │      │                  ├ [16]: https://linux.oracle.com/errata/ELSA-2023-4233.html 
                        │      │                  ├ [17]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/KWCH
                        │      │                  │       WSICWVZSAXP2YAXM65JC2GR53547/ 
                        │      │                  ├ [18]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/YZ5M
                        │      │                  │       2GSAIHFPLHYJXUPQ2QDJCLWXUGO3/ 
                        │      │                  ├ [19]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/KWCHWS
                        │      │                  │       ICWVZSAXP2YAXM65JC2GR53547/ 
                        │      │                  ├ [20]: https://nvd.nist.gov/vuln/detail/CVE-2023-25193 
                        │      │                  ├ [21]: https://security.netapp.com/advisory/ntap-202307
                        │      │                  │       25-0006/ 
                        │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-6263-1 
                        │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6272-1 
                        │      │                  ╰ [24]: https://www.cve.org/CVERecord?id=CVE-2023-25193 
                        │      ├ PublishedDate   : 2023-02-04T20:15:08.027Z 
                        │      ╰ LastModifiedDate: 2023-11-07T04:08:55.837Z 
                        ├ [18] ╭ VulnerabilityID : CVE-2022-3857 
                        │      ├ PkgID           : java-1.8.0-openjdk-headless@1.8.0.402.b06-2.el9.x86_64 
                        │      ├ PkgName         : java-1.8.0-openjdk-headless 
                        │      ├ InstalledVersion: 1:1.8.0.402.b06-2.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-3857 
                        │      ├ Title           : Null pointer dereference leads to segmentation fault 
                        │      ├ Description     : A flaw was found in libpng 1.6.38. A crafted PNG image
                        │      │                   can lead to a segmentation fault and denial of service in
                        │      │                   png_setup_paeth_row() function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-476 
                        │      ├ VendorSeverity   ╭ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-3857 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2022-3857 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2022-3857 
                        │      │                  ├ [3]: https://security.netapp.com/advisory/ntap-2023040
                        │      │                  │      6-0004/ 
                        │      │                  ├ [4]: https://sourceforge.net/p/libpng/bugs/300/ 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2022-3857 
                        │      ├ PublishedDate   : 2023-03-06T23:15:11.087Z 
                        │      ╰ LastModifiedDate: 2023-04-06T13:15:08.467Z 
                        ├ [19] ╭ VulnerabilityID : CVE-2023-30571 
                        │      ├ PkgID           : libarchive@3.5.3-4.el9.x86_64 
                        │      ├ PkgName         : libarchive 
                        │      ├ InstalledVersion: 3.5.3-4.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-30571 
                        │      ├ Title           : libarchive: Race condition in multi-threaded use of
                        │      │                   archive_write_disk_header() on posix based systems 
                        │      ├ Description     : Libarchive through 3.6.2 can cause directories to have
                        │      │                   world-writable permissions. The umask() call inside
                        │      │                   archive_write_disk_posix.c changes the umask of the whole
                        │      │                   process for a very short period of time; a race condition
                        │      │                   with another thread can lead to a permanent umask 0 setting.
                        │      │                    Such a race condition could lead to implicit directory
                        │      │                   creation with permissions 0777 (without the sticky bit),
                        │      │                   which means that any low-privileged local user can delete
                        │      │                   and rename files inside those directories. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-362 
                        │      ├ VendorSeverity   ╭ nvd   : 2 
                        │      │                  ╰ redhat: 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:H 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:H 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-30571 
                        │      │                  ├ [1]: https://access.redhat.com/solutions/7033331 
                        │      │                  ├ [2]: https://github.com/libarchive/libarchive/issues/1876 
                        │      │                  ├ [3]: https://groups.google.com/g/libarchive-announce 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-30571 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-30571 
                        │      ├ PublishedDate   : 2023-05-29T20:15:09.513Z 
                        │      ╰ LastModifiedDate: 2023-06-05T16:40:57.93Z 
                        ├ [20] ╭ VulnerabilityID : CVE-2023-46218 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-26.el9_3.2.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-26.el9_3.2 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-46218 
                        │      ├ Title           : curl: information disclosure by exploiting a mixed case flaw 
                        │      ├ Description     : This flaw allows a malicious HTTP server to set "super
                        │      │                   cookies" in curl that
                        │      │                   are then passed back to more origins than what is otherwise
                        │      │                   allowed or
                        │      │                   possible. This allows a site to set cookies that then would
                        │      │                   get sent to
                        │      │                   different and unrelated sites and domains.
                        │      │                   
                        │      │                   It could do this by exploiting a mixed case flaw in curl's
                        │      │                   function that
                        │      │                   verifies a given cookie domain against the Public Suffix
                        │      │                   List (PSL). For
                        │      │                   example a cookie could be set with `domain=co.UK` when the
                        │      │                   URL used a lower
                        │      │                   case hostname `curl.co.uk`, even though `co.uk` is listed as
                        │      │                    a PSL domain.
                        │      │                    
                        │      ├ Severity        : MEDIUM 
                        │      ├ VendorSeverity   ╭ amazon     : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           L/I:L/A:N 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           L/I:N/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-46218 
                        │      │                  ├ [1] : https://curl.se/docs/CVE-2023-46218.html 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-46218 
                        │      │                  ├ [3] : https://hackerone.com/reports/2212193 
                        │      │                  ├ [4] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/12/msg00015.html 
                        │      │                  ├ [5] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/3ZX3VW
                        │      │                  │       67N4ACRAPMV2QS2LVYGD7H2MVE/ 
                        │      │                  ├ [6] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/UOGXU2
                        │      │                  │       5FMMT2X6UUITQ7EZZYMJ42YWWD/ 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2023-46218 
                        │      │                  ├ [8] : https://security.netapp.com/advisory/ntap-202401
                        │      │                  │       25-0007/ 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-6535-1 
                        │      │                  ├ [10]: https://www.cve.org/CVERecord?id=CVE-2023-46218 
                        │      │                  ╰ [11]: https://www.debian.org/security/2023/dsa-5587 
                        │      ├ PublishedDate   : 2023-12-07T01:15:07.16Z 
                        │      ╰ LastModifiedDate: 2024-01-25T14:15:26.117Z 
                        ├ [21] ╭ VulnerabilityID : CVE-2022-27943 
                        │      ├ PkgID           : libgcc@11.4.1-2.1.el9.x86_64 
                        │      ├ PkgName         : libgcc 
                        │      ├ InstalledVersion: 11.4.1-2.1.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-27943 
                        │      ├ Title           : libiberty/rust-demangle.c in GNU GCC 11.2 allows stack
                        │      │                   exhaustion in demangle_const 
                        │      ├ Description     : libiberty/rust-demangle.c in GNU GCC 11.2 allows stack
                        │      │                   consumption in demangle_const, as demonstrated by
                        │      │                   nm-new. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-674 
                        │      ├ VendorSeverity   ╭ amazon: 1 
                        │      │                  ├ nvd   : 2 
                        │      │                  ├ redhat: 1 
                        │      │                  ╰ ubuntu: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ├ V2Score : 4.3 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2022-27943 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2022-27943 
                        │      │                  ├ [2] : https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105039 
                        │      │                  ├ [3] : https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=1
                        │      │                  │       a770b01ef415e114164b6151d1e55acdee09371 
                        │      │                  ├ [4] : https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=9
                        │      │                  │       234cdca6ee88badfc00297e72f13dac4e540c79 
                        │      │                  ├ [5] : https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=f
                        │      │                  │       c968115a742d9e4674d9725ce9c2106b91b6ead 
                        │      │                  ├ [6] : https://gcc.gnu.org/pipermail/gcc-patches/2022-M
                        │      │                  │       arch/592244.html 
                        │      │                  ├ [7] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/H424
                        │      │                  │       YXGW7OKXS2NCAP35OP6Y4P4AW6VG/ 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2022-27943 
                        │      │                  ├ [9] : https://sourceware.org/bugzilla/show_bug.cgi?id=28995 
                        │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2022-27943 
                        │      ├ PublishedDate   : 2022-03-26T13:15:07.9Z 
                        │      ╰ LastModifiedDate: 2023-11-07T03:45:32.64Z 
                        ├ [22] ╭ VulnerabilityID : CVE-2022-3857 
                        │      ├ PkgID           : libpng@1.6.37-12.el9.x86_64 
                        │      ├ PkgName         : libpng 
                        │      ├ InstalledVersion: 2:1.6.37-12.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-3857 
                        │      ├ Title           : Null pointer dereference leads to segmentation fault 
                        │      ├ Description     : A flaw was found in libpng 1.6.38. A crafted PNG image
                        │      │                   can lead to a segmentation fault and denial of service in
                        │      │                   png_setup_paeth_row() function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-476 
                        │      ├ VendorSeverity   ╭ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-3857 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2022-3857 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2022-3857 
                        │      │                  ├ [3]: https://security.netapp.com/advisory/ntap-2023040
                        │      │                  │      6-0004/ 
                        │      │                  ├ [4]: https://sourceforge.net/p/libpng/bugs/300/ 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2022-3857 
                        │      ├ PublishedDate   : 2023-03-06T23:15:11.087Z 
                        │      ╰ LastModifiedDate: 2023-04-06T13:15:08.467Z 
                        ├ [23] ╭ VulnerabilityID : CVE-2022-27943 
                        │      ├ PkgID           : libstdc++@11.4.1-2.1.el9.x86_64 
                        │      ├ PkgName         : libstdc++ 
                        │      ├ InstalledVersion: 11.4.1-2.1.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-27943 
                        │      ├ Title           : libiberty/rust-demangle.c in GNU GCC 11.2 allows stack
                        │      │                   exhaustion in demangle_const 
                        │      ├ Description     : libiberty/rust-demangle.c in GNU GCC 11.2 allows stack
                        │      │                   consumption in demangle_const, as demonstrated by
                        │      │                   nm-new. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-674 
                        │      ├ VendorSeverity   ╭ amazon: 1 
                        │      │                  ├ nvd   : 2 
                        │      │                  ├ redhat: 1 
                        │      │                  ╰ ubuntu: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ├ V2Score : 4.3 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2022-27943 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2022-27943 
                        │      │                  ├ [2] : https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105039 
                        │      │                  ├ [3] : https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=1
                        │      │                  │       a770b01ef415e114164b6151d1e55acdee09371 
                        │      │                  ├ [4] : https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=9
                        │      │                  │       234cdca6ee88badfc00297e72f13dac4e540c79 
                        │      │                  ├ [5] : https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=f
                        │      │                  │       c968115a742d9e4674d9725ce9c2106b91b6ead 
                        │      │                  ├ [6] : https://gcc.gnu.org/pipermail/gcc-patches/2022-M
                        │      │                  │       arch/592244.html 
                        │      │                  ├ [7] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/H424
                        │      │                  │       YXGW7OKXS2NCAP35OP6Y4P4AW6VG/ 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2022-27943 
                        │      │                  ├ [9] : https://sourceware.org/bugzilla/show_bug.cgi?id=28995 
                        │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2022-27943 
                        │      ├ PublishedDate   : 2022-03-26T13:15:07.9Z 
                        │      ╰ LastModifiedDate: 2023-11-07T03:45:32.64Z 
                        ├ [24] ╭ VulnerabilityID : CVE-2023-45322 
                        │      ├ PkgID           : libxml2@2.9.13-5.el9_3.x86_64 
                        │      ├ PkgName         : libxml2 
                        │      ├ InstalledVersion: 2.9.13-5.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-45322 
                        │      ├ Title           : libxml2: use-after-free in xmlUnlinkNode() in tree.c 
                        │      ├ Description     : libxml2 through 2.11.5 has a use-after-free that can
                        │      │                   only occur after a certain memory allocation fails. This
                        │      │                   occurs in xmlUnlinkNode in tree.c. NOTE: the vendor's
                        │      │                   position is "I don't think these issues are critical enough
                        │      │                   to warrant a CVE ID ... because an attacker typically can't
                        │      │                   control when memory allocations fail." 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-416 
                        │      ├ VendorSeverity   ╭ amazon     : 3 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ╰ redhat     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2023/1
                        │      │                  │      0/06/5 
                        │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2023-45322 
                        │      │                  ├ [2]: https://gitlab.gnome.org/GNOME/libxml2/-/issues/344 
                        │      │                  ├ [3]: https://gitlab.gnome.org/GNOME/libxml2/-/issues/583 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-45322 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-45322 
                        │      ├ PublishedDate   : 2023-10-06T22:15:11.66Z 
                        │      ╰ LastModifiedDate: 2023-11-07T04:21:45Z 
                        ├ [25] ╭ VulnerabilityID : CVE-2022-4899 
                        │      ├ PkgID           : libzstd@1.5.1-2.el9.x86_64 
                        │      ├ PkgName         : libzstd 
                        │      ├ InstalledVersion: 1.5.1-2.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-4899 
                        │      ├ Title           : zstd: mysql: buffer overrun in util.c 
                        │      ├ Description     : A vulnerability was found in zstd v1.4.10, where an
                        │      │                   attacker can supply empty string as an argument to the
                        │      │                   command line tool to cause buffer overrun. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-400 
                        │      ├ VendorSeverity   ╭ amazon: 2 
                        │      │                  ├ ghsa  : 3 
                        │      │                  ├ nvd   : 3 
                        │      │                  ├ photon: 3 
                        │      │                  ├ redhat: 1 
                        │      │                  ╰ ubuntu: 1 
                        │      ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2022-4899 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2022-4899 
                        │      │                  ├ [2] : https://github.com/facebook/zstd 
                        │      │                  ├ [3] : https://github.com/facebook/zstd/issues/3200 
                        │      │                  ├ [4] : https://github.com/facebook/zstd/pull/3220 
                        │      │                  ├ [5] : https://github.com/pypa/advisory-database/tree/m
                        │      │                  │       ain/vulns/zstd/PYSEC-2023-121.yaml 
                        │      │                  ├ [6] : https://github.com/sergey-dryabzhinsky/python-zs
                        │      │                  │       td/commit/c8a619aebdbd6b838fbfef6e19325a70f631a4c6
                        │      │                  │        
                        │      │                  ├ [7] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/C63H
                        │      │                  │       AGVLQA6FJNDCHR7CNZZL6VSLILB2/ 
                        │      │                  ├ [8] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/JEHR
                        │      │                  │       BBYYTPA4DETOM5XAKGCP37NUTLOA/ 
                        │      │                  ├ [9] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/QYLD
                        │      │                  │       K6ODVC4LJSDULLX6Q2YHTFOWABCN/ 
                        │      │                  ├ [10]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/C63HAG
                        │      │                  │       VLQA6FJNDCHR7CNZZL6VSLILB2/ 
                        │      │                  ├ [11]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/JEHRBB
                        │      │                  │       YYTPA4DETOM5XAKGCP37NUTLOA/ 
                        │      │                  ├ [12]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/QYLDK6
                        │      │                  │       ODVC4LJSDULLX6Q2YHTFOWABCN/ 
                        │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2022-4899 
                        │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202307
                        │      │                  │       25-0005/ 
                        │      │                  ╰ [15]: https://www.cve.org/CVERecord?id=CVE-2022-4899 
                        │      ├ PublishedDate   : 2023-03-31T20:15:07.213Z 
                        │      ╰ LastModifiedDate: 2023-11-07T03:59:16.09Z 
                        ├ [26] ╭ VulnerabilityID : CVE-2022-29458 
                        │      ├ PkgID           : ncurses-base@6.2-10.20210508.el9.noarch 
                        │      ├ PkgName         : ncurses-base 
                        │      ├ InstalledVersion: 6.2-10.20210508.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-29458 
                        │      ├ Title           : segfaulting OOB read 
                        │      ├ Description     : ncurses 6.3 before patch 20220416 has an out-of-bounds
                        │      │                   read and segmentation violation in convert_strings in
                        │      │                   tinfo/read_entry.c in the terminfo library. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-125 
                        │      ├ VendorSeverity   ╭ amazon     : 2 
                        │      │                  ├ cbl-mariner: 3 
                        │      │                  ├ nvd        : 3 
                        │      │                  ├ photon     : 3 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:P/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           H/I:N/A:H 
                        │      │                  │        ├ V2Score : 5.8 
                        │      │                  │        ╰ V3Score : 7.1 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           L/I:N/A:H 
                        │      │                           ╰ V3Score : 6.1 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2022/Oct/28 
                        │      │                  ├ [1] : http://seclists.org/fulldisclosure/2022/Oct/41 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2022-29458 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2022-29458 
                        │      │                  ├ [4] : https://invisible-island.net/ncurses/NEWS.html#t
                        │      │                  │       20220416 
                        │      │                  ├ [5] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       2/10/msg00037.html 
                        │      │                  ├ [6] : https://lists.gnu.org/archive/html/bug-ncurses/2
                        │      │                  │       022-04/msg00014.html 
                        │      │                  ├ [7] : https://lists.gnu.org/archive/html/bug-ncurses/2
                        │      │                  │       022-04/msg00016.html 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2022-29458 
                        │      │                  ├ [9] : https://support.apple.com/kb/HT213488 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-5477-1 
                        │      │                  ├ [11]: https://ubuntu.com/security/notices/USN-6099-1 
                        │      │                  ╰ [12]: https://www.cve.org/CVERecord?id=CVE-2022-29458 
                        │      ├ PublishedDate   : 2022-04-18T21:15:07.6Z 
                        │      ╰ LastModifiedDate: 2023-11-07T03:46:02.1Z 
                        ├ [27] ╭ VulnerabilityID : CVE-2023-50495 
                        │      ├ PkgID           : ncurses-base@6.2-10.20210508.el9.noarch 
                        │      ├ PkgName         : ncurses-base 
                        │      ├ InstalledVersion: 6.2-10.20210508.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-50495 
                        │      ├ Title           : ncurses: segmentation fault via _nc_wrap_entry() 
                        │      ├ Description     : NCurse v6.4-20230418 was discovered to contain a
                        │      │                   segmentation fault via the component _nc_wrap_entry(). 
                        │      ├ Severity        : LOW 
                        │      ├ VendorSeverity   ╭ amazon: 2 
                        │      │                  ├ nvd   : 2 
                        │      │                  ╰ redhat: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-50495 
                        │      │                  ├ [1]: https://lists.gnu.org/archive/html/bug-ncurses/20
                        │      │                  │      23-04/msg00020.html 
                        │      │                  ├ [2]: https://lists.gnu.org/archive/html/bug-ncurses/20
                        │      │                  │      23-04/msg00029.html 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-50495 
                        │      │                  ├ [4]: https://security.netapp.com/advisory/ntap-2024011
                        │      │                  │      9-0008/ 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-50495 
                        │      ├ PublishedDate   : 2023-12-12T15:15:07.867Z 
                        │      ╰ LastModifiedDate: 2024-01-19T16:15:10.193Z 
                        ├ [28] ╭ VulnerabilityID : CVE-2022-29458 
                        │      ├ PkgID           : ncurses-libs@6.2-10.20210508.el9.x86_64 
                        │      ├ PkgName         : ncurses-libs 
                        │      ├ InstalledVersion: 6.2-10.20210508.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-29458 
                        │      ├ Title           : segfaulting OOB read 
                        │      ├ Description     : ncurses 6.3 before patch 20220416 has an out-of-bounds
                        │      │                   read and segmentation violation in convert_strings in
                        │      │                   tinfo/read_entry.c in the terminfo library. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-125 
                        │      ├ VendorSeverity   ╭ amazon     : 2 
                        │      │                  ├ cbl-mariner: 3 
                        │      │                  ├ nvd        : 3 
                        │      │                  ├ photon     : 3 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:P/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           H/I:N/A:H 
                        │      │                  │        ├ V2Score : 5.8 
                        │      │                  │        ╰ V3Score : 7.1 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           L/I:N/A:H 
                        │      │                           ╰ V3Score : 6.1 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2022/Oct/28 
                        │      │                  ├ [1] : http://seclists.org/fulldisclosure/2022/Oct/41 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2022-29458 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2022-29458 
                        │      │                  ├ [4] : https://invisible-island.net/ncurses/NEWS.html#t
                        │      │                  │       20220416 
                        │      │                  ├ [5] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       2/10/msg00037.html 
                        │      │                  ├ [6] : https://lists.gnu.org/archive/html/bug-ncurses/2
                        │      │                  │       022-04/msg00014.html 
                        │      │                  ├ [7] : https://lists.gnu.org/archive/html/bug-ncurses/2
                        │      │                  │       022-04/msg00016.html 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2022-29458 
                        │      │                  ├ [9] : https://support.apple.com/kb/HT213488 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-5477-1 
                        │      │                  ├ [11]: https://ubuntu.com/security/notices/USN-6099-1 
                        │      │                  ╰ [12]: https://www.cve.org/CVERecord?id=CVE-2022-29458 
                        │      ├ PublishedDate   : 2022-04-18T21:15:07.6Z 
                        │      ╰ LastModifiedDate: 2023-11-07T03:46:02.1Z 
                        ├ [29] ╭ VulnerabilityID : CVE-2023-50495 
                        │      ├ PkgID           : ncurses-libs@6.2-10.20210508.el9.x86_64 
                        │      ├ PkgName         : ncurses-libs 
                        │      ├ InstalledVersion: 6.2-10.20210508.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-50495 
                        │      ├ Title           : ncurses: segmentation fault via _nc_wrap_entry() 
                        │      ├ Description     : NCurse v6.4-20230418 was discovered to contain a
                        │      │                   segmentation fault via the component _nc_wrap_entry(). 
                        │      ├ Severity        : LOW 
                        │      ├ VendorSeverity   ╭ amazon: 2 
                        │      │                  ├ nvd   : 2 
                        │      │                  ╰ redhat: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-50495 
                        │      │                  ├ [1]: https://lists.gnu.org/archive/html/bug-ncurses/20
                        │      │                  │      23-04/msg00020.html 
                        │      │                  ├ [2]: https://lists.gnu.org/archive/html/bug-ncurses/20
                        │      │                  │      23-04/msg00029.html 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-50495 
                        │      │                  ├ [4]: https://security.netapp.com/advisory/ntap-2024011
                        │      │                  │      9-0008/ 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-50495 
                        │      ├ PublishedDate   : 2023-12-12T15:15:07.867Z 
                        │      ╰ LastModifiedDate: 2024-01-19T16:15:10.193Z 
                        ├ [30] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nspr@4.35.0-4.el9_3.x86_64 
                        │      ├ PkgName         : nspr 
                        │      ├ InstalledVersion: 4.35.0-4.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : nss: Information exposure when DH secret are reused
                        │      │                   across multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE
                        │      │                   ciphersuites inherit in the TLS specification. To mitigate
                        │      │                   this vulnerability, Firefox disabled support for DHE
                        │      │                   ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ VendorSeverity   ╭ nvd   : 2 
                        │      │                  ╰ redhat: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2020-12413 
                        │      │                  ├ [1]: https://bugzilla.mozilla.org/show_bug.cgi?id=CVE-
                        │      │                  │      2020-12413 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2020-12413 
                        │      │                  ├ [3]: https://raccoon-attack.com/ 
                        │      │                  ├ [4]: https://raccoon-attack.com/RacoonAttack.pdf 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2020-12413 
                        │      ├ PublishedDate   : 2023-02-16T22:15:10.58Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:51.89Z 
                        ├ [31] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss@3.90.0-4.el9_3.x86_64 
                        │      ├ PkgName         : nss 
                        │      ├ InstalledVersion: 3.90.0-4.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : nss: Information exposure when DH secret are reused
                        │      │                   across multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE
                        │      │                   ciphersuites inherit in the TLS specification. To mitigate
                        │      │                   this vulnerability, Firefox disabled support for DHE
                        │      │                   ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ VendorSeverity   ╭ nvd   : 2 
                        │      │                  ╰ redhat: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2020-12413 
                        │      │                  ├ [1]: https://bugzilla.mozilla.org/show_bug.cgi?id=CVE-
                        │      │                  │      2020-12413 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2020-12413 
                        │      │                  ├ [3]: https://raccoon-attack.com/ 
                        │      │                  ├ [4]: https://raccoon-attack.com/RacoonAttack.pdf 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2020-12413 
                        │      ├ PublishedDate   : 2023-02-16T22:15:10.58Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:51.89Z 
                        ├ [32] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss-softokn@3.90.0-4.el9_3.x86_64 
                        │      ├ PkgName         : nss-softokn 
                        │      ├ InstalledVersion: 3.90.0-4.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : nss: Information exposure when DH secret are reused
                        │      │                   across multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE
                        │      │                   ciphersuites inherit in the TLS specification. To mitigate
                        │      │                   this vulnerability, Firefox disabled support for DHE
                        │      │                   ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ VendorSeverity   ╭ nvd   : 2 
                        │      │                  ╰ redhat: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2020-12413 
                        │      │                  ├ [1]: https://bugzilla.mozilla.org/show_bug.cgi?id=CVE-
                        │      │                  │      2020-12413 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2020-12413 
                        │      │                  ├ [3]: https://raccoon-attack.com/ 
                        │      │                  ├ [4]: https://raccoon-attack.com/RacoonAttack.pdf 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2020-12413 
                        │      ├ PublishedDate   : 2023-02-16T22:15:10.58Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:51.89Z 
                        ├ [33] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss-softokn-freebl@3.90.0-4.el9_3.x86_64 
                        │      ├ PkgName         : nss-softokn-freebl 
                        │      ├ InstalledVersion: 3.90.0-4.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : nss: Information exposure when DH secret are reused
                        │      │                   across multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE
                        │      │                   ciphersuites inherit in the TLS specification. To mitigate
                        │      │                   this vulnerability, Firefox disabled support for DHE
                        │      │                   ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ VendorSeverity   ╭ nvd   : 2 
                        │      │                  ╰ redhat: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2020-12413 
                        │      │                  ├ [1]: https://bugzilla.mozilla.org/show_bug.cgi?id=CVE-
                        │      │                  │      2020-12413 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2020-12413 
                        │      │                  ├ [3]: https://raccoon-attack.com/ 
                        │      │                  ├ [4]: https://raccoon-attack.com/RacoonAttack.pdf 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2020-12413 
                        │      ├ PublishedDate   : 2023-02-16T22:15:10.58Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:51.89Z 
                        ├ [34] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss-sysinit@3.90.0-4.el9_3.x86_64 
                        │      ├ PkgName         : nss-sysinit 
                        │      ├ InstalledVersion: 3.90.0-4.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : nss: Information exposure when DH secret are reused
                        │      │                   across multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE
                        │      │                   ciphersuites inherit in the TLS specification. To mitigate
                        │      │                   this vulnerability, Firefox disabled support for DHE
                        │      │                   ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ VendorSeverity   ╭ nvd   : 2 
                        │      │                  ╰ redhat: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2020-12413 
                        │      │                  ├ [1]: https://bugzilla.mozilla.org/show_bug.cgi?id=CVE-
                        │      │                  │      2020-12413 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2020-12413 
                        │      │                  ├ [3]: https://raccoon-attack.com/ 
                        │      │                  ├ [4]: https://raccoon-attack.com/RacoonAttack.pdf 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2020-12413 
                        │      ├ PublishedDate   : 2023-02-16T22:15:10.58Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:51.89Z 
                        ├ [35] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss-util@3.90.0-4.el9_3.x86_64 
                        │      ├ PkgName         : nss-util 
                        │      ├ InstalledVersion: 3.90.0-4.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : nss: Information exposure when DH secret are reused
                        │      │                   across multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE
                        │      │                   ciphersuites inherit in the TLS specification. To mitigate
                        │      │                   this vulnerability, Firefox disabled support for DHE
                        │      │                   ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ VendorSeverity   ╭ nvd   : 2 
                        │      │                  ╰ redhat: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2020-12413 
                        │      │                  ├ [1]: https://bugzilla.mozilla.org/show_bug.cgi?id=CVE-
                        │      │                  │      2020-12413 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2020-12413 
                        │      │                  ├ [3]: https://raccoon-attack.com/ 
                        │      │                  ├ [4]: https://raccoon-attack.com/RacoonAttack.pdf 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2020-12413 
                        │      ├ PublishedDate   : 2023-02-16T22:15:10.58Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:51.89Z 
                        ├ [36] ╭ VulnerabilityID : CVE-2023-2953 
                        │      ├ PkgID           : openldap@2.6.3-1.el9.x86_64 
                        │      ├ PkgName         : openldap 
                        │      ├ InstalledVersion: 2.6.3-1.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2953 
                        │      ├ Title           : null pointer dereference in  ber_memalloc_x  function 
                        │      ├ Description     : A vulnerability was found in openldap. This security
                        │      │                   flaw causes a null pointer dereference in ber_memalloc_x()
                        │      │                   function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-476 
                        │      ├ VendorSeverity   ╭ amazon : 2 
                        │      │                  ├ bitnami: 3 
                        │      │                  ├ nvd    : 3 
                        │      │                  ├ photon : 3 
                        │      │                  ├ redhat : 1 
                        │      │                  ╰ ubuntu : 1 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ├ nvd     ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C
                        │      │                            │           :N/I:L/A:H 
                        │      │                            ╰ V3Score : 7.1 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2023/Jul/47 
                        │      │                  ├ [1] : http://seclists.org/fulldisclosure/2023/Jul/48 
                        │      │                  ├ [2] : http://seclists.org/fulldisclosure/2023/Jul/52 
                        │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2023-2953 
                        │      │                  ├ [4] : https://bugs.openldap.org/show_bug.cgi?id=9904 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-2953 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-2953 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-202307
                        │      │                  │       03-0005/ 
                        │      │                  ├ [8] : https://support.apple.com/kb/HT213843 
                        │      │                  ├ [9] : https://support.apple.com/kb/HT213844 
                        │      │                  ├ [10]: https://support.apple.com/kb/HT213845 
                        │      │                  ├ [11]: https://ubuntu.com/security/notices/USN-6197-1 
                        │      │                  ├ [12]: https://ubuntu.com/security/notices/USN-6616-1 
                        │      │                  ╰ [13]: https://www.cve.org/CVERecord?id=CVE-2023-2953 
                        │      ├ PublishedDate   : 2023-05-30T22:15:10.613Z 
                        │      ╰ LastModifiedDate: 2023-08-02T16:46:03.663Z 
                        ├ [37] ╭ VulnerabilityID : CVE-2023-2975 
                        │      ├ PkgID           : openssl@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2975 
                        │      ├ Title           : openssl: AES-SIV cipher implementation contains a bug
                        │      │                   that causes it to ignore empty associated data entries 
                        │      ├ Description     : Issue summary: The AES-SIV cipher implementation
                        │      │                   contains a bug that causes
                        │      │                   it to ignore empty associated data entries which are
                        │      │                   unauthenticated as
                        │      │                   a consequence.
                        │      │                   
                        │      │                   Impact summary: Applications that use the AES-SIV algorithm
                        │      │                   and want to
                        │      │                   authenticate empty data entries as associated data can be
                        │      │                   mislead by removing
                        │      │                   adding or reordering such empty entries as these are ignored
                        │      │                    by the OpenSSL
                        │      │                   implementation. We are currently unaware of any such
                        │      │                   applications.
                        │      │                   
                        │      │                   The AES-SIV algorithm allows for authentication of multiple
                        │      │                   associated
                        │      │                   data entries along with the encryption. To authenticate
                        │      │                   empty data the
                        │      │                   application has to call EVP_EncryptUpdate() (or
                        │      │                   EVP_CipherUpdate()) with
                        │      │                   NULL pointer as the output buffer and 0 as the input buffer
                        │      │                   length.
                        │      │                   The AES-SIV implementation in OpenSSL just returns success
                        │      │                   for such a call
                        │      │                   instead of performing the associated data authentication
                        │      │                   operation.
                        │      │                   The empty data thus will not be authenticated.
                        │      │                   
                        │      │                   As this issue does not affect non-empty associated data
                        │      │                   authentication and
                        │      │                   we expect it to be rare for an application to use empty
                        │      │                   associated data
                        │      │                   entries this is qualified as Low severity issue. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-287 
                        │      ├ VendorSeverity   ╭ amazon: 2 
                        │      │                  ├ nvd   : 2 
                        │      │                  ├ photon: 2 
                        │      │                  ├ redhat: 1 
                        │      │                  ╰ ubuntu: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/15/1 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/19/5 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2023-2975 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-2975 
                        │      │                  ├ [4] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=00e2f5eea29994d19293ec4e8c8775ba73678598
                        │      │                  │        
                        │      │                  ├ [5] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=6a83f0c958811f07e0d11dfc6b5a6a98edfd5bdc
                        │      │                  │        
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-2975 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-202307
                        │      │                  │       25-0004/ 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-6450-1 
                        │      │                  ├ [9] : https://www.cve.org/CVERecord?id=CVE-2023-2975 
                        │      │                  ╰ [10]: https://www.openssl.org/news/secadv/20230714.txt 
                        │      ├ PublishedDate   : 2023-07-14T12:15:09.023Z 
                        │      ╰ LastModifiedDate: 2023-07-27T13:02:02.013Z 
                        ├ [38] ╭ VulnerabilityID : CVE-2023-3446 
                        │      ├ PkgID           : openssl@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-3446 
                        │      ├ Title           : openssl: Excessive time spent checking DH keys and
                        │      │                   parameters 
                        │      ├ Description     : Issue summary: Checking excessively long DH keys or
                        │      │                   parameters may be very slow.
                        │      │                   
                        │      │                   Impact summary: Applications that use the functions
                        │      │                   DH_check(), DH_check_ex()
                        │      │                   or EVP_PKEY_param_check() to check a DH key or DH parameters
                        │      │                    may experience long
                        │      │                   delays. Where the key or parameters that are being checked
                        │      │                   have been obtained
                        │      │                   from an untrusted source this may lead to a Denial of
                        │      │                   Service.
                        │      │                   
                        │      │                   The function DH_check() performs various checks on DH
                        │      │                   parameters. One of those
                        │      │                   checks confirms that the modulus ('p' parameter) is not too
                        │      │                   large. Trying to use
                        │      │                   a very large modulus is slow and OpenSSL will not normally
                        │      │                   use a modulus which
                        │      │                   is over 10,000 bits in length.
                        │      │                   
                        │      │                   However the DH_check() function checks numerous aspects of
                        │      │                   the key or parameters
                        │      │                   that have been supplied. Some of those checks use the
                        │      │                   supplied modulus value
                        │      │                   even if it has already been found to be too large.
                        │      │                   
                        │      │                   An application that calls DH_check() and supplies a key or
                        │      │                   parameters obtained
                        │      │                   from an untrusted source could be vulernable to a Denial of
                        │      │                   Service attack.
                        │      │                   
                        │      │                   The function DH_check() is itself called by a number of
                        │      │                   other OpenSSL functions.
                        │      │                   An application calling any of those other functions may
                        │      │                   similarly be affected.
                        │      │                   The other functions affected by this are DH_check_ex() and
                        │      │                   EVP_PKEY_param_check().
                        │      │                   
                        │      │                   Also vulnerable are the OpenSSL dhparam and pkeyparam
                        │      │                   command line applications
                        │      │                   when using the '-check' option.
                        │      │                   
                        │      │                   The OpenSSL SSL/TLS implementation is not affected by this
                        │      │                   issue.
                        │      │                   The OpenSSL 3.0 and 3.1 FIPS providers are not affected by
                        │      │                   this issue. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-1333 
                        │      ├ VendorSeverity   ╭ alma       : 1 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:L 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/19/4 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/19/5 
                        │      │                  ├ [2] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/19/6 
                        │      │                  ├ [3] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/31/1 
                        │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2023:7877 
                        │      │                  ├ [5] : https://access.redhat.com/security/cve/CVE-2023-3446 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2224962 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2227852 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/2248616 
                        │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-3446 
                        │      │                  ├ [10]: https://errata.almalinux.org/8/ALSA-2023-7877.html 
                        │      │                  ├ [11]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=1fa20cf2f506113c761777127a38bce5068740eb
                        │      │                  │        
                        │      │                  ├ [12]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=8780a896543a654e757db1b9396383f9d8095528
                        │      │                  │        
                        │      │                  ├ [13]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=9a0a4d3c1e7138915563c0df4fe6a3f9377b839c
                        │      │                  │        
                        │      │                  ├ [14]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=fc9867c1e03c22ebf56943be205202e576aabf23
                        │      │                  │        
                        │      │                  ├ [15]: https://linux.oracle.com/cve/CVE-2023-3446.html 
                        │      │                  ├ [16]: https://linux.oracle.com/errata/ELSA-2024-12056.html 
                        │      │                  ├ [17]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/08/msg00019.html 
                        │      │                  ├ [18]: https://nvd.nist.gov/vuln/detail/CVE-2023-3446 
                        │      │                  ├ [19]: https://security.netapp.com/advisory/ntap-202308
                        │      │                  │       03-0011/ 
                        │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6435-1 
                        │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-6435-2 
                        │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-6450-1 
                        │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2023-3446 
                        │      │                  ╰ [24]: https://www.openssl.org/news/secadv/20230719.txt 
                        │      ├ PublishedDate   : 2023-07-19T12:15:10.003Z 
                        │      ╰ LastModifiedDate: 2023-10-03T15:48:00.24Z 
                        ├ [39] ╭ VulnerabilityID : CVE-2023-3817 
                        │      ├ PkgID           : openssl@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-3817 
                        │      ├ Title           : OpenSSL: Excessive time spent checking DH q parameter value 
                        │      ├ Description     : Issue summary: Checking excessively long DH keys or
                        │      │                   parameters may be very slow.
                        │      │                   
                        │      │                   Impact summary: Applications that use the functions
                        │      │                   DH_check(), DH_check_ex()
                        │      │                   or EVP_PKEY_param_check() to check a DH key or DH parameters
                        │      │                    may experience long
                        │      │                   delays. Where the key or parameters that are being checked
                        │      │                   have been obtained
                        │      │                   from an untrusted source this may lead to a Denial of
                        │      │                   Service.
                        │      │                   
                        │      │                   The function DH_check() performs various checks on DH
                        │      │                   parameters. After fixing
                        │      │                   CVE-2023-3446 it was discovered that a large q parameter
                        │      │                   value can also trigger
                        │      │                   an overly long computation during some of these checks. A
                        │      │                   correct q value,
                        │      │                   if present, cannot be larger than the modulus p parameter,
                        │      │                   thus it is
                        │      │                   unnecessary to perform these checks if q is larger than p.
                        │      │                   
                        │      │                   An application that calls DH_check() and supplies a key or
                        │      │                   parameters obtained
                        │      │                   from an untrusted source could be vulnerable to a Denial of
                        │      │                   Service attack.
                        │      │                   
                        │      │                   The function DH_check() is itself called by a number of
                        │      │                   other OpenSSL functions.
                        │      │                   An application calling any of those other functions may
                        │      │                   similarly be affected.
                        │      │                   The other functions affected by this are DH_check_ex() and
                        │      │                   EVP_PKEY_param_check().
                        │      │                   
                        │      │                   Also vulnerable are the OpenSSL dhparam and pkeyparam
                        │      │                   command line applications
                        │      │                   when using the "-check" option.
                        │      │                   
                        │      │                   The OpenSSL SSL/TLS implementation is not affected by this
                        │      │                   issue.
                        │      │                   
                        │      │                   The OpenSSL 3.0 and 3.1 FIPS providers are not affected by
                        │      │                   this issue. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-834 
                        │      ├ VendorSeverity   ╭ alma       : 1 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:L 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2023/Jul/43 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/31/1 
                        │      │                  ├ [2] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       09/22/11 
                        │      │                  ├ [3] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       09/22/9 
                        │      │                  ├ [4] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       11/06/2 
                        │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2023:7877 
                        │      │                  ├ [6] : https://access.redhat.com/security/cve/CVE-2023-3817 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2224962 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/2227852 
                        │      │                  ├ [9] : https://bugzilla.redhat.com/2248616 
                        │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-3817 
                        │      │                  ├ [11]: https://errata.almalinux.org/8/ALSA-2023-7877.html 
                        │      │                  ├ [12]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=6a1eb62c29db6cb5eec707f9338aee00f44e26f5
                        │      │                  │        
                        │      │                  ├ [13]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=869ad69aadd985c7b8ca6f4e5dd0eb274c9f3644
                        │      │                  │        
                        │      │                  ├ [14]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=9002fd07327a91f35ba6c1307e71fa6fd4409b7f
                        │      │                  │        
                        │      │                  ├ [15]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=91ddeba0f2269b017dc06c46c993a788974b1aa5
                        │      │                  │        
                        │      │                  ├ [16]: https://linux.oracle.com/cve/CVE-2023-3817.html 
                        │      │                  ├ [17]: https://linux.oracle.com/errata/ELSA-2024-12056.html 
                        │      │                  ├ [18]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/08/msg00019.html 
                        │      │                  ├ [19]: https://nvd.nist.gov/vuln/detail/CVE-2023-3817 
                        │      │                  ├ [20]: https://security.netapp.com/advisory/ntap-202308
                        │      │                  │       18-0014/ 
                        │      │                  ├ [21]: https://security.netapp.com/advisory/ntap-202310
                        │      │                  │       27-0008/ 
                        │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-6435-1 
                        │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6435-2 
                        │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6450-1 
                        │      │                  ├ [25]: https://www.cve.org/CVERecord?id=CVE-2023-3817 
                        │      │                  ╰ [26]: https://www.openssl.org/news/secadv/20230731.txt 
                        │      ├ PublishedDate   : 2023-07-31T16:15:10.497Z 
                        │      ╰ LastModifiedDate: 2023-11-06T19:15:09.12Z 
                        ├ [40] ╭ VulnerabilityID : CVE-2023-5678 
                        │      ├ PkgID           : openssl@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-5678 
                        │      ├ Title           : openssl: Generating excessively long X9.42 DH keys or
                        │      │                   checking excessively long X9.42 DH keys or parameters may be
                        │      │                    very slow 
                        │      ├ Description     : Issue summary: Generating excessively long X9.42 DH
                        │      │                   keys or checking
                        │      │                   excessively long X9.42 DH keys or parameters may be very
                        │      │                   slow.
                        │      │                   
                        │      │                   Impact summary: Applications that use the functions
                        │      │                   DH_generate_key() to
                        │      │                   generate an X9.42 DH key may experience long delays. 
                        │      │                   Likewise, applications
                        │      │                   that use DH_check_pub_key(), DH_check_pub_key_ex() or
                        │      │                   EVP_PKEY_public_check()
                        │      │                   to check an X9.42 DH key or X9.42 DH parameters may
                        │      │                   experience long delays.
                        │      │                   Where the key or parameters that are being checked have been
                        │      │                    obtained from
                        │      │                   an untrusted source this may lead to a Denial of Service.
                        │      │                   
                        │      │                   While DH_check() performs all the necessary checks (as of
                        │      │                   CVE-2023-3817),
                        │      │                   DH_check_pub_key() doesn't make any of these checks, and is
                        │      │                   therefore
                        │      │                   vulnerable for excessively large P and Q parameters.
                        │      │                   
                        │      │                   Likewise, while DH_generate_key() performs a check for an
                        │      │                   excessively large
                        │      │                   P, it doesn't check for an excessively large Q.
                        │      │                   
                        │      │                   An application that calls DH_generate_key() or
                        │      │                   DH_check_pub_key() and
                        │      │                   supplies a key or parameters obtained from an untrusted
                        │      │                   source could be
                        │      │                   vulnerable to a Denial of Service attack.
                        │      │                   
                        │      │                   DH_generate_key() and DH_check_pub_key() are also called by
                        │      │                   a number of
                        │      │                   other OpenSSL functions.  An application calling any of
                        │      │                   those other
                        │      │                   functions may similarly be affected.  The other functions
                        │      │                   affected by this
                        │      │                   are DH_check_pub_key_ex(), EVP_PKEY_public_check(), and
                        │      │                   EVP_PKEY_generate().
                        │      │                   
                        │      │                   Also vulnerable are the OpenSSL pkey command line
                        │      │                   application when using the
                        │      │                   "-pubcheck" option, as well as the OpenSSL genpkey command
                        │      │                   line application.
                        │      │                   
                        │      │                   The OpenSSL SSL/TLS implementation is not affected by this
                        │      │                   issue.
                        │      │                   
                        │      │                   The OpenSSL 3.0 and 3.1 FIPS providers are not affected by
                        │      │                   this issue.
                        │      │                   
                        │      │                    
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-754 
                        │      ├ VendorSeverity   ╭ alma       : 1 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:L 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:7877 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-5678 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2224962 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2227852 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2248616 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-5678 
                        │      │                  ├ [6] : https://errata.almalinux.org/8/ALSA-2023-7877.html 
                        │      │                  ├ [7] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=34efaef6c103d636ab507a0cc34dca4d3aecc055
                        │      │                  │        
                        │      │                  ├ [8] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=710fee740904b6290fef0dd5536fbcedbc38ff0c
                        │      │                  │        
                        │      │                  ├ [9] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=db925ae2e65d0d925adef429afc37f75bd1c2017
                        │      │                  │        
                        │      │                  ├ [10]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=ddeb4b6c6d527e54ce9a99cba785c0f7776e54b6
                        │      │                  │        
                        │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2023-5678.html 
                        │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2024-12056.html 
                        │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2023-5678 
                        │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202311
                        │      │                  │       30-0010/ 
                        │      │                  ├ [15]: https://www.cve.org/CVERecord?id=CVE-2023-5678 
                        │      │                  ╰ [16]: https://www.openssl.org/news/secadv/20231106.txt 
                        │      ├ PublishedDate   : 2023-11-06T16:15:42.67Z 
                        │      ╰ LastModifiedDate: 2023-11-30T22:15:09.723Z 
                        ├ [41] ╭ VulnerabilityID : CVE-2023-6129 
                        │      ├ PkgID           : openssl@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-6129 
                        │      ├ Title           : openssl: POLY1305 MAC implementation corrupts vector
                        │      │                   registers on PowerPC 
                        │      ├ Description     : Issue summary: The POLY1305 MAC (message authentication
                        │      │                    code) implementation
                        │      │                   contains a bug that might corrupt the internal state of
                        │      │                   applications running
                        │      │                   on PowerPC CPU based platforms if the CPU provides vector
                        │      │                   instructions.
                        │      │                   
                        │      │                   Impact summary: If an attacker can influence whether the
                        │      │                   POLY1305 MAC
                        │      │                   algorithm is used, the application state might be corrupted
                        │      │                   with various
                        │      │                   application dependent consequences.
                        │      │                   
                        │      │                   The POLY1305 MAC (message authentication code)
                        │      │                   implementation in OpenSSL for
                        │      │                   PowerPC CPUs restores the contents of vector registers in a
                        │      │                   different order
                        │      │                   than they are saved. Thus the contents of some of these
                        │      │                   vector registers
                        │      │                   are corrupted when returning to the caller. The vulnerable
                        │      │                   code is used only
                        │      │                   on newer PowerPC processors supporting the PowerISA 2.07
                        │      │                   instructions.
                        │      │                   
                        │      │                   The consequences of this kind of internal application state
                        │      │                   corruption can
                        │      │                   be various - from no consequences, if the calling
                        │      │                   application does not
                        │      │                   depend on the contents of non-volatile XMM registers at all,
                        │      │                    to the worst
                        │      │                   consequences, where the attacker could get complete control
                        │      │                   of the application
                        │      │                   process. However unless the compiler uses the vector
                        │      │                   registers for storing
                        │      │                   pointers, the most likely consequence, if any, would be an
                        │      │                   incorrect result
                        │      │                   of some application dependent calculations or a crash
                        │      │                   leading to a denial of
                        │      │                   service.
                        │      │                   
                        │      │                   The POLY1305 MAC algorithm is most frequently used as part
                        │      │                   of the
                        │      │                   CHACHA20-POLY1305 AEAD (authenticated encryption with
                        │      │                   associated data)
                        │      │                   algorithm. The most common usage of this AEAD cipher is with
                        │      │                    TLS protocol
                        │      │                   versions 1.2 and 1.3. If this cipher is enabled on the
                        │      │                   server a malicious
                        │      │                   client can influence whether this AEAD cipher is used. This
                        │      │                   implies that
                        │      │                   TLS server applications using OpenSSL can be potentially
                        │      │                   impacted. However
                        │      │                   we are currently not aware of any concrete application that
                        │      │                   would be affected
                        │      │                   by this issue therefore we consider this a Low severity
                        │      │                   security issue. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-787 
                        │      ├ VendorSeverity   ╭ nvd   : 2 
                        │      │                  ├ redhat: 1 
                        │      │                  ╰ ubuntu: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-6129 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-6129 
                        │      │                  ├ [2]: https://github.com/openssl/openssl/commit/050d263
                        │      │                  │      83d4e264966fb83428e72d5d48f402d35 
                        │      │                  ├ [3]: https://github.com/openssl/openssl/commit/5b139f9
                        │      │                  │      5c9a47a55a0c54100f3837b1eee942b04 
                        │      │                  ├ [4]: https://github.com/openssl/openssl/commit/f3fc580
                        │      │                  │      8fe9ff74042d639839610d03b8fdcc015 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-6129 
                        │      │                  ├ [6]: https://www.cve.org/CVERecord?id=CVE-2023-6129 
                        │      │                  ├ [7]: https://www.openssl.org/news/secadv/20240109.txt 
                        │      │                  ╰ [8]: https://www.openwall.com/lists/oss-security/2024/
                        │      │                         01/09/1 
                        │      ├ PublishedDate   : 2024-01-09T17:15:12.147Z 
                        │      ╰ LastModifiedDate: 2024-01-23T21:32:01.973Z 
                        ├ [42] ╭ VulnerabilityID : CVE-2023-6237 
                        │      ├ PkgID           : openssl@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-6237 
                        │      ├ Title           : openssl: Excessive time spent checking invalid RSA
                        │      │                   public keys 
                        │      ├ Description     : A flaw was found in OpenSSL. When the
                        │      │                   EVP_PKEY_public_check() function is called in RSA public
                        │      │                   keys, a computation is done to confirm that the RSA modulus,
                        │      │                    n, is composite. For valid RSA keys, n is a product of two
                        │      │                   or more large primes and this computation completes quickly.
                        │      │                    However, if n is a large prime, this computation takes a
                        │      │                   long time. An application that calls EVP_PKEY_public_check()
                        │      │                    and supplies an RSA key obtained from an untrusted source
                        │      │                   could be vulnerable to a Denial of Service attack. 
                        │      ├ Severity        : LOW 
                        │      ├ VendorSeverity   ╭ redhat: 1 
                        │      │                  ╰ ubuntu: 1 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-6237 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2023-6237 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-6237 
                        │                         ├ [3]: https://www.cve.org/CVERecord?id=CVE-2023-6237 
                        │                         ├ [4]: https://www.openssl.org/news/secadv/20240115.txt 
                        │                         ╰ [5]: https://www.openwall.com/lists/oss-security/2024/
                        │                                01/15/2 
                        ├ [43] ╭ VulnerabilityID : CVE-2024-0727 
                        │      ├ PkgID           : openssl@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-0727 
                        │      ├ Title           : openssl: denial of service via null dereference 
                        │      ├ Description     : Issue summary: Processing a maliciously formatted
                        │      │                   PKCS12 file may lead OpenSSL
                        │      │                   to crash leading to a potential Denial of Service attack
                        │      │                   
                        │      │                   Impact summary: Applications loading files in the PKCS12
                        │      │                   format from untrusted
                        │      │                   sources might terminate abruptly.
                        │      │                   
                        │      │                   A file in PKCS12 format can contain certificates and keys
                        │      │                   and may come from an
                        │      │                   untrusted source. The PKCS12 specification allows certain
                        │      │                   fields to be NULL, but
                        │      │                   OpenSSL does not correctly check for this case. This can
                        │      │                   lead to a NULL pointer
                        │      │                   dereference that results in OpenSSL crashing. If an
                        │      │                   application processes PKCS12
                        │      │                   files from an untrusted source using the OpenSSL APIs then
                        │      │                   that application will
                        │      │                   be vulnerable to this issue.
                        │      │                   
                        │      │                   OpenSSL APIs that are vulnerable to this are:
                        │      │                   PKCS12_parse(),
                        │      │                   PKCS12_unpack_p7data(), PKCS12_unpack_p7encdata(),
                        │      │                   PKCS12_unpack_authsafes()
                        │      │                   and PKCS12_newpass().
                        │      │                   
                        │      │                   We have also fixed a similar issue in SMIME_write_PKCS7().
                        │      │                   However since this
                        │      │                   function is related to writing data we do not consider it
                        │      │                   security significant.
                        │      │                   
                        │      │                   The FIPS modules in 3.2, 3.1 and 3.0 are not affected by
                        │      │                   this issue. 
                        │      ├ Severity        : LOW 
                        │      ├ VendorSeverity   ╭ redhat: 1 
                        │      │                  ╰ ubuntu: 1 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 3.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2024-0727 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2024-0727 
                        │      │                  ├ [2] : https://github.com/openssl/openssl/commit/09df43
                        │      │                  │       95b5071217b76dc7d3d2e630eb8c5a79c2 
                        │      │                  ├ [3] : https://github.com/openssl/openssl/commit/775acf
                        │      │                  │       dbd0c6af9ac855f34969cdab0c0c90844a 
                        │      │                  ├ [4] : https://github.com/openssl/openssl/commit/d135ee
                        │      │                  │       ab8a5dbf72b3da5240bab9ddb7678dbd2c 
                        │      │                  ├ [5] : https://github.com/openssl/openssl/pull/23362 
                        │      │                  ├ [6] : https://github.openssl.org/openssl/extended-rele
                        │      │                  │       ases/commit/03b3941d60c4bce58fab69a0c22377ab439bc0e8
                        │      │                  │       [m 
                        │      │                  ├ [7] : https://github.openssl.org/openssl/extended-rele
                        │      │                  │       ases/commit/aebaa5883e31122b404e450732dc833dc9dee539
                        │      │                  │       [m 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2024-0727 
                        │      │                  ├ [9] : https://www.cve.org/CVERecord?id=CVE-2024-0727 
                        │      │                  ╰ [10]: https://www.openssl.org/news/secadv/20240125.txt 
                        │      ├ PublishedDate   : 2024-01-26T09:15:07.637Z 
                        │      ╰ LastModifiedDate: 2024-01-26T13:51:45.267Z 
                        ├ [44] ╭ VulnerabilityID : CVE-2023-2975 
                        │      ├ PkgID           : openssl-libs@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2975 
                        │      ├ Title           : openssl: AES-SIV cipher implementation contains a bug
                        │      │                   that causes it to ignore empty associated data entries 
                        │      ├ Description     : Issue summary: The AES-SIV cipher implementation
                        │      │                   contains a bug that causes
                        │      │                   it to ignore empty associated data entries which are
                        │      │                   unauthenticated as
                        │      │                   a consequence.
                        │      │                   
                        │      │                   Impact summary: Applications that use the AES-SIV algorithm
                        │      │                   and want to
                        │      │                   authenticate empty data entries as associated data can be
                        │      │                   mislead by removing
                        │      │                   adding or reordering such empty entries as these are ignored
                        │      │                    by the OpenSSL
                        │      │                   implementation. We are currently unaware of any such
                        │      │                   applications.
                        │      │                   
                        │      │                   The AES-SIV algorithm allows for authentication of multiple
                        │      │                   associated
                        │      │                   data entries along with the encryption. To authenticate
                        │      │                   empty data the
                        │      │                   application has to call EVP_EncryptUpdate() (or
                        │      │                   EVP_CipherUpdate()) with
                        │      │                   NULL pointer as the output buffer and 0 as the input buffer
                        │      │                   length.
                        │      │                   The AES-SIV implementation in OpenSSL just returns success
                        │      │                   for such a call
                        │      │                   instead of performing the associated data authentication
                        │      │                   operation.
                        │      │                   The empty data thus will not be authenticated.
                        │      │                   
                        │      │                   As this issue does not affect non-empty associated data
                        │      │                   authentication and
                        │      │                   we expect it to be rare for an application to use empty
                        │      │                   associated data
                        │      │                   entries this is qualified as Low severity issue. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-287 
                        │      ├ VendorSeverity   ╭ amazon: 2 
                        │      │                  ├ nvd   : 2 
                        │      │                  ├ photon: 2 
                        │      │                  ├ redhat: 1 
                        │      │                  ╰ ubuntu: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/15/1 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/19/5 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2023-2975 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-2975 
                        │      │                  ├ [4] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=00e2f5eea29994d19293ec4e8c8775ba73678598
                        │      │                  │        
                        │      │                  ├ [5] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=6a83f0c958811f07e0d11dfc6b5a6a98edfd5bdc
                        │      │                  │        
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-2975 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-202307
                        │      │                  │       25-0004/ 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-6450-1 
                        │      │                  ├ [9] : https://www.cve.org/CVERecord?id=CVE-2023-2975 
                        │      │                  ╰ [10]: https://www.openssl.org/news/secadv/20230714.txt 
                        │      ├ PublishedDate   : 2023-07-14T12:15:09.023Z 
                        │      ╰ LastModifiedDate: 2023-07-27T13:02:02.013Z 
                        ├ [45] ╭ VulnerabilityID : CVE-2023-3446 
                        │      ├ PkgID           : openssl-libs@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-3446 
                        │      ├ Title           : openssl: Excessive time spent checking DH keys and
                        │      │                   parameters 
                        │      ├ Description     : Issue summary: Checking excessively long DH keys or
                        │      │                   parameters may be very slow.
                        │      │                   
                        │      │                   Impact summary: Applications that use the functions
                        │      │                   DH_check(), DH_check_ex()
                        │      │                   or EVP_PKEY_param_check() to check a DH key or DH parameters
                        │      │                    may experience long
                        │      │                   delays. Where the key or parameters that are being checked
                        │      │                   have been obtained
                        │      │                   from an untrusted source this may lead to a Denial of
                        │      │                   Service.
                        │      │                   
                        │      │                   The function DH_check() performs various checks on DH
                        │      │                   parameters. One of those
                        │      │                   checks confirms that the modulus ('p' parameter) is not too
                        │      │                   large. Trying to use
                        │      │                   a very large modulus is slow and OpenSSL will not normally
                        │      │                   use a modulus which
                        │      │                   is over 10,000 bits in length.
                        │      │                   
                        │      │                   However the DH_check() function checks numerous aspects of
                        │      │                   the key or parameters
                        │      │                   that have been supplied. Some of those checks use the
                        │      │                   supplied modulus value
                        │      │                   even if it has already been found to be too large.
                        │      │                   
                        │      │                   An application that calls DH_check() and supplies a key or
                        │      │                   parameters obtained
                        │      │                   from an untrusted source could be vulernable to a Denial of
                        │      │                   Service attack.
                        │      │                   
                        │      │                   The function DH_check() is itself called by a number of
                        │      │                   other OpenSSL functions.
                        │      │                   An application calling any of those other functions may
                        │      │                   similarly be affected.
                        │      │                   The other functions affected by this are DH_check_ex() and
                        │      │                   EVP_PKEY_param_check().
                        │      │                   
                        │      │                   Also vulnerable are the OpenSSL dhparam and pkeyparam
                        │      │                   command line applications
                        │      │                   when using the '-check' option.
                        │      │                   
                        │      │                   The OpenSSL SSL/TLS implementation is not affected by this
                        │      │                   issue.
                        │      │                   The OpenSSL 3.0 and 3.1 FIPS providers are not affected by
                        │      │                   this issue. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-1333 
                        │      ├ VendorSeverity   ╭ alma       : 1 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:L 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/19/4 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/19/5 
                        │      │                  ├ [2] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/19/6 
                        │      │                  ├ [3] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/31/1 
                        │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2023:7877 
                        │      │                  ├ [5] : https://access.redhat.com/security/cve/CVE-2023-3446 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2224962 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2227852 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/2248616 
                        │      │                  ├ [9] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-3446 
                        │      │                  ├ [10]: https://errata.almalinux.org/8/ALSA-2023-7877.html 
                        │      │                  ├ [11]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=1fa20cf2f506113c761777127a38bce5068740eb
                        │      │                  │        
                        │      │                  ├ [12]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=8780a896543a654e757db1b9396383f9d8095528
                        │      │                  │        
                        │      │                  ├ [13]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=9a0a4d3c1e7138915563c0df4fe6a3f9377b839c
                        │      │                  │        
                        │      │                  ├ [14]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=fc9867c1e03c22ebf56943be205202e576aabf23
                        │      │                  │        
                        │      │                  ├ [15]: https://linux.oracle.com/cve/CVE-2023-3446.html 
                        │      │                  ├ [16]: https://linux.oracle.com/errata/ELSA-2024-12056.html 
                        │      │                  ├ [17]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/08/msg00019.html 
                        │      │                  ├ [18]: https://nvd.nist.gov/vuln/detail/CVE-2023-3446 
                        │      │                  ├ [19]: https://security.netapp.com/advisory/ntap-202308
                        │      │                  │       03-0011/ 
                        │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6435-1 
                        │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-6435-2 
                        │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-6450-1 
                        │      │                  ├ [23]: https://www.cve.org/CVERecord?id=CVE-2023-3446 
                        │      │                  ╰ [24]: https://www.openssl.org/news/secadv/20230719.txt 
                        │      ├ PublishedDate   : 2023-07-19T12:15:10.003Z 
                        │      ╰ LastModifiedDate: 2023-10-03T15:48:00.24Z 
                        ├ [46] ╭ VulnerabilityID : CVE-2023-3817 
                        │      ├ PkgID           : openssl-libs@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-3817 
                        │      ├ Title           : OpenSSL: Excessive time spent checking DH q parameter value 
                        │      ├ Description     : Issue summary: Checking excessively long DH keys or
                        │      │                   parameters may be very slow.
                        │      │                   
                        │      │                   Impact summary: Applications that use the functions
                        │      │                   DH_check(), DH_check_ex()
                        │      │                   or EVP_PKEY_param_check() to check a DH key or DH parameters
                        │      │                    may experience long
                        │      │                   delays. Where the key or parameters that are being checked
                        │      │                   have been obtained
                        │      │                   from an untrusted source this may lead to a Denial of
                        │      │                   Service.
                        │      │                   
                        │      │                   The function DH_check() performs various checks on DH
                        │      │                   parameters. After fixing
                        │      │                   CVE-2023-3446 it was discovered that a large q parameter
                        │      │                   value can also trigger
                        │      │                   an overly long computation during some of these checks. A
                        │      │                   correct q value,
                        │      │                   if present, cannot be larger than the modulus p parameter,
                        │      │                   thus it is
                        │      │                   unnecessary to perform these checks if q is larger than p.
                        │      │                   
                        │      │                   An application that calls DH_check() and supplies a key or
                        │      │                   parameters obtained
                        │      │                   from an untrusted source could be vulnerable to a Denial of
                        │      │                   Service attack.
                        │      │                   
                        │      │                   The function DH_check() is itself called by a number of
                        │      │                   other OpenSSL functions.
                        │      │                   An application calling any of those other functions may
                        │      │                   similarly be affected.
                        │      │                   The other functions affected by this are DH_check_ex() and
                        │      │                   EVP_PKEY_param_check().
                        │      │                   
                        │      │                   Also vulnerable are the OpenSSL dhparam and pkeyparam
                        │      │                   command line applications
                        │      │                   when using the "-check" option.
                        │      │                   
                        │      │                   The OpenSSL SSL/TLS implementation is not affected by this
                        │      │                   issue.
                        │      │                   
                        │      │                   The OpenSSL 3.0 and 3.1 FIPS providers are not affected by
                        │      │                   this issue. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-834 
                        │      ├ VendorSeverity   ╭ alma       : 1 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:L 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2023/Jul/43 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/31/1 
                        │      │                  ├ [2] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       09/22/11 
                        │      │                  ├ [3] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       09/22/9 
                        │      │                  ├ [4] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       11/06/2 
                        │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2023:7877 
                        │      │                  ├ [6] : https://access.redhat.com/security/cve/CVE-2023-3817 
                        │      │                  ├ [7] : https://bugzilla.redhat.com/2224962 
                        │      │                  ├ [8] : https://bugzilla.redhat.com/2227852 
                        │      │                  ├ [9] : https://bugzilla.redhat.com/2248616 
                        │      │                  ├ [10]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-3817 
                        │      │                  ├ [11]: https://errata.almalinux.org/8/ALSA-2023-7877.html 
                        │      │                  ├ [12]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=6a1eb62c29db6cb5eec707f9338aee00f44e26f5
                        │      │                  │        
                        │      │                  ├ [13]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=869ad69aadd985c7b8ca6f4e5dd0eb274c9f3644
                        │      │                  │        
                        │      │                  ├ [14]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=9002fd07327a91f35ba6c1307e71fa6fd4409b7f
                        │      │                  │        
                        │      │                  ├ [15]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=91ddeba0f2269b017dc06c46c993a788974b1aa5
                        │      │                  │        
                        │      │                  ├ [16]: https://linux.oracle.com/cve/CVE-2023-3817.html 
                        │      │                  ├ [17]: https://linux.oracle.com/errata/ELSA-2024-12056.html 
                        │      │                  ├ [18]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/08/msg00019.html 
                        │      │                  ├ [19]: https://nvd.nist.gov/vuln/detail/CVE-2023-3817 
                        │      │                  ├ [20]: https://security.netapp.com/advisory/ntap-202308
                        │      │                  │       18-0014/ 
                        │      │                  ├ [21]: https://security.netapp.com/advisory/ntap-202310
                        │      │                  │       27-0008/ 
                        │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-6435-1 
                        │      │                  ├ [23]: https://ubuntu.com/security/notices/USN-6435-2 
                        │      │                  ├ [24]: https://ubuntu.com/security/notices/USN-6450-1 
                        │      │                  ├ [25]: https://www.cve.org/CVERecord?id=CVE-2023-3817 
                        │      │                  ╰ [26]: https://www.openssl.org/news/secadv/20230731.txt 
                        │      ├ PublishedDate   : 2023-07-31T16:15:10.497Z 
                        │      ╰ LastModifiedDate: 2023-11-06T19:15:09.12Z 
                        ├ [47] ╭ VulnerabilityID : CVE-2023-5678 
                        │      ├ PkgID           : openssl-libs@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-5678 
                        │      ├ Title           : openssl: Generating excessively long X9.42 DH keys or
                        │      │                   checking excessively long X9.42 DH keys or parameters may be
                        │      │                    very slow 
                        │      ├ Description     : Issue summary: Generating excessively long X9.42 DH
                        │      │                   keys or checking
                        │      │                   excessively long X9.42 DH keys or parameters may be very
                        │      │                   slow.
                        │      │                   
                        │      │                   Impact summary: Applications that use the functions
                        │      │                   DH_generate_key() to
                        │      │                   generate an X9.42 DH key may experience long delays. 
                        │      │                   Likewise, applications
                        │      │                   that use DH_check_pub_key(), DH_check_pub_key_ex() or
                        │      │                   EVP_PKEY_public_check()
                        │      │                   to check an X9.42 DH key or X9.42 DH parameters may
                        │      │                   experience long delays.
                        │      │                   Where the key or parameters that are being checked have been
                        │      │                    obtained from
                        │      │                   an untrusted source this may lead to a Denial of Service.
                        │      │                   
                        │      │                   While DH_check() performs all the necessary checks (as of
                        │      │                   CVE-2023-3817),
                        │      │                   DH_check_pub_key() doesn't make any of these checks, and is
                        │      │                   therefore
                        │      │                   vulnerable for excessively large P and Q parameters.
                        │      │                   
                        │      │                   Likewise, while DH_generate_key() performs a check for an
                        │      │                   excessively large
                        │      │                   P, it doesn't check for an excessively large Q.
                        │      │                   
                        │      │                   An application that calls DH_generate_key() or
                        │      │                   DH_check_pub_key() and
                        │      │                   supplies a key or parameters obtained from an untrusted
                        │      │                   source could be
                        │      │                   vulnerable to a Denial of Service attack.
                        │      │                   
                        │      │                   DH_generate_key() and DH_check_pub_key() are also called by
                        │      │                   a number of
                        │      │                   other OpenSSL functions.  An application calling any of
                        │      │                   those other
                        │      │                   functions may similarly be affected.  The other functions
                        │      │                   affected by this
                        │      │                   are DH_check_pub_key_ex(), EVP_PKEY_public_check(), and
                        │      │                   EVP_PKEY_generate().
                        │      │                   
                        │      │                   Also vulnerable are the OpenSSL pkey command line
                        │      │                   application when using the
                        │      │                   "-pubcheck" option, as well as the OpenSSL genpkey command
                        │      │                   line application.
                        │      │                   
                        │      │                   The OpenSSL SSL/TLS implementation is not affected by this
                        │      │                   issue.
                        │      │                   
                        │      │                   The OpenSSL 3.0 and 3.1 FIPS providers are not affected by
                        │      │                   this issue.
                        │      │                   
                        │      │                    
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-754 
                        │      ├ VendorSeverity   ╭ alma       : 1 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:L 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:7877 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-5678 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2224962 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2227852 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2248616 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-5678 
                        │      │                  ├ [6] : https://errata.almalinux.org/8/ALSA-2023-7877.html 
                        │      │                  ├ [7] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=34efaef6c103d636ab507a0cc34dca4d3aecc055
                        │      │                  │        
                        │      │                  ├ [8] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=710fee740904b6290fef0dd5536fbcedbc38ff0c
                        │      │                  │        
                        │      │                  ├ [9] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=db925ae2e65d0d925adef429afc37f75bd1c2017
                        │      │                  │        
                        │      │                  ├ [10]: https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=ddeb4b6c6d527e54ce9a99cba785c0f7776e54b6
                        │      │                  │        
                        │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2023-5678.html 
                        │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2024-12056.html 
                        │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2023-5678 
                        │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202311
                        │      │                  │       30-0010/ 
                        │      │                  ├ [15]: https://www.cve.org/CVERecord?id=CVE-2023-5678 
                        │      │                  ╰ [16]: https://www.openssl.org/news/secadv/20231106.txt 
                        │      ├ PublishedDate   : 2023-11-06T16:15:42.67Z 
                        │      ╰ LastModifiedDate: 2023-11-30T22:15:09.723Z 
                        ├ [48] ╭ VulnerabilityID : CVE-2023-6129 
                        │      ├ PkgID           : openssl-libs@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-6129 
                        │      ├ Title           : openssl: POLY1305 MAC implementation corrupts vector
                        │      │                   registers on PowerPC 
                        │      ├ Description     : Issue summary: The POLY1305 MAC (message authentication
                        │      │                    code) implementation
                        │      │                   contains a bug that might corrupt the internal state of
                        │      │                   applications running
                        │      │                   on PowerPC CPU based platforms if the CPU provides vector
                        │      │                   instructions.
                        │      │                   
                        │      │                   Impact summary: If an attacker can influence whether the
                        │      │                   POLY1305 MAC
                        │      │                   algorithm is used, the application state might be corrupted
                        │      │                   with various
                        │      │                   application dependent consequences.
                        │      │                   
                        │      │                   The POLY1305 MAC (message authentication code)
                        │      │                   implementation in OpenSSL for
                        │      │                   PowerPC CPUs restores the contents of vector registers in a
                        │      │                   different order
                        │      │                   than they are saved. Thus the contents of some of these
                        │      │                   vector registers
                        │      │                   are corrupted when returning to the caller. The vulnerable
                        │      │                   code is used only
                        │      │                   on newer PowerPC processors supporting the PowerISA 2.07
                        │      │                   instructions.
                        │      │                   
                        │      │                   The consequences of this kind of internal application state
                        │      │                   corruption can
                        │      │                   be various - from no consequences, if the calling
                        │      │                   application does not
                        │      │                   depend on the contents of non-volatile XMM registers at all,
                        │      │                    to the worst
                        │      │                   consequences, where the attacker could get complete control
                        │      │                   of the application
                        │      │                   process. However unless the compiler uses the vector
                        │      │                   registers for storing
                        │      │                   pointers, the most likely consequence, if any, would be an
                        │      │                   incorrect result
                        │      │                   of some application dependent calculations or a crash
                        │      │                   leading to a denial of
                        │      │                   service.
                        │      │                   
                        │      │                   The POLY1305 MAC algorithm is most frequently used as part
                        │      │                   of the
                        │      │                   CHACHA20-POLY1305 AEAD (authenticated encryption with
                        │      │                   associated data)
                        │      │                   algorithm. The most common usage of this AEAD cipher is with
                        │      │                    TLS protocol
                        │      │                   versions 1.2 and 1.3. If this cipher is enabled on the
                        │      │                   server a malicious
                        │      │                   client can influence whether this AEAD cipher is used. This
                        │      │                   implies that
                        │      │                   TLS server applications using OpenSSL can be potentially
                        │      │                   impacted. However
                        │      │                   we are currently not aware of any concrete application that
                        │      │                   would be affected
                        │      │                   by this issue therefore we consider this a Low severity
                        │      │                   security issue. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-787 
                        │      ├ VendorSeverity   ╭ nvd   : 2 
                        │      │                  ├ redhat: 1 
                        │      │                  ╰ ubuntu: 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-6129 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-6129 
                        │      │                  ├ [2]: https://github.com/openssl/openssl/commit/050d263
                        │      │                  │      83d4e264966fb83428e72d5d48f402d35 
                        │      │                  ├ [3]: https://github.com/openssl/openssl/commit/5b139f9
                        │      │                  │      5c9a47a55a0c54100f3837b1eee942b04 
                        │      │                  ├ [4]: https://github.com/openssl/openssl/commit/f3fc580
                        │      │                  │      8fe9ff74042d639839610d03b8fdcc015 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-6129 
                        │      │                  ├ [6]: https://www.cve.org/CVERecord?id=CVE-2023-6129 
                        │      │                  ├ [7]: https://www.openssl.org/news/secadv/20240109.txt 
                        │      │                  ╰ [8]: https://www.openwall.com/lists/oss-security/2024/
                        │      │                         01/09/1 
                        │      ├ PublishedDate   : 2024-01-09T17:15:12.147Z 
                        │      ╰ LastModifiedDate: 2024-01-23T21:32:01.973Z 
                        ├ [49] ╭ VulnerabilityID : CVE-2023-6237 
                        │      ├ PkgID           : openssl-libs@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-6237 
                        │      ├ Title           : openssl: Excessive time spent checking invalid RSA
                        │      │                   public keys 
                        │      ├ Description     : A flaw was found in OpenSSL. When the
                        │      │                   EVP_PKEY_public_check() function is called in RSA public
                        │      │                   keys, a computation is done to confirm that the RSA modulus,
                        │      │                    n, is composite. For valid RSA keys, n is a product of two
                        │      │                   or more large primes and this computation completes quickly.
                        │      │                    However, if n is a large prime, this computation takes a
                        │      │                   long time. An application that calls EVP_PKEY_public_check()
                        │      │                    and supplies an RSA key obtained from an untrusted source
                        │      │                   could be vulnerable to a Denial of Service attack. 
                        │      ├ Severity        : LOW 
                        │      ├ VendorSeverity   ╭ redhat: 1 
                        │      │                  ╰ ubuntu: 1 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-6237 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2023-6237 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-6237 
                        │                         ├ [3]: https://www.cve.org/CVERecord?id=CVE-2023-6237 
                        │                         ├ [4]: https://www.openssl.org/news/secadv/20240115.txt 
                        │                         ╰ [5]: https://www.openwall.com/lists/oss-security/2024/
                        │                                01/15/2 
                        ├ [50] ╭ VulnerabilityID : CVE-2024-0727 
                        │      ├ PkgID           : openssl-libs@3.0.7-25.el9_3.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-25.el9_3 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-0727 
                        │      ├ Title           : openssl: denial of service via null dereference 
                        │      ├ Description     : Issue summary: Processing a maliciously formatted
                        │      │                   PKCS12 file may lead OpenSSL
                        │      │                   to crash leading to a potential Denial of Service attack
                        │      │                   
                        │      │                   Impact summary: Applications loading files in the PKCS12
                        │      │                   format from untrusted
                        │      │                   sources might terminate abruptly.
                        │      │                   
                        │      │                   A file in PKCS12 format can contain certificates and keys
                        │      │                   and may come from an
                        │      │                   untrusted source. The PKCS12 specification allows certain
                        │      │                   fields to be NULL, but
                        │      │                   OpenSSL does not correctly check for this case. This can
                        │      │                   lead to a NULL pointer
                        │      │                   dereference that results in OpenSSL crashing. If an
                        │      │                   application processes PKCS12
                        │      │                   files from an untrusted source using the OpenSSL APIs then
                        │      │                   that application will
                        │      │                   be vulnerable to this issue.
                        │      │                   
                        │      │                   OpenSSL APIs that are vulnerable to this are:
                        │      │                   PKCS12_parse(),
                        │      │                   PKCS12_unpack_p7data(), PKCS12_unpack_p7encdata(),
                        │      │                   PKCS12_unpack_authsafes()
                        │      │                   and PKCS12_newpass().
                        │      │                   
                        │      │                   We have also fixed a similar issue in SMIME_write_PKCS7().
                        │      │                   However since this
                        │      │                   function is related to writing data we do not consider it
                        │      │                   security significant.
                        │      │                   
                        │      │                   The FIPS modules in 3.2, 3.1 and 3.0 are not affected by
                        │      │                   this issue. 
                        │      ├ Severity        : LOW 
                        │      ├ VendorSeverity   ╭ redhat: 1 
                        │      │                  ╰ ubuntu: 1 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 3.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2024-0727 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2024-0727 
                        │      │                  ├ [2] : https://github.com/openssl/openssl/commit/09df43
                        │      │                  │       95b5071217b76dc7d3d2e630eb8c5a79c2 
                        │      │                  ├ [3] : https://github.com/openssl/openssl/commit/775acf
                        │      │                  │       dbd0c6af9ac855f34969cdab0c0c90844a 
                        │      │                  ├ [4] : https://github.com/openssl/openssl/commit/d135ee
                        │      │                  │       ab8a5dbf72b3da5240bab9ddb7678dbd2c 
                        │      │                  ├ [5] : https://github.com/openssl/openssl/pull/23362 
                        │      │                  ├ [6] : https://github.openssl.org/openssl/extended-rele
                        │      │                  │       ases/commit/03b3941d60c4bce58fab69a0c22377ab439bc0e8
                        │      │                  │       [m 
                        │      │                  ├ [7] : https://github.openssl.org/openssl/extended-rele
                        │      │                  │       ases/commit/aebaa5883e31122b404e450732dc833dc9dee539
                        │      │                  │       [m 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2024-0727 
                        │      │                  ├ [9] : https://www.cve.org/CVERecord?id=CVE-2024-0727 
                        │      │                  ╰ [10]: https://www.openssl.org/news/secadv/20240125.txt 
                        │      ├ PublishedDate   : 2024-01-26T09:15:07.637Z 
                        │      ╰ LastModifiedDate: 2024-01-26T13:51:45.267Z 
                        ├ [51] ╭ VulnerabilityID : CVE-2024-22365 
                        │      ├ PkgID           : pam@1.5.1-15.el9.x86_64 
                        │      ├ PkgName         : pam 
                        │      ├ InstalledVersion: 1.5.1-15.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-22365 
                        │      ├ Title           : pam: allowing unpriledged user to block another user
                        │      │                   namespace 
                        │      ├ Description     : A vulnerability was found in Linux PAM. An unprivileged
                        │      │                    user that is not yet in a corresponding mount namespace
                        │      │                   with ~/tmp mounted as a polyinstantiated dir can place a
                        │      │                   FIFO there, and a subsequent attempt to login as this user
                        │      │                   with `pam_namespace` configured will cause the `openat()` in
                        │      │                    `protect_dir()` to block the attempt, causing a local
                        │      │                   denial of service. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ VendorSeverity   ╭ redhat: 2 
                        │      │                  ╰ ubuntu: 2 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-22365 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2024-22365 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2024-22365 
                        │                         ├ [3]: https://ubuntu.com/security/notices/USN-6588-1 
                        │                         ├ [4]: https://www.cve.org/CVERecord?id=CVE-2024-22365 
                        │                         ╰ [5]: https://www.openwall.com/lists/oss-security/2024/
                        │                                01/18/3 
                        ├ [52] ╭ VulnerabilityID : CVE-2022-41409 
                        │      ├ PkgID           : pcre2@10.40-2.el9.x86_64 
                        │      ├ PkgName         : pcre2 
                        │      ├ InstalledVersion: 10.40-2.el9 
                        │      ├ Status          : under_investigation 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-41409 
                        │      ├ Title           : pcre2: negative repeat value in a pcre2test subject
                        │      │                   line leads to inifinite loop 
                        │      ├ Description     : Integer overflow vulnerability in pcre2test before
                        │      │                   10.41 allows attackers to cause a denial of service or other
                        │      │                    unspecified impacts via negative input. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-190 
                        │      ├ VendorSeverity   ╭ amazon     : 1 
                        │      │                  ├ cbl-mariner: 3 
                        │      │                  ├ nvd        : 3 
                        │      │                  ├ photon     : 3 
                        │      │                  ╰ redhat     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-41409 
                        │      │                  ├ [1]: https://github.com/PCRE2Project/pcre2/commit/94e1
                        │      │                  │      c001761373b7d9450768aa15d04c25547a35 
                        │      │                  ├ [2]: https://github.com/PCRE2Project/pcre2/issues/141 
                        │      │                  ├ [3]: https://github.com/advisories/GHSA-4qfx-v7wh-3q4j 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2022-41409 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2022-41409 
                        │      ├ PublishedDate   : 2023-07-18T14:15:12.197Z 
                        │      ╰ LastModifiedDate: 2023-07-27T03:46:09.807Z 
                        ├ [53] ╭ VulnerabilityID : CVE-2022-41409 
                        │      ├ PkgID           : pcre2-syntax@10.40-2.el9.noarch 
                        │      ├ PkgName         : pcre2-syntax 
                        │      ├ InstalledVersion: 10.40-2.el9 
                        │      ├ Status          : under_investigation 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-41409 
                        │      ├ Title           : pcre2: negative repeat value in a pcre2test subject
                        │      │                   line leads to inifinite loop 
                        │      ├ Description     : Integer overflow vulnerability in pcre2test before
                        │      │                   10.41 allows attackers to cause a denial of service or other
                        │      │                    unspecified impacts via negative input. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-190 
                        │      ├ VendorSeverity   ╭ amazon     : 1 
                        │      │                  ├ cbl-mariner: 3 
                        │      │                  ├ nvd        : 3 
                        │      │                  ├ photon     : 3 
                        │      │                  ╰ redhat     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-41409 
                        │      │                  ├ [1]: https://github.com/PCRE2Project/pcre2/commit/94e1
                        │      │                  │      c001761373b7d9450768aa15d04c25547a35 
                        │      │                  ├ [2]: https://github.com/PCRE2Project/pcre2/issues/141 
                        │      │                  ├ [3]: https://github.com/advisories/GHSA-4qfx-v7wh-3q4j 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2022-41409 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2022-41409 
                        │      ├ PublishedDate   : 2023-07-18T14:15:12.197Z 
                        │      ╰ LastModifiedDate: 2023-07-27T03:46:09.807Z 
                        ├ [54] ╭ VulnerabilityID : CVE-2021-23336 
                        │      ├ PkgID           : python-unversioned-command@3.9.18-1.el9_3.1.noarch 
                        │      ├ PkgName         : python-unversioned-command 
                        │      ├ InstalledVersion: 3.9.18-1.el9_3.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-23336 
                        │      ├ Title           : python: Web cache poisoning via urllib.parse.parse_qsl
                        │      │                   and urllib.parse.parse_qs by using a semicolon in query
                        │      │                   parameters 
                        │      ├ Description     : The package python/cpython from 0 and before 3.6.13,
                        │      │                   from 3.7.0 and before 3.7.10, from 3.8.0 and before 3.8.8,
                        │      │                   from 3.9.0 and before 3.9.2 are vulnerable to Web Cache
                        │      │                   Poisoning via urllib.parse.parse_qsl and
                        │      │                   urllib.parse.parse_qs by using a vector called parameter
                        │      │                   cloaking. When the attacker can separate query parameters
                        │      │                   using a semicolon (;), they can cause a difference in the
                        │      │                   interpretation of the request between the proxy (running
                        │      │                   with default configuration) and the server. This can result
                        │      │                   in malicious requests being cached as completely safe ones,
                        │      │                   as the proxy would usually not see the semicolon as a
                        │      │                   separator, and therefore would not include it in a cache key
                        │      │                    of an unkeyed parameter. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-444 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ bitnami    : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C
                        │      │                  │         │           :N/I:L/A:H 
                        │      │                  │         ╰ V3Score : 5.9 
                        │      │                  ├ nvd     ╭ V2Vector: AV:N/AC:H/Au:N/C:N/I:P/A:P 
                        │      │                  │         ├ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C
                        │      │                  │         │           :N/I:L/A:H 
                        │      │                  │         ├ V2Score : 4 
                        │      │                  │         ╰ V3Score : 5.9 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C
                        │      │                            │           :N/I:L/A:H 
                        │      │                            ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2021/
                        │      │                  │       02/19/4 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2021/
                        │      │                  │       05/01/2 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2021-23336 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2021-23336 
                        │      │                  ├ [4] : https://errata.almalinux.org/8/ALSA-2021-4162.html 
                        │      │                  ├ [5] : https://github.com/python/cpython/commit/fcbe0cb
                        │      │                  │       04d35189401c0c880ebfb4311e952d776 (master) 
                        │      │                  ├ [6] : https://github.com/python/cpython/pull/24297 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2021-23336.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2021-4162.html 
                        │      │                  ├ [9] : https://lists.apache.org/thread.html/ra8ce70088b
                        │      │                  │       a291f358e077cafdb14d174b7a1ce9a9d86d1b332d6367%40%3Cu
                        │      │                  │       sers.airflow.apache.org%3E 
                        │      │                  ├ [10]: https://lists.apache.org/thread.html/rc005f4de9d
                        │      │                  │       9b0ba943ceb8ff5a21a5c6ff8a9df52632476698d99432%40%3Ca
                        │      │                  │       nnounce.apache.org%3E 
                        │      │                  ├ [11]: https://lists.apache.org/thread.html/rf9fa47ab66
                        │      │                  │       495c78bb4120b0754dd9531ca2ff0430f6685ac9b07772%40%3Cd
                        │      │                  │       ev.mina.apache.org%3E 
                        │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/02/msg00030.html 
                        │      │                  ├ [13]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/04/msg00005.html 
                        │      │                  ├ [14]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/04/msg00015.html 
                        │      │                  ├ [15]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/09/msg00022.html 
                        │      │                  ├ [16]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/3EPY
                        │      │                  │       WWFDV22CJ5AOH5VCE72DOASZZ255/ 
                        │      │                  ├ [17]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/3YKK
                        │      │                  │       DLXL3UEZ3J426C2XTBS63AHE46SM/ 
                        │      │                  ├ [18]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/46N6
                        │      │                  │       A52EGSXHJYCZWVMBJJIH4NWIV2B5/ 
                        │      │                  ├ [19]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/FONH
                        │      │                  │       JIOZOFD7CD35KZL6SVBUTMBPGZGA/ 
                        │      │                  ├ [20]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/HCQT
                        │      │                  │       CSP6SCVIYNIRUJC5X7YBVUHPLSC4/ 
                        │      │                  ├ [21]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/HZTM
                        │      │                  │       7KLHFCE3LWSEVO2NAFLUHMGYMCRY/ 
                        │      │                  ├ [22]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/IHQD
                        │      │                  │       U7NXA7EWAE4W7VO6MURVJIULEPPR/ 
                        │      │                  ├ [23]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/KJXC
                        │      │                  │       MHLY7H3FIYLE4OKDYUILU2CCRUCZ/ 
                        │      │                  ├ [24]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/LVNH
                        │      │                  │       6Z24IG3E67ZCQGGJ46FZB4XFLQNZ/ 
                        │      │                  ├ [25]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/MNUN
                        │      │                  │       5SOMFL2BBKP6ZAICIIUPQKZDMGYO/ 
                        │      │                  ├ [26]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/MP57
                        │      │                  │       2OLHMS7MZO4KUPSCIMSZIA5IZZ62/ 
                        │      │                  ├ [27]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/N6VX
                        │      │                  │       JZSZ6N64AILJX4CTMACYGQGHHD5C/ 
                        │      │                  ├ [28]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/NJSC
                        │      │                  │       SN722JO2E2AGPWD4NTGVELVRPB4R/ 
                        │      │                  ├ [29]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/NODW
                        │      │                  │       HDIFBQE5RU5PUWUVE47JOT5VCMJ2/ 
                        │      │                  ├ [30]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/OAGS
                        │      │                  │       WNGZJ6HQ5ISA67SNMK3CJRKICET7/ 
                        │      │                  ├ [31]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/RSLQ
                        │      │                  │       D5CCM75IZGAMBDGUZEATYU5YSGJ7/ 
                        │      │                  ├ [32]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/SGIY
                        │      │                  │       6I4YS3WOXAK4SXKIEOC2G4VZKIR7/ 
                        │      │                  ├ [33]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/TFTE
                        │      │                  │       LUMWZE3KV3JB2H5EE6VFRZFRD5MV/ 
                        │      │                  ├ [34]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/W2LS
                        │      │                  │       KBEFI5SYEY5FM6ICZVZM5WRQUCS4/ 
                        │      │                  ├ [35]: https://nvd.nist.gov/vuln/detail/CVE-2021-23336 
                        │      │                  ├ [36]: https://security.gentoo.org/glsa/202104-04 
                        │      │                  ├ [37]: https://security.netapp.com/advisory/ntap-202103
                        │      │                  │       26-0004/ 
                        │      │                  ├ [38]: https://snyk.io/blog/cache-poisoning-in-popular-
                        │      │                  │       open-source-packages/ 
                        │      │                  ├ [39]: https://snyk.io/vuln/SNYK-UPSTREAM-PYTHONCPYTHON
                        │      │                  │       -1074933 
                        │      │                  ├ [40]: https://ubuntu.com/security/notices/USN-4742-1 
                        │      │                  ├ [41]: https://www.cve.org/CVERecord?id=CVE-2021-23336 
                        │      │                  ├ [42]: https://www.djangoproject.com/weblog/2021/feb/19
                        │      │                  │       /security-releases/ 
                        │      │                  ├ [43]: https://www.oracle.com//security-alerts/cpujul20
                        │      │                  │       21.html 
                        │      │                  ├ [44]: https://www.oracle.com/security-alerts/cpuApr202
                        │      │                  │       1.html 
                        │      │                  ├ [45]: https://www.oracle.com/security-alerts/cpujan202
                        │      │                  │       2.html 
                        │      │                  ╰ [46]: https://www.oracle.com/security-alerts/cpuoct202
                        │      │                          1.html 
                        │      ├ PublishedDate   : 2021-02-15T13:15:12.433Z 
                        │      ╰ LastModifiedDate: 2023-11-07T03:30:51.953Z 
                        ├ [55] ╭ VulnerabilityID : CVE-2022-0391 
                        │      ├ PkgID           : python-unversioned-command@3.9.18-1.el9_3.1.noarch 
                        │      ├ PkgName         : python-unversioned-command 
                        │      ├ InstalledVersion: 3.9.18-1.el9_3.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-0391 
                        │      ├ Title           : python: urllib.parse does not sanitize URLs containing
                        │      │                   ASCII newline and tabs 
                        │      ├ Description     : A flaw was found in Python, specifically within the
                        │      │                   urllib.parse module. This module helps break Uniform
                        │      │                   Resource Locator (URL) strings into components. The issue
                        │      │                   involves how the urlparse method does not sanitize input and
                        │      │                    allows characters like '\r' and '\n' in the URL path. This
                        │      │                   flaw allows an attacker to input a crafted URL, leading to
                        │      │                   injection attacks. This flaw affects Python versions prior
                        │      │                   to 3.10.0b1, 3.9.5, 3.8.11, 3.7.11 and 3.6.14. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ bitnami    : 3 
                        │      │                  ├ cbl-mariner: 3 
                        │      │                  ├ nvd        : 3 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ photon     : 3 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:H/A:N 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ├ nvd     ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:P/A:N 
                        │      │                  │         ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:H/A:N 
                        │      │                  │         ├ V2Score : 5 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                            │           :N/I:L/A:N 
                        │      │                            ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2022:6457 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2022-0391 
                        │      │                  ├ [2] : https://bugs.python.org/issue43882 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2047376 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2075390 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2022-0391 
                        │      │                  ├ [6] : https://errata.almalinux.org/8/ALSA-2022-6457.html 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2022-0391.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2023-3550.html 
                        │      │                  ├ [9] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/09/msg00022.html 
                        │      │                  ├ [10]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/CSD2
                        │      │                  │       YBXP3ZF44E44QMIIAR5VTO35KTRB/ 
                        │      │                  ├ [11]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/UDBD
                        │      │                  │       BAU6HUPZHISBOARTXZ5GKHF2VH5U/ 
                        │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2022-0391 
                        │      │                  ├ [13]: https://security.gentoo.org/glsa/202305-02 
                        │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202202
                        │      │                  │       25-0009/ 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-5342-1 
                        │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-5342-2 
                        │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2022-0391 
                        │      │                  ╰ [18]: https://www.oracle.com/security-alerts/cpuapr202
                        │      │                          2.html 
                        │      ├ PublishedDate   : 2022-02-09T23:15:16.58Z 
                        │      ╰ LastModifiedDate: 2023-11-07T03:41:13.75Z 
                        ├ [56] ╭ VulnerabilityID : CVE-2023-36632 
                        │      ├ PkgID           : python-unversioned-command@3.9.18-1.el9_3.1.noarch 
                        │      ├ PkgName         : python-unversioned-command 
                        │      ├ InstalledVersion: 3.9.18-1.el9_3.1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-36632 
                        │      ├ Title           : python: RecursionError: maximum recursion depth
                        │      │                   exceeded while calling a Python object 
                        │      ├ Description     : The legacy email.utils.parseaddr function in Python
                        │      │                   through 3.11.4 allows attackers to trigger "RecursionError:
                        │      │                   maximum recursion depth exceeded while calling a Python
                        │      │                   object" via a crafted argument. This argument is plausibly
                        │      │                   an untrusted value from an application's input data that was
                        │      │                    supposed to contain a name and an e-mail address. NOTE:
                        │      │                   email.utils.parseaddr is categorized as a Legacy API in the
                        │      │                   documentation of the Python email package. Applications
                        │      │                   should instead use the email.parser.BytesParser or
                        │      │                   email.parser.Parser class. NOTE: the vendor's perspective is
                        │      │                    that this is neither a vulnerability nor a bug. The email
                        │      │                   package is intended to have size limits and to throw an
                        │      │                   exception when limits are exceeded; they were exceeded by
                        │      │                   the example demonstration code. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-674 
                        │      ├ VendorSeverity   ╭ bitnami: 3 
                        │      │                  ├ nvd    : 3 
                        │      │                  ╰ redhat : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ├ nvd     ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                            │           :N/I:N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-36632 
                        │      │                  ├ [1]: https://docs.python.org/3/library/email.html 
                        │      │                  ├ [2]: https://docs.python.org/3/library/email.utils.html 
                        │      │                  ├ [3]: https://github.com/Daybreak2019/PoC_python3.9_Vul
                        │      │                  │      /blob/main/RecursionError-email.utils.parseaddr.py
                        │      │                  │      [m 
                        │      │                  ├ [4]: https://github.com/python/cpython/issues/103800 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-36632 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-36632 
                        │      ├ PublishedDate   : 2023-06-25T18:15:09.313Z 
                        │      ╰ LastModifiedDate: 2023-11-07T04:16:39.19Z 
                        ├ [57] ╭ VulnerabilityID : CVE-2021-23336 
                        │      ├ PkgID           : python3@3.9.18-1.el9_3.1.x86_64 
                        │      ├ PkgName         : python3 
                        │      ├ InstalledVersion: 3.9.18-1.el9_3.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-23336 
                        │      ├ Title           : python: Web cache poisoning via urllib.parse.parse_qsl
                        │      │                   and urllib.parse.parse_qs by using a semicolon in query
                        │      │                   parameters 
                        │      ├ Description     : The package python/cpython from 0 and before 3.6.13,
                        │      │                   from 3.7.0 and before 3.7.10, from 3.8.0 and before 3.8.8,
                        │      │                   from 3.9.0 and before 3.9.2 are vulnerable to Web Cache
                        │      │                   Poisoning via urllib.parse.parse_qsl and
                        │      │                   urllib.parse.parse_qs by using a vector called parameter
                        │      │                   cloaking. When the attacker can separate query parameters
                        │      │                   using a semicolon (;), they can cause a difference in the
                        │      │                   interpretation of the request between the proxy (running
                        │      │                   with default configuration) and the server. This can result
                        │      │                   in malicious requests being cached as completely safe ones,
                        │      │                   as the proxy would usually not see the semicolon as a
                        │      │                   separator, and therefore would not include it in a cache key
                        │      │                    of an unkeyed parameter. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-444 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ bitnami    : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C
                        │      │                  │         │           :N/I:L/A:H 
                        │      │                  │         ╰ V3Score : 5.9 
                        │      │                  ├ nvd     ╭ V2Vector: AV:N/AC:H/Au:N/C:N/I:P/A:P 
                        │      │                  │         ├ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C
                        │      │                  │         │           :N/I:L/A:H 
                        │      │                  │         ├ V2Score : 4 
                        │      │                  │         ╰ V3Score : 5.9 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C
                        │      │                            │           :N/I:L/A:H 
                        │      │                            ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2021/
                        │      │                  │       02/19/4 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2021/
                        │      │                  │       05/01/2 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2021-23336 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2021-23336 
                        │      │                  ├ [4] : https://errata.almalinux.org/8/ALSA-2021-4162.html 
                        │      │                  ├ [5] : https://github.com/python/cpython/commit/fcbe0cb
                        │      │                  │       04d35189401c0c880ebfb4311e952d776 (master) 
                        │      │                  ├ [6] : https://github.com/python/cpython/pull/24297 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2021-23336.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2021-4162.html 
                        │      │                  ├ [9] : https://lists.apache.org/thread.html/ra8ce70088b
                        │      │                  │       a291f358e077cafdb14d174b7a1ce9a9d86d1b332d6367%40%3Cu
                        │      │                  │       sers.airflow.apache.org%3E 
                        │      │                  ├ [10]: https://lists.apache.org/thread.html/rc005f4de9d
                        │      │                  │       9b0ba943ceb8ff5a21a5c6ff8a9df52632476698d99432%40%3Ca
                        │      │                  │       nnounce.apache.org%3E 
                        │      │                  ├ [11]: https://lists.apache.org/thread.html/rf9fa47ab66
                        │      │                  │       495c78bb4120b0754dd9531ca2ff0430f6685ac9b07772%40%3Cd
                        │      │                  │       ev.mina.apache.org%3E 
                        │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/02/msg00030.html 
                        │      │                  ├ [13]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/04/msg00005.html 
                        │      │                  ├ [14]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/04/msg00015.html 
                        │      │                  ├ [15]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/09/msg00022.html 
                        │      │                  ├ [16]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/3EPY
                        │      │                  │       WWFDV22CJ5AOH5VCE72DOASZZ255/ 
                        │      │                  ├ [17]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/3YKK
                        │      │                  │       DLXL3UEZ3J426C2XTBS63AHE46SM/ 
                        │      │                  ├ [18]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/46N6
                        │      │                  │       A52EGSXHJYCZWVMBJJIH4NWIV2B5/ 
                        │      │                  ├ [19]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/FONH
                        │      │                  │       JIOZOFD7CD35KZL6SVBUTMBPGZGA/ 
                        │      │                  ├ [20]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/HCQT
                        │      │                  │       CSP6SCVIYNIRUJC5X7YBVUHPLSC4/ 
                        │      │                  ├ [21]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/HZTM
                        │      │                  │       7KLHFCE3LWSEVO2NAFLUHMGYMCRY/ 
                        │      │                  ├ [22]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/IHQD
                        │      │                  │       U7NXA7EWAE4W7VO6MURVJIULEPPR/ 
                        │      │                  ├ [23]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/KJXC
                        │      │                  │       MHLY7H3FIYLE4OKDYUILU2CCRUCZ/ 
                        │      │                  ├ [24]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/LVNH
                        │      │                  │       6Z24IG3E67ZCQGGJ46FZB4XFLQNZ/ 
                        │      │                  ├ [25]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/MNUN
                        │      │                  │       5SOMFL2BBKP6ZAICIIUPQKZDMGYO/ 
                        │      │                  ├ [26]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/MP57
                        │      │                  │       2OLHMS7MZO4KUPSCIMSZIA5IZZ62/ 
                        │      │                  ├ [27]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/N6VX
                        │      │                  │       JZSZ6N64AILJX4CTMACYGQGHHD5C/ 
                        │      │                  ├ [28]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/NJSC
                        │      │                  │       SN722JO2E2AGPWD4NTGVELVRPB4R/ 
                        │      │                  ├ [29]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/NODW
                        │      │                  │       HDIFBQE5RU5PUWUVE47JOT5VCMJ2/ 
                        │      │                  ├ [30]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/OAGS
                        │      │                  │       WNGZJ6HQ5ISA67SNMK3CJRKICET7/ 
                        │      │                  ├ [31]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/RSLQ
                        │      │                  │       D5CCM75IZGAMBDGUZEATYU5YSGJ7/ 
                        │      │                  ├ [32]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/SGIY
                        │      │                  │       6I4YS3WOXAK4SXKIEOC2G4VZKIR7/ 
                        │      │                  ├ [33]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/TFTE
                        │      │                  │       LUMWZE3KV3JB2H5EE6VFRZFRD5MV/ 
                        │      │                  ├ [34]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/W2LS
                        │      │                  │       KBEFI5SYEY5FM6ICZVZM5WRQUCS4/ 
                        │      │                  ├ [35]: https://nvd.nist.gov/vuln/detail/CVE-2021-23336 
                        │      │                  ├ [36]: https://security.gentoo.org/glsa/202104-04 
                        │      │                  ├ [37]: https://security.netapp.com/advisory/ntap-202103
                        │      │                  │       26-0004/ 
                        │      │                  ├ [38]: https://snyk.io/blog/cache-poisoning-in-popular-
                        │      │                  │       open-source-packages/ 
                        │      │                  ├ [39]: https://snyk.io/vuln/SNYK-UPSTREAM-PYTHONCPYTHON
                        │      │                  │       -1074933 
                        │      │                  ├ [40]: https://ubuntu.com/security/notices/USN-4742-1 
                        │      │                  ├ [41]: https://www.cve.org/CVERecord?id=CVE-2021-23336 
                        │      │                  ├ [42]: https://www.djangoproject.com/weblog/2021/feb/19
                        │      │                  │       /security-releases/ 
                        │      │                  ├ [43]: https://www.oracle.com//security-alerts/cpujul20
                        │      │                  │       21.html 
                        │      │                  ├ [44]: https://www.oracle.com/security-alerts/cpuApr202
                        │      │                  │       1.html 
                        │      │                  ├ [45]: https://www.oracle.com/security-alerts/cpujan202
                        │      │                  │       2.html 
                        │      │                  ╰ [46]: https://www.oracle.com/security-alerts/cpuoct202
                        │      │                          1.html 
                        │      ├ PublishedDate   : 2021-02-15T13:15:12.433Z 
                        │      ╰ LastModifiedDate: 2023-11-07T03:30:51.953Z 
                        ├ [58] ╭ VulnerabilityID : CVE-2022-0391 
                        │      ├ PkgID           : python3@3.9.18-1.el9_3.1.x86_64 
                        │      ├ PkgName         : python3 
                        │      ├ InstalledVersion: 3.9.18-1.el9_3.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-0391 
                        │      ├ Title           : python: urllib.parse does not sanitize URLs containing
                        │      │                   ASCII newline and tabs 
                        │      ├ Description     : A flaw was found in Python, specifically within the
                        │      │                   urllib.parse module. This module helps break Uniform
                        │      │                   Resource Locator (URL) strings into components. The issue
                        │      │                   involves how the urlparse method does not sanitize input and
                        │      │                    allows characters like '\r' and '\n' in the URL path. This
                        │      │                   flaw allows an attacker to input a crafted URL, leading to
                        │      │                   injection attacks. This flaw affects Python versions prior
                        │      │                   to 3.10.0b1, 3.9.5, 3.8.11, 3.7.11 and 3.6.14. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ bitnami    : 3 
                        │      │                  ├ cbl-mariner: 3 
                        │      │                  ├ nvd        : 3 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ photon     : 3 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:H/A:N 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ├ nvd     ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:P/A:N 
                        │      │                  │         ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:H/A:N 
                        │      │                  │         ├ V2Score : 5 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                            │           :N/I:L/A:N 
                        │      │                            ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2022:6457 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2022-0391 
                        │      │                  ├ [2] : https://bugs.python.org/issue43882 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2047376 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2075390 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2022-0391 
                        │      │                  ├ [6] : https://errata.almalinux.org/8/ALSA-2022-6457.html 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2022-0391.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2023-3550.html 
                        │      │                  ├ [9] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/09/msg00022.html 
                        │      │                  ├ [10]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/CSD2
                        │      │                  │       YBXP3ZF44E44QMIIAR5VTO35KTRB/ 
                        │      │                  ├ [11]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/UDBD
                        │      │                  │       BAU6HUPZHISBOARTXZ5GKHF2VH5U/ 
                        │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2022-0391 
                        │      │                  ├ [13]: https://security.gentoo.org/glsa/202305-02 
                        │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202202
                        │      │                  │       25-0009/ 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-5342-1 
                        │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-5342-2 
                        │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2022-0391 
                        │      │                  ╰ [18]: https://www.oracle.com/security-alerts/cpuapr202
                        │      │                          2.html 
                        │      ├ PublishedDate   : 2022-02-09T23:15:16.58Z 
                        │      ╰ LastModifiedDate: 2023-11-07T03:41:13.75Z 
                        ├ [59] ╭ VulnerabilityID : CVE-2023-36632 
                        │      ├ PkgID           : python3@3.9.18-1.el9_3.1.x86_64 
                        │      ├ PkgName         : python3 
                        │      ├ InstalledVersion: 3.9.18-1.el9_3.1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-36632 
                        │      ├ Title           : python: RecursionError: maximum recursion depth
                        │      │                   exceeded while calling a Python object 
                        │      ├ Description     : The legacy email.utils.parseaddr function in Python
                        │      │                   through 3.11.4 allows attackers to trigger "RecursionError:
                        │      │                   maximum recursion depth exceeded while calling a Python
                        │      │                   object" via a crafted argument. This argument is plausibly
                        │      │                   an untrusted value from an application's input data that was
                        │      │                    supposed to contain a name and an e-mail address. NOTE:
                        │      │                   email.utils.parseaddr is categorized as a Legacy API in the
                        │      │                   documentation of the Python email package. Applications
                        │      │                   should instead use the email.parser.BytesParser or
                        │      │                   email.parser.Parser class. NOTE: the vendor's perspective is
                        │      │                    that this is neither a vulnerability nor a bug. The email
                        │      │                   package is intended to have size limits and to throw an
                        │      │                   exception when limits are exceeded; they were exceeded by
                        │      │                   the example demonstration code. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-674 
                        │      ├ VendorSeverity   ╭ bitnami: 3 
                        │      │                  ├ nvd    : 3 
                        │      │                  ╰ redhat : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ├ nvd     ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                            │           :N/I:N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-36632 
                        │      │                  ├ [1]: https://docs.python.org/3/library/email.html 
                        │      │                  ├ [2]: https://docs.python.org/3/library/email.utils.html 
                        │      │                  ├ [3]: https://github.com/Daybreak2019/PoC_python3.9_Vul
                        │      │                  │      /blob/main/RecursionError-email.utils.parseaddr.py
                        │      │                  │      [m 
                        │      │                  ├ [4]: https://github.com/python/cpython/issues/103800 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-36632 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-36632 
                        │      ├ PublishedDate   : 2023-06-25T18:15:09.313Z 
                        │      ╰ LastModifiedDate: 2023-11-07T04:16:39.19Z 
                        ├ [60] ╭ VulnerabilityID : CVE-2021-23336 
                        │      ├ PkgID           : python3-libs@3.9.18-1.el9_3.1.x86_64 
                        │      ├ PkgName         : python3-libs 
                        │      ├ InstalledVersion: 3.9.18-1.el9_3.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-23336 
                        │      ├ Title           : python: Web cache poisoning via urllib.parse.parse_qsl
                        │      │                   and urllib.parse.parse_qs by using a semicolon in query
                        │      │                   parameters 
                        │      ├ Description     : The package python/cpython from 0 and before 3.6.13,
                        │      │                   from 3.7.0 and before 3.7.10, from 3.8.0 and before 3.8.8,
                        │      │                   from 3.9.0 and before 3.9.2 are vulnerable to Web Cache
                        │      │                   Poisoning via urllib.parse.parse_qsl and
                        │      │                   urllib.parse.parse_qs by using a vector called parameter
                        │      │                   cloaking. When the attacker can separate query parameters
                        │      │                   using a semicolon (;), they can cause a difference in the
                        │      │                   interpretation of the request between the proxy (running
                        │      │                   with default configuration) and the server. This can result
                        │      │                   in malicious requests being cached as completely safe ones,
                        │      │                   as the proxy would usually not see the semicolon as a
                        │      │                   separator, and therefore would not include it in a cache key
                        │      │                    of an unkeyed parameter. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-444 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ bitnami    : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C
                        │      │                  │         │           :N/I:L/A:H 
                        │      │                  │         ╰ V3Score : 5.9 
                        │      │                  ├ nvd     ╭ V2Vector: AV:N/AC:H/Au:N/C:N/I:P/A:P 
                        │      │                  │         ├ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C
                        │      │                  │         │           :N/I:L/A:H 
                        │      │                  │         ├ V2Score : 4 
                        │      │                  │         ╰ V3Score : 5.9 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C
                        │      │                            │           :N/I:L/A:H 
                        │      │                            ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2021/
                        │      │                  │       02/19/4 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2021/
                        │      │                  │       05/01/2 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2021-23336 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2021-23336 
                        │      │                  ├ [4] : https://errata.almalinux.org/8/ALSA-2021-4162.html 
                        │      │                  ├ [5] : https://github.com/python/cpython/commit/fcbe0cb
                        │      │                  │       04d35189401c0c880ebfb4311e952d776 (master) 
                        │      │                  ├ [6] : https://github.com/python/cpython/pull/24297 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2021-23336.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2021-4162.html 
                        │      │                  ├ [9] : https://lists.apache.org/thread.html/ra8ce70088b
                        │      │                  │       a291f358e077cafdb14d174b7a1ce9a9d86d1b332d6367%40%3Cu
                        │      │                  │       sers.airflow.apache.org%3E 
                        │      │                  ├ [10]: https://lists.apache.org/thread.html/rc005f4de9d
                        │      │                  │       9b0ba943ceb8ff5a21a5c6ff8a9df52632476698d99432%40%3Ca
                        │      │                  │       nnounce.apache.org%3E 
                        │      │                  ├ [11]: https://lists.apache.org/thread.html/rf9fa47ab66
                        │      │                  │       495c78bb4120b0754dd9531ca2ff0430f6685ac9b07772%40%3Cd
                        │      │                  │       ev.mina.apache.org%3E 
                        │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/02/msg00030.html 
                        │      │                  ├ [13]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/04/msg00005.html 
                        │      │                  ├ [14]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/04/msg00015.html 
                        │      │                  ├ [15]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/09/msg00022.html 
                        │      │                  ├ [16]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/3EPY
                        │      │                  │       WWFDV22CJ5AOH5VCE72DOASZZ255/ 
                        │      │                  ├ [17]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/3YKK
                        │      │                  │       DLXL3UEZ3J426C2XTBS63AHE46SM/ 
                        │      │                  ├ [18]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/46N6
                        │      │                  │       A52EGSXHJYCZWVMBJJIH4NWIV2B5/ 
                        │      │                  ├ [19]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/FONH
                        │      │                  │       JIOZOFD7CD35KZL6SVBUTMBPGZGA/ 
                        │      │                  ├ [20]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/HCQT
                        │      │                  │       CSP6SCVIYNIRUJC5X7YBVUHPLSC4/ 
                        │      │                  ├ [21]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/HZTM
                        │      │                  │       7KLHFCE3LWSEVO2NAFLUHMGYMCRY/ 
                        │      │                  ├ [22]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/IHQD
                        │      │                  │       U7NXA7EWAE4W7VO6MURVJIULEPPR/ 
                        │      │                  ├ [23]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/KJXC
                        │      │                  │       MHLY7H3FIYLE4OKDYUILU2CCRUCZ/ 
                        │      │                  ├ [24]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/LVNH
                        │      │                  │       6Z24IG3E67ZCQGGJ46FZB4XFLQNZ/ 
                        │      │                  ├ [25]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/MNUN
                        │      │                  │       5SOMFL2BBKP6ZAICIIUPQKZDMGYO/ 
                        │      │                  ├ [26]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/MP57
                        │      │                  │       2OLHMS7MZO4KUPSCIMSZIA5IZZ62/ 
                        │      │                  ├ [27]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/N6VX
                        │      │                  │       JZSZ6N64AILJX4CTMACYGQGHHD5C/ 
                        │      │                  ├ [28]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/NJSC
                        │      │                  │       SN722JO2E2AGPWD4NTGVELVRPB4R/ 
                        │      │                  ├ [29]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/NODW
                        │      │                  │       HDIFBQE5RU5PUWUVE47JOT5VCMJ2/ 
                        │      │                  ├ [30]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/OAGS
                        │      │                  │       WNGZJ6HQ5ISA67SNMK3CJRKICET7/ 
                        │      │                  ├ [31]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/RSLQ
                        │      │                  │       D5CCM75IZGAMBDGUZEATYU5YSGJ7/ 
                        │      │                  ├ [32]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/SGIY
                        │      │                  │       6I4YS3WOXAK4SXKIEOC2G4VZKIR7/ 
                        │      │                  ├ [33]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/TFTE
                        │      │                  │       LUMWZE3KV3JB2H5EE6VFRZFRD5MV/ 
                        │      │                  ├ [34]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/W2LS
                        │      │                  │       KBEFI5SYEY5FM6ICZVZM5WRQUCS4/ 
                        │      │                  ├ [35]: https://nvd.nist.gov/vuln/detail/CVE-2021-23336 
                        │      │                  ├ [36]: https://security.gentoo.org/glsa/202104-04 
                        │      │                  ├ [37]: https://security.netapp.com/advisory/ntap-202103
                        │      │                  │       26-0004/ 
                        │      │                  ├ [38]: https://snyk.io/blog/cache-poisoning-in-popular-
                        │      │                  │       open-source-packages/ 
                        │      │                  ├ [39]: https://snyk.io/vuln/SNYK-UPSTREAM-PYTHONCPYTHON
                        │      │                  │       -1074933 
                        │      │                  ├ [40]: https://ubuntu.com/security/notices/USN-4742-1 
                        │      │                  ├ [41]: https://www.cve.org/CVERecord?id=CVE-2021-23336 
                        │      │                  ├ [42]: https://www.djangoproject.com/weblog/2021/feb/19
                        │      │                  │       /security-releases/ 
                        │      │                  ├ [43]: https://www.oracle.com//security-alerts/cpujul20
                        │      │                  │       21.html 
                        │      │                  ├ [44]: https://www.oracle.com/security-alerts/cpuApr202
                        │      │                  │       1.html 
                        │      │                  ├ [45]: https://www.oracle.com/security-alerts/cpujan202
                        │      │                  │       2.html 
                        │      │                  ╰ [46]: https://www.oracle.com/security-alerts/cpuoct202
                        │      │                          1.html 
                        │      ├ PublishedDate   : 2021-02-15T13:15:12.433Z 
                        │      ╰ LastModifiedDate: 2023-11-07T03:30:51.953Z 
                        ├ [61] ╭ VulnerabilityID : CVE-2022-0391 
                        │      ├ PkgID           : python3-libs@3.9.18-1.el9_3.1.x86_64 
                        │      ├ PkgName         : python3-libs 
                        │      ├ InstalledVersion: 3.9.18-1.el9_3.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-0391 
                        │      ├ Title           : python: urllib.parse does not sanitize URLs containing
                        │      │                   ASCII newline and tabs 
                        │      ├ Description     : A flaw was found in Python, specifically within the
                        │      │                   urllib.parse module. This module helps break Uniform
                        │      │                   Resource Locator (URL) strings into components. The issue
                        │      │                   involves how the urlparse method does not sanitize input and
                        │      │                    allows characters like '\r' and '\n' in the URL path. This
                        │      │                   flaw allows an attacker to input a crafted URL, leading to
                        │      │                   injection attacks. This flaw affects Python versions prior
                        │      │                   to 3.10.0b1, 3.9.5, 3.8.11, 3.7.11 and 3.6.14. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ VendorSeverity   ╭ alma       : 2 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ bitnami    : 3 
                        │      │                  ├ cbl-mariner: 3 
                        │      │                  ├ nvd        : 3 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ photon     : 3 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:H/A:N 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ├ nvd     ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:P/A:N 
                        │      │                  │         ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:H/A:N 
                        │      │                  │         ├ V2Score : 5 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                            │           :N/I:L/A:N 
                        │      │                            ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2022:6457 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2022-0391 
                        │      │                  ├ [2] : https://bugs.python.org/issue43882 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2047376 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2075390 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2022-0391 
                        │      │                  ├ [6] : https://errata.almalinux.org/8/ALSA-2022-6457.html 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2022-0391.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2023-3550.html 
                        │      │                  ├ [9] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/09/msg00022.html 
                        │      │                  ├ [10]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/CSD2
                        │      │                  │       YBXP3ZF44E44QMIIAR5VTO35KTRB/ 
                        │      │                  ├ [11]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/UDBD
                        │      │                  │       BAU6HUPZHISBOARTXZ5GKHF2VH5U/ 
                        │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2022-0391 
                        │      │                  ├ [13]: https://security.gentoo.org/glsa/202305-02 
                        │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202202
                        │      │                  │       25-0009/ 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-5342-1 
                        │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-5342-2 
                        │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2022-0391 
                        │      │                  ╰ [18]: https://www.oracle.com/security-alerts/cpuapr202
                        │      │                          2.html 
                        │      ├ PublishedDate   : 2022-02-09T23:15:16.58Z 
                        │      ╰ LastModifiedDate: 2023-11-07T03:41:13.75Z 
                        ├ [62] ╭ VulnerabilityID : CVE-2023-36632 
                        │      ├ PkgID           : python3-libs@3.9.18-1.el9_3.1.x86_64 
                        │      ├ PkgName         : python3-libs 
                        │      ├ InstalledVersion: 3.9.18-1.el9_3.1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-36632 
                        │      ├ Title           : python: RecursionError: maximum recursion depth
                        │      │                   exceeded while calling a Python object 
                        │      ├ Description     : The legacy email.utils.parseaddr function in Python
                        │      │                   through 3.11.4 allows attackers to trigger "RecursionError:
                        │      │                   maximum recursion depth exceeded while calling a Python
                        │      │                   object" via a crafted argument. This argument is plausibly
                        │      │                   an untrusted value from an application's input data that was
                        │      │                    supposed to contain a name and an e-mail address. NOTE:
                        │      │                   email.utils.parseaddr is categorized as a Legacy API in the
                        │      │                   documentation of the Python email package. Applications
                        │      │                   should instead use the email.parser.BytesParser or
                        │      │                   email.parser.Parser class. NOTE: the vendor's perspective is
                        │      │                    that this is neither a vulnerability nor a bug. The email
                        │      │                   package is intended to have size limits and to throw an
                        │      │                   exception when limits are exceeded; they were exceeded by
                        │      │                   the example demonstration code. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-674 
                        │      ├ VendorSeverity   ╭ bitnami: 3 
                        │      │                  ├ nvd    : 3 
                        │      │                  ╰ redhat : 2 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ├ nvd     ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                  │         │           :N/I:N/A:H 
                        │      │                  │         ╰ V3Score : 7.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C
                        │      │                            │           :N/I:N/A:H 
                        │      │                            ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-36632 
                        │      │                  ├ [1]: https://docs.python.org/3/library/email.html 
                        │      │                  ├ [2]: https://docs.python.org/3/library/email.utils.html 
                        │      │                  ├ [3]: https://github.com/Daybreak2019/PoC_python3.9_Vul
                        │      │                  │      /blob/main/RecursionError-email.utils.parseaddr.py
                        │      │                  │      [m 
                        │      │                  ├ [4]: https://github.com/python/cpython/issues/103800 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-36632 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-36632 
                        │      ├ PublishedDate   : 2023-06-25T18:15:09.313Z 
                        │      ╰ LastModifiedDate: 2023-11-07T04:16:39.19Z 
                        ├ [63] ╭ VulnerabilityID : CVE-2021-3572 
                        │      ├ PkgID           : python3-pip-wheel@21.2.3-7.el9.noarch 
                        │      ├ PkgName         : python3-pip-wheel 
                        │      ├ InstalledVersion: 21.2.3-7.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-3572 
                        │      ├ Title           : python-pip: Incorrect handling of unicode separators in
                        │      │                    git references 
                        │      ├ Description     : A flaw was found in python-pip in the way it handled
                        │      │                   Unicode separators in git references. A remote attacker
                        │      │                   could possibly use this issue to install a different
                        │      │                   revision on a repository. The highest threat from this
                        │      │                   vulnerability is to data integrity. This is fixed in
                        │      │                   python-pip version 21.1. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-20 
                        │      ├ VendorSeverity   ╭ alma       : 1 
                        │      │                  ├ amazon     : 2 
                        │      │                  ├ bitnami    : 2 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ ghsa       : 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ oracle-oval: 3 
                        │      │                  ├ redhat     : 1 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C
                        │      │                  │         │           :N/I:H/A:N 
                        │      │                  │         ╰ V3Score : 5.7 
                        │      │                  ├ ghsa    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C
                        │      │                  │         │           :N/I:H/A:N 
                        │      │                  │         ╰ V3Score : 5.7 
                        │      │                  ├ nvd     ╭ V2Vector: AV:N/AC:M/Au:S/C:N/I:P/A:N 
                        │      │                  │         ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C
                        │      │                  │         │           :N/I:H/A:N 
                        │      │                  │         ├ V2Score : 3.5 
                        │      │                  │         ╰ V3Score : 5.7 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:U/C
                        │      │                            │           :N/I:H/A:N 
                        │      │                            ╰ V3Score : 4.5 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2021:3254 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2021-3572 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=1962856 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2021-3572 
                        │      │                  ├ [4] : https://github.com/pypa/pip 
                        │      │                  ├ [5] : https://github.com/pypa/pip/commit/e46bdda971139
                        │      │                  │       2fec0c45c1175bae6db847cb30b 
                        │      │                  ├ [6] : https://github.com/pypa/pip/issues/10042 
                        │      │                  ├ [7] : https://github.com/pypa/pip/issues/10042#issueco
                        │      │                  │       mment-857452480 
                        │      │                  ├ [8] : https://github.com/pypa/pip/pull/9827 
                        │      │                  ├ [9] : https://github.com/skazi0/CVE-2021-3572/blob/mas
                        │      │                  │       ter/CVE-2021-3572-v9.0.1.patch 
                        │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2021-3572.html 
                        │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2023-12349.html 
                        │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2021-3572 
                        │      │                  ├ [13]: https://packetstormsecurity.com/files/162712/USN
                        │      │                  │       -4961-1.txt 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-4961-2 
                        │      │                  ├ [15]: https://www.cve.org/CVERecord?id=CVE-2021-3572 
                        │      │                  ├ [16]: https://www.oracle.com/security-alerts/cpuapr202
                        │      │                  │       2.html 
                        │      │                  ╰ [17]: https://www.oracle.com/security-alerts/cpujul202
                        │      │                          2.html 
                        │      ├ PublishedDate   : 2021-11-10T18:15:09.51Z 
                        │      ╰ LastModifiedDate: 2022-10-05T02:14:39.75Z 
                        ├ [64] ╭ VulnerabilityID : CVE-2024-0232 
                        │      ├ PkgID           : sqlite-libs@3.34.1-7.el9_3.x86_64 
                        │      ├ PkgName         : sqlite-libs 
                        │      ├ InstalledVersion: 3.34.1-7.el9_3 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2024-0232 
                        │      ├ Title           : sqlite: use-after-free bug in jsonParseAddNodeArray 
                        │      ├ Description     : A heap use-after-free issue has been identified in
                        │      │                   SQLite in the jsonParseAddNodeArray() function in sqlite3.c.
                        │      │                    This flaw allows a local attacker to leverage a victim to
                        │      │                   pass specially crafted malicious input to the application,
                        │      │                   potentially causing a crash and leading to a denial of
                        │      │                   service. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-416 
                        │      ├ VendorSeverity   ╭ bitnami: 2 
                        │      │                  ├ nvd    : 2 
                        │      │                  ╰ redhat : 1 
                        │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C
                        │      │                  │         │           :N/I:N/A:H 
                        │      │                  │         ╰ V3Score : 5.5 
                        │      │                  ├ nvd     ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C
                        │      │                  │         │           :N/I:N/A:H 
                        │      │                  │         ╰ V3Score : 5.5 
                        │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:U/C
                        │      │                            │           :N/I:N/A:H 
                        │      │                            ╰ V3Score : 4.7 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2024-0232 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2243754 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2024-0232 
                        │      │                  ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2024-0232 
                        │      ├ PublishedDate   : 2024-01-16T14:15:48.327Z 
                        │      ╰ LastModifiedDate: 2024-01-24T14:14:14.603Z 
                        ├ [65] ╭ VulnerabilityID : CVE-2023-28486 
                        │      ├ PkgID           : sudo@1.9.5p2-9.el9.x86_64 
                        │      ├ PkgName         : sudo 
                        │      ├ InstalledVersion: 1.9.5p2-9.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28486 
                        │      ├ Title           : sudo: Sudo does not escape control characters in log
                        │      │                   messages 
                        │      ├ Description     : Sudo before 1.9.13 does not escape control characters
                        │      │                   in log messages. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-116 
                        │      ├ VendorSeverity   ╭ amazon     : 3 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           L/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           L/I:N/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-28486 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-28486 
                        │      │                  ├ [2]: https://github.com/sudo-project/sudo/commit/334da
                        │      │                  │      f92b31b79ce68ed75e2ee14fca265f029ca 
                        │      │                  ├ [3]: https://github.com/sudo-project/sudo/releases/tag
                        │      │                  │      /SUDO_1_9_13 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-28486 
                        │      │                  ├ [5]: https://security.gentoo.org/glsa/202309-12 
                        │      │                  ├ [6]: https://security.netapp.com/advisory/ntap-2023042
                        │      │                  │      0-0002/ 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-6005-1 
                        │      │                  ├ [8]: https://ubuntu.com/security/notices/USN-6005-2 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-28486 
                        │      ├ PublishedDate   : 2023-03-16T01:15:47.003Z 
                        │      ╰ LastModifiedDate: 2023-11-02T01:59:06.177Z 
                        ├ [66] ╭ VulnerabilityID : CVE-2023-28487 
                        │      ├ PkgID           : sudo@1.9.5p2-9.el9.x86_64 
                        │      ├ PkgName         : sudo 
                        │      ├ InstalledVersion: 1.9.5p2-9.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28487 
                        │      ├ Title           : sudo: Sudo does not escape control characters in
                        │      │                   sudoreplay output 
                        │      ├ Description     : Sudo before 1.9.13 does not escape control characters
                        │      │                   in sudoreplay output. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-116 
                        │      ├ VendorSeverity   ╭ amazon     : 3 
                        │      │                  ├ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ photon     : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           L/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           L/I:N/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-28487 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-28487 
                        │      │                  ├ [2]: https://github.com/sudo-project/sudo/commit/334da
                        │      │                  │      f92b31b79ce68ed75e2ee14fca265f029ca 
                        │      │                  ├ [3]: https://github.com/sudo-project/sudo/releases/tag
                        │      │                  │      /SUDO_1_9_13 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-28487 
                        │      │                  ├ [5]: https://security.gentoo.org/glsa/202309-12 
                        │      │                  ├ [6]: https://security.netapp.com/advisory/ntap-2023042
                        │      │                  │      0-0002/ 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-6005-1 
                        │      │                  ├ [8]: https://ubuntu.com/security/notices/USN-6005-2 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-28487 
                        │      ├ PublishedDate   : 2023-03-16T01:15:47.067Z 
                        │      ╰ LastModifiedDate: 2023-11-02T01:58:22.777Z 
                        ├ [67] ╭ VulnerabilityID : CVE-2023-42465 
                        │      ├ PkgID           : sudo@1.9.5p2-9.el9.x86_64 
                        │      ├ PkgName         : sudo 
                        │      ├ InstalledVersion: 1.9.5p2-9.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-42465 
                        │      ├ Title           : sudo: Targeted Corruption of Register and Stack Variables 
                        │      ├ Description     : Sudo before 1.9.15 might allow row hammer attacks (for
                        │      │                   authentication bypass or privilege escalation) because
                        │      │                   application logic sometimes is based on not equaling an
                        │      │                   error value (instead of equaling a success value), and
                        │      │                   because the values do not resist flips of a single bit.[
                        │      │                   m 
                        │      ├ Severity        : MEDIUM 
                        │      ├ VendorSeverity   ╭ cbl-mariner: 3 
                        │      │                  ├ nvd        : 3 
                        │      │                  ├ photon     : 3 
                        │      │                  ╰ redhat     : 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:
                        │      │                           │           H/I:H/A:H 
                        │      │                           ╰ V3Score : 7 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-42465 
                        │      │                  ├ [1] : https://arxiv.org/abs/2309.02545 
                        │      │                  ├ [2] : https://arxiv.org/pdf/2309.02545.pdf 
                        │      │                  ├ [3] : https://github.com/sudo-project/sudo/commit/7873
                        │      │                  │       f8334c8d31031f8cfa83bd97ac6029309e4f 
                        │      │                  ├ [4] : https://github.com/sudo-project/sudo/releases/ta
                        │      │                  │       g/SUDO_1_9_15 
                        │      │                  ├ [5] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce%40lists.fedoraproject.org/message/U6XM
                        │      │                  │       RUJCPII4MPWG43HTYR76DGLEYEFZ/ 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-42465 
                        │      │                  ├ [7] : https://security.gentoo.org/glsa/202401-29 
                        │      │                  ├ [8] : https://www.cve.org/CVERecord?id=CVE-2023-42465 
                        │      │                  ├ [9] : https://www.openwall.com/lists/oss-security/2023
                        │      │                  │       /12/21/9 
                        │      │                  ╰ [10]: https://www.sudo.ws/releases/changelog/ 
                        │      ├ PublishedDate   : 2023-12-22T16:15:08.057Z 
                        │      ╰ LastModifiedDate: 2024-01-28T04:15:07.59Z 
                        ├ [68] ╭ VulnerabilityID : CVE-2021-3997 
                        │      ├ PkgID           : systemd-libs@252-18.el9.x86_64 
                        │      ├ PkgName         : systemd-libs 
                        │      ├ InstalledVersion: 252-18.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-3997 
                        │      ├ Title           : Uncontrolled recursion in systemd-tmpfiles when
                        │      │                   removing files 
                        │      ├ Description     : A flaw was found in systemd. An uncontrolled recursion
                        │      │                   in systemd-tmpfiles may lead to a denial of service at boot
                        │      │                   time when too many nested directories are created in
                        │      │                   /tmp. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-674 
                        │      ├ VendorSeverity   ╭ amazon: 2 
                        │      │                  ├ nvd   : 2 
                        │      │                  ├ photon: 2 
                        │      │                  ├ redhat: 2 
                        │      │                  ╰ ubuntu: 2 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-3997 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2024639 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2021-3997 
                        │      │                  ├ [3]: https://github.com/systemd/systemd/commit/5b1cf7a
                        │      │                  │      9be37e20133c0208005274ce4a5b5c6a1 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2021-3997 
                        │      │                  ├ [5]: https://security.gentoo.org/glsa/202305-15 
                        │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-5226-1 
                        │      │                  ├ [7]: https://www.cve.org/CVERecord?id=CVE-2021-3997 
                        │      │                  ╰ [8]: https://www.openwall.com/lists/oss-security/2022/
                        │      │                         01/10/2 
                        │      ├ PublishedDate   : 2022-08-23T20:15:08.67Z 
                        │      ╰ LastModifiedDate: 2023-05-03T12:15:15.95Z 
                        ├ [69] ╭ VulnerabilityID : CVE-2023-7008 
                        │      ├ PkgID           : systemd-libs@252-18.el9.x86_64 
                        │      ├ PkgName         : systemd-libs 
                        │      ├ InstalledVersion: 252-18.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-7008 
                        │      ├ Title           : systemd-resolved: Unsigned name response in signed zone
                        │      │                    is not refused when DNSSEC=yes 
                        │      ├ Description     : A vulnerability was found in systemd-resolved. This
                        │      │                   issue may allow systemd-resolved to accept records of
                        │      │                   DNSSEC-signed domains even when they have no signature,
                        │      │                   allowing man-in-the-middles (or the upstream DNS resolver)
                        │      │                   to manipulate records. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-300 
                        │      ├ VendorSeverity   ╭ cbl-mariner: 2 
                        │      │                  ├ nvd        : 2 
                        │      │                  ├ redhat     : 2 
                        │      │                  ╰ ubuntu     : 1 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:H/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:H/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-7008 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2222261 
                        │      │                  ├ [2]: https://bugzilla.redhat.com/show_bug.cgi?id=2222672 
                        │      │                  ├ [3]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-7008 
                        │      │                  ├ [4]: https://github.com/systemd/systemd/issues/25676 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/4GMDEG5P
                        │      │                  │      KONWNHOEYSUDRT6JEOISRMN2/ 
                        │      │                  ├ [6]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/QHNBXGKJ
                        │      │                  │      WISJETTTDTZKTBFIBJUOSLKL/ 
                        │      │                  ├ [7]: https://nvd.nist.gov/vuln/detail/CVE-2023-7008 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-7008 
                        │      ├ PublishedDate   : 2023-12-23T13:15:07.573Z 
                        │      ╰ LastModifiedDate: 2024-01-27T03:15:07.933Z 
                        ├ [70] ╭ VulnerabilityID : CVE-2005-2541 
                        │      ├ PkgID           : tar@1.34-6.el9_1.x86_64 
                        │      ├ PkgName         : tar 
                        │      ├ InstalledVersion: 2:1.34-6.el9_1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                        │      │                  │         550b2054679b3909297ce5b98 
                        │      │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                        │      │                            00d5a7b7d0fe8361b2354be85 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2005-2541 
                        │      ├ Title           : tar: does not properly warn the user when extracting
                        │      │                   setuid or setgid files 
                        │      ├ Description     : Tar 1.15.1 does not properly warn the user when
                        │      │                   extracting setuid or setgid files, which may allow local
                        │      │                   users or remote attackers to gain privileges. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ VendorSeverity   ╭ nvd   : 3 
                        │      │                  ╰ redhat: 2 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:C/I:C/A:C 
                        │      │                  │        ╰ V2Score : 10 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:U/C:
                        │      │                           │           H/I:H/A:H 
                        │      │                           ╰ V3Score : 7 
                        │      ├ References       ╭ [0]: http://marc.info/?l=bugtraq&m=112327628230258&w=2 
                        │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2005-2541 
                        │      │                  ├ [2]: https://lists.apache.org/thread.html/rc713534b10f
                        │      │                  │      9daeee2e0990239fa407e2118e4aa9e88a7041177497c%40%3Ciss
                        │      │                  │      ues.guacamole.apache.org%3E 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2005-2541 
                        │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2005-2541 
                        │      ├ PublishedDate   : 2005-08-10T04:00:00Z 
                        │      ╰ LastModifiedDate: 2023-11-07T01:57:39.453Z 
                        ╰ [71] ╭ VulnerabilityID : CVE-2023-39804 
                               ├ PkgID           : tar@1.34-6.el9_1.x86_64 
                               ├ PkgName         : tar 
                               ├ InstalledVersion: 2:1.34-6.el9_1 
                               ├ Status          : will_not_fix 
                               ├ Layer            ╭ Digest: sha256:abad931c50e5e687a3f8a51fca01310c067e94a
                               │                  │         550b2054679b3909297ce5b98 
                               │                  ╰ DiffID: sha256:c87dda8a77b3c06dd67bc9e327e53649c35290a
                               │                            00d5a7b7d0fe8361b2354be85 
                               ├ SeveritySource  : redhat 
                               ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-39804 
                               ├ Title           : tar: Incorrectly handled extension attributes in PAX
                               │                   archives can lead to a crash 
                               ├ Description     : A flaw was found in tar. This issue occurs when
                               │                   extended attributes are processed in PAX archives, and could
                               │                    allow an attacker to cause an application crash, resulting
                               │                   in a denial of service. 
                               ├ Severity        : LOW 
                               ├ VendorSeverity   ╭ amazon: 1 
                               │                  ├ photon: 1 
                               │                  ├ redhat: 1 
                               │                  ╰ ubuntu: 2 
                               ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                               │                           │           N/I:N/A:L 
                               │                           ╰ V3Score : 3.3 
                               ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-39804 
                                                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                                                  │      E-2023-39804 
                                                  ├ [2]: https://git.savannah.gnu.org/cgit/tar.git/commit/
                                                  │      ?id=a339f05cd269013fa133d2f148d73f6f7d4247e4 
                                                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-39804 
                                                  ├ [4]: https://ubuntu.com/security/notices/USN-6543-1 
                                                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-39804 
````
