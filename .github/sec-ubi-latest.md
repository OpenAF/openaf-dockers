````yaml
─ [0] ╭ Target         : openaf/oaf:ubi (redhat 9.2) 
      ├ Class          : os-pkgs 
      ├ Type           : redhat 
      ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2021-3468 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9_2.1.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-3468 
                        │      ├ Title           : avahi: Local DoS by event-busy-loop from writing long
                        │      │                   lines to /run/avahi-daemon/socket 
                        │      ├ Description     : A flaw was found in avahi in versions 0.6 up to 0.8.
                        │      │                   The event used to signal the termination of the client
                        │      │                   connection on the avahi Unix socket is not correctly handled
                        │      │                    in the client_work function, allowing a local attacker to
                        │      │                   trigger an infinite loop. The highest threat from this
                        │      │                   vulnerability is to the availability of the avahi service,
                        │      │                   which becomes unresponsive after this flaw is
                        │      │                   triggered. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-835 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:L/AC:L/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ├ V2Score : 2.1 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-3468 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1939614 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2021-3468 
                        │      │                  ├ [3]: https://lists.debian.org/debian-lts-announce/2022
                        │      │                  │      /06/msg00009.html 
                        │      │                  ├ [4]: https://lists.debian.org/debian-lts-announce/2023
                        │      │                  │      /06/msg00028.html 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2021-3468 
                        │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-5008-1 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-5008-2 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2021-3468 
                        │      ├ PublishedDate   : 2021-06-02T16:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-22T02:15:00Z 
                        ├ [1]  ╭ VulnerabilityID : CVE-2021-3502 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9_2.1.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-3502 
                        │      ├ Title           : reachable assertion in avahi_s_host_name_resolver_start
                        │      │                    when trying to resolve badly-formatted hostnames 
                        │      ├ Description     : A flaw was found in avahi 0.8-5. A reachable assertion
                        │      │                   is present in avahi_s_host_name_resolver_start function
                        │      │                   allowing a local attacker to crash the avahi service by
                        │      │                   requesting hostname resolutions through the avahi socket or
                        │      │                   dbus methods for invalid hostnames. The highest threat from
                        │      │                   this vulnerability is to the service availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ╭ [0]: CWE-476 
                        │      │                  ╰ [1]: CWE-617 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:L/AC:L/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ├ V2Score : 2.1 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-3502 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1946914 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2021-3502 
                        │      │                  ├ [3]: https://github.com/lathiat/avahi/issues/338 
                        │      │                  ├ [4]: https://github.com/lathiat/avahi/pull/324 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2021-3502 
                        │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-5008-1 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2021-3502 
                        │      ├ PublishedDate   : 2021-05-07T12:15:00Z 
                        │      ╰ LastModifiedDate: 2021-05-17T17:30:00Z 
                        ├ [2]  ╭ VulnerabilityID : CVE-2023-1981 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9_2.1.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9_2.1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-1981 
                        │      ├ Title           : avahi-daemon can be crashed via DBus 
                        │      ├ Description     : A vulnerability was found in the avahi library. This
                        │      │                   flaw allows an unprivileged user to make a dbus call,
                        │      │                   causing the avahi daemon to crash. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-400 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-1981 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2185911 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-1981 
                        │      │                  ├ [3]: https://github.com/lathiat/avahi/issues/375 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-1981 
                        │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-6129-1 
                        │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-6129-2 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2023-1981 
                        │      ├ PublishedDate   : 2023-05-26T18:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-02T19:06:00Z 
                        ├ [3]  ╭ VulnerabilityID : CVE-2023-38469 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9_2.1.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-38469 
                        │      ├ Title           : Reachable assertion in avahi_dns_packet_append_record 
                        │      ├ Description     : No description is available for this CVE. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-38469 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2023-38469 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-38469 
                        │                         ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2023-38469 
                        ├ [4]  ╭ VulnerabilityID : CVE-2023-38470 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9_2.1.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-38470 
                        │      ├ Title           : Reachable assertion in avahi_escape_label 
                        │      ├ Description     : No description is available for this CVE. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-38470 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2023-38470 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-38470 
                        │                         ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2023-38470 
                        ├ [5]  ╭ VulnerabilityID : CVE-2023-38471 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9_2.1.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-38471 
                        │      ├ Title           : Reachable assertion in dbus_set_host_name 
                        │      ├ Description     : No description is available for this CVE. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-38471 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2023-38471 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-38471 
                        │                         ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2023-38471 
                        ├ [6]  ╭ VulnerabilityID : CVE-2023-38472 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9_2.1.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-38472 
                        │      ├ Title           : Reachable assertion in avahi_rdata_parse 
                        │      ├ Description     : No description is available for this CVE. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-38472 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2023-38472 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-38472 
                        │                         ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2023-38472 
                        ├ [7]  ╭ VulnerabilityID : CVE-2023-38473 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9_2.1.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-38473 
                        │      ├ Title           : Reachable assertion in avahi_alternative_host_name 
                        │      ├ Description     : No description is available for this CVE. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-38473 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2023-38473 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-38473 
                        │                         ╰ [3]: https://www.cve.org/CVERecord?id=CVE-2023-38473 
                        ├ [8]  ╭ VulnerabilityID : CVE-2017-6519 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9_2.1.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2017-6519 
                        │      ├ Title           : Multicast DNS responds to unicast queries outside of
                        │      │                   local network 
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
                        │      │                  │       5bc8466e24ff0ecc5e75b45a705334ab6a444e64e840a0@%3Ciss
                        │      │                  │       ues.bookkeeper.apache.org%3E 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2017-6519 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-3876-1 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-3876-2 
                        │      │                  ├ [11]: https://usn.ubuntu.com/3876-1/ 
                        │      │                  ├ [12]: https://usn.ubuntu.com/3876-2/ 
                        │      │                  ├ [13]: https://www.cve.org/CVERecord?id=CVE-2017-6519 
                        │      │                  ├ [14]: https://www.kb.cert.org/vuls/id/550620 
                        │      │                  ╰ [15]: https://www.secfu.net/advisories 
                        │      ├ PublishedDate   : 2017-05-01T01:59:00Z 
                        │      ╰ LastModifiedDate: 2020-07-29T12:15:00Z 
                        ├ [9]  ╭ VulnerabilityID : CVE-2023-32360 
                        │      ├ PkgID           : cups-libs@2.3.3op2-16.el9.x86_64 
                        │      ├ PkgName         : cups-libs 
                        │      ├ InstalledVersion: 1:2.3.3op2-16.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-32360 
                        │      ├ Title           : Information leak through Cups-Get-Document operation 
                        │      ├ Description     : An authentication issue was addressed with improved
                        │      │                   state management. This issue is fixed in macOS Big Sur
                        │      │                   11.7.7, macOS Monterey 12.6.6, macOS Ventura 13.4. An
                        │      │                   unauthenticated user may be able to access recently printed
                        │      │                   documents. 
                        │      ├ Severity        : HIGH 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-32360 
                        │      │                  ├ [1]: https://nvd.nist.gov/vuln/detail/CVE-2023-32360 
                        │      │                  ├ [2]: https://support.apple.com/en-us/HT213758 
                        │      │                  ├ [3]: https://support.apple.com/en-us/HT213759 
                        │      │                  ├ [4]: https://support.apple.com/en-us/HT213760 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-32360 
                        │      ├ PublishedDate   : 2023-06-23T18:15:00Z 
                        │      ╰ LastModifiedDate: 2023-07-27T04:15:00Z 
                        ├ [10] ╭ VulnerabilityID : CVE-2023-32324 
                        │      ├ PkgID           : cups-libs@2.3.3op2-16.el9.x86_64 
                        │      ├ PkgName         : cups-libs 
                        │      ├ InstalledVersion: 1:2.3.3op2-16.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-32324 
                        │      ├ Title           : heap buffer overflow may lead to DoS 
                        │      ├ Description     : OpenPrinting CUPS is an open source printing system. In
                        │      │                    versions 2.4.2 and prior, a heap buffer overflow
                        │      │                   vulnerability would allow a remote attacker to launch a
                        │      │                   denial of service (DoS) attack. A buffer overflow
                        │      │                   vulnerability in the function `format_log_line` could allow
                        │      │                   remote attackers to cause a DoS on the affected system.
                        │      │                   Exploitation of the vulnerability can be triggered when the
                        │      │                   configuration file `cupsd.conf` sets the value of `loglevel
                        │      │                   `to `DEBUG`. No known patches or workarounds exist at time
                        │      │                   of publication. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-787 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-32324 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-32324 
                        │      │                  ├ [2]: https://github.com/OpenPrinting/cups/security/adv
                        │      │                  │      isories/GHSA-cxc6-w2g7-69p7 
                        │      │                  ├ [3]: https://lists.debian.org/debian-lts-announce/2023
                        │      │                  │      /06/msg00001.html 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-32324 
                        │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-6128-1 
                        │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-6128-2 
                        │      │                  ├ [7]: https://www.cve.org/CVERecord?id=CVE-2023-32324 
                        │      │                  ╰ [8]: https://www.openwall.com/lists/oss-security/2023/
                        │      │                         06/01/1 
                        │      ├ PublishedDate   : 2023-06-01T17:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-08T14:32:00Z 
                        ├ [11] ╭ VulnerabilityID : CVE-2023-34241 
                        │      ├ PkgID           : cups-libs@2.3.3op2-16.el9.x86_64 
                        │      ├ PkgName         : cups-libs 
                        │      ├ InstalledVersion: 1:2.3.3op2-16.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-34241 
                        │      ├ Title           : use-after-free in cupsdAcceptClient() in scheduler/client.c 
                        │      ├ Description     : OpenPrinting CUPS is a standards-based, open source
                        │      │                   printing system for Linux and other Unix-like operating
                        │      │                   systems. Starting in version 2.0.0 and prior to version
                        │      │                   2.4.6, CUPS logs data of free memory to the logging service
                        │      │                   AFTER the connection has been closed, when it should have
                        │      │                   logged the data right before. This is a use-after-free bug
                        │      │                   that impacts the entire cupsd process.
                        │      │                   
                        │      │                   The exact cause of this issue is the function
                        │      │                   `httpClose(con->http)` being called in `scheduler/client.c`.
                        │      │                    The problem is that httpClose always, provided its argument
                        │      │                    is not null, frees the pointer at the end of the call, only
                        │      │                    for cupsdLogClient to pass the pointer to httpGetHostname.
                        │      │                   This issue happens in function `cupsdAcceptClient` if
                        │      │                   LogLevel is warn or higher and in two scenarios: there is a
                        │      │                   double-lookup for the IP Address (HostNameLookups Double is
                        │      │                   set in `cupsd.conf`) which fails to resolve, or if CUPS is
                        │      │                   compiled with TCP wrappers and the connection is refused by
                        │      │                   rules from `/etc/hosts.allow` and `/etc/hosts.deny`.
                        │      │                   
                        │      │                   Version 2.4.6 has a patch for this issue. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-416 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.1 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:H 
                        │      │                           ╰ V3Score : 7.1 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       06/23/10 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       06/26/1 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2023-34241 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-34241 
                        │      │                  ├ [4] : https://github.com/OpenPrinting/cups/commit/9809
                        │      │                  │       947a959e18409dcf562a3466ef246cb90cb2 
                        │      │                  ├ [5] : https://github.com/OpenPrinting/cups/releases/ta
                        │      │                  │       g/v2.4.6 
                        │      │                  ├ [6] : https://github.com/OpenPrinting/cups/security/ad
                        │      │                  │       visories/GHSA-qjgh-5hcq-5f25 
                        │      │                  ├ [7] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/06/msg00038.html 
                        │      │                  ├ [8] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/7I7DWG
                        │      │                  │       YGEMBNLZF5UQBMF3SONR37YUBN/ 
                        │      │                  ├ [9] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/TBIYKD
                        │      │                  │       S3UG3W4Z7YOHTR2AWFNBRYPNYY/ 
                        │      │                  ├ [10]: https://nvd.nist.gov/vuln/detail/CVE-2023-34241 
                        │      │                  ├ [11]: https://support.apple.com/kb/HT213843 
                        │      │                  ├ [12]: https://support.apple.com/kb/HT213844 
                        │      │                  ├ [13]: https://support.apple.com/kb/HT213845 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6184-1 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6184-2 
                        │      │                  ╰ [16]: https://www.cve.org/CVERecord?id=CVE-2023-34241 
                        │      ├ PublishedDate   : 2023-06-22T23:15:00Z 
                        │      ╰ LastModifiedDate: 2023-07-28T21:15:00Z 
                        ├ [12] ╭ VulnerabilityID : CVE-2021-25317 
                        │      ├ PkgID           : cups-libs@2.3.3op2-16.el9.x86_64 
                        │      ├ PkgName         : cups-libs 
                        │      ├ InstalledVersion: 1:2.3.3op2-16.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
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
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/GWPGZLT3
                        │      │                  │      U776Q5YPPSA6LGFWWBDWBVH3/ 
                        │      │                  ├ [3]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/H74BP746
                        │      │                  │      O5NNVCBUTLLZYAFBPESFVECV/ 
                        │      │                  ├ [4]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/S37IDQGH
                        │      │                  │      TORQ3Z6VRDQIGBYVOI27YG47/ 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2021-25317 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2021-25317 
                        │      ├ PublishedDate   : 2021-05-05T10:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-14T18:49:00Z 
                        ├ [13] ╭ VulnerabilityID : CVE-2023-27536 
                        │      ├ PkgID           : curl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27536 
                        │      ├ Title           : GSS delegation too eager connection re-use 
                        │      ├ Description     : An authentication bypass vulnerability exists libcurl
                        │      │                   <8.0.0 in the connection reuse feature which can reuse
                        │      │                   previously established connections with incorrect user
                        │      │                   permissions due to a failure to check for changes in the
                        │      │                   CURLOPT_GSSAPI_DELEGATION option. This vulnerability affects
                        │      │                    krb5/kerberos/negotiate/GSSAPI transfers and could
                        │      │                   potentially result in unauthorized access to sensitive
                        │      │                   information. The safest option is to not reuse connections
                        │      │                   if the CURLOPT_GSSAPI_DELEGATION option has been
                        │      │                   changed. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-287 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:4523 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-27536 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2179092 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2196786 
                        │      │                  ├ [4] : https://curl.se/docs/CVE-2023-27536.html 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-27536 
                        │      │                  ├ [6] : https://errata.almalinux.org/8/ALSA-2023-4523.html 
                        │      │                  ├ [7] : https://hackerone.com/reports/1895135 
                        │      │                  ├ [8] : https://linux.oracle.com/cve/CVE-2023-27536.html 
                        │      │                  ├ [9] : https://linux.oracle.com/errata/ELSA-2023-4523.html 
                        │      │                  ├ [10]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/04/msg00025.html 
                        │      │                  ├ [11]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/36NBD5
                        │      │                  │       YLJXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2023-27536 
                        │      │                  ├ [13]: https://security.netapp.com/advisory/ntap-202304
                        │      │                  │       20-0010/ 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-5964-2 
                        │      │                  ╰ [16]: https://www.cve.org/CVERecord?id=CVE-2023-27536 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-06T20:34:00Z 
                        ├ [14] ╭ VulnerabilityID : CVE-2023-28321 
                        │      ├ VendorIDs        ─ [0]: RHSA-2023:4354 
                        │      ├ PkgID           : curl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ FixedVersion    : 7.76.1-23.el9_2.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28321 
                        │      ├ Title           : IDN wildcard match may lead to Improper Cerificate
                        │      │                   Validation 
                        │      ├ Description     : An improper certificate validation vulnerability exists
                        │      │                    in curl <v8.1.0 in the way it supports matching of wildcard
                        │      │                    patterns when listed as "Subject Alternative Name" in TLS
                        │      │                   server certificates. curl can be built to use its own name
                        │      │                   matching function for TLS rather than one provided by a TLS
                        │      │                   library. This private wildcard matching function would match
                        │      │                    IDN (International Domain Name) hosts incorrectly and could
                        │      │                    as a result accept patterns that otherwise should mismatch.
                        │      │                    IDN hostnames are converted to puny code before used for
                        │      │                   certificate checks. Puny coded names always start with
                        │      │                   `xn--` and should not be allowed to pattern match, but the
                        │      │                   wildcard check in curl could still check for `x*`, which
                        │      │                   would match even though the IDN name most likely contained
                        │      │                   nothing even resembling an `x`. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-295 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:H/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:H/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2023/Jul/47 
                        │      │                  ├ [1] : http://seclists.org/fulldisclosure/2023/Jul/48 
                        │      │                  ├ [2] : http://seclists.org/fulldisclosure/2023/Jul/52 
                        │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2023:4354 
                        │      │                  ├ [4] : https://access.redhat.com/security/cve/CVE-2023-28321 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2196786 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2196793 
                        │      │                  ├ [7] : https://curl.se/docs/CVE-2023-28321.html 
                        │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-28321 
                        │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2023-4354.html 
                        │      │                  ├ [10]: https://hackerone.com/reports/1950627 
                        │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2023-28321.html 
                        │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2023-4523.html 
                        │      │                  ├ [13]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/F4I75R
                        │      │                  │       DGX5ULSSCBE5BF3P5I5SFO7ULQ/ 
                        │      │                  ├ [14]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/Z2LIWH
                        │      │                  │       WKOVH24COGGBCVOWDXXIUPKOMK/ 
                        │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2023-28321 
                        │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-202306
                        │      │                  │       09-0009/ 
                        │      │                  ├ [17]: https://support.apple.com/kb/HT213843 
                        │      │                  ├ [18]: https://support.apple.com/kb/HT213844 
                        │      │                  ├ [19]: https://support.apple.com/kb/HT213845 
                        │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6237-1 
                        │      │                  ╰ [21]: https://www.cve.org/CVERecord?id=CVE-2023-28321 
                        │      ├ PublishedDate   : 2023-05-26T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-02T16:46:00Z 
                        ├ [15] ╭ VulnerabilityID : CVE-2023-27533 
                        │      ├ PkgID           : curl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27533 
                        │      ├ Title           : TELNET option IAC injection 
                        │      ├ Description     : A vulnerability in input validation exists in curl <8.0
                        │      │                    during communication using the TELNET protocol may allow an
                        │      │                    attacker to pass on maliciously crafted user name and
                        │      │                   "telnet options" during server negotiation. The lack of
                        │      │                   proper input scrubbing allows an attacker to send content or
                        │      │                    perform option negotiation without the application's
                        │      │                   intent. This vulnerability could be exploited if an
                        │      │                   application allows user input, thereby enabling attackers to
                        │      │                    execute arbitrary code on the system. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 8.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 3.1 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-27533 
                        │      │                  ├ [1] : https://curl.se/docs/CVE-2023-27533.html 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-27533 
                        │      │                  ├ [3] : https://hackerone.com/reports/1891474 
                        │      │                  ├ [4] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/04/msg00025.html 
                        │      │                  ├ [5] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/36NBD5
                        │      │                  │       YLJXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-27533 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-202304
                        │      │                  │       20-0011/ 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-5964-2 
                        │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2023-27533 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-21T23:15:00Z 
                        ├ [16] ╭ VulnerabilityID : CVE-2023-27534 
                        │      ├ PkgID           : curl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27534 
                        │      ├ Title           : SFTP path ~ resolving discrepancy 
                        │      ├ Description     : A path traversal vulnerability exists in curl <8.0.0
                        │      │                   SFTP implementation causes the tilde (~) character to be
                        │      │                   wrongly replaced when used as a prefix in the first path
                        │      │                   element, in addition to its intended use as the first
                        │      │                   element to indicate a path relative to the user's home
                        │      │                   directory. Attackers can exploit this flaw to bypass
                        │      │                   filtering or execute arbitrary code by crafting a path like
                        │      │                   /~2/foo while accessing a server with a specific
                        │      │                   user. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-22 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 8.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           L/I:N/A:N 
                        │      │                           ╰ V3Score : 3.7 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-27534 
                        │      │                  ├ [1]: https://curl.se/docs/CVE-2023-27534.html 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-27534 
                        │      │                  ├ [3]: https://hackerone.com/reports/1892351 
                        │      │                  ├ [4]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/36NBD5YL
                        │      │                  │      JXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-27534 
                        │      │                  ├ [6]: https://security.netapp.com/advisory/ntap-2023042
                        │      │                  │      0-0012/ 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-27534 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-20T09:15:00Z 
                        ├ [17] ╭ VulnerabilityID : CVE-2023-27538 
                        │      ├ PkgID           : curl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27538 
                        │      ├ Title           : SSH connection too eager reuse still 
                        │      ├ Description     : An authentication bypass vulnerability exists in
                        │      │                   libcurl prior to v8.0.0 where it reuses a previously
                        │      │                   established SSH connection despite the fact that an SSH
                        │      │                   option was modified, which should have prevented reuse.
                        │      │                   libcurl maintains a pool of previously used connections to
                        │      │                   reuse them for subsequent transfers if the configurations
                        │      │                   match. However, two SSH settings were omitted from the
                        │      │                   configuration check, allowing them to match easily,
                        │      │                   potentially leading to the reuse of an inappropriate
                        │      │                   connection. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-287 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-27538 
                        │      │                  ├ [1]: https://curl.se/docs/CVE-2023-27538.html 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-27538 
                        │      │                  ├ [3]: https://hackerone.com/reports/1898475 
                        │      │                  ├ [4]: https://lists.debian.org/debian-lts-announce/2023
                        │      │                  │      /04/msg00025.html 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/36NBD5YL
                        │      │                  │      JXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-27538 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-2023042
                        │      │                  │      0-0010/ 
                        │      │                  ├ [8]: https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-27538 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-21T23:15:00Z 
                        ├ [18] ╭ VulnerabilityID : CVE-2023-28322 
                        │      ├ VendorIDs        ─ [0]: RHSA-2023:4354 
                        │      ├ PkgID           : curl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ FixedVersion    : 7.76.1-23.el9_2.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28322 
                        │      ├ Title           : more POST-after-PUT confusion 
                        │      ├ Description     : An information disclosure vulnerability exists in curl
                        │      │                   <v8.1.0 when doing HTTP(S) transfers, libcurl might
                        │      │                   erroneously use the read callback (`CURLOPT_READFUNCTION`)
                        │      │                   to ask for data to send, even when the `CURLOPT_POSTFIELDS`
                        │      │                   option has been set, if the same handle previously wasused
                        │      │                   to issue a `PUT` request which used that callback. This flaw
                        │      │                    may surprise the application and cause it to misbehave and
                        │      │                   either send off the wrong data or use memory after free or
                        │      │                   similar in the second transfer. The problem exists in the
                        │      │                   logic for a reused handle when it is (expected to be)
                        │      │                   changed from a PUT to a POST. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           L/I:N/A:N 
                        │      │                  │        ╰ V3Score : 3.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           L/I:N/A:N 
                        │      │                           ╰ V3Score : 3.7 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2023/Jul/47 
                        │      │                  ├ [1] : http://seclists.org/fulldisclosure/2023/Jul/48 
                        │      │                  ├ [2] : http://seclists.org/fulldisclosure/2023/Jul/52 
                        │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2023:4354 
                        │      │                  ├ [4] : https://access.redhat.com/security/cve/CVE-2023-28322 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2196786 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2196793 
                        │      │                  ├ [7] : https://curl.se/docs/CVE-2023-28322.html 
                        │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-28322 
                        │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2023-4354.html 
                        │      │                  ├ [10]: https://hackerone.com/reports/1954658 
                        │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2023-28322.html 
                        │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2023-4354.html 
                        │      │                  ├ [13]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/F4I75R
                        │      │                  │       DGX5ULSSCBE5BF3P5I5SFO7ULQ/ 
                        │      │                  ├ [14]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/Z2LIWH
                        │      │                  │       WKOVH24COGGBCVOWDXXIUPKOMK/ 
                        │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2023-28322 
                        │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-202306
                        │      │                  │       09-0009/ 
                        │      │                  ├ [17]: https://support.apple.com/kb/HT213843 
                        │      │                  ├ [18]: https://support.apple.com/kb/HT213844 
                        │      │                  ├ [19]: https://support.apple.com/kb/HT213845 
                        │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6237-1 
                        │      │                  ╰ [21]: https://www.cve.org/CVERecord?id=CVE-2023-28322 
                        │      ├ PublishedDate   : 2023-05-26T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-02T16:46:00Z 
                        ├ [19] ╭ VulnerabilityID : CVE-2023-34969 
                        │      ├ VendorIDs        ─ [0]: RHSA-2023:4569 
                        │      ├ PkgID           : dbus-libs@1.12.20-7.el9_1.x86_64 
                        │      ├ PkgName         : dbus-libs 
                        │      ├ InstalledVersion: 1:1.12.20-7.el9_1 
                        │      ├ FixedVersion    : 1:1.12.20-7.el9_2.1 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-34969 
                        │      ├ Title           : assertion failure when a monitor is active and a
                        │      │                   message from the driver cannot be delivered 
                        │      ├ Description     : D-Bus before 1.15.6 sometimes allows unprivileged users
                        │      │                    to crash dbus-daemon. If a privileged user with control
                        │      │                   over the dbus-daemon is using the
                        │      │                   org.freedesktop.DBus.Monitoring interface to monitor message
                        │      │                    bus traffic, then an unprivileged user with the ability to
                        │      │                   connect to the same dbus-daemon can cause a dbus-daemon
                        │      │                   crash under some circumstances via an unreplyable message.
                        │      │                   When done on the well-known system bus, this is a
                        │      │                   denial-of-service vulnerability. The fixed versions are
                        │      │                   1.12.28, 1.14.8, and 1.15.6. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-400 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:4569 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-34969 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2213166 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-34969 
                        │      │                  ├ [4] : https://errata.almalinux.org/9/ALSA-2023-4569.html 
                        │      │                  ├ [5] : https://gitlab.freedesktop.org/dbus/dbus/-/issues/457 
                        │      │                  ├ [6] : https://linux.oracle.com/cve/CVE-2023-34969.html 
                        │      │                  ├ [7] : https://linux.oracle.com/errata/ELSA-2023-4569.html 
                        │      │                  ├ [8] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/BZYCDR
                        │      │                  │       MD7B4XO4HF6C6YTLH4YUD7TANP/ 
                        │      │                  ├ [9] : https://nvd.nist.gov/vuln/detail/CVE-2023-34969 
                        │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2023-34969 
                        │      ├ PublishedDate   : 2023-06-08T03:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-24T03:15:00Z 
                        ├ [20] ╭ VulnerabilityID : CVE-2023-4156 
                        │      ├ PkgID           : gawk@5.1.0-6.el9.x86_64 
                        │      ├ PkgName         : gawk 
                        │      ├ InstalledVersion: 5.1.0-6.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-4156 
                        │      ├ Title           : heap out of bound read in builtin.c 
                        │      ├ Description     : A heap out-of-bounds read flaw was found in builtin.c
                        │      │                   in the gawk package. This issue may lead to a crash and
                        │      │                   could be used to read sensitive information. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 3.3 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-4156 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2023-4156 
                        │                         ├ [2]: https://git.savannah.gnu.org/gitweb/?p=gawk.git;a
                        │                         │      =commitdiff;h=e709eb829448ce040087a3fc5481db6bfcaae212
                        │                         │       (gawk-5.2.0) 
                        │                         ├ [3]: https://mail.gnu.org/archive/html/bug-gawk/2022-0
                        │                         │      8/msg00000.html 
                        │                         ├ [4]: https://mail.gnu.org/archive/html/bug-gawk/2022-0
                        │                         │      8/msg00023.html 
                        │                         ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-4156 
                        │                         ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-4156 
                        ├ [21] ╭ VulnerabilityID : CVE-2023-29499 
                        │      ├ PkgID           : glib2@2.68.4-6.el9.x86_64 
                        │      ├ PkgName         : glib2 
                        │      ├ InstalledVersion: 2.68.4-6.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-29499 
                        │      ├ Title           : GVariant offset table entry size is not checked in
                        │      │                   is_normal() 
                        │      ├ Description     : A flaw was found in GLib. GVariant deserialization
                        │      │                   fails to validate that the input conforms to the expected
                        │      │                   format, leading to denial of service. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-29499 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2023-29499 
                        │                         ├ [2]: https://gitlab.gnome.org/GNOME/glib/-/issues/2794 
                        │                         ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-29499 
                        │                         ├ [4]: https://ubuntu.com/security/notices/USN-6165-1 
                        │                         ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-29499 
                        ├ [22] ╭ VulnerabilityID : CVE-2023-32611 
                        │      ├ PkgID           : glib2@2.68.4-6.el9.x86_64 
                        │      ├ PkgName         : glib2 
                        │      ├ InstalledVersion: 2.68.4-6.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-32611 
                        │      ├ Title           : g_variant_byteswap() can take a long time with some
                        │      │                   non-normal inputs 
                        │      ├ Description     : A flaw was found in GLib. GVariant deserialization is
                        │      │                   vulnerable to a slowdown issue where a crafted GVariant can
                        │      │                   cause excessive processing, leading to denial of
                        │      │                   service. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-32611 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2023-32611 
                        │                         ├ [2]: https://gitlab.gnome.org/GNOME/glib/-/issues/2797 
                        │                         ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-32611 
                        │                         ├ [4]: https://ubuntu.com/security/notices/USN-6165-1 
                        │                         ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-32611 
                        ├ [23] ╭ VulnerabilityID : CVE-2023-32636 
                        │      ├ PkgID           : glib2@2.68.4-6.el9.x86_64 
                        │      ├ PkgName         : glib2 
                        │      ├ InstalledVersion: 2.68.4-6.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-32636 
                        │      ├ Title           : Timeout in fuzz_variant_text 
                        │      ├ Description     : No description is available for this CVE. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 4.7 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-32636 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2023-32636 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-32636 
                        │                         ├ [3]: https://ubuntu.com/security/notices/USN-6165-1 
                        │                         ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2023-32636 
                        ├ [24] ╭ VulnerabilityID : CVE-2023-32665 
                        │      ├ PkgID           : glib2@2.68.4-6.el9.x86_64 
                        │      ├ PkgName         : glib2 
                        │      ├ InstalledVersion: 2.68.4-6.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-32665 
                        │      ├ Title           : GVariant deserialisation does not match spec for
                        │      │                   non-normal data 
                        │      ├ Description     : A flaw was found in GLib. GVariant deserialization is
                        │      │                   vulnerable to an exponential blowup issue where a crafted
                        │      │                   GVariant can cause excessive processing, leading to denial
                        │      │                   of service. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-32665 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │                         │      E-2023-32665 
                        │                         ├ [2]: https://gitlab.gnome.org/GNOME/glib/-/issues/2121 
                        │                         ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-32665 
                        │                         ├ [4]: https://ubuntu.com/security/notices/USN-6165-1 
                        │                         ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-32665 
                        ├ [25] ╭ VulnerabilityID : CVE-2021-43618 
                        │      ├ PkgID           : gmp@6.2.0-10.el9.x86_64 
                        │      ├ PkgName         : gmp 
                        │      ├ InstalledVersion: 1:6.2.0-10.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-43618 
                        │      ├ Title           : Integer overflow and resultant buffer overflow via
                        │      │                   crafted input 
                        │      ├ Description     : GNU Multiple Precision Arithmetic Library (GMP) through
                        │      │                    6.2.1 has an mpz/inp_raw.c integer overflow and resultant
                        │      │                   buffer overflow via crafted input, leading to a segmentation
                        │      │                    fault on 32-bit platforms. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-190 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ├ V2Score : 5 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2022/Oct/8 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2022/
                        │      │                  │       10/13/3 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2021-43618 
                        │      │                  ├ [3] : https://bugs.debian.org/994405 
                        │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2021-43618 
                        │      │                  ├ [5] : https://gmplib.org/list-archives/gmp-bugs/2021-S
                        │      │                  │       eptember/005077.html 
                        │      │                  ├ [6] : https://gmplib.org/repo/gmp-6.2/rev/561a9c25298e 
                        │      │                  ├ [7] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/12/msg00001.html 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2021-43618 
                        │      │                  ├ [9] : https://security.netapp.com/advisory/ntap-202211
                        │      │                  │       11-0001/ 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-5672-1 
                        │      │                  ├ [11]: https://ubuntu.com/security/notices/USN-5672-2 
                        │      │                  ╰ [12]: https://www.cve.org/CVERecord?id=CVE-2021-43618 
                        │      ├ PublishedDate   : 2021-11-15T04:15:00Z 
                        │      ╰ LastModifiedDate: 2022-12-08T22:15:00Z 
                        ├ [26] ╭ VulnerabilityID : CVE-2022-3219 
                        │      ├ PkgID           : gnupg2@2.3.3-2.el9_0.x86_64 
                        │      ├ PkgName         : gnupg2 
                        │      ├ InstalledVersion: 2.3.3-2.el9_0 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-3219 
                        │      ├ Title           : denial of service issue (resource consumption) using
                        │      │                   compressed packets 
                        │      ├ Description     : GnuPG can be made to spin on a relatively small input
                        │      │                   by (for example) crafting a public key with thousands of
                        │      │                   signatures attached, compressed down to just a few
                        │      │                   KB. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-787 
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
                        │      ├ PublishedDate   : 2023-02-23T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-26T16:31:00Z 
                        ├ [27] ╭ VulnerabilityID : CVE-2023-25193 
                        │      ├ PkgID           : harfbuzz@2.7.4-8.el9.x86_64 
                        │      ├ PkgName         : harfbuzz 
                        │      ├ InstalledVersion: 2.7.4-8.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-25193 
                        │      ├ Title           : allows attackers to trigger O(n^2) growth via
                        │      │                   consecutive marks 
                        │      ├ Description     : hb-ot-layout-gsubgpos.hh in HarfBuzz through 6.0.0
                        │      │                   allows attackers to trigger O(n^2) growth via consecutive
                        │      │                   marks during the process of looking back for base glyphs
                        │      │                   when attaching marks. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-770 
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
                        │      │                  │       877925ddbf34f74a1229f3ca1716bb6170dc
                        │      │                  │       (reverted) 
                        │      │                  ├ [15]: https://linux.oracle.com/cve/CVE-2023-25193.html 
                        │      │                  ├ [16]: https://linux.oracle.com/errata/ELSA-2023-4233.html 
                        │      │                  ├ [17]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/KWCHWS
                        │      │                  │       ICWVZSAXP2YAXM65JC2GR53547/ 
                        │      │                  ├ [18]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/YZ5M2G
                        │      │                  │       SAIHFPLHYJXUPQ2QDJCLWXUGO3/ 
                        │      │                  ├ [19]: https://nvd.nist.gov/vuln/detail/CVE-2023-25193 
                        │      │                  ├ [20]: https://security.netapp.com/advisory/ntap-202307
                        │      │                  │       25-0006/ 
                        │      │                  ├ [21]: https://ubuntu.com/security/notices/USN-6263-1 
                        │      │                  ├ [22]: https://ubuntu.com/security/notices/USN-6272-1 
                        │      │                  ╰ [23]: https://www.cve.org/CVERecord?id=CVE-2023-25193 
                        │      ├ PublishedDate   : 2023-02-04T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-07-25T15:15:00Z 
                        ├ [28] ╭ VulnerabilityID : CVE-2023-22049 
                        │      ├ VendorIDs        ─ [0]: RHSA-2023:4178 
                        │      ├ PkgID           : java-1.8.0-openjdk-headless@1.8.0.372.b07-2.el9.x86_64 
                        │      ├ PkgName         : java-1.8.0-openjdk-headless 
                        │      ├ InstalledVersion: 1:1.8.0.372.b07-2.el9 
                        │      ├ FixedVersion    : 1:1.8.0.382.b05-2.el9 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-22049 
                        │      ├ Title           : improper handling of slash characters in URI-to-path
                        │      │                   conversion (8305312) 
                        │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM
                        │      │                   Enterprise Edition, Oracle GraalVM for JDK product of Oracle
                        │      │                    Java SE (component: Libraries).  Supported versions that
                        │      │                   are affected are Oracle Java SE: 8u371, 8u371-perf, 11.0.19,
                        │      │                    17.0.7, 20.0.1; Oracle GraalVM Enterprise Edition: 20.3.10,
                        │      │                    21.3.6, 22.3.2; Oracle GraalVM for JDK: 17.0.7 and  20.0.1.
                        │      │                    Difficult to exploit vulnerability allows unauthenticated
                        │      │                   attacker with network access via multiple protocols to
                        │      │                   compromise Oracle Java SE, Oracle GraalVM Enterprise
                        │      │                   Edition, Oracle GraalVM for JDK.  Successful attacks of this
                        │      │                    vulnerability can result in  unauthorized update, insert or
                        │      │                    delete access to some of Oracle Java SE, Oracle GraalVM
                        │      │                   Enterprise Edition, Oracle GraalVM for JDK accessible data.
                        │      │                   Note: This vulnerability can be exploited by using APIs in
                        │      │                   the specified Component, e.g., through a web service which
                        │      │                   supplies data to the APIs. This vulnerability also applies
                        │      │                   to Java deployments, typically in clients running sandboxed
                        │      │                   Java Web Start applications or sandboxed Java applets, that
                        │      │                   load and run untrusted code (e.g., code that comes from the
                        │      │                   internet) and rely on the Java sandbox for security. CVSS
                        │      │                   3.1 Base Score 3.7 (Integrity impacts).  CVSS Vector:
                        │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 3.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 3.7 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:4178 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-22049 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2221645 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2221647 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2219727 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2221645 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2221647 
                        │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-22045 
                        │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-22049 
                        │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2023-4178.html 
                        │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2023:4176 
                        │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2023-22049.html 
                        │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2023-4233.html 
                        │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2023-22049 
                        │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202307
                        │      │                  │       25-0006/ 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6263-1 
                        │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6272-1 
                        │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2023-22049 
                        │      │                  ├ [18]: https://www.debian.org/security/2023/dsa-5458 
                        │      │                  ├ [19]: https://www.debian.org/security/2023/dsa-5478 
                        │      │                  ╰ [20]: https://www.oracle.com/security-alerts/cpujul202
                        │      │                          3.html 
                        │      ├ PublishedDate   : 2023-07-18T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-17T19:15:00Z 
                        ├ [29] ╭ VulnerabilityID : CVE-2022-3857 
                        │      ├ PkgID           : java-1.8.0-openjdk-headless@1.8.0.372.b07-2.el9.x86_64 
                        │      ├ PkgName         : java-1.8.0-openjdk-headless 
                        │      ├ InstalledVersion: 1:1.8.0.372.b07-2.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-3857 
                        │      ├ Title           : Null pointer dereference leads to segmentation fault 
                        │      ├ Description     : A flaw was found in libpng 1.6.38. A crafted PNG image
                        │      │                   can lead to a segmentation fault and denial of service in
                        │      │                   png_setup_paeth_row() function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-476 
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
                        │      ├ PublishedDate   : 2023-03-06T23:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-06T13:15:00Z 
                        ├ [30] ╭ VulnerabilityID : CVE-2023-22045 
                        │      ├ VendorIDs        ─ [0]: RHSA-2023:4178 
                        │      ├ PkgID           : java-1.8.0-openjdk-headless@1.8.0.372.b07-2.el9.x86_64 
                        │      ├ PkgName         : java-1.8.0-openjdk-headless 
                        │      ├ InstalledVersion: 1:1.8.0.372.b07-2.el9 
                        │      ├ FixedVersion    : 1:1.8.0.382.b05-2.el9 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-22045 
                        │      ├ Title           : array indexing integer overflow issue (8304468) 
                        │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM
                        │      │                   Enterprise Edition, Oracle GraalVM for JDK product of Oracle
                        │      │                    Java SE (component: Hotspot).  Supported versions that are
                        │      │                   affected are Oracle Java SE: 8u371, 8u371-perf, 11.0.19,
                        │      │                   17.0.7, 20.0.1; Oracle GraalVM Enterprise Edition: 20.3.10,
                        │      │                   21.3.6, 22.3.2; Oracle GraalVM for JDK: 17.0.7 and  20.0.1.
                        │      │                   Difficult to exploit vulnerability allows unauthenticated
                        │      │                   attacker with network access via multiple protocols to
                        │      │                   compromise Oracle Java SE, Oracle GraalVM Enterprise
                        │      │                   Edition, Oracle GraalVM for JDK.  Successful attacks of this
                        │      │                    vulnerability can result in  unauthorized read access to a
                        │      │                   subset of Oracle Java SE, Oracle GraalVM Enterprise Edition,
                        │      │                    Oracle GraalVM for JDK accessible data. Note: This
                        │      │                   vulnerability can be exploited by using APIs in the
                        │      │                   specified Component, e.g., through a web service which
                        │      │                   supplies data to the APIs. This vulnerability also applies
                        │      │                   to Java deployments, typically in clients running sandboxed
                        │      │                   Java Web Start applications or sandboxed Java applets, that
                        │      │                   load and run untrusted code (e.g., code that comes from the
                        │      │                   internet) and rely on the Java sandbox for security. CVSS
                        │      │                   3.1 Base Score 3.7 (Confidentiality impacts).  CVSS Vector:
                        │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N). 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           L/I:N/A:N 
                        │      │                  │        ╰ V3Score : 3.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           L/I:N/A:N 
                        │      │                           ╰ V3Score : 3.7 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:4178 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-22045 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2221645 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2221647 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2219727 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2221645 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2221647 
                        │      │                  ├ [7] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-22045 
                        │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-22049 
                        │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2023-4178.html 
                        │      │                  ├ [10]: https://errata.rockylinux.org/RLSA-2023:4176 
                        │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2023-22045.html 
                        │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2023-4233.html 
                        │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2023-22045 
                        │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202307
                        │      │                  │       25-0006/ 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6263-1 
                        │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6272-1 
                        │      │                  ├ [17]: https://www.cve.org/CVERecord?id=CVE-2023-22045 
                        │      │                  ├ [18]: https://www.debian.org/security/2023/dsa-5458 
                        │      │                  ├ [19]: https://www.debian.org/security/2023/dsa-5478 
                        │      │                  ╰ [20]: https://www.oracle.com/security-alerts/cpujul202
                        │      │                          3.html 
                        │      ├ PublishedDate   : 2023-07-18T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-17T19:15:00Z 
                        ├ [31] ╭ VulnerabilityID : CVE-2023-36054 
                        │      ├ PkgID           : krb5-libs@1.20.1-9.el9_2.x86_64 
                        │      ├ PkgName         : krb5-libs 
                        │      ├ InstalledVersion: 1.20.1-9.el9_2 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-36054 
                        │      ├ Title           : Denial of service through freeing uninitialized pointer 
                        │      ├ Description     : lib/kadm5/kadm_rpc_xdr.c in MIT Kerberos 5 (aka krb5)
                        │      │                   before 1.20.2 and 1.21.x before 1.21.1 frees an
                        │      │                   uninitialized pointer. A remote authenticated user can
                        │      │                   trigger a kadmind crash. This occurs because
                        │      │                   _xdr_kadm5_principal_ent_rec does not validate the
                        │      │                   relationship between n_key_data and the key_data array
                        │      │                   count. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-824 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:A/AC:L/PR:L/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.7 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-36054 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-36054 
                        │      │                  ├ [2]: https://github.com/krb5/krb5/commit/ef08b09c94595
                        │      │                  │      51aabbe7924fb176f1583053cdd 
                        │      │                  ├ [3]: https://github.com/krb5/krb5/compare/krb5-1.20.1-
                        │      │                  │      final...krb5-1.20.2-final 
                        │      │                  ├ [4]: https://github.com/krb5/krb5/compare/krb5-1.21-fi
                        │      │                  │      nal...krb5-1.21.1-final 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-36054 
                        │      │                  ├ [6]: https://web.mit.edu/kerberos/www/advisories/ 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2023-36054 
                        │      ├ PublishedDate   : 2023-08-07T19:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-15T17:57:00Z 
                        ├ [32] ╭ VulnerabilityID : CVE-2023-39975 
                        │      ├ PkgID           : krb5-libs@1.20.1-9.el9_2.x86_64 
                        │      ├ PkgName         : krb5-libs 
                        │      ├ InstalledVersion: 1.20.1-9.el9_2 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-39975 
                        │      ├ Title           : double-free in KDC TGS processing 
                        │      ├ Description     : kdc/do_tgs_req.c in MIT Kerberos 5 (aka krb5) 1.21
                        │      │                   before 1.21.2 has a double free that is reachable if an
                        │      │                   authenticated user can trigger an authorization-data
                        │      │                   handling failure. Incorrect data is copied from one ticket
                        │      │                   to another. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-415 
                        │      ├ CVSS             ─ nvd ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I
                        │      │                        │           :H/A:H 
                        │      │                        ╰ V3Score : 8.8 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-39975 
                        │      │                  ├ [1]: https://github.com/krb5/krb5/commit/88a1701b423c1
                        │      │                  │      3991a8064feeb26952d3641d840 
                        │      │                  ├ [2]: https://github.com/krb5/krb5/compare/krb5-1.21.1-
                        │      │                  │      final...krb5-1.21.2-final 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-39975 
                        │      │                  ├ [4]: https://web.mit.edu/kerberos/www/advisories/ 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-39975 
                        │      ├ PublishedDate   : 2023-08-16T15:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-22T23:17:00Z 
                        ├ [33] ╭ VulnerabilityID : CVE-2023-30571 
                        │      ├ PkgID           : libarchive@3.5.3-4.el9.x86_64 
                        │      ├ PkgName         : libarchive 
                        │      ├ InstalledVersion: 3.5.3-4.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-30571 
                        │      ├ Title           : Race condition in multi-threaded use of
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
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:H 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:H 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-30571 
                        │      │                  ├ [1]: https://github.com/libarchive/libarchive/issues/1876 
                        │      │                  ├ [2]: https://groups.google.com/g/libarchive-announce 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-30571 
                        │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2023-30571 
                        │      ├ PublishedDate   : 2023-05-29T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-05T16:40:00Z 
                        ├ [34] ╭ VulnerabilityID : CVE-2023-2603 
                        │      ├ PkgID           : libcap@2.48-8.el9.x86_64 
                        │      ├ PkgName         : libcap 
                        │      ├ InstalledVersion: 2.48-8.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2603 
                        │      ├ Title           : Integer Overflow in _libcap_strdup() 
                        │      ├ Description     : A vulnerability was found in libcap. This issue occurs
                        │      │                   in the _libcap_strdup() function and can lead to an integer
                        │      │                   overflow if the input string is close to 4GiB. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-190 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 7.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                           │           L/I:H/A:H 
                        │      │                           ╰ V3Score : 7.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:4524 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-2603 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2209113 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2209114 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2209113 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-2603 
                        │      │                  ├ [6] : https://errata.almalinux.org/8/ALSA-2023-4524.html 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2023-2603.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2023-4524.html 
                        │      │                  ├ [9] : https://nvd.nist.gov/vuln/detail/CVE-2023-2603 
                        │      │                  ├ [10]: https://sites.google.com/site/fullycapable/relea
                        │      │                  │       se-notes-for-libcap#h.iuvg7sbjg8pe 
                        │      │                  ├ [11]: https://ubuntu.com/security/notices/USN-6166-1 
                        │      │                  ├ [12]: https://ubuntu.com/security/notices/USN-6166-2 
                        │      │                  ├ [13]: https://www.cve.org/CVERecord?id=CVE-2023-2603 
                        │      │                  ├ [14]: https://www.openwall.com/lists/oss-security/2023
                        │      │                  │       /05/15/4 
                        │      │                  ╰ [15]: https://www.x41-dsec.de/static/reports/X41-libca
                        │      │                          p-Code-Review-2023-OSTIF-Final-Report.pdf 
                        │      ├ PublishedDate   : 2023-06-06T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-21T19:02:00Z 
                        ├ [35] ╭ VulnerabilityID : CVE-2023-2602 
                        │      ├ PkgID           : libcap@2.48-8.el9.x86_64 
                        │      ├ PkgName         : libcap 
                        │      ├ InstalledVersion: 2.48-8.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2602 
                        │      ├ Title           : Memory Leak on pthread_create() Error 
                        │      ├ Description     : A vulnerability was found in the pthread_create()
                        │      │                   function in libcap. This issue may allow a malicious actor
                        │      │                   to use cause __real_pthread_create() to return an error,
                        │      │                   which can exhaust the process memory. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-401 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:L 
                        │      │                  │        ╰ V3Score : 3.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:L 
                        │      │                           ╰ V3Score : 3.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:4524 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-2602 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2209113 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2209114 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/show_bug.cgi?id=2209114 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-2602 
                        │      │                  ├ [6] : https://errata.almalinux.org/8/ALSA-2023-4524.html 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2023-2602.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2023-4524.html 
                        │      │                  ├ [9] : https://nvd.nist.gov/vuln/detail/CVE-2023-2602 
                        │      │                  ├ [10]: https://sites.google.com/site/fullycapable/relea
                        │      │                  │       se-notes-for-libcap#h.iuvg7sbjg8pe 
                        │      │                  ├ [11]: https://ubuntu.com/security/notices/USN-6166-1 
                        │      │                  ├ [12]: https://www.cve.org/CVERecord?id=CVE-2023-2602 
                        │      │                  ├ [13]: https://www.openwall.com/lists/oss-security/2023
                        │      │                  │       /05/15/4 
                        │      │                  ╰ [14]: https://www.x41-dsec.de/static/reports/X41-libca
                        │      │                          p-Code-Review-2023-OSTIF-Final-Report.pdf 
                        │      ├ PublishedDate   : 2023-06-06T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-14T18:07:00Z 
                        ├ [36] ╭ VulnerabilityID : CVE-2023-27536 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27536 
                        │      ├ Title           : GSS delegation too eager connection re-use 
                        │      ├ Description     : An authentication bypass vulnerability exists libcurl
                        │      │                   <8.0.0 in the connection reuse feature which can reuse
                        │      │                   previously established connections with incorrect user
                        │      │                   permissions due to a failure to check for changes in the
                        │      │                   CURLOPT_GSSAPI_DELEGATION option. This vulnerability affects
                        │      │                    krb5/kerberos/negotiate/GSSAPI transfers and could
                        │      │                   potentially result in unauthorized access to sensitive
                        │      │                   information. The safest option is to not reuse connections
                        │      │                   if the CURLOPT_GSSAPI_DELEGATION option has been
                        │      │                   changed. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-287 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:4523 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-27536 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2179092 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2196786 
                        │      │                  ├ [4] : https://curl.se/docs/CVE-2023-27536.html 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-27536 
                        │      │                  ├ [6] : https://errata.almalinux.org/8/ALSA-2023-4523.html 
                        │      │                  ├ [7] : https://hackerone.com/reports/1895135 
                        │      │                  ├ [8] : https://linux.oracle.com/cve/CVE-2023-27536.html 
                        │      │                  ├ [9] : https://linux.oracle.com/errata/ELSA-2023-4523.html 
                        │      │                  ├ [10]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/04/msg00025.html 
                        │      │                  ├ [11]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/36NBD5
                        │      │                  │       YLJXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2023-27536 
                        │      │                  ├ [13]: https://security.netapp.com/advisory/ntap-202304
                        │      │                  │       20-0010/ 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-5964-2 
                        │      │                  ╰ [16]: https://www.cve.org/CVERecord?id=CVE-2023-27536 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-06T20:34:00Z 
                        ├ [37] ╭ VulnerabilityID : CVE-2023-28321 
                        │      ├ VendorIDs        ─ [0]: RHSA-2023:4354 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ FixedVersion    : 7.76.1-23.el9_2.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28321 
                        │      ├ Title           : IDN wildcard match may lead to Improper Cerificate
                        │      │                   Validation 
                        │      ├ Description     : An improper certificate validation vulnerability exists
                        │      │                    in curl <v8.1.0 in the way it supports matching of wildcard
                        │      │                    patterns when listed as "Subject Alternative Name" in TLS
                        │      │                   server certificates. curl can be built to use its own name
                        │      │                   matching function for TLS rather than one provided by a TLS
                        │      │                   library. This private wildcard matching function would match
                        │      │                    IDN (International Domain Name) hosts incorrectly and could
                        │      │                    as a result accept patterns that otherwise should mismatch.
                        │      │                    IDN hostnames are converted to puny code before used for
                        │      │                   certificate checks. Puny coded names always start with
                        │      │                   `xn--` and should not be allowed to pattern match, but the
                        │      │                   wildcard check in curl could still check for `x*`, which
                        │      │                   would match even though the IDN name most likely contained
                        │      │                   nothing even resembling an `x`. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-295 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:H/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:H/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2023/Jul/47 
                        │      │                  ├ [1] : http://seclists.org/fulldisclosure/2023/Jul/48 
                        │      │                  ├ [2] : http://seclists.org/fulldisclosure/2023/Jul/52 
                        │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2023:4354 
                        │      │                  ├ [4] : https://access.redhat.com/security/cve/CVE-2023-28321 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2196786 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2196793 
                        │      │                  ├ [7] : https://curl.se/docs/CVE-2023-28321.html 
                        │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-28321 
                        │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2023-4354.html 
                        │      │                  ├ [10]: https://hackerone.com/reports/1950627 
                        │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2023-28321.html 
                        │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2023-4523.html 
                        │      │                  ├ [13]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/F4I75R
                        │      │                  │       DGX5ULSSCBE5BF3P5I5SFO7ULQ/ 
                        │      │                  ├ [14]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/Z2LIWH
                        │      │                  │       WKOVH24COGGBCVOWDXXIUPKOMK/ 
                        │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2023-28321 
                        │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-202306
                        │      │                  │       09-0009/ 
                        │      │                  ├ [17]: https://support.apple.com/kb/HT213843 
                        │      │                  ├ [18]: https://support.apple.com/kb/HT213844 
                        │      │                  ├ [19]: https://support.apple.com/kb/HT213845 
                        │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6237-1 
                        │      │                  ╰ [21]: https://www.cve.org/CVERecord?id=CVE-2023-28321 
                        │      ├ PublishedDate   : 2023-05-26T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-02T16:46:00Z 
                        ├ [38] ╭ VulnerabilityID : CVE-2023-27533 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27533 
                        │      ├ Title           : TELNET option IAC injection 
                        │      ├ Description     : A vulnerability in input validation exists in curl <8.0
                        │      │                    during communication using the TELNET protocol may allow an
                        │      │                    attacker to pass on maliciously crafted user name and
                        │      │                   "telnet options" during server negotiation. The lack of
                        │      │                   proper input scrubbing allows an attacker to send content or
                        │      │                    perform option negotiation without the application's
                        │      │                   intent. This vulnerability could be exploited if an
                        │      │                   application allows user input, thereby enabling attackers to
                        │      │                    execute arbitrary code on the system. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 8.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 3.1 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-27533 
                        │      │                  ├ [1] : https://curl.se/docs/CVE-2023-27533.html 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-27533 
                        │      │                  ├ [3] : https://hackerone.com/reports/1891474 
                        │      │                  ├ [4] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/04/msg00025.html 
                        │      │                  ├ [5] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/36NBD5
                        │      │                  │       YLJXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-27533 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-202304
                        │      │                  │       20-0011/ 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-5964-2 
                        │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2023-27533 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-21T23:15:00Z 
                        ├ [39] ╭ VulnerabilityID : CVE-2023-27534 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27534 
                        │      ├ Title           : SFTP path ~ resolving discrepancy 
                        │      ├ Description     : A path traversal vulnerability exists in curl <8.0.0
                        │      │                   SFTP implementation causes the tilde (~) character to be
                        │      │                   wrongly replaced when used as a prefix in the first path
                        │      │                   element, in addition to its intended use as the first
                        │      │                   element to indicate a path relative to the user's home
                        │      │                   directory. Attackers can exploit this flaw to bypass
                        │      │                   filtering or execute arbitrary code by crafting a path like
                        │      │                   /~2/foo while accessing a server with a specific
                        │      │                   user. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-22 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 8.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           L/I:N/A:N 
                        │      │                           ╰ V3Score : 3.7 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-27534 
                        │      │                  ├ [1]: https://curl.se/docs/CVE-2023-27534.html 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-27534 
                        │      │                  ├ [3]: https://hackerone.com/reports/1892351 
                        │      │                  ├ [4]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/36NBD5YL
                        │      │                  │      JXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-27534 
                        │      │                  ├ [6]: https://security.netapp.com/advisory/ntap-2023042
                        │      │                  │      0-0012/ 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-27534 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-20T09:15:00Z 
                        ├ [40] ╭ VulnerabilityID : CVE-2023-27538 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27538 
                        │      ├ Title           : SSH connection too eager reuse still 
                        │      ├ Description     : An authentication bypass vulnerability exists in
                        │      │                   libcurl prior to v8.0.0 where it reuses a previously
                        │      │                   established SSH connection despite the fact that an SSH
                        │      │                   option was modified, which should have prevented reuse.
                        │      │                   libcurl maintains a pool of previously used connections to
                        │      │                   reuse them for subsequent transfers if the configurations
                        │      │                   match. However, two SSH settings were omitted from the
                        │      │                   configuration check, allowing them to match easily,
                        │      │                   potentially leading to the reuse of an inappropriate
                        │      │                   connection. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-287 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-27538 
                        │      │                  ├ [1]: https://curl.se/docs/CVE-2023-27538.html 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-27538 
                        │      │                  ├ [3]: https://hackerone.com/reports/1898475 
                        │      │                  ├ [4]: https://lists.debian.org/debian-lts-announce/2023
                        │      │                  │      /04/msg00025.html 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/36NBD5YL
                        │      │                  │      JXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-27538 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-2023042
                        │      │                  │      0-0010/ 
                        │      │                  ├ [8]: https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-27538 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-21T23:15:00Z 
                        ├ [41] ╭ VulnerabilityID : CVE-2023-28322 
                        │      ├ VendorIDs        ─ [0]: RHSA-2023:4354 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ FixedVersion    : 7.76.1-23.el9_2.2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28322 
                        │      ├ Title           : more POST-after-PUT confusion 
                        │      ├ Description     : An information disclosure vulnerability exists in curl
                        │      │                   <v8.1.0 when doing HTTP(S) transfers, libcurl might
                        │      │                   erroneously use the read callback (`CURLOPT_READFUNCTION`)
                        │      │                   to ask for data to send, even when the `CURLOPT_POSTFIELDS`
                        │      │                   option has been set, if the same handle previously wasused
                        │      │                   to issue a `PUT` request which used that callback. This flaw
                        │      │                    may surprise the application and cause it to misbehave and
                        │      │                   either send off the wrong data or use memory after free or
                        │      │                   similar in the second transfer. The problem exists in the
                        │      │                   logic for a reused handle when it is (expected to be)
                        │      │                   changed from a PUT to a POST. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                  │        │           L/I:N/A:N 
                        │      │                  │        ╰ V3Score : 3.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           L/I:N/A:N 
                        │      │                           ╰ V3Score : 3.7 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2023/Jul/47 
                        │      │                  ├ [1] : http://seclists.org/fulldisclosure/2023/Jul/48 
                        │      │                  ├ [2] : http://seclists.org/fulldisclosure/2023/Jul/52 
                        │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2023:4354 
                        │      │                  ├ [4] : https://access.redhat.com/security/cve/CVE-2023-28322 
                        │      │                  ├ [5] : https://bugzilla.redhat.com/2196786 
                        │      │                  ├ [6] : https://bugzilla.redhat.com/2196793 
                        │      │                  ├ [7] : https://curl.se/docs/CVE-2023-28322.html 
                        │      │                  ├ [8] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-28322 
                        │      │                  ├ [9] : https://errata.almalinux.org/9/ALSA-2023-4354.html 
                        │      │                  ├ [10]: https://hackerone.com/reports/1954658 
                        │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2023-28322.html 
                        │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2023-4354.html 
                        │      │                  ├ [13]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/F4I75R
                        │      │                  │       DGX5ULSSCBE5BF3P5I5SFO7ULQ/ 
                        │      │                  ├ [14]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/Z2LIWH
                        │      │                  │       WKOVH24COGGBCVOWDXXIUPKOMK/ 
                        │      │                  ├ [15]: https://nvd.nist.gov/vuln/detail/CVE-2023-28322 
                        │      │                  ├ [16]: https://security.netapp.com/advisory/ntap-202306
                        │      │                  │       09-0009/ 
                        │      │                  ├ [17]: https://support.apple.com/kb/HT213843 
                        │      │                  ├ [18]: https://support.apple.com/kb/HT213844 
                        │      │                  ├ [19]: https://support.apple.com/kb/HT213845 
                        │      │                  ├ [20]: https://ubuntu.com/security/notices/USN-6237-1 
                        │      │                  ╰ [21]: https://www.cve.org/CVERecord?id=CVE-2023-28322 
                        │      ├ PublishedDate   : 2023-05-26T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-02T16:46:00Z 
                        ├ [42] ╭ VulnerabilityID : CVE-2023-22652 
                        │      ├ VendorIDs        ─ [0]: RHSA-2023:4347 
                        │      ├ PkgID           : libeconf@0.4.1-2.el9.x86_64 
                        │      ├ PkgName         : libeconf 
                        │      ├ InstalledVersion: 0.4.1-2.el9 
                        │      ├ FixedVersion    : 0.4.1-3.el9_2 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-22652 
                        │      ├ Title           : stack-based buffer overflow in read_file() in
                        │      │                   lib/getfilecontents.c 
                        │      ├ Description     : A Buffer Copy without Checking Size of Input ('Classic
                        │      │                   Buffer Overflow') vulnerability in openSUSE libeconf leads
                        │      │                   to DoS via malformed config files.
                        │      │                   This issue affects libeconf: before 0.5.2.
                        │      │                   
                        │      │                    
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-120 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/errata/RHSA-2023:4347 
                        │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2023-22652 
                        │      │                  ├ [2]: https://bugzilla.redhat.com/2212463 
                        │      │                  ├ [3]: https://bugzilla.suse.com/show_bug.cgi?id=CVE-202
                        │      │                  │      3-22652 
                        │      │                  ├ [4]: https://errata.almalinux.org/9/ALSA-2023-4347.html 
                        │      │                  ├ [5]: https://https://github.com/openSUSE/libeconf/issu
                        │      │                  │      es/177 
                        │      │                  ├ [6]: https://linux.oracle.com/cve/CVE-2023-22652.html 
                        │      │                  ├ [7]: https://linux.oracle.com/errata/ELSA-2023-4347.html 
                        │      │                  ├ [8]: https://nvd.nist.gov/vuln/detail/CVE-2023-22652 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-22652 
                        │      ├ PublishedDate   : 2023-06-01T12:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-08T18:29:00Z 
                        ├ [43] ╭ VulnerabilityID : CVE-2022-27943 
                        │      ├ PkgID           : libgcc@11.3.1-4.3.el9.x86_64 
                        │      ├ PkgName         : libgcc 
                        │      ├ InstalledVersion: 11.3.1-4.3.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-27943 
                        │      ├ Title           : libiberty/rust-demangle.c in GNU GCC 11.2 allows stack
                        │      │                   exhaustion in demangle_const 
                        │      ├ Description     : libiberty/rust-demangle.c in GNU GCC 11.2 allows stack
                        │      │                   consumption in demangle_const, as demonstrated by
                        │      │                   nm-new. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-674 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ├ V2Score : 4.3 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-27943 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2022-27943 
                        │      │                  ├ [2]: https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105039 
                        │      │                  ├ [3]: https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=92
                        │      │                  │      34cdca6ee88badfc00297e72f13dac4e540c79 
                        │      │                  ├ [4]: https://gcc.gnu.org/pipermail/gcc-patches/2022-Ma
                        │      │                  │      rch/592244.html 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/H424YXGW
                        │      │                  │      7OKXS2NCAP35OP6Y4P4AW6VG/ 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2022-27943 
                        │      │                  ├ [7]: https://sourceware.org/bugzilla/show_bug.cgi?id=28995 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2022-27943 
                        │      ├ PublishedDate   : 2022-03-26T13:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-08T14:22:00Z 
                        ├ [44] ╭ VulnerabilityID : CVE-2022-3857 
                        │      ├ PkgID           : libpng@1.6.37-12.el9.x86_64 
                        │      ├ PkgName         : libpng 
                        │      ├ InstalledVersion: 2:1.6.37-12.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-3857 
                        │      ├ Title           : Null pointer dereference leads to segmentation fault 
                        │      ├ Description     : A flaw was found in libpng 1.6.38. A crafted PNG image
                        │      │                   can lead to a segmentation fault and denial of service in
                        │      │                   png_setup_paeth_row() function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-476 
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
                        │      ├ PublishedDate   : 2023-03-06T23:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-06T13:15:00Z 
                        ├ [45] ╭ VulnerabilityID : CVE-2022-27943 
                        │      ├ PkgID           : libstdc++@11.3.1-4.3.el9.x86_64 
                        │      ├ PkgName         : libstdc++ 
                        │      ├ InstalledVersion: 11.3.1-4.3.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-27943 
                        │      ├ Title           : libiberty/rust-demangle.c in GNU GCC 11.2 allows stack
                        │      │                   exhaustion in demangle_const 
                        │      ├ Description     : libiberty/rust-demangle.c in GNU GCC 11.2 allows stack
                        │      │                   consumption in demangle_const, as demonstrated by
                        │      │                   nm-new. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-674 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ├ V2Score : 4.3 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-27943 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2022-27943 
                        │      │                  ├ [2]: https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105039 
                        │      │                  ├ [3]: https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=92
                        │      │                  │      34cdca6ee88badfc00297e72f13dac4e540c79 
                        │      │                  ├ [4]: https://gcc.gnu.org/pipermail/gcc-patches/2022-Ma
                        │      │                  │      rch/592244.html 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/H424YXGW
                        │      │                  │      7OKXS2NCAP35OP6Y4P4AW6VG/ 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2022-27943 
                        │      │                  ├ [7]: https://sourceware.org/bugzilla/show_bug.cgi?id=28995 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2022-27943 
                        │      ├ PublishedDate   : 2022-03-26T13:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-08T14:22:00Z 
                        ├ [46] ╭ VulnerabilityID : CVE-2023-28484 
                        │      ├ VendorIDs        ─ [0]: RHSA-2023:4349 
                        │      ├ PkgID           : libxml2@2.9.13-3.el9_1.x86_64 
                        │      ├ PkgName         : libxml2 
                        │      ├ InstalledVersion: 2.9.13-3.el9_1 
                        │      ├ FixedVersion    : 2.9.13-3.el9_2.1 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28484 
                        │      ├ Title           : NULL dereference in xmlSchemaFixupComplexType 
                        │      ├ Description     : In libxml2 before 2.10.4, parsing of certain invalid
                        │      │                   XSD schemas can lead to a NULL pointer dereference and
                        │      │                   subsequently a segfault. This occurs in
                        │      │                   xmlSchemaFixupComplexType in xmlschemas.c. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-476 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:4349 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-28484 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2185984 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2185994 
                        │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-28484 
                        │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2023-4349.html 
                        │      │                  ├ [6] : https://gitlab.gnome.org/GNOME/libxml2/-/commit/
                        │      │                  │       4c6922f763ad958c48ff66f82823ae21f2e92ee6 
                        │      │                  ├ [7] : https://gitlab.gnome.org/GNOME/libxml2/-/commit/
                        │      │                  │       647e072ea0a2f12687fa05c172f4c4713fdb0c4f 
                        │      │                  ├ [8] : https://gitlab.gnome.org/GNOME/libxml2/-/issues/491 
                        │      │                  ├ [9] : https://gitlab.gnome.org/GNOME/libxml2/-/release
                        │      │                  │       s/v2.10.4 
                        │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2023-28484.html 
                        │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2023-4529.html 
                        │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/04/msg00031.html 
                        │      │                  ├ [13]: https://nvd.nist.gov/vuln/detail/CVE-2023-28484 
                        │      │                  ├ [14]: https://security.netapp.com/advisory/ntap-202306
                        │      │                  │       01-0006/ 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6028-1 
                        │      │                  ├ [16]: https://ubuntu.com/security/notices/USN-6028-2 
                        │      │                  ╰ [17]: https://www.cve.org/CVERecord?id=CVE-2023-28484 
                        │      ├ PublishedDate   : 2023-04-24T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-01T14:15:00Z 
                        ├ [47] ╭ VulnerabilityID : CVE-2023-29469 
                        │      ├ VendorIDs        ─ [0]: RHSA-2023:4349 
                        │      ├ PkgID           : libxml2@2.9.13-3.el9_1.x86_64 
                        │      ├ PkgName         : libxml2 
                        │      ├ InstalledVersion: 2.9.13-3.el9_1 
                        │      ├ FixedVersion    : 2.9.13-3.el9_2.1 
                        │      ├ Status          : fixed 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-29469 
                        │      ├ Title           : Hashing of empty dict strings isn't deterministic 
                        │      ├ Description     : An issue was discovered in libxml2 before 2.10.4. When
                        │      │                   hashing empty dict strings in a crafted XML document,
                        │      │                   xmlDictComputeFastKey in dict.c can produce
                        │      │                   non-deterministic values, leading to various logic and
                        │      │                   memory errors, such as a double free. This behavior occurs
                        │      │                   because there is an attempt to use the first byte of an
                        │      │                   empty string, and any value is possible (not solely the '\0'
                        │      │                    value). 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-415 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2023:4349 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-29469 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/2185984 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2185994 
                        │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-29469 
                        │      │                  ├ [5] : https://errata.almalinux.org/9/ALSA-2023-4349.html 
                        │      │                  ├ [6] : https://gitlab.gnome.org/GNOME/libxml2/-/commit/
                        │      │                  │       09a2dd453007f9c7205274623acdd73747c22d64 
                        │      │                  ├ [7] : https://gitlab.gnome.org/GNOME/libxml2/-/issues/510 
                        │      │                  ├ [8] : https://gitlab.gnome.org/GNOME/libxml2/-/release
                        │      │                  │       s/v2.10.4 
                        │      │                  ├ [9] : https://linux.oracle.com/cve/CVE-2023-29469.html 
                        │      │                  ├ [10]: https://linux.oracle.com/errata/ELSA-2023-4529.html 
                        │      │                  ├ [11]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/04/msg00031.html 
                        │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2023-29469 
                        │      │                  ├ [13]: https://security.netapp.com/advisory/ntap-202306
                        │      │                  │       01-0006/ 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-6028-1 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-6028-2 
                        │      │                  ╰ [16]: https://www.cve.org/CVERecord?id=CVE-2023-29469 
                        │      ├ PublishedDate   : 2023-04-24T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-01T14:15:00Z 
                        ├ [48] ╭ VulnerabilityID : CVE-2022-4899 
                        │      ├ PkgID           : libzstd@1.5.1-2.el9.x86_64 
                        │      ├ PkgName         : libzstd 
                        │      ├ InstalledVersion: 1.5.1-2.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-4899 
                        │      ├ Title           : buffer overrun in util.c 
                        │      ├ Description     : A vulnerability was found in zstd v1.4.10, where an
                        │      │                   attacker can supply empty string as an argument to the
                        │      │                   command line tool to cause buffer overrun. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-400 
                        │      ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ├ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-4899 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2022-4899 
                        │      │                  ├ [2]: https://github.com/advisories/GHSA-5c9c-6x87-f9vm 
                        │      │                  ├ [3]: https://github.com/facebook/zstd/issues/3200 
                        │      │                  ├ [4]: https://github.com/facebook/zstd/pull/3220 
                        │      │                  ├ [5]: https://github.com/pypa/advisory-database/tree/ma
                        │      │                  │      in/vulns/zstd/PYSEC-2023-121.yaml 
                        │      │                  ├ [6]: https://github.com/sergey-dryabzhinsky/python-zst
                        │      │                  │      d/commit/c8a619aebdbd6b838fbfef6e19325a70f631a4c6[
                        │      │                  │      m 
                        │      │                  ├ [7]: https://nvd.nist.gov/vuln/detail/CVE-2022-4899 
                        │      │                  ├ [8]: https://security.netapp.com/advisory/ntap-2023072
                        │      │                  │      5-0005/ 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2022-4899 
                        │      ├ PublishedDate   : 2023-03-31T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-07-25T15:15:00Z 
                        ├ [49] ╭ VulnerabilityID : CVE-2023-29491 
                        │      ├ PkgID           : ncurses-base@6.2-8.20210508.el9.noarch 
                        │      ├ PkgName         : ncurses-base 
                        │      ├ InstalledVersion: 6.2-8.20210508.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-29491 
                        │      ├ Title           : Local users can trigger security-relevant memory
                        │      │                   corruption via malformed data 
                        │      ├ Description     : ncurses before 6.4 20230408, when used by a setuid
                        │      │                   application, allows local users to trigger security-relevant
                        │      │                    memory corruption via malformed data in a terminfo database
                        │      │                    file that is found in $HOME/.terminfo or reached via the
                        │      │                   TERMINFO or TERM environment variable. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-787 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 7.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                           │           H/I:H/A:H 
                        │      │                           ╰ V3Score : 7.8 
                        │      ├ References       ╭ [0] : http://ncurses.scripts.mit.edu/?p=ncurses.git;a=
                        │      │                  │       commit;h=eb51b1ea1f75a0ec17c9c5937cb28df1e8eeec56
                        │      │                  │       [m 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       04/19/10 
                        │      │                  ├ [2] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       04/19/11 
                        │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2023-29491 
                        │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-29491 
                        │      │                  ├ [5] : https://invisible-island.net/ncurses/NEWS.html#i
                        │      │                  │       ndex-t20230408 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-29491 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-202305
                        │      │                  │       17-0009/ 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-6099-1 
                        │      │                  ├ [9] : https://www.cve.org/CVERecord?id=CVE-2023-29491 
                        │      │                  ├ [10]: https://www.openwall.com/lists/oss-security/2023
                        │      │                  │       /04/12/5 
                        │      │                  ╰ [11]: https://www.openwall.com/lists/oss-security/2023
                        │      │                          /04/13/4 
                        │      ├ PublishedDate   : 2023-04-14T01:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-17T20:15:00Z 
                        ├ [50] ╭ VulnerabilityID : CVE-2022-29458 
                        │      ├ PkgID           : ncurses-base@6.2-8.20210508.el9.noarch 
                        │      ├ PkgName         : ncurses-base 
                        │      ├ InstalledVersion: 6.2-8.20210508.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-29458 
                        │      ├ Title           : segfaulting OOB read 
                        │      ├ Description     : ncurses 6.3 before patch 20220416 has an out-of-bounds
                        │      │                   read and segmentation violation in convert_strings in
                        │      │                   tinfo/read_entry.c in the terminfo library. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-125 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:P/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           H/I:N/A:H 
                        │      │                  │        ├ V2Score : 5.8 
                        │      │                  │        ╰ V3Score : 7.1 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           L/I:N/A:H 
                        │      │                           ╰ V3Score : 6.1 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2022/Oct/41 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2022-29458 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2022-29458 
                        │      │                  ├ [3] : https://invisible-island.net/ncurses/NEWS.html#t
                        │      │                  │       20220416 
                        │      │                  ├ [4] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       2/10/msg00037.html 
                        │      │                  ├ [5] : https://lists.gnu.org/archive/html/bug-ncurses/2
                        │      │                  │       022-04/msg00014.html 
                        │      │                  ├ [6] : https://lists.gnu.org/archive/html/bug-ncurses/2
                        │      │                  │       022-04/msg00016.html 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2022-29458 
                        │      │                  ├ [8] : https://support.apple.com/kb/HT213488 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-5477-1 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-6099-1 
                        │      │                  ╰ [11]: https://www.cve.org/CVERecord?id=CVE-2022-29458 
                        │      ├ PublishedDate   : 2022-04-18T21:15:00Z 
                        │      ╰ LastModifiedDate: 2022-11-08T19:46:00Z 
                        ├ [51] ╭ VulnerabilityID : CVE-2023-29491 
                        │      ├ PkgID           : ncurses-libs@6.2-8.20210508.el9.x86_64 
                        │      ├ PkgName         : ncurses-libs 
                        │      ├ InstalledVersion: 6.2-8.20210508.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-29491 
                        │      ├ Title           : Local users can trigger security-relevant memory
                        │      │                   corruption via malformed data 
                        │      ├ Description     : ncurses before 6.4 20230408, when used by a setuid
                        │      │                   application, allows local users to trigger security-relevant
                        │      │                    memory corruption via malformed data in a terminfo database
                        │      │                    file that is found in $HOME/.terminfo or reached via the
                        │      │                   TERMINFO or TERM environment variable. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-787 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 7.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                           │           H/I:H/A:H 
                        │      │                           ╰ V3Score : 7.8 
                        │      ├ References       ╭ [0] : http://ncurses.scripts.mit.edu/?p=ncurses.git;a=
                        │      │                  │       commit;h=eb51b1ea1f75a0ec17c9c5937cb28df1e8eeec56
                        │      │                  │       [m 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       04/19/10 
                        │      │                  ├ [2] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       04/19/11 
                        │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2023-29491 
                        │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-29491 
                        │      │                  ├ [5] : https://invisible-island.net/ncurses/NEWS.html#i
                        │      │                  │       ndex-t20230408 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-29491 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-202305
                        │      │                  │       17-0009/ 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-6099-1 
                        │      │                  ├ [9] : https://www.cve.org/CVERecord?id=CVE-2023-29491 
                        │      │                  ├ [10]: https://www.openwall.com/lists/oss-security/2023
                        │      │                  │       /04/12/5 
                        │      │                  ╰ [11]: https://www.openwall.com/lists/oss-security/2023
                        │      │                          /04/13/4 
                        │      ├ PublishedDate   : 2023-04-14T01:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-17T20:15:00Z 
                        ├ [52] ╭ VulnerabilityID : CVE-2022-29458 
                        │      ├ PkgID           : ncurses-libs@6.2-8.20210508.el9.x86_64 
                        │      ├ PkgName         : ncurses-libs 
                        │      ├ InstalledVersion: 6.2-8.20210508.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-29458 
                        │      ├ Title           : segfaulting OOB read 
                        │      ├ Description     : ncurses 6.3 before patch 20220416 has an out-of-bounds
                        │      │                   read and segmentation violation in convert_strings in
                        │      │                   tinfo/read_entry.c in the terminfo library. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-125 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:P/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           H/I:N/A:H 
                        │      │                  │        ├ V2Score : 5.8 
                        │      │                  │        ╰ V3Score : 7.1 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           L/I:N/A:H 
                        │      │                           ╰ V3Score : 6.1 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2022/Oct/41 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2022-29458 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2022-29458 
                        │      │                  ├ [3] : https://invisible-island.net/ncurses/NEWS.html#t
                        │      │                  │       20220416 
                        │      │                  ├ [4] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       2/10/msg00037.html 
                        │      │                  ├ [5] : https://lists.gnu.org/archive/html/bug-ncurses/2
                        │      │                  │       022-04/msg00014.html 
                        │      │                  ├ [6] : https://lists.gnu.org/archive/html/bug-ncurses/2
                        │      │                  │       022-04/msg00016.html 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2022-29458 
                        │      │                  ├ [8] : https://support.apple.com/kb/HT213488 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-5477-1 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-6099-1 
                        │      │                  ╰ [11]: https://www.cve.org/CVERecord?id=CVE-2022-29458 
                        │      ├ PublishedDate   : 2022-04-18T21:15:00Z 
                        │      ╰ LastModifiedDate: 2022-11-08T19:46:00Z 
                        ├ [53] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nspr@4.34.0-18.el9_1.x86_64 
                        │      ├ PkgName         : nspr 
                        │      ├ InstalledVersion: 4.34.0-18.el9_1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : Information exposure when DH secret are reused across
                        │      │                   multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE
                        │      │                   ciphersuites inherit in the TLS specification. To mitigate
                        │      │                   this vulnerability, Firefox disabled support for DHE
                        │      │                   ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
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
                        │      ├ PublishedDate   : 2023-02-16T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:00Z 
                        ├ [54] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss@3.79.0-18.el9_1.x86_64 
                        │      ├ PkgName         : nss 
                        │      ├ InstalledVersion: 3.79.0-18.el9_1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : Information exposure when DH secret are reused across
                        │      │                   multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE
                        │      │                   ciphersuites inherit in the TLS specification. To mitigate
                        │      │                   this vulnerability, Firefox disabled support for DHE
                        │      │                   ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
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
                        │      ├ PublishedDate   : 2023-02-16T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:00Z 
                        ├ [55] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss-softokn@3.79.0-18.el9_1.x86_64 
                        │      ├ PkgName         : nss-softokn 
                        │      ├ InstalledVersion: 3.79.0-18.el9_1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : Information exposure when DH secret are reused across
                        │      │                   multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE
                        │      │                   ciphersuites inherit in the TLS specification. To mitigate
                        │      │                   this vulnerability, Firefox disabled support for DHE
                        │      │                   ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
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
                        │      ├ PublishedDate   : 2023-02-16T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:00Z 
                        ├ [56] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss-softokn-freebl@3.79.0-18.el9_1.x86_64 
                        │      ├ PkgName         : nss-softokn-freebl 
                        │      ├ InstalledVersion: 3.79.0-18.el9_1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : Information exposure when DH secret are reused across
                        │      │                   multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE
                        │      │                   ciphersuites inherit in the TLS specification. To mitigate
                        │      │                   this vulnerability, Firefox disabled support for DHE
                        │      │                   ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
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
                        │      ├ PublishedDate   : 2023-02-16T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:00Z 
                        ├ [57] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss-sysinit@3.79.0-18.el9_1.x86_64 
                        │      ├ PkgName         : nss-sysinit 
                        │      ├ InstalledVersion: 3.79.0-18.el9_1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : Information exposure when DH secret are reused across
                        │      │                   multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE
                        │      │                   ciphersuites inherit in the TLS specification. To mitigate
                        │      │                   this vulnerability, Firefox disabled support for DHE
                        │      │                   ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
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
                        │      ├ PublishedDate   : 2023-02-16T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:00Z 
                        ├ [58] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss-util@3.79.0-18.el9_1.x86_64 
                        │      ├ PkgName         : nss-util 
                        │      ├ InstalledVersion: 3.79.0-18.el9_1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : Information exposure when DH secret are reused across
                        │      │                   multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE
                        │      │                   ciphersuites inherit in the TLS specification. To mitigate
                        │      │                   this vulnerability, Firefox disabled support for DHE
                        │      │                   ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
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
                        │      ├ PublishedDate   : 2023-02-16T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:00Z 
                        ├ [59] ╭ VulnerabilityID : CVE-2023-2953 
                        │      ├ PkgID           : openldap@2.6.2-3.el9.x86_64 
                        │      ├ PkgName         : openldap 
                        │      ├ InstalledVersion: 2.6.2-3.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2953 
                        │      ├ Title           : null pointer dereference in  ber_memalloc_x  function 
                        │      ├ Description     : A vulnerability was found in openldap. This security
                        │      │                   flaw causes a null pointer dereference in ber_memalloc_x()
                        │      │                   function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-476 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:L/A:H 
                        │      │                           ╰ V3Score : 7.1 
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
                        │      │                  ╰ [12]: https://www.cve.org/CVERecord?id=CVE-2023-2953 
                        │      ├ PublishedDate   : 2023-05-30T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-02T16:46:00Z 
                        ├ [60] ╭ VulnerabilityID : CVE-2023-2953 
                        │      ├ PkgID           : openldap-compat@2.6.2-3.el9.x86_64 
                        │      ├ PkgName         : openldap-compat 
                        │      ├ InstalledVersion: 2.6.2-3.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2953 
                        │      ├ Title           : null pointer dereference in  ber_memalloc_x  function 
                        │      ├ Description     : A vulnerability was found in openldap. This security
                        │      │                   flaw causes a null pointer dereference in ber_memalloc_x()
                        │      │                   function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-476 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:L/A:H 
                        │      │                           ╰ V3Score : 7.1 
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
                        │      │                  ╰ [12]: https://www.cve.org/CVERecord?id=CVE-2023-2953 
                        │      ├ PublishedDate   : 2023-05-30T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-02T16:46:00Z 
                        ├ [61] ╭ VulnerabilityID : CVE-2023-2975 
                        │      ├ PkgID           : openssl@3.0.7-16.el9_2.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-16.el9_2 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2975 
                        │      ├ Title           : AES-SIV cipher implementation contains a bug that
                        │      │                   causes it to ignore empty associated data entries 
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
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2023/0
                        │      │                  │      7/15/1 
                        │      │                  ├ [1]: http://www.openwall.com/lists/oss-security/2023/0
                        │      │                  │      7/19/5 
                        │      │                  ├ [2]: https://access.redhat.com/security/cve/CVE-2023-2975 
                        │      │                  ├ [3]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-2975 
                        │      │                  ├ [4]: https://git.openssl.org/gitweb/?p=openssl.git;a=c
                        │      │                  │      ommitdiff;h=00e2f5eea29994d19293ec4e8c8775ba73678598[
                        │      │                  │      m 
                        │      │                  ├ [5]: https://git.openssl.org/gitweb/?p=openssl.git;a=c
                        │      │                  │      ommitdiff;h=6a83f0c958811f07e0d11dfc6b5a6a98edfd5bdc[
                        │      │                  │      m 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-2975 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-2023072
                        │      │                  │      5-0004/ 
                        │      │                  ├ [8]: https://www.cve.org/CVERecord?id=CVE-2023-2975 
                        │      │                  ╰ [9]: https://www.openssl.org/news/secadv/20230714.txt 
                        │      ├ PublishedDate   : 2023-07-14T12:15:00Z 
                        │      ╰ LastModifiedDate: 2023-07-27T13:02:00Z 
                        ├ [62] ╭ VulnerabilityID : CVE-2023-3446 
                        │      ├ PkgID           : openssl@3.0.7-16.el9_2.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-16.el9_2 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-3446 
                        │      ├ Title           : Excessive time spent checking DH keys and parameters 
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
                        │      │                  ├ [4] : https://access.redhat.com/security/cve/CVE-2023-3446 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-3446 
                        │      │                  ├ [6] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=1fa20cf2f506113c761777127a38bce5068740eb
                        │      │                  │        
                        │      │                  ├ [7] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=8780a896543a654e757db1b9396383f9d8095528
                        │      │                  │        
                        │      │                  ├ [8] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=9a0a4d3c1e7138915563c0df4fe6a3f9377b839c
                        │      │                  │        
                        │      │                  ├ [9] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=fc9867c1e03c22ebf56943be205202e576aabf23
                        │      │                  │        
                        │      │                  ├ [10]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/08/msg00019.html 
                        │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2023-3446 
                        │      │                  ├ [12]: https://security.netapp.com/advisory/ntap-202308
                        │      │                  │       03-0011/ 
                        │      │                  ├ [13]: https://www.cve.org/CVERecord?id=CVE-2023-3446 
                        │      │                  ╰ [14]: https://www.openssl.org/news/secadv/20230719.txt 
                        │      ├ PublishedDate   : 2023-07-19T12:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-16T08:15:00Z 
                        ├ [63] ╭ VulnerabilityID : CVE-2023-3817 
                        │      ├ PkgID           : openssl@3.0.7-16.el9_2.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-16.el9_2 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-3817 
                        │      ├ Title           : Excessive time spent checking DH q parameter value 
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
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:L 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2023/Jul/43 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/31/1 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2023-3817 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-3817 
                        │      │                  ├ [4] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=6a1eb62c29db6cb5eec707f9338aee00f44e26f5
                        │      │                  │        
                        │      │                  ├ [5] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=869ad69aadd985c7b8ca6f4e5dd0eb274c9f3644
                        │      │                  │        
                        │      │                  ├ [6] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=9002fd07327a91f35ba6c1307e71fa6fd4409b7f
                        │      │                  │        
                        │      │                  ├ [7] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=91ddeba0f2269b017dc06c46c993a788974b1aa5
                        │      │                  │        
                        │      │                  ├ [8] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/08/msg00019.html 
                        │      │                  ├ [9] : https://nvd.nist.gov/vuln/detail/CVE-2023-3817 
                        │      │                  ├ [10]: https://security.netapp.com/advisory/ntap-202308
                        │      │                  │       18-0014/ 
                        │      │                  ├ [11]: https://www.cve.org/CVERecord?id=CVE-2023-3817 
                        │      │                  ╰ [12]: https://www.openssl.org/news/secadv/20230731.txt 
                        │      ├ PublishedDate   : 2023-07-31T16:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-18T14:15:00Z 
                        ├ [64] ╭ VulnerabilityID : CVE-2023-2975 
                        │      ├ PkgID           : openssl-libs@3.0.7-16.el9_2.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-16.el9_2 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2975 
                        │      ├ Title           : AES-SIV cipher implementation contains a bug that
                        │      │                   causes it to ignore empty associated data entries 
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
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: http://www.openwall.com/lists/oss-security/2023/0
                        │      │                  │      7/15/1 
                        │      │                  ├ [1]: http://www.openwall.com/lists/oss-security/2023/0
                        │      │                  │      7/19/5 
                        │      │                  ├ [2]: https://access.redhat.com/security/cve/CVE-2023-2975 
                        │      │                  ├ [3]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-2975 
                        │      │                  ├ [4]: https://git.openssl.org/gitweb/?p=openssl.git;a=c
                        │      │                  │      ommitdiff;h=00e2f5eea29994d19293ec4e8c8775ba73678598[
                        │      │                  │      m 
                        │      │                  ├ [5]: https://git.openssl.org/gitweb/?p=openssl.git;a=c
                        │      │                  │      ommitdiff;h=6a83f0c958811f07e0d11dfc6b5a6a98edfd5bdc[
                        │      │                  │      m 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-2975 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-2023072
                        │      │                  │      5-0004/ 
                        │      │                  ├ [8]: https://www.cve.org/CVERecord?id=CVE-2023-2975 
                        │      │                  ╰ [9]: https://www.openssl.org/news/secadv/20230714.txt 
                        │      ├ PublishedDate   : 2023-07-14T12:15:00Z 
                        │      ╰ LastModifiedDate: 2023-07-27T13:02:00Z 
                        ├ [65] ╭ VulnerabilityID : CVE-2023-3446 
                        │      ├ PkgID           : openssl-libs@3.0.7-16.el9_2.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-16.el9_2 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-3446 
                        │      ├ Title           : Excessive time spent checking DH keys and parameters 
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
                        │      │                  ├ [4] : https://access.redhat.com/security/cve/CVE-2023-3446 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-3446 
                        │      │                  ├ [6] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=1fa20cf2f506113c761777127a38bce5068740eb
                        │      │                  │        
                        │      │                  ├ [7] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=8780a896543a654e757db1b9396383f9d8095528
                        │      │                  │        
                        │      │                  ├ [8] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=9a0a4d3c1e7138915563c0df4fe6a3f9377b839c
                        │      │                  │        
                        │      │                  ├ [9] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=fc9867c1e03c22ebf56943be205202e576aabf23
                        │      │                  │        
                        │      │                  ├ [10]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/08/msg00019.html 
                        │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2023-3446 
                        │      │                  ├ [12]: https://security.netapp.com/advisory/ntap-202308
                        │      │                  │       03-0011/ 
                        │      │                  ├ [13]: https://www.cve.org/CVERecord?id=CVE-2023-3446 
                        │      │                  ╰ [14]: https://www.openssl.org/news/secadv/20230719.txt 
                        │      ├ PublishedDate   : 2023-07-19T12:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-16T08:15:00Z 
                        ├ [66] ╭ VulnerabilityID : CVE-2023-3817 
                        │      ├ PkgID           : openssl-libs@3.0.7-16.el9_2.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-16.el9_2 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-3817 
                        │      ├ Title           : Excessive time spent checking DH q parameter value 
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
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:L 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2023/Jul/43 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/
                        │      │                  │       07/31/1 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2023-3817 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2023-3817 
                        │      │                  ├ [4] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=6a1eb62c29db6cb5eec707f9338aee00f44e26f5
                        │      │                  │        
                        │      │                  ├ [5] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=869ad69aadd985c7b8ca6f4e5dd0eb274c9f3644
                        │      │                  │        
                        │      │                  ├ [6] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=9002fd07327a91f35ba6c1307e71fa6fd4409b7f
                        │      │                  │        
                        │      │                  ├ [7] : https://git.openssl.org/gitweb/?p=openssl.git;a=
                        │      │                  │       commitdiff;h=91ddeba0f2269b017dc06c46c993a788974b1aa5
                        │      │                  │        
                        │      │                  ├ [8] : https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       3/08/msg00019.html 
                        │      │                  ├ [9] : https://nvd.nist.gov/vuln/detail/CVE-2023-3817 
                        │      │                  ├ [10]: https://security.netapp.com/advisory/ntap-202308
                        │      │                  │       18-0014/ 
                        │      │                  ├ [11]: https://www.cve.org/CVERecord?id=CVE-2023-3817 
                        │      │                  ╰ [12]: https://www.openssl.org/news/secadv/20230731.txt 
                        │      ├ PublishedDate   : 2023-07-31T16:15:00Z 
                        │      ╰ LastModifiedDate: 2023-08-18T14:15:00Z 
                        ├ [67] ╭ VulnerabilityID : CVE-2007-4559 
                        │      ├ PkgID           : python-unversioned-command@3.9.16-1.el9_2.1.noarch 
                        │      ├ PkgName         : python-unversioned-command 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2007-4559 
                        │      ├ Title           : tarfile module directory traversal 
                        │      ├ Description     : Directory traversal vulnerability in the (1) extract
                        │      │                   and (2) extractall functions in the tarfile module in Python
                        │      │                    allows user-assisted remote attackers to overwrite
                        │      │                   arbitrary files via a .. (dot dot) sequence in filenames in
                        │      │                   a TAR archive, a related issue to CVE-2001-1267. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-22 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:P/I:P/A:P 
                        │      │                  │        ╰ V2Score : 6.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:H/A:N 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: http://mail.python.org/pipermail/python-dev/2007-
                        │      │                  │      August/074290.html 
                        │      │                  ├ [1]: http://mail.python.org/pipermail/python-dev/2007-
                        │      │                  │      August/074292.html 
                        │      │                  ├ [2]: http://secunia.com/advisories/26623 
                        │      │                  ├ [3]: http://www.vupen.com/english/advisories/2007/3022 
                        │      │                  ├ [4]: https://access.redhat.com/security/cve/CVE-2007-4559 
                        │      │                  ├ [5]: https://bugzilla.redhat.com/show_bug.cgi?id=263261 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2007-4559 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2007-4559 
                        │      ├ PublishedDate   : 2007-08-28T01:17:00Z 
                        │      ╰ LastModifiedDate: 2023-08-02T17:28:00Z 
                        ├ [68] ╭ VulnerabilityID : CVE-2021-23336 
                        │      ├ PkgID           : python-unversioned-command@3.9.16-1.el9_2.1.noarch 
                        │      ├ PkgName         : python-unversioned-command 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
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
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:H/Au:N/C:N/I:P/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:L/A:H 
                        │      │                  │        ├ V2Score : 4 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:L/A:H 
                        │      │                           ╰ V3Score : 5.9 
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
                        │      │                  │       a291f358e077cafdb14d174b7a1ce9a9d86d1b332d6367@%3Cuse
                        │      │                  │       rs.airflow.apache.org%3E 
                        │      │                  ├ [10]: https://lists.apache.org/thread.html/rc005f4de9d
                        │      │                  │       9b0ba943ceb8ff5a21a5c6ff8a9df52632476698d99432@%3Cann
                        │      │                  │       ounce.apache.org%3E 
                        │      │                  ├ [11]: https://lists.apache.org/thread.html/rf9fa47ab66
                        │      │                  │       495c78bb4120b0754dd9531ca2ff0430f6685ac9b07772@%3Cdev
                        │      │                  │       .mina.apache.org%3E 
                        │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/02/msg00030.html 
                        │      │                  ├ [13]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/04/msg00005.html 
                        │      │                  ├ [14]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/04/msg00015.html 
                        │      │                  ├ [15]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/3EPYWW
                        │      │                  │       FDV22CJ5AOH5VCE72DOASZZ255/ 
                        │      │                  ├ [16]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/3YKKDL
                        │      │                  │       XL3UEZ3J426C2XTBS63AHE46SM/ 
                        │      │                  ├ [17]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/46N6A5
                        │      │                  │       2EGSXHJYCZWVMBJJIH4NWIV2B5/ 
                        │      │                  ├ [18]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/FONHJI
                        │      │                  │       OZOFD7CD35KZL6SVBUTMBPGZGA/ 
                        │      │                  ├ [19]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/HCQTCS
                        │      │                  │       P6SCVIYNIRUJC5X7YBVUHPLSC4/ 
                        │      │                  ├ [20]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/HZTM7K
                        │      │                  │       LHFCE3LWSEVO2NAFLUHMGYMCRY/ 
                        │      │                  ├ [21]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/IHQDU7
                        │      │                  │       NXA7EWAE4W7VO6MURVJIULEPPR/ 
                        │      │                  ├ [22]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/KJXCMH
                        │      │                  │       LY7H3FIYLE4OKDYUILU2CCRUCZ/ 
                        │      │                  ├ [23]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/LVNH6Z
                        │      │                  │       24IG3E67ZCQGGJ46FZB4XFLQNZ/ 
                        │      │                  ├ [24]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/MNUN5S
                        │      │                  │       OMFL2BBKP6ZAICIIUPQKZDMGYO/ 
                        │      │                  ├ [25]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/MP572O
                        │      │                  │       LHMS7MZO4KUPSCIMSZIA5IZZ62/ 
                        │      │                  ├ [26]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/N6VXJZ
                        │      │                  │       SZ6N64AILJX4CTMACYGQGHHD5C/ 
                        │      │                  ├ [27]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/NJSCSN
                        │      │                  │       722JO2E2AGPWD4NTGVELVRPB4R/ 
                        │      │                  ├ [28]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/NODWHD
                        │      │                  │       IFBQE5RU5PUWUVE47JOT5VCMJ2/ 
                        │      │                  ├ [29]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/OAGSWN
                        │      │                  │       GZJ6HQ5ISA67SNMK3CJRKICET7/ 
                        │      │                  ├ [30]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/RSLQD5
                        │      │                  │       CCM75IZGAMBDGUZEATYU5YSGJ7/ 
                        │      │                  ├ [31]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/SGIY6I
                        │      │                  │       4YS3WOXAK4SXKIEOC2G4VZKIR7/ 
                        │      │                  ├ [32]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/TFTELU
                        │      │                  │       MWZE3KV3JB2H5EE6VFRZFRD5MV/ 
                        │      │                  ├ [33]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/W2LSKB
                        │      │                  │       EFI5SYEY5FM6ICZVZM5WRQUCS4/ 
                        │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2021-23336 
                        │      │                  ├ [35]: https://security.gentoo.org/glsa/202104-04 
                        │      │                  ├ [36]: https://security.netapp.com/advisory/ntap-202103
                        │      │                  │       26-0004/ 
                        │      │                  ├ [37]: https://snyk.io/blog/cache-poisoning-in-popular-
                        │      │                  │       open-source-packages/ 
                        │      │                  ├ [38]: https://snyk.io/vuln/SNYK-UPSTREAM-PYTHONCPYTHON
                        │      │                  │       -1074933 
                        │      │                  ├ [39]: https://ubuntu.com/security/notices/USN-4742-1 
                        │      │                  ├ [40]: https://www.cve.org/CVERecord?id=CVE-2021-23336 
                        │      │                  ├ [41]: https://www.djangoproject.com/weblog/2021/feb/19
                        │      │                  │       /security-releases/ 
                        │      │                  ├ [42]: https://www.oracle.com//security-alerts/cpujul20
                        │      │                  │       21.html 
                        │      │                  ├ [43]: https://www.oracle.com/security-alerts/cpuApr202
                        │      │                  │       1.html 
                        │      │                  ├ [44]: https://www.oracle.com/security-alerts/cpujan202
                        │      │                  │       2.html 
                        │      │                  ╰ [45]: https://www.oracle.com/security-alerts/cpuoct202
                        │      │                          1.html 
                        │      ├ PublishedDate   : 2021-02-15T13:15:00Z 
                        │      ╰ LastModifiedDate: 2022-03-04T19:13:00Z 
                        ├ [69] ╭ VulnerabilityID : CVE-2022-0391 
                        │      ├ PkgID           : python-unversioned-command@3.9.16-1.el9_2.1.noarch 
                        │      ├ PkgName         : python-unversioned-command 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-0391 
                        │      ├ Title           : urllib.parse does not sanitize URLs containing ASCII
                        │      │                   newline and tabs 
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
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:P/A:N 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:H/A:N 
                        │      │                  │        ├ V2Score : 5 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
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
                        │      │                  ├ [9] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/CSD2YB
                        │      │                  │       XP3ZF44E44QMIIAR5VTO35KTRB/ 
                        │      │                  ├ [10]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/UDBDBA
                        │      │                  │       U6HUPZHISBOARTXZ5GKHF2VH5U/ 
                        │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2022-0391 
                        │      │                  ├ [12]: https://security.gentoo.org/glsa/202305-02 
                        │      │                  ├ [13]: https://security.netapp.com/advisory/ntap-202202
                        │      │                  │       25-0009/ 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-5342-1 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-5342-2 
                        │      │                  ├ [16]: https://www.cve.org/CVERecord?id=CVE-2022-0391 
                        │      │                  ╰ [17]: https://www.oracle.com/security-alerts/cpuapr202
                        │      │                          2.html 
                        │      ├ PublishedDate   : 2022-02-09T23:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-03T11:15:00Z 
                        ├ [70] ╭ VulnerabilityID : CVE-2023-27043 
                        │      ├ PkgID           : python-unversioned-command@3.9.16-1.el9_2.1.noarch 
                        │      ├ PkgName         : python-unversioned-command 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27043 
                        │      ├ Title           : Parsing errors in email/_parseaddr.py lead to incorrect
                        │      │                    value in email address part of tuple 
                        │      ├ Description     : The email module of Python through 3.11.3 incorrectly
                        │      │                   parses e-mail addresses that contain a special character.
                        │      │                   The wrong portion of an RFC2822 header is identified as the
                        │      │                   value of the addr-spec. In some applications, an attacker
                        │      │                   can bypass a protection mechanism in which application
                        │      │                   access is granted only after verifying receipt of e-mail to
                        │      │                   a specific domain (e.g., only @company.example.com addresses
                        │      │                    may be used for signup). This occurs in email/_parseaddr.py
                        │      │                    in recent versions of Python. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-20 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: http://python.org 
                        │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2023-27043 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-27043 
                        │      │                  ├ [3]: https://github.com/python/cpython/issues/102988 
                        │      │                  ├ [4]: https://github.com/python/cpython/pull/102990 
                        │      │                  ├ [5]: https://github.com/python/cpython/pull/105127 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-27043 
                        │      │                  ├ [7]: https://python-security.readthedocs.io/vuln/email
                        │      │                  │      -parseaddr-realname.html 
                        │      │                  ├ [8]: https://security.netapp.com/advisory/ntap-2023060
                        │      │                  │      1-0003/ 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-27043 
                        │      ├ PublishedDate   : 2023-04-19T00:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-01T14:15:00Z 
                        ├ [71] ╭ VulnerabilityID : CVE-2023-36632 
                        │      ├ PkgID           : python-unversioned-command@3.9.16-1.el9_2.1.noarch 
                        │      ├ PkgName         : python-unversioned-command 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-36632 
                        │      ├ Title           : maximum recursion depth exceeded while calling a Python
                        │      │                    object 
                        │      ├ Description     : ** DISPUTED ** The legacy email.utils.parseaddr
                        │      │                   function in Python through 3.11.4 allows attackers to
                        │      │                   trigger "RecursionError: maximum recursion depth exceeded
                        │      │                   while calling a Python object" via a crafted argument. This
                        │      │                   argument is plausibly an untrusted value from an
                        │      │                   application's input data that was supposed to contain a name
                        │      │                    and an e-mail address. NOTE: email.utils.parseaddr is
                        │      │                   categorized as a Legacy API in the documentation of the
                        │      │                   Python email package. Applications should instead use the
                        │      │                   email.parser.BytesParser or email.parser.Parser class. NOTE:
                        │      │                    the vendor's perspective is that this is neither a
                        │      │                   vulnerability nor a bug. The email package is intended to
                        │      │                   have size limits and to throw an exception when limits are
                        │      │                   exceeded; they were exceeded by the example demonstration
                        │      │                   code. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-674 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-36632 
                        │      │                  ├ [1]: https://docs.python.org/3/library/email.html 
                        │      │                  ├ [2]: https://docs.python.org/3/library/email.utils.html 
                        │      │                  ├ [3]: https://github.com/Daybreak2019/PoC_python3.9_Vul
                        │      │                  │      /blob/main/RecursionError-email.utils.parseaddr.py
                        │      │                  │      [m 
                        │      │                  ├ [4]: https://github.com/python/cpython/issues/103800 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-36632 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-36632 
                        │      ├ PublishedDate   : 2023-06-25T18:15:00Z 
                        │      ╰ LastModifiedDate: 2023-07-06T16:00:00Z 
                        ├ [72] ╭ VulnerabilityID : CVE-2007-4559 
                        │      ├ PkgID           : python3@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2007-4559 
                        │      ├ Title           : tarfile module directory traversal 
                        │      ├ Description     : Directory traversal vulnerability in the (1) extract
                        │      │                   and (2) extractall functions in the tarfile module in Python
                        │      │                    allows user-assisted remote attackers to overwrite
                        │      │                   arbitrary files via a .. (dot dot) sequence in filenames in
                        │      │                   a TAR archive, a related issue to CVE-2001-1267. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-22 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:P/I:P/A:P 
                        │      │                  │        ╰ V2Score : 6.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:H/A:N 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: http://mail.python.org/pipermail/python-dev/2007-
                        │      │                  │      August/074290.html 
                        │      │                  ├ [1]: http://mail.python.org/pipermail/python-dev/2007-
                        │      │                  │      August/074292.html 
                        │      │                  ├ [2]: http://secunia.com/advisories/26623 
                        │      │                  ├ [3]: http://www.vupen.com/english/advisories/2007/3022 
                        │      │                  ├ [4]: https://access.redhat.com/security/cve/CVE-2007-4559 
                        │      │                  ├ [5]: https://bugzilla.redhat.com/show_bug.cgi?id=263261 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2007-4559 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2007-4559 
                        │      ├ PublishedDate   : 2007-08-28T01:17:00Z 
                        │      ╰ LastModifiedDate: 2023-08-02T17:28:00Z 
                        ├ [73] ╭ VulnerabilityID : CVE-2021-23336 
                        │      ├ PkgID           : python3@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
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
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:H/Au:N/C:N/I:P/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:L/A:H 
                        │      │                  │        ├ V2Score : 4 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:L/A:H 
                        │      │                           ╰ V3Score : 5.9 
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
                        │      │                  │       a291f358e077cafdb14d174b7a1ce9a9d86d1b332d6367@%3Cuse
                        │      │                  │       rs.airflow.apache.org%3E 
                        │      │                  ├ [10]: https://lists.apache.org/thread.html/rc005f4de9d
                        │      │                  │       9b0ba943ceb8ff5a21a5c6ff8a9df52632476698d99432@%3Cann
                        │      │                  │       ounce.apache.org%3E 
                        │      │                  ├ [11]: https://lists.apache.org/thread.html/rf9fa47ab66
                        │      │                  │       495c78bb4120b0754dd9531ca2ff0430f6685ac9b07772@%3Cdev
                        │      │                  │       .mina.apache.org%3E 
                        │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/02/msg00030.html 
                        │      │                  ├ [13]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/04/msg00005.html 
                        │      │                  ├ [14]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/04/msg00015.html 
                        │      │                  ├ [15]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/3EPYWW
                        │      │                  │       FDV22CJ5AOH5VCE72DOASZZ255/ 
                        │      │                  ├ [16]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/3YKKDL
                        │      │                  │       XL3UEZ3J426C2XTBS63AHE46SM/ 
                        │      │                  ├ [17]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/46N6A5
                        │      │                  │       2EGSXHJYCZWVMBJJIH4NWIV2B5/ 
                        │      │                  ├ [18]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/FONHJI
                        │      │                  │       OZOFD7CD35KZL6SVBUTMBPGZGA/ 
                        │      │                  ├ [19]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/HCQTCS
                        │      │                  │       P6SCVIYNIRUJC5X7YBVUHPLSC4/ 
                        │      │                  ├ [20]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/HZTM7K
                        │      │                  │       LHFCE3LWSEVO2NAFLUHMGYMCRY/ 
                        │      │                  ├ [21]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/IHQDU7
                        │      │                  │       NXA7EWAE4W7VO6MURVJIULEPPR/ 
                        │      │                  ├ [22]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/KJXCMH
                        │      │                  │       LY7H3FIYLE4OKDYUILU2CCRUCZ/ 
                        │      │                  ├ [23]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/LVNH6Z
                        │      │                  │       24IG3E67ZCQGGJ46FZB4XFLQNZ/ 
                        │      │                  ├ [24]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/MNUN5S
                        │      │                  │       OMFL2BBKP6ZAICIIUPQKZDMGYO/ 
                        │      │                  ├ [25]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/MP572O
                        │      │                  │       LHMS7MZO4KUPSCIMSZIA5IZZ62/ 
                        │      │                  ├ [26]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/N6VXJZ
                        │      │                  │       SZ6N64AILJX4CTMACYGQGHHD5C/ 
                        │      │                  ├ [27]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/NJSCSN
                        │      │                  │       722JO2E2AGPWD4NTGVELVRPB4R/ 
                        │      │                  ├ [28]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/NODWHD
                        │      │                  │       IFBQE5RU5PUWUVE47JOT5VCMJ2/ 
                        │      │                  ├ [29]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/OAGSWN
                        │      │                  │       GZJ6HQ5ISA67SNMK3CJRKICET7/ 
                        │      │                  ├ [30]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/RSLQD5
                        │      │                  │       CCM75IZGAMBDGUZEATYU5YSGJ7/ 
                        │      │                  ├ [31]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/SGIY6I
                        │      │                  │       4YS3WOXAK4SXKIEOC2G4VZKIR7/ 
                        │      │                  ├ [32]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/TFTELU
                        │      │                  │       MWZE3KV3JB2H5EE6VFRZFRD5MV/ 
                        │      │                  ├ [33]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/W2LSKB
                        │      │                  │       EFI5SYEY5FM6ICZVZM5WRQUCS4/ 
                        │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2021-23336 
                        │      │                  ├ [35]: https://security.gentoo.org/glsa/202104-04 
                        │      │                  ├ [36]: https://security.netapp.com/advisory/ntap-202103
                        │      │                  │       26-0004/ 
                        │      │                  ├ [37]: https://snyk.io/blog/cache-poisoning-in-popular-
                        │      │                  │       open-source-packages/ 
                        │      │                  ├ [38]: https://snyk.io/vuln/SNYK-UPSTREAM-PYTHONCPYTHON
                        │      │                  │       -1074933 
                        │      │                  ├ [39]: https://ubuntu.com/security/notices/USN-4742-1 
                        │      │                  ├ [40]: https://www.cve.org/CVERecord?id=CVE-2021-23336 
                        │      │                  ├ [41]: https://www.djangoproject.com/weblog/2021/feb/19
                        │      │                  │       /security-releases/ 
                        │      │                  ├ [42]: https://www.oracle.com//security-alerts/cpujul20
                        │      │                  │       21.html 
                        │      │                  ├ [43]: https://www.oracle.com/security-alerts/cpuApr202
                        │      │                  │       1.html 
                        │      │                  ├ [44]: https://www.oracle.com/security-alerts/cpujan202
                        │      │                  │       2.html 
                        │      │                  ╰ [45]: https://www.oracle.com/security-alerts/cpuoct202
                        │      │                          1.html 
                        │      ├ PublishedDate   : 2021-02-15T13:15:00Z 
                        │      ╰ LastModifiedDate: 2022-03-04T19:13:00Z 
                        ├ [74] ╭ VulnerabilityID : CVE-2022-0391 
                        │      ├ PkgID           : python3@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-0391 
                        │      ├ Title           : urllib.parse does not sanitize URLs containing ASCII
                        │      │                   newline and tabs 
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
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:P/A:N 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:H/A:N 
                        │      │                  │        ├ V2Score : 5 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
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
                        │      │                  ├ [9] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/CSD2YB
                        │      │                  │       XP3ZF44E44QMIIAR5VTO35KTRB/ 
                        │      │                  ├ [10]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/UDBDBA
                        │      │                  │       U6HUPZHISBOARTXZ5GKHF2VH5U/ 
                        │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2022-0391 
                        │      │                  ├ [12]: https://security.gentoo.org/glsa/202305-02 
                        │      │                  ├ [13]: https://security.netapp.com/advisory/ntap-202202
                        │      │                  │       25-0009/ 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-5342-1 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-5342-2 
                        │      │                  ├ [16]: https://www.cve.org/CVERecord?id=CVE-2022-0391 
                        │      │                  ╰ [17]: https://www.oracle.com/security-alerts/cpuapr202
                        │      │                          2.html 
                        │      ├ PublishedDate   : 2022-02-09T23:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-03T11:15:00Z 
                        ├ [75] ╭ VulnerabilityID : CVE-2023-27043 
                        │      ├ PkgID           : python3@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27043 
                        │      ├ Title           : Parsing errors in email/_parseaddr.py lead to incorrect
                        │      │                    value in email address part of tuple 
                        │      ├ Description     : The email module of Python through 3.11.3 incorrectly
                        │      │                   parses e-mail addresses that contain a special character.
                        │      │                   The wrong portion of an RFC2822 header is identified as the
                        │      │                   value of the addr-spec. In some applications, an attacker
                        │      │                   can bypass a protection mechanism in which application
                        │      │                   access is granted only after verifying receipt of e-mail to
                        │      │                   a specific domain (e.g., only @company.example.com addresses
                        │      │                    may be used for signup). This occurs in email/_parseaddr.py
                        │      │                    in recent versions of Python. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-20 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: http://python.org 
                        │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2023-27043 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-27043 
                        │      │                  ├ [3]: https://github.com/python/cpython/issues/102988 
                        │      │                  ├ [4]: https://github.com/python/cpython/pull/102990 
                        │      │                  ├ [5]: https://github.com/python/cpython/pull/105127 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-27043 
                        │      │                  ├ [7]: https://python-security.readthedocs.io/vuln/email
                        │      │                  │      -parseaddr-realname.html 
                        │      │                  ├ [8]: https://security.netapp.com/advisory/ntap-2023060
                        │      │                  │      1-0003/ 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-27043 
                        │      ├ PublishedDate   : 2023-04-19T00:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-01T14:15:00Z 
                        ├ [76] ╭ VulnerabilityID : CVE-2023-36632 
                        │      ├ PkgID           : python3@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-36632 
                        │      ├ Title           : maximum recursion depth exceeded while calling a Python
                        │      │                    object 
                        │      ├ Description     : ** DISPUTED ** The legacy email.utils.parseaddr
                        │      │                   function in Python through 3.11.4 allows attackers to
                        │      │                   trigger "RecursionError: maximum recursion depth exceeded
                        │      │                   while calling a Python object" via a crafted argument. This
                        │      │                   argument is plausibly an untrusted value from an
                        │      │                   application's input data that was supposed to contain a name
                        │      │                    and an e-mail address. NOTE: email.utils.parseaddr is
                        │      │                   categorized as a Legacy API in the documentation of the
                        │      │                   Python email package. Applications should instead use the
                        │      │                   email.parser.BytesParser or email.parser.Parser class. NOTE:
                        │      │                    the vendor's perspective is that this is neither a
                        │      │                   vulnerability nor a bug. The email package is intended to
                        │      │                   have size limits and to throw an exception when limits are
                        │      │                   exceeded; they were exceeded by the example demonstration
                        │      │                   code. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-674 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-36632 
                        │      │                  ├ [1]: https://docs.python.org/3/library/email.html 
                        │      │                  ├ [2]: https://docs.python.org/3/library/email.utils.html 
                        │      │                  ├ [3]: https://github.com/Daybreak2019/PoC_python3.9_Vul
                        │      │                  │      /blob/main/RecursionError-email.utils.parseaddr.py
                        │      │                  │      [m 
                        │      │                  ├ [4]: https://github.com/python/cpython/issues/103800 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-36632 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-36632 
                        │      ├ PublishedDate   : 2023-06-25T18:15:00Z 
                        │      ╰ LastModifiedDate: 2023-07-06T16:00:00Z 
                        ├ [77] ╭ VulnerabilityID : CVE-2007-4559 
                        │      ├ PkgID           : python3-libs@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3-libs 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2007-4559 
                        │      ├ Title           : tarfile module directory traversal 
                        │      ├ Description     : Directory traversal vulnerability in the (1) extract
                        │      │                   and (2) extractall functions in the tarfile module in Python
                        │      │                    allows user-assisted remote attackers to overwrite
                        │      │                   arbitrary files via a .. (dot dot) sequence in filenames in
                        │      │                   a TAR archive, a related issue to CVE-2001-1267. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-22 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:P/I:P/A:P 
                        │      │                  │        ╰ V2Score : 6.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:H/A:N 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: http://mail.python.org/pipermail/python-dev/2007-
                        │      │                  │      August/074290.html 
                        │      │                  ├ [1]: http://mail.python.org/pipermail/python-dev/2007-
                        │      │                  │      August/074292.html 
                        │      │                  ├ [2]: http://secunia.com/advisories/26623 
                        │      │                  ├ [3]: http://www.vupen.com/english/advisories/2007/3022 
                        │      │                  ├ [4]: https://access.redhat.com/security/cve/CVE-2007-4559 
                        │      │                  ├ [5]: https://bugzilla.redhat.com/show_bug.cgi?id=263261 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2007-4559 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2007-4559 
                        │      ├ PublishedDate   : 2007-08-28T01:17:00Z 
                        │      ╰ LastModifiedDate: 2023-08-02T17:28:00Z 
                        ├ [78] ╭ VulnerabilityID : CVE-2021-23336 
                        │      ├ PkgID           : python3-libs@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3-libs 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
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
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:H/Au:N/C:N/I:P/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:L/A:H 
                        │      │                  │        ├ V2Score : 4 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:
                        │      │                           │           N/I:L/A:H 
                        │      │                           ╰ V3Score : 5.9 
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
                        │      │                  │       a291f358e077cafdb14d174b7a1ce9a9d86d1b332d6367@%3Cuse
                        │      │                  │       rs.airflow.apache.org%3E 
                        │      │                  ├ [10]: https://lists.apache.org/thread.html/rc005f4de9d
                        │      │                  │       9b0ba943ceb8ff5a21a5c6ff8a9df52632476698d99432@%3Cann
                        │      │                  │       ounce.apache.org%3E 
                        │      │                  ├ [11]: https://lists.apache.org/thread.html/rf9fa47ab66
                        │      │                  │       495c78bb4120b0754dd9531ca2ff0430f6685ac9b07772@%3Cdev
                        │      │                  │       .mina.apache.org%3E 
                        │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/02/msg00030.html 
                        │      │                  ├ [13]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/04/msg00005.html 
                        │      │                  ├ [14]: https://lists.debian.org/debian-lts-announce/202
                        │      │                  │       1/04/msg00015.html 
                        │      │                  ├ [15]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/3EPYWW
                        │      │                  │       FDV22CJ5AOH5VCE72DOASZZ255/ 
                        │      │                  ├ [16]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/3YKKDL
                        │      │                  │       XL3UEZ3J426C2XTBS63AHE46SM/ 
                        │      │                  ├ [17]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/46N6A5
                        │      │                  │       2EGSXHJYCZWVMBJJIH4NWIV2B5/ 
                        │      │                  ├ [18]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/FONHJI
                        │      │                  │       OZOFD7CD35KZL6SVBUTMBPGZGA/ 
                        │      │                  ├ [19]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/HCQTCS
                        │      │                  │       P6SCVIYNIRUJC5X7YBVUHPLSC4/ 
                        │      │                  ├ [20]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/HZTM7K
                        │      │                  │       LHFCE3LWSEVO2NAFLUHMGYMCRY/ 
                        │      │                  ├ [21]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/IHQDU7
                        │      │                  │       NXA7EWAE4W7VO6MURVJIULEPPR/ 
                        │      │                  ├ [22]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/KJXCMH
                        │      │                  │       LY7H3FIYLE4OKDYUILU2CCRUCZ/ 
                        │      │                  ├ [23]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/LVNH6Z
                        │      │                  │       24IG3E67ZCQGGJ46FZB4XFLQNZ/ 
                        │      │                  ├ [24]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/MNUN5S
                        │      │                  │       OMFL2BBKP6ZAICIIUPQKZDMGYO/ 
                        │      │                  ├ [25]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/MP572O
                        │      │                  │       LHMS7MZO4KUPSCIMSZIA5IZZ62/ 
                        │      │                  ├ [26]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/N6VXJZ
                        │      │                  │       SZ6N64AILJX4CTMACYGQGHHD5C/ 
                        │      │                  ├ [27]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/NJSCSN
                        │      │                  │       722JO2E2AGPWD4NTGVELVRPB4R/ 
                        │      │                  ├ [28]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/NODWHD
                        │      │                  │       IFBQE5RU5PUWUVE47JOT5VCMJ2/ 
                        │      │                  ├ [29]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/OAGSWN
                        │      │                  │       GZJ6HQ5ISA67SNMK3CJRKICET7/ 
                        │      │                  ├ [30]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/RSLQD5
                        │      │                  │       CCM75IZGAMBDGUZEATYU5YSGJ7/ 
                        │      │                  ├ [31]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/SGIY6I
                        │      │                  │       4YS3WOXAK4SXKIEOC2G4VZKIR7/ 
                        │      │                  ├ [32]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/TFTELU
                        │      │                  │       MWZE3KV3JB2H5EE6VFRZFRD5MV/ 
                        │      │                  ├ [33]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/W2LSKB
                        │      │                  │       EFI5SYEY5FM6ICZVZM5WRQUCS4/ 
                        │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2021-23336 
                        │      │                  ├ [35]: https://security.gentoo.org/glsa/202104-04 
                        │      │                  ├ [36]: https://security.netapp.com/advisory/ntap-202103
                        │      │                  │       26-0004/ 
                        │      │                  ├ [37]: https://snyk.io/blog/cache-poisoning-in-popular-
                        │      │                  │       open-source-packages/ 
                        │      │                  ├ [38]: https://snyk.io/vuln/SNYK-UPSTREAM-PYTHONCPYTHON
                        │      │                  │       -1074933 
                        │      │                  ├ [39]: https://ubuntu.com/security/notices/USN-4742-1 
                        │      │                  ├ [40]: https://www.cve.org/CVERecord?id=CVE-2021-23336 
                        │      │                  ├ [41]: https://www.djangoproject.com/weblog/2021/feb/19
                        │      │                  │       /security-releases/ 
                        │      │                  ├ [42]: https://www.oracle.com//security-alerts/cpujul20
                        │      │                  │       21.html 
                        │      │                  ├ [43]: https://www.oracle.com/security-alerts/cpuApr202
                        │      │                  │       1.html 
                        │      │                  ├ [44]: https://www.oracle.com/security-alerts/cpujan202
                        │      │                  │       2.html 
                        │      │                  ╰ [45]: https://www.oracle.com/security-alerts/cpuoct202
                        │      │                          1.html 
                        │      ├ PublishedDate   : 2021-02-15T13:15:00Z 
                        │      ╰ LastModifiedDate: 2022-03-04T19:13:00Z 
                        ├ [79] ╭ VulnerabilityID : CVE-2022-0391 
                        │      ├ PkgID           : python3-libs@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3-libs 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-0391 
                        │      ├ Title           : urllib.parse does not sanitize URLs containing ASCII
                        │      │                   newline and tabs 
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
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:P/A:N 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:H/A:N 
                        │      │                  │        ├ V2Score : 5 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
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
                        │      │                  ├ [9] : https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/CSD2YB
                        │      │                  │       XP3ZF44E44QMIIAR5VTO35KTRB/ 
                        │      │                  ├ [10]: https://lists.fedoraproject.org/archives/list/pa
                        │      │                  │       ckage-announce@lists.fedoraproject.org/message/UDBDBA
                        │      │                  │       U6HUPZHISBOARTXZ5GKHF2VH5U/ 
                        │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2022-0391 
                        │      │                  ├ [12]: https://security.gentoo.org/glsa/202305-02 
                        │      │                  ├ [13]: https://security.netapp.com/advisory/ntap-202202
                        │      │                  │       25-0009/ 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-5342-1 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-5342-2 
                        │      │                  ├ [16]: https://www.cve.org/CVERecord?id=CVE-2022-0391 
                        │      │                  ╰ [17]: https://www.oracle.com/security-alerts/cpuapr202
                        │      │                          2.html 
                        │      ├ PublishedDate   : 2022-02-09T23:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-03T11:15:00Z 
                        ├ [80] ╭ VulnerabilityID : CVE-2023-27043 
                        │      ├ PkgID           : python3-libs@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3-libs 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27043 
                        │      ├ Title           : Parsing errors in email/_parseaddr.py lead to incorrect
                        │      │                    value in email address part of tuple 
                        │      ├ Description     : The email module of Python through 3.11.3 incorrectly
                        │      │                   parses e-mail addresses that contain a special character.
                        │      │                   The wrong portion of an RFC2822 header is identified as the
                        │      │                   value of the addr-spec. In some applications, an attacker
                        │      │                   can bypass a protection mechanism in which application
                        │      │                   access is granted only after verifying receipt of e-mail to
                        │      │                   a specific domain (e.g., only @company.example.com addresses
                        │      │                    may be used for signup). This occurs in email/_parseaddr.py
                        │      │                    in recent versions of Python. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-20 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: http://python.org 
                        │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2023-27043 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                        │      │                  │      E-2023-27043 
                        │      │                  ├ [3]: https://github.com/python/cpython/issues/102988 
                        │      │                  ├ [4]: https://github.com/python/cpython/pull/102990 
                        │      │                  ├ [5]: https://github.com/python/cpython/pull/105127 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-27043 
                        │      │                  ├ [7]: https://python-security.readthedocs.io/vuln/email
                        │      │                  │      -parseaddr-realname.html 
                        │      │                  ├ [8]: https://security.netapp.com/advisory/ntap-2023060
                        │      │                  │      1-0003/ 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-27043 
                        │      ├ PublishedDate   : 2023-04-19T00:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-01T14:15:00Z 
                        ├ [81] ╭ VulnerabilityID : CVE-2023-36632 
                        │      ├ PkgID           : python3-libs@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3-libs 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-36632 
                        │      ├ Title           : maximum recursion depth exceeded while calling a Python
                        │      │                    object 
                        │      ├ Description     : ** DISPUTED ** The legacy email.utils.parseaddr
                        │      │                   function in Python through 3.11.4 allows attackers to
                        │      │                   trigger "RecursionError: maximum recursion depth exceeded
                        │      │                   while calling a Python object" via a crafted argument. This
                        │      │                   argument is plausibly an untrusted value from an
                        │      │                   application's input data that was supposed to contain a name
                        │      │                    and an e-mail address. NOTE: email.utils.parseaddr is
                        │      │                   categorized as a Legacy API in the documentation of the
                        │      │                   Python email package. Applications should instead use the
                        │      │                   email.parser.BytesParser or email.parser.Parser class. NOTE:
                        │      │                    the vendor's perspective is that this is neither a
                        │      │                   vulnerability nor a bug. The email package is intended to
                        │      │                   have size limits and to throw an exception when limits are
                        │      │                   exceeded; they were exceeded by the example demonstration
                        │      │                   code. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-674 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-36632 
                        │      │                  ├ [1]: https://docs.python.org/3/library/email.html 
                        │      │                  ├ [2]: https://docs.python.org/3/library/email.utils.html 
                        │      │                  ├ [3]: https://github.com/Daybreak2019/PoC_python3.9_Vul
                        │      │                  │      /blob/main/RecursionError-email.utils.parseaddr.py
                        │      │                  │      [m 
                        │      │                  ├ [4]: https://github.com/python/cpython/issues/103800 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-36632 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-36632 
                        │      ├ PublishedDate   : 2023-06-25T18:15:00Z 
                        │      ╰ LastModifiedDate: 2023-07-06T16:00:00Z 
                        ├ [82] ╭ VulnerabilityID : CVE-2021-3572 
                        │      ├ PkgID           : python3-pip-wheel@21.2.3-6.el9.noarch 
                        │      ├ PkgName         : python3-pip-wheel 
                        │      ├ InstalledVersion: 21.2.3-6.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
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
                        │      ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:
                        │      │                  │        │           N/I:H/A:N 
                        │      │                  │        ╰ V3Score : 5.7 
                        │      │                  ├ nvd    ╭ V2Vector: AV:N/AC:M/Au:S/C:N/I:P/A:N 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:
                        │      │                  │        │           N/I:H/A:N 
                        │      │                  │        ├ V2Score : 3.5 
                        │      │                  │        ╰ V3Score : 5.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:U/C:
                        │      │                           │           N/I:H/A:N 
                        │      │                           ╰ V3Score : 4.5 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2021:3254 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2021-3572 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=1962856 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=C
                        │      │                  │       VE-2021-3572 
                        │      │                  ├ [4] : https://github.com/advisories/GHSA-5xp3-jfq3-5q8x 
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
                        │      ├ PublishedDate   : 2021-11-10T18:15:00Z 
                        │      ╰ LastModifiedDate: 2022-10-05T02:14:00Z 
                        ├ [83] ╭ VulnerabilityID : CVE-2021-35937 
                        │      ├ PkgID           : rpm@4.16.1.3-22.el9.x86_64 
                        │      ├ PkgName         : rpm 
                        │      ├ InstalledVersion: 4.16.1.3-22.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-35937 
                        │      ├ Title           : TOCTOU race in checks for unsafe symlinks 
                        │      ├ Description     : A race condition vulnerability was found in rpm. A
                        │      │                   local unprivileged user could use this flaw to bypass the
                        │      │                   checks that were introduced in response to CVE-2017-7500 and
                        │      │                    CVE-2017-7501, potentially gaining root privileges. The
                        │      │                   highest threat from this vulnerability is to data
                        │      │                   confidentiality and integrity as well as system
                        │      │                   availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-367 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 6.4 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:H/UI:R/S:U/C:
                        │      │                           │           H/I:H/A:H 
                        │      │                           ╰ V3Score : 6.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-35937 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1964125 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2021-35937 
                        │      │                  ├ [3]: https://rpm.org/wiki/Releases/4.18.0 
                        │      │                  ├ [4]: https://security.gentoo.org/glsa/202210-22 
                        │      │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2021-35937 
                        │      │                  ╰ [6]: https://www.usenix.org/legacy/event/sec05/tech/fu
                        │      │                         ll_papers/borisov/borisov.pdf 
                        │      ├ PublishedDate   : 2022-08-25T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-26T17:48:00Z 
                        ├ [84] ╭ VulnerabilityID : CVE-2021-35938 
                        │      ├ PkgID           : rpm@4.16.1.3-22.el9.x86_64 
                        │      ├ PkgName         : rpm 
                        │      ├ InstalledVersion: 4.16.1.3-22.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-35938 
                        │      ├ Title           : races with chown/chmod/capabilities calls during
                        │      │                   installation 
                        │      ├ Description     : A symbolic link issue was found in rpm. It occurs when
                        │      │                   rpm sets the desired permissions and credentials after
                        │      │                   installing a file. A local unprivileged user could use this
                        │      │                   flaw to exchange the original file with a symbolic link to a
                        │      │                    security-critical file and escalate their privileges on the
                        │      │                    system. The highest threat from this vulnerability is to
                        │      │                   data confidentiality and integrity as well as system
                        │      │                   availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-59 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 6.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:
                        │      │                           │           H/I:H/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-35938 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1964114 
                        │      │                  ├ [2]: https://bugzilla.suse.com/show_bug.cgi?id=1157880 
                        │      │                  ├ [3]: https://github.com/rpm-software-management/rpm/co
                        │      │                  │      mmit/25a435e90844ea98fe5eb7bef22c1aecf3a9c033 
                        │      │                  ├ [4]: https://github.com/rpm-software-management/rpm/pu
                        │      │                  │      ll/1919 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2021-35938 
                        │      │                  ├ [6]: https://rpm.org/wiki/Releases/4.18.0 
                        │      │                  ├ [7]: https://security.gentoo.org/glsa/202210-22 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2021-35938 
                        │      ├ PublishedDate   : 2022-08-25T20:15:00Z 
                        │      ╰ LastModifiedDate: 2022-11-29T18:06:00Z 
                        ├ [85] ╭ VulnerabilityID : CVE-2021-35939 
                        │      ├ PkgID           : rpm@4.16.1.3-22.el9.x86_64 
                        │      ├ PkgName         : rpm 
                        │      ├ InstalledVersion: 4.16.1.3-22.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-35939 
                        │      ├ Title           : checks for unsafe symlinks are not performed for
                        │      │                   intermediary directories 
                        │      ├ Description     : It was found that the fix for CVE-2017-7500 and
                        │      │                   CVE-2017-7501 was incomplete: the check was only implemented
                        │      │                    for the parent directory of the file to be created. A local
                        │      │                    unprivileged user who owns another ancestor directory could
                        │      │                    potentially use this flaw to gain root privileges. The
                        │      │                   highest threat from this vulnerability is to data
                        │      │                   confidentiality and integrity as well as system
                        │      │                   availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-59 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 6.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:
                        │      │                           │           H/I:H/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-35939 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1964129 
                        │      │                  ├ [2]: https://github.com/rpm-software-management/rpm/co
                        │      │                  │      mmit/96ec957e281220f8e137a2d5eb23b83a6377d556 
                        │      │                  ├ [3]: https://github.com/rpm-software-management/rpm/pu
                        │      │                  │      ll/1919 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2021-35939 
                        │      │                  ├ [5]: https://rpm.org/wiki/Releases/4.18.0 
                        │      │                  ├ [6]: https://security.gentoo.org/glsa/202210-22 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2021-35939 
                        │      ├ PublishedDate   : 2022-08-26T16:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-04T01:16:00Z 
                        ├ [86] ╭ VulnerabilityID : CVE-2021-35937 
                        │      ├ PkgID           : rpm-libs@4.16.1.3-22.el9.x86_64 
                        │      ├ PkgName         : rpm-libs 
                        │      ├ InstalledVersion: 4.16.1.3-22.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-35937 
                        │      ├ Title           : TOCTOU race in checks for unsafe symlinks 
                        │      ├ Description     : A race condition vulnerability was found in rpm. A
                        │      │                   local unprivileged user could use this flaw to bypass the
                        │      │                   checks that were introduced in response to CVE-2017-7500 and
                        │      │                    CVE-2017-7501, potentially gaining root privileges. The
                        │      │                   highest threat from this vulnerability is to data
                        │      │                   confidentiality and integrity as well as system
                        │      │                   availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-367 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 6.4 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:H/UI:R/S:U/C:
                        │      │                           │           H/I:H/A:H 
                        │      │                           ╰ V3Score : 6.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-35937 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1964125 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2021-35937 
                        │      │                  ├ [3]: https://rpm.org/wiki/Releases/4.18.0 
                        │      │                  ├ [4]: https://security.gentoo.org/glsa/202210-22 
                        │      │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2021-35937 
                        │      │                  ╰ [6]: https://www.usenix.org/legacy/event/sec05/tech/fu
                        │      │                         ll_papers/borisov/borisov.pdf 
                        │      ├ PublishedDate   : 2022-08-25T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-26T17:48:00Z 
                        ├ [87] ╭ VulnerabilityID : CVE-2021-35938 
                        │      ├ PkgID           : rpm-libs@4.16.1.3-22.el9.x86_64 
                        │      ├ PkgName         : rpm-libs 
                        │      ├ InstalledVersion: 4.16.1.3-22.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-35938 
                        │      ├ Title           : races with chown/chmod/capabilities calls during
                        │      │                   installation 
                        │      ├ Description     : A symbolic link issue was found in rpm. It occurs when
                        │      │                   rpm sets the desired permissions and credentials after
                        │      │                   installing a file. A local unprivileged user could use this
                        │      │                   flaw to exchange the original file with a symbolic link to a
                        │      │                    security-critical file and escalate their privileges on the
                        │      │                    system. The highest threat from this vulnerability is to
                        │      │                   data confidentiality and integrity as well as system
                        │      │                   availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-59 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 6.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:
                        │      │                           │           H/I:H/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-35938 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1964114 
                        │      │                  ├ [2]: https://bugzilla.suse.com/show_bug.cgi?id=1157880 
                        │      │                  ├ [3]: https://github.com/rpm-software-management/rpm/co
                        │      │                  │      mmit/25a435e90844ea98fe5eb7bef22c1aecf3a9c033 
                        │      │                  ├ [4]: https://github.com/rpm-software-management/rpm/pu
                        │      │                  │      ll/1919 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2021-35938 
                        │      │                  ├ [6]: https://rpm.org/wiki/Releases/4.18.0 
                        │      │                  ├ [7]: https://security.gentoo.org/glsa/202210-22 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2021-35938 
                        │      ├ PublishedDate   : 2022-08-25T20:15:00Z 
                        │      ╰ LastModifiedDate: 2022-11-29T18:06:00Z 
                        ├ [88] ╭ VulnerabilityID : CVE-2021-35939 
                        │      ├ PkgID           : rpm-libs@4.16.1.3-22.el9.x86_64 
                        │      ├ PkgName         : rpm-libs 
                        │      ├ InstalledVersion: 4.16.1.3-22.el9 
                        │      ├ Status          : will_not_fix 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-35939 
                        │      ├ Title           : checks for unsafe symlinks are not performed for
                        │      │                   intermediary directories 
                        │      ├ Description     : It was found that the fix for CVE-2017-7500 and
                        │      │                   CVE-2017-7501 was incomplete: the check was only implemented
                        │      │                    for the parent directory of the file to be created. A local
                        │      │                    unprivileged user who owns another ancestor directory could
                        │      │                    potentially use this flaw to gain root privileges. The
                        │      │                   highest threat from this vulnerability is to data
                        │      │                   confidentiality and integrity as well as system
                        │      │                   availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-59 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:
                        │      │                  │        │           H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 6.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:
                        │      │                           │           H/I:H/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-35939 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1964129 
                        │      │                  ├ [2]: https://github.com/rpm-software-management/rpm/co
                        │      │                  │      mmit/96ec957e281220f8e137a2d5eb23b83a6377d556 
                        │      │                  ├ [3]: https://github.com/rpm-software-management/rpm/pu
                        │      │                  │      ll/1919 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2021-35939 
                        │      │                  ├ [5]: https://rpm.org/wiki/Releases/4.18.0 
                        │      │                  ├ [6]: https://security.gentoo.org/glsa/202210-22 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2021-35939 
                        │      ├ PublishedDate   : 2022-08-26T16:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-04T01:16:00Z 
                        ├ [89] ╭ VulnerabilityID : CVE-2023-36191 
                        │      ├ PkgID           : sqlite-libs@3.34.1-6.el9_1.x86_64 
                        │      ├ PkgName         : sqlite-libs 
                        │      ├ InstalledVersion: 3.34.1-6.el9_1 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                        │      │                  │         34cc313627f8113246276bf0f 
                        │      │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                        │      │                            e8e7055ef62d24ba202202e19 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-36191 
                        │      ├ Title           : CLI fault on missing -nonce 
                        │      ├ Description     : sqlite3 v3.40.1 was discovered to contain a
                        │      │                   segmentation violation at /sqlite3_aflpp/shell.c. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:
                        │      │                  │        │           N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                        │      │                           │           N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-36191 
                        │      │                  ├ [1]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/KREKCQTJ
                        │      │                  │      DVI2AEBG5ECZPSOQXIC2L5XL/ 
                        │      │                  ├ [2]: https://lists.fedoraproject.org/archives/list/pac
                        │      │                  │      kage-announce@lists.fedoraproject.org/message/UBAHED5Y
                        │      │                  │      FJPRGSEKNZIYHZBGSVHGEHOH/ 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-36191 
                        │      │                  ├ [4]: https://www.cve.org/CVERecord?id=CVE-2023-36191 
                        │      │                  ╰ [5]: https://www.sqlite.org/forum/forumpost/19f55ef73b 
                        │      ├ PublishedDate   : 2023-06-23T02:15:00Z 
                        │      ╰ LastModifiedDate: 2023-07-04T04:15:00Z 
                        ├ [90] ╭ VulnerabilityID : CVE-2023-28486 
                        │      ├ PkgID           : sudo@1.9.5p2-9.el9.x86_64 
                        │      ├ PkgName         : sudo 
                        │      ├ InstalledVersion: 1.9.5p2-9.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28486 
                        │      ├ Title           : Sudo does not escape control characters in log messages 
                        │      ├ Description     : Sudo before 1.9.13 does not escape control characters
                        │      │                   in log messages. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-116 
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
                        │      │                  ├ [5]: https://security.netapp.com/advisory/ntap-2023042
                        │      │                  │      0-0002/ 
                        │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-6005-1 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-6005-2 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-28486 
                        │      ├ PublishedDate   : 2023-03-16T01:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-20T09:15:00Z 
                        ├ [91] ╭ VulnerabilityID : CVE-2023-28487 
                        │      ├ PkgID           : sudo@1.9.5p2-9.el9.x86_64 
                        │      ├ PkgName         : sudo 
                        │      ├ InstalledVersion: 1.9.5p2-9.el9 
                        │      ├ Status          : affected 
                        │      ├ Layer            ╭ Digest: sha256:cd88437a6094844c24dfcee4fd130d1b07fc2f1
                        │      │                  │         6d7d03765489b31e3b215f5e5 
                        │      │                  ╰ DiffID: sha256:1f3978e72111e44ebf85001b385520335f432ee
                        │      │                            09d3cd5d1208c1c286751fce9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28487 
                        │      ├ Title           : Sudo does not escape control characters in sudoreplay output 
                        │      ├ Description     : Sudo before 1.9.13 does not escape control characters
                        │      │                   in sudoreplay output. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-116 
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
                        │      │                  ├ [5]: https://security.netapp.com/advisory/ntap-2023042
                        │      │                  │      0-0002/ 
                        │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-6005-1 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-6005-2 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-28487 
                        │      ├ PublishedDate   : 2023-03-16T01:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-20T09:15:00Z 
                        ╰ [92] ╭ VulnerabilityID : CVE-2021-3997 
                               ├ PkgID           : systemd-libs@252-14.el9_2.1.x86_64 
                               ├ PkgName         : systemd-libs 
                               ├ InstalledVersion: 252-14.el9_2.1 
                               ├ Status          : affected 
                               ├ Layer            ╭ Digest: sha256:62742f27dce5ebff467a57ad6bfa680820f3bc5
                               │                  │         34cc313627f8113246276bf0f 
                               │                  ╰ DiffID: sha256:8ed77c26f435056ec36532ec08d271f276190e7
                               │                            e8e7055ef62d24ba202202e19 
                               ├ SeveritySource  : redhat 
                               ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-3997 
                               ├ Title           : Uncontrolled recursion in systemd-tmpfiles when
                               │                   removing files 
                               ├ Description     : A flaw was found in systemd. An uncontrolled recursion
                               │                   in systemd-tmpfiles may lead to a denial of service at boot
                               │                   time when too many nested directories are created in
                               │                   /tmp. 
                               ├ Severity        : MEDIUM 
                               ├ CweIDs           ─ [0]: CWE-674 
                               ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                               │                  │        │           N/I:N/A:H 
                               │                  │        ╰ V3Score : 5.5 
                               │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:
                               │                           │           N/I:N/A:H 
                               │                           ╰ V3Score : 5.5 
                               ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-3997 
                               │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2024639 
                               │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CV
                               │                  │      E-2021-3997 
                               │                  ├ [3]: https://github.com/systemd/systemd/commit/5b1cf7a
                               │                  │      9be37e20133c0208005274ce4a5b5c6a1 
                               │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2021-3997 
                               │                  ├ [5]: https://security.gentoo.org/glsa/202305-15 
                               │                  ├ [6]: https://ubuntu.com/security/notices/USN-5226-1 
                               │                  ├ [7]: https://www.cve.org/CVERecord?id=CVE-2021-3997 
                               │                  ╰ [8]: https://www.openwall.com/lists/oss-security/2022/
                               │                         01/10/2 
                               ├ PublishedDate   : 2022-08-23T20:15:00Z 
                               ╰ LastModifiedDate: 2023-05-03T12:15:00Z 
````
