````yaml
╭ [0] ╭ Target         : openaf/oaf:latest (alpine 3.18.0) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2023-2804 
│                             ├ PkgID           : libjpeg-turbo@2.1.5.1-r2 
│                             ├ PkgName         : libjpeg-turbo 
│                             ├ InstalledVersion: 2.1.5.1-r2 
│                             ├ FixedVersion    : 2.1.5.1-r3 
│                             ├ Layer            ╭ Digest: sha256:4bd636f0a6b69e68e5cc9810353492fbc0c73895fa1a31f6def8d4817c4aeff1 
│                             │                  ╰ DiffID: sha256:616f28a7f8dbd7550739728498d1bc7cceff76b35a95e43a39fb4001f92968d4 
│                             ├ SeveritySource  : nvd 
│                             ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-2804 
│                             ├ DataSource       ╭ ID  : alpine 
│                             │                  ├ Name: Alpine Secdb 
│                             │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                             ├ Title           : heap-buffer-overflow in h2v2_merged_upsample_internal() at /libjpeg-turbo/jdmrgext.c 
│                             ├ Description     : A heap-based buffer overflow issue was discovered in libjpeg-turbo in h2v2_merged_upsample_internal()
│                             │                   function of jdmrgext.c file. The vulnerability can only be exploited with 12-bit data precision for which the
│                             │                    range of the sample data type exceeds the valid sample range, hence, an attacker could craft a 12-bit
│                             │                   lossless JPEG image that contains out-of-range 12-bit samples. An application attempting to decompress such
│                             │                   image using merged upsampling would lead to segmentation fault or buffer overflows, causing an application to
│                             │                    crash. 
│                             ├ Severity        : MEDIUM 
│                             ├ CweIDs           ─ [0]: CWE-787 
│                             ├ CVSS             ╭ nvd    ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
│                             │                  │        ╰ V3Score : 6.5 
│                             │                  ╰ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H 
│                             │                           ╰ V3Score : 6.5 
│                             ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-2804 
│                             │                  ├ [1]: https://bugzilla.redhat.com/show_bug.cgi?id=2208447 
│                             │                  ├ [2]: https://github.com/libjpeg-turbo/libjpeg-turbo/commit/9f756bc67a84d4566bf74a0c2432aa55da404021 
│                             │                  ├ [3]: https://github.com/libjpeg-turbo/libjpeg-turbo/issues/668#issuecomment-1492586118 
│                             │                  ├ [4]: https://github.com/libjpeg-turbo/libjpeg-turbo/issues/675 
│                             │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2023-2804 
│                             │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-2804 
│                             ├ PublishedDate   : 2023-05-25T22:15:00Z 
│                             ╰ LastModifiedDate: 2023-06-06T13:40:00Z 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ╰ Vulnerabilities ╭ [0] ╭ VulnerabilityID : CVE-2023-26048 
                        │     ├ PkgName         : org.eclipse.jetty:jetty-client 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ InstalledVersion: 9.4.50.v20221201 
                        │     ├ FixedVersion    : 9.4.51.v20230217, 10.0.14, 11.0.14 
                        │     ├ Layer            ╭ Digest: sha256:4bd636f0a6b69e68e5cc9810353492fbc0c73895fa1a31f6def8d4817c4aeff1 
                        │     │                  ╰ DiffID: sha256:616f28a7f8dbd7550739728498d1bc7cceff76b35a95e43a39fb4001f92968d4 
                        │     ├ SeveritySource  : nvd 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-26048 
                        │     ├ DataSource       ╭ ID  : glad 
                        │     │                  ├ Name: GitLab Advisory Database Community 
                        │     │                  ╰ URL : https://gitlab.com/gitlab-org/advisories-community 
                        │     ├ Title           : OutOfMemoryError for large multipart without filename in Eclipse Jetty 
                        │     ├ Description     : Jetty is a java based web server and servlet engine. In affected versions servlets with multipart
                        │     │                   support (e.g. annotated with `@MultipartConfig`) that call `HttpServletRequest.getParameter()` or
                        │     │                   `HttpServletRequest.getParts()` may cause `OutOfMemoryError` when the client sends a multipart request with a
                        │     │                    part that has a name but no filename and very large content. This happens even with the default settings of
                        │     │                   `fileSizeThreshold=0` which should stream the whole part content to disk. An attacker client may send a large
                        │     │                    multipart request and cause the server to throw `OutOfMemoryError`. However, the server may be able to
                        │     │                   recover after the `OutOfMemoryError` and continue its service -- although it may take some time. This issue
                        │     │                   has been patched in versions 9.4.51, 10.0.14, and 11.0.14. Users are advised to upgrade. Users unable to
                        │     │                   upgrade may set the multipart parameter `maxRequestSize` which must be set to a non-negative value, so the
                        │     │                   whole multipart content is limited (although still read into memory). 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-770 
                        │     ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L 
                        │     │                  │      ╰ V3Score : 5.3 
                        │     │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L 
                        │     │                         ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26048 
                        │     │                  ├ [1]: https://github.com/advisories/GHSA-qw69-rqj8-6qw8 
                        │     │                  ├ [2]: https://github.com/eclipse/jetty.project/issues/9076 
                        │     │                  ├ [3]: https://github.com/eclipse/jetty.project/pull/9344 
                        │     │                  ├ [4]: https://github.com/eclipse/jetty.project/pull/9345 
                        │     │                  ├ [5]: https://github.com/eclipse/jetty.project/releases/tag/jetty-9.4.51.v20230217 
                        │     │                  ├ [6]: https://github.com/eclipse/jetty.project/security/advisories/GHSA-qw69-rqj8-6qw8 
                        │     │                  ├ [7]: https://github.com/jakartaee/servlet/blob/6.0.0/spec/src/main/asciidoc/servlet-spec-body.adoc#32-f
                        │     │                  │      ile-upload 
                        │     │                  ├ [8]: https://nvd.nist.gov/vuln/detail/CVE-2023-26048 
                        │     │                  ╰ [9]: https://security.netapp.com/advisory/ntap-20230526-0001/ 
                        │     ├ PublishedDate   : 2023-04-18T21:15:00Z 
                        │     ╰ LastModifiedDate: 2023-05-26T20:15:00Z 
                        ├ [1] ╭ VulnerabilityID : CVE-2023-26049 
                        │     ├ PkgName         : org.eclipse.jetty:jetty-client 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ InstalledVersion: 9.4.50.v20221201 
                        │     ├ FixedVersion    : 9.4.51.v20230217, 10.0.14, 11.0.14 
                        │     ├ Layer            ╭ Digest: sha256:4bd636f0a6b69e68e5cc9810353492fbc0c73895fa1a31f6def8d4817c4aeff1 
                        │     │                  ╰ DiffID: sha256:616f28a7f8dbd7550739728498d1bc7cceff76b35a95e43a39fb4001f92968d4 
                        │     ├ SeveritySource  : nvd 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-26049 
                        │     ├ DataSource       ╭ ID  : glad 
                        │     │                  ├ Name: GitLab Advisory Database Community 
                        │     │                  ╰ URL : https://gitlab.com/gitlab-org/advisories-community 
                        │     ├ Title           : Eclipse Jetty's cookie parsing of quoted values can exfiltrate values from other cookies 
                        │     ├ Description     : Jetty is a java based web server and servlet engine. Nonstandard cookie parsing in Jetty may allow an
                        │     │                   attacker to smuggle cookies within other cookies, or otherwise perform unintended behavior by tampering with
                        │     │                   the cookie parsing mechanism. If Jetty sees a cookie VALUE that starts with `"` (double quote), it will
                        │     │                   continue to read the cookie string until it sees a closing quote -- even if a semicolon is encountered. So, a
                        │     │                    cookie header such as: `DISPLAY_LANGUAGE="b; JSESSIONID=1337; c=d"` will be parsed as one cookie, with the
                        │     │                   name DISPLAY_LANGUAGE and a value of b; JSESSIONID=1337; c=d instead of 3 separate cookies. This has security
                        │     │                    implications because if, say, JSESSIONID is an HttpOnly cookie, and the DISPLAY_LANGUAGE cookie value is
                        │     │                   rendered on the page, an attacker can smuggle the JSESSIONID cookie into the DISPLAY_LANGUAGE cookie and
                        │     │                   thereby exfiltrate it. This is significant when an intermediary is enacting some policy based on cookies, so
                        │     │                   a smuggled cookie can bypass that policy yet still be seen by the Jetty server or its logging system. This
                        │     │                   issue has been addressed in versions 9.4.51, 10.0.14, 11.0.14, and 12.0.0.beta0 and users are advised to
                        │     │                   upgrade. There are no known workarounds for this issue. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:U/C:L/I:N/A:N 
                        │     │                  │      ╰ V3Score : 2.4 
                        │     │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N 
                        │     │                         ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26049 
                        │     │                  ├ [1]: https://github.com/advisories/GHSA-p26g-97m4-6q7c 
                        │     │                  ├ [2]: https://github.com/eclipse/jetty.project/pull/9339 
                        │     │                  ├ [3]: https://github.com/eclipse/jetty.project/pull/9352 
                        │     │                  ├ [4]: https://github.com/eclipse/jetty.project/releases/tag/jetty-9.4.51.v20230217 
                        │     │                  ├ [5]: https://github.com/eclipse/jetty.project/security/advisories/GHSA-p26g-97m4-6q7c 
                        │     │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-26049 
                        │     │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230526-0001/ 
                        │     │                  ├ [8]: https://www.rfc-editor.org/rfc/rfc2965 
                        │     │                  ╰ [9]: https://www.rfc-editor.org/rfc/rfc6265 
                        │     ├ PublishedDate   : 2023-04-18T21:15:00Z 
                        │     ╰ LastModifiedDate: 2023-05-26T20:15:00Z 
                        ├ [2] ╭ VulnerabilityID : CVE-2023-26048 
                        │     ├ PkgName         : org.eclipse.jetty:jetty-http 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ InstalledVersion: 9.4.50.v20221201 
                        │     ├ FixedVersion    : 9.4.51.v20230217, 10.0.14, 11.0.14 
                        │     ├ Layer            ╭ Digest: sha256:4bd636f0a6b69e68e5cc9810353492fbc0c73895fa1a31f6def8d4817c4aeff1 
                        │     │                  ╰ DiffID: sha256:616f28a7f8dbd7550739728498d1bc7cceff76b35a95e43a39fb4001f92968d4 
                        │     ├ SeveritySource  : nvd 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-26048 
                        │     ├ DataSource       ╭ ID  : glad 
                        │     │                  ├ Name: GitLab Advisory Database Community 
                        │     │                  ╰ URL : https://gitlab.com/gitlab-org/advisories-community 
                        │     ├ Title           : OutOfMemoryError for large multipart without filename in Eclipse Jetty 
                        │     ├ Description     : Jetty is a java based web server and servlet engine. In affected versions servlets with multipart
                        │     │                   support (e.g. annotated with `@MultipartConfig`) that call `HttpServletRequest.getParameter()` or
                        │     │                   `HttpServletRequest.getParts()` may cause `OutOfMemoryError` when the client sends a multipart request with a
                        │     │                    part that has a name but no filename and very large content. This happens even with the default settings of
                        │     │                   `fileSizeThreshold=0` which should stream the whole part content to disk. An attacker client may send a large
                        │     │                    multipart request and cause the server to throw `OutOfMemoryError`. However, the server may be able to
                        │     │                   recover after the `OutOfMemoryError` and continue its service -- although it may take some time. This issue
                        │     │                   has been patched in versions 9.4.51, 10.0.14, and 11.0.14. Users are advised to upgrade. Users unable to
                        │     │                   upgrade may set the multipart parameter `maxRequestSize` which must be set to a non-negative value, so the
                        │     │                   whole multipart content is limited (although still read into memory). 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-770 
                        │     ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L 
                        │     │                  │      ╰ V3Score : 5.3 
                        │     │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L 
                        │     │                         ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26048 
                        │     │                  ├ [1]: https://github.com/advisories/GHSA-qw69-rqj8-6qw8 
                        │     │                  ├ [2]: https://github.com/eclipse/jetty.project/issues/9076 
                        │     │                  ├ [3]: https://github.com/eclipse/jetty.project/pull/9344 
                        │     │                  ├ [4]: https://github.com/eclipse/jetty.project/pull/9345 
                        │     │                  ├ [5]: https://github.com/eclipse/jetty.project/releases/tag/jetty-9.4.51.v20230217 
                        │     │                  ├ [6]: https://github.com/eclipse/jetty.project/security/advisories/GHSA-qw69-rqj8-6qw8 
                        │     │                  ├ [7]: https://github.com/jakartaee/servlet/blob/6.0.0/spec/src/main/asciidoc/servlet-spec-body.adoc#32-f
                        │     │                  │      ile-upload 
                        │     │                  ├ [8]: https://nvd.nist.gov/vuln/detail/CVE-2023-26048 
                        │     │                  ╰ [9]: https://security.netapp.com/advisory/ntap-20230526-0001/ 
                        │     ├ PublishedDate   : 2023-04-18T21:15:00Z 
                        │     ╰ LastModifiedDate: 2023-05-26T20:15:00Z 
                        ├ [3] ╭ VulnerabilityID : CVE-2023-26049 
                        │     ├ PkgName         : org.eclipse.jetty:jetty-http 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ InstalledVersion: 9.4.50.v20221201 
                        │     ├ FixedVersion    : 9.4.51.v20230217, 10.0.14, 11.0.14 
                        │     ├ Layer            ╭ Digest: sha256:4bd636f0a6b69e68e5cc9810353492fbc0c73895fa1a31f6def8d4817c4aeff1 
                        │     │                  ╰ DiffID: sha256:616f28a7f8dbd7550739728498d1bc7cceff76b35a95e43a39fb4001f92968d4 
                        │     ├ SeveritySource  : nvd 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-26049 
                        │     ├ DataSource       ╭ ID  : glad 
                        │     │                  ├ Name: GitLab Advisory Database Community 
                        │     │                  ╰ URL : https://gitlab.com/gitlab-org/advisories-community 
                        │     ├ Title           : Eclipse Jetty's cookie parsing of quoted values can exfiltrate values from other cookies 
                        │     ├ Description     : Jetty is a java based web server and servlet engine. Nonstandard cookie parsing in Jetty may allow an
                        │     │                   attacker to smuggle cookies within other cookies, or otherwise perform unintended behavior by tampering with
                        │     │                   the cookie parsing mechanism. If Jetty sees a cookie VALUE that starts with `"` (double quote), it will
                        │     │                   continue to read the cookie string until it sees a closing quote -- even if a semicolon is encountered. So, a
                        │     │                    cookie header such as: `DISPLAY_LANGUAGE="b; JSESSIONID=1337; c=d"` will be parsed as one cookie, with the
                        │     │                   name DISPLAY_LANGUAGE and a value of b; JSESSIONID=1337; c=d instead of 3 separate cookies. This has security
                        │     │                    implications because if, say, JSESSIONID is an HttpOnly cookie, and the DISPLAY_LANGUAGE cookie value is
                        │     │                   rendered on the page, an attacker can smuggle the JSESSIONID cookie into the DISPLAY_LANGUAGE cookie and
                        │     │                   thereby exfiltrate it. This is significant when an intermediary is enacting some policy based on cookies, so
                        │     │                   a smuggled cookie can bypass that policy yet still be seen by the Jetty server or its logging system. This
                        │     │                   issue has been addressed in versions 9.4.51, 10.0.14, 11.0.14, and 12.0.0.beta0 and users are advised to
                        │     │                   upgrade. There are no known workarounds for this issue. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:U/C:L/I:N/A:N 
                        │     │                  │      ╰ V3Score : 2.4 
                        │     │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N 
                        │     │                         ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26049 
                        │     │                  ├ [1]: https://github.com/advisories/GHSA-p26g-97m4-6q7c 
                        │     │                  ├ [2]: https://github.com/eclipse/jetty.project/pull/9339 
                        │     │                  ├ [3]: https://github.com/eclipse/jetty.project/pull/9352 
                        │     │                  ├ [4]: https://github.com/eclipse/jetty.project/releases/tag/jetty-9.4.51.v20230217 
                        │     │                  ├ [5]: https://github.com/eclipse/jetty.project/security/advisories/GHSA-p26g-97m4-6q7c 
                        │     │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-26049 
                        │     │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230526-0001/ 
                        │     │                  ├ [8]: https://www.rfc-editor.org/rfc/rfc2965 
                        │     │                  ╰ [9]: https://www.rfc-editor.org/rfc/rfc6265 
                        │     ├ PublishedDate   : 2023-04-18T21:15:00Z 
                        │     ╰ LastModifiedDate: 2023-05-26T20:15:00Z 
                        ├ [4] ╭ VulnerabilityID : CVE-2023-26048 
                        │     ├ PkgName         : org.eclipse.jetty:jetty-io 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ InstalledVersion: 9.4.50.v20221201 
                        │     ├ FixedVersion    : 9.4.51.v20230217, 10.0.14, 11.0.14 
                        │     ├ Layer            ╭ Digest: sha256:4bd636f0a6b69e68e5cc9810353492fbc0c73895fa1a31f6def8d4817c4aeff1 
                        │     │                  ╰ DiffID: sha256:616f28a7f8dbd7550739728498d1bc7cceff76b35a95e43a39fb4001f92968d4 
                        │     ├ SeveritySource  : nvd 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-26048 
                        │     ├ DataSource       ╭ ID  : glad 
                        │     │                  ├ Name: GitLab Advisory Database Community 
                        │     │                  ╰ URL : https://gitlab.com/gitlab-org/advisories-community 
                        │     ├ Title           : OutOfMemoryError for large multipart without filename in Eclipse Jetty 
                        │     ├ Description     : Jetty is a java based web server and servlet engine. In affected versions servlets with multipart
                        │     │                   support (e.g. annotated with `@MultipartConfig`) that call `HttpServletRequest.getParameter()` or
                        │     │                   `HttpServletRequest.getParts()` may cause `OutOfMemoryError` when the client sends a multipart request with a
                        │     │                    part that has a name but no filename and very large content. This happens even with the default settings of
                        │     │                   `fileSizeThreshold=0` which should stream the whole part content to disk. An attacker client may send a large
                        │     │                    multipart request and cause the server to throw `OutOfMemoryError`. However, the server may be able to
                        │     │                   recover after the `OutOfMemoryError` and continue its service -- although it may take some time. This issue
                        │     │                   has been patched in versions 9.4.51, 10.0.14, and 11.0.14. Users are advised to upgrade. Users unable to
                        │     │                   upgrade may set the multipart parameter `maxRequestSize` which must be set to a non-negative value, so the
                        │     │                   whole multipart content is limited (although still read into memory). 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-770 
                        │     ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L 
                        │     │                  │      ╰ V3Score : 5.3 
                        │     │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L 
                        │     │                         ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26048 
                        │     │                  ├ [1]: https://github.com/advisories/GHSA-qw69-rqj8-6qw8 
                        │     │                  ├ [2]: https://github.com/eclipse/jetty.project/issues/9076 
                        │     │                  ├ [3]: https://github.com/eclipse/jetty.project/pull/9344 
                        │     │                  ├ [4]: https://github.com/eclipse/jetty.project/pull/9345 
                        │     │                  ├ [5]: https://github.com/eclipse/jetty.project/releases/tag/jetty-9.4.51.v20230217 
                        │     │                  ├ [6]: https://github.com/eclipse/jetty.project/security/advisories/GHSA-qw69-rqj8-6qw8 
                        │     │                  ├ [7]: https://github.com/jakartaee/servlet/blob/6.0.0/spec/src/main/asciidoc/servlet-spec-body.adoc#32-f
                        │     │                  │      ile-upload 
                        │     │                  ├ [8]: https://nvd.nist.gov/vuln/detail/CVE-2023-26048 
                        │     │                  ╰ [9]: https://security.netapp.com/advisory/ntap-20230526-0001/ 
                        │     ├ PublishedDate   : 2023-04-18T21:15:00Z 
                        │     ╰ LastModifiedDate: 2023-05-26T20:15:00Z 
                        ├ [5] ╭ VulnerabilityID : CVE-2023-26049 
                        │     ├ PkgName         : org.eclipse.jetty:jetty-io 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ InstalledVersion: 9.4.50.v20221201 
                        │     ├ FixedVersion    : 9.4.51.v20230217, 10.0.14, 11.0.14 
                        │     ├ Layer            ╭ Digest: sha256:4bd636f0a6b69e68e5cc9810353492fbc0c73895fa1a31f6def8d4817c4aeff1 
                        │     │                  ╰ DiffID: sha256:616f28a7f8dbd7550739728498d1bc7cceff76b35a95e43a39fb4001f92968d4 
                        │     ├ SeveritySource  : nvd 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-26049 
                        │     ├ DataSource       ╭ ID  : glad 
                        │     │                  ├ Name: GitLab Advisory Database Community 
                        │     │                  ╰ URL : https://gitlab.com/gitlab-org/advisories-community 
                        │     ├ Title           : Eclipse Jetty's cookie parsing of quoted values can exfiltrate values from other cookies 
                        │     ├ Description     : Jetty is a java based web server and servlet engine. Nonstandard cookie parsing in Jetty may allow an
                        │     │                   attacker to smuggle cookies within other cookies, or otherwise perform unintended behavior by tampering with
                        │     │                   the cookie parsing mechanism. If Jetty sees a cookie VALUE that starts with `"` (double quote), it will
                        │     │                   continue to read the cookie string until it sees a closing quote -- even if a semicolon is encountered. So, a
                        │     │                    cookie header such as: `DISPLAY_LANGUAGE="b; JSESSIONID=1337; c=d"` will be parsed as one cookie, with the
                        │     │                   name DISPLAY_LANGUAGE and a value of b; JSESSIONID=1337; c=d instead of 3 separate cookies. This has security
                        │     │                    implications because if, say, JSESSIONID is an HttpOnly cookie, and the DISPLAY_LANGUAGE cookie value is
                        │     │                   rendered on the page, an attacker can smuggle the JSESSIONID cookie into the DISPLAY_LANGUAGE cookie and
                        │     │                   thereby exfiltrate it. This is significant when an intermediary is enacting some policy based on cookies, so
                        │     │                   a smuggled cookie can bypass that policy yet still be seen by the Jetty server or its logging system. This
                        │     │                   issue has been addressed in versions 9.4.51, 10.0.14, 11.0.14, and 12.0.0.beta0 and users are advised to
                        │     │                   upgrade. There are no known workarounds for this issue. 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:U/C:L/I:N/A:N 
                        │     │                  │      ╰ V3Score : 2.4 
                        │     │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N 
                        │     │                         ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26049 
                        │     │                  ├ [1]: https://github.com/advisories/GHSA-p26g-97m4-6q7c 
                        │     │                  ├ [2]: https://github.com/eclipse/jetty.project/pull/9339 
                        │     │                  ├ [3]: https://github.com/eclipse/jetty.project/pull/9352 
                        │     │                  ├ [4]: https://github.com/eclipse/jetty.project/releases/tag/jetty-9.4.51.v20230217 
                        │     │                  ├ [5]: https://github.com/eclipse/jetty.project/security/advisories/GHSA-p26g-97m4-6q7c 
                        │     │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-26049 
                        │     │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230526-0001/ 
                        │     │                  ├ [8]: https://www.rfc-editor.org/rfc/rfc2965 
                        │     │                  ╰ [9]: https://www.rfc-editor.org/rfc/rfc6265 
                        │     ├ PublishedDate   : 2023-04-18T21:15:00Z 
                        │     ╰ LastModifiedDate: 2023-05-26T20:15:00Z 
                        ├ [6] ╭ VulnerabilityID : CVE-2023-26048 
                        │     ├ PkgName         : org.eclipse.jetty:jetty-util 
                        │     ├ PkgPath         : openaf/openaf.jar 
                        │     ├ InstalledVersion: 9.4.50.v20221201 
                        │     ├ FixedVersion    : 9.4.51.v20230217, 10.0.14, 11.0.14 
                        │     ├ Layer            ╭ Digest: sha256:4bd636f0a6b69e68e5cc9810353492fbc0c73895fa1a31f6def8d4817c4aeff1 
                        │     │                  ╰ DiffID: sha256:616f28a7f8dbd7550739728498d1bc7cceff76b35a95e43a39fb4001f92968d4 
                        │     ├ SeveritySource  : nvd 
                        │     ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-26048 
                        │     ├ DataSource       ╭ ID  : glad 
                        │     │                  ├ Name: GitLab Advisory Database Community 
                        │     │                  ╰ URL : https://gitlab.com/gitlab-org/advisories-community 
                        │     ├ Title           : OutOfMemoryError for large multipart without filename in Eclipse Jetty 
                        │     ├ Description     : Jetty is a java based web server and servlet engine. In affected versions servlets with multipart
                        │     │                   support (e.g. annotated with `@MultipartConfig`) that call `HttpServletRequest.getParameter()` or
                        │     │                   `HttpServletRequest.getParts()` may cause `OutOfMemoryError` when the client sends a multipart request with a
                        │     │                    part that has a name but no filename and very large content. This happens even with the default settings of
                        │     │                   `fileSizeThreshold=0` which should stream the whole part content to disk. An attacker client may send a large
                        │     │                    multipart request and cause the server to throw `OutOfMemoryError`. However, the server may be able to
                        │     │                   recover after the `OutOfMemoryError` and continue its service -- although it may take some time. This issue
                        │     │                   has been patched in versions 9.4.51, 10.0.14, and 11.0.14. Users are advised to upgrade. Users unable to
                        │     │                   upgrade may set the multipart parameter `maxRequestSize` which must be set to a non-negative value, so the
                        │     │                   whole multipart content is limited (although still read into memory). 
                        │     ├ Severity        : MEDIUM 
                        │     ├ CweIDs           ─ [0]: CWE-770 
                        │     ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L 
                        │     │                  │      ╰ V3Score : 5.3 
                        │     │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L 
                        │     │                         ╰ V3Score : 5.3 
                        │     ├ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26048 
                        │     │                  ├ [1]: https://github.com/advisories/GHSA-qw69-rqj8-6qw8 
                        │     │                  ├ [2]: https://github.com/eclipse/jetty.project/issues/9076 
                        │     │                  ├ [3]: https://github.com/eclipse/jetty.project/pull/9344 
                        │     │                  ├ [4]: https://github.com/eclipse/jetty.project/pull/9345 
                        │     │                  ├ [5]: https://github.com/eclipse/jetty.project/releases/tag/jetty-9.4.51.v20230217 
                        │     │                  ├ [6]: https://github.com/eclipse/jetty.project/security/advisories/GHSA-qw69-rqj8-6qw8 
                        │     │                  ├ [7]: https://github.com/jakartaee/servlet/blob/6.0.0/spec/src/main/asciidoc/servlet-spec-body.adoc#32-f
                        │     │                  │      ile-upload 
                        │     │                  ├ [8]: https://nvd.nist.gov/vuln/detail/CVE-2023-26048 
                        │     │                  ╰ [9]: https://security.netapp.com/advisory/ntap-20230526-0001/ 
                        │     ├ PublishedDate   : 2023-04-18T21:15:00Z 
                        │     ╰ LastModifiedDate: 2023-05-26T20:15:00Z 
                        ╰ [7] ╭ VulnerabilityID : CVE-2023-26049 
                              ├ PkgName         : org.eclipse.jetty:jetty-util 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ InstalledVersion: 9.4.50.v20221201 
                              ├ FixedVersion    : 9.4.51.v20230217, 10.0.14, 11.0.14 
                              ├ Layer            ╭ Digest: sha256:4bd636f0a6b69e68e5cc9810353492fbc0c73895fa1a31f6def8d4817c4aeff1 
                              │                  ╰ DiffID: sha256:616f28a7f8dbd7550739728498d1bc7cceff76b35a95e43a39fb4001f92968d4 
                              ├ SeveritySource  : nvd 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-26049 
                              ├ DataSource       ╭ ID  : glad 
                              │                  ├ Name: GitLab Advisory Database Community 
                              │                  ╰ URL : https://gitlab.com/gitlab-org/advisories-community 
                              ├ Title           : Eclipse Jetty's cookie parsing of quoted values can exfiltrate values from other cookies 
                              ├ Description     : Jetty is a java based web server and servlet engine. Nonstandard cookie parsing in Jetty may allow an
                              │                   attacker to smuggle cookies within other cookies, or otherwise perform unintended behavior by tampering with
                              │                   the cookie parsing mechanism. If Jetty sees a cookie VALUE that starts with `"` (double quote), it will
                              │                   continue to read the cookie string until it sees a closing quote -- even if a semicolon is encountered. So, a
                              │                    cookie header such as: `DISPLAY_LANGUAGE="b; JSESSIONID=1337; c=d"` will be parsed as one cookie, with the
                              │                   name DISPLAY_LANGUAGE and a value of b; JSESSIONID=1337; c=d instead of 3 separate cookies. This has security
                              │                    implications because if, say, JSESSIONID is an HttpOnly cookie, and the DISPLAY_LANGUAGE cookie value is
                              │                   rendered on the page, an attacker can smuggle the JSESSIONID cookie into the DISPLAY_LANGUAGE cookie and
                              │                   thereby exfiltrate it. This is significant when an intermediary is enacting some policy based on cookies, so
                              │                   a smuggled cookie can bypass that policy yet still be seen by the Jetty server or its logging system. This
                              │                   issue has been addressed in versions 9.4.51, 10.0.14, 11.0.14, and 12.0.0.beta0 and users are advised to
                              │                   upgrade. There are no known workarounds for this issue. 
                              ├ Severity        : MEDIUM 
                              ├ CVSS             ╭ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:U/C:L/I:N/A:N 
                              │                  │      ╰ V3Score : 2.4 
                              │                  ╰ nvd  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N 
                              │                         ╰ V3Score : 5.3 
                              ├ References       ╭ [0]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26049 
                              │                  ├ [1]: https://github.com/advisories/GHSA-p26g-97m4-6q7c 
                              │                  ├ [2]: https://github.com/eclipse/jetty.project/pull/9339 
                              │                  ├ [3]: https://github.com/eclipse/jetty.project/pull/9352 
                              │                  ├ [4]: https://github.com/eclipse/jetty.project/releases/tag/jetty-9.4.51.v20230217 
                              │                  ├ [5]: https://github.com/eclipse/jetty.project/security/advisories/GHSA-p26g-97m4-6q7c 
                              │                  ├ [6]: https://nvd.nist.gov/vuln/detail/CVE-2023-26049 
                              │                  ├ [7]: https://security.netapp.com/advisory/ntap-20230526-0001/ 
                              │                  ├ [8]: https://www.rfc-editor.org/rfc/rfc2965 
                              │                  ╰ [9]: https://www.rfc-editor.org/rfc/rfc6265 
                              ├ PublishedDate   : 2023-04-18T21:15:00Z 
                              ╰ LastModifiedDate: 2023-05-26T20:15:00Z 
````
