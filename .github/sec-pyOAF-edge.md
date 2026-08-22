```yaml
╭ [0] ╭ Target         : openaf/pyoaf:edge (alpine 3.24.1) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-41254 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-41254 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:fe6ebca4054bf9111745eb206a1a124f65e4544012129967d6446
│                       │      │                   feb7dbc977a 
│                       │      ├ Title           : Little CMS: lcms2: mm2/Little-CMS: Little CMS: Information
│                       │      │                   disclosure or denial of service via integer overflow in
│                       │      │                   CubeSize 
│                       │      ├ Description     : Little CMS (lcms2) through 2.18 has an integer overflow in
│                       │      │                   CubeSize in cmslut.c because the overflow check is performed
│                       │      │                    after the multiplication. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-696
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ julia      : 3 
│                       │      │                  ├ nvd        : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ├ julia   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ├ nvd     ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:
│                       │      │                            │           N/A:H 
│                       │      │                            ╰ V3Score : 6.1 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://abhinavagarwal07.github.io/posts/lcms2-cubesize-overf
│                       │      │                  low/                                                         
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899             
│                       │      │                                                                               
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-41254        
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2459420                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502751                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502782                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502783                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502784                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502791                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502792                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502793                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2503636                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636          
│                       │      │                                                                               
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147
│                       │      │                                                                               
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html          
│                       │      │                                                                               
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                
│                       │      │                                                                               
│                       │      │                  https://github.com/mm2/Little-CMS/commit/da6110b1d14abc394633
│                       │      │                  a388209abd5ebedd7ab0                                         
│                       │      │                  https://github.com/mm2/Little-CMS/commit/e0641b1828d0a1af5ecb
│                       │      │                  1b11fe22f24fceefd4bc                                         
│                       │      │                  https://github.com/mm2/Little-CMS/commit/e0641b1828d0a1af5ecb
│                       │      │                  1b11fe22f24fceefd4bc#commitcomment-183284136                 
│                       │      │                  https://github.com/mm2/Little-CMS/security/advisories/GHSA-4x
│                       │      │                  p6-rcgg-m9qq                                                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-41254.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html         
│                       │      │                                                                               
│                       │      │                  https://lists.debian.org/debian-lts-announce/2026/05/msg00014
│                       │      │                  .html                                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-41254              
│                       │      │                                                                               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-2
│                       │      │                  1                                                            
│                       │      │                  https://ubuntu.com/security/notices/USN-8209-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8209-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-41254              
│                       │      │                                                                               
│                       │      │                  https://www.openwall.com/lists/oss-security/2026/04/17/16    
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-18T07:16:10.807Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:46:23.47Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-47063 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47063 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:2c7a2df6e1030fc30ca9a585664191c82a38b8c8073f5e89b2633
│                       │      │                   986335f5b04 
│                       │      ├ Title           : openjdk: Enhance Jar handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Libraries).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u491, 8u491-perf, 11.0.31,
│                       │      │                   17.0.19, 21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK:
│                       │      │                   17.0.19 and  21.0.11; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.18. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   7.5 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 7.5 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47063         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47063.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47063               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47063               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:12.19Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:50:40.373Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-62574 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-62574 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e035c56b5b474cb8db254b193c5c5717955d75aa4be99467debd6
│                       │      │                   e3ea66706fe 
│                       │      ├ Title           : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Orac ... 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Install).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u501, 11.0.32, 17.0.20, 21.0.12,
│                       │      │                   25.0.4, 26.0.2; Oracle GraalVM for JDK: 17.0.20 and 
│                       │      │                   21.0.12; Oracle GraalVM Enterprise Edition: 21.3.19. Easily
│                       │      │                   exploitable vulnerability allows low privileged attacker
│                       │      │                   with logon to the infrastructure where Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   executes to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in takeover of Oracle Java
│                       │      │                   SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. CVSS 3.1 Base Score 7.8 (Confidentiality, Integrity
│                       │      │                    and Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ─ bitnami: 3 
│                       │      ├ CVSS             ─ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:
│                       │      │                            │           H/A:H 
│                       │      │                            ╰ V3Score : 7.8 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-62574               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  https://www.oracle.com/security-alerts/cspuaug2026.html       
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:19:09.667Z 
│                       │      ╰ LastModifiedDate: 2026-08-18T21:17:09.31Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-46917 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46917 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:9fd74d8ace5a386c23ccace7c6cf90c15b22d7c4e2cff3c682ba5
│                       │      │                   05cae3064ae 
│                       │      ├ Title           : openjdk: Improve DTLS handshaking (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Easily exploitable
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via TLS to compromise Oracle Java SE, Oracle GraalVM
│                       │      │                   for JDK, Oracle GraalVM Enterprise Edition.  Successful
│                       │      │                   attacks of this vulnerability can result in unauthorized
│                       │      │                   ability to cause a partial denial of service (partial DOS)
│                       │      │                   of Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition. Note: This vulnerability can only be
│                       │      │                   exploited by supplying data to APIs in the specified
│                       │      │                   Component without using Untrusted Java Web Start
│                       │      │                   applications or Untrusted Java applets, such as through a
│                       │      │                   web service. CVSS 3.1 Base Score 5.3 (Availability impacts).
│                       │      │                     CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-46917         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-46917.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-46917               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-46917               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:01.81Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:55:54.35Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-46968 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46968 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:23ef48423364b993af58e10d7d32a0897fd38125ef3b963cc5b7f
│                       │      │                   3b19758ac73 
│                       │      ├ Title           : openjdk: Enhance TLS certificate handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: JSSE). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u491, 8u491-perf, 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Difficult to exploit
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via TLS to compromise Oracle Java SE.  Successful
│                       │      │                   attacks of this vulnerability can result in  unauthorized
│                       │      │                   creation, deletion or modification access to critical data
│                       │      │                   or all Oracle Java SE accessible data. Note: This
│                       │      │                   vulnerability can only be exploited by supplying data to
│                       │      │                   APIs in the specified Component without using Untrusted Java
│                       │      │                    Web Start applications or Untrusted Java applets, such as
│                       │      │                   through a web service. CVSS 3.1 Base Score 5.9 (Integrity
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 5.9 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 5.9 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-46968         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-46968.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-46968               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-46968               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:02.76Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T15:27:29.943Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-47021 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47021 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:30838385fc0109ab055be5ffb9ed2097c74524fb84c71201fb7b3
│                       │      │                   e81d5b2a080 
│                       │      ├ Title           : openjdk: Enhance XBM image support (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Easily exploitable vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 5.3 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-400
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47021         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47021.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47021               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47021               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:07.67Z 
│                       │      ╰ LastModifiedDate: 2026-08-12T20:17:44.44Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-47027 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47027 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:c44d5b3c4727431a9a5584fa7eba38c1d68a9d6b942bb793c7ef9
│                       │      │                   c46bd398939 
│                       │      ├ Title           : openjdk: Enhance Jar file processing (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: Libraries). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u491, 8u491-perf, 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Easily exploitable
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via multiple protocols to compromise Oracle Java SE. 
│                       │      │                    Successful attacks of this vulnerability can result in
│                       │      │                   unauthorized ability to cause a partial denial of service
│                       │      │                   (partial DOS) of Oracle Java SE. Note: This vulnerability
│                       │      │                   can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   5.3 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47027         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47027.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47027               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47027               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:08.25Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:55:05.263Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-60147 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-60147 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:b22141e56f08623f0d6481c535a33079d22eff34d9048b282d97c
│                       │      │                   4409fce2d4d 
│                       │      ├ Title           : openjdk: Improve certification checking (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u491, 8u491-perf, 11.0.31,
│                       │      │                   17.0.19, 21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK:
│                       │      │                   17.0.19 and  21.0.11; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.18. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized update,
│                       │      │                   insert or delete access to some of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data as well as  unauthorized read access to a
│                       │      │                   subset of Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition accessible data. Note: This
│                       │      │                   vulnerability can be exploited by using APIs in the
│                       │      │                   specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 6.5 (Confidentiality and Integrity impacts). 
│                       │      │                    CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │      │                  │         │           L/A:N 
│                       │      │                  │         ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │      │                            │           L/A:N 
│                       │      │                            ╰ V3Score : 6.5 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-60147         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-60147.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-60147               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-60147               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:15.407Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:49:46.977Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-47010 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47010 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:5739139503446b56c0dd0370f8cb7039517b39c5d27ff85c487ab
│                       │      │                   5503aa20ba0 
│                       │      ├ Title           : openjdk: Enhance JPEG handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: ImageIO).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 3.7 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           L/A:N 
│                       │      │                  │         ╰ V3Score : 3.7 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           L/A:N 
│                       │      │                            ╰ V3Score : 3.7 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47010         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47010.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47010               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47010               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:06.497Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T15:13:21.283Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-47059 
│                       │      ├ PkgID           : openjdk21-jre@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.11_p10-r0?arch=x86_
│                       │      │                  │       64&distro=3.24.1 
│                       │      │                  ╰ UID : f569ce2a974c0718 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47059 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e5ce738f13dca0c951115f202fe8235db6f424113d39c3b69a503
│                       │      │                   d5f4d06f457 
│                       │      ├ Title           : openjdk: Enhance AWT ImagingLib (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. This vulnerability
│                       │      │                   does not apply to Java deployments, typically in servers,
│                       │      │                   that load and run only trusted code (e.g., code installed by
│                       │      │                    an administrator). CVSS 3.1 Base Score 3.7 (Availability
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 3.7 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 3.7 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47059         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47059.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47059               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47059               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:11.727Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:51:30.65Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-41254 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ SeveritySource  : nvd 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-41254 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:db7630dad13a3a070bfcf2b632edb72f607151ef350f7c94b53da
│                       │      │                   029ce60204b 
│                       │      ├ Title           : Little CMS: lcms2: mm2/Little-CMS: Little CMS: Information
│                       │      │                   disclosure or denial of service via integer overflow in
│                       │      │                   CubeSize 
│                       │      ├ Description     : Little CMS (lcms2) through 2.18 has an integer overflow in
│                       │      │                   CubeSize in cmslut.c because the overflow check is performed
│                       │      │                    after the multiplication. 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-696
│                       │      │                  CWE-190
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 2 
│                       │      │                  ├ azure      : 2 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ julia      : 3 
│                       │      │                  ├ nvd        : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ├ julia   ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ├ nvd     ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:H 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:
│                       │      │                            │           N/A:H 
│                       │      │                            ╰ V3Score : 6.1 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://abhinavagarwal07.github.io/posts/lcms2-cubesize-overf
│                       │      │                  low/                                                         
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899             
│                       │      │                                                                               
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-41254        
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2459420                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502751                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502782                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502783                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502784                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502791                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502792                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2502793                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/2503636                          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793          
│                       │      │                                                                               
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636          
│                       │      │                                                                               
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                 
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063
│                       │      │                                                                               
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147
│                       │      │                                                                               
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html          
│                       │      │                                                                               
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                
│                       │      │                                                                               
│                       │      │                  https://github.com/mm2/Little-CMS/commit/da6110b1d14abc394633
│                       │      │                  a388209abd5ebedd7ab0                                         
│                       │      │                  https://github.com/mm2/Little-CMS/commit/e0641b1828d0a1af5ecb
│                       │      │                  1b11fe22f24fceefd4bc                                         
│                       │      │                  https://github.com/mm2/Little-CMS/commit/e0641b1828d0a1af5ecb
│                       │      │                  1b11fe22f24fceefd4bc#commitcomment-183284136                 
│                       │      │                  https://github.com/mm2/Little-CMS/security/advisories/GHSA-4x
│                       │      │                  p6-rcgg-m9qq                                                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-41254.html             
│                       │      │                                                                               
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html         
│                       │      │                                                                               
│                       │      │                  https://lists.debian.org/debian-lts-announce/2026/05/msg00014
│                       │      │                  .html                                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-41254              
│                       │      │                                                                               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-2
│                       │      │                  1                                                            
│                       │      │                  https://ubuntu.com/security/notices/USN-8209-1               
│                       │      │                                                                               
│                       │      │                  https://ubuntu.com/security/notices/USN-8209-2               
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-41254              
│                       │      │                                                                               
│                       │      │                  https://www.openwall.com/lists/oss-security/2026/04/17/16    
│                       │      │                                                                               
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-04-18T07:16:10.807Z 
│                       │      ╰ LastModifiedDate: 2026-06-17T10:46:23.47Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-47063 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47063 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:732e556fb024b7c4bd8e374fd49bde3601bb3285374480b30ecc4
│                       │      │                   2f387e6e5af 
│                       │      ├ Title           : openjdk: Enhance Jar handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Libraries).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u491, 8u491-perf, 11.0.31,
│                       │      │                   17.0.19, 21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK:
│                       │      │                   17.0.19 and  21.0.11; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.18. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized creation,
│                       │      │                   deletion or modification access to critical data or all
│                       │      │                   Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition accessible data. Note: This vulnerability
│                       │      │                    can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   7.5 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 7.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 7.5 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47063         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47063.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47063               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47063               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:12.19Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:50:40.373Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-62574 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-62574 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:021d1a287d93e016bd8cd69a7a9c3c03995eb3f6e55fe88cc75d8
│                       │      │                   1b8b9669ee7 
│                       │      ├ Title           : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Orac ... 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Install).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u501, 11.0.32, 17.0.20, 21.0.12,
│                       │      │                   25.0.4, 26.0.2; Oracle GraalVM for JDK: 17.0.20 and 
│                       │      │                   21.0.12; Oracle GraalVM Enterprise Edition: 21.3.19. Easily
│                       │      │                   exploitable vulnerability allows low privileged attacker
│                       │      │                   with logon to the infrastructure where Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   executes to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in takeover of Oracle Java
│                       │      │                   SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise
│                       │      │                   Edition. CVSS 3.1 Base Score 7.8 (Confidentiality, Integrity
│                       │      │                    and Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H). 
│                       │      ├ Severity        : HIGH 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ─ bitnami: 3 
│                       │      ├ CVSS             ─ bitnami ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:
│                       │      │                            │           H/A:H 
│                       │      │                            ╰ V3Score : 7.8 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-62574               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  https://www.oracle.com/security-alerts/cspuaug2026.html       
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:19:09.667Z 
│                       │      ╰ LastModifiedDate: 2026-08-18T21:17:09.31Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-46917 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46917 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:b58c25622ad76bd1b34cf25c3b61fc83a5bc5a15c7df7c02f390e
│                       │      │                   a459b88e659 
│                       │      ├ Title           : openjdk: Improve DTLS handshaking (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: JSSE).  Supported versions that are affected
│                       │      │                   are Oracle Java SE: 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Easily exploitable
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via TLS to compromise Oracle Java SE, Oracle GraalVM
│                       │      │                   for JDK, Oracle GraalVM Enterprise Edition.  Successful
│                       │      │                   attacks of this vulnerability can result in unauthorized
│                       │      │                   ability to cause a partial denial of service (partial DOS)
│                       │      │                   of Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM
│                       │      │                   Enterprise Edition. Note: This vulnerability can only be
│                       │      │                   exploited by supplying data to APIs in the specified
│                       │      │                   Component without using Untrusted Java Web Start
│                       │      │                   applications or Untrusted Java applets, such as through a
│                       │      │                   web service. CVSS 3.1 Base Score 5.3 (Availability impacts).
│                       │      │                     CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-46917         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-46917.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-46917               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-46917               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:01.81Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:55:54.35Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-46968 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-46968 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:2e9d59a263ed055318b05abe70887d672f1951eaa0abc642ade1c
│                       │      │                   fccf3b84003 
│                       │      ├ Title           : openjdk: Enhance TLS certificate handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: JSSE). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u491, 8u491-perf, 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Difficult to exploit
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via TLS to compromise Oracle Java SE.  Successful
│                       │      │                   attacks of this vulnerability can result in  unauthorized
│                       │      │                   creation, deletion or modification access to critical data
│                       │      │                   or all Oracle Java SE accessible data. Note: This
│                       │      │                   vulnerability can only be exploited by supplying data to
│                       │      │                   APIs in the specified Component without using Untrusted Java
│                       │      │                    Web Start applications or Untrusted Java applets, such as
│                       │      │                   through a web service. CVSS 3.1 Base Score 5.9 (Integrity
│                       │      │                   impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           H/A:N 
│                       │      │                  │         ╰ V3Score : 5.9 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           H/A:N 
│                       │      │                            ╰ V3Score : 5.9 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-46968         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-46968.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-46968               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-46968               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:02.76Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T15:27:29.943Z 
│                       ├ [15] ╭ VulnerabilityID : CVE-2026-47021 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47021 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:2dfbd3193561ff163297cdd7d9b95c6654293945b997639651f63
│                       │      │                   016b7f3211e 
│                       │      ├ Title           : openjdk: Enhance XBM image support (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: 2D).  Supported versions that are affected are
│                       │      │                   Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Easily exploitable vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in unauthorized ability to cause a
│                       │      │                   partial denial of service (partial DOS) of Oracle Java SE,
│                       │      │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 5.3 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-400
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47021         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47021.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47021               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47021               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:07.67Z 
│                       │      ╰ LastModifiedDate: 2026-08-12T20:17:44.44Z 
│                       ├ [16] ╭ VulnerabilityID : CVE-2026-47027 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47027 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:57cca1bd5ad40bc661c9ad8d253f24e0eda205194a38bb6d26e2a
│                       │      │                   914d25ff61c 
│                       │      ├ Title           : openjdk: Enhance Jar file processing (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in Oracle Java SE (component: Libraries). 
│                       │      │                   Supported versions that are affected are Oracle Java SE:
│                       │      │                   8u491, 8u491-perf, 11.0.31, 17.0.19, 21.0.11, 25.0.3,
│                       │      │                   26.0.1; Oracle GraalVM for JDK: 17.0.19 and  21.0.11; Oracle
│                       │      │                    GraalVM Enterprise Edition: 21.3.18. Easily exploitable
│                       │      │                   vulnerability allows unauthenticated attacker with network
│                       │      │                   access via multiple protocols to compromise Oracle Java SE. 
│                       │      │                    Successful attacks of this vulnerability can result in
│                       │      │                   unauthorized ability to cause a partial denial of service
│                       │      │                   (partial DOS) of Oracle Java SE. Note: This vulnerability
│                       │      │                   can be exploited by using APIs in the specified Component,
│                       │      │                   e.g., through a web service which supplies data to the APIs.
│                       │      │                    This vulnerability also applies to Java deployments,
│                       │      │                   typically in clients running sandboxed Java Web Start
│                       │      │                   applications or sandboxed Java applets, that load and run
│                       │      │                   untrusted code (e.g., code that comes from the internet) and
│                       │      │                    rely on the Java sandbox for security. CVSS 3.1 Base Score
│                       │      │                   5.3 (Availability impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           N/A:L 
│                       │      │                  │         ╰ V3Score : 5.3 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           N/A:L 
│                       │      │                            ╰ V3Score : 5.3 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47027         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47027.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47027               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47027               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:08.25Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:55:05.263Z 
│                       ├ [17] ╭ VulnerabilityID : CVE-2026-60147 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-60147 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:076f2d599af6e092dc3b3af8772ad0b8f8ab76364e8bec338a1b8
│                       │      │                   239a7b58da5 
│                       │      ├ Title           : openjdk: Improve certification checking (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: Security).  Supported versions that are
│                       │      │                   affected are Oracle Java SE: 8u491, 8u491-perf, 11.0.31,
│                       │      │                   17.0.19, 21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK:
│                       │      │                   17.0.19 and  21.0.11; Oracle GraalVM Enterprise Edition:
│                       │      │                   21.3.18. Easily exploitable vulnerability allows
│                       │      │                   unauthenticated attacker with network access via multiple
│                       │      │                   protocols to compromise Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition.  Successful attacks
│                       │      │                   of this vulnerability can result in  unauthorized update,
│                       │      │                   insert or delete access to some of Oracle Java SE, Oracle
│                       │      │                   GraalVM for JDK, Oracle GraalVM Enterprise Edition
│                       │      │                   accessible data as well as  unauthorized read access to a
│                       │      │                   subset of Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition accessible data. Note: This
│                       │      │                   vulnerability can be exploited by using APIs in the
│                       │      │                   specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 6.5 (Confidentiality and Integrity impacts). 
│                       │      │                    CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N). 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 2 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 2 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │      │                  │         │           L/A:N 
│                       │      │                  │         ╰ V3Score : 6.5 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:
│                       │      │                            │           L/A:N 
│                       │      │                            ╰ V3Score : 6.5 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-60147         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-60147.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-60147               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-60147               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:15.407Z 
│                       │      ╰ LastModifiedDate: 2026-08-03T18:49:46.977Z 
│                       ├ [18] ╭ VulnerabilityID : CVE-2026-47010 
│                       │      ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                       │      ├ PkgName         : openjdk21-jre-headless 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                       │      │                  │       arch=x86_64&distro=3.24.1 
│                       │      │                  ╰ UID : e50dcf6a51ec8089 
│                       │      ├ InstalledVersion: 21.0.11_p10-r0 
│                       │      ├ FixedVersion    : 21.0.12_p8-r0 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                       │      │                  │         4e4c9f62e347164a4006 
│                       │      │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                       │      │                            77bbbb6e1ea62d15f4ee 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47010 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:fad68cfedbd9466cdd32b02dfa68c9b1cd14f1adcb5397c97b28c
│                       │      │                   3c0853f0249 
│                       │      ├ Title           : openjdk: Enhance JPEG handling (Oracle CPU 2026-07) 
│                       │      ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                       │      │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                       │      │                    (component: ImageIO).  Supported versions that are affected
│                       │      │                    are Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                       │      │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                       │      │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                       │      │                   Difficult to exploit vulnerability allows unauthenticated
│                       │      │                   attacker with network access via multiple protocols to
│                       │      │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                       │      │                   GraalVM Enterprise Edition.  Successful attacks of this
│                       │      │                   vulnerability can result in  unauthorized update, insert or
│                       │      │                   delete access to some of Oracle Java SE, Oracle GraalVM for
│                       │      │                   JDK, Oracle GraalVM Enterprise Edition accessible data.
│                       │      │                   Note: This vulnerability can be exploited by using APIs in
│                       │      │                   the specified Component, e.g., through a web service which
│                       │      │                   supplies data to the APIs. This vulnerability also applies
│                       │      │                   to Java deployments, typically in clients running sandboxed
│                       │      │                   Java Web Start applications or sandboxed Java applets, that
│                       │      │                   load and run untrusted code (e.g., code that comes from the
│                       │      │                   internet) and rely on the Java sandbox for security. CVSS
│                       │      │                   3.1 Base Score 3.7 (Integrity impacts).  CVSS Vector:
│                       │      │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N). 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-284
│                       │      │                  
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ amazon     : 3 
│                       │      │                  ├ bitnami    : 1 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 1 
│                       │      │                  ╰ rocky      : 3 
│                       │      ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                  │         │           L/A:N 
│                       │      │                  │         ╰ V3Score : 3.7 
│                       │      │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                       │      │                            │           L/A:N 
│                       │      │                            ╰ V3Score : 3.7 
│                       │      ├ References                                                                     
│                       │      │                  ──────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-47010         
│                       │      │                  https://bugzilla.redhat.com/2459420                           
│                       │      │                  https://bugzilla.redhat.com/2502751                           
│                       │      │                  https://bugzilla.redhat.com/2502782                           
│                       │      │                  https://bugzilla.redhat.com/2502783                           
│                       │      │                  https://bugzilla.redhat.com/2502784                           
│                       │      │                  https://bugzilla.redhat.com/2502791                           
│                       │      │                  https://bugzilla.redhat.com/2502792                           
│                       │      │                  https://bugzilla.redhat.com/2502793                           
│                       │      │                  https://bugzilla.redhat.com/2503636                           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                       │      │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                       │      │                  https://creativecommons.org/licenses/by/4.0/                  
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                       │      │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                       │      │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                       │      │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                       │      │                  https://linux.oracle.com/cve/CVE-2026-47010.html              
│                       │      │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47010               
│                       │      │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-47010               
│                       │      │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                       │      │                  
│                       │      ├ PublishedDate   : 2026-07-21T22:17:06.497Z 
│                       │      ╰ LastModifiedDate: 2026-07-31T15:13:21.283Z 
│                       ╰ [19] ╭ VulnerabilityID : CVE-2026-47059 
│                              ├ PkgID           : openjdk21-jre-headless@21.0.11_p10-r0 
│                              ├ PkgName         : openjdk21-jre-headless 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.11_p10-r0?
│                              │                  │       arch=x86_64&distro=3.24.1 
│                              │                  ╰ UID : e50dcf6a51ec8089 
│                              ├ InstalledVersion: 21.0.11_p10-r0 
│                              ├ FixedVersion    : 21.0.12_p8-r0 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:e75cbaefc0433d7c5850cec05a6c533ef54d45c19126
│                              │                  │         4e4c9f62e347164a4006 
│                              │                  ╰ DiffID: sha256:6fa3fec420de0c2f78798883e529d478f398e7489ffa
│                              │                            77bbbb6e1ea62d15f4ee 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-47059 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Fingerprint     : sha256:7a213d62029a7f0025890616da566e2fe98cd79dfd258a8bda527
│                              │                   0443e1b5c2b 
│                              ├ Title           : openjdk: Enhance AWT ImagingLib (Oracle CPU 2026-07) 
│                              ├ Description     : Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK,
│                              │                    Oracle GraalVM Enterprise Edition product of Oracle Java SE
│                              │                    (component: 2D).  Supported versions that are affected are
│                              │                   Oracle Java SE: 8u491, 8u491-perf, 11.0.31, 17.0.19,
│                              │                   21.0.11, 25.0.3, 26.0.1; Oracle GraalVM for JDK: 17.0.19 and
│                              │                     21.0.11; Oracle GraalVM Enterprise Edition: 21.3.18.
│                              │                   Difficult to exploit vulnerability allows unauthenticated
│                              │                   attacker with network access via multiple protocols to
│                              │                   compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle
│                              │                   GraalVM Enterprise Edition.  Successful attacks of this
│                              │                   vulnerability can result in unauthorized ability to cause a
│                              │                   partial denial of service (partial DOS) of Oracle Java SE,
│                              │                   Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.
│                              │                   Note: This vulnerability applies to Java deployments,
│                              │                   typically in clients running sandboxed Java Web Start
│                              │                   applications or sandboxed Java applets, that load and run
│                              │                   untrusted code (e.g., code that comes from the internet) and
│                              │                    rely on the Java sandbox for security. This vulnerability
│                              │                   does not apply to Java deployments, typically in servers,
│                              │                   that load and run only trusted code (e.g., code installed by
│                              │                    an administrator). CVSS 3.1 Base Score 3.7 (Availability
│                              │                   impacts).  CVSS Vector:
│                              │                   (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L). 
│                              ├ Severity        : LOW 
│                              ├ CweIDs                  
│                              │                  ───────
│                              │                  CWE-284
│                              │                  
│                              ├ VendorSeverity   ╭ alma       : 3 
│                              │                  ├ amazon     : 3 
│                              │                  ├ bitnami    : 1 
│                              │                  ├ oracle-oval: 3 
│                              │                  ├ redhat     : 1 
│                              │                  ╰ rocky      : 3 
│                              ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                              │                  │         │           N/A:L 
│                              │                  │         ╰ V3Score : 3.7 
│                              │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:
│                              │                            │           N/A:L 
│                              │                            ╰ V3Score : 3.7 
│                              ├ References                                                                     
│                              │                  ──────────────────────────────────────────────────────────────
│                              │                  https://access.redhat.com/errata/RHSA-2026:42899              
│                              │                  https://access.redhat.com/security/cve/CVE-2026-47059         
│                              │                  https://bugzilla.redhat.com/2459420                           
│                              │                  https://bugzilla.redhat.com/2502751                           
│                              │                  https://bugzilla.redhat.com/2502782                           
│                              │                  https://bugzilla.redhat.com/2502783                           
│                              │                  https://bugzilla.redhat.com/2502784                           
│                              │                  https://bugzilla.redhat.com/2502791                           
│                              │                  https://bugzilla.redhat.com/2502792                           
│                              │                  https://bugzilla.redhat.com/2502793                           
│                              │                  https://bugzilla.redhat.com/2503636                           
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2459420           
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502751           
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502782           
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502783           
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502784           
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502791           
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502792           
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2502793           
│                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2503636           
│                              │                  https://creativecommons.org/licenses/by/4.0/                  
│                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-41254 
│                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46917 
│                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-46968 
│                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47010 
│                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47021 
│                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47027 
│                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47059 
│                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47063 
│                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-60147 
│                              │                  https://errata.almalinux.org/9/ALSA-2026-42899.html           
│                              │                  https://errata.rockylinux.org/RLSA-2026:42899                 
│                              │                  https://linux.oracle.com/cve/CVE-2026-47059.html              
│                              │                  https://linux.oracle.com/errata/ELSA-2026-42899.html          
│                              │                  https://nvd.nist.gov/vuln/detail/CVE-2026-47059               
│                              │                  https://openjdk.org/groups/vulnerability/advisories/2026-07-21
│                              │                  https://www.cve.org/CVERecord?id=CVE-2026-47059               
│                              │                  https://www.oracle.com/security-alerts/cpujul2026.html        
│                              │                  
│                              ├ PublishedDate   : 2026-07-21T22:17:11.727Z 
│                              ╰ LastModifiedDate: 2026-08-03T18:51:30.65Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages 
```
