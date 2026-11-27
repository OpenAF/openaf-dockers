```yaml
╭ [0] ╭ Target  : openaf/oaf:deb-nightly (debian forky/sid) 
│     ├ Class   : os-pkgs 
│     ├ Type    : debian 
│     ╰ Packages 
├ [1] ╭ Target  : Java 
│     ├ Class   : lang-pkgs 
│     ├ Type    : jar 
│     ╰ Packages 
╰ [2] ╭ Target         : usr/bin/pebble 
      ├ Class          : lang-pkgs 
      ├ Type           : gobinary 
      ├ Packages        
      ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2026-97054 
                              ├ VendorIDs                    
                              │                  ────────────
                              │                  GO-2026-6859
                              ├ PkgID           : stdlib@v1.27.3 
                              ├ PkgName         : stdlib 
                              ├ PkgIdentifier    ╭ PURL: pkg:golang/stdlib@v1.27.3 
                              │                  ╰ UID : e374b4c8f0056732 
                              ├ InstalledVersion: v1.27.3 
                              ├ FixedVersion    : 1.26.11, 1.27.4 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:b0d55fd96911a1f8821a8850fc6e9d73237a185de24ac
                              │                  │         e1c181d7c3239fc4f43 
                              │                  ╰ DiffID: sha256:cd49f46787cc4148524fb829896e4d00649316877e0bd
                              │                            00942a134527614d3db 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-97054 
                              ├ DataSource       ╭ ID  : govulndb 
                              │                  ├ Name: The Go Vulnerability Database 
                              │                  ╰ URL : https://pkg.go.dev/vuln/ 
                              ├ Fingerprint     : sha256:66b3d603c580f2cfa1224b3ee8092194d32b7b50d786c95301676e
                              │                   7c9e2f9c38 
                              ├ Title           : net/http: golang: net/http: Denial of Service via race
                              │                   condition when handling oversized HTTP/1 requests 
                              ├ Description     : For HTTP/1 servers, when MaxBytesReader's limit is exceeded,
                              │                   "Connection: close" header is automatically set without
                              │                   synchronization, which might race with another header being
                              │                   set explicitly in the server handler. As a result, an HTTP/1
                              │                   server that utilizes MaxBytesReader or MaxBytesHandler can
                              │                   crash due to runtime panic if its handler reads the request
                              │                   body concurrently with writing the response header. 
                              ├ Severity        : MEDIUM 
                              ├ CweIDs                  
                              │                  ───────
                              │                  CWE-362
                              │                  CWE-820
                              ├ VendorSeverity   ╭ alma       : 2 
                              │                  ├ amazon     : 2 
                              │                  ├ bitnami    : 2 
                              │                  ├ oracle-oval: 2 
                              │                  ├ photon     : 2 
                              │                  ├ redhat     : 2 
                              │                  ╰ rocky      : 2 
                              ├ CVSS             ╭ bitnami ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
                              │                  │         │           /A:H 
                              │                  │         ╰ V3Score : 5.9 
                              │                  ╰ redhat  ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
                              │                            │           /A:H 
                              │                            ╰ V3Score : 5.9 
                              ├ References                                                                    
                              │                  ─────────────────────────────────────────────────────────────
                              │                  https://access.redhat.com/errata/RHSA-2026:102586            
                              │                  https://access.redhat.com/errata/RHSA-2026:102592            
                              │                  https://access.redhat.com/security/cve/CVE-2026-97054        
                              │                  https://bugzilla.redhat.com/2571442                          
                              │                  https://bugzilla.redhat.com/2571443                          
                              │                  https://bugzilla.redhat.com/2571444                          
                              │                  https://bugzilla.redhat.com/2571445                          
                              │                  https://bugzilla.redhat.com/2571446                          
                              │                  https://bugzilla.redhat.com/2571447                          
                              │                  https://bugzilla.redhat.com/2571448                          
                              │                  https://bugzilla.redhat.com/2571449                          
                              │                  https://bugzilla.redhat.com/2571450                          
                              │                  https://bugzilla.redhat.com/2571451                          
                              │                  https://bugzilla.redhat.com/2571452                          
                              │                  https://bugzilla.redhat.com/2571453                          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2571442          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2571443          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2571444          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2571445          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2571446          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2571447          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2571448          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2571449          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2571450          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2571451          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2571452          
                              │                  https://bugzilla.redhat.com/show_bug.cgi?id=2571453          
                              │                  https://creativecommons.org/licenses/by/4.0/                 
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97033
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97034
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97035
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97036
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97037
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97038
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97039
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97040
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97041
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97042
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97043
                              │                  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-97054
                              │                  https://errata.almalinux.org/8/ALSA-2026-102592.html         
                              │                  https://errata.rockylinux.org/RLSA-2026:102586               
                              │                  https://go.dev/cl/862185                                     
                              │                  https://go.dev/issue/82563                                   
                              │                  https://groups.google.com/g/golang-announce/c/iY8TY0wWgbM    
                              │                  https://linux.oracle.com/cve/CVE-2026-97054.html             
                              │                  https://linux.oracle.com/errata/ELSA-2026-102592.html        
                              │                  https://nvd.nist.gov/vuln/detail/CVE-2026-97054              
                              │                  https://pkg.go.dev/vuln/GO-2026-6859                         
                              │                  https://www.cve.org/CVERecord?id=CVE-2026-97054              
                              ├ PublishedDate   : 2026-11-11T05:19:58.943Z 
                              ╰ LastModifiedDate: 2026-11-16T16:17:56.29Z 
```
