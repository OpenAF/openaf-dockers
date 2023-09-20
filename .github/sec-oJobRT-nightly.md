````yaml
╭ [0] ╭ Target: openaf/ojobrt:nightly (alpine 3.18.3) 
│     ├ Class : os-pkgs 
│     ╰ Type  : alpine 
╰ [1] ╭ Target         : Java 
      ├ Class          : lang-pkgs 
      ├ Type           : jar 
      ╰ Vulnerabilities ─ [0] ╭ VulnerabilityID : CVE-2023-4759 
                              ├ PkgName         : org.eclipse.jgit:org.eclipse.jgit 
                              ├ PkgPath         : openaf/openaf.jar 
                              ├ InstalledVersion: 5.8.1.202007141445-r 
                              ├ FixedVersion    : 6.6.1.202309021850-r 
                              ├ Status          : fixed 
                              ├ Layer            ╭ Digest: sha256:071a673c51162e6a52aa7777d16356dd1ef38e6e
                              │                  │         0ab6c070ffd82d55d6f4a045 
                              │                  ╰ DiffID: sha256:020f05f5692c13d532afeabeb0d42a50fbb9c72d
                              │                            97d4edcbecd7d77c90dc0af6 
                              ├ SeveritySource  : ghsa 
                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2023-4759 
                              ├ DataSource       ╭ ID  : ghsa 
                              │                  ├ Name: GitHub Security Advisory Maven 
                              │                  ╰ URL : https://github.com/advisories?query=type%3Areview
                              │                          ed+ecosystem%3Amaven 
                              ├ Title           : arbitrary file overwrite 
                              ├ Description     : Arbitrary File Overwrite in Eclipse JGit <= 6.6.0
                              │                   
                              │                   In Eclipse JGit, all versions <= 6.6.0.202305301015-r, a
                              │                   symbolic link present in a specially crafted git repository
                              │                   can be used to write a file to locations outside the working
                              │                   tree when this repository is cloned with JGit to a
                              │                   case-insensitive filesystem, or when a checkout from a clone
                              │                   of such a repository is performed on a case-insensitive
                              │                   filesystem.
                              │                   
                              │                   This can happen on checkout (DirCacheCheckout), merge
                              │                   (ResolveMerger via its WorkingTreeUpdater), pull (PullCommand
                              │                    using merge), and when applying a patch (PatchApplier). This
                              │                    can be exploited for remote code execution (RCE), for
                              │                   instance if the file written outside the working tree is a
                              │                   git filter that gets executed on a subsequent git command.
                              │                   
                              │                   The issue occurs only on case-insensitive filesystems, like
                              │                   the default filesystems on Windows and macOS. The user
                              │                   performing the clone or checkout must have the rights to
                              │                   create symbolic links for the problem to occur, and symbolic
                              │                   links must be enabled in the git configuration.
                              │                   
                              │                   Setting git configuration option core.symlinks = false before
                              │                    checking out avoids the problem.
                              │                   
                              │                   The issue was fixed in Eclipse JGit version
                              │                   6.6.1.202309021850-r and 6.7.0.202309050840-r, available via 
                              │                    Maven Central
                              │                   https://repo1.maven.org/maven2/org/eclipse/jgit/  and 
                              │                   repo.eclipse.org
                              │                   https://repo.eclipse.org/content/repositories/jgit-releases/
                              │                   .
                              │                   
                              │                   
                              │                   The JGit maintainers would like to thank RyotaK for finding
                              │                   and reporting this issue.
                              │                   
                              │                   
                              │                   
                              │                    
                              ├ Severity        : HIGH 
                              ├ CVSS             ─ ghsa ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I
                              │                         │           :H/A:H 
                              │                         ╰ V3Score : 8.8 
                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2023-4759 
                              │                  ├ [1]: https://git.eclipse.org/c/jgit/jgit.git 
                              │                  ├ [2]: https://git.eclipse.org/c/jgit/jgit.git/commit/?id
                              │                  │      =9072103f3b3cf64dd12ad2949836ab98f62dabf1 
                              │                  ├ [3]: https://gitlab.eclipse.org/security/vulnerability-
                              │                  │      reports/-/issues/11 
                              │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2023-4759 
                              │                  ├ [5]: https://projects.eclipse.org/projects/technology.j
                              │                  │      git/releases/6.6.1 
                              │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2023-4759 
                              ├ PublishedDate   : 2023-09-12T10:15:00Z 
                              ╰ LastModifiedDate: 2023-09-12T11:51:00Z 
````
