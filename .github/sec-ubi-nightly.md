````yaml
─ [0] ╭ Target         : openaf/oaf:ubi-nightly (redhat 9.2) 
      ├ Class          : os-pkgs 
      ├ Type           : redhat 
      ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2021-3468 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-3468 
                        │      ├ Title           : avahi: Local DoS by event-busy-loop from writing long lines to /run/avahi-daemon/socket 
                        │      ├ Description     : A flaw was found in avahi in versions 0.6 up to 0.8. The event used to signal the termination of the
                        │      │                   client connection on the avahi Unix socket is not correctly handled in the client_work function, allowing a
                        │      │                   local attacker to trigger an infinite loop. The highest threat from this vulnerability is to the
                        │      │                   availability of the avahi service, which becomes unresponsive after this flaw is triggered. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-835 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:L/AC:L/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ├ V2Score : 2.1 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-3468 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1939614 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3468 
                        │      │                  ├ [3]: https://lists.debian.org/debian-lts-announce/2022/06/msg00009.html 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2021-3468 
                        │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-5008-1 
                        │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-5008-2 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2021-3468 
                        │      ├ PublishedDate   : 2021-06-02T16:15:00Z 
                        │      ╰ LastModifiedDate: 2023-01-20T02:24:00Z 
                        ├ [1]  ╭ VulnerabilityID : CVE-2021-3502 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-3502 
                        │      ├ Title           : reachable assertion in avahi_s_host_name_resolver_start when trying to resolve badly-formatted hostnames 
                        │      ├ Description     : A flaw was found in avahi 0.8-5. A reachable assertion is present in avahi_s_host_name_resolver_start
                        │      │                   function allowing a local attacker to crash the avahi service by requesting hostname resolutions through the
                        │      │                    avahi socket or dbus methods for invalid hostnames. The highest threat from this vulnerability is to the
                        │      │                   service availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ╭ [0]: CWE-476 
                        │      │                  ╰ [1]: CWE-617 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:L/AC:L/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ├ V2Score : 2.1 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-3502 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1946914 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3502 
                        │      │                  ├ [3]: https://github.com/lathiat/avahi/issues/338 
                        │      │                  ├ [4]: https://github.com/lathiat/avahi/pull/324 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2021-3502 
                        │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-5008-1 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2021-3502 
                        │      ├ PublishedDate   : 2021-05-07T12:15:00Z 
                        │      ╰ LastModifiedDate: 2021-05-17T17:30:00Z 
                        ├ [2]  ╭ VulnerabilityID : CVE-2023-1981 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-1981 
                        │      ├ Title           : avahi-daemon can be crashed via DBus 
                        │      ├ Description     : A vulnerability was found in the avahi library. This flaw allows an unprivileged user to make a dbus
                        │      │                   call, causing the avahi daemon to crash. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-400 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-1981 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2185911 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1981 
                        │      │                  ├ [3]: https://github.com/lathiat/avahi/issues/375 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-1981 
                        │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-6129-1 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-1981 
                        │      ├ PublishedDate   : 2023-05-26T18:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-02T19:06:00Z 
                        ├ [3]  ╭ VulnerabilityID : CVE-2017-6519 
                        │      ├ PkgID           : avahi-libs@0.8-12.el9.x86_64 
                        │      ├ PkgName         : avahi-libs 
                        │      ├ InstalledVersion: 0.8-12.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2017-6519 
                        │      ├ Title           : Multicast DNS responds to unicast queries outside of local network 
                        │      ├ Description     : avahi-daemon in Avahi through 0.6.32 and 0.7 inadvertently responds to IPv6 unicast queries with source
                        │      │                    addresses that are not on-link, which allows remote attackers to cause a denial of service (traffic
                        │      │                   amplification) and may cause information leakage by obtaining potentially sensitive  information from the
                        │      │                   responding device via port-5353 UDP packets.  NOTE: this may overlap CVE-2015-2809. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-346 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:P/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H 
                        │      │                  │        ├ V2Score : 6.4 
                        │      │                  │        ╰ V3Score : 9.1 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:N/A:L 
                        │      │                           ╰ V3Score : 5.8 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2017-6519 
                        │      │                  ├ [1] : https://bugzilla.redhat.com/show_bug.cgi?id=1426712 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-6519 
                        │      │                  ├ [3] : https://github.com/lathiat/avahi/issues/203 
                        │      │                  ├ [4] : https://github.com/lathiat/avahi/issues/203#issuecomment-449536790 
                        │      │                  ├ [5] : https://linux.oracle.com/cve/CVE-2017-6519.html 
                        │      │                  ├ [6] : https://linux.oracle.com/errata/ELSA-2020-1176.html 
                        │      │                  ├ [7] : https://lists.apache.org/thread.html/r1b103833cb5bc8466e24ff0ecc5e75b45a705334ab6a444e64e840a0@%
                        │      │                  │       3Cissues.bookkeeper.apache.org%3E 
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
                        ├ [4]  ╭ VulnerabilityID : CVE-2023-32324 
                        │      ├ PkgID           : cups-libs@2.3.3op2-16.el9.x86_64 
                        │      ├ PkgName         : cups-libs 
                        │      ├ InstalledVersion: 1:2.3.3op2-16.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-32324 
                        │      ├ Title           : heap buffer overflow may lead to DoS 
                        │      ├ Description     : OpenPrinting CUPS is an open source printing system. In versions 2.4.2 and prior, a heap buffer
                        │      │                   overflow vulnerability would allow a remote attacker to launch a denial of service (DoS) attack. A buffer
                        │      │                   overflow vulnerability in the function `format_log_line` could allow remote attackers to cause a DoS on the
                        │      │                   affected system. Exploitation of the vulnerability can be triggered when the configuration file `cupsd.conf`
                        │      │                    sets the value of `loglevel `to `DEBUG`. No known patches or workarounds exist at time of
                        │      │                   publication. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-787 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-32324 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32324 
                        │      │                  ├ [2]: https://github.com/OpenPrinting/cups/security/advisories/GHSA-cxc6-w2g7-69p7 
                        │      │                  ├ [3]: https://lists.debian.org/debian-lts-announce/2023/06/msg00001.html 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-32324 
                        │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-6128-1 
                        │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-6128-2 
                        │      │                  ├ [7]: https://www.cve.org/CVERecord?id=CVE-2023-32324 
                        │      │                  ╰ [8]: https://www.openwall.com/lists/oss-security/2023/06/01/1 
                        │      ├ PublishedDate   : 2023-06-01T17:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-08T14:32:00Z 
                        ├ [5]  ╭ VulnerabilityID : CVE-2021-25317 
                        │      ├ PkgID           : cups-libs@2.3.3op2-16.el9.x86_64 
                        │      ├ PkgName         : cups-libs 
                        │      ├ InstalledVersion: 1:2.3.3op2-16.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-25317 
                        │      ├ Title           : cups: insecure permissions of /var/log/cups allows for symlink attacks 
                        │      ├ Description     : A Incorrect Default Permissions vulnerability in the packaging of cups of SUSE Linux Enterprise Server
                        │      │                   11-SP4-LTSS, SUSE Manager Server 4.0, SUSE OpenStack Cloud Crowbar 9; openSUSE Leap 15.2, Factory allows
                        │      │                   local attackers with control of the lp users to create files as root with 0644 permissions without the
                        │      │                   ability to set the content. This issue affects: SUSE Linux Enterprise Server 11-SP4-LTSS cups versions prior
                        │      │                    to 1.3.9. SUSE Manager Server 4.0 cups versions prior to 2.2.7. SUSE OpenStack Cloud Crowbar 9 cups
                        │      │                   versions prior to 1.7.5. openSUSE Leap 15.2 cups versions prior to 2.2.7. openSUSE Factory cups version
                        │      │                   2.3.3op2-2.1 and prior versions. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-276 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:L/AC:L/Au:N/C:N/I:P/A:N 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N 
                        │      │                  │        ├ V2Score : 2.1 
                        │      │                  │        ╰ V3Score : 3.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 2 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-25317 
                        │      │                  ├ [1]: https://bugzilla.suse.com/show_bug.cgi?id=1184161 
                        │      │                  ├ [2]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/GW
                        │      │                  │      PGZLT3U776Q5YPPSA6LGFWWBDWBVH3/ 
                        │      │                  ├ [3]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/H7
                        │      │                  │      4BP746O5NNVCBUTLLZYAFBPESFVECV/ 
                        │      │                  ├ [4]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/S3
                        │      │                  │      7IDQGHTORQ3Z6VRDQIGBYVOI27YG47/ 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2021-25317 
                        │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2021-25317 
                        │      ├ PublishedDate   : 2021-05-05T10:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-14T18:49:00Z 
                        ├ [6]  ╭ VulnerabilityID : CVE-2023-27536 
                        │      ├ PkgID           : curl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27536 
                        │      ├ Title           : GSS delegation too eager connection re-use 
                        │      ├ Description     : An authentication bypass vulnerability exists libcurl <8.0.0 in the connection reuse feature which can
                        │      │                   reuse previously established connections with incorrect user permissions due to a failure to check for
                        │      │                   changes in the CURLOPT_GSSAPI_DELEGATION option. This vulnerability affects krb5/kerberos/negotiate/GSSAPI
                        │      │                   transfers and could potentially result in unauthorized access to sensitive information. The safest option is
                        │      │                    to not reuse connections if the CURLOPT_GSSAPI_DELEGATION option has been changed. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-287 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-27536 
                        │      │                  ├ [1] : https://curl.se/docs/CVE-2023-27536.html 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27536 
                        │      │                  ├ [3] : https://hackerone.com/reports/1895135 
                        │      │                  ├ [4] : https://lists.debian.org/debian-lts-announce/2023/04/msg00025.html 
                        │      │                  ├ [5] : https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/3
                        │      │                  │       6NBD5YLJXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-27536 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-20230420-0010/ 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-5964-2 
                        │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2023-27536 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-06T20:34:00Z 
                        ├ [7]  ╭ VulnerabilityID : CVE-2023-28321 
                        │      ├ PkgID           : curl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28321 
                        │      ├ Title           : IDN wildcard match may lead to Improper Cerificate Validation 
                        │      ├ Description     : An improper certificate validation vulnerability exists in curl <v8.1.0 in the way it supports matching
                        │      │                    of wildcard patterns when listed as "Subject Alternative Name" in TLS server certificates. curl can be
                        │      │                   built to use its own name matching function for TLS rather than one provided by a TLS library. This private
                        │      │                   wildcard matching function would match IDN (International Domain Name) hosts incorrectly and could as a
                        │      │                   result accept patterns that otherwise should mismatch. IDN hostnames are converted to puny code before used
                        │      │                   for certificate checks. Puny coded names always start with `xn--` and should not be allowed to pattern
                        │      │                   match, but the wildcard check in curl could still check for `x*`, which would match even though the IDN name
                        │      │                    most likely contained nothing even resembling an `x`. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-295 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L 
                        │      │                           ╰ V3Score : 5.6 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-28321 
                        │      │                  ├ [1]: https://curl.se/docs/CVE-2023-28321.html 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28321 
                        │      │                  ├ [3]: https://hackerone.com/reports/1950627 
                        │      │                  ├ [4]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/F4
                        │      │                  │      I75RDGX5ULSSCBE5BF3P5I5SFO7ULQ/ 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/Z2
                        │      │                  │      LIWHWKOVH24COGGBCVOWDXXIUPKOMK/ 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-28321 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230609-0009/ 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-28321 
                        │      ├ PublishedDate   : 2023-05-26T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-09T08:15:00Z 
                        ├ [8]  ╭ VulnerabilityID : CVE-2023-28322 
                        │      ├ PkgID           : curl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28322 
                        │      ├ Title           : more POST-after-PUT confusion 
                        │      ├ Description     : An information disclosure vulnerability exists in curl <v8.1.0 when doing HTTP(S) transfers, libcurl
                        │      │                   might erroneously use the read callback (`CURLOPT_READFUNCTION`) to ask for data to send, even when the
                        │      │                   `CURLOPT_POSTFIELDS` option has been set, if the same handle previously wasused to issue a `PUT` request
                        │      │                   which used that callback. This flaw may surprise the application and cause it to misbehave and either send
                        │      │                   off the wrong data or use memory after free or similar in the second transfer. The problem exists in the
                        │      │                   logic for a reused handle when it is (expected to be) changed from a PUT to a POST. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N 
                        │      │                  │        ╰ V3Score : 9.1 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:L 
                        │      │                           ╰ V3Score : 4.8 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-28322 
                        │      │                  ├ [1]: https://curl.se/docs/CVE-2023-28322.html 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28322 
                        │      │                  ├ [3]: https://hackerone.com/reports/1954658 
                        │      │                  ├ [4]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/F4
                        │      │                  │      I75RDGX5ULSSCBE5BF3P5I5SFO7ULQ/ 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/Z2
                        │      │                  │      LIWHWKOVH24COGGBCVOWDXXIUPKOMK/ 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-28322 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230609-0009/ 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-28322 
                        │      ├ PublishedDate   : 2023-05-26T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-09T08:15:00Z 
                        ├ [9]  ╭ VulnerabilityID : CVE-2023-27533 
                        │      ├ PkgID           : curl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27533 
                        │      ├ Title           : TELNET option IAC injection 
                        │      ├ Description     : A vulnerability in input validation exists in curl <8.0 during communication using the TELNET protocol
                        │      │                   may allow an attacker to pass on maliciously crafted user name and "telnet options" during server
                        │      │                   negotiation. The lack of proper input scrubbing allows an attacker to send content or perform option
                        │      │                   negotiation without the application's intent. This vulnerability could be exploited if an application allows
                        │      │                    user input, thereby enabling attackers to execute arbitrary code on the system. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 8.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 3.1 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-27533 
                        │      │                  ├ [1] : https://curl.se/docs/CVE-2023-27533.html 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27533 
                        │      │                  ├ [3] : https://hackerone.com/reports/1891474 
                        │      │                  ├ [4] : https://lists.debian.org/debian-lts-announce/2023/04/msg00025.html 
                        │      │                  ├ [5] : https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/3
                        │      │                  │       6NBD5YLJXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-27533 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-20230420-0011/ 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-5964-2 
                        │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2023-27533 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-21T23:15:00Z 
                        ├ [10] ╭ VulnerabilityID : CVE-2023-27534 
                        │      ├ PkgID           : curl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27534 
                        │      ├ Title           : SFTP path ~ resolving discrepancy 
                        │      ├ Description     : A path traversal vulnerability exists in curl <8.0.0 SFTP implementation causes the tilde (~) character
                        │      │                    to be wrongly replaced when used as a prefix in the first path element, in addition to its intended use as
                        │      │                   the first element to indicate a path relative to the user's home directory. Attackers can exploit this flaw
                        │      │                   to bypass filtering or execute arbitrary code by crafting a path like /~2/foo while accessing a server with
                        │      │                   a specific user. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-22 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 8.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N 
                        │      │                           ╰ V3Score : 3.7 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-27534 
                        │      │                  ├ [1]: https://curl.se/docs/CVE-2023-27534.html 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27534 
                        │      │                  ├ [3]: https://hackerone.com/reports/1892351 
                        │      │                  ├ [4]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/36
                        │      │                  │      NBD5YLJXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-27534 
                        │      │                  ├ [6]: https://security.netapp.com/advisory/ntap-20230420-0012/ 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-27534 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-20T09:15:00Z 
                        ├ [11] ╭ VulnerabilityID : CVE-2023-27538 
                        │      ├ PkgID           : curl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : curl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27538 
                        │      ├ Title           : SSH connection too eager reuse still 
                        │      ├ Description     : An authentication bypass vulnerability exists in libcurl prior to v8.0.0 where it reuses a previously
                        │      │                   established SSH connection despite the fact that an SSH option was modified, which should have prevented
                        │      │                   reuse. libcurl maintains a pool of previously used connections to reuse them for subsequent transfers if the
                        │      │                    configurations match. However, two SSH settings were omitted from the configuration check, allowing them to
                        │      │                    match easily, potentially leading to the reuse of an inappropriate connection. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-287 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-27538 
                        │      │                  ├ [1]: https://curl.se/docs/CVE-2023-27538.html 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27538 
                        │      │                  ├ [3]: https://hackerone.com/reports/1898475 
                        │      │                  ├ [4]: https://lists.debian.org/debian-lts-announce/2023/04/msg00025.html 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/36
                        │      │                  │      NBD5YLJXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-27538 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230420-0010/ 
                        │      │                  ├ [8]: https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-27538 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-21T23:15:00Z 
                        ├ [12] ╭ VulnerabilityID : CVE-2023-34969 
                        │      ├ PkgID           : dbus-libs@1.12.20-7.el9_1.x86_64 
                        │      ├ PkgName         : dbus-libs 
                        │      ├ InstalledVersion: 1:1.12.20-7.el9_1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-34969 
                        │      ├ Title           : assertion failure when a monitor is active and a message from the driver cannot be delivered 
                        │      ├ Description     : D-Bus before 1.15.6 sometimes allows unprivileged users to crash dbus-daemon. If a privileged user with
                        │      │                    control over the dbus-daemon is using the org.freedesktop.DBus.Monitoring interface to monitor message bus
                        │      │                   traffic, then an unprivileged user with the ability to connect to the same dbus-daemon can cause a
                        │      │                   dbus-daemon crash under some circumstances via an unreplyable message. When done on the well-known system
                        │      │                   bus, this is a denial-of-service vulnerability. The fixed versions are 1.12.28, 1.14.8, and 1.15.6. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-34969 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34969 
                        │      │                  ├ [2]: https://gitlab.freedesktop.org/dbus/dbus/-/issues/457 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-34969 
                        │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2023-34969 
                        │      ├ PublishedDate   : 2023-06-08T03:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-08T17:08:00Z 
                        ├ [13] ╭ VulnerabilityID : CVE-2023-29499 
                        │      ├ PkgID           : glib2@2.68.4-6.el9.x86_64 
                        │      ├ PkgName         : glib2 
                        │      ├ InstalledVersion: 2.68.4-6.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-29499 
                        │      ├ Title           : GVariant offset table entry size is not checked in is_normal() 
                        │      ├ Description     : No description is available for this CVE. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-29499 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29499 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-29499 
                        │                         ├ [3]: https://ubuntu.com/security/notices/USN-6165-1 
                        │                         ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2023-29499 
                        ├ [14] ╭ VulnerabilityID : CVE-2023-32611 
                        │      ├ PkgID           : glib2@2.68.4-6.el9.x86_64 
                        │      ├ PkgName         : glib2 
                        │      ├ InstalledVersion: 2.68.4-6.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-32611 
                        │      ├ Title           : g_variant_byteswap() can take a long time with some non-normal inputs 
                        │      ├ Description     : No description is available for this CVE. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-32611 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32611 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-32611 
                        │                         ├ [3]: https://ubuntu.com/security/notices/USN-6165-1 
                        │                         ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2023-32611 
                        ├ [15] ╭ VulnerabilityID : CVE-2023-32636 
                        │      ├ PkgID           : glib2@2.68.4-6.el9.x86_64 
                        │      ├ PkgName         : glib2 
                        │      ├ InstalledVersion: 2.68.4-6.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-32636 
                        │      ├ Title           : Timeout in fuzz_variant_text 
                        │      ├ Description     : No description is available for this CVE. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 4.7 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-32636 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32636 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-32636 
                        │                         ├ [3]: https://ubuntu.com/security/notices/USN-6165-1 
                        │                         ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2023-32636 
                        ├ [16] ╭ VulnerabilityID : CVE-2023-32665 
                        │      ├ PkgID           : glib2@2.68.4-6.el9.x86_64 
                        │      ├ PkgName         : glib2 
                        │      ├ InstalledVersion: 2.68.4-6.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-32665 
                        │      ├ Title           : GVariant deserialisation does not match spec for non-normal data 
                        │      ├ Description     : No description is available for this CVE. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ╰ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-32665 
                        │                         ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32665 
                        │                         ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2023-32665 
                        │                         ├ [3]: https://ubuntu.com/security/notices/USN-6165-1 
                        │                         ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2023-32665 
                        ├ [17] ╭ VulnerabilityID : CVE-2021-43618 
                        │      ├ PkgID           : gmp@6.2.0-10.el9.x86_64 
                        │      ├ PkgName         : gmp 
                        │      ├ InstalledVersion: 1:6.2.0-10.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-43618 
                        │      ├ Title           : Integer overflow and resultant buffer overflow via crafted input 
                        │      ├ Description     : GNU Multiple Precision Arithmetic Library (GMP) through 6.2.1 has an mpz/inp_raw.c integer overflow and
                        │      │                    resultant buffer overflow via crafted input, leading to a segmentation fault on 32-bit platforms. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-190 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ├ V2Score : 5 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2022/Oct/8 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2022/10/13/3 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2021-43618 
                        │      │                  ├ [3] : https://bugs.debian.org/994405 
                        │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43618 
                        │      │                  ├ [5] : https://gmplib.org/list-archives/gmp-bugs/2021-September/005077.html 
                        │      │                  ├ [6] : https://gmplib.org/repo/gmp-6.2/rev/561a9c25298e 
                        │      │                  ├ [7] : https://lists.debian.org/debian-lts-announce/2021/12/msg00001.html 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2021-43618 
                        │      │                  ├ [9] : https://security.netapp.com/advisory/ntap-20221111-0001/ 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-5672-1 
                        │      │                  ├ [11]: https://ubuntu.com/security/notices/USN-5672-2 
                        │      │                  ╰ [12]: https://www.cve.org/CVERecord?id=CVE-2021-43618 
                        │      ├ PublishedDate   : 2021-11-15T04:15:00Z 
                        │      ╰ LastModifiedDate: 2022-12-08T22:15:00Z 
                        ├ [18] ╭ VulnerabilityID : CVE-2022-3219 
                        │      ├ PkgID           : gnupg2@2.3.3-2.el9_0.x86_64 
                        │      ├ PkgName         : gnupg2 
                        │      ├ InstalledVersion: 2.3.3-2.el9_0 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-3219 
                        │      ├ Title           : denial of service issue (resource consumption) using compressed packets 
                        │      ├ Description     : GnuPG can be made to spin on a relatively small input by (for example) crafting a public key with
                        │      │                   thousands of signatures attached, compressed down to just a few KB. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-787 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L 
                        │      │                  │        ╰ V3Score : 3.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.2 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-3219 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2127010 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3219 
                        │      │                  ├ [3]: https://dev.gnupg.org/D556 
                        │      │                  ├ [4]: https://dev.gnupg.org/T5993 
                        │      │                  ├ [5]: https://marc.info/?l=oss-security&m=165696590211434&w=4 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2022-3219 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230324-0001/ 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2022-3219 
                        │      ├ PublishedDate   : 2023-02-23T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-26T16:31:00Z 
                        ├ [19] ╭ VulnerabilityID : CVE-2023-25193 
                        │      ├ PkgID           : harfbuzz@2.7.4-8.el9.x86_64 
                        │      ├ PkgName         : harfbuzz 
                        │      ├ InstalledVersion: 2.7.4-8.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-25193 
                        │      ├ Title           : allows attackers to trigger O(n^2) growth via consecutive marks 
                        │      ├ Description     : hb-ot-layout-gsubgpos.hh in HarfBuzz through 6.0.0 allows attackers to trigger O(n^2) growth via
                        │      │                   consecutive marks during the process of looking back for base glyphs when attaching marks. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-770 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-25193 
                        │      │                  ├ [1]: https://chromium.googlesource.com/chromium/src/+/e1f324aa681af54101c1f2d173d92adb80e37088/DEPS#361 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25193 
                        │      │                  ├ [3]: https://github.com/harfbuzz/harfbuzz/blob/2822b589bc837fae6f66233e2cf2eef0f6ce8470/src/hb-ot-layo
                        │      │                  │      ut-gsubgpos.hh 
                        │      │                  ├ [4]: https://github.com/harfbuzz/harfbuzz/commit/85be877925ddbf34f74a1229f3ca1716bb6170dc 
                        │      │                  ├ [5]: https://github.com/harfbuzz/harfbuzz/commit/85be877925ddbf34f74a1229f3ca1716bb6170dc (reverted) 
                        │      │                  ├ [6]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/KW
                        │      │                  │      CHWSICWVZSAXP2YAXM65JC2GR53547/ 
                        │      │                  ├ [7]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/YZ
                        │      │                  │      5M2GSAIHFPLHYJXUPQ2QDJCLWXUGO3/ 
                        │      │                  ├ [8]: https://nvd.nist.gov/vuln/detail/CVE-2023-25193 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-25193 
                        │      ├ PublishedDate   : 2023-02-04T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-03-14T05:15:00Z 
                        ├ [20] ╭ VulnerabilityID : CVE-2022-3857 
                        │      ├ PkgID           : java-1.8.0-openjdk-headless@1.8.0.372.b07-2.el9.x86_64 
                        │      ├ PkgName         : java-1.8.0-openjdk-headless 
                        │      ├ InstalledVersion: 1:1.8.0.372.b07-2.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-3857 
                        │      ├ Title           : Null pointer dereference leads to segmentation fault 
                        │      ├ Description     : A flaw was found in libpng 1.6.38. A crafted PNG image can lead to a segmentation fault and denial of
                        │      │                   service in png_setup_paeth_row() function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-476 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-3857 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3857 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2022-3857 
                        │      │                  ├ [3]: https://security.netapp.com/advisory/ntap-20230406-0004/ 
                        │      │                  ├ [4]: https://sourceforge.net/p/libpng/bugs/300/ 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2022-3857 
                        │      ├ PublishedDate   : 2023-03-06T23:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-06T13:15:00Z 
                        ├ [21] ╭ VulnerabilityID : CVE-2023-30571 
                        │      ├ PkgID           : libarchive@3.5.3-4.el9.x86_64 
                        │      ├ PkgName         : libarchive 
                        │      ├ InstalledVersion: 3.5.3-4.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-30571 
                        │      ├ Title           : Race condition in multi-threaded use of archive_write_disk_header() on posix based systems 
                        │      ├ Description     : Libarchive through 3.6.2 can cause directories to have world-writable permissions. The umask() call
                        │      │                   inside archive_write_disk_posix.c changes the umask of the whole process for a very short period of time; a
                        │      │                   race condition with another thread can lead to a permanent umask 0 setting. Such a race condition could lead
                        │      │                    to implicit directory creation with permissions 0777 (without the sticky bit), which means that any
                        │      │                   low-privileged local user can delete and rename files inside those directories. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-362 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:H 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:R/S:C/C:L/I:L/A:N 
                        │      │                           ╰ V3Score : 3.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-30571 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-30571 
                        │      │                  ├ [2]: https://github.com/libarchive/libarchive/issues/1876 
                        │      │                  ├ [3]: https://groups.google.com/g/libarchive-announce 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-30571 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2023-30571 
                        │      ├ PublishedDate   : 2023-05-29T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-05T16:40:00Z 
                        ├ [22] ╭ VulnerabilityID : CVE-2023-29383 
                        │      ├ PkgID           : libblkid@2.37.4-11.el9_2.x86_64 
                        │      ├ PkgName         : libblkid 
                        │      ├ InstalledVersion: 2.37.4-11.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-29383 
                        │      ├ Title           : Improper input validation in shadow-utils package utility chfn 
                        │      ├ Description     : In Shadow 4.13, it is possible to inject control characters into fields provided to the SUID program
                        │      │                   chfn (change finger). Although it is not possible to exploit this directly (e.g., adding a new user fails
                        │      │                   because \n is in the block list), it is possible to misrepresent the /etc/passwd file when viewed. Use of \r
                        │      │                    manipulations and Unicode characters to work around blocking of the : character make it possible to give
                        │      │                   the impression that a new user has been added. In other words, an adversary may be able to convince a system
                        │      │                    administrator to take the system offline (an indirect, social-engineered denial of service) by
                        │      │                   demonstrating that "cat /etc/passwd" shows a rogue user account. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 3.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-29383 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29383 
                        │      │                  ├ [2]: https://github.com/shadow-maint/shadow/commit/e5905c4b84d4fb90aefcd96ee618411ebfac663d 
                        │      │                  ├ [3]: https://github.com/shadow-maint/shadow/pull/687 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-29383 
                        │      │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2023-29383 
                        │      │                  ├ [6]: https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/cve-2023-29383-abusing-linux-chfn
                        │      │                  │      -to-misrepresent-etc-passwd/ 
                        │      │                  ╰ [7]: https://www.trustwave.com/en-us/resources/security-resources/security-advisories/?fid=31797 
                        │      ├ PublishedDate   : 2023-04-14T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-24T18:05:00Z 
                        ├ [23] ╭ VulnerabilityID : CVE-2023-2603 
                        │      ├ PkgID           : libcap@2.48-8.el9.x86_64 
                        │      ├ PkgName         : libcap 
                        │      ├ InstalledVersion: 2.48-8.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2603 
                        │      ├ Title           : Integer Overflow in _libcap_strdup() 
                        │      ├ Description     : A vulnerability was found in libcap. This issue occurs in the _libcap_strdup() function and can lead to
                        │      │                    an integer overflow if the input string is close to 4GiB. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L 
                        │      │                           ╰ V3Score : 4.4 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-2603 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2209113 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2603 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-2603 
                        │      │                  ├ [4]: https://sites.google.com/site/fullycapable/release-notes-for-libcap#h.iuvg7sbjg8pe 
                        │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-6166-1 
                        │      │                  ├ [6]: https://www.cve.org/CVERecord?id=CVE-2023-2603 
                        │      │                  ├ [7]: https://www.openwall.com/lists/oss-security/2023/05/15/4 
                        │      │                  ╰ [8]: https://www.x41-dsec.de/static/reports/X41-libcap-Code-Review-2023-OSTIF-Final-Report.pdf 
                        │      ├ PublishedDate   : 2023-06-06T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-07T02:45:00Z 
                        ├ [24] ╭ VulnerabilityID : CVE-2023-2602 
                        │      ├ PkgID           : libcap@2.48-8.el9.x86_64 
                        │      ├ PkgName         : libcap 
                        │      ├ InstalledVersion: 2.48-8.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2602 
                        │      ├ Title           : Memory Leak on pthread_create() Error 
                        │      ├ Description     : A vulnerability was found in the pthread_create() function in libcap. This issue may allow a malicious
                        │      │                   actor to use cause __real_pthread_create() to return an error, which can exhaust the process memory.[
                        │      │                   m 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-401 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L 
                        │      │                  │        ╰ V3Score : 3.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L 
                        │      │                           ╰ V3Score : 3.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-2602 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2209114 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2602 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-2602 
                        │      │                  ├ [4]: https://sites.google.com/site/fullycapable/release-notes-for-libcap#h.iuvg7sbjg8pe 
                        │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-6166-1 
                        │      │                  ├ [6]: https://www.cve.org/CVERecord?id=CVE-2023-2602 
                        │      │                  ├ [7]: https://www.openwall.com/lists/oss-security/2023/05/15/4 
                        │      │                  ╰ [8]: https://www.x41-dsec.de/static/reports/X41-libcap-Code-Review-2023-OSTIF-Final-Report.pdf 
                        │      ├ PublishedDate   : 2023-06-06T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-14T18:07:00Z 
                        ├ [25] ╭ VulnerabilityID : CVE-2023-27536 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27536 
                        │      ├ Title           : GSS delegation too eager connection re-use 
                        │      ├ Description     : An authentication bypass vulnerability exists libcurl <8.0.0 in the connection reuse feature which can
                        │      │                   reuse previously established connections with incorrect user permissions due to a failure to check for
                        │      │                   changes in the CURLOPT_GSSAPI_DELEGATION option. This vulnerability affects krb5/kerberos/negotiate/GSSAPI
                        │      │                   transfers and could potentially result in unauthorized access to sensitive information. The safest option is
                        │      │                    to not reuse connections if the CURLOPT_GSSAPI_DELEGATION option has been changed. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-287 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-27536 
                        │      │                  ├ [1] : https://curl.se/docs/CVE-2023-27536.html 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27536 
                        │      │                  ├ [3] : https://hackerone.com/reports/1895135 
                        │      │                  ├ [4] : https://lists.debian.org/debian-lts-announce/2023/04/msg00025.html 
                        │      │                  ├ [5] : https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/3
                        │      │                  │       6NBD5YLJXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-27536 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-20230420-0010/ 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-5964-2 
                        │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2023-27536 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-06T20:34:00Z 
                        ├ [26] ╭ VulnerabilityID : CVE-2023-28321 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28321 
                        │      ├ Title           : IDN wildcard match may lead to Improper Cerificate Validation 
                        │      ├ Description     : An improper certificate validation vulnerability exists in curl <v8.1.0 in the way it supports matching
                        │      │                    of wildcard patterns when listed as "Subject Alternative Name" in TLS server certificates. curl can be
                        │      │                   built to use its own name matching function for TLS rather than one provided by a TLS library. This private
                        │      │                   wildcard matching function would match IDN (International Domain Name) hosts incorrectly and could as a
                        │      │                   result accept patterns that otherwise should mismatch. IDN hostnames are converted to puny code before used
                        │      │                   for certificate checks. Puny coded names always start with `xn--` and should not be allowed to pattern
                        │      │                   match, but the wildcard check in curl could still check for `x*`, which would match even though the IDN name
                        │      │                    most likely contained nothing even resembling an `x`. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-295 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L 
                        │      │                           ╰ V3Score : 5.6 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-28321 
                        │      │                  ├ [1]: https://curl.se/docs/CVE-2023-28321.html 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28321 
                        │      │                  ├ [3]: https://hackerone.com/reports/1950627 
                        │      │                  ├ [4]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/F4
                        │      │                  │      I75RDGX5ULSSCBE5BF3P5I5SFO7ULQ/ 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/Z2
                        │      │                  │      LIWHWKOVH24COGGBCVOWDXXIUPKOMK/ 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-28321 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230609-0009/ 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-28321 
                        │      ├ PublishedDate   : 2023-05-26T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-09T08:15:00Z 
                        ├ [27] ╭ VulnerabilityID : CVE-2023-28322 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28322 
                        │      ├ Title           : more POST-after-PUT confusion 
                        │      ├ Description     : An information disclosure vulnerability exists in curl <v8.1.0 when doing HTTP(S) transfers, libcurl
                        │      │                   might erroneously use the read callback (`CURLOPT_READFUNCTION`) to ask for data to send, even when the
                        │      │                   `CURLOPT_POSTFIELDS` option has been set, if the same handle previously wasused to issue a `PUT` request
                        │      │                   which used that callback. This flaw may surprise the application and cause it to misbehave and either send
                        │      │                   off the wrong data or use memory after free or similar in the second transfer. The problem exists in the
                        │      │                   logic for a reused handle when it is (expected to be) changed from a PUT to a POST. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N 
                        │      │                  │        ╰ V3Score : 9.1 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:L 
                        │      │                           ╰ V3Score : 4.8 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-28322 
                        │      │                  ├ [1]: https://curl.se/docs/CVE-2023-28322.html 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28322 
                        │      │                  ├ [3]: https://hackerone.com/reports/1954658 
                        │      │                  ├ [4]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/F4
                        │      │                  │      I75RDGX5ULSSCBE5BF3P5I5SFO7ULQ/ 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/Z2
                        │      │                  │      LIWHWKOVH24COGGBCVOWDXXIUPKOMK/ 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-28322 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230609-0009/ 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-28322 
                        │      ├ PublishedDate   : 2023-05-26T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-09T08:15:00Z 
                        ├ [28] ╭ VulnerabilityID : CVE-2023-27533 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27533 
                        │      ├ Title           : TELNET option IAC injection 
                        │      ├ Description     : A vulnerability in input validation exists in curl <8.0 during communication using the TELNET protocol
                        │      │                   may allow an attacker to pass on maliciously crafted user name and "telnet options" during server
                        │      │                   negotiation. The lack of proper input scrubbing allows an attacker to send content or perform option
                        │      │                   negotiation without the application's intent. This vulnerability could be exploited if an application allows
                        │      │                    user input, thereby enabling attackers to execute arbitrary code on the system. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 8.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 3.1 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-27533 
                        │      │                  ├ [1] : https://curl.se/docs/CVE-2023-27533.html 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27533 
                        │      │                  ├ [3] : https://hackerone.com/reports/1891474 
                        │      │                  ├ [4] : https://lists.debian.org/debian-lts-announce/2023/04/msg00025.html 
                        │      │                  ├ [5] : https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/3
                        │      │                  │       6NBD5YLJXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-27533 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-20230420-0011/ 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-5964-2 
                        │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2023-27533 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-21T23:15:00Z 
                        ├ [29] ╭ VulnerabilityID : CVE-2023-27534 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27534 
                        │      ├ Title           : SFTP path ~ resolving discrepancy 
                        │      ├ Description     : A path traversal vulnerability exists in curl <8.0.0 SFTP implementation causes the tilde (~) character
                        │      │                    to be wrongly replaced when used as a prefix in the first path element, in addition to its intended use as
                        │      │                   the first element to indicate a path relative to the user's home directory. Attackers can exploit this flaw
                        │      │                   to bypass filtering or execute arbitrary code by crafting a path like /~2/foo while accessing a server with
                        │      │                   a specific user. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-22 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 8.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N 
                        │      │                           ╰ V3Score : 3.7 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-27534 
                        │      │                  ├ [1]: https://curl.se/docs/CVE-2023-27534.html 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27534 
                        │      │                  ├ [3]: https://hackerone.com/reports/1892351 
                        │      │                  ├ [4]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/36
                        │      │                  │      NBD5YLJXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-27534 
                        │      │                  ├ [6]: https://security.netapp.com/advisory/ntap-20230420-0012/ 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-27534 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-20T09:15:00Z 
                        ├ [30] ╭ VulnerabilityID : CVE-2023-27538 
                        │      ├ PkgID           : libcurl-minimal@7.76.1-23.el9_2.1.x86_64 
                        │      ├ PkgName         : libcurl-minimal 
                        │      ├ InstalledVersion: 7.76.1-23.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27538 
                        │      ├ Title           : SSH connection too eager reuse still 
                        │      ├ Description     : An authentication bypass vulnerability exists in libcurl prior to v8.0.0 where it reuses a previously
                        │      │                   established SSH connection despite the fact that an SSH option was modified, which should have prevented
                        │      │                   reuse. libcurl maintains a pool of previously used connections to reuse them for subsequent transfers if the
                        │      │                    configurations match. However, two SSH settings were omitted from the configuration check, allowing them to
                        │      │                    match easily, potentially leading to the reuse of an inappropriate connection. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-287 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-27538 
                        │      │                  ├ [1]: https://curl.se/docs/CVE-2023-27538.html 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27538 
                        │      │                  ├ [3]: https://hackerone.com/reports/1898475 
                        │      │                  ├ [4]: https://lists.debian.org/debian-lts-announce/2023/04/msg00025.html 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/36
                        │      │                  │      NBD5YLJXXEDZLDGNFCERWRYJQ6LAQW/ 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-27538 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230420-0010/ 
                        │      │                  ├ [8]: https://ubuntu.com/security/notices/USN-5964-1 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-27538 
                        │      ├ PublishedDate   : 2023-03-30T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-21T23:15:00Z 
                        ├ [31] ╭ VulnerabilityID : CVE-2023-22652 
                        │      ├ PkgID           : libeconf@0.4.1-2.el9.x86_64 
                        │      ├ PkgName         : libeconf 
                        │      ├ InstalledVersion: 0.4.1-2.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-22652 
                        │      ├ Title           : stack-based buffer overflow in read_file() in lib/getfilecontents.c 
                        │      ├ Description     : A Buffer Copy without Checking Size of Input ('Classic Buffer Overflow') vulnerability in openSUSE
                        │      │                   libeconf leads to DoS via malformed config files.
                        │      │                   This issue affects libeconf: before 0.5.2.
                        │      │                   
                        │      │                    
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-120 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-22652 
                        │      │                  ├ [1]: https://bugzilla.suse.com/show_bug.cgi?id=CVE-2023-22652 
                        │      │                  ├ [2]: https://https://github.com/openSUSE/libeconf/issues/177 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-22652 
                        │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2023-22652 
                        │      ├ PublishedDate   : 2023-06-01T12:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-08T18:29:00Z 
                        ├ [32] ╭ VulnerabilityID : CVE-2022-27943 
                        │      ├ PkgID           : libgcc@11.3.1-4.3.el9.x86_64 
                        │      ├ PkgName         : libgcc 
                        │      ├ InstalledVersion: 11.3.1-4.3.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-27943 
                        │      ├ Title           : libiberty/rust-demangle.c in GNU GCC 11.2 allows stack exhaustion in demangle_const 
                        │      ├ Description     : libiberty/rust-demangle.c in GNU GCC 11.2 allows stack consumption in demangle_const, as demonstrated
                        │      │                   by nm-new. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-400 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                  │        ├ V2Score : 4.3 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-27943 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27943 
                        │      │                  ├ [2]: https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105039 
                        │      │                  ├ [3]: https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=9234cdca6ee88badfc00297e72f13dac4e540c79 
                        │      │                  ├ [4]: https://gcc.gnu.org/pipermail/gcc-patches/2022-March/592244.html 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/H4
                        │      │                  │      24YXGW7OKXS2NCAP35OP6Y4P4AW6VG/ 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2022-27943 
                        │      │                  ├ [7]: https://sourceware.org/bugzilla/show_bug.cgi?id=28995 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2022-27943 
                        │      ├ PublishedDate   : 2022-03-26T13:15:00Z 
                        │      ╰ LastModifiedDate: 2022-12-22T20:29:00Z 
                        ├ [33] ╭ VulnerabilityID : CVE-2023-29383 
                        │      ├ PkgID           : libmount@2.37.4-11.el9_2.x86_64 
                        │      ├ PkgName         : libmount 
                        │      ├ InstalledVersion: 2.37.4-11.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-29383 
                        │      ├ Title           : Improper input validation in shadow-utils package utility chfn 
                        │      ├ Description     : In Shadow 4.13, it is possible to inject control characters into fields provided to the SUID program
                        │      │                   chfn (change finger). Although it is not possible to exploit this directly (e.g., adding a new user fails
                        │      │                   because \n is in the block list), it is possible to misrepresent the /etc/passwd file when viewed. Use of \r
                        │      │                    manipulations and Unicode characters to work around blocking of the : character make it possible to give
                        │      │                   the impression that a new user has been added. In other words, an adversary may be able to convince a system
                        │      │                    administrator to take the system offline (an indirect, social-engineered denial of service) by
                        │      │                   demonstrating that "cat /etc/passwd" shows a rogue user account. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 3.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-29383 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29383 
                        │      │                  ├ [2]: https://github.com/shadow-maint/shadow/commit/e5905c4b84d4fb90aefcd96ee618411ebfac663d 
                        │      │                  ├ [3]: https://github.com/shadow-maint/shadow/pull/687 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-29383 
                        │      │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2023-29383 
                        │      │                  ├ [6]: https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/cve-2023-29383-abusing-linux-chfn
                        │      │                  │      -to-misrepresent-etc-passwd/ 
                        │      │                  ╰ [7]: https://www.trustwave.com/en-us/resources/security-resources/security-advisories/?fid=31797 
                        │      ├ PublishedDate   : 2023-04-14T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-24T18:05:00Z 
                        ├ [34] ╭ VulnerabilityID : CVE-2018-14048 
                        │      ├ PkgID           : libpng@1.6.37-12.el9.x86_64 
                        │      ├ PkgName         : libpng 
                        │      ├ InstalledVersion: 2:1.6.37-12.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2018-14048 
                        │      ├ Title           : libpng: Segmentation fault in png.c:png_free_data function causing denial of service 
                        │      ├ Description     : An issue has been found in libpng 1.6.34. It is a SEGV in the function png_free_data in png.c, related
                        │      │                   to the recommended error handling for png_read_image. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                  │        ├ V2Score : 4.3 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.0/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L 
                        │      │                           ╰ V3Score : 3.3 
                        │      ├ References       ╭ [0] : http://packetstormsecurity.com/files/152561/Slackware-Security-Advisory-libpng-Updates.html 
                        │      │                  ├ [1] : http://www.oracle.com/technetwork/security-advisory/cpuoct2018-4428296.html 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2018-14048 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-14048 
                        │      │                  ├ [4] : https://github.com/fouzhe/security/tree/master/libpng 
                        │      │                  ├ [5] : https://github.com/glennrp/libpng/issues/238 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2018-14048 
                        │      │                  ├ [7] : https://seclists.org/bugtraq/2019/Apr/30 
                        │      │                  ├ [8] : https://security.gentoo.org/glsa/201908-02 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-5432-1 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-5432-2 
                        │      │                  ╰ [11]: https://www.cve.org/CVERecord?id=CVE-2018-14048 
                        │      ├ PublishedDate   : 2018-07-13T16:29:00Z 
                        │      ╰ LastModifiedDate: 2022-06-27T17:35:00Z 
                        ├ [35] ╭ VulnerabilityID : CVE-2022-3857 
                        │      ├ PkgID           : libpng@1.6.37-12.el9.x86_64 
                        │      ├ PkgName         : libpng 
                        │      ├ InstalledVersion: 2:1.6.37-12.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-3857 
                        │      ├ Title           : Null pointer dereference leads to segmentation fault 
                        │      ├ Description     : A flaw was found in libpng 1.6.38. A crafted PNG image can lead to a segmentation fault and denial of
                        │      │                   service in png_setup_paeth_row() function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-476 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-3857 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3857 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2022-3857 
                        │      │                  ├ [3]: https://security.netapp.com/advisory/ntap-20230406-0004/ 
                        │      │                  ├ [4]: https://sourceforge.net/p/libpng/bugs/300/ 
                        │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2022-3857 
                        │      ├ PublishedDate   : 2023-03-06T23:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-06T13:15:00Z 
                        ├ [36] ╭ VulnerabilityID : CVE-2023-29383 
                        │      ├ PkgID           : libsmartcols@2.37.4-11.el9_2.x86_64 
                        │      ├ PkgName         : libsmartcols 
                        │      ├ InstalledVersion: 2.37.4-11.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-29383 
                        │      ├ Title           : Improper input validation in shadow-utils package utility chfn 
                        │      ├ Description     : In Shadow 4.13, it is possible to inject control characters into fields provided to the SUID program
                        │      │                   chfn (change finger). Although it is not possible to exploit this directly (e.g., adding a new user fails
                        │      │                   because \n is in the block list), it is possible to misrepresent the /etc/passwd file when viewed. Use of \r
                        │      │                    manipulations and Unicode characters to work around blocking of the : character make it possible to give
                        │      │                   the impression that a new user has been added. In other words, an adversary may be able to convince a system
                        │      │                    administrator to take the system offline (an indirect, social-engineered denial of service) by
                        │      │                   demonstrating that "cat /etc/passwd" shows a rogue user account. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 3.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-29383 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29383 
                        │      │                  ├ [2]: https://github.com/shadow-maint/shadow/commit/e5905c4b84d4fb90aefcd96ee618411ebfac663d 
                        │      │                  ├ [3]: https://github.com/shadow-maint/shadow/pull/687 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-29383 
                        │      │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2023-29383 
                        │      │                  ├ [6]: https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/cve-2023-29383-abusing-linux-chfn
                        │      │                  │      -to-misrepresent-etc-passwd/ 
                        │      │                  ╰ [7]: https://www.trustwave.com/en-us/resources/security-resources/security-advisories/?fid=31797 
                        │      ├ PublishedDate   : 2023-04-14T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-24T18:05:00Z 
                        ├ [37] ╭ VulnerabilityID : CVE-2022-27943 
                        │      ├ PkgID           : libstdc++@11.3.1-4.3.el9.x86_64 
                        │      ├ PkgName         : libstdc++ 
                        │      ├ InstalledVersion: 11.3.1-4.3.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-27943 
                        │      ├ Title           : libiberty/rust-demangle.c in GNU GCC 11.2 allows stack exhaustion in demangle_const 
                        │      ├ Description     : libiberty/rust-demangle.c in GNU GCC 11.2 allows stack consumption in demangle_const, as demonstrated
                        │      │                   by nm-new. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-400 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                  │        ├ V2Score : 4.3 
                        │      │                  │        ╰ V3Score : 5.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-27943 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27943 
                        │      │                  ├ [2]: https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105039 
                        │      │                  ├ [3]: https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=9234cdca6ee88badfc00297e72f13dac4e540c79 
                        │      │                  ├ [4]: https://gcc.gnu.org/pipermail/gcc-patches/2022-March/592244.html 
                        │      │                  ├ [5]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/H4
                        │      │                  │      24YXGW7OKXS2NCAP35OP6Y4P4AW6VG/ 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2022-27943 
                        │      │                  ├ [7]: https://sourceware.org/bugzilla/show_bug.cgi?id=28995 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2022-27943 
                        │      ├ PublishedDate   : 2022-03-26T13:15:00Z 
                        │      ╰ LastModifiedDate: 2022-12-22T20:29:00Z 
                        ├ [38] ╭ VulnerabilityID : CVE-2023-29383 
                        │      ├ PkgID           : libuuid@2.37.4-11.el9_2.x86_64 
                        │      ├ PkgName         : libuuid 
                        │      ├ InstalledVersion: 2.37.4-11.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-29383 
                        │      ├ Title           : Improper input validation in shadow-utils package utility chfn 
                        │      ├ Description     : In Shadow 4.13, it is possible to inject control characters into fields provided to the SUID program
                        │      │                   chfn (change finger). Although it is not possible to exploit this directly (e.g., adding a new user fails
                        │      │                   because \n is in the block list), it is possible to misrepresent the /etc/passwd file when viewed. Use of \r
                        │      │                    manipulations and Unicode characters to work around blocking of the : character make it possible to give
                        │      │                   the impression that a new user has been added. In other words, an adversary may be able to convince a system
                        │      │                    administrator to take the system offline (an indirect, social-engineered denial of service) by
                        │      │                   demonstrating that "cat /etc/passwd" shows a rogue user account. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 3.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-29383 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29383 
                        │      │                  ├ [2]: https://github.com/shadow-maint/shadow/commit/e5905c4b84d4fb90aefcd96ee618411ebfac663d 
                        │      │                  ├ [3]: https://github.com/shadow-maint/shadow/pull/687 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-29383 
                        │      │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2023-29383 
                        │      │                  ├ [6]: https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/cve-2023-29383-abusing-linux-chfn
                        │      │                  │      -to-misrepresent-etc-passwd/ 
                        │      │                  ╰ [7]: https://www.trustwave.com/en-us/resources/security-resources/security-advisories/?fid=31797 
                        │      ├ PublishedDate   : 2023-04-14T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-24T18:05:00Z 
                        ├ [39] ╭ VulnerabilityID : CVE-2023-28484 
                        │      ├ PkgID           : libxml2@2.9.13-3.el9_1.x86_64 
                        │      ├ PkgName         : libxml2 
                        │      ├ InstalledVersion: 2.9.13-3.el9_1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28484 
                        │      ├ Title           : NULL dereference in xmlSchemaFixupComplexType 
                        │      ├ Description     : In libxml2 before 2.10.4, parsing of certain invalid XSD schemas can lead to a NULL pointer dereference
                        │      │                    and subsequently a segfault. This occurs in xmlSchemaFixupComplexType in xmlschemas.c. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-476 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-28484 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28484 
                        │      │                  ├ [2] : https://gitlab.gnome.org/GNOME/libxml2/-/commit/4c6922f763ad958c48ff66f82823ae21f2e92ee6 
                        │      │                  ├ [3] : https://gitlab.gnome.org/GNOME/libxml2/-/commit/647e072ea0a2f12687fa05c172f4c4713fdb0c4f 
                        │      │                  ├ [4] : https://gitlab.gnome.org/GNOME/libxml2/-/issues/491 
                        │      │                  ├ [5] : https://gitlab.gnome.org/GNOME/libxml2/-/releases/v2.10.4 
                        │      │                  ├ [6] : https://lists.debian.org/debian-lts-announce/2023/04/msg00031.html 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2023-28484 
                        │      │                  ├ [8] : https://security.netapp.com/advisory/ntap-20230601-0006/ 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-6028-1 
                        │      │                  ╰ [10]: https://www.cve.org/CVERecord?id=CVE-2023-28484 
                        │      ├ PublishedDate   : 2023-04-24T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-01T14:15:00Z 
                        ├ [40] ╭ VulnerabilityID : CVE-2023-29469 
                        │      ├ PkgID           : libxml2@2.9.13-3.el9_1.x86_64 
                        │      ├ PkgName         : libxml2 
                        │      ├ InstalledVersion: 2.9.13-3.el9_1 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-29469 
                        │      ├ Title           : Hashing of empty dict strings isn't deterministic 
                        │      ├ Description     : An issue was discovered in libxml2 before 2.10.4. When hashing empty dict strings in a crafted XML
                        │      │                   document, xmlDictComputeFastKey in dict.c can produce non-deterministic values, leading to various logic and
                        │      │                    memory errors, such as a double free. This behavior occurs because there is an attempt to use the first
                        │      │                   byte of an empty string, and any value is possible (not solely the '\0' value). 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-415 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 6.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-29469 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29469 
                        │      │                  ├ [2]: https://gitlab.gnome.org/GNOME/libxml2/-/commit/09a2dd453007f9c7205274623acdd73747c22d64 
                        │      │                  ├ [3]: https://gitlab.gnome.org/GNOME/libxml2/-/issues/510 
                        │      │                  ├ [4]: https://gitlab.gnome.org/GNOME/libxml2/-/releases/v2.10.4 
                        │      │                  ├ [5]: https://lists.debian.org/debian-lts-announce/2023/04/msg00031.html 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-29469 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230601-0006/ 
                        │      │                  ├ [8]: https://ubuntu.com/security/notices/USN-6028-1 
                        │      │                  ╰ [9]: https://www.cve.org/CVERecord?id=CVE-2023-29469 
                        │      ├ PublishedDate   : 2023-04-24T21:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-01T14:15:00Z 
                        ├ [41] ╭ VulnerabilityID : CVE-2022-4899 
                        │      ├ PkgID           : libzstd@1.5.1-2.el9.x86_64 
                        │      ├ PkgName         : libzstd 
                        │      ├ InstalledVersion: 1.5.1-2.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-4899 
                        │      ├ Title           : buffer overrun in util.c 
                        │      ├ Description     : A vulnerability was found in zstd v1.4.10, where an attacker can supply empty string as an argument to
                        │      │                   the command line tool to cause buffer overrun. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-400 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2022-4899 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4899 
                        │      │                  ├ [2]: https://github.com/facebook/zstd/issues/3200 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2022-4899 
                        │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2022-4899 
                        │      ├ PublishedDate   : 2023-03-31T20:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-07T01:19:00Z 
                        ├ [42] ╭ VulnerabilityID : CVE-2023-29491 
                        │      ├ PkgID           : ncurses-base@6.2-8.20210508.el9.noarch 
                        │      ├ PkgName         : ncurses-base 
                        │      ├ InstalledVersion: 6.2-8.20210508.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-29491 
                        │      ├ Title           : Local users can trigger security-relevant memory corruption via malformed data 
                        │      ├ Description     : ncurses before 6.4 20230408, when used by a setuid application, allows local users to trigger
                        │      │                   security-relevant memory corruption via malformed data in a terminfo database file that is found in
                        │      │                   $HOME/.terminfo or reached via the TERMINFO or TERM environment variable. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-787 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 7.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H 
                        │      │                           ╰ V3Score : 7 
                        │      ├ References       ╭ [0] : http://ncurses.scripts.mit.edu/?p=ncurses.git;a=commit;h=eb51b1ea1f75a0ec17c9c5937cb28df1e8eeec56 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/04/19/10 
                        │      │                  ├ [2] : http://www.openwall.com/lists/oss-security/2023/04/19/11 
                        │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2023-29491 
                        │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29491 
                        │      │                  ├ [5] : https://invisible-island.net/ncurses/NEWS.html#index-t20230408 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-29491 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-20230517-0009/ 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-6099-1 
                        │      │                  ├ [9] : https://www.cve.org/CVERecord?id=CVE-2023-29491 
                        │      │                  ├ [10]: https://www.openwall.com/lists/oss-security/2023/04/12/5 
                        │      │                  ╰ [11]: https://www.openwall.com/lists/oss-security/2023/04/13/4 
                        │      ├ PublishedDate   : 2023-04-14T01:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-17T20:15:00Z 
                        ├ [43] ╭ VulnerabilityID : CVE-2022-29458 
                        │      ├ PkgID           : ncurses-base@6.2-8.20210508.el9.noarch 
                        │      ├ PkgName         : ncurses-base 
                        │      ├ InstalledVersion: 6.2-8.20210508.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-29458 
                        │      ├ Title           : ncurses: segfaulting OOB read 
                        │      ├ Description     : ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in
                        │      │                   convert_strings in tinfo/read_entry.c in the terminfo library. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-125 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:P/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:H 
                        │      │                  │        ├ V2Score : 5.8 
                        │      │                  │        ╰ V3Score : 7.1 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:H 
                        │      │                           ╰ V3Score : 6.1 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2022/Oct/41 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2022-29458 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29458 
                        │      │                  ├ [3] : https://invisible-island.net/ncurses/NEWS.html#t20220416 
                        │      │                  ├ [4] : https://lists.debian.org/debian-lts-announce/2022/10/msg00037.html 
                        │      │                  ├ [5] : https://lists.gnu.org/archive/html/bug-ncurses/2022-04/msg00014.html 
                        │      │                  ├ [6] : https://lists.gnu.org/archive/html/bug-ncurses/2022-04/msg00016.html 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2022-29458 
                        │      │                  ├ [8] : https://support.apple.com/kb/HT213488 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-5477-1 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-6099-1 
                        │      │                  ╰ [11]: https://www.cve.org/CVERecord?id=CVE-2022-29458 
                        │      ├ PublishedDate   : 2022-04-18T21:15:00Z 
                        │      ╰ LastModifiedDate: 2022-11-08T19:46:00Z 
                        ├ [44] ╭ VulnerabilityID : CVE-2023-29491 
                        │      ├ PkgID           : ncurses-libs@6.2-8.20210508.el9.x86_64 
                        │      ├ PkgName         : ncurses-libs 
                        │      ├ InstalledVersion: 6.2-8.20210508.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-29491 
                        │      ├ Title           : Local users can trigger security-relevant memory corruption via malformed data 
                        │      ├ Description     : ncurses before 6.4 20230408, when used by a setuid application, allows local users to trigger
                        │      │                   security-relevant memory corruption via malformed data in a terminfo database file that is found in
                        │      │                   $HOME/.terminfo or reached via the TERMINFO or TERM environment variable. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-787 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 7.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H 
                        │      │                           ╰ V3Score : 7 
                        │      ├ References       ╭ [0] : http://ncurses.scripts.mit.edu/?p=ncurses.git;a=commit;h=eb51b1ea1f75a0ec17c9c5937cb28df1e8eeec56 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2023/04/19/10 
                        │      │                  ├ [2] : http://www.openwall.com/lists/oss-security/2023/04/19/11 
                        │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2023-29491 
                        │      │                  ├ [4] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29491 
                        │      │                  ├ [5] : https://invisible-island.net/ncurses/NEWS.html#index-t20230408 
                        │      │                  ├ [6] : https://nvd.nist.gov/vuln/detail/CVE-2023-29491 
                        │      │                  ├ [7] : https://security.netapp.com/advisory/ntap-20230517-0009/ 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-6099-1 
                        │      │                  ├ [9] : https://www.cve.org/CVERecord?id=CVE-2023-29491 
                        │      │                  ├ [10]: https://www.openwall.com/lists/oss-security/2023/04/12/5 
                        │      │                  ╰ [11]: https://www.openwall.com/lists/oss-security/2023/04/13/4 
                        │      ├ PublishedDate   : 2023-04-14T01:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-17T20:15:00Z 
                        ├ [45] ╭ VulnerabilityID : CVE-2022-29458 
                        │      ├ PkgID           : ncurses-libs@6.2-8.20210508.el9.x86_64 
                        │      ├ PkgName         : ncurses-libs 
                        │      ├ InstalledVersion: 6.2-8.20210508.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-29458 
                        │      ├ Title           : ncurses: segfaulting OOB read 
                        │      ├ Description     : ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in
                        │      │                   convert_strings in tinfo/read_entry.c in the terminfo library. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-125 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:P/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:H 
                        │      │                  │        ├ V2Score : 5.8 
                        │      │                  │        ╰ V3Score : 7.1 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:H 
                        │      │                           ╰ V3Score : 6.1 
                        │      ├ References       ╭ [0] : http://seclists.org/fulldisclosure/2022/Oct/41 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2022-29458 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29458 
                        │      │                  ├ [3] : https://invisible-island.net/ncurses/NEWS.html#t20220416 
                        │      │                  ├ [4] : https://lists.debian.org/debian-lts-announce/2022/10/msg00037.html 
                        │      │                  ├ [5] : https://lists.gnu.org/archive/html/bug-ncurses/2022-04/msg00014.html 
                        │      │                  ├ [6] : https://lists.gnu.org/archive/html/bug-ncurses/2022-04/msg00016.html 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2022-29458 
                        │      │                  ├ [8] : https://support.apple.com/kb/HT213488 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-5477-1 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-6099-1 
                        │      │                  ╰ [11]: https://www.cve.org/CVERecord?id=CVE-2022-29458 
                        │      ├ PublishedDate   : 2022-04-18T21:15:00Z 
                        │      ╰ LastModifiedDate: 2022-11-08T19:46:00Z 
                        ├ [46] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nspr@4.34.0-18.el9_1.x86_64 
                        │      ├ PkgName         : nspr 
                        │      ├ InstalledVersion: 4.34.0-18.el9_1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : nss: Information exposure when DH secret are reused across multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE ciphersuites inherit in the TLS specification. To mitigate
                        │      │                    this vulnerability, Firefox disabled support for DHE ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : Attack: 
                        │      │                  ├ [1] : Brinkmann, 
                        │      │                  ├ [2] : Explanation 
                        │      │                  ├ [3] : Exploiting 
                        │      │                  ├ [4] : Finding 
                        │      │                  ├ [5] : Marcus 
                        │      │                  ├ [6] : Merget, 
                        │      │                  ├ [7] : Most-Significant-Bit-Oracles 
                        │      │                  ├ [8] : Raccoon 
                        │      │                  ├ [9] : Robert 
                        │      │                  ├ [10]: TLS-DH(E) 
                        │      │                  ├ [11]: Thorough 
                        │      │                  ├ [12]: al. 
                        │      │                  ├ [13]: and 
                        │      │                  ├ [14]: be 
                        │      │                  ├ [15]: by 
                        │      │                  ├ [16]: can 
                        │      │                  ├ [17]: et 
                        │      │                  ├ [18]: found: 
                        │      │                  ├ [19]: https://access.redhat.com/security/cve/CVE-2020-12413 
                        │      │                  ├ [20]: https://bugzilla.mozilla.org/show_bug.cgi?id=CVE-2020-12413 
                        │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2020-12413 
                        │      │                  ├ [22]: https://raccoon-attack.com/ 
                        │      │                  ├ [23]: https://raccoon-attack.com/RacoonAttack.pdf 
                        │      │                  ├ [24]: https://www.cve.org/CVERecord?id=CVE-2020-12413 
                        │      │                  ╰ [25]: in 
                        │      ├ PublishedDate   : 2023-02-16T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:00Z 
                        ├ [47] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss@3.79.0-18.el9_1.x86_64 
                        │      ├ PkgName         : nss 
                        │      ├ InstalledVersion: 3.79.0-18.el9_1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : nss: Information exposure when DH secret are reused across multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE ciphersuites inherit in the TLS specification. To mitigate
                        │      │                    this vulnerability, Firefox disabled support for DHE ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : Attack: 
                        │      │                  ├ [1] : Brinkmann, 
                        │      │                  ├ [2] : Explanation 
                        │      │                  ├ [3] : Exploiting 
                        │      │                  ├ [4] : Finding 
                        │      │                  ├ [5] : Marcus 
                        │      │                  ├ [6] : Merget, 
                        │      │                  ├ [7] : Most-Significant-Bit-Oracles 
                        │      │                  ├ [8] : Raccoon 
                        │      │                  ├ [9] : Robert 
                        │      │                  ├ [10]: TLS-DH(E) 
                        │      │                  ├ [11]: Thorough 
                        │      │                  ├ [12]: al. 
                        │      │                  ├ [13]: and 
                        │      │                  ├ [14]: be 
                        │      │                  ├ [15]: by 
                        │      │                  ├ [16]: can 
                        │      │                  ├ [17]: et 
                        │      │                  ├ [18]: found: 
                        │      │                  ├ [19]: https://access.redhat.com/security/cve/CVE-2020-12413 
                        │      │                  ├ [20]: https://bugzilla.mozilla.org/show_bug.cgi?id=CVE-2020-12413 
                        │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2020-12413 
                        │      │                  ├ [22]: https://raccoon-attack.com/ 
                        │      │                  ├ [23]: https://raccoon-attack.com/RacoonAttack.pdf 
                        │      │                  ├ [24]: https://www.cve.org/CVERecord?id=CVE-2020-12413 
                        │      │                  ╰ [25]: in 
                        │      ├ PublishedDate   : 2023-02-16T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:00Z 
                        ├ [48] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss-softokn@3.79.0-18.el9_1.x86_64 
                        │      ├ PkgName         : nss-softokn 
                        │      ├ InstalledVersion: 3.79.0-18.el9_1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : nss: Information exposure when DH secret are reused across multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE ciphersuites inherit in the TLS specification. To mitigate
                        │      │                    this vulnerability, Firefox disabled support for DHE ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : Attack: 
                        │      │                  ├ [1] : Brinkmann, 
                        │      │                  ├ [2] : Explanation 
                        │      │                  ├ [3] : Exploiting 
                        │      │                  ├ [4] : Finding 
                        │      │                  ├ [5] : Marcus 
                        │      │                  ├ [6] : Merget, 
                        │      │                  ├ [7] : Most-Significant-Bit-Oracles 
                        │      │                  ├ [8] : Raccoon 
                        │      │                  ├ [9] : Robert 
                        │      │                  ├ [10]: TLS-DH(E) 
                        │      │                  ├ [11]: Thorough 
                        │      │                  ├ [12]: al. 
                        │      │                  ├ [13]: and 
                        │      │                  ├ [14]: be 
                        │      │                  ├ [15]: by 
                        │      │                  ├ [16]: can 
                        │      │                  ├ [17]: et 
                        │      │                  ├ [18]: found: 
                        │      │                  ├ [19]: https://access.redhat.com/security/cve/CVE-2020-12413 
                        │      │                  ├ [20]: https://bugzilla.mozilla.org/show_bug.cgi?id=CVE-2020-12413 
                        │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2020-12413 
                        │      │                  ├ [22]: https://raccoon-attack.com/ 
                        │      │                  ├ [23]: https://raccoon-attack.com/RacoonAttack.pdf 
                        │      │                  ├ [24]: https://www.cve.org/CVERecord?id=CVE-2020-12413 
                        │      │                  ╰ [25]: in 
                        │      ├ PublishedDate   : 2023-02-16T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:00Z 
                        ├ [49] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss-softokn-freebl@3.79.0-18.el9_1.x86_64 
                        │      ├ PkgName         : nss-softokn-freebl 
                        │      ├ InstalledVersion: 3.79.0-18.el9_1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : nss: Information exposure when DH secret are reused across multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE ciphersuites inherit in the TLS specification. To mitigate
                        │      │                    this vulnerability, Firefox disabled support for DHE ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : Attack: 
                        │      │                  ├ [1] : Brinkmann, 
                        │      │                  ├ [2] : Explanation 
                        │      │                  ├ [3] : Exploiting 
                        │      │                  ├ [4] : Finding 
                        │      │                  ├ [5] : Marcus 
                        │      │                  ├ [6] : Merget, 
                        │      │                  ├ [7] : Most-Significant-Bit-Oracles 
                        │      │                  ├ [8] : Raccoon 
                        │      │                  ├ [9] : Robert 
                        │      │                  ├ [10]: TLS-DH(E) 
                        │      │                  ├ [11]: Thorough 
                        │      │                  ├ [12]: al. 
                        │      │                  ├ [13]: and 
                        │      │                  ├ [14]: be 
                        │      │                  ├ [15]: by 
                        │      │                  ├ [16]: can 
                        │      │                  ├ [17]: et 
                        │      │                  ├ [18]: found: 
                        │      │                  ├ [19]: https://access.redhat.com/security/cve/CVE-2020-12413 
                        │      │                  ├ [20]: https://bugzilla.mozilla.org/show_bug.cgi?id=CVE-2020-12413 
                        │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2020-12413 
                        │      │                  ├ [22]: https://raccoon-attack.com/ 
                        │      │                  ├ [23]: https://raccoon-attack.com/RacoonAttack.pdf 
                        │      │                  ├ [24]: https://www.cve.org/CVERecord?id=CVE-2020-12413 
                        │      │                  ╰ [25]: in 
                        │      ├ PublishedDate   : 2023-02-16T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:00Z 
                        ├ [50] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss-sysinit@3.79.0-18.el9_1.x86_64 
                        │      ├ PkgName         : nss-sysinit 
                        │      ├ InstalledVersion: 3.79.0-18.el9_1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : nss: Information exposure when DH secret are reused across multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE ciphersuites inherit in the TLS specification. To mitigate
                        │      │                    this vulnerability, Firefox disabled support for DHE ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : Attack: 
                        │      │                  ├ [1] : Brinkmann, 
                        │      │                  ├ [2] : Explanation 
                        │      │                  ├ [3] : Exploiting 
                        │      │                  ├ [4] : Finding 
                        │      │                  ├ [5] : Marcus 
                        │      │                  ├ [6] : Merget, 
                        │      │                  ├ [7] : Most-Significant-Bit-Oracles 
                        │      │                  ├ [8] : Raccoon 
                        │      │                  ├ [9] : Robert 
                        │      │                  ├ [10]: TLS-DH(E) 
                        │      │                  ├ [11]: Thorough 
                        │      │                  ├ [12]: al. 
                        │      │                  ├ [13]: and 
                        │      │                  ├ [14]: be 
                        │      │                  ├ [15]: by 
                        │      │                  ├ [16]: can 
                        │      │                  ├ [17]: et 
                        │      │                  ├ [18]: found: 
                        │      │                  ├ [19]: https://access.redhat.com/security/cve/CVE-2020-12413 
                        │      │                  ├ [20]: https://bugzilla.mozilla.org/show_bug.cgi?id=CVE-2020-12413 
                        │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2020-12413 
                        │      │                  ├ [22]: https://raccoon-attack.com/ 
                        │      │                  ├ [23]: https://raccoon-attack.com/RacoonAttack.pdf 
                        │      │                  ├ [24]: https://www.cve.org/CVERecord?id=CVE-2020-12413 
                        │      │                  ╰ [25]: in 
                        │      ├ PublishedDate   : 2023-02-16T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:00Z 
                        ├ [51] ╭ VulnerabilityID : CVE-2020-12413 
                        │      ├ PkgID           : nss-util@3.79.0-18.el9_1.x86_64 
                        │      ├ PkgName         : nss-util 
                        │      ├ InstalledVersion: 3.79.0-18.el9_1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2020-12413 
                        │      ├ Title           : nss: Information exposure when DH secret are reused across multiple TLS connections 
                        │      ├ Description     : The Raccoon attack is a timing attack on DHE ciphersuites inherit in the TLS specification. To mitigate
                        │      │                    this vulnerability, Firefox disabled support for DHE ciphersuites. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-203 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : Attack: 
                        │      │                  ├ [1] : Brinkmann, 
                        │      │                  ├ [2] : Explanation 
                        │      │                  ├ [3] : Exploiting 
                        │      │                  ├ [4] : Finding 
                        │      │                  ├ [5] : Marcus 
                        │      │                  ├ [6] : Merget, 
                        │      │                  ├ [7] : Most-Significant-Bit-Oracles 
                        │      │                  ├ [8] : Raccoon 
                        │      │                  ├ [9] : Robert 
                        │      │                  ├ [10]: TLS-DH(E) 
                        │      │                  ├ [11]: Thorough 
                        │      │                  ├ [12]: al. 
                        │      │                  ├ [13]: and 
                        │      │                  ├ [14]: be 
                        │      │                  ├ [15]: by 
                        │      │                  ├ [16]: can 
                        │      │                  ├ [17]: et 
                        │      │                  ├ [18]: found: 
                        │      │                  ├ [19]: https://access.redhat.com/security/cve/CVE-2020-12413 
                        │      │                  ├ [20]: https://bugzilla.mozilla.org/show_bug.cgi?id=CVE-2020-12413 
                        │      │                  ├ [21]: https://nvd.nist.gov/vuln/detail/CVE-2020-12413 
                        │      │                  ├ [22]: https://raccoon-attack.com/ 
                        │      │                  ├ [23]: https://raccoon-attack.com/RacoonAttack.pdf 
                        │      │                  ├ [24]: https://www.cve.org/CVERecord?id=CVE-2020-12413 
                        │      │                  ╰ [25]: in 
                        │      ├ PublishedDate   : 2023-02-16T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-28T19:49:00Z 
                        ├ [52] ╭ VulnerabilityID : CVE-2021-27212 
                        │      ├ PkgID           : openldap@2.6.2-3.el9.x86_64 
                        │      ├ PkgName         : openldap 
                        │      ├ InstalledVersion: 2.6.2-3.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-27212 
                        │      ├ Title           : openldap: Assertion failure in slapd in the issuerAndThisUpdateCheck function 
                        │      ├ Description     : In OpenLDAP through 2.4.57 and 2.5.x through 2.5.1alpha, an assertion failure in slapd can occur in the
                        │      │                    issuerAndThisUpdateCheck function via a crafted packet, resulting in a denial of service (daemon exit) via
                        │      │                   a short timestamp. This is related to schema_init.c and checkTime. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-617 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ├ V2Score : 5 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2021-27212 
                        │      │                  ├ [1] : https://bugs.openldap.org/show_bug.cgi?id=9454 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27212 
                        │      │                  ├ [3] : https://git.openldap.org/openldap/openldap/-/commit/3539fc33212b528c56b716584f2c2994af7c30b0 
                        │      │                  ├ [4] : https://git.openldap.org/openldap/openldap/-/commit/9badb73425a67768c09bcaed1a9c26c684af6c30 
                        │      │                  ├ [5] : https://lists.apache.org/thread.html/r58af02e294bd07f487e2c64ffc0a29b837db5600e33b6e698b9d696b@%
                        │      │                  │       3Cissues.bookkeeper.apache.org%3E 
                        │      │                  ├ [6] : https://lists.apache.org/thread.html/rf4c02775860db415b4955778a131c2795223f61cb8c6a450893651e4@%
                        │      │                  │       3Cissues.bookkeeper.apache.org%3E 
                        │      │                  ├ [7] : https://lists.debian.org/debian-lts-announce/2021/02/msg00035.html 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2021-27212 
                        │      │                  ├ [9] : https://security.netapp.com/advisory/ntap-20210319-0005/ 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-4744-1 
                        │      │                  ├ [11]: https://www.cve.org/CVERecord?id=CVE-2021-27212 
                        │      │                  ╰ [12]: https://www.debian.org/security/2021/dsa-4860 
                        │      ├ PublishedDate   : 2021-02-14T03:15:00Z 
                        │      ╰ LastModifiedDate: 2021-09-13T19:46:00Z 
                        ├ [53] ╭ VulnerabilityID : CVE-2023-2953 
                        │      ├ PkgID           : openldap@2.6.2-3.el9.x86_64 
                        │      ├ PkgName         : openldap 
                        │      ├ InstalledVersion: 2.6.2-3.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2953 
                        │      ├ Title           : null pointer dereference in  ber_memalloc_x  function 
                        │      ├ Description     : A vulnerability was found in openldap. This security flaw causes a null pointer dereference in
                        │      │                   ber_memalloc_x() function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-476 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-2953 
                        │      │                  ├ [1]: https://bugs.openldap.org/show_bug.cgi?id=9904 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2953 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-2953 
                        │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2023-2953 
                        │      ├ PublishedDate   : 2023-05-30T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-06T17:17:00Z 
                        ├ [54] ╭ VulnerabilityID : CVE-2021-27212 
                        │      ├ PkgID           : openldap-compat@2.6.2-3.el9.x86_64 
                        │      ├ PkgName         : openldap-compat 
                        │      ├ InstalledVersion: 2.6.2-3.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-27212 
                        │      ├ Title           : openldap: Assertion failure in slapd in the issuerAndThisUpdateCheck function 
                        │      ├ Description     : In OpenLDAP through 2.4.57 and 2.5.x through 2.5.1alpha, an assertion failure in slapd can occur in the
                        │      │                    issuerAndThisUpdateCheck function via a crafted packet, resulting in a denial of service (daemon exit) via
                        │      │                   a short timestamp. This is related to schema_init.c and checkTime. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-617 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:N/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ├ V2Score : 5 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 7.5 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2021-27212 
                        │      │                  ├ [1] : https://bugs.openldap.org/show_bug.cgi?id=9454 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27212 
                        │      │                  ├ [3] : https://git.openldap.org/openldap/openldap/-/commit/3539fc33212b528c56b716584f2c2994af7c30b0 
                        │      │                  ├ [4] : https://git.openldap.org/openldap/openldap/-/commit/9badb73425a67768c09bcaed1a9c26c684af6c30 
                        │      │                  ├ [5] : https://lists.apache.org/thread.html/r58af02e294bd07f487e2c64ffc0a29b837db5600e33b6e698b9d696b@%
                        │      │                  │       3Cissues.bookkeeper.apache.org%3E 
                        │      │                  ├ [6] : https://lists.apache.org/thread.html/rf4c02775860db415b4955778a131c2795223f61cb8c6a450893651e4@%
                        │      │                  │       3Cissues.bookkeeper.apache.org%3E 
                        │      │                  ├ [7] : https://lists.debian.org/debian-lts-announce/2021/02/msg00035.html 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2021-27212 
                        │      │                  ├ [9] : https://security.netapp.com/advisory/ntap-20210319-0005/ 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-4744-1 
                        │      │                  ├ [11]: https://www.cve.org/CVERecord?id=CVE-2021-27212 
                        │      │                  ╰ [12]: https://www.debian.org/security/2021/dsa-4860 
                        │      ├ PublishedDate   : 2021-02-14T03:15:00Z 
                        │      ╰ LastModifiedDate: 2021-09-13T19:46:00Z 
                        ├ [55] ╭ VulnerabilityID : CVE-2023-2953 
                        │      ├ PkgID           : openldap-compat@2.6.2-3.el9.x86_64 
                        │      ├ PkgName         : openldap-compat 
                        │      ├ InstalledVersion: 2.6.2-3.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2953 
                        │      ├ Title           : null pointer dereference in  ber_memalloc_x  function 
                        │      ├ Description     : A vulnerability was found in openldap. This security flaw causes a null pointer dereference in
                        │      │                   ber_memalloc_x() function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-476 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-2953 
                        │      │                  ├ [1]: https://bugs.openldap.org/show_bug.cgi?id=9904 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2953 
                        │      │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2023-2953 
                        │      │                  ╰ [4]: https://www.cve.org/CVERecord?id=CVE-2023-2953 
                        │      ├ PublishedDate   : 2023-05-30T22:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-06T17:17:00Z 
                        ├ [56] ╭ VulnerabilityID : CVE-2023-0464 
                        │      ├ PkgID           : openssl@3.0.7-6.el9_2.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-6.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-0464 
                        │      ├ Title           : Denial of service by excessive resource usage in verifying X509 policy constraints 
                        │      ├ Description     : A security vulnerability has been identified in all supported versions
                        │      │                   
                        │      │                   of OpenSSL related to the verification of X.509 certificate chains
                        │      │                   that include policy constraints.  Attackers may be able to exploit this
                        │      │                   vulnerability by creating a malicious certificate chain that triggers
                        │      │                   exponential use of computational resources, leading to a denial-of-service
                        │      │                   (DoS) attack on affected systems.
                        │      │                   
                        │      │                   Policy processing is disabled by default but can be enabled by passing
                        │      │                   the `-policy' argument to the command line utilities or by calling the
                        │      │                   `X509_VERIFY_PARAM_set1_policies()' function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-295 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-0464 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0464 
                        │      │                  ├ [2] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=2017771e2db3e2b96f89bbe8766c3209f6a99545 
                        │      │                  ├ [3] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=2dcd4f1e3115f38cefa43e3efbe9b801c27e642e 
                        │      │                  ├ [4] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=879f7080d7e141f415c79eaa3a8ac4a3dad0348b 
                        │      │                  ├ [5] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=959c59c7a0164117e7f8366466a32bb1f8d77ff1 
                        │      │                  ├ [6] : https://lists.debian.org/debian-lts-announce/2023/06/msg00011.html 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2023-0464 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-6039-1 
                        │      │                  ├ [9] : https://www.cve.org/CVERecord?id=CVE-2023-0464 
                        │      │                  ├ [10]: https://www.debian.org/security/2023/dsa-5417 
                        │      │                  ╰ [11]: https://www.openssl.org/news/secadv/20230322.txt 
                        │      ├ PublishedDate   : 2023-03-22T17:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-08T19:15:00Z 
                        ├ [57] ╭ VulnerabilityID : CVE-2023-0465 
                        │      ├ PkgID           : openssl@3.0.7-6.el9_2.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-6.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-0465 
                        │      ├ Title           : Invalid certificate policies in leaf certificates are silently ignored 
                        │      ├ Description     : Applications that use a non-default option when verifying certificates may be
                        │      │                   vulnerable to an attack from a malicious CA to circumvent certain checks.
                        │      │                   
                        │      │                   Invalid certificate policies in leaf certificates are silently ignored by
                        │      │                   OpenSSL and other certificate policy checks are skipped for that certificate.
                        │      │                   A malicious CA could use this to deliberately assert invalid certificate policies
                        │      │                   in order to circumvent policy checking on the certificate altogether.
                        │      │                   
                        │      │                   Policy processing is disabled by default but can be enabled by passing
                        │      │                   the `-policy' argument to the command line utilities or by calling the
                        │      │                   `X509_VERIFY_PARAM_set1_policies()' function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-295 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-0465 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0465 
                        │      │                  ├ [2] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=10325176f3d3e98c6e2b3bf5ab1e3b334de6947a 
                        │      │                  ├ [3] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=1dd43e0709fece299b15208f36cc7c76209ba0bb 
                        │      │                  ├ [4] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=b013765abfa80036dc779dd0e50602c57bb3bf95 
                        │      │                  ├ [5] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=facfb1ab745646e97a1920977ae4a9965ea61d5c 
                        │      │                  ├ [6] : https://lists.debian.org/debian-lts-announce/2023/06/msg00011.html 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2023-0465 
                        │      │                  ├ [8] : https://security.netapp.com/advisory/ntap-20230414-0001/ 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-6039-1 
                        │      │                  ├ [10]: https://www.cve.org/CVERecord?id=CVE-2023-0465 
                        │      │                  ├ [11]: https://www.debian.org/security/2023/dsa-5417 
                        │      │                  ╰ [12]: https://www.openssl.org/news/secadv/20230328.txt 
                        │      ├ PublishedDate   : 2023-03-28T15:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-08T19:15:00Z 
                        ├ [58] ╭ VulnerabilityID : CVE-2023-0466 
                        │      ├ PkgID           : openssl@3.0.7-6.el9_2.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-6.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-0466 
                        │      ├ Title           : Certificate policy check not enabled 
                        │      ├ Description     : The function X509_VERIFY_PARAM_add0_policy() is documented to
                        │      │                   implicitly enable the certificate policy check when doing certificate
                        │      │                   verification. However the implementation of the function does not
                        │      │                   enable the check which allows certificates with invalid or incorrect
                        │      │                   policies to pass the certificate verification.
                        │      │                   
                        │      │                   As suddenly enabling the policy check could break existing deployments it was
                        │      │                   decided to keep the existing behavior of the X509_VERIFY_PARAM_add0_policy()
                        │      │                   function.
                        │      │                   
                        │      │                   Instead the applications that require OpenSSL to perform certificate
                        │      │                   policy check need to use X509_VERIFY_PARAM_set1_policies() or explicitly
                        │      │                   enable the policy check by calling X509_VERIFY_PARAM_set_flags() with
                        │      │                   the X509_V_FLAG_POLICY_CHECK flag argument.
                        │      │                   
                        │      │                   Certificate policy checks are disabled by default in OpenSSL and are not
                        │      │                   commonly used by applications. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-295 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-0466 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0466 
                        │      │                  ├ [2] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=0d16b7e99aafc0b4a6d729eec65a411a7e025f0a 
                        │      │                  ├ [3] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=51e8a84ce742db0f6c70510d0159dad8f7825908 
                        │      │                  ├ [4] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=73398dea26de9899fb4baa94098ad0a61f435c72 
                        │      │                  ├ [5] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=fc814a30fc4f0bc54fcea7d9a7462f5457aab061 
                        │      │                  ├ [6] : https://lists.debian.org/debian-lts-announce/2023/06/msg00011.html 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2023-0466 
                        │      │                  ├ [8] : https://security.netapp.com/advisory/ntap-20230414-0001/ 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-6039-1 
                        │      │                  ├ [10]: https://www.cve.org/CVERecord?id=CVE-2023-0466 
                        │      │                  ├ [11]: https://www.debian.org/security/2023/dsa-5417 
                        │      │                  ╰ [12]: https://www.openssl.org/news/secadv/20230328.txt 
                        │      ├ PublishedDate   : 2023-03-28T15:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-08T19:15:00Z 
                        ├ [59] ╭ VulnerabilityID : CVE-2023-1255 
                        │      ├ PkgID           : openssl@3.0.7-6.el9_2.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-6.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-1255 
                        │      ├ Title           : Input buffer over-read in AES-XTS implementation on 64 bit ARM 
                        │      ├ Description     : Issue summary: The AES-XTS cipher decryption implementation for 64 bit ARM
                        │      │                   platform contains a bug that could cause it to read past the input buffer,
                        │      │                   leading to a crash.
                        │      │                   
                        │      │                   Impact summary: Applications that use the AES-XTS algorithm on the 64 bit ARM
                        │      │                   platform can crash in rare circumstances. The AES-XTS algorithm is usually
                        │      │                   used for disk encryption.
                        │      │                   
                        │      │                   The AES-XTS cipher decryption implementation for 64 bit ARM platform will read
                        │      │                   past the end of the ciphertext buffer if the ciphertext size is 4 mod 5 in 16
                        │      │                   byte blocks, e.g. 144 bytes or 1024 bytes. If the memory after the ciphertext
                        │      │                   buffer is unmapped, this will trigger a crash which results in a denial of
                        │      │                   service.
                        │      │                   
                        │      │                   If an attacker can control the size and location of the ciphertext buffer
                        │      │                   being decrypted by an application using AES-XTS on 64 bit ARM, the
                        │      │                   application is affected. This is fairly unlikely making this issue
                        │      │                   a Low severity one. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-125 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.1 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-1255 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1255 
                        │      │                  ├ [2]: https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=02ac9c9420275868472f33b01def01218742b8bb 
                        │      │                  ├ [3]: https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=bc2f61ad70971869b242fc1cb445b98bad50074a 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-1255 
                        │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-6119-1 
                        │      │                  ├ [6]: https://www.cve.org/CVERecord?id=CVE-2023-1255 
                        │      │                  ├ [7]: https://www.openssl.org/news/secadv/20230419.txt 
                        │      │                  ╰ [8]: https://www.openssl.org/news/secadv/20230420.txt 
                        │      ├ PublishedDate   : 2023-04-20T17:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-02T16:42:00Z 
                        ├ [60] ╭ VulnerabilityID : CVE-2023-2650 
                        │      ├ PkgID           : openssl@3.0.7-6.el9_2.x86_64 
                        │      ├ PkgName         : openssl 
                        │      ├ InstalledVersion: 1:3.0.7-6.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2650 
                        │      ├ Title           : Possible DoS translating ASN.1 object identifiers 
                        │      ├ Description     : Issue summary: Processing some specially crafted ASN.1 object identifiers or
                        │      │                   data containing them may be very slow.
                        │      │                   
                        │      │                   Impact summary: Applications that use OBJ_obj2txt() directly, or use any of
                        │      │                   the OpenSSL subsystems OCSP, PKCS7/SMIME, CMS, CMP/CRMF or TS with no message
                        │      │                   size limit may experience notable to very long delays when processing those
                        │      │                   messages, which may lead to a Denial of Service.
                        │      │                   
                        │      │                   An OBJECT IDENTIFIER is composed of a series of numbers - sub-identifiers -
                        │      │                   most of which have no size limit.  OBJ_obj2txt() may be used to translate
                        │      │                   an ASN.1 OBJECT IDENTIFIER given in DER encoding form (using the OpenSSL
                        │      │                   type ASN1_OBJECT) to its canonical numeric text form, which are the
                        │      │                   sub-identifiers of the OBJECT IDENTIFIER in decimal form, separated by
                        │      │                   periods.
                        │      │                   
                        │      │                   When one of the sub-identifiers in the OBJECT IDENTIFIER is very large
                        │      │                   (these are sizes that are seen as absurdly large, taking up tens or hundreds
                        │      │                   of KiBs), the translation to a decimal number in text may take a very long
                        │      │                   time.  The time complexity is O(n^2) with 'n' being the size of the
                        │      │                   sub-identifiers in bytes (*).
                        │      │                   
                        │      │                   With OpenSSL 3.0, support to fetch cryptographic algorithms using names /
                        │      │                   identifiers in string form was introduced.  This includes using OBJECT
                        │      │                   IDENTIFIERs in canonical numeric text form as identifiers for fetching
                        │      │                   algorithms.
                        │      │                   
                        │      │                   Such OBJECT IDENTIFIERs may be received through the ASN.1 structure
                        │      │                   AlgorithmIdentifier, which is commonly used in multiple protocols to specify
                        │      │                   what cryptographic algorithm should be used to sign or verify, encrypt or
                        │      │                   decrypt, or digest passed data.
                        │      │                   
                        │      │                   Applications that call OBJ_obj2txt() directly with untrusted data are
                        │      │                   affected, with any version of OpenSSL.  If the use is for the mere purpose
                        │      │                   of display, the severity is considered low.
                        │      │                   
                        │      │                   In OpenSSL 3.0 and newer, this affects the subsystems OCSP, PKCS7/SMIME,
                        │      │                   CMS, CMP/CRMF or TS.  It also impacts anything that processes X.509
                        │      │                   certificates, including simple things like verifying its signature.
                        │      │                   
                        │      │                   The impact on TLS is relatively low, because all versions of OpenSSL have a
                        │      │                   100KiB limit on the peer's certificate chain.  Additionally, this only
                        │      │                   impacts clients, or servers that have explicitly enabled client
                        │      │                   authentication.
                        │      │                   
                        │      │                   In OpenSSL 1.1.1 and 1.0.2, this only affects displaying diverse objects,
                        │      │                   such as X.509 certificates.  This is assumed to not happen in such a way
                        │      │                   that it would cause a Denial of Service, so these versions are considered
                        │      │                   not affected by this issue in such a way that it would be cause for concern,
                        │      │                   and the severity is therefore considered low. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-770 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2023/05/30/1 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-2650 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2650 
                        │      │                  ├ [3] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=423a2bc737a908ad0c77bda470b2b59dc879936b 
                        │      │                  ├ [4] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=853c5e56ee0b8650c73140816bb8b91d6163422c 
                        │      │                  ├ [5] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=9e209944b35cf82368071f160a744b6178f9b098 
                        │      │                  ├ [6] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=db779b0e10b047f2585615e0b8f2acdf21f8544a 
                        │      │                  ├ [7] : https://lists.debian.org/debian-lts-announce/2023/06/msg00011.html 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2023-2650 
                        │      │                  ├ [9] : https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2023-0009 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-6119-1 
                        │      │                  ├ [11]: https://www.cve.org/CVERecord?id=CVE-2023-2650 
                        │      │                  ├ [12]: https://www.debian.org/security/2023/dsa-5417 
                        │      │                  ╰ [13]: https://www.openssl.org/news/secadv/20230530.txt 
                        │      ├ PublishedDate   : 2023-05-30T14:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-09T00:15:00Z 
                        ├ [61] ╭ VulnerabilityID : CVE-2023-0464 
                        │      ├ PkgID           : openssl-libs@3.0.7-6.el9_2.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-6.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-0464 
                        │      ├ Title           : Denial of service by excessive resource usage in verifying X509 policy constraints 
                        │      ├ Description     : A security vulnerability has been identified in all supported versions
                        │      │                   
                        │      │                   of OpenSSL related to the verification of X.509 certificate chains
                        │      │                   that include policy constraints.  Attackers may be able to exploit this
                        │      │                   vulnerability by creating a malicious certificate chain that triggers
                        │      │                   exponential use of computational resources, leading to a denial-of-service
                        │      │                   (DoS) attack on affected systems.
                        │      │                   
                        │      │                   Policy processing is disabled by default but can be enabled by passing
                        │      │                   the `-policy' argument to the command line utilities or by calling the
                        │      │                   `X509_VERIFY_PARAM_set1_policies()' function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-295 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-0464 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0464 
                        │      │                  ├ [2] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=2017771e2db3e2b96f89bbe8766c3209f6a99545 
                        │      │                  ├ [3] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=2dcd4f1e3115f38cefa43e3efbe9b801c27e642e 
                        │      │                  ├ [4] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=879f7080d7e141f415c79eaa3a8ac4a3dad0348b 
                        │      │                  ├ [5] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=959c59c7a0164117e7f8366466a32bb1f8d77ff1 
                        │      │                  ├ [6] : https://lists.debian.org/debian-lts-announce/2023/06/msg00011.html 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2023-0464 
                        │      │                  ├ [8] : https://ubuntu.com/security/notices/USN-6039-1 
                        │      │                  ├ [9] : https://www.cve.org/CVERecord?id=CVE-2023-0464 
                        │      │                  ├ [10]: https://www.debian.org/security/2023/dsa-5417 
                        │      │                  ╰ [11]: https://www.openssl.org/news/secadv/20230322.txt 
                        │      ├ PublishedDate   : 2023-03-22T17:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-08T19:15:00Z 
                        ├ [62] ╭ VulnerabilityID : CVE-2023-0465 
                        │      ├ PkgID           : openssl-libs@3.0.7-6.el9_2.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-6.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-0465 
                        │      ├ Title           : Invalid certificate policies in leaf certificates are silently ignored 
                        │      ├ Description     : Applications that use a non-default option when verifying certificates may be
                        │      │                   vulnerable to an attack from a malicious CA to circumvent certain checks.
                        │      │                   
                        │      │                   Invalid certificate policies in leaf certificates are silently ignored by
                        │      │                   OpenSSL and other certificate policy checks are skipped for that certificate.
                        │      │                   A malicious CA could use this to deliberately assert invalid certificate policies
                        │      │                   in order to circumvent policy checking on the certificate altogether.
                        │      │                   
                        │      │                   Policy processing is disabled by default but can be enabled by passing
                        │      │                   the `-policy' argument to the command line utilities or by calling the
                        │      │                   `X509_VERIFY_PARAM_set1_policies()' function. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-295 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-0465 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0465 
                        │      │                  ├ [2] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=10325176f3d3e98c6e2b3bf5ab1e3b334de6947a 
                        │      │                  ├ [3] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=1dd43e0709fece299b15208f36cc7c76209ba0bb 
                        │      │                  ├ [4] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=b013765abfa80036dc779dd0e50602c57bb3bf95 
                        │      │                  ├ [5] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=facfb1ab745646e97a1920977ae4a9965ea61d5c 
                        │      │                  ├ [6] : https://lists.debian.org/debian-lts-announce/2023/06/msg00011.html 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2023-0465 
                        │      │                  ├ [8] : https://security.netapp.com/advisory/ntap-20230414-0001/ 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-6039-1 
                        │      │                  ├ [10]: https://www.cve.org/CVERecord?id=CVE-2023-0465 
                        │      │                  ├ [11]: https://www.debian.org/security/2023/dsa-5417 
                        │      │                  ╰ [12]: https://www.openssl.org/news/secadv/20230328.txt 
                        │      ├ PublishedDate   : 2023-03-28T15:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-08T19:15:00Z 
                        ├ [63] ╭ VulnerabilityID : CVE-2023-0466 
                        │      ├ PkgID           : openssl-libs@3.0.7-6.el9_2.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-6.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-0466 
                        │      ├ Title           : Certificate policy check not enabled 
                        │      ├ Description     : The function X509_VERIFY_PARAM_add0_policy() is documented to
                        │      │                   implicitly enable the certificate policy check when doing certificate
                        │      │                   verification. However the implementation of the function does not
                        │      │                   enable the check which allows certificates with invalid or incorrect
                        │      │                   policies to pass the certificate verification.
                        │      │                   
                        │      │                   As suddenly enabling the policy check could break existing deployments it was
                        │      │                   decided to keep the existing behavior of the X509_VERIFY_PARAM_add0_policy()
                        │      │                   function.
                        │      │                   
                        │      │                   Instead the applications that require OpenSSL to perform certificate
                        │      │                   policy check need to use X509_VERIFY_PARAM_set1_policies() or explicitly
                        │      │                   enable the policy check by calling X509_VERIFY_PARAM_set_flags() with
                        │      │                   the X509_V_FLAG_POLICY_CHECK flag argument.
                        │      │                   
                        │      │                   Certificate policy checks are disabled by default in OpenSSL and are not
                        │      │                   commonly used by applications. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-295 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/security/cve/CVE-2023-0466 
                        │      │                  ├ [1] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0466 
                        │      │                  ├ [2] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=0d16b7e99aafc0b4a6d729eec65a411a7e025f0a 
                        │      │                  ├ [3] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=51e8a84ce742db0f6c70510d0159dad8f7825908 
                        │      │                  ├ [4] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=73398dea26de9899fb4baa94098ad0a61f435c72 
                        │      │                  ├ [5] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=fc814a30fc4f0bc54fcea7d9a7462f5457aab061 
                        │      │                  ├ [6] : https://lists.debian.org/debian-lts-announce/2023/06/msg00011.html 
                        │      │                  ├ [7] : https://nvd.nist.gov/vuln/detail/CVE-2023-0466 
                        │      │                  ├ [8] : https://security.netapp.com/advisory/ntap-20230414-0001/ 
                        │      │                  ├ [9] : https://ubuntu.com/security/notices/USN-6039-1 
                        │      │                  ├ [10]: https://www.cve.org/CVERecord?id=CVE-2023-0466 
                        │      │                  ├ [11]: https://www.debian.org/security/2023/dsa-5417 
                        │      │                  ╰ [12]: https://www.openssl.org/news/secadv/20230328.txt 
                        │      ├ PublishedDate   : 2023-03-28T15:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-08T19:15:00Z 
                        ├ [64] ╭ VulnerabilityID : CVE-2023-1255 
                        │      ├ PkgID           : openssl-libs@3.0.7-6.el9_2.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-6.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-1255 
                        │      ├ Title           : Input buffer over-read in AES-XTS implementation on 64 bit ARM 
                        │      ├ Description     : Issue summary: The AES-XTS cipher decryption implementation for 64 bit ARM
                        │      │                   platform contains a bug that could cause it to read past the input buffer,
                        │      │                   leading to a crash.
                        │      │                   
                        │      │                   Impact summary: Applications that use the AES-XTS algorithm on the 64 bit ARM
                        │      │                   platform can crash in rare circumstances. The AES-XTS algorithm is usually
                        │      │                   used for disk encryption.
                        │      │                   
                        │      │                   The AES-XTS cipher decryption implementation for 64 bit ARM platform will read
                        │      │                   past the end of the ciphertext buffer if the ciphertext size is 4 mod 5 in 16
                        │      │                   byte blocks, e.g. 144 bytes or 1024 bytes. If the memory after the ciphertext
                        │      │                   buffer is unmapped, this will trigger a crash which results in a denial of
                        │      │                   service.
                        │      │                   
                        │      │                   If an attacker can control the size and location of the ciphertext buffer
                        │      │                   being decrypted by an application using AES-XTS on 64 bit ARM, the
                        │      │                   application is affected. This is fairly unlikely making this issue
                        │      │                   a Low severity one. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-125 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 5.1 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-1255 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1255 
                        │      │                  ├ [2]: https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=02ac9c9420275868472f33b01def01218742b8bb 
                        │      │                  ├ [3]: https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=bc2f61ad70971869b242fc1cb445b98bad50074a 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-1255 
                        │      │                  ├ [5]: https://ubuntu.com/security/notices/USN-6119-1 
                        │      │                  ├ [6]: https://www.cve.org/CVERecord?id=CVE-2023-1255 
                        │      │                  ├ [7]: https://www.openssl.org/news/secadv/20230419.txt 
                        │      │                  ╰ [8]: https://www.openssl.org/news/secadv/20230420.txt 
                        │      ├ PublishedDate   : 2023-04-20T17:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-02T16:42:00Z 
                        ├ [65] ╭ VulnerabilityID : CVE-2023-2650 
                        │      ├ PkgID           : openssl-libs@3.0.7-6.el9_2.x86_64 
                        │      ├ PkgName         : openssl-libs 
                        │      ├ InstalledVersion: 1:3.0.7-6.el9_2 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2650 
                        │      ├ Title           : Possible DoS translating ASN.1 object identifiers 
                        │      ├ Description     : Issue summary: Processing some specially crafted ASN.1 object identifiers or
                        │      │                   data containing them may be very slow.
                        │      │                   
                        │      │                   Impact summary: Applications that use OBJ_obj2txt() directly, or use any of
                        │      │                   the OpenSSL subsystems OCSP, PKCS7/SMIME, CMS, CMP/CRMF or TS with no message
                        │      │                   size limit may experience notable to very long delays when processing those
                        │      │                   messages, which may lead to a Denial of Service.
                        │      │                   
                        │      │                   An OBJECT IDENTIFIER is composed of a series of numbers - sub-identifiers -
                        │      │                   most of which have no size limit.  OBJ_obj2txt() may be used to translate
                        │      │                   an ASN.1 OBJECT IDENTIFIER given in DER encoding form (using the OpenSSL
                        │      │                   type ASN1_OBJECT) to its canonical numeric text form, which are the
                        │      │                   sub-identifiers of the OBJECT IDENTIFIER in decimal form, separated by
                        │      │                   periods.
                        │      │                   
                        │      │                   When one of the sub-identifiers in the OBJECT IDENTIFIER is very large
                        │      │                   (these are sizes that are seen as absurdly large, taking up tens or hundreds
                        │      │                   of KiBs), the translation to a decimal number in text may take a very long
                        │      │                   time.  The time complexity is O(n^2) with 'n' being the size of the
                        │      │                   sub-identifiers in bytes (*).
                        │      │                   
                        │      │                   With OpenSSL 3.0, support to fetch cryptographic algorithms using names /
                        │      │                   identifiers in string form was introduced.  This includes using OBJECT
                        │      │                   IDENTIFIERs in canonical numeric text form as identifiers for fetching
                        │      │                   algorithms.
                        │      │                   
                        │      │                   Such OBJECT IDENTIFIERs may be received through the ASN.1 structure
                        │      │                   AlgorithmIdentifier, which is commonly used in multiple protocols to specify
                        │      │                   what cryptographic algorithm should be used to sign or verify, encrypt or
                        │      │                   decrypt, or digest passed data.
                        │      │                   
                        │      │                   Applications that call OBJ_obj2txt() directly with untrusted data are
                        │      │                   affected, with any version of OpenSSL.  If the use is for the mere purpose
                        │      │                   of display, the severity is considered low.
                        │      │                   
                        │      │                   In OpenSSL 3.0 and newer, this affects the subsystems OCSP, PKCS7/SMIME,
                        │      │                   CMS, CMP/CRMF or TS.  It also impacts anything that processes X.509
                        │      │                   certificates, including simple things like verifying its signature.
                        │      │                   
                        │      │                   The impact on TLS is relatively low, because all versions of OpenSSL have a
                        │      │                   100KiB limit on the peer's certificate chain.  Additionally, this only
                        │      │                   impacts clients, or servers that have explicitly enabled client
                        │      │                   authentication.
                        │      │                   
                        │      │                   In OpenSSL 1.1.1 and 1.0.2, this only affects displaying diverse objects,
                        │      │                   such as X.509 certificates.  This is assumed to not happen in such a way
                        │      │                   that it would cause a Denial of Service, so these versions are considered
                        │      │                   not affected by this issue in such a way that it would be cause for concern,
                        │      │                   and the severity is therefore considered low. 
                        │      ├ Severity        : LOW 
                        │      ├ CweIDs           ─ [0]: CWE-770 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2023/05/30/1 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2023-2650 
                        │      │                  ├ [2] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2650 
                        │      │                  ├ [3] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=423a2bc737a908ad0c77bda470b2b59dc879936b 
                        │      │                  ├ [4] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=853c5e56ee0b8650c73140816bb8b91d6163422c 
                        │      │                  ├ [5] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=9e209944b35cf82368071f160a744b6178f9b098 
                        │      │                  ├ [6] : https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=db779b0e10b047f2585615e0b8f2acdf21f8544a 
                        │      │                  ├ [7] : https://lists.debian.org/debian-lts-announce/2023/06/msg00011.html 
                        │      │                  ├ [8] : https://nvd.nist.gov/vuln/detail/CVE-2023-2650 
                        │      │                  ├ [9] : https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2023-0009 
                        │      │                  ├ [10]: https://ubuntu.com/security/notices/USN-6119-1 
                        │      │                  ├ [11]: https://www.cve.org/CVERecord?id=CVE-2023-2650 
                        │      │                  ├ [12]: https://www.debian.org/security/2023/dsa-5417 
                        │      │                  ╰ [13]: https://www.openssl.org/news/secadv/20230530.txt 
                        │      ├ PublishedDate   : 2023-05-30T14:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-09T00:15:00Z 
                        ├ [66] ╭ VulnerabilityID : CVE-2007-4559 
                        │      ├ PkgID           : python-unversioned-command@3.9.16-1.el9_2.1.noarch 
                        │      ├ PkgName         : python-unversioned-command 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2007-4559 
                        │      ├ Title           : tarfile module directory traversal 
                        │      ├ Description     : Directory traversal vulnerability in the (1) extract and (2) extractall functions in the tarfile module
                        │      │                    in Python allows user-assisted remote attackers to overwrite arbitrary files via a .. (dot dot) sequence in
                        │      │                    filenames in a TAR archive, a related issue to CVE-2001-1267. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-22 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:P/I:P/A:P 
                        │      │                  │        ╰ V2Score : 6.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: http://mail.python.org/pipermail/python-dev/2007-August/074290.html 
                        │      │                  ├ [1]: http://mail.python.org/pipermail/python-dev/2007-August/074292.html 
                        │      │                  ├ [2]: http://secunia.com/advisories/26623 
                        │      │                  ├ [3]: http://www.vupen.com/english/advisories/2007/3022 
                        │      │                  ├ [4]: https://access.redhat.com/security/cve/CVE-2007-4559 
                        │      │                  ├ [5]: https://bugzilla.redhat.com/show_bug.cgi?id=263261 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2007-4559 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2007-4559 
                        │      ├ PublishedDate   : 2007-08-28T01:17:00Z 
                        │      ╰ LastModifiedDate: 2011-03-08T02:58:00Z 
                        ├ [67] ╭ VulnerabilityID : CVE-2021-23336 
                        │      ├ PkgID           : python-unversioned-command@3.9.16-1.el9_2.1.noarch 
                        │      ├ PkgName         : python-unversioned-command 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-23336 
                        │      ├ Title           : python: Web cache poisoning via urllib.parse.parse_qsl and urllib.parse.parse_qs by using a semicolon
                        │      │                   in query parameters 
                        │      ├ Description     : The package python/cpython from 0 and before 3.6.13, from 3.7.0 and before 3.7.10, from 3.8.0 and
                        │      │                   before 3.8.8, from 3.9.0 and before 3.9.2 are vulnerable to Web Cache Poisoning via urllib.parse.parse_qsl
                        │      │                   and urllib.parse.parse_qs by using a vector called parameter cloaking. When the attacker can separate query
                        │      │                   parameters using a semicolon (;), they can cause a difference in the interpretation of the request between
                        │      │                   the proxy (running with default configuration) and the server. This can result in malicious requests being
                        │      │                   cached as completely safe ones, as the proxy would usually not see the semicolon as a separator, and
                        │      │                   therefore would not include it in a cache key of an unkeyed parameter. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-444 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:H/Au:N/C:N/I:P/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:H 
                        │      │                  │        ├ V2Score : 4 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2021/02/19/4 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2021/05/01/2 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2021-23336 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23336 
                        │      │                  ├ [4] : https://errata.almalinux.org/8/ALSA-2021-4162.html 
                        │      │                  ├ [5] : https://github.com/python/cpython/commit/fcbe0cb04d35189401c0c880ebfb4311e952d776 (master) 
                        │      │                  ├ [6] : https://github.com/python/cpython/pull/24297 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2021-23336.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2021-4162.html 
                        │      │                  ├ [9] : https://lists.apache.org/thread.html/ra8ce70088ba291f358e077cafdb14d174b7a1ce9a9d86d1b332d6367@%
                        │      │                  │       3Cusers.airflow.apache.org%3E 
                        │      │                  ├ [10]: https://lists.apache.org/thread.html/rc005f4de9d9b0ba943ceb8ff5a21a5c6ff8a9df52632476698d99432@%
                        │      │                  │       3Cannounce.apache.org%3E 
                        │      │                  ├ [11]: https://lists.apache.org/thread.html/rf9fa47ab66495c78bb4120b0754dd9531ca2ff0430f6685ac9b07772@%
                        │      │                  │       3Cdev.mina.apache.org%3E 
                        │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/2021/02/msg00030.html 
                        │      │                  ├ [13]: https://lists.debian.org/debian-lts-announce/2021/04/msg00005.html 
                        │      │                  ├ [14]: https://lists.debian.org/debian-lts-announce/2021/04/msg00015.html 
                        │      │                  ├ [15]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/3
                        │      │                  │       EPYWWFDV22CJ5AOH5VCE72DOASZZ255/ 
                        │      │                  ├ [16]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/3
                        │      │                  │       YKKDLXL3UEZ3J426C2XTBS63AHE46SM/ 
                        │      │                  ├ [17]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/4
                        │      │                  │       6N6A52EGSXHJYCZWVMBJJIH4NWIV2B5/ 
                        │      │                  ├ [18]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/F
                        │      │                  │       ONHJIOZOFD7CD35KZL6SVBUTMBPGZGA/ 
                        │      │                  ├ [19]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/H
                        │      │                  │       CQTCSP6SCVIYNIRUJC5X7YBVUHPLSC4/ 
                        │      │                  ├ [20]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/H
                        │      │                  │       ZTM7KLHFCE3LWSEVO2NAFLUHMGYMCRY/ 
                        │      │                  ├ [21]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/I
                        │      │                  │       HQDU7NXA7EWAE4W7VO6MURVJIULEPPR/ 
                        │      │                  ├ [22]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/K
                        │      │                  │       JXCMHLY7H3FIYLE4OKDYUILU2CCRUCZ/ 
                        │      │                  ├ [23]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/L
                        │      │                  │       VNH6Z24IG3E67ZCQGGJ46FZB4XFLQNZ/ 
                        │      │                  ├ [24]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/M
                        │      │                  │       NUN5SOMFL2BBKP6ZAICIIUPQKZDMGYO/ 
                        │      │                  ├ [25]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/M
                        │      │                  │       P572OLHMS7MZO4KUPSCIMSZIA5IZZ62/ 
                        │      │                  ├ [26]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/N
                        │      │                  │       6VXJZSZ6N64AILJX4CTMACYGQGHHD5C/ 
                        │      │                  ├ [27]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/N
                        │      │                  │       JSCSN722JO2E2AGPWD4NTGVELVRPB4R/ 
                        │      │                  ├ [28]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/N
                        │      │                  │       ODWHDIFBQE5RU5PUWUVE47JOT5VCMJ2/ 
                        │      │                  ├ [29]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/O
                        │      │                  │       AGSWNGZJ6HQ5ISA67SNMK3CJRKICET7/ 
                        │      │                  ├ [30]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/R
                        │      │                  │       SLQD5CCM75IZGAMBDGUZEATYU5YSGJ7/ 
                        │      │                  ├ [31]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/S
                        │      │                  │       GIY6I4YS3WOXAK4SXKIEOC2G4VZKIR7/ 
                        │      │                  ├ [32]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/T
                        │      │                  │       FTELUMWZE3KV3JB2H5EE6VFRZFRD5MV/ 
                        │      │                  ├ [33]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/W
                        │      │                  │       2LSKBEFI5SYEY5FM6ICZVZM5WRQUCS4/ 
                        │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2021-23336 
                        │      │                  ├ [35]: https://security.gentoo.org/glsa/202104-04 
                        │      │                  ├ [36]: https://security.netapp.com/advisory/ntap-20210326-0004/ 
                        │      │                  ├ [37]: https://snyk.io/blog/cache-poisoning-in-popular-open-source-packages/ 
                        │      │                  ├ [38]: https://snyk.io/vuln/SNYK-UPSTREAM-PYTHONCPYTHON-1074933 
                        │      │                  ├ [39]: https://ubuntu.com/security/notices/USN-4742-1 
                        │      │                  ├ [40]: https://www.cve.org/CVERecord?id=CVE-2021-23336 
                        │      │                  ├ [41]: https://www.djangoproject.com/weblog/2021/feb/19/security-releases/ 
                        │      │                  ├ [42]: https://www.oracle.com//security-alerts/cpujul2021.html 
                        │      │                  ├ [43]: https://www.oracle.com/security-alerts/cpuApr2021.html 
                        │      │                  ├ [44]: https://www.oracle.com/security-alerts/cpujan2022.html 
                        │      │                  ╰ [45]: https://www.oracle.com/security-alerts/cpuoct2021.html 
                        │      ├ PublishedDate   : 2021-02-15T13:15:00Z 
                        │      ╰ LastModifiedDate: 2022-03-04T19:13:00Z 
                        ├ [68] ╭ VulnerabilityID : CVE-2022-0391 
                        │      ├ PkgID           : python-unversioned-command@3.9.16-1.el9_2.1.noarch 
                        │      ├ PkgName         : python-unversioned-command 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-0391 
                        │      ├ Title           : python: urllib.parse does not sanitize URLs containing ASCII newline and tabs 
                        │      ├ Description     : A flaw was found in Python, specifically within the urllib.parse module. This module helps break
                        │      │                   Uniform Resource Locator (URL) strings into components. The issue involves how the urlparse method does not
                        │      │                   sanitize input and allows characters like '\r' and '\n' in the URL path. This flaw allows an attacker to
                        │      │                   input a crafted URL, leading to injection attacks. This flaw affects Python versions prior to 3.10.0b1,
                        │      │                   3.9.5, 3.8.11, 3.7.11 and 3.6.14. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:P/A:N 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N 
                        │      │                  │        ├ V2Score : 5 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2022:6457 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2022-0391 
                        │      │                  ├ [2] : https://bugs.python.org/issue43882 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2047376 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2075390 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0391 
                        │      │                  ├ [6] : https://errata.almalinux.org/8/ALSA-2022-6457.html 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2022-0391.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2022-6457.html 
                        │      │                  ├ [9] : https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/C
                        │      │                  │       SD2YBXP3ZF44E44QMIIAR5VTO35KTRB/ 
                        │      │                  ├ [10]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/U
                        │      │                  │       DBDBAU6HUPZHISBOARTXZ5GKHF2VH5U/ 
                        │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2022-0391 
                        │      │                  ├ [12]: https://security.gentoo.org/glsa/202305-02 
                        │      │                  ├ [13]: https://security.netapp.com/advisory/ntap-20220225-0009/ 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-5342-1 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-5342-2 
                        │      │                  ├ [16]: https://www.cve.org/CVERecord?id=CVE-2022-0391 
                        │      │                  ╰ [17]: https://www.oracle.com/security-alerts/cpuapr2022.html 
                        │      ├ PublishedDate   : 2022-02-09T23:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-03T11:15:00Z 
                        ├ [69] ╭ VulnerabilityID : CVE-2023-27043 
                        │      ├ PkgID           : python-unversioned-command@3.9.16-1.el9_2.1.noarch 
                        │      ├ PkgName         : python-unversioned-command 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27043 
                        │      ├ Title           : Parsing errors in email/_parseaddr.py lead to incorrect value in email address part of tuple 
                        │      ├ Description     : The email module of Python through 3.11.3 incorrectly parses e-mail addresses that contain a special
                        │      │                   character. The wrong portion of an RFC2822 header is identified as the value of the addr-spec. In some
                        │      │                   applications, an attacker can bypass a protection mechanism in which application access is granted only
                        │      │                   after verifying receipt of e-mail to a specific domain (e.g., only @company.example.com addresses may be
                        │      │                   used for signup). This occurs in email/_parseaddr.py in recent versions of Python. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-20 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: http://python.org 
                        │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2023-27043 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27043 
                        │      │                  ├ [3]: https://github.com/python/cpython/issues/102988 
                        │      │                  ├ [4]: https://github.com/python/cpython/pull/102990 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-27043 
                        │      │                  ├ [6]: https://python-security.readthedocs.io/vuln/email-parseaddr-realname.html 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230601-0003/ 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-27043 
                        │      ├ PublishedDate   : 2023-04-19T00:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-01T14:15:00Z 
                        ├ [70] ╭ VulnerabilityID : CVE-2007-4559 
                        │      ├ PkgID           : python3@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2007-4559 
                        │      ├ Title           : tarfile module directory traversal 
                        │      ├ Description     : Directory traversal vulnerability in the (1) extract and (2) extractall functions in the tarfile module
                        │      │                    in Python allows user-assisted remote attackers to overwrite arbitrary files via a .. (dot dot) sequence in
                        │      │                    filenames in a TAR archive, a related issue to CVE-2001-1267. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-22 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:P/I:P/A:P 
                        │      │                  │        ╰ V2Score : 6.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: http://mail.python.org/pipermail/python-dev/2007-August/074290.html 
                        │      │                  ├ [1]: http://mail.python.org/pipermail/python-dev/2007-August/074292.html 
                        │      │                  ├ [2]: http://secunia.com/advisories/26623 
                        │      │                  ├ [3]: http://www.vupen.com/english/advisories/2007/3022 
                        │      │                  ├ [4]: https://access.redhat.com/security/cve/CVE-2007-4559 
                        │      │                  ├ [5]: https://bugzilla.redhat.com/show_bug.cgi?id=263261 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2007-4559 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2007-4559 
                        │      ├ PublishedDate   : 2007-08-28T01:17:00Z 
                        │      ╰ LastModifiedDate: 2011-03-08T02:58:00Z 
                        ├ [71] ╭ VulnerabilityID : CVE-2021-23336 
                        │      ├ PkgID           : python3@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-23336 
                        │      ├ Title           : python: Web cache poisoning via urllib.parse.parse_qsl and urllib.parse.parse_qs by using a semicolon
                        │      │                   in query parameters 
                        │      ├ Description     : The package python/cpython from 0 and before 3.6.13, from 3.7.0 and before 3.7.10, from 3.8.0 and
                        │      │                   before 3.8.8, from 3.9.0 and before 3.9.2 are vulnerable to Web Cache Poisoning via urllib.parse.parse_qsl
                        │      │                   and urllib.parse.parse_qs by using a vector called parameter cloaking. When the attacker can separate query
                        │      │                   parameters using a semicolon (;), they can cause a difference in the interpretation of the request between
                        │      │                   the proxy (running with default configuration) and the server. This can result in malicious requests being
                        │      │                   cached as completely safe ones, as the proxy would usually not see the semicolon as a separator, and
                        │      │                   therefore would not include it in a cache key of an unkeyed parameter. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-444 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:H/Au:N/C:N/I:P/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:H 
                        │      │                  │        ├ V2Score : 4 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2021/02/19/4 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2021/05/01/2 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2021-23336 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23336 
                        │      │                  ├ [4] : https://errata.almalinux.org/8/ALSA-2021-4162.html 
                        │      │                  ├ [5] : https://github.com/python/cpython/commit/fcbe0cb04d35189401c0c880ebfb4311e952d776 (master) 
                        │      │                  ├ [6] : https://github.com/python/cpython/pull/24297 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2021-23336.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2021-4162.html 
                        │      │                  ├ [9] : https://lists.apache.org/thread.html/ra8ce70088ba291f358e077cafdb14d174b7a1ce9a9d86d1b332d6367@%
                        │      │                  │       3Cusers.airflow.apache.org%3E 
                        │      │                  ├ [10]: https://lists.apache.org/thread.html/rc005f4de9d9b0ba943ceb8ff5a21a5c6ff8a9df52632476698d99432@%
                        │      │                  │       3Cannounce.apache.org%3E 
                        │      │                  ├ [11]: https://lists.apache.org/thread.html/rf9fa47ab66495c78bb4120b0754dd9531ca2ff0430f6685ac9b07772@%
                        │      │                  │       3Cdev.mina.apache.org%3E 
                        │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/2021/02/msg00030.html 
                        │      │                  ├ [13]: https://lists.debian.org/debian-lts-announce/2021/04/msg00005.html 
                        │      │                  ├ [14]: https://lists.debian.org/debian-lts-announce/2021/04/msg00015.html 
                        │      │                  ├ [15]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/3
                        │      │                  │       EPYWWFDV22CJ5AOH5VCE72DOASZZ255/ 
                        │      │                  ├ [16]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/3
                        │      │                  │       YKKDLXL3UEZ3J426C2XTBS63AHE46SM/ 
                        │      │                  ├ [17]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/4
                        │      │                  │       6N6A52EGSXHJYCZWVMBJJIH4NWIV2B5/ 
                        │      │                  ├ [18]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/F
                        │      │                  │       ONHJIOZOFD7CD35KZL6SVBUTMBPGZGA/ 
                        │      │                  ├ [19]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/H
                        │      │                  │       CQTCSP6SCVIYNIRUJC5X7YBVUHPLSC4/ 
                        │      │                  ├ [20]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/H
                        │      │                  │       ZTM7KLHFCE3LWSEVO2NAFLUHMGYMCRY/ 
                        │      │                  ├ [21]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/I
                        │      │                  │       HQDU7NXA7EWAE4W7VO6MURVJIULEPPR/ 
                        │      │                  ├ [22]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/K
                        │      │                  │       JXCMHLY7H3FIYLE4OKDYUILU2CCRUCZ/ 
                        │      │                  ├ [23]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/L
                        │      │                  │       VNH6Z24IG3E67ZCQGGJ46FZB4XFLQNZ/ 
                        │      │                  ├ [24]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/M
                        │      │                  │       NUN5SOMFL2BBKP6ZAICIIUPQKZDMGYO/ 
                        │      │                  ├ [25]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/M
                        │      │                  │       P572OLHMS7MZO4KUPSCIMSZIA5IZZ62/ 
                        │      │                  ├ [26]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/N
                        │      │                  │       6VXJZSZ6N64AILJX4CTMACYGQGHHD5C/ 
                        │      │                  ├ [27]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/N
                        │      │                  │       JSCSN722JO2E2AGPWD4NTGVELVRPB4R/ 
                        │      │                  ├ [28]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/N
                        │      │                  │       ODWHDIFBQE5RU5PUWUVE47JOT5VCMJ2/ 
                        │      │                  ├ [29]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/O
                        │      │                  │       AGSWNGZJ6HQ5ISA67SNMK3CJRKICET7/ 
                        │      │                  ├ [30]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/R
                        │      │                  │       SLQD5CCM75IZGAMBDGUZEATYU5YSGJ7/ 
                        │      │                  ├ [31]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/S
                        │      │                  │       GIY6I4YS3WOXAK4SXKIEOC2G4VZKIR7/ 
                        │      │                  ├ [32]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/T
                        │      │                  │       FTELUMWZE3KV3JB2H5EE6VFRZFRD5MV/ 
                        │      │                  ├ [33]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/W
                        │      │                  │       2LSKBEFI5SYEY5FM6ICZVZM5WRQUCS4/ 
                        │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2021-23336 
                        │      │                  ├ [35]: https://security.gentoo.org/glsa/202104-04 
                        │      │                  ├ [36]: https://security.netapp.com/advisory/ntap-20210326-0004/ 
                        │      │                  ├ [37]: https://snyk.io/blog/cache-poisoning-in-popular-open-source-packages/ 
                        │      │                  ├ [38]: https://snyk.io/vuln/SNYK-UPSTREAM-PYTHONCPYTHON-1074933 
                        │      │                  ├ [39]: https://ubuntu.com/security/notices/USN-4742-1 
                        │      │                  ├ [40]: https://www.cve.org/CVERecord?id=CVE-2021-23336 
                        │      │                  ├ [41]: https://www.djangoproject.com/weblog/2021/feb/19/security-releases/ 
                        │      │                  ├ [42]: https://www.oracle.com//security-alerts/cpujul2021.html 
                        │      │                  ├ [43]: https://www.oracle.com/security-alerts/cpuApr2021.html 
                        │      │                  ├ [44]: https://www.oracle.com/security-alerts/cpujan2022.html 
                        │      │                  ╰ [45]: https://www.oracle.com/security-alerts/cpuoct2021.html 
                        │      ├ PublishedDate   : 2021-02-15T13:15:00Z 
                        │      ╰ LastModifiedDate: 2022-03-04T19:13:00Z 
                        ├ [72] ╭ VulnerabilityID : CVE-2022-0391 
                        │      ├ PkgID           : python3@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-0391 
                        │      ├ Title           : python: urllib.parse does not sanitize URLs containing ASCII newline and tabs 
                        │      ├ Description     : A flaw was found in Python, specifically within the urllib.parse module. This module helps break
                        │      │                   Uniform Resource Locator (URL) strings into components. The issue involves how the urlparse method does not
                        │      │                   sanitize input and allows characters like '\r' and '\n' in the URL path. This flaw allows an attacker to
                        │      │                   input a crafted URL, leading to injection attacks. This flaw affects Python versions prior to 3.10.0b1,
                        │      │                   3.9.5, 3.8.11, 3.7.11 and 3.6.14. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:P/A:N 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N 
                        │      │                  │        ├ V2Score : 5 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2022:6457 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2022-0391 
                        │      │                  ├ [2] : https://bugs.python.org/issue43882 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2047376 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2075390 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0391 
                        │      │                  ├ [6] : https://errata.almalinux.org/8/ALSA-2022-6457.html 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2022-0391.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2022-6457.html 
                        │      │                  ├ [9] : https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/C
                        │      │                  │       SD2YBXP3ZF44E44QMIIAR5VTO35KTRB/ 
                        │      │                  ├ [10]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/U
                        │      │                  │       DBDBAU6HUPZHISBOARTXZ5GKHF2VH5U/ 
                        │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2022-0391 
                        │      │                  ├ [12]: https://security.gentoo.org/glsa/202305-02 
                        │      │                  ├ [13]: https://security.netapp.com/advisory/ntap-20220225-0009/ 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-5342-1 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-5342-2 
                        │      │                  ├ [16]: https://www.cve.org/CVERecord?id=CVE-2022-0391 
                        │      │                  ╰ [17]: https://www.oracle.com/security-alerts/cpuapr2022.html 
                        │      ├ PublishedDate   : 2022-02-09T23:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-03T11:15:00Z 
                        ├ [73] ╭ VulnerabilityID : CVE-2023-27043 
                        │      ├ PkgID           : python3@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27043 
                        │      ├ Title           : Parsing errors in email/_parseaddr.py lead to incorrect value in email address part of tuple 
                        │      ├ Description     : The email module of Python through 3.11.3 incorrectly parses e-mail addresses that contain a special
                        │      │                   character. The wrong portion of an RFC2822 header is identified as the value of the addr-spec. In some
                        │      │                   applications, an attacker can bypass a protection mechanism in which application access is granted only
                        │      │                   after verifying receipt of e-mail to a specific domain (e.g., only @company.example.com addresses may be
                        │      │                   used for signup). This occurs in email/_parseaddr.py in recent versions of Python. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-20 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: http://python.org 
                        │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2023-27043 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27043 
                        │      │                  ├ [3]: https://github.com/python/cpython/issues/102988 
                        │      │                  ├ [4]: https://github.com/python/cpython/pull/102990 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-27043 
                        │      │                  ├ [6]: https://python-security.readthedocs.io/vuln/email-parseaddr-realname.html 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230601-0003/ 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-27043 
                        │      ├ PublishedDate   : 2023-04-19T00:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-01T14:15:00Z 
                        ├ [74] ╭ VulnerabilityID : CVE-2007-4559 
                        │      ├ PkgID           : python3-libs@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3-libs 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2007-4559 
                        │      ├ Title           : tarfile module directory traversal 
                        │      ├ Description     : Directory traversal vulnerability in the (1) extract and (2) extractall functions in the tarfile module
                        │      │                    in Python allows user-assisted remote attackers to overwrite arbitrary files via a .. (dot dot) sequence in
                        │      │                    filenames in a TAR archive, a related issue to CVE-2001-1267. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-22 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:M/Au:N/C:P/I:P/A:P 
                        │      │                  │        ╰ V2Score : 6.8 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N 
                        │      │                           ╰ V3Score : 5.5 
                        │      ├ References       ╭ [0]: http://mail.python.org/pipermail/python-dev/2007-August/074290.html 
                        │      │                  ├ [1]: http://mail.python.org/pipermail/python-dev/2007-August/074292.html 
                        │      │                  ├ [2]: http://secunia.com/advisories/26623 
                        │      │                  ├ [3]: http://www.vupen.com/english/advisories/2007/3022 
                        │      │                  ├ [4]: https://access.redhat.com/security/cve/CVE-2007-4559 
                        │      │                  ├ [5]: https://bugzilla.redhat.com/show_bug.cgi?id=263261 
                        │      │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2007-4559 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2007-4559 
                        │      ├ PublishedDate   : 2007-08-28T01:17:00Z 
                        │      ╰ LastModifiedDate: 2011-03-08T02:58:00Z 
                        ├ [75] ╭ VulnerabilityID : CVE-2021-23336 
                        │      ├ PkgID           : python3-libs@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3-libs 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-23336 
                        │      ├ Title           : python: Web cache poisoning via urllib.parse.parse_qsl and urllib.parse.parse_qs by using a semicolon
                        │      │                   in query parameters 
                        │      ├ Description     : The package python/cpython from 0 and before 3.6.13, from 3.7.0 and before 3.7.10, from 3.8.0 and
                        │      │                   before 3.8.8, from 3.9.0 and before 3.9.2 are vulnerable to Web Cache Poisoning via urllib.parse.parse_qsl
                        │      │                   and urllib.parse.parse_qs by using a vector called parameter cloaking. When the attacker can separate query
                        │      │                   parameters using a semicolon (;), they can cause a difference in the interpretation of the request between
                        │      │                   the proxy (running with default configuration) and the server. This can result in malicious requests being
                        │      │                   cached as completely safe ones, as the proxy would usually not see the semicolon as a separator, and
                        │      │                   therefore would not include it in a cache key of an unkeyed parameter. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-444 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:H/Au:N/C:N/I:P/A:P 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:H 
                        │      │                  │        ├ V2Score : 4 
                        │      │                  │        ╰ V3Score : 5.9 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:H 
                        │      │                           ╰ V3Score : 5.9 
                        │      ├ References       ╭ [0] : http://www.openwall.com/lists/oss-security/2021/02/19/4 
                        │      │                  ├ [1] : http://www.openwall.com/lists/oss-security/2021/05/01/2 
                        │      │                  ├ [2] : https://access.redhat.com/security/cve/CVE-2021-23336 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23336 
                        │      │                  ├ [4] : https://errata.almalinux.org/8/ALSA-2021-4162.html 
                        │      │                  ├ [5] : https://github.com/python/cpython/commit/fcbe0cb04d35189401c0c880ebfb4311e952d776 (master) 
                        │      │                  ├ [6] : https://github.com/python/cpython/pull/24297 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2021-23336.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2021-4162.html 
                        │      │                  ├ [9] : https://lists.apache.org/thread.html/ra8ce70088ba291f358e077cafdb14d174b7a1ce9a9d86d1b332d6367@%
                        │      │                  │       3Cusers.airflow.apache.org%3E 
                        │      │                  ├ [10]: https://lists.apache.org/thread.html/rc005f4de9d9b0ba943ceb8ff5a21a5c6ff8a9df52632476698d99432@%
                        │      │                  │       3Cannounce.apache.org%3E 
                        │      │                  ├ [11]: https://lists.apache.org/thread.html/rf9fa47ab66495c78bb4120b0754dd9531ca2ff0430f6685ac9b07772@%
                        │      │                  │       3Cdev.mina.apache.org%3E 
                        │      │                  ├ [12]: https://lists.debian.org/debian-lts-announce/2021/02/msg00030.html 
                        │      │                  ├ [13]: https://lists.debian.org/debian-lts-announce/2021/04/msg00005.html 
                        │      │                  ├ [14]: https://lists.debian.org/debian-lts-announce/2021/04/msg00015.html 
                        │      │                  ├ [15]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/3
                        │      │                  │       EPYWWFDV22CJ5AOH5VCE72DOASZZ255/ 
                        │      │                  ├ [16]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/3
                        │      │                  │       YKKDLXL3UEZ3J426C2XTBS63AHE46SM/ 
                        │      │                  ├ [17]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/4
                        │      │                  │       6N6A52EGSXHJYCZWVMBJJIH4NWIV2B5/ 
                        │      │                  ├ [18]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/F
                        │      │                  │       ONHJIOZOFD7CD35KZL6SVBUTMBPGZGA/ 
                        │      │                  ├ [19]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/H
                        │      │                  │       CQTCSP6SCVIYNIRUJC5X7YBVUHPLSC4/ 
                        │      │                  ├ [20]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/H
                        │      │                  │       ZTM7KLHFCE3LWSEVO2NAFLUHMGYMCRY/ 
                        │      │                  ├ [21]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/I
                        │      │                  │       HQDU7NXA7EWAE4W7VO6MURVJIULEPPR/ 
                        │      │                  ├ [22]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/K
                        │      │                  │       JXCMHLY7H3FIYLE4OKDYUILU2CCRUCZ/ 
                        │      │                  ├ [23]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/L
                        │      │                  │       VNH6Z24IG3E67ZCQGGJ46FZB4XFLQNZ/ 
                        │      │                  ├ [24]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/M
                        │      │                  │       NUN5SOMFL2BBKP6ZAICIIUPQKZDMGYO/ 
                        │      │                  ├ [25]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/M
                        │      │                  │       P572OLHMS7MZO4KUPSCIMSZIA5IZZ62/ 
                        │      │                  ├ [26]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/N
                        │      │                  │       6VXJZSZ6N64AILJX4CTMACYGQGHHD5C/ 
                        │      │                  ├ [27]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/N
                        │      │                  │       JSCSN722JO2E2AGPWD4NTGVELVRPB4R/ 
                        │      │                  ├ [28]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/N
                        │      │                  │       ODWHDIFBQE5RU5PUWUVE47JOT5VCMJ2/ 
                        │      │                  ├ [29]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/O
                        │      │                  │       AGSWNGZJ6HQ5ISA67SNMK3CJRKICET7/ 
                        │      │                  ├ [30]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/R
                        │      │                  │       SLQD5CCM75IZGAMBDGUZEATYU5YSGJ7/ 
                        │      │                  ├ [31]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/S
                        │      │                  │       GIY6I4YS3WOXAK4SXKIEOC2G4VZKIR7/ 
                        │      │                  ├ [32]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/T
                        │      │                  │       FTELUMWZE3KV3JB2H5EE6VFRZFRD5MV/ 
                        │      │                  ├ [33]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/W
                        │      │                  │       2LSKBEFI5SYEY5FM6ICZVZM5WRQUCS4/ 
                        │      │                  ├ [34]: https://nvd.nist.gov/vuln/detail/CVE-2021-23336 
                        │      │                  ├ [35]: https://security.gentoo.org/glsa/202104-04 
                        │      │                  ├ [36]: https://security.netapp.com/advisory/ntap-20210326-0004/ 
                        │      │                  ├ [37]: https://snyk.io/blog/cache-poisoning-in-popular-open-source-packages/ 
                        │      │                  ├ [38]: https://snyk.io/vuln/SNYK-UPSTREAM-PYTHONCPYTHON-1074933 
                        │      │                  ├ [39]: https://ubuntu.com/security/notices/USN-4742-1 
                        │      │                  ├ [40]: https://www.cve.org/CVERecord?id=CVE-2021-23336 
                        │      │                  ├ [41]: https://www.djangoproject.com/weblog/2021/feb/19/security-releases/ 
                        │      │                  ├ [42]: https://www.oracle.com//security-alerts/cpujul2021.html 
                        │      │                  ├ [43]: https://www.oracle.com/security-alerts/cpuApr2021.html 
                        │      │                  ├ [44]: https://www.oracle.com/security-alerts/cpujan2022.html 
                        │      │                  ╰ [45]: https://www.oracle.com/security-alerts/cpuoct2021.html 
                        │      ├ PublishedDate   : 2021-02-15T13:15:00Z 
                        │      ╰ LastModifiedDate: 2022-03-04T19:13:00Z 
                        ├ [76] ╭ VulnerabilityID : CVE-2022-0391 
                        │      ├ PkgID           : python3-libs@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3-libs 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2022-0391 
                        │      ├ Title           : python: urllib.parse does not sanitize URLs containing ASCII newline and tabs 
                        │      ├ Description     : A flaw was found in Python, specifically within the urllib.parse module. This module helps break
                        │      │                   Uniform Resource Locator (URL) strings into components. The issue involves how the urlparse method does not
                        │      │                   sanitize input and allows characters like '\r' and '\n' in the URL path. This flaw allows an attacker to
                        │      │                   input a crafted URL, leading to injection attacks. This flaw affects Python versions prior to 3.10.0b1,
                        │      │                   3.9.5, 3.8.11, 3.7.11 and 3.6.14. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-74 
                        │      ├ CVSS             ╭ nvd    ╭ V2Vector: AV:N/AC:L/Au:N/C:N/I:P/A:N 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N 
                        │      │                  │        ├ V2Score : 5 
                        │      │                  │        ╰ V3Score : 7.5 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2022:6457 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2022-0391 
                        │      │                  ├ [2] : https://bugs.python.org/issue43882 
                        │      │                  ├ [3] : https://bugzilla.redhat.com/2047376 
                        │      │                  ├ [4] : https://bugzilla.redhat.com/2075390 
                        │      │                  ├ [5] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0391 
                        │      │                  ├ [6] : https://errata.almalinux.org/8/ALSA-2022-6457.html 
                        │      │                  ├ [7] : https://linux.oracle.com/cve/CVE-2022-0391.html 
                        │      │                  ├ [8] : https://linux.oracle.com/errata/ELSA-2022-6457.html 
                        │      │                  ├ [9] : https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/C
                        │      │                  │       SD2YBXP3ZF44E44QMIIAR5VTO35KTRB/ 
                        │      │                  ├ [10]: https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/U
                        │      │                  │       DBDBAU6HUPZHISBOARTXZ5GKHF2VH5U/ 
                        │      │                  ├ [11]: https://nvd.nist.gov/vuln/detail/CVE-2022-0391 
                        │      │                  ├ [12]: https://security.gentoo.org/glsa/202305-02 
                        │      │                  ├ [13]: https://security.netapp.com/advisory/ntap-20220225-0009/ 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-5342-1 
                        │      │                  ├ [15]: https://ubuntu.com/security/notices/USN-5342-2 
                        │      │                  ├ [16]: https://www.cve.org/CVERecord?id=CVE-2022-0391 
                        │      │                  ╰ [17]: https://www.oracle.com/security-alerts/cpuapr2022.html 
                        │      ├ PublishedDate   : 2022-02-09T23:15:00Z 
                        │      ╰ LastModifiedDate: 2023-05-03T11:15:00Z 
                        ├ [77] ╭ VulnerabilityID : CVE-2023-27043 
                        │      ├ PkgID           : python3-libs@3.9.16-1.el9_2.1.x86_64 
                        │      ├ PkgName         : python3-libs 
                        │      ├ InstalledVersion: 3.9.16-1.el9_2.1 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-27043 
                        │      ├ Title           : Parsing errors in email/_parseaddr.py lead to incorrect value in email address part of tuple 
                        │      ├ Description     : The email module of Python through 3.11.3 incorrectly parses e-mail addresses that contain a special
                        │      │                   character. The wrong portion of an RFC2822 header is identified as the value of the addr-spec. In some
                        │      │                   applications, an attacker can bypass a protection mechanism in which application access is granted only
                        │      │                   after verifying receipt of e-mail to a specific domain (e.g., only @company.example.com addresses may be
                        │      │                   used for signup). This occurs in email/_parseaddr.py in recent versions of Python. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-20 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: http://python.org 
                        │      │                  ├ [1]: https://access.redhat.com/security/cve/CVE-2023-27043 
                        │      │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27043 
                        │      │                  ├ [3]: https://github.com/python/cpython/issues/102988 
                        │      │                  ├ [4]: https://github.com/python/cpython/pull/102990 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-27043 
                        │      │                  ├ [6]: https://python-security.readthedocs.io/vuln/email-parseaddr-realname.html 
                        │      │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230601-0003/ 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-27043 
                        │      ├ PublishedDate   : 2023-04-19T00:15:00Z 
                        │      ╰ LastModifiedDate: 2023-06-01T14:15:00Z 
                        ├ [78] ╭ VulnerabilityID : CVE-2021-3572 
                        │      ├ PkgID           : python3-pip-wheel@21.2.3-6.el9.noarch 
                        │      ├ PkgName         : python3-pip-wheel 
                        │      ├ InstalledVersion: 21.2.3-6.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-3572 
                        │      ├ Title           : python-pip: Incorrect handling of unicode separators in git references 
                        │      ├ Description     : A flaw was found in python-pip in the way it handled Unicode separators in git references. A remote
                        │      │                   attacker could possibly use this issue to install a different revision on a repository. The highest threat
                        │      │                   from this vulnerability is to data integrity. This is fixed in python-pip version 21.1. 
                        │      ├ Severity        : LOW 
                        │      ├ CVSS             ╭ ghsa   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:H/A:N 
                        │      │                  │        ╰ V3Score : 5.7 
                        │      │                  ├ nvd    ╭ V2Vector: AV:N/AC:M/Au:S/C:N/I:P/A:N 
                        │      │                  │        ├ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:H/A:N 
                        │      │                  │        ├ V2Score : 3.5 
                        │      │                  │        ╰ V3Score : 5.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:U/C:N/I:H/A:N 
                        │      │                           ╰ V3Score : 4.5 
                        │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2021:3254 
                        │      │                  ├ [1] : https://access.redhat.com/security/cve/CVE-2021-3572 
                        │      │                  ├ [2] : https://bugzilla.redhat.com/show_bug.cgi?id=1962856 
                        │      │                  ├ [3] : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3572 
                        │      │                  ├ [4] : https://github.com/advisories/GHSA-5xp3-jfq3-5q8x 
                        │      │                  ├ [5] : https://github.com/pypa/pip/commit/e46bdda9711392fec0c45c1175bae6db847cb30b 
                        │      │                  ├ [6] : https://github.com/pypa/pip/issues/10042 
                        │      │                  ├ [7] : https://github.com/pypa/pip/issues/10042#issuecomment-857452480 
                        │      │                  ├ [8] : https://github.com/pypa/pip/pull/9827 
                        │      │                  ├ [9] : https://github.com/skazi0/CVE-2021-3572/blob/master/CVE-2021-3572-v9.0.1.patch 
                        │      │                  ├ [10]: https://linux.oracle.com/cve/CVE-2021-3572.html 
                        │      │                  ├ [11]: https://linux.oracle.com/errata/ELSA-2023-12349.html 
                        │      │                  ├ [12]: https://nvd.nist.gov/vuln/detail/CVE-2021-3572 
                        │      │                  ├ [13]: https://packetstormsecurity.com/files/162712/USN-4961-1.txt 
                        │      │                  ├ [14]: https://ubuntu.com/security/notices/USN-4961-2 
                        │      │                  ├ [15]: https://www.cve.org/CVERecord?id=CVE-2021-3572 
                        │      │                  ├ [16]: https://www.oracle.com/security-alerts/cpuapr2022.html 
                        │      │                  ╰ [17]: https://www.oracle.com/security-alerts/cpujul2022.html 
                        │      ├ PublishedDate   : 2021-11-10T18:15:00Z 
                        │      ╰ LastModifiedDate: 2022-10-05T02:14:00Z 
                        ├ [79] ╭ VulnerabilityID : CVE-2021-35937 
                        │      ├ PkgID           : rpm@4.16.1.3-22.el9.x86_64 
                        │      ├ PkgName         : rpm 
                        │      ├ InstalledVersion: 4.16.1.3-22.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-35937 
                        │      ├ Title           : TOCTOU race in checks for unsafe symlinks 
                        │      ├ Description     : A race condition vulnerability was found in rpm. A local unprivileged user could use this flaw to
                        │      │                   bypass the checks that were introduced in response to CVE-2017-7500 and CVE-2017-7501, potentially gaining
                        │      │                   root privileges. The highest threat from this vulnerability is to data confidentiality and integrity as well
                        │      │                    as system availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ╭ [0]: CWE-59 
                        │      │                  ╰ [1]: CWE-367 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 6.4 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:H/UI:R/S:U/C:H/I:H/A:H 
                        │      │                           ╰ V3Score : 6.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-35937 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1964125 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2021-35937 
                        │      │                  ├ [3]: https://rpm.org/wiki/Releases/4.18.0 
                        │      │                  ├ [4]: https://security.gentoo.org/glsa/202210-22 
                        │      │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2021-35937 
                        │      │                  ╰ [6]: https://www.usenix.org/legacy/event/sec05/tech/full_papers/borisov/borisov.pdf 
                        │      ├ PublishedDate   : 2022-08-25T20:15:00Z 
                        │      ╰ LastModifiedDate: 2022-11-16T20:05:00Z 
                        ├ [80] ╭ VulnerabilityID : CVE-2021-35938 
                        │      ├ PkgID           : rpm@4.16.1.3-22.el9.x86_64 
                        │      ├ PkgName         : rpm 
                        │      ├ InstalledVersion: 4.16.1.3-22.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-35938 
                        │      ├ Title           : races with chown/chmod/capabilities calls during installation 
                        │      ├ Description     : A symbolic link issue was found in rpm. It occurs when rpm sets the desired permissions and credentials
                        │      │                    after installing a file. A local unprivileged user could use this flaw to exchange the original file with a
                        │      │                    symbolic link to a security-critical file and escalate their privileges on the system. The highest threat
                        │      │                   from this vulnerability is to data confidentiality and integrity as well as system availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-59 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 6.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-35938 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1964114 
                        │      │                  ├ [2]: https://bugzilla.suse.com/show_bug.cgi?id=1157880 
                        │      │                  ├ [3]: https://github.com/rpm-software-management/rpm/commit/25a435e90844ea98fe5eb7bef22c1aecf3a9c033 
                        │      │                  ├ [4]: https://github.com/rpm-software-management/rpm/pull/1919 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2021-35938 
                        │      │                  ├ [6]: https://rpm.org/wiki/Releases/4.18.0 
                        │      │                  ├ [7]: https://security.gentoo.org/glsa/202210-22 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2021-35938 
                        │      ├ PublishedDate   : 2022-08-25T20:15:00Z 
                        │      ╰ LastModifiedDate: 2022-11-29T18:06:00Z 
                        ├ [81] ╭ VulnerabilityID : CVE-2021-35939 
                        │      ├ PkgID           : rpm@4.16.1.3-22.el9.x86_64 
                        │      ├ PkgName         : rpm 
                        │      ├ InstalledVersion: 4.16.1.3-22.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-35939 
                        │      ├ Title           : checks for unsafe symlinks are not performed for intermediary directories 
                        │      ├ Description     : It was found that the fix for CVE-2017-7500 and CVE-2017-7501 was incomplete: the check was only
                        │      │                   implemented for the parent directory of the file to be created. A local unprivileged user who owns another
                        │      │                   ancestor directory could potentially use this flaw to gain root privileges. The highest threat from this
                        │      │                   vulnerability is to data confidentiality and integrity as well as system availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-59 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 6.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-35939 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1964129 
                        │      │                  ├ [2]: https://github.com/rpm-software-management/rpm/commit/96ec957e281220f8e137a2d5eb23b83a6377d556 
                        │      │                  ├ [3]: https://github.com/rpm-software-management/rpm/pull/1919 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2021-35939 
                        │      │                  ├ [5]: https://rpm.org/wiki/Releases/4.18.0 
                        │      │                  ├ [6]: https://security.gentoo.org/glsa/202210-22 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2021-35939 
                        │      ├ PublishedDate   : 2022-08-26T16:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-04T01:16:00Z 
                        ├ [82] ╭ VulnerabilityID : CVE-2021-35937 
                        │      ├ PkgID           : rpm-libs@4.16.1.3-22.el9.x86_64 
                        │      ├ PkgName         : rpm-libs 
                        │      ├ InstalledVersion: 4.16.1.3-22.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-35937 
                        │      ├ Title           : TOCTOU race in checks for unsafe symlinks 
                        │      ├ Description     : A race condition vulnerability was found in rpm. A local unprivileged user could use this flaw to
                        │      │                   bypass the checks that were introduced in response to CVE-2017-7500 and CVE-2017-7501, potentially gaining
                        │      │                   root privileges. The highest threat from this vulnerability is to data confidentiality and integrity as well
                        │      │                    as system availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ╭ [0]: CWE-59 
                        │      │                  ╰ [1]: CWE-367 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 6.4 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:H/PR:H/UI:R/S:U/C:H/I:H/A:H 
                        │      │                           ╰ V3Score : 6.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-35937 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1964125 
                        │      │                  ├ [2]: https://nvd.nist.gov/vuln/detail/CVE-2021-35937 
                        │      │                  ├ [3]: https://rpm.org/wiki/Releases/4.18.0 
                        │      │                  ├ [4]: https://security.gentoo.org/glsa/202210-22 
                        │      │                  ├ [5]: https://www.cve.org/CVERecord?id=CVE-2021-35937 
                        │      │                  ╰ [6]: https://www.usenix.org/legacy/event/sec05/tech/full_papers/borisov/borisov.pdf 
                        │      ├ PublishedDate   : 2022-08-25T20:15:00Z 
                        │      ╰ LastModifiedDate: 2022-11-16T20:05:00Z 
                        ├ [83] ╭ VulnerabilityID : CVE-2021-35938 
                        │      ├ PkgID           : rpm-libs@4.16.1.3-22.el9.x86_64 
                        │      ├ PkgName         : rpm-libs 
                        │      ├ InstalledVersion: 4.16.1.3-22.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-35938 
                        │      ├ Title           : races with chown/chmod/capabilities calls during installation 
                        │      ├ Description     : A symbolic link issue was found in rpm. It occurs when rpm sets the desired permissions and credentials
                        │      │                    after installing a file. A local unprivileged user could use this flaw to exchange the original file with a
                        │      │                    symbolic link to a security-critical file and escalate their privileges on the system. The highest threat
                        │      │                   from this vulnerability is to data confidentiality and integrity as well as system availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-59 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 6.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-35938 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1964114 
                        │      │                  ├ [2]: https://bugzilla.suse.com/show_bug.cgi?id=1157880 
                        │      │                  ├ [3]: https://github.com/rpm-software-management/rpm/commit/25a435e90844ea98fe5eb7bef22c1aecf3a9c033 
                        │      │                  ├ [4]: https://github.com/rpm-software-management/rpm/pull/1919 
                        │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2021-35938 
                        │      │                  ├ [6]: https://rpm.org/wiki/Releases/4.18.0 
                        │      │                  ├ [7]: https://security.gentoo.org/glsa/202210-22 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2021-35938 
                        │      ├ PublishedDate   : 2022-08-25T20:15:00Z 
                        │      ╰ LastModifiedDate: 2022-11-29T18:06:00Z 
                        ├ [84] ╭ VulnerabilityID : CVE-2021-35939 
                        │      ├ PkgID           : rpm-libs@4.16.1.3-22.el9.x86_64 
                        │      ├ PkgName         : rpm-libs 
                        │      ├ InstalledVersion: 4.16.1.3-22.el9 
                        │      ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                        │      │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-35939 
                        │      ├ Title           : checks for unsafe symlinks are not performed for intermediary directories 
                        │      ├ Description     : It was found that the fix for CVE-2017-7500 and CVE-2017-7501 was incomplete: the check was only
                        │      │                   implemented for the parent directory of the file to be created. A local unprivileged user who owns another
                        │      │                   ancestor directory could potentially use this flaw to gain root privileges. The highest threat from this
                        │      │                   vulnerability is to data confidentiality and integrity as well as system availability. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-59 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H 
                        │      │                  │        ╰ V3Score : 6.7 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H 
                        │      │                           ╰ V3Score : 6.5 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-35939 
                        │      │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=1964129 
                        │      │                  ├ [2]: https://github.com/rpm-software-management/rpm/commit/96ec957e281220f8e137a2d5eb23b83a6377d556 
                        │      │                  ├ [3]: https://github.com/rpm-software-management/rpm/pull/1919 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2021-35939 
                        │      │                  ├ [5]: https://rpm.org/wiki/Releases/4.18.0 
                        │      │                  ├ [6]: https://security.gentoo.org/glsa/202210-22 
                        │      │                  ╰ [7]: https://www.cve.org/CVERecord?id=CVE-2021-35939 
                        │      ├ PublishedDate   : 2022-08-26T16:15:00Z 
                        │      ╰ LastModifiedDate: 2023-02-04T01:16:00Z 
                        ├ [85] ╭ VulnerabilityID : CVE-2023-28486 
                        │      ├ PkgID           : sudo@1.9.5p2-9.el9.x86_64 
                        │      ├ PkgName         : sudo 
                        │      ├ InstalledVersion: 1.9.5p2-9.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28486 
                        │      ├ Title           : sudo: Sudo does not escape control characters in log messages 
                        │      ├ Description     : Sudo before 1.9.13 does not escape control characters in log messages. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-116 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-28486 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28486 
                        │      │                  ├ [2]: https://github.com/sudo-project/sudo/commit/334daf92b31b79ce68ed75e2ee14fca265f029ca 
                        │      │                  ├ [3]: https://github.com/sudo-project/sudo/releases/tag/SUDO_1_9_13 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-28486 
                        │      │                  ├ [5]: https://security.netapp.com/advisory/ntap-20230420-0002/ 
                        │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-6005-1 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-6005-2 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-28486 
                        │      ├ PublishedDate   : 2023-03-16T01:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-20T09:15:00Z 
                        ├ [86] ╭ VulnerabilityID : CVE-2023-28487 
                        │      ├ PkgID           : sudo@1.9.5p2-9.el9.x86_64 
                        │      ├ PkgName         : sudo 
                        │      ├ InstalledVersion: 1.9.5p2-9.el9 
                        │      ├ Layer            ╭ Digest: sha256:fad6ab6d8d5a55c3f95552080d6816f3ee7a8db26e2edad24ff8f077c13d57e7 
                        │      │                  ╰ DiffID: sha256:a362797a134218cbb31955628ef11d226dc8fe989e30c2ac857b3d3157ad5957 
                        │      ├ SeveritySource  : redhat 
                        │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-28487 
                        │      ├ Title           : Sudo does not escape control characters in sudoreplay output 
                        │      ├ Description     : Sudo before 1.9.13 does not escape control characters in sudoreplay output. 
                        │      ├ Severity        : MEDIUM 
                        │      ├ CweIDs           ─ [0]: CWE-116 
                        │      ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N 
                        │      │                  │        ╰ V3Score : 5.3 
                        │      │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N 
                        │      │                           ╰ V3Score : 5.3 
                        │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-28487 
                        │      │                  ├ [1]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28487 
                        │      │                  ├ [2]: https://github.com/sudo-project/sudo/commit/334daf92b31b79ce68ed75e2ee14fca265f029ca 
                        │      │                  ├ [3]: https://github.com/sudo-project/sudo/releases/tag/SUDO_1_9_13 
                        │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-28487 
                        │      │                  ├ [5]: https://security.netapp.com/advisory/ntap-20230420-0002/ 
                        │      │                  ├ [6]: https://ubuntu.com/security/notices/USN-6005-1 
                        │      │                  ├ [7]: https://ubuntu.com/security/notices/USN-6005-2 
                        │      │                  ╰ [8]: https://www.cve.org/CVERecord?id=CVE-2023-28487 
                        │      ├ PublishedDate   : 2023-03-16T01:15:00Z 
                        │      ╰ LastModifiedDate: 2023-04-20T09:15:00Z 
                        ╰ [87] ╭ VulnerabilityID : CVE-2021-3997 
                               ├ PkgID           : systemd-libs@252-13.el9_2.x86_64 
                               ├ PkgName         : systemd-libs 
                               ├ InstalledVersion: 252-13.el9_2 
                               ├ Layer            ╭ Digest: sha256:a9f076b473b10f92470b5c7fe238962e80f6eedd374d74105fcfad39afb4f699 
                               │                  ╰ DiffID: sha256:c358f169fa44c7c7da69ded43ad543cd296aa75806582c559018a3bf2db75ea9 
                               ├ SeveritySource  : redhat 
                               ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2021-3997 
                               ├ Title           : systemd: Uncontrolled recursion in systemd-tmpfiles when removing files 
                               ├ Description     : A flaw was found in systemd. An uncontrolled recursion in systemd-tmpfiles may lead to a denial of
                               │                   service at boot time when too many nested directories are created in /tmp. 
                               ├ Severity        : MEDIUM 
                               ├ CweIDs           ─ [0]: CWE-674 
                               ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H 
                               │                  │        ╰ V3Score : 5.5 
                               │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H 
                               │                           ╰ V3Score : 5.5 
                               ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2021-3997 
                               │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2024639 
                               │                  ├ [2]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3997 
                               │                  ├ [3]: https://github.com/systemd/systemd/commit/5b1cf7a9be37e20133c0208005274ce4a5b5c6a1 
                               │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2021-3997 
                               │                  ├ [5]: https://security.gentoo.org/glsa/202305-15 
                               │                  ├ [6]: https://ubuntu.com/security/notices/USN-5226-1 
                               │                  ├ [7]: https://www.cve.org/CVERecord?id=CVE-2021-3997 
                               │                  ╰ [8]: https://www.openwall.com/lists/oss-security/2022/01/10/2 
                               ├ PublishedDate   : 2022-08-23T20:15:00Z 
                               ╰ LastModifiedDate: 2023-05-03T12:15:00Z 
````
