```yaml
╭ [0] ╭ Target         : openaf/oaf:latest (alpine 3.24.4) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-114938 
│                       │      ├ PkgID           : openjdk21-jre@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.13.0.3_p1-r0?arch=x
│                       │      │                  │       86_64&distro=3.24.4 
│                       │      │                  ╰ UID : fb3717618354d5b 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114938 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:a634dde7f464030050c4aefe085c436e3632cf498bf0114cbe705
│                       │      │                   2a8d5465374 
│                       │      ├ Title           : OpenJDK: OpenJDK: remote code execution via memory
│                       │      │                   corruption on x86-64 systems with AVX-512 VBMI 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Compiler).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u511b33-perf, 17.0.21.0.3,
│                       │      │                   21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK:
│                       │      │                    17.0.21.0.3 and  21.0.13.0.3; Oracle GraalVM Enterprise
│                       │      │                   Edition: 21.3.20.0.3. Difficult to exploit vulnerability
│                       │      │                   allows unauthenticated attacker with network access via
│                       │      │                   multiple protocols to compromise Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in
│                       │      │                   takeover of Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition. Note: This vulnerability can
│                       │      │                   only be exploited by supplying data to APIs in the specified
│                       │      │                    Component without using Untrusted Java Web Start
│                       │      │                   applications or Untrusted Java applets, such as through a
│                       │      │                   web service. CVSS 3.1 Base Score 8.1 (Confidentiality,
│                       │      │                   Integrity and Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H). 
│                       │      ├ Severity        : CRITICAL 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-122
│                       │      ├ VendorSeverity   ─ redhat: 4 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 9.8 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/11/17/31     
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114938       
│                       │      │                  https://access.redhat.com/security/cve/cve-2026-114938       
│                       │      │                  https://calif.io/java4shell                                  
│                       │      │                  https://github.com/Azure/azure-functions-java-worker/issues/9
│                       │      │                  09                                                           
│                       │      │                  https://github.com/chainguard-dev/cg-skills/pull/17          
│                       │      │                                                                               
│                       │      │                  https://github.com/corretto/corretto-27/blob/27.0.1.1.4/CHANG
│                       │      │                  ELOG.md                                                      
│                       │      │                  https://news.ycombinator.com/item?id=50538240                
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114938             
│                       │      │                                                                               
│                       │      │                  https://www.cisa.gov/news-events/alerts/2026/11/17/critical-j
│                       │      │                  ava-vulnerability-requires-immediate-patching                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114938             
│                       │      │                                                                               
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html      
│                       │      ├ PublishedDate   : 2026-11-17T22:18:23.777Z 
│                       │      ╰ LastModifiedDate: 2026-11-18T13:45:37.953Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-114939 
│                       │      ├ PkgID           : openjdk21-jre@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.13.0.3_p1-r0?arch=x
│                       │      │                  │       86_64&distro=3.24.4 
│                       │      │                  ╰ UID : fb3717618354d5b 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114939 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:c68761ba2dcbeb8b727db3e08c0510763f16f63cd70bc31d4ef63
│                       │      │                   1082bd535c0 
│                       │      ├ Title           : OpenJDK: OpenJDK: The acceptor does not properly implement
│                       │      │                   RFC 4120 requirements for handling cross-realm tickets. 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JGSS).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 8u511b33, 8u511b33-perf, 11.0.33.0.3,
│                       │      │                   17.0.21.0.3,  21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle
│                       │      │                   GraalVM for JDK: 17.0.21.0.3 and  21.0.13.0.3; Oracle
│                       │      │                   GraalVM Enterprise Edition: 21.3.20.0.3. Difficult to
│                       │      │                   exploit vulnerability allows unauthenticated attacker with
│                       │      │                   network access via multiple protocols to compromise Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition.  Successful attacks of this vulnerability can
│                       │      │                   result in  unauthorized creation, deletion or modification
│                       │      │                   access to critical data or all Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data as well as  unauthorized access to critical
│                       │      │                   data or complete access to all Oracle Java SE, Oracle
│                       │      │                   accessible data. Note: This vulnerability applies to Java
│                       │      │                   deployments, typically in clients running sandboxed Java Web
│                       │      │                    Start applications or sandboxed Java applets, that load and
│                       │      │                    run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. This
│                       │      │                   vulnerability does not apply to Java deployments, typically
│                       │      │                   in servers, that load and run only trusted code (e.g., code
│                       │      │                   installed by an administrator). CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ redhat: 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114939 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114939       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114939       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:23.92Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:23.92Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-114940 
│                       │      ├ PkgID           : openjdk21-jre@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.13.0.3_p1-r0?arch=x
│                       │      │                  │       86_64&distro=3.24.4 
│                       │      │                  ╰ UID : fb3717618354d5b 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114940 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:67cb22baf1124b0bf43aac05f9bdc395551a25bcecb376bc534b6
│                       │      │                   38fa7060cfc 
│                       │      ├ Title           : OpenJDK: OpenJDK: Improve TLS client connections 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 8u511b33, 8u511b33-perf, 11.0.33.0.3,
│                       │      │                   17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle
│                       │      │                   GraalVM for JDK: 17.0.21.0.3 and  21.0.13.0.3; Oracle
│                       │      │                   GraalVM Enterprise Edition: 21.3.20.0.3. Difficult to
│                       │      │                   exploit vulnerability allows unauthenticated attacker with
│                       │      │                   network access via TLS to compromise Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized creation, deletion or modification access to
│                       │      │                   critical data or all Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition accessible data as well
│                       │      │                   as  unauthorized access to critical data or complete access
│                       │      │                   to all Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition accessible data. Note: This
│                       │      │                   vulnerability can be exploited by using APIs in the
│                       │      │                   specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 7.4 (Confidentiality and Integrity impacts). 
│                       │      │                    CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ redhat: 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114940 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114940       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114940       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.05Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.05Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-114941 
│                       │      ├ PkgID           : openjdk21-jre@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.13.0.3_p1-r0?arch=x
│                       │      │                  │       86_64&distro=3.24.4 
│                       │      │                  ╰ UID : fb3717618354d5b 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114941 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:804a5faad8784949ec74f12b5760f92836bebee6290e3cb7002b2
│                       │      │                   1b0388f8ff9 
│                       │      ├ Title           : OpenJDK: OpenJDK: Improve integer compression 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK
│                       │      │                   product of Oracle Java SE (component: Compiler).  Supported
│                       │      │                   versions that are affected are Oracle Java SE: 21.0.13.0.3,
│                       │      │                   25.0.5.0.3 and  27.0.1.0.3; Oracle GraalVM for JDK:
│                       │      │                   21.0.13.0.3. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK.  Successful attacks of this vulnerability can result in
│                       │      │                    unauthorized ability to cause a hang or frequently
│                       │      │                   repeatable crash (complete DOS) of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK as well as  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK accessible data and  unauthorized read access to a
│                       │      │                   subset of Oracle Java SE, Oracle GraalVM for JDK accessible
│                       │      │                   data. Note: This vulnerability can only be exploited by
│                       │      │                   supplying data to APIs in the specified Component without
│                       │      │                   using Untrusted Java Web Start applications or Untrusted
│                       │      │                   Java applets, such as through a web service. CVSS 3.1 Base
│                       │      │                   Score 7.0 (Confidentiality, Integrity and Availability
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ redhat: 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114941 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114941       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114941       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.177Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.177Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-114942 
│                       │      ├ PkgID           : openjdk21-jre@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.13.0.3_p1-r0?arch=x
│                       │      │                  │       86_64&distro=3.24.4 
│                       │      │                  ╰ UID : fb3717618354d5b 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114942 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e9e58a2cf5b156f8fc5f2240256aeb792219ebc8dd2468b562cd8
│                       │      │                   7dfeed6a1c5 
│                       │      ├ Title           : OpenJDK: OpenJDK: Enhance vector masks 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK
│                       │      │                   product of Oracle Java SE (component: Libraries).  Supported
│                       │      │                    versions that are affected are Oracle Java SE: 21.0.13.0.3,
│                       │      │                    25.0.5.0.3 and  27.0.1.0.3; Oracle GraalVM for JDK:
│                       │      │                   21.0.13.0.3. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK.  Successful attacks of this vulnerability can result in
│                       │      │                    unauthorized ability to cause a hang or frequently
│                       │      │                   repeatable crash (complete DOS) of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK as well as  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK accessible data and  unauthorized read access to a
│                       │      │                   subset of Oracle Java SE, Oracle GraalVM for JDK accessible
│                       │      │                   data. Note: This vulnerability can only be exploited by
│                       │      │                   supplying data to APIs in the specified Component without
│                       │      │                   using Untrusted Java Web Start applications or Untrusted
│                       │      │                   Java applets, such as through a web service. CVSS 3.1 Base
│                       │      │                   Score 7.0 (Confidentiality, Integrity and Availability
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ redhat: 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114942 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114942       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114942       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.297Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.297Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-114943 
│                       │      ├ PkgID           : openjdk21-jre@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.13.0.3_p1-r0?arch=x
│                       │      │                  │       86_64&distro=3.24.4 
│                       │      │                  ╰ UID : fb3717618354d5b 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114943 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:9c0ae031cfd4fa16c8a20c65d1edc97bbe07290e8115edd559eb4
│                       │      │                   806768342ab 
│                       │      ├ Title           : OpenJDK: OpenJDK: Enhance JFR Events 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u511b33-perf, 11.0.33.0.3,
│                       │      │                   17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle
│                       │      │                   GraalVM for JDK: 17.0.21.0.3 and  21.0.13.0.3; Oracle
│                       │      │                   GraalVM Enterprise Edition: 21.3.20.0.3. Difficult to
│                       │      │                   exploit vulnerability allows unauthenticated attacker with
│                       │      │                   network access via multiple protocols to compromise Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition.  Successful attacks of this vulnerability can
│                       │      │                   result in unauthorized ability to cause a hang or frequently
│                       │      │                    repeatable crash (complete DOS) of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition as well
│                       │      │                   as  unauthorized update, insert or delete access to some of
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   6.5 (Integrity and Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:H). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114943 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114943       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114943       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.41Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.41Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-114944 
│                       │      ├ PkgID           : openjdk21-jre@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.13.0.3_p1-r0?arch=x
│                       │      │                  │       86_64&distro=3.24.4 
│                       │      │                  ╰ UID : fb3717618354d5b 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114944 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8aa43e237ccc1c67eec2a3098aa30f07a7e8fdfabe6dbe4cd4a14
│                       │      │                   d9328a8f469 
│                       │      ├ Title           : OpenJDK: OpenJDK: Enhance JMX Connections 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Core Java Libraries).  Supported versions that
│                       │      │                   are affected are Oracle Java SE: 8u511b33, 8u511b33-perf,
│                       │      │                   11.0.33.0.3, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3,
│                       │      │                   27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3 and 
│                       │      │                   21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3.
│                       │      │                    Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized creation, deletion
│                       │      │                    or modification access to critical data or all Oracle Java
│                       │      │                   SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 5.9
│                       │      │                   (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114944 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114944       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114944       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.54Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.54Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-114945 
│                       │      ├ PkgID           : openjdk21-jre@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.13.0.3_p1-r0?arch=x
│                       │      │                  │       86_64&distro=3.24.4 
│                       │      │                  ╰ UID : fb3717618354d5b 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114945 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:fe84874302942e6afd3819863903fb49d7d08bca1e410cc5105e9
│                       │      │                   6821c308893 
│                       │      ├ Title           : OpenJDK: OpenJDK: Enhance StringBuilder checks 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK
│                       │      │                   product of Oracle Java SE (component: Libraries).  Supported
│                       │      │                    versions that are affected are Oracle Java SE: 21.0.13.0.3,
│                       │      │                    25.0.5.0.3 and  27.0.1.0.3; Oracle GraalVM for JDK:
│                       │      │                   21.0.13.0.3. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK.  Successful attacks of this vulnerability can result in
│                       │      │                     unauthorized update, insert or delete access to some of
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK accessible data.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 5.3 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114945 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114945       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114945       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.673Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.673Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-114946 
│                       │      ├ PkgID           : openjdk21-jre@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.13.0.3_p1-r0?arch=x
│                       │      │                  │       86_64&distro=3.24.4 
│                       │      │                  ╰ UID : fb3717618354d5b 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114946 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:551d17e881ae3b00e3448e3afc8c0d504092dc0c3796cad2c7686
│                       │      │                   cbef38d84a3 
│                       │      ├ Title           : OpenJDK: OpenJDK: Enhance loop handling 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Compiler).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u511b33, 8u511b33-perf,
│                       │      │                   11.0.33.0.3, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3,
│                       │      │                   27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3 and 
│                       │      │                   21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3.
│                       │      │                    Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data as
│                       │      │                   well as  unauthorized read access to a subset of Oracle Java
│                       │      │                    SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 4.8
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114946 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114946       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114946       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.793Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.793Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-114938 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.13.0.3_p1-
│                       │      │                  │       r0?arch=x86_64&distro=3.24.4 
│                       │      │                  ╰ UID : b0a26b10e64e3413 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114938 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:1b3f9f2ee6d78d84e6e45d0acd5175b8fa46284eef02842708385
│                       │      │                   ffddc610ec9 
│                       │      ├ Title           : OpenJDK: OpenJDK: remote code execution via memory
│                       │      │                   corruption on x86-64 systems with AVX-512 VBMI 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Compiler).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u511b33-perf, 17.0.21.0.3,
│                       │      │                   21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK:
│                       │      │                    17.0.21.0.3 and  21.0.13.0.3; Oracle GraalVM Enterprise
│                       │      │                   Edition: 21.3.20.0.3. Difficult to exploit vulnerability
│                       │      │                   allows unauthenticated attacker with network access via
│                       │      │                   multiple protocols to compromise Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in
│                       │      │                   takeover of Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition. Note: This vulnerability can
│                       │      │                   only be exploited by supplying data to APIs in the specified
│                       │      │                    Component without using Untrusted Java Web Start
│                       │      │                   applications or Untrusted Java applets, such as through a
│                       │      │                   web service. CVSS 3.1 Base Score 8.1 (Confidentiality,
│                       │      │                   Integrity and Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H). 
│                       │      ├ Severity        : CRITICAL 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-122
│                       │      ├ VendorSeverity   ─ redhat: 4 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 9.8 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  http://www.openwall.com/lists/oss-security/2026/11/17/31     
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114938       
│                       │      │                  https://access.redhat.com/security/cve/cve-2026-114938       
│                       │      │                  https://calif.io/java4shell                                  
│                       │      │                  https://github.com/Azure/azure-functions-java-worker/issues/9
│                       │      │                  09                                                           
│                       │      │                  https://github.com/chainguard-dev/cg-skills/pull/17          
│                       │      │                                                                               
│                       │      │                  https://github.com/corretto/corretto-27/blob/27.0.1.1.4/CHANG
│                       │      │                  ELOG.md                                                      
│                       │      │                  https://news.ycombinator.com/item?id=50538240                
│                       │      │                                                                               
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114938             
│                       │      │                                                                               
│                       │      │                  https://www.cisa.gov/news-events/alerts/2026/11/17/critical-j
│                       │      │                  ava-vulnerability-requires-immediate-patching                
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114938             
│                       │      │                                                                               
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html      
│                       │      ├ PublishedDate   : 2026-11-17T22:18:23.777Z 
│                       │      ╰ LastModifiedDate: 2026-11-18T13:45:37.953Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-114939 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.13.0.3_p1-
│                       │      │                  │       r0?arch=x86_64&distro=3.24.4 
│                       │      │                  ╰ UID : b0a26b10e64e3413 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114939 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:d75dfab4228b5f678ae02cd6e81dc3e6da85d596590451c3091e3
│                       │      │                   79aab159de9 
│                       │      ├ Title           : OpenJDK: OpenJDK: The acceptor does not properly implement
│                       │      │                   RFC 4120 requirements for handling cross-realm tickets. 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JGSS).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 8u511b33, 8u511b33-perf, 11.0.33.0.3,
│                       │      │                   17.0.21.0.3,  21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle
│                       │      │                   GraalVM for JDK: 17.0.21.0.3 and  21.0.13.0.3; Oracle
│                       │      │                   GraalVM Enterprise Edition: 21.3.20.0.3. Difficult to
│                       │      │                   exploit vulnerability allows unauthenticated attacker with
│                       │      │                   network access via multiple protocols to compromise Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition.  Successful attacks of this vulnerability can
│                       │      │                   result in  unauthorized creation, deletion or modification
│                       │      │                   access to critical data or all Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data as well as  unauthorized access to critical
│                       │      │                   data or complete access to all Oracle Java SE, Oracle
│                       │      │                   accessible data. Note: This vulnerability applies to Java
│                       │      │                   deployments, typically in clients running sandboxed Java Web
│                       │      │                    Start applications or sandboxed Java applets, that load and
│                       │      │                    run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. This
│                       │      │                   vulnerability does not apply to Java deployments, typically
│                       │      │                   in servers, that load and run only trusted code (e.g., code
│                       │      │                   installed by an administrator). CVSS 3.1 Base Score 7.4
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ redhat: 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114939 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114939       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114939       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:23.92Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:23.92Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-114940 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.13.0.3_p1-
│                       │      │                  │       r0?arch=x86_64&distro=3.24.4 
│                       │      │                  ╰ UID : b0a26b10e64e3413 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114940 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:ae3f1b8b3f8ce7eaab218fadd39696acb303e3284cbd81d7e4a63
│                       │      │                   c646c61eb97 
│                       │      ├ Title           : OpenJDK: OpenJDK: Improve TLS client connections 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 8u511b33, 8u511b33-perf, 11.0.33.0.3,
│                       │      │                   17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle
│                       │      │                   GraalVM for JDK: 17.0.21.0.3 and  21.0.13.0.3; Oracle
│                       │      │                   GraalVM Enterprise Edition: 21.3.20.0.3. Difficult to
│                       │      │                   exploit vulnerability allows unauthenticated attacker with
│                       │      │                   network access via TLS to compromise Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition. 
│                       │      │                   Successful attacks of this vulnerability can result in 
│                       │      │                   unauthorized creation, deletion or modification access to
│                       │      │                   critical data or all Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition accessible data as well
│                       │      │                   as  unauthorized access to critical data or complete access
│                       │      │                   to all Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition accessible data. Note: This
│                       │      │                   vulnerability can be exploited by using APIs in the
│                       │      │                   specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 7.4 (Confidentiality and Integrity impacts). 
│                       │      │                    CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ redhat: 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 7.4 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114940 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114940       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114940       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.05Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.05Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-114941 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.13.0.3_p1-
│                       │      │                  │       r0?arch=x86_64&distro=3.24.4 
│                       │      │                  ╰ UID : b0a26b10e64e3413 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114941 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:02c0a11a884a9cbeb29d1496f719f948faf9a9bb74444a9abf31d
│                       │      │                   b4b89cf7746 
│                       │      ├ Title           : OpenJDK: OpenJDK: Improve integer compression 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK
│                       │      │                   product of Oracle Java SE (component: Compiler).  Supported
│                       │      │                   versions that are affected are Oracle Java SE: 21.0.13.0.3,
│                       │      │                   25.0.5.0.3 and  27.0.1.0.3; Oracle GraalVM for JDK:
│                       │      │                   21.0.13.0.3. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK.  Successful attacks of this vulnerability can result in
│                       │      │                    unauthorized ability to cause a hang or frequently
│                       │      │                   repeatable crash (complete DOS) of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK as well as  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK accessible data and  unauthorized read access to a
│                       │      │                   subset of Oracle Java SE, Oracle GraalVM for JDK accessible
│                       │      │                   data. Note: This vulnerability can only be exploited by
│                       │      │                   supplying data to APIs in the specified Component without
│                       │      │                   using Untrusted Java Web Start applications or Untrusted
│                       │      │                   Java applets, such as through a web service. CVSS 3.1 Base
│                       │      │                   Score 7.0 (Confidentiality, Integrity and Availability
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ redhat: 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114941 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114941       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114941       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.177Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.177Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-114942 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.13.0.3_p1-
│                       │      │                  │       r0?arch=x86_64&distro=3.24.4 
│                       │      │                  ╰ UID : b0a26b10e64e3413 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114942 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:4eedac1b8d9d9a5af38599ad1ff15df093e42e1eac7d70e3d6448
│                       │      │                   9e06437d03a 
│                       │      ├ Title           : OpenJDK: OpenJDK: Enhance vector masks 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK
│                       │      │                   product of Oracle Java SE (component: Libraries).  Supported
│                       │      │                    versions that are affected are Oracle Java SE: 21.0.13.0.3,
│                       │      │                    25.0.5.0.3 and  27.0.1.0.3; Oracle GraalVM for JDK:
│                       │      │                   21.0.13.0.3. Difficult to exploit vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK.  Successful attacks of this vulnerability can result in
│                       │      │                    unauthorized ability to cause a hang or frequently
│                       │      │                   repeatable crash (complete DOS) of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK as well as  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK accessible data and  unauthorized read access to a
│                       │      │                   subset of Oracle Java SE, Oracle GraalVM for JDK accessible
│                       │      │                   data. Note: This vulnerability can only be exploited by
│                       │      │                   supplying data to APIs in the specified Component without
│                       │      │                   using Untrusted Java Web Start applications or Untrusted
│                       │      │                   Java applets, such as through a web service. CVSS 3.1 Base
│                       │      │                   Score 7.0 (Confidentiality, Integrity and Availability
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ VendorSeverity   ─ redhat: 3 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114942 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114942       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114942       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.297Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.297Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-114943 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.13.0.3_p1-
│                       │      │                  │       r0?arch=x86_64&distro=3.24.4 
│                       │      │                  ╰ UID : b0a26b10e64e3413 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114943 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:7f5fdfa52db6dad92b01a9137f7e2468b6adbff29d7faac50b21b
│                       │      │                   cf13e7d9766 
│                       │      ├ Title           : OpenJDK: OpenJDK: Enhance JFR Events 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Hotspot).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u511b33-perf, 11.0.33.0.3,
│                       │      │                   17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle
│                       │      │                   GraalVM for JDK: 17.0.21.0.3 and  21.0.13.0.3; Oracle
│                       │      │                   GraalVM Enterprise Edition: 21.3.20.0.3. Difficult to
│                       │      │                   exploit vulnerability allows unauthenticated attacker with
│                       │      │                   network access via multiple protocols to compromise Oracle
│                       │      │                   Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition.  Successful attacks of this vulnerability can
│                       │      │                   result in unauthorized ability to cause a hang or frequently
│                       │      │                    repeatable crash (complete DOS) of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition as well
│                       │      │                   as  unauthorized update, insert or delete access to some of
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   6.5 (Integrity and Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:H). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 6.5 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114943 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114943       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114943       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.41Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.41Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-114944 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.13.0.3_p1-
│                       │      │                  │       r0?arch=x86_64&distro=3.24.4 
│                       │      │                  ╰ UID : b0a26b10e64e3413 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114944 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:0db88f0d4a5ab22e14df7c54b1e1c43e54f4082f3ea6e7d1c1e25
│                       │      │                   c7bac8cbb16 
│                       │      ├ Title           : OpenJDK: OpenJDK: Enhance JMX Connections 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Core Java Libraries).  Supported versions that
│                       │      │                   are affected are Oracle Java SE: 8u511b33, 8u511b33-perf,
│                       │      │                   11.0.33.0.3, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3,
│                       │      │                   27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3 and 
│                       │      │                   21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3.
│                       │      │                    Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized creation, deletion
│                       │      │                    or modification access to critical data or all Oracle Java
│                       │      │                   SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 5.9
│                       │      │                   (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114944 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114944       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114944       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.54Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.54Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-114945 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.13.0.3_p1-
│                       │      │                  │       r0?arch=x86_64&distro=3.24.4 
│                       │      │                  ╰ UID : b0a26b10e64e3413 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114945 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:00cd3a8c77944af5d74cba819f0f6e2528818cd6b4abb3bebc560
│                       │      │                   a593a98be32 
│                       │      ├ Title           : OpenJDK: OpenJDK: Enhance StringBuilder checks 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK
│                       │      │                   product of Oracle Java SE (component: Libraries).  Supported
│                       │      │                    versions that are affected are Oracle Java SE: 21.0.13.0.3,
│                       │      │                    25.0.5.0.3 and  27.0.1.0.3; Oracle GraalVM for JDK:
│                       │      │                   21.0.13.0.3. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK.  Successful attacks of this vulnerability can result in
│                       │      │                     unauthorized update, insert or delete access to some of
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK accessible data.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 5.3 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114945 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114945       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114945       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.673Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.673Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2026-114946 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.13.0.3_p1-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.13.0.3_p1-
│                       │      │                  │       r0?arch=x86_64&distro=3.24.4 
│                       │      │                  ╰ UID : b0a26b10e64e3413 
│                       │      ├ InstalledVersion: 21.0.13.0.3_p1-r0 
│                       │      ├ FixedVersion    : 21.0.13.1_p2-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                       │      │                  │         e0c2eec37e22ebf6f240 
│                       │      │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                       │      │                            5d28144c37dbf4bb71d7 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-114946 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8176defac03ea05829154656c83bf89cc558d4546477132504b7d
│                       │      │                   db841a444b9 
│                       │      ├ Title           : OpenJDK: OpenJDK: Enhance loop handling 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Compiler).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u511b33, 8u511b33-perf,
│                       │      │                   11.0.33.0.3, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3,
│                       │      │                   27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3 and 
│                       │      │                   21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3.
│                       │      │                    Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data as
│                       │      │                   well as  unauthorized read access to a subset of Oracle Java
│                       │      │                    SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition accessible data. Note: This vulnerability can be
│                       │      │                   exploited by using APIs in the specified Component, e.g.,
│                       │      │                   through a web service which supplies data to the APIs. This
│                       │      │                   vulnerability also applies to Java deployments, typically in
│                       │      │                    clients running sandboxed Java Web Start applications or
│                       │      │                   sandboxed Java applets, that load and run untrusted code
│                       │      │                   (e.g., code that comes from the internet) and rely on the
│                       │      │                   Java sandbox for security. CVSS 3.1 Base Score 4.8
│                       │      │                   (Confidentiality and Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ VendorSeverity   ─ redhat: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References                                                              
│                       │      │                  ───────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-114946 
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-114946       
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-114946       
│                       │      │                  https://www.oracle.com/security-alerts/cspunov2026.html
│                       │      ├ PublishedDate   : 2026-11-17T22:18:24.793Z 
│                       │      ╰ LastModifiedDate: 2026-11-17T22:18:24.793Z 
│                       ╰ [18] ╭ VulnerabilityID : CVE-2026-4738 
│                              ├ PkgID           : zlib@1.3.2-r1 
│                              ├ PkgName         : zlib 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/zlib@1.3.2-r1?arch=x86_64&distro=3.24.4 
│                              │                  ╰ UID : 926381dc853769fb 
│                              ├ InstalledVersion: 1.3.2-r1 
│                              ├ FixedVersion    : 1.4-r0 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:e5005db9a2f95eda18f911570b68b5ea4a341cd973ed
│                              │                  │         e0c2eec37e22ebf6f240 
│                              │                  ╰ DiffID: sha256:588c1636bfe809e49d7d90762ee9e3d2a1cdabe17ed7
│                              │                            5d28144c37dbf4bb71d7 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4738 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Fingerprint     : sha256:f5256ff505f3e96c23f1cd901e4733eed2c5bfe547115def774af
│                              │                   416a22d797b 
│                              ├ Title           : Improper Restriction of Operations within the Bounds of a
│                              │                   Memory Buffe ... 
│                              ├ Description     : Improper Restriction of Operations within the Bounds of a
│                              │                   Memory Buffer vulnerability in OSGeo gdal
│                              │                   (frmts/zlib/contrib/infback9 modules). This vulnerability is
│                              │                    associated with program files inftree9.C‎.
│                              │                   
│                              │                   This issue affects gdal: before 3.11.0. 
│                              ├ Severity        : MEDIUM 
│                              ├ CweIDs                  
│                              │                  ───────
│                              │                  CWE-119
│                              ├ VendorSeverity   ╭ bitnami: 4 
│                              │                  ├ julia  : 4 
│                              │                  ╰ ubuntu : 2 
│                              ├ CVSS             ╭ bitnami ╭ V40Vector: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:P/VC:H
│                              │                  │         │            /VI:H/VA:H/SC:H/SI:H/SA:H/E:A/S:P/AU:Y
│                              │                  │         │            /R:U/V:C/RE:L/U:Amber 
│                              │                  │         ╰ V40Score : 9.4 
│                              │                  ╰ julia   ╭ V40Vector: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:P/VC:H
│                              │                            │            /VI:H/VA:H/SC:H/SI:H/SA:H/E:A/S:P/AU:Y
│                              │                            │            /R:U/V:C/RE:L/U:Amber 
│                              │                            ╰ V40Score : 9.4 
│                              ├ References                                                        
│                              │                  ─────────────────────────────────────────────────
│                              │                  https://github.com/OSGeo/gdal/pull/12244         
│                              │                  https://github.com/advisories/GHSA-hp6p-5qh5-w9fj
│                              │                  https://nvd.nist.gov/vuln/detail/CVE-2026-4738   
│                              │                  https://www.cve.org/CVERecord?id=CVE-2026-4738   
│                              ├ PublishedDate   : 2026-03-24T04:17:29Z 
│                              ╰ LastModifiedDate: 2026-06-17T10:57:09.03Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages 
```
