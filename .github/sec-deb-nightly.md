````yaml
╭ [0] ╭ Target         : openaf/oaf:deb-nightly (ubuntu 25.04) 
│     ├ Class          : os-pkgs 
│     ├ Type           : ubuntu 
│     ├ Packages        ╭ [0]   ╭ ID            : apt@3.0.0 
│     │                 │       ├ Name          : apt 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/apt@3.0.0?arch=amd64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : dd37368ed7eb17af 
│     │                 │       ├ Version       : 3.0.0 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : apt 
│     │                 │       ├ SrcVersion    : 3.0.0 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: curl 
│     │                 │       │                ├ [2]: BSD-3-Clause 
│     │                 │       │                ├ [3]: MIT 
│     │                 │       │                ╰ [4]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: base-passwd@3.6.6 
│     │                 │       │                ├ [1]: gpgv@2.4.4-2ubuntu23.1 
│     │                 │       │                ├ [2]: libapt-pkg7.0@3.0.0 
│     │                 │       │                ├ [3]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [4]: libgcc-s1@15-20250404-0ubuntu1 
│     │                 │       │                ├ [5]: libseccomp2@2.5.5-1ubuntu6 
│     │                 │       │                ├ [6]: libssl3t64@3.4.1-1ubuntu4 
│     │                 │       │                ├ [7]: libstdc++6@15-20250404-0ubuntu1 
│     │                 │       │                ├ [8]: libsystemd0@257.4-1ubuntu3.2 
│     │                 │       │                ╰ [9]: ubuntu-keyring@2023.11.28.1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:b5bce5019d6fc37297775dfa79d1cef5730356e7f1015c5ec3a8d9
│     │                 │       │                 82db558be2 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/bin/apt 
│     │                 │                        ├ [1]  : /usr/bin/apt-cache 
│     │                 │                        ├ [2]  : /usr/bin/apt-cdrom 
│     │                 │                        ├ [3]  : /usr/bin/apt-config 
│     │                 │                        ├ [4]  : /usr/bin/apt-get 
│     │                 │                        ├ [5]  : /usr/bin/apt-mark 
│     │                 │                        ├ [6]  : /usr/lib/apt/apt-extracttemplates 
│     │                 │                        ├ [7]  : /usr/lib/apt/apt-helper 
│     │                 │                        ├ [8]  : /usr/lib/apt/apt.systemd.daily 
│     │                 │                        ├ [9]  : /usr/lib/apt/methods/cdrom 
│     │                 │                        ├ [10] : /usr/lib/apt/methods/copy 
│     │                 │                        ├ [11] : /usr/lib/apt/methods/file 
│     │                 │                        ├ [12] : /usr/lib/apt/methods/gpgv 
│     │                 │                        ├ [13] : /usr/lib/apt/methods/http 
│     │                 │                        ├ [14] : /usr/lib/apt/methods/mirror 
│     │                 │                        ├ [15] : /usr/lib/apt/methods/rred 
│     │                 │                        ├ [16] : /usr/lib/apt/methods/store 
│     │                 │                        ├ [17] : /usr/lib/apt/solvers/dump 
│     │                 │                        ├ [18] : /usr/lib/dpkg/methods/apt/desc.apt 
│     │                 │                        ├ [19] : /usr/lib/dpkg/methods/apt/install 
│     │                 │                        ├ [20] : /usr/lib/dpkg/methods/apt/names 
│     │                 │                        ├ [21] : /usr/lib/dpkg/methods/apt/setup 
│     │                 │                        ├ [22] : /usr/lib/dpkg/methods/apt/update 
│     │                 │                        ├ [23] : /usr/lib/systemd/system/apt-daily-upgrade.service 
│     │                 │                        ├ [24] : /usr/lib/systemd/system/apt-daily-upgrade.timer 
│     │                 │                        ├ [25] : /usr/lib/systemd/system/apt-daily.service 
│     │                 │                        ├ [26] : /usr/lib/systemd/system/apt-daily.timer 
│     │                 │                        ├ [27] : /usr/lib/x86_64-linux-gnu/libapt-private.so.0.0.0 
│     │                 │                        ├ [28] : /usr/share/apt/default-sequoia.config 
│     │                 │                        ├ [29] : /usr/share/bash-completion/completions/apt 
│     │                 │                        ├ [30] : /usr/share/bug/apt/script 
│     │                 │                        ├ [31] : /usr/share/doc/apt/README.md.gz 
│     │                 │                        ├ [32] : /usr/share/doc/apt/copyright 
│     │                 │                        ├ [33] : /usr/share/doc/apt/examples/apt.conf 
│     │                 │                        ├ [34] : /usr/share/doc/apt/examples/configure-index 
│     │                 │                        ├ [35] : /usr/share/doc/apt/examples/preferences 
│     │                 │                        ├ [36] : /usr/share/doc/apt/examples/ubuntu.sources 
│     │                 │                        ├ [37] : /usr/share/lintian/overrides/apt 
│     │                 │                        ├ [38] : /usr/share/locale/ar/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [39] : /usr/share/locale/ast/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [40] : /usr/share/locale/bg/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [41] : /usr/share/locale/bs/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [42] : /usr/share/locale/ca/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [43] : /usr/share/locale/cs/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [44] : /usr/share/locale/cy/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [45] : /usr/share/locale/da/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [46] : /usr/share/locale/de/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [47] : /usr/share/locale/dz/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [48] : /usr/share/locale/el/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [49] : /usr/share/locale/es/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [50] : /usr/share/locale/eu/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [51] : /usr/share/locale/fi/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [52] : /usr/share/locale/fr/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [53] : /usr/share/locale/gl/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [54] : /usr/share/locale/hu/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [55] : /usr/share/locale/it/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [56] : /usr/share/locale/ja/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [57] : /usr/share/locale/km/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [58] : /usr/share/locale/ko/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [59] : /usr/share/locale/ku/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [60] : /usr/share/locale/lt/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [61] : /usr/share/locale/mr/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [62] : /usr/share/locale/nb/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [63] : /usr/share/locale/ne/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [64] : /usr/share/locale/nl/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [65] : /usr/share/locale/nn/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [66] : /usr/share/locale/pl/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [67] : /usr/share/locale/pt/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [68] : /usr/share/locale/pt_BR/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [69] : /usr/share/locale/ro/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [70] : /usr/share/locale/ru/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [71] : /usr/share/locale/sk/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [72] : /usr/share/locale/sl/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [73] : /usr/share/locale/sv/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [74] : /usr/share/locale/th/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [75] : /usr/share/locale/tl/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [76] : /usr/share/locale/tr/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [77] : /usr/share/locale/uk/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [78] : /usr/share/locale/vi/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [79] : /usr/share/locale/zh_CN/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [80] : /usr/share/locale/zh_TW/LC_MESSAGES/apt.mo 
│     │                 │                        ├ [81] : /usr/share/man/de/man1/apt-transport-http.1.gz 
│     │                 │                        ├ [82] : /usr/share/man/de/man1/apt-transport-https.1.gz 
│     │                 │                        ├ [83] : /usr/share/man/de/man1/apt-transport-mirror.1.gz 
│     │                 │                        ├ [84] : /usr/share/man/de/man5/apt.conf.5.gz 
│     │                 │                        ├ [85] : /usr/share/man/de/man5/apt_auth.conf.5.gz 
│     │                 │                        ├ [86] : /usr/share/man/de/man5/apt_preferences.5.gz 
│     │                 │                        ├ [87] : /usr/share/man/de/man5/sources.list.5.gz 
│     │                 │                        ├ [88] : /usr/share/man/de/man7/apt-patterns.7.gz 
│     │                 │                        ├ [89] : /usr/share/man/de/man8/apt-cache.8.gz 
│     │                 │                        ├ [90] : /usr/share/man/de/man8/apt-cdrom.8.gz 
│     │                 │                        ├ [91] : /usr/share/man/de/man8/apt-config.8.gz 
│     │                 │                        ├ [92] : /usr/share/man/de/man8/apt-get.8.gz 
│     │                 │                        ├ [93] : /usr/share/man/de/man8/apt-mark.8.gz 
│     │                 │                        ├ [94] : /usr/share/man/de/man8/apt-secure.8.gz 
│     │                 │                        ├ [95] : /usr/share/man/de/man8/apt.8.gz 
│     │                 │                        ├ [96] : /usr/share/man/es/man5/apt_preferences.5.gz 
│     │                 │                        ├ [97] : /usr/share/man/es/man8/apt-cache.8.gz 
│     │                 │                        ├ [98] : /usr/share/man/es/man8/apt-cdrom.8.gz 
│     │                 │                        ├ [99] : /usr/share/man/es/man8/apt-config.8.gz 
│     │                 │                        ├ [100]: /usr/share/man/fr/man1/apt-transport-http.1.gz 
│     │                 │                        ├ [101]: /usr/share/man/fr/man1/apt-transport-https.1.gz 
│     │                 │                        ├ [102]: /usr/share/man/fr/man1/apt-transport-mirror.1.gz 
│     │                 │                        ├ [103]: /usr/share/man/fr/man5/apt.conf.5.gz 
│     │                 │                        ├ [104]: /usr/share/man/fr/man5/apt_auth.conf.5.gz 
│     │                 │                        ├ [105]: /usr/share/man/fr/man5/apt_preferences.5.gz 
│     │                 │                        ├ [106]: /usr/share/man/fr/man5/sources.list.5.gz 
│     │                 │                        ├ [107]: /usr/share/man/fr/man7/apt-patterns.7.gz 
│     │                 │                        ├ [108]: /usr/share/man/fr/man8/apt-cache.8.gz 
│     │                 │                        ├ [109]: /usr/share/man/fr/man8/apt-cdrom.8.gz 
│     │                 │                        ├ [110]: /usr/share/man/fr/man8/apt-config.8.gz 
│     │                 │                        ├ [111]: /usr/share/man/fr/man8/apt-get.8.gz 
│     │                 │                        ├ [112]: /usr/share/man/fr/man8/apt-mark.8.gz 
│     │                 │                        ├ [113]: /usr/share/man/fr/man8/apt-secure.8.gz 
│     │                 │                        ├ [114]: /usr/share/man/fr/man8/apt.8.gz 
│     │                 │                        ├ [115]: /usr/share/man/it/man5/apt.conf.5.gz 
│     │                 │                        ├ [116]: /usr/share/man/it/man5/apt_preferences.5.gz 
│     │                 │                        ├ [117]: /usr/share/man/it/man8/apt-cache.8.gz 
│     │                 │                        ├ [118]: /usr/share/man/it/man8/apt-cdrom.8.gz 
│     │                 │                        ├ [119]: /usr/share/man/it/man8/apt-config.8.gz 
│     │                 │                        ├ [120]: /usr/share/man/it/man8/apt-mark.8.gz 
│     │                 │                        ├ [121]: /usr/share/man/it/man8/apt.8.gz 
│     │                 │                        ├ [122]: /usr/share/man/ja/man5/apt.conf.5.gz 
│     │                 │                        ├ [123]: /usr/share/man/ja/man5/apt_preferences.5.gz 
│     │                 │                        ├ [124]: /usr/share/man/ja/man8/apt-cache.8.gz 
│     │                 │                        ├ [125]: /usr/share/man/ja/man8/apt-cdrom.8.gz 
│     │                 │                        ├ [126]: /usr/share/man/ja/man8/apt-config.8.gz 
│     │                 │                        ├ [127]: /usr/share/man/ja/man8/apt-mark.8.gz 
│     │                 │                        ├ [128]: /usr/share/man/ja/man8/apt.8.gz 
│     │                 │                        ├ [129]: /usr/share/man/man1/apt-transport-http.1.gz 
│     │                 │                        ├ [130]: /usr/share/man/man1/apt-transport-https.1.gz 
│     │                 │                        ├ [131]: /usr/share/man/man1/apt-transport-mirror.1.gz 
│     │                 │                        ├ [132]: /usr/share/man/man5/apt.conf.5.gz 
│     │                 │                        ├ [133]: /usr/share/man/man5/apt_auth.conf.5.gz 
│     │                 │                        ├ [134]: /usr/share/man/man5/apt_preferences.5.gz 
│     │                 │                        ├ [135]: /usr/share/man/man5/sources.list.5.gz 
│     │                 │                        ├ [136]: /usr/share/man/man7/apt-patterns.7.gz 
│     │                 │                        ├ [137]: /usr/share/man/man8/apt-cache.8.gz 
│     │                 │                        ├ [138]: /usr/share/man/man8/apt-cdrom.8.gz 
│     │                 │                        ├ [139]: /usr/share/man/man8/apt-config.8.gz 
│     │                 │                        ├ [140]: /usr/share/man/man8/apt-get.8.gz 
│     │                 │                        ├ [141]: /usr/share/man/man8/apt-mark.8.gz 
│     │                 │                        ├ [142]: /usr/share/man/man8/apt-secure.8.gz 
│     │                 │                        ├ [143]: /usr/share/man/man8/apt.8.gz 
│     │                 │                        ├ [144]: /usr/share/man/nl/man1/apt-transport-http.1.gz 
│     │                 │                        ├ [145]: /usr/share/man/nl/man1/apt-transport-https.1.gz 
│     │                 │                        ├ [146]: /usr/share/man/nl/man1/apt-transport-mirror.1.gz 
│     │                 │                        ├ [147]: /usr/share/man/nl/man5/apt.conf.5.gz 
│     │                 │                        ├ [148]: /usr/share/man/nl/man5/apt_auth.conf.5.gz 
│     │                 │                        ├ [149]: /usr/share/man/nl/man5/apt_preferences.5.gz 
│     │                 │                        ├ [150]: /usr/share/man/nl/man5/sources.list.5.gz 
│     │                 │                        ├ [151]: /usr/share/man/nl/man7/apt-patterns.7.gz 
│     │                 │                        ├ [152]: /usr/share/man/nl/man8/apt-cache.8.gz 
│     │                 │                        ├ [153]: /usr/share/man/nl/man8/apt-cdrom.8.gz 
│     │                 │                        ├ [154]: /usr/share/man/nl/man8/apt-config.8.gz 
│     │                 │                        ├ [155]: /usr/share/man/nl/man8/apt-get.8.gz 
│     │                 │                        ├ [156]: /usr/share/man/nl/man8/apt-mark.8.gz 
│     │                 │                        ├ [157]: /usr/share/man/nl/man8/apt-secure.8.gz 
│     │                 │                        ├ [158]: /usr/share/man/nl/man8/apt.8.gz 
│     │                 │                        ├ [159]: /usr/share/man/pl/man5/apt_preferences.5.gz 
│     │                 │                        ├ [160]: /usr/share/man/pl/man8/apt-cache.8.gz 
│     │                 │                        ├ [161]: /usr/share/man/pl/man8/apt-cdrom.8.gz 
│     │                 │                        ├ [162]: /usr/share/man/pl/man8/apt-config.8.gz 
│     │                 │                        ├ [163]: /usr/share/man/pt/man1/apt-transport-http.1.gz 
│     │                 │                        ├ [164]: /usr/share/man/pt/man1/apt-transport-https.1.gz 
│     │                 │                        ├ [165]: /usr/share/man/pt/man1/apt-transport-mirror.1.gz 
│     │                 │                        ├ [166]: /usr/share/man/pt/man5/apt.conf.5.gz 
│     │                 │                        ├ [167]: /usr/share/man/pt/man5/apt_auth.conf.5.gz 
│     │                 │                        ├ [168]: /usr/share/man/pt/man5/apt_preferences.5.gz 
│     │                 │                        ├ [169]: /usr/share/man/pt/man5/sources.list.5.gz 
│     │                 │                        ├ [170]: /usr/share/man/pt/man7/apt-patterns.7.gz 
│     │                 │                        ├ [171]: /usr/share/man/pt/man8/apt-cache.8.gz 
│     │                 │                        ├ [172]: /usr/share/man/pt/man8/apt-cdrom.8.gz 
│     │                 │                        ├ [173]: /usr/share/man/pt/man8/apt-config.8.gz 
│     │                 │                        ├ [174]: /usr/share/man/pt/man8/apt-get.8.gz 
│     │                 │                        ├ [175]: /usr/share/man/pt/man8/apt-mark.8.gz 
│     │                 │                        ├ [176]: /usr/share/man/pt/man8/apt-secure.8.gz 
│     │                 │                        ╰ [177]: /usr/share/man/pt/man8/apt.8.gz 
│     │                 ├ [1]   ╭ ID            : base-files@13.6ubuntu2 
│     │                 │       ├ Name          : base-files 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/base-files@13.6ubuntu2?arch=amd64&distr
│     │                 │       │                │       o=ubuntu-25.04 
│     │                 │       │                ╰ UID : 3bca0b3ff7ff9a95 
│     │                 │       ├ Version       : 13.6ubuntu2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : base-files 
│     │                 │       ├ SrcVersion    : 13.6ubuntu2 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ╰ [1]: verbatim 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libcrypt1@1:4.4.38-1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:08712fa60e955a6a4be46c879fa18ba90e05e109ef9100c1ef0a9d
│     │                 │       │                 39610a9265 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/locale-check 
│     │                 │                        ├ [1] : /usr/lib/os-release 
│     │                 │                        ├ [2] : /usr/lib/systemd/system/motd-news.service 
│     │                 │                        ├ [3] : /usr/lib/systemd/system/motd-news.timer 
│     │                 │                        ├ [4] : /usr/share/base-files/dot.bashrc 
│     │                 │                        ├ [5] : /usr/share/base-files/dot.profile 
│     │                 │                        ├ [6] : /usr/share/base-files/dot.profile.md5sums 
│     │                 │                        ├ [7] : /usr/share/base-files/info.dir 
│     │                 │                        ├ [8] : /usr/share/base-files/motd 
│     │                 │                        ├ [9] : /usr/share/base-files/networks 
│     │                 │                        ├ [10]: /usr/share/base-files/profile 
│     │                 │                        ├ [11]: /usr/share/base-files/profile.md5sums 
│     │                 │                        ├ [12]: /usr/share/base-files/staff-group-for-usr-local 
│     │                 │                        ├ [13]: /usr/share/common-licenses/Apache-2.0 
│     │                 │                        ├ [14]: /usr/share/common-licenses/Artistic 
│     │                 │                        ├ [15]: /usr/share/common-licenses/BSD 
│     │                 │                        ├ [16]: /usr/share/common-licenses/CC0-1.0 
│     │                 │                        ├ [17]: /usr/share/common-licenses/GFDL-1.2 
│     │                 │                        ├ [18]: /usr/share/common-licenses/GFDL-1.3 
│     │                 │                        ├ [19]: /usr/share/common-licenses/GPL-1 
│     │                 │                        ├ [20]: /usr/share/common-licenses/GPL-2 
│     │                 │                        ├ [21]: /usr/share/common-licenses/GPL-3 
│     │                 │                        ├ [22]: /usr/share/common-licenses/LGPL-2 
│     │                 │                        ├ [23]: /usr/share/common-licenses/LGPL-2.1 
│     │                 │                        ├ [24]: /usr/share/common-licenses/LGPL-3 
│     │                 │                        ├ [25]: /usr/share/common-licenses/MPL-1.1 
│     │                 │                        ├ [26]: /usr/share/common-licenses/MPL-2.0 
│     │                 │                        ├ [27]: /usr/share/doc/base-files/NEWS.Debian.gz 
│     │                 │                        ├ [28]: /usr/share/doc/base-files/README 
│     │                 │                        ├ [29]: /usr/share/doc/base-files/README.FHS 
│     │                 │                        ├ [30]: /usr/share/doc/base-files/changelog.gz 
│     │                 │                        ├ [31]: /usr/share/doc/base-files/copyright 
│     │                 │                        ├ [32]: /usr/share/dot.bashrc 
│     │                 │                        ├ [33]: /usr/share/dot.profile 
│     │                 │                        ├ [34]: /usr/share/dot.profile.md5sums 
│     │                 │                        ├ [35]: /usr/share/info.dir 
│     │                 │                        ├ [36]: /usr/share/lintian/overrides/base-files 
│     │                 │                        ├ [37]: /usr/share/motd 
│     │                 │                        ├ [38]: /usr/share/networks 
│     │                 │                        ├ [39]: /usr/share/pixmaps/ubuntu-logo-text-dark.png 
│     │                 │                        ├ [40]: /usr/share/pixmaps/ubuntu-logo-text.png 
│     │                 │                        ├ [41]: /usr/share/pixmaps/ubuntu-logo.svg 
│     │                 │                        ├ [42]: /usr/share/profile 
│     │                 │                        ├ [43]: /usr/share/profile.md5sums 
│     │                 │                        ╰ [44]: /usr/share/staff-group-for-usr-local 
│     │                 ├ [2]   ╭ ID            : base-passwd@3.6.6 
│     │                 │       ├ Name          : base-passwd 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/base-passwd@3.6.6?arch=amd64&distro=ubu
│     │                 │       │                │       ntu-25.04 
│     │                 │       │                ╰ UID : fcdeef7f9604590c 
│     │                 │       ├ Version       : 3.6.6 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : base-passwd 
│     │                 │       ├ SrcVersion    : 3.6.6 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-only 
│     │                 │       │                ╰ [1]: public-domain 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [1]: libdebconfclient0@0.277ubuntu1 
│     │                 │       │                ╰ [2]: libselinux1@3.7-3ubuntu3 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:43b0f45cf22e32b131509963b8489ee9fbcb85c26f88208b177be0
│     │                 │       │                 51978f31ad 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/sbin/update-passwd 
│     │                 │                        ├ [1] : /usr/share/base-passwd/group.master 
│     │                 │                        ├ [2] : /usr/share/base-passwd/passwd.master 
│     │                 │                        ├ [3] : /usr/share/doc-base/base-passwd.users-and-groups 
│     │                 │                        ├ [4] : /usr/share/doc/base-passwd/README 
│     │                 │                        ├ [5] : /usr/share/doc/base-passwd/changelog.gz 
│     │                 │                        ├ [6] : /usr/share/doc/base-passwd/copyright 
│     │                 │                        ├ [7] : /usr/share/doc/base-passwd/users-and-groups.html 
│     │                 │                        ├ [8] : /usr/share/doc/base-passwd/users-and-groups.txt.gz 
│     │                 │                        ├ [9] : /usr/share/lintian/overrides/base-passwd 
│     │                 │                        ├ [10]: /usr/share/man/de/man8/update-passwd.8.gz 
│     │                 │                        ├ [11]: /usr/share/man/es/man8/update-passwd.8.gz 
│     │                 │                        ├ [12]: /usr/share/man/fr/man8/update-passwd.8.gz 
│     │                 │                        ├ [13]: /usr/share/man/ja/man8/update-passwd.8.gz 
│     │                 │                        ├ [14]: /usr/share/man/man8/update-passwd.8.gz 
│     │                 │                        ├ [15]: /usr/share/man/pl/man8/update-passwd.8.gz 
│     │                 │                        ├ [16]: /usr/share/man/ro/man8/update-passwd.8.gz 
│     │                 │                        ╰ [17]: /usr/share/man/ru/man8/update-passwd.8.gz 
│     │                 ├ [3]   ╭ ID            : bash@5.2.37-1.1ubuntu1 
│     │                 │       ├ Name          : bash 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/bash@5.2.37-1.1ubuntu1?arch=amd64&distr
│     │                 │       │                │       o=ubuntu-25.04 
│     │                 │       │                ╰ UID : 8eab56d0a19de20c 
│     │                 │       ├ Version       : 5.2.37 
│     │                 │       ├ Release       : 1.1ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : bash 
│     │                 │       ├ SrcVersion    : 5.2.37 
│     │                 │       ├ SrcRelease    : 1.1ubuntu1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-3.0-or-later 
│     │                 │       │                ├ [1] : GPL-3.0-only 
│     │                 │       │                ├ [2] : GPL-3+ with Bison exception 
│     │                 │       │                ├ [3] : GPL-2.0-or-later 
│     │                 │       │                ├ [4] : GPL-2.0-only 
│     │                 │       │                ├ [5] : GFDL-1.3-no-invariants-only 
│     │                 │       │                ├ [6] : GFDL-1.3-only 
│     │                 │       │                ├ [7] : Latex2e 
│     │                 │       │                ├ [8] : BSD-4-Clause-UC 
│     │                 │       │                ├ [9] : MIT 
│     │                 │       │                ╰ [10]: permissive 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: base-files@13.6ubuntu2 
│     │                 │       │                ╰ [1]: debianutils@5.21 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:e16b87410314e44fcf0d30227bdc99866fd91e212d690cfa48f88b
│     │                 │       │                 b65b043a74 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/bash 
│     │                 │                        ├ [1] : /usr/bin/bashbug 
│     │                 │                        ├ [2] : /usr/bin/clear_console 
│     │                 │                        ├ [3] : /usr/share/debianutils/shells.d/bash 
│     │                 │                        ├ [4] : /usr/share/doc/bash/COMPAT.gz 
│     │                 │                        ├ [5] : /usr/share/doc/bash/INTRO.gz 
│     │                 │                        ├ [6] : /usr/share/doc/bash/NEWS.gz 
│     │                 │                        ├ [7] : /usr/share/doc/bash/POSIX.gz 
│     │                 │                        ├ [8] : /usr/share/doc/bash/RBASH 
│     │                 │                        ├ [9] : /usr/share/doc/bash/README.Debian.gz 
│     │                 │                        ├ [10]: /usr/share/doc/bash/README.abs-guide 
│     │                 │                        ├ [11]: /usr/share/doc/bash/README.commands.gz 
│     │                 │                        ├ [12]: /usr/share/doc/bash/README.gz 
│     │                 │                        ├ [13]: /usr/share/doc/bash/changelog.Debian.gz 
│     │                 │                        ├ [14]: /usr/share/doc/bash/copyright 
│     │                 │                        ├ [15]: /usr/share/doc/bash/inputrc.arrows 
│     │                 │                        ├ [16]: /usr/share/lintian/overrides/bash 
│     │                 │                        ├ [17]: /usr/share/man/man1/bash.1.gz 
│     │                 │                        ├ [18]: /usr/share/man/man1/bashbug.1.gz 
│     │                 │                        ├ [19]: /usr/share/man/man1/clear_console.1.gz 
│     │                 │                        ├ [20]: /usr/share/man/man1/rbash.1.gz 
│     │                 │                        ├ [21]: /usr/share/man/man7/bash-builtins.7.gz 
│     │                 │                        ╰ [22]: /usr/share/menu/bash 
│     │                 ├ [4]   ╭ ID            : bash-completion@1:2.16.0-7 
│     │                 │       ├ Name          : bash-completion 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/bash-completion@2.16.0-7?arch=all&distr
│     │                 │       │                │       o=ubuntu-25.04&epoch=1 
│     │                 │       │                ╰ UID : 5e446113d8cd7171 
│     │                 │       ├ Version       : 2.16.0 
│     │                 │       ├ Release       : 7 
│     │                 │       ├ Epoch         : 1 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : bash-completion 
│     │                 │       ├ SrcVersion    : 2.16.0 
│     │                 │       ├ SrcRelease    : 7 
│     │                 │       ├ SrcEpoch      : 1 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ╰ [1]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/bin/dh_bash-completion 
│     │                 │                        ├ [1]  : /usr/share/bash-completion/bash_completion 
│     │                 │                        ├ [2]  : /usr/share/bash-completion/completions/2to3 
│     │                 │                        ├ [3]  : /usr/share/bash-completion/completions/7z 
│     │                 │                        ├ [4]  : /usr/share/bash-completion/completions/_adb 
│     │                 │                        ├ [5]  : /usr/share/bash-completion/completions/_argc 
│     │                 │                        ├ [6]  : /usr/share/bash-completion/completions/_cal 
│     │                 │                        ├ [7]  : /usr/share/bash-completion/completions/_cargo 
│     │                 │                        ├ [8]  : /usr/share/bash-completion/completions/_chfn 
│     │                 │                        ├ [9]  : /usr/share/bash-completion/completions/_chsh 
│     │                 │                        ├ [10] : /usr/share/bash-completion/completions/_coder 
│     │                 │                        ├ [11] : /usr/share/bash-completion/completions/_delta 
│     │                 │                        ├ [12] : /usr/share/bash-completion/completions/_dmesg 
│     │                 │                        ├ [13] : /usr/share/bash-completion/completions/_eject 
│     │                 │                        ├ [14] : /usr/share/bash-completion/completions/_flamegraph 
│     │                 │                        ├ [15] : /usr/share/bash-completion/completions/_gaiacli 
│     │                 │                        ├ [16] : /usr/share/bash-completion/completions/_gh 
│     │                 │                        ├ [17] : /usr/share/bash-completion/completions/_golangci-lint 
│     │                 │                        ├ [18] : /usr/share/bash-completion/completions/_gsctl 
│     │                 │                        ├ [19] : /usr/share/bash-completion/completions/_hexdump 
│     │                 │                        ├ [20] : /usr/share/bash-completion/completions/_hwclock 
│     │                 │                        ├ [21] : /usr/share/bash-completion/completions/_insmod 
│     │                 │                        ├ [22] : /usr/share/bash-completion/completions/_ionice 
│     │                 │                        ├ [23] : /usr/share/bash-completion/completions/_jj 
│     │                 │                        ├ [24] : /usr/share/bash-completion/completions/_jungle 
│     │                 │                        ├ [25] : /usr/share/bash-completion/completions/_keyring 
│     │                 │                        ├ [26] : /usr/share/bash-completion/completions/_kontena 
│     │                 │                        ├ [27] : /usr/share/bash-completion/completions/_look 
│     │                 │                        ├ [28] : /usr/share/bash-completion/completions/_mdbook 
│     │                 │                        ├ [29] : /usr/share/bash-completion/completions/_mock 
│     │                 │                        ├ [30] : /usr/share/bash-completion/completions/_modinfo 
│     │                 │                        ├ [31] : /usr/share/bash-completion/completions/_modprobe 
│     │                 │                        ├ [32] : /usr/share/bash-completion/completions/_modules 
│     │                 │                        ├ [33] : /usr/share/bash-completion/completions/_mount 
│     │                 │                        ├ [34] : /usr/share/bash-completion/completions/_mount.linux 
│     │                 │                        ├ [35] : /usr/share/bash-completion/completions/_mtr 
│     │                 │                        ├ [36] : /usr/share/bash-completion/completions/_newgrp 
│     │                 │                        ├ [37] : /usr/share/bash-completion/completions/_nmcli 
│     │                 │                        ├ [38] : /usr/share/bash-completion/completions/_nox 
│     │                 │                        ├ [39] : /usr/share/bash-completion/completions/_nvm 
│     │                 │                        ├ [40] : /usr/share/bash-completion/completions/_pip 
│     │                 │                        ├ [41] : /usr/share/bash-completion/completions/_pipenv 
│     │                 │                        ├ [42] : /usr/share/bash-completion/completions/_renice 
│     │                 │                        ├ [43] : /usr/share/bash-completion/completions/_repomanage 
│     │                 │                        ├ [44] : /usr/share/bash-completion/completions/_reptyr 
│     │                 │                        ├ [45] : /usr/share/bash-completion/completions/_rfkill 
│     │                 │                        ├ [46] : /usr/share/bash-completion/completions/_rg 
│     │                 │                        ├ [47] : /usr/share/bash-completion/completions/_rmmod 
│     │                 │                        ├ [48] : /usr/share/bash-completion/completions/_rtcwake 
│     │                 │                        ├ [49] : /usr/share/bash-completion/completions/_ruff 
│     │                 │                        ├ [50] : /usr/share/bash-completion/completions/_runuser 
│     │                 │                        ├ [51] : /usr/share/bash-completion/completions/_rustup 
│     │                 │                        ├ [52] : /usr/share/bash-completion/completions/_secret-tool 
│     │                 │                        ├ [53] : /usr/share/bash-completion/completions/_slackpkg 
│     │                 │                        ├ [54] : /usr/share/bash-completion/completions/_sops 
│     │                 │                        ├ [55] : /usr/share/bash-completion/completions/_stern 
│     │                 │                        ├ [56] : /usr/share/bash-completion/completions/_stripe 
│     │                 │                        ├ [57] : /usr/share/bash-completion/completions/_su 
│     │                 │                        ├ [58] : /usr/share/bash-completion/completions/_svn 
│     │                 │                        ├ [59] : /usr/share/bash-completion/completions/_svnadmin 
│     │                 │                        ├ [60] : /usr/share/bash-completion/completions/_svnlook 
│     │                 │                        ├ [61] : /usr/share/bash-completion/completions/_task 
│     │                 │                        ├ [62] : /usr/share/bash-completion/completions/_tokio-console 
│     │                 │                        ├ [63] : /usr/share/bash-completion/completions/_udevadm 
│     │                 │                        ├ [64] : /usr/share/bash-completion/completions/_umount 
│     │                 │                        ├ [65] : /usr/share/bash-completion/completions/_umount.linux 
│     │                 │                        ├ [66] : /usr/share/bash-completion/completions/_uvx 
│     │                 │                        ├ [67] : /usr/share/bash-completion/completions/_vault 
│     │                 │                        ├ [68] : /usr/share/bash-completion/completions/_wasmer 
│     │                 │                        ├ [69] : /usr/share/bash-completion/completions/_write 
│     │                 │                        ├ [70] : /usr/share/bash-completion/completions/_xm 
│     │                 │                        ├ [71] : /usr/share/bash-completion/completions/_yq 
│     │                 │                        ├ [72] : /usr/share/bash-completion/completions/_yum 
│     │                 │                        ├ [73] : /usr/share/bash-completion/completions/a2x 
│     │                 │                        ├ [74] : /usr/share/bash-completion/completions/abook 
│     │                 │                        ├ [75] : /usr/share/bash-completion/completions/aclocal 
│     │                 │                        ├ [76] : /usr/share/bash-completion/completions/acpi 
│     │                 │                        ├ [77] : /usr/share/bash-completion/completions/add_members 
│     │                 │                        ├ [78] : /usr/share/bash-completion/completions/alias 
│     │                 │                        ├ [79] : /usr/share/bash-completion/completions/ant 
│     │                 │                        ├ [80] : /usr/share/bash-completion/completions/apache2ctl 
│     │                 │                        ├ [81] : /usr/share/bash-completion/completions/appdata-validate 
│     │                 │                        ├ [82] : /usr/share/bash-completion/completions/apt-build 
│     │                 │                        ├ [83] : /usr/share/bash-completion/completions/apt-cache 
│     │                 │                        ├ [84] : /usr/share/bash-completion/completions/apt-get 
│     │                 │                        ├ [85] : /usr/share/bash-completion/completions/apt-mark 
│     │                 │                        ├ [86] : /usr/share/bash-completion/completions/aptitude 
│     │                 │                        ├ [87] : /usr/share/bash-completion/completions/arch 
│     │                 │                        ├ [88] : /usr/share/bash-completion/completions/arp 
│     │                 │                        ├ [89] : /usr/share/bash-completion/completions/arping 
│     │                 │                        ├ [90] : /usr/share/bash-completion/completions/arpspoof 
│     │                 │                        ├ [91] : /usr/share/bash-completion/completions/asciidoc 
│     │                 │                        ├ [92] : /usr/share/bash-completion/completions/aspell 
│     │                 │                        ├ [93] : /usr/share/bash-completion/completions/autoconf 
│     │                 │                        ├ [94] : /usr/share/bash-completion/completions/automake 
│     │                 │                        ├ [95] : /usr/share/bash-completion/completions/autoreconf 
│     │                 │                        ├ [96] : /usr/share/bash-completion/completions/autorpm 
│     │                 │                        ├ [97] : /usr/share/bash-completion/completions/autoscan 
│     │                 │                        ├ [98] : /usr/share/bash-completion/completions/avahi-browse 
│     │                 │                        ├ [99] : /usr/share/bash-completion/completions/avctrl 
│     │                 │                        ├ [100]: /usr/share/bash-completion/completions/badblocks 
│     │                 │                        ├ [101]: /usr/share/bash-completion/completions/bind 
│     │                 │                        ├ [102]: /usr/share/bash-completion/completions/bk 
│     │                 │                        ├ [103]: /usr/share/bash-completion/completions/brctl 
│     │                 │                        ├ [104]: /usr/share/bash-completion/completions/btdownloadhead
│     │                 │                        │        less.py 
│     │                 │                        ├ [105]: /usr/share/bash-completion/completions/bzip2 
│     │                 │                        ├ [106]: /usr/share/bash-completion/completions/cancel 
│     │                 │                        ├ [107]: /usr/share/bash-completion/completions/cardctl 
│     │                 │                        ├ [108]: /usr/share/bash-completion/completions/carton 
│     │                 │                        ├ [109]: /usr/share/bash-completion/completions/ccache 
│     │                 │                        ├ [110]: /usr/share/bash-completion/completions/ccze 
│     │                 │                        ├ [111]: /usr/share/bash-completion/completions/cd 
│     │                 │                        ├ [112]: /usr/share/bash-completion/completions/cfagent 
│     │                 │                        ├ [113]: /usr/share/bash-completion/completions/cfrun 
│     │                 │                        ├ [114]: /usr/share/bash-completion/completions/chage 
│     │                 │                        ├ [115]: /usr/share/bash-completion/completions/change_pw 
│     │                 │                        ├ [116]: /usr/share/bash-completion/completions/check_db 
│     │                 │                        ├ [117]: /usr/share/bash-completion/completions/check_perms 
│     │                 │                        ├ [118]: /usr/share/bash-completion/completions/checksec 
│     │                 │                        ├ [119]: /usr/share/bash-completion/completions/chflags 
│     │                 │                        ├ [120]: /usr/share/bash-completion/completions/chgrp 
│     │                 │                        ├ [121]: /usr/share/bash-completion/completions/chkconfig 
│     │                 │                        ├ [122]: /usr/share/bash-completion/completions/chmod 
│     │                 │                        ├ [123]: /usr/share/bash-completion/completions/chown 
│     │                 │                        ├ [124]: /usr/share/bash-completion/completions/chpasswd 
│     │                 │                        ├ [125]: /usr/share/bash-completion/completions/chromium-browser 
│     │                 │                        ├ [126]: /usr/share/bash-completion/completions/chronyc 
│     │                 │                        ├ [127]: /usr/share/bash-completion/completions/chrpath 
│     │                 │                        ├ [128]: /usr/share/bash-completion/completions/cksfv 
│     │                 │                        ├ [129]: /usr/share/bash-completion/completions/cleanarch 
│     │                 │                        ├ [130]: /usr/share/bash-completion/completions/clisp 
│     │                 │                        ├ [131]: /usr/share/bash-completion/completions/clone_member 
│     │                 │                        ├ [132]: /usr/share/bash-completion/completions/complete 
│     │                 │                        ├ [133]: /usr/share/bash-completion/completions/config_list 
│     │                 │                        ├ [134]: /usr/share/bash-completion/completions/configure 
│     │                 │                        ├ [135]: /usr/share/bash-completion/completions/convert 
│     │                 │                        ├ [136]: /usr/share/bash-completion/completions/cowsay 
│     │                 │                        ├ [137]: /usr/share/bash-completion/completions/cpan2dist 
│     │                 │                        ├ [138]: /usr/share/bash-completion/completions/cpio 
│     │                 │                        ├ [139]: /usr/share/bash-completion/completions/cppcheck 
│     │                 │                        ├ [140]: /usr/share/bash-completion/completions/crontab 
│     │                 │                        ├ [141]: /usr/share/bash-completion/completions/cryptsetup 
│     │                 │                        ├ [142]: /usr/share/bash-completion/completions/curl 
│     │                 │                        ├ [143]: /usr/share/bash-completion/completions/cvs 
│     │                 │                        ├ [144]: /usr/share/bash-completion/completions/cvsps 
│     │                 │                        ├ [145]: /usr/share/bash-completion/completions/dd 
│     │                 │                        ├ [146]: /usr/share/bash-completion/completions/declare 
│     │                 │                        ├ [147]: /usr/share/bash-completion/completions/deja-dup 
│     │                 │                        ├ [148]: /usr/share/bash-completion/completions/desktop-file-v
│     │                 │                        │        alidate 
│     │                 │                        ├ [149]: /usr/share/bash-completion/completions/dhclient 
│     │                 │                        ├ [150]: /usr/share/bash-completion/completions/dict 
│     │                 │                        ├ [151]: /usr/share/bash-completion/completions/dmypy 
│     │                 │                        ├ [152]: /usr/share/bash-completion/completions/dnssec-keygen 
│     │                 │                        ├ [153]: /usr/share/bash-completion/completions/dnsspoof 
│     │                 │                        ├ [154]: /usr/share/bash-completion/completions/dot 
│     │                 │                        ├ [155]: /usr/share/bash-completion/completions/dpkg 
│     │                 │                        ├ [156]: /usr/share/bash-completion/completions/dpkg-source 
│     │                 │                        ├ [157]: /usr/share/bash-completion/completions/dselect 
│     │                 │                        ├ [158]: /usr/share/bash-completion/completions/dsniff 
│     │                 │                        ├ [159]: /usr/share/bash-completion/completions/dumpdb 
│     │                 │                        ├ [160]: /usr/share/bash-completion/completions/dumpe2fs 
│     │                 │                        ├ [161]: /usr/share/bash-completion/completions/e2freefrag 
│     │                 │                        ├ [162]: /usr/share/bash-completion/completions/e2label 
│     │                 │                        ├ [163]: /usr/share/bash-completion/completions/ebtables 
│     │                 │                        ├ [164]: /usr/share/bash-completion/completions/ecryptfs-migra
│     │                 │                        │        te-home 
│     │                 │                        ├ [165]: /usr/share/bash-completion/completions/env 
│     │                 │                        ├ [166]: /usr/share/bash-completion/completions/eog 
│     │                 │                        ├ [167]: /usr/share/bash-completion/completions/ether-wake 
│     │                 │                        ├ [168]: /usr/share/bash-completion/completions/evince 
│     │                 │                        ├ [169]: /usr/share/bash-completion/completions/explodepkg 
│     │                 │                        ├ [170]: /usr/share/bash-completion/completions/export 
│     │                 │                        ├ [171]: /usr/share/bash-completion/completions/faillog 
│     │                 │                        ├ [172]: /usr/share/bash-completion/completions/fbgs 
│     │                 │                        ├ [173]: /usr/share/bash-completion/completions/fbi 
│     │                 │                        ├ [174]: /usr/share/bash-completion/completions/feh 
│     │                 │                        ├ [175]: /usr/share/bash-completion/completions/file 
│     │                 │                        ├ [176]: /usr/share/bash-completion/completions/file-roller 
│     │                 │                        ├ [177]: /usr/share/bash-completion/completions/filefrag 
│     │                 │                        ├ [178]: /usr/share/bash-completion/completions/filesnarf 
│     │                 │                        ├ [179]: /usr/share/bash-completion/completions/find 
│     │                 │                        ├ [180]: /usr/share/bash-completion/completions/find_member 
│     │                 │                        ├ [181]: /usr/share/bash-completion/completions/fio 
│     │                 │                        ├ [182]: /usr/share/bash-completion/completions/firefox 
│     │                 │                        ├ [183]: /usr/share/bash-completion/completions/flake8 
│     │                 │                        ├ [184]: /usr/share/bash-completion/completions/fprintd-delete 
│     │                 │                        ├ [185]: /usr/share/bash-completion/completions/fprintd-enroll 
│     │                 │                        ├ [186]: /usr/share/bash-completion/completions/freeciv 
│     │                 │                        ├ [187]: /usr/share/bash-completion/completions/freeciv-server 
│     │                 │                        ├ [188]: /usr/share/bash-completion/completions/function 
│     │                 │                        ├ [189]: /usr/share/bash-completion/completions/fusermount 
│     │                 │                        ├ [190]: /usr/share/bash-completion/completions/gcc 
│     │                 │                        ├ [191]: /usr/share/bash-completion/completions/gcl 
│     │                 │                        ├ [192]: /usr/share/bash-completion/completions/gdb 
│     │                 │                        ├ [193]: /usr/share/bash-completion/completions/genaliases 
│     │                 │                        ├ [194]: /usr/share/bash-completion/completions/gendiff 
│     │                 │                        ├ [195]: /usr/share/bash-completion/completions/genisoimage 
│     │                 │                        ├ [196]: /usr/share/bash-completion/completions/geoiplookup 
│     │                 │                        ├ [197]: /usr/share/bash-completion/completions/getconf 
│     │                 │                        ├ [198]: /usr/share/bash-completion/completions/getent 
│     │                 │                        ├ [199]: /usr/share/bash-completion/completions/gkrellm 
│     │                 │                        ├ [200]: /usr/share/bash-completion/completions/gm 
│     │                 │                        ├ [201]: /usr/share/bash-completion/completions/gnatmake 
│     │                 │                        ├ [202]: /usr/share/bash-completion/completions/gnokii 
│     │                 │                        ├ [203]: /usr/share/bash-completion/completions/gnome-mplayer 
│     │                 │                        ├ [204]: /usr/share/bash-completion/completions/gnome-screenshot 
│     │                 │                        ├ [205]: /usr/share/bash-completion/completions/gpasswd 
│     │                 │                        ├ [206]: /usr/share/bash-completion/completions/gpg 
│     │                 │                        ├ [207]: /usr/share/bash-completion/completions/gpg2 
│     │                 │                        ├ [208]: /usr/share/bash-completion/completions/gpgv 
│     │                 │                        ├ [209]: /usr/share/bash-completion/completions/gphoto2 
│     │                 │                        ├ [210]: /usr/share/bash-completion/completions/gprof 
│     │                 │                        ├ [211]: /usr/share/bash-completion/completions/groupadd 
│     │                 │                        ├ [212]: /usr/share/bash-completion/completions/groupdel 
│     │                 │                        ├ [213]: /usr/share/bash-completion/completions/groupmems 
│     │                 │                        ├ [214]: /usr/share/bash-completion/completions/groupmod 
│     │                 │                        ├ [215]: /usr/share/bash-completion/completions/growisofs 
│     │                 │                        ├ [216]: /usr/share/bash-completion/completions/grpck 
│     │                 │                        ├ [217]: /usr/share/bash-completion/completions/gssdp-discover 
│     │                 │                        ├ [218]: /usr/share/bash-completion/completions/gzip 
│     │                 │                        ├ [219]: /usr/share/bash-completion/completions/hash 
│     │                 │                        ├ [220]: /usr/share/bash-completion/completions/hcitool 
│     │                 │                        ├ [221]: /usr/share/bash-completion/completions/hddtemp 
│     │                 │                        ├ [222]: /usr/share/bash-completion/completions/help 
│     │                 │                        ├ [223]: /usr/share/bash-completion/completions/hid2hci 
│     │                 │                        ├ [224]: /usr/share/bash-completion/completions/hostname 
│     │                 │                        ├ [225]: /usr/share/bash-completion/completions/hping2 
│     │                 │                        ├ [226]: /usr/share/bash-completion/completions/htop 
│     │                 │                        ├ [227]: /usr/share/bash-completion/completions/htpasswd 
│     │                 │                        ├ [228]: /usr/share/bash-completion/completions/hunspell 
│     │                 │                        ├ [229]: /usr/share/bash-completion/completions/iconv 
│     │                 │                        ├ [230]: /usr/share/bash-completion/completions/id 
│     │                 │                        ├ [231]: /usr/share/bash-completion/completions/idn 
│     │                 │                        ├ [232]: /usr/share/bash-completion/completions/ifstat 
│     │                 │                        ├ [233]: /usr/share/bash-completion/completions/iftop 
│     │                 │                        ├ [234]: /usr/share/bash-completion/completions/ifup 
│     │                 │                        ├ [235]: /usr/share/bash-completion/completions/influx 
│     │                 │                        ├ [236]: /usr/share/bash-completion/completions/info 
│     │                 │                        ├ [237]: /usr/share/bash-completion/completions/inject 
│     │                 │                        ├ [238]: /usr/share/bash-completion/completions/inotifywait 
│     │                 │                        ├ [239]: /usr/share/bash-completion/completions/installpkg 
│     │                 │                        ├ [240]: /usr/share/bash-completion/completions/interdiff 
│     │                 │                        ├ [241]: /usr/share/bash-completion/completions/invoke-rc.d 
│     │                 │                        ├ [242]: /usr/share/bash-completion/completions/ip 
│     │                 │                        ├ [243]: /usr/share/bash-completion/completions/ipcalc 
│     │                 │                        ├ [244]: /usr/share/bash-completion/completions/iperf 
│     │                 │                        ├ [245]: /usr/share/bash-completion/completions/ipmitool 
│     │                 │                        ├ [246]: /usr/share/bash-completion/completions/ipsec 
│     │                 │                        ├ [247]: /usr/share/bash-completion/completions/iptables 
│     │                 │                        ├ [248]: /usr/share/bash-completion/completions/ipv6calc 
│     │                 │                        ├ [249]: /usr/share/bash-completion/completions/iscsiadm 
│     │                 │                        ├ [250]: /usr/share/bash-completion/completions/isort 
│     │                 │                        ├ [251]: /usr/share/bash-completion/completions/isql 
│     │                 │                        ├ [252]: /usr/share/bash-completion/completions/iwconfig 
│     │                 │                        ├ [253]: /usr/share/bash-completion/completions/iwlist 
│     │                 │                        ├ [254]: /usr/share/bash-completion/completions/iwpriv 
│     │                 │                        ├ [255]: /usr/share/bash-completion/completions/iwspy 
│     │                 │                        ├ [256]: /usr/share/bash-completion/completions/jar 
│     │                 │                        ├ [257]: /usr/share/bash-completion/completions/jarsigner 
│     │                 │                        ├ [258]: /usr/share/bash-completion/completions/java 
│     │                 │                        ├ [259]: /usr/share/bash-completion/completions/javaws 
│     │                 │                        ├ [260]: /usr/share/bash-completion/completions/jpegoptim 
│     │                 │                        ├ [261]: /usr/share/bash-completion/completions/jps 
│     │                 │                        ├ [262]: /usr/share/bash-completion/completions/jq 
│     │                 │                        ├ [263]: /usr/share/bash-completion/completions/jshint 
│     │                 │                        ├ [264]: /usr/share/bash-completion/completions/json_xs 
│     │                 │                        ├ [265]: /usr/share/bash-completion/completions/jsonschema 
│     │                 │                        ├ [266]: /usr/share/bash-completion/completions/k3b 
│     │                 │                        ├ [267]: /usr/share/bash-completion/completions/kcov 
│     │                 │                        ├ [268]: /usr/share/bash-completion/completions/kill 
│     │                 │                        ├ [269]: /usr/share/bash-completion/completions/killall 
│     │                 │                        ├ [270]: /usr/share/bash-completion/completions/koji 
│     │                 │                        ├ [271]: /usr/share/bash-completion/completions/ktutil 
│     │                 │                        ├ [272]: /usr/share/bash-completion/completions/larch 
│     │                 │                        ├ [273]: /usr/share/bash-completion/completions/lastlog 
│     │                 │                        ├ [274]: /usr/share/bash-completion/completions/ldapsearch 
│     │                 │                        ├ [275]: /usr/share/bash-completion/completions/ldapvi 
│     │                 │                        ├ [276]: /usr/share/bash-completion/completions/lftp 
│     │                 │                        ├ [277]: /usr/share/bash-completion/completions/lftpget 
│     │                 │                        ├ [278]: /usr/share/bash-completion/completions/lilo 
│     │                 │                        ├ [279]: /usr/share/bash-completion/completions/links 
│     │                 │                        ├ [280]: /usr/share/bash-completion/completions/lintian 
│     │                 │                        ├ [281]: /usr/share/bash-completion/completions/lisp 
│     │                 │                        ├ [282]: /usr/share/bash-completion/completions/list_admins 
│     │                 │                        ├ [283]: /usr/share/bash-completion/completions/list_lists 
│     │                 │                        ├ [284]: /usr/share/bash-completion/completions/list_members 
│     │                 │                        ├ [285]: /usr/share/bash-completion/completions/list_owners 
│     │                 │                        ├ [286]: /usr/share/bash-completion/completions/locale-gen 
│     │                 │                        ├ [287]: /usr/share/bash-completion/completions/lpq 
│     │                 │                        ├ [288]: /usr/share/bash-completion/completions/lpr 
│     │                 │                        ├ [289]: /usr/share/bash-completion/completions/lrzip 
│     │                 │                        ├ [290]: /usr/share/bash-completion/completions/lsof 
│     │                 │                        ├ [291]: /usr/share/bash-completion/completions/lsscsi 
│     │                 │                        ├ [292]: /usr/share/bash-completion/completions/lsusb 
│     │                 │                        ├ [293]: /usr/share/bash-completion/completions/lua 
│     │                 │                        ├ [294]: /usr/share/bash-completion/completions/luac 
│     │                 │                        ├ [295]: /usr/share/bash-completion/completions/luseradd 
│     │                 │                        ├ [296]: /usr/share/bash-completion/completions/luserdel 
│     │                 │                        ├ [297]: /usr/share/bash-completion/completions/lvm 
│     │                 │                        ├ [298]: /usr/share/bash-completion/completions/lz4 
│     │                 │                        ├ [299]: /usr/share/bash-completion/completions/lzip 
│     │                 │                        ├ [300]: /usr/share/bash-completion/completions/lzma 
│     │                 │                        ├ [301]: /usr/share/bash-completion/completions/lzop 
│     │                 │                        ├ [302]: /usr/share/bash-completion/completions/macof 
│     │                 │                        ├ [303]: /usr/share/bash-completion/completions/mailmanctl 
│     │                 │                        ├ [304]: /usr/share/bash-completion/completions/make 
│     │                 │                        ├ [305]: /usr/share/bash-completion/completions/makepkg 
│     │                 │                        ├ [306]: /usr/share/bash-completion/completions/man 
│     │                 │                        ├ [307]: /usr/share/bash-completion/completions/mc 
│     │                 │                        ├ [308]: /usr/share/bash-completion/completions/mcrypt 
│     │                 │                        ├ [309]: /usr/share/bash-completion/completions/mdadm 
│     │                 │                        ├ [310]: /usr/share/bash-completion/completions/mdtool 
│     │                 │                        ├ [311]: /usr/share/bash-completion/completions/medusa 
│     │                 │                        ├ [312]: /usr/share/bash-completion/completions/mfiutil 
│     │                 │                        ├ [313]: /usr/share/bash-completion/completions/mii-diag 
│     │                 │                        ├ [314]: /usr/share/bash-completion/completions/mii-tool 
│     │                 │                        ├ [315]: /usr/share/bash-completion/completions/minicom 
│     │                 │                        ├ [316]: /usr/share/bash-completion/completions/mkinitrd 
│     │                 │                        ├ [317]: /usr/share/bash-completion/completions/mktemp 
│     │                 │                        ├ [318]: /usr/share/bash-completion/completions/mmsitepass 
│     │                 │                        ├ [319]: /usr/share/bash-completion/completions/monodevelop 
│     │                 │                        ├ [320]: /usr/share/bash-completion/completions/mplayer 
│     │                 │                        ├ [321]: /usr/share/bash-completion/completions/mr 
│     │                 │                        ├ [322]: /usr/share/bash-completion/completions/msynctool 
│     │                 │                        ├ [323]: /usr/share/bash-completion/completions/mtx 
│     │                 │                        ├ [324]: /usr/share/bash-completion/completions/munin-node-con
│     │                 │                        │        figure 
│     │                 │                        ├ [325]: /usr/share/bash-completion/completions/munin-run 
│     │                 │                        ├ [326]: /usr/share/bash-completion/completions/munin-update 
│     │                 │                        ├ [327]: /usr/share/bash-completion/completions/munindoc 
│     │                 │                        ├ [328]: /usr/share/bash-completion/completions/mussh 
│     │                 │                        ├ [329]: /usr/share/bash-completion/completions/mutt 
│     │                 │                        ├ [330]: /usr/share/bash-completion/completions/mypy 
│     │                 │                        ├ [331]: /usr/share/bash-completion/completions/mysql 
│     │                 │                        ├ [332]: /usr/share/bash-completion/completions/mysqladmin 
│     │                 │                        ├ [333]: /usr/share/bash-completion/completions/nc 
│     │                 │                        ├ [334]: /usr/share/bash-completion/completions/ncftp 
│     │                 │                        ├ [335]: /usr/share/bash-completion/completions/nethogs 
│     │                 │                        ├ [336]: /usr/share/bash-completion/completions/newlist 
│     │                 │                        ├ [337]: /usr/share/bash-completion/completions/newusers 
│     │                 │                        ├ [338]: /usr/share/bash-completion/completions/ngrep 
│     │                 │                        ├ [339]: /usr/share/bash-completion/completions/nmap 
│     │                 │                        ├ [340]: /usr/share/bash-completion/completions/nproc 
│     │                 │                        ├ [341]: /usr/share/bash-completion/completions/nslookup 
│     │                 │                        ├ [342]: /usr/share/bash-completion/completions/nsupdate 
│     │                 │                        ├ [343]: /usr/share/bash-completion/completions/ntpdate 
│     │                 │                        ├ [344]: /usr/share/bash-completion/completions/oggdec 
│     │                 │                        ├ [345]: /usr/share/bash-completion/completions/openssl 
│     │                 │                        ├ [346]: /usr/share/bash-completion/completions/opera 
│     │                 │                        ├ [347]: /usr/share/bash-completion/completions/optipng 
│     │                 │                        ├ [348]: /usr/share/bash-completion/completions/p4 
│     │                 │                        ├ [349]: /usr/share/bash-completion/completions/pack200 
│     │                 │                        ├ [350]: /usr/share/bash-completion/completions/passwd 
│     │                 │                        ├ [351]: /usr/share/bash-completion/completions/patch 
│     │                 │                        ├ [352]: /usr/share/bash-completion/completions/pdftoppm 
│     │                 │                        ├ [353]: /usr/share/bash-completion/completions/pdftotext 
│     │                 │                        ├ [354]: /usr/share/bash-completion/completions/perl 
│     │                 │                        ├ [355]: /usr/share/bash-completion/completions/perlcritic 
│     │                 │                        ├ [356]: /usr/share/bash-completion/completions/perltidy 
│     │                 │                        ├ [357]: /usr/share/bash-completion/completions/pgrep 
│     │                 │                        ├ [358]: /usr/share/bash-completion/completions/pidof 
│     │                 │                        ├ [359]: /usr/share/bash-completion/completions/pine 
│     │                 │                        ├ [360]: /usr/share/bash-completion/completions/ping 
│     │                 │                        ├ [361]: /usr/share/bash-completion/completions/pkg-config 
│     │                 │                        ├ [362]: /usr/share/bash-completion/completions/pkg-get 
│     │                 │                        ├ [363]: /usr/share/bash-completion/completions/pkgadd 
│     │                 │                        ├ [364]: /usr/share/bash-completion/completions/pkgrm 
│     │                 │                        ├ [365]: /usr/share/bash-completion/completions/pkgtool 
│     │                 │                        ├ [366]: /usr/share/bash-completion/completions/plague-client 
│     │                 │                        ├ [367]: /usr/share/bash-completion/completions/pm-hibernate 
│     │                 │                        ├ [368]: /usr/share/bash-completion/completions/pm-is-supported 
│     │                 │                        ├ [369]: /usr/share/bash-completion/completions/pm-powersave 
│     │                 │                        ├ [370]: /usr/share/bash-completion/completions/pngfix 
│     │                 │                        ├ [371]: /usr/share/bash-completion/completions/postcat 
│     │                 │                        ├ [372]: /usr/share/bash-completion/completions/postconf 
│     │                 │                        ├ [373]: /usr/share/bash-completion/completions/postfix 
│     │                 │                        ├ [374]: /usr/share/bash-completion/completions/postmap 
│     │                 │                        ├ [375]: /usr/share/bash-completion/completions/postsuper 
│     │                 │                        ├ [376]: /usr/share/bash-completion/completions/povray 
│     │                 │                        ├ [377]: /usr/share/bash-completion/completions/prelink 
│     │                 │                        ├ [378]: /usr/share/bash-completion/completions/printenv 
│     │                 │                        ├ [379]: /usr/share/bash-completion/completions/protoc 
│     │                 │                        ├ [380]: /usr/share/bash-completion/completions/ps 
│     │                 │                        ├ [381]: /usr/share/bash-completion/completions/psql 
│     │                 │                        ├ [382]: /usr/share/bash-completion/completions/puppet 
│     │                 │                        ├ [383]: /usr/share/bash-completion/completions/pv 
│     │                 │                        ├ [384]: /usr/share/bash-completion/completions/pwck 
│     │                 │                        ├ [385]: /usr/share/bash-completion/completions/pwd 
│     │                 │                        ├ [386]: /usr/share/bash-completion/completions/pwdx 
│     │                 │                        ├ [387]: /usr/share/bash-completion/completions/pwgen 
│     │                 │                        ├ [388]: /usr/share/bash-completion/completions/pycodestyle 
│     │                 │                        ├ [389]: /usr/share/bash-completion/completions/pydoc 
│     │                 │                        ├ [390]: /usr/share/bash-completion/completions/pydocstyle 
│     │                 │                        ├ [391]: /usr/share/bash-completion/completions/pyflakes 
│     │                 │                        ├ [392]: /usr/share/bash-completion/completions/pylint 
│     │                 │                        ├ [393]: /usr/share/bash-completion/completions/pytest 
│     │                 │                        ├ [394]: /usr/share/bash-completion/completions/python 
│     │                 │                        ├ [395]: /usr/share/bash-completion/completions/pyvenv 
│     │                 │                        ├ [396]: /usr/share/bash-completion/completions/qdbus 
│     │                 │                        ├ [397]: /usr/share/bash-completion/completions/qemu 
│     │                 │                        ├ [398]: /usr/share/bash-completion/completions/qrunner 
│     │                 │                        ├ [399]: /usr/share/bash-completion/completions/querybts 
│     │                 │                        ├ [400]: /usr/share/bash-completion/completions/quota 
│     │                 │                        ├ [401]: /usr/share/bash-completion/completions/radvdump 
│     │                 │                        ├ [402]: /usr/share/bash-completion/completions/rcs 
│     │                 │                        ├ [403]: /usr/share/bash-completion/completions/rdesktop 
│     │                 │                        ├ [404]: /usr/share/bash-completion/completions/remove_members 
│     │                 │                        ├ [405]: /usr/share/bash-completion/completions/removepkg 
│     │                 │                        ├ [406]: /usr/share/bash-completion/completions/reportbug 
│     │                 │                        ├ [407]: /usr/share/bash-completion/completions/resolvconf 
│     │                 │                        ├ [408]: /usr/share/bash-completion/completions/ri 
│     │                 │                        ├ [409]: /usr/share/bash-completion/completions/rmlist 
│     │                 │                        ├ [410]: /usr/share/bash-completion/completions/route 
│     │                 │                        ├ [411]: /usr/share/bash-completion/completions/rpcdebug 
│     │                 │                        ├ [412]: /usr/share/bash-completion/completions/rpm 
│     │                 │                        ├ [413]: /usr/share/bash-completion/completions/rpm2tgz 
│     │                 │                        ├ [414]: /usr/share/bash-completion/completions/rpmcheck 
│     │                 │                        ├ [415]: /usr/share/bash-completion/completions/rrdtool 
│     │                 │                        ├ [416]: /usr/share/bash-completion/completions/rsync 
│     │                 │                        ├ [417]: /usr/share/bash-completion/completions/sbcl 
│     │                 │                        ├ [418]: /usr/share/bash-completion/completions/sbopkg 
│     │                 │                        ├ [419]: /usr/share/bash-completion/completions/screen 
│     │                 │                        ├ [420]: /usr/share/bash-completion/completions/scrub 
│     │                 │                        ├ [421]: /usr/share/bash-completion/completions/set 
│     │                 │                        ├ [422]: /usr/share/bash-completion/completions/sh 
│     │                 │                        ├ [423]: /usr/share/bash-completion/completions/sha256sum 
│     │                 │                        ├ [424]: /usr/share/bash-completion/completions/shellcheck 
│     │                 │                        ├ [425]: /usr/share/bash-completion/completions/sitecopy 
│     │                 │                        ├ [426]: /usr/share/bash-completion/completions/slabtop 
│     │                 │                        ├ [427]: /usr/share/bash-completion/completions/slapt-get 
│     │                 │                        ├ [428]: /usr/share/bash-completion/completions/slapt-src 
│     │                 │                        ├ [429]: /usr/share/bash-completion/completions/smartctl 
│     │                 │                        ├ [430]: /usr/share/bash-completion/completions/smbclient 
│     │                 │                        ├ [431]: /usr/share/bash-completion/completions/snownews 
│     │                 │                        ├ [432]: /usr/share/bash-completion/completions/sqlite3 
│     │                 │                        ├ [433]: /usr/share/bash-completion/completions/ss 
│     │                 │                        ├ [434]: /usr/share/bash-completion/completions/ssh 
│     │                 │                        ├ [435]: /usr/share/bash-completion/completions/ssh-add 
│     │                 │                        ├ [436]: /usr/share/bash-completion/completions/ssh-copy-id 
│     │                 │                        ├ [437]: /usr/share/bash-completion/completions/ssh-keygen 
│     │                 │                        ├ [438]: /usr/share/bash-completion/completions/ssh-keyscan 
│     │                 │                        ├ [439]: /usr/share/bash-completion/completions/sshfs 
│     │                 │                        ├ [440]: /usr/share/bash-completion/completions/sshmitm 
│     │                 │                        ├ [441]: /usr/share/bash-completion/completions/sshow 
│     │                 │                        ├ [442]: /usr/share/bash-completion/completions/strace 
│     │                 │                        ├ [443]: /usr/share/bash-completion/completions/strings 
│     │                 │                        ├ [444]: /usr/share/bash-completion/completions/sudo 
│     │                 │                        ├ [445]: /usr/share/bash-completion/completions/svcadm 
│     │                 │                        ├ [446]: /usr/share/bash-completion/completions/svk 
│     │                 │                        ├ [447]: /usr/share/bash-completion/completions/sync_members 
│     │                 │                        ├ [448]: /usr/share/bash-completion/completions/synclient 
│     │                 │                        ├ [449]: /usr/share/bash-completion/completions/sysbench 
│     │                 │                        ├ [450]: /usr/share/bash-completion/completions/sysctl 
│     │                 │                        ├ [451]: /usr/share/bash-completion/completions/tar 
│     │                 │                        ├ [452]: /usr/share/bash-completion/completions/tcpdump 
│     │                 │                        ├ [453]: /usr/share/bash-completion/completions/tcpkill 
│     │                 │                        ├ [454]: /usr/share/bash-completion/completions/tcpnice 
│     │                 │                        ├ [455]: /usr/share/bash-completion/completions/timeout 
│     │                 │                        ├ [456]: /usr/share/bash-completion/completions/tipc 
│     │                 │                        ├ [457]: /usr/share/bash-completion/completions/tox 
│     │                 │                        ├ [458]: /usr/share/bash-completion/completions/tracepath 
│     │                 │                        ├ [459]: /usr/share/bash-completion/completions/tree 
│     │                 │                        ├ [460]: /usr/share/bash-completion/completions/truncate 
│     │                 │                        ├ [461]: /usr/share/bash-completion/completions/tshark 
│     │                 │                        ├ [462]: /usr/share/bash-completion/completions/tsig-keygen 
│     │                 │                        ├ [463]: /usr/share/bash-completion/completions/tune2fs 
│     │                 │                        ├ [464]: /usr/share/bash-completion/completions/ulimit 
│     │                 │                        ├ [465]: /usr/share/bash-completion/completions/unace 
│     │                 │                        ├ [466]: /usr/share/bash-completion/completions/unpack200 
│     │                 │                        ├ [467]: /usr/share/bash-completion/completions/unrar 
│     │                 │                        ├ [468]: /usr/share/bash-completion/completions/unshunt 
│     │                 │                        ├ [469]: /usr/share/bash-completion/completions/update-alterna
│     │                 │                        │        tives 
│     │                 │                        ├ [470]: /usr/share/bash-completion/completions/update-rc.d 
│     │                 │                        ├ [471]: /usr/share/bash-completion/completions/upgradepkg 
│     │                 │                        ├ [472]: /usr/share/bash-completion/completions/urlsnarf 
│     │                 │                        ├ [473]: /usr/share/bash-completion/completions/useradd 
│     │                 │                        ├ [474]: /usr/share/bash-completion/completions/userdel 
│     │                 │                        ├ [475]: /usr/share/bash-completion/completions/usermod 
│     │                 │                        ├ [476]: /usr/share/bash-completion/completions/valgrind 
│     │                 │                        ├ [477]: /usr/share/bash-completion/completions/vipw 
│     │                 │                        ├ [478]: /usr/share/bash-completion/completions/vmstat 
│     │                 │                        ├ [479]: /usr/share/bash-completion/completions/vncviewer 
│     │                 │                        ├ [480]: /usr/share/bash-completion/completions/vpnc 
│     │                 │                        ├ [481]: /usr/share/bash-completion/completions/watch 
│     │                 │                        ├ [482]: /usr/share/bash-completion/completions/webmitm 
│     │                 │                        ├ [483]: /usr/share/bash-completion/completions/wget 
│     │                 │                        ├ [484]: /usr/share/bash-completion/completions/wine 
│     │                 │                        ├ [485]: /usr/share/bash-completion/completions/withlist 
│     │                 │                        ├ [486]: /usr/share/bash-completion/completions/wodim 
│     │                 │                        ├ [487]: /usr/share/bash-completion/completions/wol 
│     │                 │                        ├ [488]: /usr/share/bash-completion/completions/wsimport 
│     │                 │                        ├ [489]: /usr/share/bash-completion/completions/wtf 
│     │                 │                        ├ [490]: /usr/share/bash-completion/completions/wvdial 
│     │                 │                        ├ [491]: /usr/share/bash-completion/completions/xdg-mime 
│     │                 │                        ├ [492]: /usr/share/bash-completion/completions/xdg-settings 
│     │                 │                        ├ [493]: /usr/share/bash-completion/completions/xev 
│     │                 │                        ├ [494]: /usr/share/bash-completion/completions/xfreerdp 
│     │                 │                        ├ [495]: /usr/share/bash-completion/completions/xgamma 
│     │                 │                        ├ [496]: /usr/share/bash-completion/completions/xhost 
│     │                 │                        ├ [497]: /usr/share/bash-completion/completions/xmllint 
│     │                 │                        ├ [498]: /usr/share/bash-completion/completions/xmlwf 
│     │                 │                        ├ [499]: /usr/share/bash-completion/completions/xmms 
│     │                 │                        ├ [500]: /usr/share/bash-completion/completions/xmodmap 
│     │                 │                        ├ [501]: /usr/share/bash-completion/completions/xrandr 
│     │                 │                        ├ [502]: /usr/share/bash-completion/completions/xrdb 
│     │                 │                        ├ [503]: /usr/share/bash-completion/completions/xsltproc 
│     │                 │                        ├ [504]: /usr/share/bash-completion/completions/xvfb-run 
│     │                 │                        ├ [505]: /usr/share/bash-completion/completions/xxd 
│     │                 │                        ├ [506]: /usr/share/bash-completion/completions/xz 
│     │                 │                        ├ [507]: /usr/share/bash-completion/completions/xzdec 
│     │                 │                        ├ [508]: /usr/share/bash-completion/completions/ypmatch 
│     │                 │                        ├ [509]: /usr/share/bash-completion/completions/yum-arch 
│     │                 │                        ├ [510]: /usr/share/bash-completion/completions/zopfli 
│     │                 │                        ├ [511]: /usr/share/bash-completion/completions/zopflipng 
│     │                 │                        ├ [512]: /usr/share/bash-completion/helpers/make-extract-targe
│     │                 │                        │        ts.awk 
│     │                 │                        ├ [513]: /usr/share/bash-completion/helpers/perl 
│     │                 │                        ├ [514]: /usr/share/bash-completion/helpers/python 
│     │                 │                        ├ [515]: /usr/share/cmake/bash-completion/bash-completion-conf
│     │                 │                        │        ig-version.cmake 
│     │                 │                        ├ [516]: /usr/share/cmake/bash-completion/bash-completion-conf
│     │                 │                        │        ig.cmake 
│     │                 │                        ├ [517]: /usr/share/doc/bash-completion/AUTHORS 
│     │                 │                        ├ [518]: /usr/share/doc/bash-completion/CONTRIBUTING.md.gz 
│     │                 │                        ├ [519]: /usr/share/doc/bash-completion/README.Debian 
│     │                 │                        ├ [520]: /usr/share/doc/bash-completion/README.md.gz 
│     │                 │                        ├ [521]: /usr/share/doc/bash-completion/changelog.Debian.gz 
│     │                 │                        ├ [522]: /usr/share/doc/bash-completion/copyright 
│     │                 │                        ├ [523]: /usr/share/lintian/overrides/bash-completion 
│     │                 │                        ├ [524]: /usr/share/man/man1/dh_bash-completion.1.gz 
│     │                 │                        ├ [525]: /usr/share/perl5/Debian/Debhelper/Sequence/bash_compl
│     │                 │                        │        etion.pm 
│     │                 │                        ╰ [526]: /usr/share/pkgconfig/bash-completion.pc 
│     │                 ├ [5]   ╭ ID            : bsdutils@1:2.40.2-14ubuntu1.1 
│     │                 │       ├ Name          : bsdutils 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/bsdutils@2.40.2-14ubuntu1.1?arch=amd64&
│     │                 │       │                │       distro=ubuntu-25.04&epoch=1 
│     │                 │       │                ╰ UID : 267c69bb9bba97a 
│     │                 │       ├ Version       : 2.40.2 
│     │                 │       ├ Release       : 14ubuntu1.1 
│     │                 │       ├ Epoch         : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : util-linux 
│     │                 │       ├ SrcVersion    : 2.40.2 
│     │                 │       ├ SrcRelease    : 14ubuntu1.1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-or-later 
│     │                 │       │                ├ [1] : GPL-2.0-only 
│     │                 │       │                ├ [2] : GPL-3.0-or-later 
│     │                 │       │                ├ [3] : LGPL-2.1-or-later 
│     │                 │       │                ├ [4] : public-domain 
│     │                 │       │                ├ [5] : BSD-4-Clause 
│     │                 │       │                ├ [6] : MIT 
│     │                 │       │                ├ [7] : ISC 
│     │                 │       │                ├ [8] : BSD-3-Clause 
│     │                 │       │                ├ [9] : BSLA 
│     │                 │       │                ├ [10]: LGPL-2.0-or-later 
│     │                 │       │                ├ [11]: BSD-2-Clause 
│     │                 │       │                ├ [12]: LGPL-3.0-or-later 
│     │                 │       │                ├ [13]: GPL-3.0-only 
│     │                 │       │                ├ [14]: LGPL-2.0-only 
│     │                 │       │                ├ [15]: LGPL-2.1-only 
│     │                 │       │                ╰ [16]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/logger 
│     │                 │                        ├ [1] : /usr/bin/renice 
│     │                 │                        ├ [2] : /usr/bin/script 
│     │                 │                        ├ [3] : /usr/bin/scriptlive 
│     │                 │                        ├ [4] : /usr/bin/scriptreplay 
│     │                 │                        ├ [5] : /usr/bin/wall 
│     │                 │                        ├ [6] : /usr/share/bash-completion/completions/logger 
│     │                 │                        ├ [7] : /usr/share/bash-completion/completions/renice 
│     │                 │                        ├ [8] : /usr/share/bash-completion/completions/script 
│     │                 │                        ├ [9] : /usr/share/bash-completion/completions/scriptlive 
│     │                 │                        ├ [10]: /usr/share/bash-completion/completions/scriptreplay 
│     │                 │                        ├ [11]: /usr/share/bash-completion/completions/wall 
│     │                 │                        ├ [12]: /usr/share/doc/bsdutils/NEWS.Debian.gz 
│     │                 │                        ├ [13]: /usr/share/doc/bsdutils/changelog.Debian.gz 
│     │                 │                        ├ [14]: /usr/share/doc/bsdutils/copyright 
│     │                 │                        ├ [15]: /usr/share/lintian/overrides/bsdutils 
│     │                 │                        ├ [16]: /usr/share/man/man1/logger.1.gz 
│     │                 │                        ├ [17]: /usr/share/man/man1/renice.1.gz 
│     │                 │                        ├ [18]: /usr/share/man/man1/script.1.gz 
│     │                 │                        ├ [19]: /usr/share/man/man1/scriptlive.1.gz 
│     │                 │                        ├ [20]: /usr/share/man/man1/scriptreplay.1.gz 
│     │                 │                        ╰ [21]: /usr/share/man/man1/wall.1.gz 
│     │                 ├ [6]   ╭ ID            : ca-certificates@20241223 
│     │                 │       ├ Name          : ca-certificates 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/ca-certificates@20241223?arch=all&distr
│     │                 │       │                │       o=ubuntu-25.04 
│     │                 │       │                ╰ UID : 53f03c3bf01a95ec 
│     │                 │       ├ Version       : 20241223 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : ca-certificates 
│     │                 │       ├ SrcVersion    : 20241223 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: GPL-2.0-only 
│     │                 │       │                ╰ [2]: MPL-2.0 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: debconf@1.5.87ubuntu1 
│     │                 │       │                ╰ [1]: openssl@3.4.1-1ubuntu4 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/sbin/update-ca-certificates 
│     │                 │                        ├ [1]  : /usr/share/ca-certificates/mozilla/ACCVRAIZ1.crt 
│     │                 │                        ├ [2]  : /usr/share/ca-certificates/mozilla/AC_RAIZ_FNMT-RCM.crt 
│     │                 │                        ├ [3]  : /usr/share/ca-certificates/mozilla/AC_RAIZ_FNMT-RCM_S
│     │                 │                        │        ERVIDORES_SEGUROS.crt 
│     │                 │                        ├ [4]  : /usr/share/ca-certificates/mozilla/ANF_Secure_Server_
│     │                 │                        │        Root_CA.crt 
│     │                 │                        ├ [5]  : /usr/share/ca-certificates/mozilla/Actalis_Authentica
│     │                 │                        │        tion_Root_CA.crt 
│     │                 │                        ├ [6]  : /usr/share/ca-certificates/mozilla/AffirmTrust_Commer
│     │                 │                        │        cial.crt 
│     │                 │                        ├ [7]  : /usr/share/ca-certificates/mozilla/AffirmTrust_Networ
│     │                 │                        │        king.crt 
│     │                 │                        ├ [8]  : /usr/share/ca-certificates/mozilla/AffirmTrust_Premiu
│     │                 │                        │        m.crt 
│     │                 │                        ├ [9]  : /usr/share/ca-certificates/mozilla/AffirmTrust_Premiu
│     │                 │                        │        m_ECC.crt 
│     │                 │                        ├ [10] : /usr/share/ca-certificates/mozilla/Amazon_Root_CA_1.crt 
│     │                 │                        ├ [11] : /usr/share/ca-certificates/mozilla/Amazon_Root_CA_2.crt 
│     │                 │                        ├ [12] : /usr/share/ca-certificates/mozilla/Amazon_Root_CA_3.crt 
│     │                 │                        ├ [13] : /usr/share/ca-certificates/mozilla/Amazon_Root_CA_4.crt 
│     │                 │                        ├ [14] : /usr/share/ca-certificates/mozilla/Atos_TrustedRoot_2
│     │                 │                        │        011.crt 
│     │                 │                        ├ [15] : /usr/share/ca-certificates/mozilla/Atos_TrustedRoot_R
│     │                 │                        │        oot_CA_ECC_TLS_2021.crt 
│     │                 │                        ├ [16] : /usr/share/ca-certificates/mozilla/Atos_TrustedRoot_R
│     │                 │                        │        oot_CA_RSA_TLS_2021.crt 
│     │                 │                        ├ [17] : /usr/share/ca-certificates/mozilla/Autoridad_de_Certi
│     │                 │                        │        ficacion_Firmaprofesional_CIF_A62634068.crt 
│     │                 │                        ├ [18] : /usr/share/ca-certificates/mozilla/BJCA_Global_Root_C
│     │                 │                        │        A1.crt 
│     │                 │                        ├ [19] : /usr/share/ca-certificates/mozilla/BJCA_Global_Root_C
│     │                 │                        │        A2.crt 
│     │                 │                        ├ [20] : /usr/share/ca-certificates/mozilla/Baltimore_CyberTru
│     │                 │                        │        st_Root.crt 
│     │                 │                        ├ [21] : /usr/share/ca-certificates/mozilla/Buypass_Class_2_Ro
│     │                 │                        │        ot_CA.crt 
│     │                 │                        ├ [22] : /usr/share/ca-certificates/mozilla/Buypass_Class_3_Ro
│     │                 │                        │        ot_CA.crt 
│     │                 │                        ├ [23] : /usr/share/ca-certificates/mozilla/CA_Disig_Root_R2.crt 
│     │                 │                        ├ [24] : /usr/share/ca-certificates/mozilla/CFCA_EV_ROOT.crt 
│     │                 │                        ├ [25] : /usr/share/ca-certificates/mozilla/COMODO_Certificati
│     │                 │                        │        on_Authority.crt 
│     │                 │                        ├ [26] : /usr/share/ca-certificates/mozilla/COMODO_ECC_Certifi
│     │                 │                        │        cation_Authority.crt 
│     │                 │                        ├ [27] : /usr/share/ca-certificates/mozilla/COMODO_RSA_Certifi
│     │                 │                        │        cation_Authority.crt 
│     │                 │                        ├ [28] : /usr/share/ca-certificates/mozilla/Certainly_Root_E1.
│     │                 │                        │        crt 
│     │                 │                        ├ [29] : /usr/share/ca-certificates/mozilla/Certainly_Root_R1.
│     │                 │                        │        crt 
│     │                 │                        ├ [30] : /usr/share/ca-certificates/mozilla/Certigna.crt 
│     │                 │                        ├ [31] : /usr/share/ca-certificates/mozilla/Certigna_Root_CA.crt 
│     │                 │                        ├ [32] : /usr/share/ca-certificates/mozilla/Certum_EC-384_CA.crt 
│     │                 │                        ├ [33] : /usr/share/ca-certificates/mozilla/Certum_Trusted_Net
│     │                 │                        │        work_CA.crt 
│     │                 │                        ├ [34] : /usr/share/ca-certificates/mozilla/Certum_Trusted_Net
│     │                 │                        │        work_CA_2.crt 
│     │                 │                        ├ [35] : /usr/share/ca-certificates/mozilla/Certum_Trusted_Roo
│     │                 │                        │        t_CA.crt 
│     │                 │                        ├ [36] : /usr/share/ca-certificates/mozilla/CommScope_Public_T
│     │                 │                        │        rust_ECC_Root-01.crt 
│     │                 │                        ├ [37] : /usr/share/ca-certificates/mozilla/CommScope_Public_T
│     │                 │                        │        rust_ECC_Root-02.crt 
│     │                 │                        ├ [38] : /usr/share/ca-certificates/mozilla/CommScope_Public_T
│     │                 │                        │        rust_RSA_Root-01.crt 
│     │                 │                        ├ [39] : /usr/share/ca-certificates/mozilla/CommScope_Public_T
│     │                 │                        │        rust_RSA_Root-02.crt 
│     │                 │                        ├ [40] : /usr/share/ca-certificates/mozilla/Comodo_AAA_Service
│     │                 │                        │        s_root.crt 
│     │                 │                        ├ [41] : /usr/share/ca-certificates/mozilla/D-TRUST_BR_Root_CA
│     │                 │                        │        _1_2020.crt 
│     │                 │                        ├ [42] : /usr/share/ca-certificates/mozilla/D-TRUST_EV_Root_CA
│     │                 │                        │        _1_2020.crt 
│     │                 │                        ├ [43] : /usr/share/ca-certificates/mozilla/D-TRUST_Root_Class
│     │                 │                        │        _3_CA_2_2009.crt 
│     │                 │                        ├ [44] : /usr/share/ca-certificates/mozilla/D-TRUST_Root_Class
│     │                 │                        │        _3_CA_2_EV_2009.crt 
│     │                 │                        ├ [45] : /usr/share/ca-certificates/mozilla/DigiCert_Assured_I
│     │                 │                        │        D_Root_CA.crt 
│     │                 │                        ├ [46] : /usr/share/ca-certificates/mozilla/DigiCert_Assured_I
│     │                 │                        │        D_Root_G2.crt 
│     │                 │                        ├ [47] : /usr/share/ca-certificates/mozilla/DigiCert_Assured_I
│     │                 │                        │        D_Root_G3.crt 
│     │                 │                        ├ [48] : /usr/share/ca-certificates/mozilla/DigiCert_Global_Ro
│     │                 │                        │        ot_CA.crt 
│     │                 │                        ├ [49] : /usr/share/ca-certificates/mozilla/DigiCert_Global_Ro
│     │                 │                        │        ot_G2.crt 
│     │                 │                        ├ [50] : /usr/share/ca-certificates/mozilla/DigiCert_Global_Ro
│     │                 │                        │        ot_G3.crt 
│     │                 │                        ├ [51] : /usr/share/ca-certificates/mozilla/DigiCert_High_Assu
│     │                 │                        │        rance_EV_Root_CA.crt 
│     │                 │                        ├ [52] : /usr/share/ca-certificates/mozilla/DigiCert_TLS_ECC_P
│     │                 │                        │        384_Root_G5.crt 
│     │                 │                        ├ [53] : /usr/share/ca-certificates/mozilla/DigiCert_TLS_RSA40
│     │                 │                        │        96_Root_G5.crt 
│     │                 │                        ├ [54] : /usr/share/ca-certificates/mozilla/DigiCert_Trusted_R
│     │                 │                        │        oot_G4.crt 
│     │                 │                        ├ [55] : /usr/share/ca-certificates/mozilla/Entrust.net_Premiu
│     │                 │                        │        m_2048_Secure_Server_CA.crt 
│     │                 │                        ├ [56] : /usr/share/ca-certificates/mozilla/Entrust_Root_Certi
│     │                 │                        │        fication_Authority.crt 
│     │                 │                        ├ [57] : /usr/share/ca-certificates/mozilla/Entrust_Root_Certi
│     │                 │                        │        fication_Authority_-_EC1.crt 
│     │                 │                        ├ [58] : /usr/share/ca-certificates/mozilla/Entrust_Root_Certi
│     │                 │                        │        fication_Authority_-_G2.crt 
│     │                 │                        ├ [59] : /usr/share/ca-certificates/mozilla/Entrust_Root_Certi
│     │                 │                        │        fication_Authority_-_G4.crt 
│     │                 │                        ├ [60] : /usr/share/ca-certificates/mozilla/FIRMAPROFESIONAL_C
│     │                 │                        │        A_ROOT-A_WEB.crt 
│     │                 │                        ├ [61] : /usr/share/ca-certificates/mozilla/GDCA_TrustAUTH_R5_
│     │                 │                        │        ROOT.crt 
│     │                 │                        ├ [62] : /usr/share/ca-certificates/mozilla/GLOBALTRUST_2020.crt 
│     │                 │                        ├ [63] : /usr/share/ca-certificates/mozilla/GTS_Root_R1.crt 
│     │                 │                        ├ [64] : /usr/share/ca-certificates/mozilla/GTS_Root_R2.crt 
│     │                 │                        ├ [65] : /usr/share/ca-certificates/mozilla/GTS_Root_R3.crt 
│     │                 │                        ├ [66] : /usr/share/ca-certificates/mozilla/GTS_Root_R4.crt 
│     │                 │                        ├ [67] : /usr/share/ca-certificates/mozilla/GlobalSign_ECC_Roo
│     │                 │                        │        t_CA_-_R4.crt 
│     │                 │                        ├ [68] : /usr/share/ca-certificates/mozilla/GlobalSign_ECC_Roo
│     │                 │                        │        t_CA_-_R5.crt 
│     │                 │                        ├ [69] : /usr/share/ca-certificates/mozilla/GlobalSign_Root_CA
│     │                 │                        │        .crt 
│     │                 │                        ├ [70] : /usr/share/ca-certificates/mozilla/GlobalSign_Root_CA
│     │                 │                        │        _-_R3.crt 
│     │                 │                        ├ [71] : /usr/share/ca-certificates/mozilla/GlobalSign_Root_CA
│     │                 │                        │        _-_R6.crt 
│     │                 │                        ├ [72] : /usr/share/ca-certificates/mozilla/GlobalSign_Root_E4
│     │                 │                        │        6.crt 
│     │                 │                        ├ [73] : /usr/share/ca-certificates/mozilla/GlobalSign_Root_R4
│     │                 │                        │        6.crt 
│     │                 │                        ├ [74] : /usr/share/ca-certificates/mozilla/Go_Daddy_Class_2_C
│     │                 │                        │        A.crt 
│     │                 │                        ├ [75] : /usr/share/ca-certificates/mozilla/Go_Daddy_Root_Cert
│     │                 │                        │        ificate_Authority_-_G2.crt 
│     │                 │                        ├ [76] : /usr/share/ca-certificates/mozilla/HARICA_TLS_ECC_Roo
│     │                 │                        │        t_CA_2021.crt 
│     │                 │                        ├ [77] : /usr/share/ca-certificates/mozilla/HARICA_TLS_RSA_Roo
│     │                 │                        │        t_CA_2021.crt 
│     │                 │                        ├ [78] : /usr/share/ca-certificates/mozilla/Hellenic_Academic_
│     │                 │                        │        and_Research_Institutions_ECC_RootCA_2015.crt 
│     │                 │                        ├ [79] : /usr/share/ca-certificates/mozilla/Hellenic_Academic_
│     │                 │                        │        and_Research_Institutions_RootCA_2015.crt 
│     │                 │                        ├ [80] : /usr/share/ca-certificates/mozilla/HiPKI_Root_CA_-_G1
│     │                 │                        │        .crt 
│     │                 │                        ├ [81] : /usr/share/ca-certificates/mozilla/Hongkong_Post_Root
│     │                 │                        │        _CA_3.crt 
│     │                 │                        ├ [82] : /usr/share/ca-certificates/mozilla/ISRG_Root_X1.crt 
│     │                 │                        ├ [83] : /usr/share/ca-certificates/mozilla/ISRG_Root_X2.crt 
│     │                 │                        ├ [84] : /usr/share/ca-certificates/mozilla/IdenTrust_Commerci
│     │                 │                        │        al_Root_CA_1.crt 
│     │                 │                        ├ [85] : /usr/share/ca-certificates/mozilla/IdenTrust_Public_S
│     │                 │                        │        ector_Root_CA_1.crt 
│     │                 │                        ├ [86] : /usr/share/ca-certificates/mozilla/Izenpe.com.crt 
│     │                 │                        ├ [87] : /usr/share/ca-certificates/mozilla/Microsec_e-Szigno_
│     │                 │                        │        Root_CA_2009.crt 
│     │                 │                        ├ [88] : /usr/share/ca-certificates/mozilla/Microsoft_ECC_Root
│     │                 │                        │        _Certificate_Authority_2017.crt 
│     │                 │                        ├ [89] : /usr/share/ca-certificates/mozilla/Microsoft_RSA_Root
│     │                 │                        │        _Certificate_Authority_2017.crt 
│     │                 │                        ├ [90] : /usr/share/ca-certificates/mozilla/NAVER_Global_Root_
│     │                 │                        │        Certification_Authority.crt 
│     │                 │                        ├ [91] : /usr/share/ca-certificates/mozilla/NetLock_Arany_=Cla
│     │                 │                        │        ss_Gold=_Főtanúsítvány.crt 
│     │                 │                        ├ [92] : /usr/share/ca-certificates/mozilla/OISTE_WISeKey_Glob
│     │                 │                        │        al_Root_GB_CA.crt 
│     │                 │                        ├ [93] : /usr/share/ca-certificates/mozilla/OISTE_WISeKey_Glob
│     │                 │                        │        al_Root_GC_CA.crt 
│     │                 │                        ├ [94] : /usr/share/ca-certificates/mozilla/QuoVadis_Root_CA_1
│     │                 │                        │        _G3.crt 
│     │                 │                        ├ [95] : /usr/share/ca-certificates/mozilla/QuoVadis_Root_CA_2
│     │                 │                        │        .crt 
│     │                 │                        ├ [96] : /usr/share/ca-certificates/mozilla/QuoVadis_Root_CA_2
│     │                 │                        │        _G3.crt 
│     │                 │                        ├ [97] : /usr/share/ca-certificates/mozilla/QuoVadis_Root_CA_3
│     │                 │                        │        .crt 
│     │                 │                        ├ [98] : /usr/share/ca-certificates/mozilla/QuoVadis_Root_CA_3
│     │                 │                        │        _G3.crt 
│     │                 │                        ├ [99] : /usr/share/ca-certificates/mozilla/SSL.com_EV_Root_Ce
│     │                 │                        │        rtification_Authority_ECC.crt 
│     │                 │                        ├ [100]: /usr/share/ca-certificates/mozilla/SSL.com_EV_Root_Ce
│     │                 │                        │        rtification_Authority_RSA_R2.crt 
│     │                 │                        ├ [101]: /usr/share/ca-certificates/mozilla/SSL.com_Root_Certi
│     │                 │                        │        fication_Authority_ECC.crt 
│     │                 │                        ├ [102]: /usr/share/ca-certificates/mozilla/SSL.com_Root_Certi
│     │                 │                        │        fication_Authority_RSA.crt 
│     │                 │                        ├ [103]: /usr/share/ca-certificates/mozilla/SSL.com_TLS_ECC_Ro
│     │                 │                        │        ot_CA_2022.crt 
│     │                 │                        ├ [104]: /usr/share/ca-certificates/mozilla/SSL.com_TLS_RSA_Ro
│     │                 │                        │        ot_CA_2022.crt 
│     │                 │                        ├ [105]: /usr/share/ca-certificates/mozilla/SZAFIR_ROOT_CA2.crt 
│     │                 │                        ├ [106]: /usr/share/ca-certificates/mozilla/Sectigo_Public_Ser
│     │                 │                        │        ver_Authentication_Root_E46.crt 
│     │                 │                        ├ [107]: /usr/share/ca-certificates/mozilla/Sectigo_Public_Ser
│     │                 │                        │        ver_Authentication_Root_R46.crt 
│     │                 │                        ├ [108]: /usr/share/ca-certificates/mozilla/SecureSign_RootCA1
│     │                 │                        │        1.crt 
│     │                 │                        ├ [109]: /usr/share/ca-certificates/mozilla/SecureSign_Root_CA
│     │                 │                        │        12.crt 
│     │                 │                        ├ [110]: /usr/share/ca-certificates/mozilla/SecureSign_Root_CA
│     │                 │                        │        14.crt 
│     │                 │                        ├ [111]: /usr/share/ca-certificates/mozilla/SecureSign_Root_CA
│     │                 │                        │        15.crt 
│     │                 │                        ├ [112]: /usr/share/ca-certificates/mozilla/SecureTrust_CA.crt 
│     │                 │                        ├ [113]: /usr/share/ca-certificates/mozilla/Secure_Global_CA.crt 
│     │                 │                        ├ [114]: /usr/share/ca-certificates/mozilla/Security_Communica
│     │                 │                        │        tion_ECC_RootCA1.crt 
│     │                 │                        ├ [115]: /usr/share/ca-certificates/mozilla/Security_Communica
│     │                 │                        │        tion_RootCA2.crt 
│     │                 │                        ├ [116]: /usr/share/ca-certificates/mozilla/Security_Communica
│     │                 │                        │        tion_RootCA3.crt 
│     │                 │                        ├ [117]: /usr/share/ca-certificates/mozilla/Starfield_Class_2_
│     │                 │                        │        CA.crt 
│     │                 │                        ├ [118]: /usr/share/ca-certificates/mozilla/Starfield_Root_Cer
│     │                 │                        │        tificate_Authority_-_G2.crt 
│     │                 │                        ├ [119]: /usr/share/ca-certificates/mozilla/Starfield_Services
│     │                 │                        │        _Root_Certificate_Authority_-_G2.crt 
│     │                 │                        ├ [120]: /usr/share/ca-certificates/mozilla/SwissSign_Gold_CA_
│     │                 │                        │        -_G2.crt 
│     │                 │                        ├ [121]: /usr/share/ca-certificates/mozilla/SwissSign_Silver_C
│     │                 │                        │        A_-_G2.crt 
│     │                 │                        ├ [122]: /usr/share/ca-certificates/mozilla/T-TeleSec_GlobalRo
│     │                 │                        │        ot_Class_2.crt 
│     │                 │                        ├ [123]: /usr/share/ca-certificates/mozilla/T-TeleSec_GlobalRo
│     │                 │                        │        ot_Class_3.crt 
│     │                 │                        ├ [124]: /usr/share/ca-certificates/mozilla/TUBITAK_Kamu_SM_SS
│     │                 │                        │        L_Kok_Sertifikasi_-_Surum_1.crt 
│     │                 │                        ├ [125]: /usr/share/ca-certificates/mozilla/TWCA_CYBER_Root_CA
│     │                 │                        │        .crt 
│     │                 │                        ├ [126]: /usr/share/ca-certificates/mozilla/TWCA_Global_Root_C
│     │                 │                        │        A.crt 
│     │                 │                        ├ [127]: /usr/share/ca-certificates/mozilla/TWCA_Root_Certific
│     │                 │                        │        ation_Authority.crt 
│     │                 │                        ├ [128]: /usr/share/ca-certificates/mozilla/Telekom_Security_T
│     │                 │                        │        LS_ECC_Root_2020.crt 
│     │                 │                        ├ [129]: /usr/share/ca-certificates/mozilla/Telekom_Security_T
│     │                 │                        │        LS_RSA_Root_2023.crt 
│     │                 │                        ├ [130]: /usr/share/ca-certificates/mozilla/TeliaSonera_Root_C
│     │                 │                        │        A_v1.crt 
│     │                 │                        ├ [131]: /usr/share/ca-certificates/mozilla/Telia_Root_CA_v2.crt 
│     │                 │                        ├ [132]: /usr/share/ca-certificates/mozilla/TrustAsia_Global_R
│     │                 │                        │        oot_CA_G3.crt 
│     │                 │                        ├ [133]: /usr/share/ca-certificates/mozilla/TrustAsia_Global_R
│     │                 │                        │        oot_CA_G4.crt 
│     │                 │                        ├ [134]: /usr/share/ca-certificates/mozilla/Trustwave_Global_C
│     │                 │                        │        ertification_Authority.crt 
│     │                 │                        ├ [135]: /usr/share/ca-certificates/mozilla/Trustwave_Global_E
│     │                 │                        │        CC_P256_Certification_Authority.crt 
│     │                 │                        ├ [136]: /usr/share/ca-certificates/mozilla/Trustwave_Global_E
│     │                 │                        │        CC_P384_Certification_Authority.crt 
│     │                 │                        ├ [137]: /usr/share/ca-certificates/mozilla/TunTrust_Root_CA.crt 
│     │                 │                        ├ [138]: /usr/share/ca-certificates/mozilla/UCA_Extended_Valid
│     │                 │                        │        ation_Root.crt 
│     │                 │                        ├ [139]: /usr/share/ca-certificates/mozilla/UCA_Global_G2_Root
│     │                 │                        │        .crt 
│     │                 │                        ├ [140]: /usr/share/ca-certificates/mozilla/USERTrust_ECC_Cert
│     │                 │                        │        ification_Authority.crt 
│     │                 │                        ├ [141]: /usr/share/ca-certificates/mozilla/USERTrust_RSA_Cert
│     │                 │                        │        ification_Authority.crt 
│     │                 │                        ├ [142]: /usr/share/ca-certificates/mozilla/XRamp_Global_CA_Ro
│     │                 │                        │        ot.crt 
│     │                 │                        ├ [143]: /usr/share/ca-certificates/mozilla/certSIGN_ROOT_CA.crt 
│     │                 │                        ├ [144]: /usr/share/ca-certificates/mozilla/certSIGN_Root_CA_G
│     │                 │                        │        2.crt 
│     │                 │                        ├ [145]: /usr/share/ca-certificates/mozilla/e-Szigno_Root_CA_2
│     │                 │                        │        017.crt 
│     │                 │                        ├ [146]: /usr/share/ca-certificates/mozilla/ePKI_Root_Certific
│     │                 │                        │        ation_Authority.crt 
│     │                 │                        ├ [147]: /usr/share/ca-certificates/mozilla/emSign_ECC_Root_CA
│     │                 │                        │        _-_C3.crt 
│     │                 │                        ├ [148]: /usr/share/ca-certificates/mozilla/emSign_ECC_Root_CA
│     │                 │                        │        _-_G3.crt 
│     │                 │                        ├ [149]: /usr/share/ca-certificates/mozilla/emSign_Root_CA_-_C
│     │                 │                        │        1.crt 
│     │                 │                        ├ [150]: /usr/share/ca-certificates/mozilla/emSign_Root_CA_-_G
│     │                 │                        │        1.crt 
│     │                 │                        ├ [151]: /usr/share/ca-certificates/mozilla/vTrus_ECC_Root_CA.
│     │                 │                        │        crt 
│     │                 │                        ├ [152]: /usr/share/ca-certificates/mozilla/vTrus_Root_CA.crt 
│     │                 │                        ├ [153]: /usr/share/doc/ca-certificates/README.Debian 
│     │                 │                        ├ [154]: /usr/share/doc/ca-certificates/changelog.gz 
│     │                 │                        ├ [155]: /usr/share/doc/ca-certificates/copyright 
│     │                 │                        ├ [156]: /usr/share/doc/ca-certificates/examples/ca-certificat
│     │                 │                        │        es-local/Makefile 
│     │                 │                        ├ [157]: /usr/share/doc/ca-certificates/examples/ca-certificat
│     │                 │                        │        es-local/README 
│     │                 │                        ├ [158]: /usr/share/doc/ca-certificates/examples/ca-certificat
│     │                 │                        │        es-local/debian/ca-certificates-local.triggers 
│     │                 │                        ├ [159]: /usr/share/doc/ca-certificates/examples/ca-certificat
│     │                 │                        │        es-local/debian/changelog 
│     │                 │                        ├ [160]: /usr/share/doc/ca-certificates/examples/ca-certificat
│     │                 │                        │        es-local/debian/compat 
│     │                 │                        ├ [161]: /usr/share/doc/ca-certificates/examples/ca-certificat
│     │                 │                        │        es-local/debian/control 
│     │                 │                        ├ [162]: /usr/share/doc/ca-certificates/examples/ca-certificat
│     │                 │                        │        es-local/debian/copyright 
│     │                 │                        ├ [163]: /usr/share/doc/ca-certificates/examples/ca-certificat
│     │                 │                        │        es-local/debian/postrm 
│     │                 │                        ├ [164]: /usr/share/doc/ca-certificates/examples/ca-certificat
│     │                 │                        │        es-local/debian/rules 
│     │                 │                        ├ [165]: /usr/share/doc/ca-certificates/examples/ca-certificat
│     │                 │                        │        es-local/debian/source/format 
│     │                 │                        ├ [166]: /usr/share/doc/ca-certificates/examples/ca-certificat
│     │                 │                        │        es-local/local/Local_Root_CA.crt 
│     │                 │                        ├ [167]: /usr/share/doc/ca-certificates/examples/ca-certificat
│     │                 │                        │        es-local/local/Makefile 
│     │                 │                        ╰ [168]: /usr/share/man/man8/update-ca-certificates.8.gz 
│     │                 ├ [7]   ╭ ID            : coreutils@9.5-1ubuntu1.25.04.2 
│     │                 │       ├ Name          : coreutils 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/coreutils@9.5-1ubuntu1.25.04.2?arch=amd
│     │                 │       │                │       64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : fb90d22e49e1fb47 
│     │                 │       ├ Version       : 9.5 
│     │                 │       ├ Release       : 1ubuntu1.25.04.2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : coreutils 
│     │                 │       ├ SrcVersion    : 9.5 
│     │                 │       ├ SrcRelease    : 1ubuntu1.25.04.2 
│     │                 │       ├ Licenses       ╭ [0]: GPL-3.0-or-later 
│     │                 │       │                ├ [1]: BSD-4-Clause-UC 
│     │                 │       │                ├ [2]: GPL-3.0-only 
│     │                 │       │                ├ [3]: ISC 
│     │                 │       │                ├ [4]: FSFULLR 
│     │                 │       │                ├ [5]: GFDL-1.3-no-invariants-only 
│     │                 │       │                ╰ [6]: GFDL-1.3-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/bin/[ 
│     │                 │                        ├ [1]  : /usr/bin/arch 
│     │                 │                        ├ [2]  : /usr/bin/b2sum 
│     │                 │                        ├ [3]  : /usr/bin/base32 
│     │                 │                        ├ [4]  : /usr/bin/base64 
│     │                 │                        ├ [5]  : /usr/bin/basename 
│     │                 │                        ├ [6]  : /usr/bin/basenc 
│     │                 │                        ├ [7]  : /usr/bin/cat 
│     │                 │                        ├ [8]  : /usr/bin/chcon 
│     │                 │                        ├ [9]  : /usr/bin/chgrp 
│     │                 │                        ├ [10] : /usr/bin/chmod 
│     │                 │                        ├ [11] : /usr/bin/chown 
│     │                 │                        ├ [12] : /usr/bin/cksum 
│     │                 │                        ├ [13] : /usr/bin/comm 
│     │                 │                        ├ [14] : /usr/bin/cp 
│     │                 │                        ├ [15] : /usr/bin/csplit 
│     │                 │                        ├ [16] : /usr/bin/cut 
│     │                 │                        ├ [17] : /usr/bin/date 
│     │                 │                        ├ [18] : /usr/bin/dd 
│     │                 │                        ├ [19] : /usr/bin/df 
│     │                 │                        ├ [20] : /usr/bin/dir 
│     │                 │                        ├ [21] : /usr/bin/dircolors 
│     │                 │                        ├ [22] : /usr/bin/dirname 
│     │                 │                        ├ [23] : /usr/bin/du 
│     │                 │                        ├ [24] : /usr/bin/echo 
│     │                 │                        ├ [25] : /usr/bin/env 
│     │                 │                        ├ [26] : /usr/bin/expand 
│     │                 │                        ├ [27] : /usr/bin/expr 
│     │                 │                        ├ [28] : /usr/bin/factor 
│     │                 │                        ├ [29] : /usr/bin/false 
│     │                 │                        ├ [30] : /usr/bin/fmt 
│     │                 │                        ├ [31] : /usr/bin/fold 
│     │                 │                        ├ [32] : /usr/bin/groups 
│     │                 │                        ├ [33] : /usr/bin/head 
│     │                 │                        ├ [34] : /usr/bin/hostid 
│     │                 │                        ├ [35] : /usr/bin/id 
│     │                 │                        ├ [36] : /usr/bin/install 
│     │                 │                        ├ [37] : /usr/bin/join 
│     │                 │                        ├ [38] : /usr/bin/link 
│     │                 │                        ├ [39] : /usr/bin/ln 
│     │                 │                        ├ [40] : /usr/bin/logname 
│     │                 │                        ├ [41] : /usr/bin/ls 
│     │                 │                        ├ [42] : /usr/bin/md5sum 
│     │                 │                        ├ [43] : /usr/bin/mkdir 
│     │                 │                        ├ [44] : /usr/bin/mkfifo 
│     │                 │                        ├ [45] : /usr/bin/mknod 
│     │                 │                        ├ [46] : /usr/bin/mktemp 
│     │                 │                        ├ [47] : /usr/bin/mv 
│     │                 │                        ├ [48] : /usr/bin/nice 
│     │                 │                        ├ [49] : /usr/bin/nl 
│     │                 │                        ├ [50] : /usr/bin/nohup 
│     │                 │                        ├ [51] : /usr/bin/nproc 
│     │                 │                        ├ [52] : /usr/bin/numfmt 
│     │                 │                        ├ [53] : /usr/bin/od 
│     │                 │                        ├ [54] : /usr/bin/paste 
│     │                 │                        ├ [55] : /usr/bin/pathchk 
│     │                 │                        ├ [56] : /usr/bin/pinky 
│     │                 │                        ├ [57] : /usr/bin/pr 
│     │                 │                        ├ [58] : /usr/bin/printenv 
│     │                 │                        ├ [59] : /usr/bin/printf 
│     │                 │                        ├ [60] : /usr/bin/ptx 
│     │                 │                        ├ [61] : /usr/bin/pwd 
│     │                 │                        ├ [62] : /usr/bin/readlink 
│     │                 │                        ├ [63] : /usr/bin/realpath 
│     │                 │                        ├ [64] : /usr/bin/rm 
│     │                 │                        ├ [65] : /usr/bin/rmdir 
│     │                 │                        ├ [66] : /usr/bin/runcon 
│     │                 │                        ├ [67] : /usr/bin/seq 
│     │                 │                        ├ [68] : /usr/bin/sha1sum 
│     │                 │                        ├ [69] : /usr/bin/sha224sum 
│     │                 │                        ├ [70] : /usr/bin/sha256sum 
│     │                 │                        ├ [71] : /usr/bin/sha384sum 
│     │                 │                        ├ [72] : /usr/bin/sha512sum 
│     │                 │                        ├ [73] : /usr/bin/shred 
│     │                 │                        ├ [74] : /usr/bin/shuf 
│     │                 │                        ├ [75] : /usr/bin/sleep 
│     │                 │                        ├ [76] : /usr/bin/sort 
│     │                 │                        ├ [77] : /usr/bin/split 
│     │                 │                        ├ [78] : /usr/bin/stat 
│     │                 │                        ├ [79] : /usr/bin/stdbuf 
│     │                 │                        ├ [80] : /usr/bin/stty 
│     │                 │                        ├ [81] : /usr/bin/sum 
│     │                 │                        ├ [82] : /usr/bin/sync 
│     │                 │                        ├ [83] : /usr/bin/tac 
│     │                 │                        ├ [84] : /usr/bin/tail 
│     │                 │                        ├ [85] : /usr/bin/tee 
│     │                 │                        ├ [86] : /usr/bin/test 
│     │                 │                        ├ [87] : /usr/bin/timeout 
│     │                 │                        ├ [88] : /usr/bin/touch 
│     │                 │                        ├ [89] : /usr/bin/tr 
│     │                 │                        ├ [90] : /usr/bin/true 
│     │                 │                        ├ [91] : /usr/bin/truncate 
│     │                 │                        ├ [92] : /usr/bin/tsort 
│     │                 │                        ├ [93] : /usr/bin/tty 
│     │                 │                        ├ [94] : /usr/bin/uname 
│     │                 │                        ├ [95] : /usr/bin/unexpand 
│     │                 │                        ├ [96] : /usr/bin/uniq 
│     │                 │                        ├ [97] : /usr/bin/unlink 
│     │                 │                        ├ [98] : /usr/bin/users 
│     │                 │                        ├ [99] : /usr/bin/vdir 
│     │                 │                        ├ [100]: /usr/bin/wc 
│     │                 │                        ├ [101]: /usr/bin/who 
│     │                 │                        ├ [102]: /usr/bin/whoami 
│     │                 │                        ├ [103]: /usr/bin/yes 
│     │                 │                        ├ [104]: /usr/libexec/coreutils/libstdbuf.so 
│     │                 │                        ├ [105]: /usr/sbin/chroot 
│     │                 │                        ├ [106]: /usr/share/doc/coreutils/AUTHORS 
│     │                 │                        ├ [107]: /usr/share/doc/coreutils/NEWS.gz 
│     │                 │                        ├ [108]: /usr/share/doc/coreutils/README.Debian 
│     │                 │                        ├ [109]: /usr/share/doc/coreutils/README.gz 
│     │                 │                        ├ [110]: /usr/share/doc/coreutils/THANKS.gz 
│     │                 │                        ├ [111]: /usr/share/doc/coreutils/TODO.gz 
│     │                 │                        ├ [112]: /usr/share/doc/coreutils/changelog.Debian.gz 
│     │                 │                        ├ [113]: /usr/share/doc/coreutils/copyright 
│     │                 │                        ├ [114]: /usr/share/info/coreutils.info.gz 
│     │                 │                        ├ [115]: /usr/share/man/man1/arch.1.gz 
│     │                 │                        ├ [116]: /usr/share/man/man1/b2sum.1.gz 
│     │                 │                        ├ [117]: /usr/share/man/man1/base32.1.gz 
│     │                 │                        ├ [118]: /usr/share/man/man1/base64.1.gz 
│     │                 │                        ├ [119]: /usr/share/man/man1/basename.1.gz 
│     │                 │                        ├ [120]: /usr/share/man/man1/basenc.1.gz 
│     │                 │                        ├ [121]: /usr/share/man/man1/cat.1.gz 
│     │                 │                        ├ [122]: /usr/share/man/man1/chcon.1.gz 
│     │                 │                        ├ [123]: /usr/share/man/man1/chgrp.1.gz 
│     │                 │                        ├ [124]: /usr/share/man/man1/chmod.1.gz 
│     │                 │                        ├ [125]: /usr/share/man/man1/chown.1.gz 
│     │                 │                        ├ [126]: /usr/share/man/man1/cksum.1.gz 
│     │                 │                        ├ [127]: /usr/share/man/man1/comm.1.gz 
│     │                 │                        ├ [128]: /usr/share/man/man1/cp.1.gz 
│     │                 │                        ├ [129]: /usr/share/man/man1/csplit.1.gz 
│     │                 │                        ├ [130]: /usr/share/man/man1/cut.1.gz 
│     │                 │                        ├ [131]: /usr/share/man/man1/date.1.gz 
│     │                 │                        ├ [132]: /usr/share/man/man1/dd.1.gz 
│     │                 │                        ├ [133]: /usr/share/man/man1/df.1.gz 
│     │                 │                        ├ [134]: /usr/share/man/man1/dir.1.gz 
│     │                 │                        ├ [135]: /usr/share/man/man1/dircolors.1.gz 
│     │                 │                        ├ [136]: /usr/share/man/man1/dirname.1.gz 
│     │                 │                        ├ [137]: /usr/share/man/man1/du.1.gz 
│     │                 │                        ├ [138]: /usr/share/man/man1/echo.1.gz 
│     │                 │                        ├ [139]: /usr/share/man/man1/env.1.gz 
│     │                 │                        ├ [140]: /usr/share/man/man1/expand.1.gz 
│     │                 │                        ├ [141]: /usr/share/man/man1/expr.1.gz 
│     │                 │                        ├ [142]: /usr/share/man/man1/factor.1.gz 
│     │                 │                        ├ [143]: /usr/share/man/man1/false.1.gz 
│     │                 │                        ├ [144]: /usr/share/man/man1/fmt.1.gz 
│     │                 │                        ├ [145]: /usr/share/man/man1/fold.1.gz 
│     │                 │                        ├ [146]: /usr/share/man/man1/groups.1.gz 
│     │                 │                        ├ [147]: /usr/share/man/man1/head.1.gz 
│     │                 │                        ├ [148]: /usr/share/man/man1/hostid.1.gz 
│     │                 │                        ├ [149]: /usr/share/man/man1/id.1.gz 
│     │                 │                        ├ [150]: /usr/share/man/man1/install.1.gz 
│     │                 │                        ├ [151]: /usr/share/man/man1/join.1.gz 
│     │                 │                        ├ [152]: /usr/share/man/man1/link.1.gz 
│     │                 │                        ├ [153]: /usr/share/man/man1/ln.1.gz 
│     │                 │                        ├ [154]: /usr/share/man/man1/logname.1.gz 
│     │                 │                        ├ [155]: /usr/share/man/man1/ls.1.gz 
│     │                 │                        ├ [156]: /usr/share/man/man1/md5sum.1.gz 
│     │                 │                        ├ [157]: /usr/share/man/man1/mkdir.1.gz 
│     │                 │                        ├ [158]: /usr/share/man/man1/mkfifo.1.gz 
│     │                 │                        ├ [159]: /usr/share/man/man1/mknod.1.gz 
│     │                 │                        ├ [160]: /usr/share/man/man1/mktemp.1.gz 
│     │                 │                        ├ [161]: /usr/share/man/man1/mv.1.gz 
│     │                 │                        ├ [162]: /usr/share/man/man1/nice.1.gz 
│     │                 │                        ├ [163]: /usr/share/man/man1/nl.1.gz 
│     │                 │                        ├ [164]: /usr/share/man/man1/nohup.1.gz 
│     │                 │                        ├ [165]: /usr/share/man/man1/nproc.1.gz 
│     │                 │                        ├ [166]: /usr/share/man/man1/numfmt.1.gz 
│     │                 │                        ├ [167]: /usr/share/man/man1/od.1.gz 
│     │                 │                        ├ [168]: /usr/share/man/man1/paste.1.gz 
│     │                 │                        ├ [169]: /usr/share/man/man1/pathchk.1.gz 
│     │                 │                        ├ [170]: /usr/share/man/man1/pinky.1.gz 
│     │                 │                        ├ [171]: /usr/share/man/man1/pr.1.gz 
│     │                 │                        ├ [172]: /usr/share/man/man1/printenv.1.gz 
│     │                 │                        ├ [173]: /usr/share/man/man1/printf.1.gz 
│     │                 │                        ├ [174]: /usr/share/man/man1/ptx.1.gz 
│     │                 │                        ├ [175]: /usr/share/man/man1/pwd.1.gz 
│     │                 │                        ├ [176]: /usr/share/man/man1/readlink.1.gz 
│     │                 │                        ├ [177]: /usr/share/man/man1/realpath.1.gz 
│     │                 │                        ├ [178]: /usr/share/man/man1/rm.1.gz 
│     │                 │                        ├ [179]: /usr/share/man/man1/rmdir.1.gz 
│     │                 │                        ├ [180]: /usr/share/man/man1/runcon.1.gz 
│     │                 │                        ├ [181]: /usr/share/man/man1/seq.1.gz 
│     │                 │                        ├ [182]: /usr/share/man/man1/sha1sum.1.gz 
│     │                 │                        ├ [183]: /usr/share/man/man1/sha224sum.1.gz 
│     │                 │                        ├ [184]: /usr/share/man/man1/sha256sum.1.gz 
│     │                 │                        ├ [185]: /usr/share/man/man1/sha384sum.1.gz 
│     │                 │                        ├ [186]: /usr/share/man/man1/sha512sum.1.gz 
│     │                 │                        ├ [187]: /usr/share/man/man1/shred.1.gz 
│     │                 │                        ├ [188]: /usr/share/man/man1/shuf.1.gz 
│     │                 │                        ├ [189]: /usr/share/man/man1/sleep.1.gz 
│     │                 │                        ├ [190]: /usr/share/man/man1/sort.1.gz 
│     │                 │                        ├ [191]: /usr/share/man/man1/split.1.gz 
│     │                 │                        ├ [192]: /usr/share/man/man1/stat.1.gz 
│     │                 │                        ├ [193]: /usr/share/man/man1/stdbuf.1.gz 
│     │                 │                        ├ [194]: /usr/share/man/man1/stty.1.gz 
│     │                 │                        ├ [195]: /usr/share/man/man1/sum.1.gz 
│     │                 │                        ├ [196]: /usr/share/man/man1/sync.1.gz 
│     │                 │                        ├ [197]: /usr/share/man/man1/tac.1.gz 
│     │                 │                        ├ [198]: /usr/share/man/man1/tail.1.gz 
│     │                 │                        ├ [199]: /usr/share/man/man1/tee.1.gz 
│     │                 │                        ├ [200]: /usr/share/man/man1/test.1.gz 
│     │                 │                        ├ [201]: /usr/share/man/man1/timeout.1.gz 
│     │                 │                        ├ [202]: /usr/share/man/man1/touch.1.gz 
│     │                 │                        ├ [203]: /usr/share/man/man1/tr.1.gz 
│     │                 │                        ├ [204]: /usr/share/man/man1/true.1.gz 
│     │                 │                        ├ [205]: /usr/share/man/man1/truncate.1.gz 
│     │                 │                        ├ [206]: /usr/share/man/man1/tsort.1.gz 
│     │                 │                        ├ [207]: /usr/share/man/man1/tty.1.gz 
│     │                 │                        ├ [208]: /usr/share/man/man1/uname.1.gz 
│     │                 │                        ├ [209]: /usr/share/man/man1/unexpand.1.gz 
│     │                 │                        ├ [210]: /usr/share/man/man1/uniq.1.gz 
│     │                 │                        ├ [211]: /usr/share/man/man1/unlink.1.gz 
│     │                 │                        ├ [212]: /usr/share/man/man1/users.1.gz 
│     │                 │                        ├ [213]: /usr/share/man/man1/vdir.1.gz 
│     │                 │                        ├ [214]: /usr/share/man/man1/wc.1.gz 
│     │                 │                        ├ [215]: /usr/share/man/man1/who.1.gz 
│     │                 │                        ├ [216]: /usr/share/man/man1/whoami.1.gz 
│     │                 │                        ├ [217]: /usr/share/man/man1/yes.1.gz 
│     │                 │                        ╰ [218]: /usr/share/man/man8/chroot.8.gz 
│     │                 ├ [8]   ╭ ID            : curl@8.12.1-3ubuntu1 
│     │                 │       ├ Name          : curl 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/curl@8.12.1-3ubuntu1?arch=amd64&distro=
│     │                 │       │                │       ubuntu-25.04 
│     │                 │       │                ╰ UID : 6ea7a92c5821dca8 
│     │                 │       ├ Version       : 8.12.1 
│     │                 │       ├ Release       : 3ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : curl 
│     │                 │       ├ SrcVersion    : 8.12.1 
│     │                 │       ├ SrcRelease    : 3ubuntu1 
│     │                 │       ├ Licenses       ╭ [0] : curl 
│     │                 │       │                ├ [1] : OLDAP-2.8 
│     │                 │       │                ├ [2] : ISC 
│     │                 │       │                ├ [3] : GPL-2+ with Autoconf-data exception 
│     │                 │       │                ├ [4] : GPL-3+ with Autoconf-data exception 
│     │                 │       │                ├ [5] : GPL-2+ with Libtool exception 
│     │                 │       │                ├ [6] : BSD-3-Clause 
│     │                 │       │                ├ [7] : BSD-4-Clause-UC 
│     │                 │       │                ├ [8] : FSFULLR 
│     │                 │       │                ├ [9] : X11 
│     │                 │       │                ╰ [10]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [1]: libcurl4t64@8.12.1-3ubuntu1 
│     │                 │       │                ╰ [2]: zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/bin/curl 
│     │                 │                        ├ [1]: /usr/bin/wcurl 
│     │                 │                        ├ [2]: /usr/share/doc/curl/NEWS.Debian.gz 
│     │                 │                        ├ [3]: /usr/share/doc/curl/README.Debian 
│     │                 │                        ├ [4]: /usr/share/doc/curl/copyright 
│     │                 │                        ├ [5]: /usr/share/fish/vendor_completions.d/curl.fish 
│     │                 │                        ├ [6]: /usr/share/man/man1/curl.1.gz 
│     │                 │                        ├ [7]: /usr/share/man/man1/wcurl.1.gz 
│     │                 │                        ╰ [8]: /usr/share/zsh/vendor-completions/_curl 
│     │                 ├ [9]   ╭ ID            : dash@0.5.12-12ubuntu1 
│     │                 │       ├ Name          : dash 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/dash@0.5.12-12ubuntu1?arch=amd64&distro
│     │                 │       │                │       =ubuntu-25.04 
│     │                 │       │                ╰ UID : 723794bf9a788d15 
│     │                 │       ├ Version       : 0.5.12 
│     │                 │       ├ Release       : 12ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : dash 
│     │                 │       ├ SrcVersion    : 0.5.12 
│     │                 │       ├ SrcRelease    : 12ubuntu1 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ├ [1]: public-domain 
│     │                 │       │                ├ [2]: GPL-2.0-or-later 
│     │                 │       │                ╰ [3]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: debianutils@5.21 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:61abacb715e51396ddb5bd675cd0474a753cb627d74cba781f96d4
│     │                 │       │                 c026da35c4 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/bin/dash 
│     │                 │                        ├ [1]: /usr/share/debianutils/shells.d/dash 
│     │                 │                        ├ [2]: /usr/share/doc/dash/README.Debian.diet 
│     │                 │                        ├ [3]: /usr/share/doc/dash/README.source 
│     │                 │                        ├ [4]: /usr/share/doc/dash/changelog.Debian.gz 
│     │                 │                        ├ [5]: /usr/share/doc/dash/copyright 
│     │                 │                        ├ [6]: /usr/share/lintian/overrides/dash 
│     │                 │                        ├ [7]: /usr/share/man/man1/dash.1.gz 
│     │                 │                        ╰ [8]: /usr/share/menu/dash 
│     │                 ├ [10]  ╭ ID            : debconf@1.5.87ubuntu1 
│     │                 │       ├ Name          : debconf 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/debconf@1.5.87ubuntu1?arch=all&distro=u
│     │                 │       │                │       buntu-25.04 
│     │                 │       │                ╰ UID : 2ec3b95e81811272 
│     │                 │       ├ Version       : 1.5.87ubuntu1 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : debconf 
│     │                 │       ├ SrcVersion    : 1.5.87ubuntu1 
│     │                 │       ├ Licenses       ─ [0]: BSD-2-Clause 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:fa7c662338d41bf69b6704234453a67254457f8ccbd1a22df6952a
│     │                 │       │                 d726c4c64e 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/bin/debconf 
│     │                 │                        ├ [1]  : /usr/bin/debconf-apt-progress 
│     │                 │                        ├ [2]  : /usr/bin/debconf-communicate 
│     │                 │                        ├ [3]  : /usr/bin/debconf-copydb 
│     │                 │                        ├ [4]  : /usr/bin/debconf-escape 
│     │                 │                        ├ [5]  : /usr/bin/debconf-set-selections 
│     │                 │                        ├ [6]  : /usr/bin/debconf-show 
│     │                 │                        ├ [7]  : /usr/sbin/dpkg-preconfigure 
│     │                 │                        ├ [8]  : /usr/sbin/dpkg-reconfigure 
│     │                 │                        ├ [9]  : /usr/share/bash-completion/completions/debconf 
│     │                 │                        ├ [10] : /usr/share/debconf/confmodule 
│     │                 │                        ├ [11] : /usr/share/debconf/confmodule.sh 
│     │                 │                        ├ [12] : /usr/share/debconf/debconf.conf 
│     │                 │                        ├ [13] : /usr/share/debconf/fix_db.pl 
│     │                 │                        ├ [14] : /usr/share/debconf/frontend 
│     │                 │                        ├ [15] : /usr/share/doc/debconf/README.Debian 
│     │                 │                        ├ [16] : /usr/share/doc/debconf/changelog.gz 
│     │                 │                        ├ [17] : /usr/share/doc/debconf/copyright 
│     │                 │                        ├ [18] : /usr/share/lintian/overrides/debconf 
│     │                 │                        ├ [19] : /usr/share/man/man1/debconf-apt-progress.1.gz 
│     │                 │                        ├ [20] : /usr/share/man/man1/debconf-communicate.1.gz 
│     │                 │                        ├ [21] : /usr/share/man/man1/debconf-copydb.1.gz 
│     │                 │                        ├ [22] : /usr/share/man/man1/debconf-escape.1.gz 
│     │                 │                        ├ [23] : /usr/share/man/man1/debconf-set-selections.1.gz 
│     │                 │                        ├ [24] : /usr/share/man/man1/debconf-show.1.gz 
│     │                 │                        ├ [25] : /usr/share/man/man1/debconf.1.gz 
│     │                 │                        ├ [26] : /usr/share/man/man8/dpkg-preconfigure.8.gz 
│     │                 │                        ├ [27] : /usr/share/man/man8/dpkg-reconfigure.8.gz 
│     │                 │                        ├ [28] : /usr/share/perl5/Debconf/AutoSelect.pm 
│     │                 │                        ├ [29] : /usr/share/perl5/Debconf/Base.pm 
│     │                 │                        ├ [30] : /usr/share/perl5/Debconf/Client/ConfModule.pm 
│     │                 │                        ├ [31] : /usr/share/perl5/Debconf/ConfModule.pm 
│     │                 │                        ├ [32] : /usr/share/perl5/Debconf/Config.pm 
│     │                 │                        ├ [33] : /usr/share/perl5/Debconf/Db.pm 
│     │                 │                        ├ [34] : /usr/share/perl5/Debconf/DbDriver.pm 
│     │                 │                        ├ [35] : /usr/share/perl5/Debconf/DbDriver/Backup.pm 
│     │                 │                        ├ [36] : /usr/share/perl5/Debconf/DbDriver/Cache.pm 
│     │                 │                        ├ [37] : /usr/share/perl5/Debconf/DbDriver/Copy.pm 
│     │                 │                        ├ [38] : /usr/share/perl5/Debconf/DbDriver/Debug.pm 
│     │                 │                        ├ [39] : /usr/share/perl5/Debconf/DbDriver/DirTree.pm 
│     │                 │                        ├ [40] : /usr/share/perl5/Debconf/DbDriver/Directory.pm 
│     │                 │                        ├ [41] : /usr/share/perl5/Debconf/DbDriver/File.pm 
│     │                 │                        ├ [42] : /usr/share/perl5/Debconf/DbDriver/LDAP.pm 
│     │                 │                        ├ [43] : /usr/share/perl5/Debconf/DbDriver/PackageDir.pm 
│     │                 │                        ├ [44] : /usr/share/perl5/Debconf/DbDriver/Pipe.pm 
│     │                 │                        ├ [45] : /usr/share/perl5/Debconf/DbDriver/Stack.pm 
│     │                 │                        ├ [46] : /usr/share/perl5/Debconf/Element.pm 
│     │                 │                        ├ [47] : /usr/share/perl5/Debconf/Element/Dialog/Boolean.pm 
│     │                 │                        ├ [48] : /usr/share/perl5/Debconf/Element/Dialog/Error.pm 
│     │                 │                        ├ [49] : /usr/share/perl5/Debconf/Element/Dialog/Multiselect.pm 
│     │                 │                        ├ [50] : /usr/share/perl5/Debconf/Element/Dialog/Note.pm 
│     │                 │                        ├ [51] : /usr/share/perl5/Debconf/Element/Dialog/Password.pm 
│     │                 │                        ├ [52] : /usr/share/perl5/Debconf/Element/Dialog/Progress.pm 
│     │                 │                        ├ [53] : /usr/share/perl5/Debconf/Element/Dialog/Select.pm 
│     │                 │                        ├ [54] : /usr/share/perl5/Debconf/Element/Dialog/String.pm 
│     │                 │                        ├ [55] : /usr/share/perl5/Debconf/Element/Dialog/Text.pm 
│     │                 │                        ├ [56] : /usr/share/perl5/Debconf/Element/Editor/Boolean.pm 
│     │                 │                        ├ [57] : /usr/share/perl5/Debconf/Element/Editor/Error.pm 
│     │                 │                        ├ [58] : /usr/share/perl5/Debconf/Element/Editor/Multiselect.pm 
│     │                 │                        ├ [59] : /usr/share/perl5/Debconf/Element/Editor/Note.pm 
│     │                 │                        ├ [60] : /usr/share/perl5/Debconf/Element/Editor/Password.pm 
│     │                 │                        ├ [61] : /usr/share/perl5/Debconf/Element/Editor/Progress.pm 
│     │                 │                        ├ [62] : /usr/share/perl5/Debconf/Element/Editor/Select.pm 
│     │                 │                        ├ [63] : /usr/share/perl5/Debconf/Element/Editor/String.pm 
│     │                 │                        ├ [64] : /usr/share/perl5/Debconf/Element/Editor/Text.pm 
│     │                 │                        ├ [65] : /usr/share/perl5/Debconf/Element/Gnome.pm 
│     │                 │                        ├ [66] : /usr/share/perl5/Debconf/Element/Gnome/Boolean.pm 
│     │                 │                        ├ [67] : /usr/share/perl5/Debconf/Element/Gnome/Error.pm 
│     │                 │                        ├ [68] : /usr/share/perl5/Debconf/Element/Gnome/Multiselect.pm 
│     │                 │                        ├ [69] : /usr/share/perl5/Debconf/Element/Gnome/Note.pm 
│     │                 │                        ├ [70] : /usr/share/perl5/Debconf/Element/Gnome/Password.pm 
│     │                 │                        ├ [71] : /usr/share/perl5/Debconf/Element/Gnome/Progress.pm 
│     │                 │                        ├ [72] : /usr/share/perl5/Debconf/Element/Gnome/Select.pm 
│     │                 │                        ├ [73] : /usr/share/perl5/Debconf/Element/Gnome/String.pm 
│     │                 │                        ├ [74] : /usr/share/perl5/Debconf/Element/Gnome/Text.pm 
│     │                 │                        ├ [75] : /usr/share/perl5/Debconf/Element/Multiselect.pm 
│     │                 │                        ├ [76] : /usr/share/perl5/Debconf/Element/Noninteractive.pm 
│     │                 │                        ├ [77] : /usr/share/perl5/Debconf/Element/Noninteractive/Boole
│     │                 │                        │        an.pm 
│     │                 │                        ├ [78] : /usr/share/perl5/Debconf/Element/Noninteractive/Error
│     │                 │                        │        .pm 
│     │                 │                        ├ [79] : /usr/share/perl5/Debconf/Element/Noninteractive/Multi
│     │                 │                        │        select.pm 
│     │                 │                        ├ [80] : /usr/share/perl5/Debconf/Element/Noninteractive/Note.pm 
│     │                 │                        ├ [81] : /usr/share/perl5/Debconf/Element/Noninteractive/Passw
│     │                 │                        │        ord.pm 
│     │                 │                        ├ [82] : /usr/share/perl5/Debconf/Element/Noninteractive/Progr
│     │                 │                        │        ess.pm 
│     │                 │                        ├ [83] : /usr/share/perl5/Debconf/Element/Noninteractive/Selec
│     │                 │                        │        t.pm 
│     │                 │                        ├ [84] : /usr/share/perl5/Debconf/Element/Noninteractive/Strin
│     │                 │                        │        g.pm 
│     │                 │                        ├ [85] : /usr/share/perl5/Debconf/Element/Noninteractive/Text.pm 
│     │                 │                        ├ [86] : /usr/share/perl5/Debconf/Element/Select.pm 
│     │                 │                        ├ [87] : /usr/share/perl5/Debconf/Element/Teletype/Boolean.pm 
│     │                 │                        ├ [88] : /usr/share/perl5/Debconf/Element/Teletype/Error.pm 
│     │                 │                        ├ [89] : /usr/share/perl5/Debconf/Element/Teletype/Multiselect
│     │                 │                        │        .pm 
│     │                 │                        ├ [90] : /usr/share/perl5/Debconf/Element/Teletype/Note.pm 
│     │                 │                        ├ [91] : /usr/share/perl5/Debconf/Element/Teletype/Password.pm 
│     │                 │                        ├ [92] : /usr/share/perl5/Debconf/Element/Teletype/Progress.pm 
│     │                 │                        ├ [93] : /usr/share/perl5/Debconf/Element/Teletype/Select.pm 
│     │                 │                        ├ [94] : /usr/share/perl5/Debconf/Element/Teletype/String.pm 
│     │                 │                        ├ [95] : /usr/share/perl5/Debconf/Element/Teletype/Text.pm 
│     │                 │                        ├ [96] : /usr/share/perl5/Debconf/Element/Web/Boolean.pm 
│     │                 │                        ├ [97] : /usr/share/perl5/Debconf/Element/Web/Error.pm 
│     │                 │                        ├ [98] : /usr/share/perl5/Debconf/Element/Web/Multiselect.pm 
│     │                 │                        ├ [99] : /usr/share/perl5/Debconf/Element/Web/Note.pm 
│     │                 │                        ├ [100]: /usr/share/perl5/Debconf/Element/Web/Password.pm 
│     │                 │                        ├ [101]: /usr/share/perl5/Debconf/Element/Web/Progress.pm 
│     │                 │                        ├ [102]: /usr/share/perl5/Debconf/Element/Web/Select.pm 
│     │                 │                        ├ [103]: /usr/share/perl5/Debconf/Element/Web/String.pm 
│     │                 │                        ├ [104]: /usr/share/perl5/Debconf/Element/Web/Text.pm 
│     │                 │                        ├ [105]: /usr/share/perl5/Debconf/Encoding.pm 
│     │                 │                        ├ [106]: /usr/share/perl5/Debconf/Format.pm 
│     │                 │                        ├ [107]: /usr/share/perl5/Debconf/Format/822.pm 
│     │                 │                        ├ [108]: /usr/share/perl5/Debconf/FrontEnd.pm 
│     │                 │                        ├ [109]: /usr/share/perl5/Debconf/FrontEnd/Dialog.pm 
│     │                 │                        ├ [110]: /usr/share/perl5/Debconf/FrontEnd/Editor.pm 
│     │                 │                        ├ [111]: /usr/share/perl5/Debconf/FrontEnd/Gnome.pm 
│     │                 │                        ├ [112]: /usr/share/perl5/Debconf/FrontEnd/Kde.pm 
│     │                 │                        ├ [113]: /usr/share/perl5/Debconf/FrontEnd/Noninteractive.pm 
│     │                 │                        ├ [114]: /usr/share/perl5/Debconf/FrontEnd/Passthrough.pm 
│     │                 │                        ├ [115]: /usr/share/perl5/Debconf/FrontEnd/Readline.pm 
│     │                 │                        ├ [116]: /usr/share/perl5/Debconf/FrontEnd/ScreenSize.pm 
│     │                 │                        ├ [117]: /usr/share/perl5/Debconf/FrontEnd/Teletype.pm 
│     │                 │                        ├ [118]: /usr/share/perl5/Debconf/FrontEnd/Text.pm 
│     │                 │                        ├ [119]: /usr/share/perl5/Debconf/FrontEnd/Web.pm 
│     │                 │                        ├ [120]: /usr/share/perl5/Debconf/Gettext.pm 
│     │                 │                        ├ [121]: /usr/share/perl5/Debconf/Iterator.pm 
│     │                 │                        ├ [122]: /usr/share/perl5/Debconf/Log.pm 
│     │                 │                        ├ [123]: /usr/share/perl5/Debconf/Path.pm 
│     │                 │                        ├ [124]: /usr/share/perl5/Debconf/Priority.pm 
│     │                 │                        ├ [125]: /usr/share/perl5/Debconf/Question.pm 
│     │                 │                        ├ [126]: /usr/share/perl5/Debconf/Template.pm 
│     │                 │                        ├ [127]: /usr/share/perl5/Debconf/Template/Transient.pm 
│     │                 │                        ├ [128]: /usr/share/perl5/Debconf/TmpFile.pm 
│     │                 │                        ├ [129]: /usr/share/perl5/Debian/DebConf/Client/ConfModule.pm 
│     │                 │                        ╰ [130]: /usr/share/pixmaps/debian-logo.png 
│     │                 ├ [11]  ╭ ID            : debianutils@5.21 
│     │                 │       ├ Name          : debianutils 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/debianutils@5.21?arch=amd64&distro=ubun
│     │                 │       │                │       tu-25.04 
│     │                 │       │                ╰ UID : f19f89e04fcf9599 
│     │                 │       ├ Version       : 5.21 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : debianutils 
│     │                 │       ├ SrcVersion    : 5.21 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: GPL-2.0-only 
│     │                 │       │                ├ [2]: public-domain 
│     │                 │       │                ╰ [3]: SMAIL-GPL 
│     │                 │       ├ Maintainer    : Ileana Dumitrescu <ileanadumitrescu95@gmail.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:62267f3691910566f9dfabc6166dbdd4e967f45482a734411a9b39
│     │                 │       │                 9b5947e55d 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/ischroot 
│     │                 │                        ├ [1] : /usr/bin/run-parts 
│     │                 │                        ├ [2] : /usr/bin/savelog 
│     │                 │                        ├ [3] : /usr/bin/tempfile 
│     │                 │                        ├ [4] : /usr/bin/which.debianutils 
│     │                 │                        ├ [5] : /usr/sbin/add-shell 
│     │                 │                        ├ [6] : /usr/sbin/installkernel 
│     │                 │                        ├ [7] : /usr/sbin/remove-shell 
│     │                 │                        ├ [8] : /usr/sbin/update-shells 
│     │                 │                        ├ [9] : /usr/share/debianutils/shells 
│     │                 │                        ├ [10]: /usr/share/doc/debianutils/README.shells 
│     │                 │                        ├ [11]: /usr/share/doc/debianutils/changelog.gz 
│     │                 │                        ├ [12]: /usr/share/doc/debianutils/copyright 
│     │                 │                        ├ [13]: /usr/share/man/de/man1/which.debianutils.1.gz 
│     │                 │                        ├ [14]: /usr/share/man/de/man8/add-shell.8.gz 
│     │                 │                        ├ [15]: /usr/share/man/de/man8/installkernel.8.gz 
│     │                 │                        ├ [16]: /usr/share/man/de/man8/remove-shell.8.gz 
│     │                 │                        ├ [17]: /usr/share/man/de/man8/run-parts.8.gz 
│     │                 │                        ├ [18]: /usr/share/man/de/man8/savelog.8.gz 
│     │                 │                        ├ [19]: /usr/share/man/es/man1/which.debianutils.1.gz 
│     │                 │                        ├ [20]: /usr/share/man/es/man8/add-shell.8.gz 
│     │                 │                        ├ [21]: /usr/share/man/es/man8/installkernel.8.gz 
│     │                 │                        ├ [22]: /usr/share/man/es/man8/remove-shell.8.gz 
│     │                 │                        ├ [23]: /usr/share/man/es/man8/run-parts.8.gz 
│     │                 │                        ├ [24]: /usr/share/man/es/man8/savelog.8.gz 
│     │                 │                        ├ [25]: /usr/share/man/fr/man1/which.debianutils.1.gz 
│     │                 │                        ├ [26]: /usr/share/man/fr/man8/add-shell.8.gz 
│     │                 │                        ├ [27]: /usr/share/man/fr/man8/installkernel.8.gz 
│     │                 │                        ├ [28]: /usr/share/man/fr/man8/remove-shell.8.gz 
│     │                 │                        ├ [29]: /usr/share/man/fr/man8/run-parts.8.gz 
│     │                 │                        ├ [30]: /usr/share/man/fr/man8/savelog.8.gz 
│     │                 │                        ├ [31]: /usr/share/man/it/man1/which.debianutils.1.gz 
│     │                 │                        ├ [32]: /usr/share/man/it/man8/add-shell.8.gz 
│     │                 │                        ├ [33]: /usr/share/man/it/man8/installkernel.8.gz 
│     │                 │                        ├ [34]: /usr/share/man/it/man8/remove-shell.8.gz 
│     │                 │                        ├ [35]: /usr/share/man/it/man8/run-parts.8.gz 
│     │                 │                        ├ [36]: /usr/share/man/it/man8/savelog.8.gz 
│     │                 │                        ├ [37]: /usr/share/man/ja/man1/which.debianutils.1.gz 
│     │                 │                        ├ [38]: /usr/share/man/ja/man8/add-shell.8.gz 
│     │                 │                        ├ [39]: /usr/share/man/ja/man8/installkernel.8.gz 
│     │                 │                        ├ [40]: /usr/share/man/ja/man8/remove-shell.8.gz 
│     │                 │                        ├ [41]: /usr/share/man/ja/man8/run-parts.8.gz 
│     │                 │                        ├ [42]: /usr/share/man/ja/man8/savelog.8.gz 
│     │                 │                        ├ [43]: /usr/share/man/man1/ischroot.1.gz 
│     │                 │                        ├ [44]: /usr/share/man/man1/tempfile.1.gz 
│     │                 │                        ├ [45]: /usr/share/man/man1/which.debianutils.1.gz 
│     │                 │                        ├ [46]: /usr/share/man/man8/add-shell.8.gz 
│     │                 │                        ├ [47]: /usr/share/man/man8/installkernel.8.gz 
│     │                 │                        ├ [48]: /usr/share/man/man8/remove-shell.8.gz 
│     │                 │                        ├ [49]: /usr/share/man/man8/run-parts.8.gz 
│     │                 │                        ├ [50]: /usr/share/man/man8/savelog.8.gz 
│     │                 │                        ├ [51]: /usr/share/man/man8/update-shells.8.gz 
│     │                 │                        ├ [52]: /usr/share/man/pl/man1/which.debianutils.1.gz 
│     │                 │                        ├ [53]: /usr/share/man/pl/man8/add-shell.8.gz 
│     │                 │                        ├ [54]: /usr/share/man/pl/man8/installkernel.8.gz 
│     │                 │                        ├ [55]: /usr/share/man/pl/man8/remove-shell.8.gz 
│     │                 │                        ├ [56]: /usr/share/man/pl/man8/run-parts.8.gz 
│     │                 │                        ├ [57]: /usr/share/man/pl/man8/savelog.8.gz 
│     │                 │                        ├ [58]: /usr/share/man/pt/man1/which.debianutils.1.gz 
│     │                 │                        ├ [59]: /usr/share/man/pt/man8/add-shell.8.gz 
│     │                 │                        ├ [60]: /usr/share/man/pt/man8/installkernel.8.gz 
│     │                 │                        ├ [61]: /usr/share/man/pt/man8/remove-shell.8.gz 
│     │                 │                        ├ [62]: /usr/share/man/pt/man8/run-parts.8.gz 
│     │                 │                        ├ [63]: /usr/share/man/pt/man8/savelog.8.gz 
│     │                 │                        ├ [64]: /usr/share/man/sl/man1/which.debianutils.1.gz 
│     │                 │                        ├ [65]: /usr/share/man/sl/man8/add-shell.8.gz 
│     │                 │                        ├ [66]: /usr/share/man/sl/man8/installkernel.8.gz 
│     │                 │                        ├ [67]: /usr/share/man/sl/man8/remove-shell.8.gz 
│     │                 │                        ├ [68]: /usr/share/man/sl/man8/run-parts.8.gz 
│     │                 │                        ╰ [69]: /usr/share/man/sl/man8/savelog.8.gz 
│     │                 ├ [12]  ╭ ID            : diffutils@1:3.10-3 
│     │                 │       ├ Name          : diffutils 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/diffutils@3.10-3?arch=amd64&distro=ubun
│     │                 │       │                │       tu-25.04&epoch=1 
│     │                 │       │                ╰ UID : a30eaf323bb43ab9 
│     │                 │       ├ Version       : 3.10 
│     │                 │       ├ Release       : 3 
│     │                 │       ├ Epoch         : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : diffutils 
│     │                 │       ├ SrcVersion    : 3.10 
│     │                 │       ├ SrcRelease    : 3 
│     │                 │       ├ SrcEpoch      : 1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-3.0-or-later 
│     │                 │       │                ├ [1] : FSFULLR 
│     │                 │       │                ├ [2] : LGPL-2.1-or-later 
│     │                 │       │                ├ [3] : GPL-3.0-with-autoconf-exception+ 
│     │                 │       │                ├ [4] : GPL-3.0-only 
│     │                 │       │                ├ [5] : GPL-3+ with texinfo exception 
│     │                 │       │                ├ [6] : LGPL-2.0-or-later 
│     │                 │       │                ├ [7] : GPL-2.0-or-later 
│     │                 │       │                ├ [8] : X11 
│     │                 │       │                ├ [9] : FSFAP 
│     │                 │       │                ├ [10]: GFDL-1.3-no-invariants-only 
│     │                 │       │                ├ [11]: LGPL-3.0-or-later 
│     │                 │       │                ├ [12]: LGPL-3.0-only 
│     │                 │       │                ├ [13]: public-domain 
│     │                 │       │                ├ [14]: LGPL-2.0-only 
│     │                 │       │                ├ [15]: LGPL-2.1-only 
│     │                 │       │                ├ [16]: GPL-2.0-only 
│     │                 │       │                ╰ [17]: GFDL-1.3-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:6e3f486cdbe3f9ca680618b5da7d9281b56b15646192a9c46131e1
│     │                 │       │                 a0ca8221d6 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/cmp 
│     │                 │                        ├ [1] : /usr/bin/diff 
│     │                 │                        ├ [2] : /usr/bin/diff3 
│     │                 │                        ├ [3] : /usr/bin/sdiff 
│     │                 │                        ├ [4] : /usr/share/doc/diffutils/NEWS.gz 
│     │                 │                        ├ [5] : /usr/share/doc/diffutils/changelog.Debian.gz 
│     │                 │                        ├ [6] : /usr/share/doc/diffutils/copyright 
│     │                 │                        ├ [7] : /usr/share/info/diffutils.info.gz 
│     │                 │                        ├ [8] : /usr/share/man/man1/cmp.1.gz 
│     │                 │                        ├ [9] : /usr/share/man/man1/diff.1.gz 
│     │                 │                        ├ [10]: /usr/share/man/man1/diff3.1.gz 
│     │                 │                        ╰ [11]: /usr/share/man/man1/sdiff.1.gz 
│     │                 ├ [13]  ╭ ID            : dpkg@1.22.18ubuntu2.2 
│     │                 │       ├ Name          : dpkg 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/dpkg@1.22.18ubuntu2.2?arch=amd64&distro
│     │                 │       │                │       =ubuntu-25.04 
│     │                 │       │                ╰ UID : 38342884803015be 
│     │                 │       ├ Version       : 1.22.18ubuntu2.2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : dpkg 
│     │                 │       ├ SrcVersion    : 1.22.18ubuntu2.2 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: public-domain-s-s-d 
│     │                 │       │                ╰ [2]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: tar@1.35+dfsg-3.1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/bin/dpkg 
│     │                 │                        ├ [1]  : /usr/bin/dpkg-deb 
│     │                 │                        ├ [2]  : /usr/bin/dpkg-divert 
│     │                 │                        ├ [3]  : /usr/bin/dpkg-maintscript-helper 
│     │                 │                        ├ [4]  : /usr/bin/dpkg-query 
│     │                 │                        ├ [5]  : /usr/bin/dpkg-realpath 
│     │                 │                        ├ [6]  : /usr/bin/dpkg-split 
│     │                 │                        ├ [7]  : /usr/bin/dpkg-statoverride 
│     │                 │                        ├ [8]  : /usr/bin/dpkg-trigger 
│     │                 │                        ├ [9]  : /usr/bin/update-alternatives 
│     │                 │                        ├ [10] : /usr/lib/systemd/system/dpkg-db-backup.service 
│     │                 │                        ├ [11] : /usr/lib/systemd/system/dpkg-db-backup.timer 
│     │                 │                        ├ [12] : /usr/libexec/dpkg/dpkg-db-backup 
│     │                 │                        ├ [13] : /usr/libexec/dpkg/dpkg-db-keeper 
│     │                 │                        ├ [14] : /usr/sbin/start-stop-daemon 
│     │                 │                        ├ [15] : /usr/share/doc/dpkg/AUTHORS 
│     │                 │                        ├ [16] : /usr/share/doc/dpkg/README.api 
│     │                 │                        ├ [17] : /usr/share/doc/dpkg/README.bug-usertags.gz 
│     │                 │                        ├ [18] : /usr/share/doc/dpkg/README.feature-removal-schedule.gz 
│     │                 │                        ├ [19] : /usr/share/doc/dpkg/THANKS.gz 
│     │                 │                        ├ [20] : /usr/share/doc/dpkg/changelog.gz 
│     │                 │                        ├ [21] : /usr/share/doc/dpkg/copyright 
│     │                 │                        ├ [22] : /usr/share/dpkg/abitable 
│     │                 │                        ├ [23] : /usr/share/dpkg/cputable 
│     │                 │                        ├ [24] : /usr/share/dpkg/ostable 
│     │                 │                        ├ [25] : /usr/share/dpkg/sh/dpkg-error.sh 
│     │                 │                        ├ [26] : /usr/share/dpkg/tupletable 
│     │                 │                        ├ [27] : /usr/share/lintian/overrides/dpkg 
│     │                 │                        ├ [28] : /usr/share/lintian/profiles/dpkg/main.profile 
│     │                 │                        ├ [29] : /usr/share/locale/ast/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [30] : /usr/share/locale/bs/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [31] : /usr/share/locale/ca/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [32] : /usr/share/locale/cs/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [33] : /usr/share/locale/da/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [34] : /usr/share/locale/de/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [35] : /usr/share/locale/dz/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [36] : /usr/share/locale/el/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [37] : /usr/share/locale/eo/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [38] : /usr/share/locale/es/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [39] : /usr/share/locale/et/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [40] : /usr/share/locale/eu/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [41] : /usr/share/locale/fr/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [42] : /usr/share/locale/gl/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [43] : /usr/share/locale/hu/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [44] : /usr/share/locale/id/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [45] : /usr/share/locale/it/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [46] : /usr/share/locale/ja/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [47] : /usr/share/locale/km/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [48] : /usr/share/locale/ko/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [49] : /usr/share/locale/ku/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [50] : /usr/share/locale/lt/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [51] : /usr/share/locale/mr/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [52] : /usr/share/locale/nb/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [53] : /usr/share/locale/ne/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [54] : /usr/share/locale/nl/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [55] : /usr/share/locale/nn/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [56] : /usr/share/locale/oc/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [57] : /usr/share/locale/pa/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [58] : /usr/share/locale/pl/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [59] : /usr/share/locale/pt/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [60] : /usr/share/locale/pt_BR/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [61] : /usr/share/locale/ro/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [62] : /usr/share/locale/ru/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [63] : /usr/share/locale/sk/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [64] : /usr/share/locale/sv/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [65] : /usr/share/locale/th/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [66] : /usr/share/locale/tl/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [67] : /usr/share/locale/tr/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [68] : /usr/share/locale/vi/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [69] : /usr/share/locale/zh_CN/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [70] : /usr/share/locale/zh_TW/LC_MESSAGES/dpkg.mo 
│     │                 │                        ├ [71] : /usr/share/man/de/man1/dpkg-deb.1.gz 
│     │                 │                        ├ [72] : /usr/share/man/de/man1/dpkg-divert.1.gz 
│     │                 │                        ├ [73] : /usr/share/man/de/man1/dpkg-maintscript-helper.1.gz 
│     │                 │                        ├ [74] : /usr/share/man/de/man1/dpkg-query.1.gz 
│     │                 │                        ├ [75] : /usr/share/man/de/man1/dpkg-realpath.1.gz 
│     │                 │                        ├ [76] : /usr/share/man/de/man1/dpkg-split.1.gz 
│     │                 │                        ├ [77] : /usr/share/man/de/man1/dpkg-statoverride.1.gz 
│     │                 │                        ├ [78] : /usr/share/man/de/man1/dpkg-trigger.1.gz 
│     │                 │                        ├ [79] : /usr/share/man/de/man1/dpkg.1.gz 
│     │                 │                        ├ [80] : /usr/share/man/de/man1/update-alternatives.1.gz 
│     │                 │                        ├ [81] : /usr/share/man/de/man5/dpkg.cfg.5.gz 
│     │                 │                        ├ [82] : /usr/share/man/de/man8/start-stop-daemon.8.gz 
│     │                 │                        ├ [83] : /usr/share/man/es/man5/dpkg.cfg.5.gz 
│     │                 │                        ├ [84] : /usr/share/man/fr/man1/dpkg-divert.1.gz 
│     │                 │                        ├ [85] : /usr/share/man/fr/man1/dpkg-maintscript-helper.1.gz 
│     │                 │                        ├ [86] : /usr/share/man/fr/man1/dpkg-query.1.gz 
│     │                 │                        ├ [87] : /usr/share/man/fr/man1/dpkg-realpath.1.gz 
│     │                 │                        ├ [88] : /usr/share/man/fr/man1/dpkg-split.1.gz 
│     │                 │                        ├ [89] : /usr/share/man/fr/man1/dpkg-trigger.1.gz 
│     │                 │                        ├ [90] : /usr/share/man/fr/man1/update-alternatives.1.gz 
│     │                 │                        ├ [91] : /usr/share/man/fr/man5/dpkg.cfg.5.gz 
│     │                 │                        ├ [92] : /usr/share/man/fr/man8/start-stop-daemon.8.gz 
│     │                 │                        ├ [93] : /usr/share/man/it/man5/dpkg.cfg.5.gz 
│     │                 │                        ├ [94] : /usr/share/man/ja/man5/dpkg.cfg.5.gz 
│     │                 │                        ├ [95] : /usr/share/man/man1/dpkg-deb.1.gz 
│     │                 │                        ├ [96] : /usr/share/man/man1/dpkg-divert.1.gz 
│     │                 │                        ├ [97] : /usr/share/man/man1/dpkg-maintscript-helper.1.gz 
│     │                 │                        ├ [98] : /usr/share/man/man1/dpkg-query.1.gz 
│     │                 │                        ├ [99] : /usr/share/man/man1/dpkg-realpath.1.gz 
│     │                 │                        ├ [100]: /usr/share/man/man1/dpkg-split.1.gz 
│     │                 │                        ├ [101]: /usr/share/man/man1/dpkg-statoverride.1.gz 
│     │                 │                        ├ [102]: /usr/share/man/man1/dpkg-trigger.1.gz 
│     │                 │                        ├ [103]: /usr/share/man/man1/dpkg.1.gz 
│     │                 │                        ├ [104]: /usr/share/man/man1/update-alternatives.1.gz 
│     │                 │                        ├ [105]: /usr/share/man/man5/dpkg.cfg.5.gz 
│     │                 │                        ├ [106]: /usr/share/man/man8/start-stop-daemon.8.gz 
│     │                 │                        ├ [107]: /usr/share/man/nl/man1/dpkg-deb.1.gz 
│     │                 │                        ├ [108]: /usr/share/man/nl/man1/dpkg-divert.1.gz 
│     │                 │                        ├ [109]: /usr/share/man/nl/man1/dpkg-maintscript-helper.1.gz 
│     │                 │                        ├ [110]: /usr/share/man/nl/man1/dpkg-query.1.gz 
│     │                 │                        ├ [111]: /usr/share/man/nl/man1/dpkg-realpath.1.gz 
│     │                 │                        ├ [112]: /usr/share/man/nl/man1/dpkg-split.1.gz 
│     │                 │                        ├ [113]: /usr/share/man/nl/man1/dpkg-statoverride.1.gz 
│     │                 │                        ├ [114]: /usr/share/man/nl/man1/dpkg-trigger.1.gz 
│     │                 │                        ├ [115]: /usr/share/man/nl/man1/dpkg.1.gz 
│     │                 │                        ├ [116]: /usr/share/man/nl/man1/update-alternatives.1.gz 
│     │                 │                        ├ [117]: /usr/share/man/nl/man5/dpkg.cfg.5.gz 
│     │                 │                        ├ [118]: /usr/share/man/nl/man8/start-stop-daemon.8.gz 
│     │                 │                        ├ [119]: /usr/share/man/pl/man5/dpkg.cfg.5.gz 
│     │                 │                        ├ [120]: /usr/share/man/pt/man1/dpkg-deb.1.gz 
│     │                 │                        ├ [121]: /usr/share/man/pt/man1/dpkg-divert.1.gz 
│     │                 │                        ├ [122]: /usr/share/man/pt/man1/dpkg-maintscript-helper.1.gz 
│     │                 │                        ├ [123]: /usr/share/man/pt/man1/dpkg-query.1.gz 
│     │                 │                        ├ [124]: /usr/share/man/pt/man1/dpkg-realpath.1.gz 
│     │                 │                        ├ [125]: /usr/share/man/pt/man1/dpkg-split.1.gz 
│     │                 │                        ├ [126]: /usr/share/man/pt/man1/dpkg-statoverride.1.gz 
│     │                 │                        ├ [127]: /usr/share/man/pt/man1/dpkg-trigger.1.gz 
│     │                 │                        ├ [128]: /usr/share/man/pt/man1/dpkg.1.gz 
│     │                 │                        ├ [129]: /usr/share/man/pt/man1/update-alternatives.1.gz 
│     │                 │                        ├ [130]: /usr/share/man/pt/man5/dpkg.cfg.5.gz 
│     │                 │                        ├ [131]: /usr/share/man/pt/man8/start-stop-daemon.8.gz 
│     │                 │                        ├ [132]: /usr/share/man/sv/man1/dpkg-deb.1.gz 
│     │                 │                        ├ [133]: /usr/share/man/sv/man1/dpkg-divert.1.gz 
│     │                 │                        ├ [134]: /usr/share/man/sv/man1/dpkg-maintscript-helper.1.gz 
│     │                 │                        ├ [135]: /usr/share/man/sv/man1/dpkg-query.1.gz 
│     │                 │                        ├ [136]: /usr/share/man/sv/man1/dpkg-realpath.1.gz 
│     │                 │                        ├ [137]: /usr/share/man/sv/man1/dpkg-split.1.gz 
│     │                 │                        ├ [138]: /usr/share/man/sv/man1/dpkg-statoverride.1.gz 
│     │                 │                        ├ [139]: /usr/share/man/sv/man1/dpkg-trigger.1.gz 
│     │                 │                        ├ [140]: /usr/share/man/sv/man1/dpkg.1.gz 
│     │                 │                        ├ [141]: /usr/share/man/sv/man1/update-alternatives.1.gz 
│     │                 │                        ├ [142]: /usr/share/man/sv/man5/dpkg.cfg.5.gz 
│     │                 │                        ├ [143]: /usr/share/man/sv/man8/start-stop-daemon.8.gz 
│     │                 │                        ╰ [144]: /usr/share/polkit-1/actions/org.dpkg.pkexec.update-al
│     │                 │                                 ternatives.policy 
│     │                 ├ [14]  ╭ ID            : e2fsprogs@1.47.2-1ubuntu1 
│     │                 │       ├ Name          : e2fsprogs 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/e2fsprogs@1.47.2-1ubuntu1?arch=amd64&di
│     │                 │       │                │       stro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 225d194153a1ce34 
│     │                 │       ├ Version       : 1.47.2 
│     │                 │       ├ Release       : 1ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : e2fsprogs 
│     │                 │       ├ SrcVersion    : 1.47.2 
│     │                 │       ├ SrcRelease    : 1ubuntu1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-only 
│     │                 │       │                ├ [1] : GPL-2.0-or-later 
│     │                 │       │                ├ [2] : 0BSD 
│     │                 │       │                ├ [3] : MIT 
│     │                 │       │                ├ [4] : BSD-3-Clause-Variant 
│     │                 │       │                ├ [5] : BSD-3-Clause 
│     │                 │       │                ├ [6] : BSD-4-Clause-CMU 
│     │                 │       │                ├ [7] : LGPL-2.0-only 
│     │                 │       │                ├ [8] : Apache-2.0 
│     │                 │       │                ├ [9] : ISC 
│     │                 │       │                ├ [10]: MIT-US-export 
│     │                 │       │                ├ [11]: Kazlib 
│     │                 │       │                ├ [12]: Latex2e 
│     │                 │       │                ╰ [13]: GPL-2+ with Texinfo exception 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: logsave@1.47.2-1ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:f600e9d0353746ae026c2af16c5179c8cec5a1d914cc1ebb53a6c0
│     │                 │       │                 67dd2d89da 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/chattr 
│     │                 │                        ├ [1] : /usr/bin/lsattr 
│     │                 │                        ├ [2] : /usr/lib/systemd/system/e2scrub@.service 
│     │                 │                        ├ [3] : /usr/lib/systemd/system/e2scrub_all.service 
│     │                 │                        ├ [4] : /usr/lib/systemd/system/e2scrub_all.timer 
│     │                 │                        ├ [5] : /usr/lib/systemd/system/e2scrub_fail@.service 
│     │                 │                        ├ [6] : /usr/lib/systemd/system/e2scrub_reap.service 
│     │                 │                        ├ [7] : /usr/lib/udev/rules.d/64-ext4.rules 
│     │                 │                        ├ [8] : /usr/lib/udev/rules.d/96-e2scrub.rules 
│     │                 │                        ├ [9] : /usr/libexec/e2fsprogs/e2scrub_all_cron 
│     │                 │                        ├ [10]: /usr/libexec/e2fsprogs/e2scrub_fail 
│     │                 │                        ├ [11]: /usr/sbin/badblocks 
│     │                 │                        ├ [12]: /usr/sbin/debugfs 
│     │                 │                        ├ [13]: /usr/sbin/dumpe2fs 
│     │                 │                        ├ [14]: /usr/sbin/e2freefrag 
│     │                 │                        ├ [15]: /usr/sbin/e2fsck 
│     │                 │                        ├ [16]: /usr/sbin/e2image 
│     │                 │                        ├ [17]: /usr/sbin/e2scrub 
│     │                 │                        ├ [18]: /usr/sbin/e2scrub_all 
│     │                 │                        ├ [19]: /usr/sbin/e2undo 
│     │                 │                        ├ [20]: /usr/sbin/e4crypt 
│     │                 │                        ├ [21]: /usr/sbin/e4defrag 
│     │                 │                        ├ [22]: /usr/sbin/filefrag 
│     │                 │                        ├ [23]: /usr/sbin/mke2fs 
│     │                 │                        ├ [24]: /usr/sbin/mklost+found 
│     │                 │                        ├ [25]: /usr/sbin/resize2fs 
│     │                 │                        ├ [26]: /usr/sbin/tune2fs 
│     │                 │                        ├ [27]: /usr/share/doc/e2fsprogs/NEWS.gz 
│     │                 │                        ├ [28]: /usr/share/doc/e2fsprogs/README 
│     │                 │                        ├ [29]: /usr/share/doc/e2fsprogs/copyright 
│     │                 │                        ├ [30]: /usr/share/man/man1/chattr.1.gz 
│     │                 │                        ├ [31]: /usr/share/man/man1/lsattr.1.gz 
│     │                 │                        ├ [32]: /usr/share/man/man5/e2fsck.conf.5.gz 
│     │                 │                        ├ [33]: /usr/share/man/man5/ext4.5.gz 
│     │                 │                        ├ [34]: /usr/share/man/man5/mke2fs.conf.5.gz 
│     │                 │                        ├ [35]: /usr/share/man/man8/badblocks.8.gz 
│     │                 │                        ├ [36]: /usr/share/man/man8/debugfs.8.gz 
│     │                 │                        ├ [37]: /usr/share/man/man8/dumpe2fs.8.gz 
│     │                 │                        ├ [38]: /usr/share/man/man8/e2freefrag.8.gz 
│     │                 │                        ├ [39]: /usr/share/man/man8/e2fsck.8.gz 
│     │                 │                        ├ [40]: /usr/share/man/man8/e2image.8.gz 
│     │                 │                        ├ [41]: /usr/share/man/man8/e2label.8.gz 
│     │                 │                        ├ [42]: /usr/share/man/man8/e2mmpstatus.8.gz 
│     │                 │                        ├ [43]: /usr/share/man/man8/e2scrub.8.gz 
│     │                 │                        ├ [44]: /usr/share/man/man8/e2scrub_all.8.gz 
│     │                 │                        ├ [45]: /usr/share/man/man8/e2undo.8.gz 
│     │                 │                        ├ [46]: /usr/share/man/man8/e4crypt.8.gz 
│     │                 │                        ├ [47]: /usr/share/man/man8/e4defrag.8.gz 
│     │                 │                        ├ [48]: /usr/share/man/man8/filefrag.8.gz 
│     │                 │                        ├ [49]: /usr/share/man/man8/mke2fs.8.gz 
│     │                 │                        ├ [50]: /usr/share/man/man8/mklost+found.8.gz 
│     │                 │                        ├ [51]: /usr/share/man/man8/resize2fs.8.gz 
│     │                 │                        ╰ [52]: /usr/share/man/man8/tune2fs.8.gz 
│     │                 ├ [15]  ╭ ID            : findutils@4.10.0-3 
│     │                 │       ├ Name          : findutils 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/findutils@4.10.0-3?arch=amd64&distro=ub
│     │                 │       │                │       untu-25.04 
│     │                 │       │                ╰ UID : dad1a0f4676cd7cb 
│     │                 │       ├ Version       : 4.10.0 
│     │                 │       ├ Release       : 3 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : findutils 
│     │                 │       ├ SrcVersion    : 4.10.0 
│     │                 │       ├ SrcRelease    : 3 
│     │                 │       ├ Licenses       ╭ [0] : GFDL-1.3-no-invariants-or-later 
│     │                 │       │                ├ [1] : GPL-3.0-or-later 
│     │                 │       │                ├ [2] : FSFAP 
│     │                 │       │                ├ [3] : GPL-2+ with Autoconf-data exception 
│     │                 │       │                ├ [4] : GPL-3+ with Autoconf-data exception 
│     │                 │       │                ├ [5] : FSFULLR 
│     │                 │       │                ├ [6] : GPL-2.0-or-later 
│     │                 │       │                ├ [7] : X11 
│     │                 │       │                ├ [8] : public-domain 
│     │                 │       │                ├ [9] : LGPL-2.1-or-later 
│     │                 │       │                ├ [10]: GPL with automake exception 
│     │                 │       │                ├ [11]: LGPL-2.0-or-later 
│     │                 │       │                ├ [12]: LGPL-3.0-or-later 
│     │                 │       │                ├ [13]: BSD-3-Clause 
│     │                 │       │                ├ [14]: GPL-3+ with Bison-2.2 exception 
│     │                 │       │                ├ [15]: LGPL-3.0-only 
│     │                 │       │                ├ [16]: ISC 
│     │                 │       │                ├ [17]: GFDL-1.3-only 
│     │                 │       │                ├ [18]: GPL-2.0-only 
│     │                 │       │                ├ [19]: GPL-3.0-only 
│     │                 │       │                ├ [20]: LGPL-2.0-only 
│     │                 │       │                ╰ [21]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:8320e9e1c753d346e3c6ecfd99c1847f0a5c04b42403bb1d6d6b76
│     │                 │       │                 9876cfe66d 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/find 
│     │                 │                        ├ [1] : /usr/bin/xargs 
│     │                 │                        ├ [2] : /usr/share/doc-base/findutils.findutils 
│     │                 │                        ├ [3] : /usr/share/doc/findutils/NEWS.gz 
│     │                 │                        ├ [4] : /usr/share/doc/findutils/README.gz 
│     │                 │                        ├ [5] : /usr/share/doc/findutils/TODO 
│     │                 │                        ├ [6] : /usr/share/doc/findutils/changelog.Debian.gz 
│     │                 │                        ├ [7] : /usr/share/doc/findutils/copyright 
│     │                 │                        ├ [8] : /usr/share/info/find-maint.info.gz 
│     │                 │                        ├ [9] : /usr/share/info/find.info.gz 
│     │                 │                        ├ [10]: /usr/share/man/man1/find.1.gz 
│     │                 │                        ╰ [11]: /usr/share/man/man1/xargs.1.gz 
│     │                 ├ [16]  ╭ ID            : gcc-14-base@14.2.0-19ubuntu2 
│     │                 │       ├ Name          : gcc-14-base 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/gcc-14-base@14.2.0-19ubuntu2?arch=amd64
│     │                 │       │                │       &distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 8b4fc42b3cdf05e9 
│     │                 │       ├ Version       : 14.2.0 
│     │                 │       ├ Release       : 19ubuntu2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : gcc-14 
│     │                 │       ├ SrcVersion    : 14.2.0 
│     │                 │       ├ SrcRelease    : 19ubuntu2 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: GPL-3.0-only 
│     │                 │       │                ├ [2]: GFDL-1.2-only 
│     │                 │       │                ├ [3]: Artistic-2.0 
│     │                 │       │                ╰ [4]: LGPL-2.0-or-later 
│     │                 │       ├ Maintainer    : Ubuntu Core developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:10cf0140d976709d9cee0a48614245766bc3088ee8a8f523900cb2
│     │                 │       │                 ae4ef9a8cb 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/share/doc/gcc-14-base/README.Debian.amd64.gz 
│     │                 │                        ├ [1]: /usr/share/doc/gcc-14-base/TODO.Debian 
│     │                 │                        ├ [2]: /usr/share/doc/gcc-14-base/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/gcc-14-base/copyright 
│     │                 ├ [17]  ╭ ID            : gcc-15-base@15-20250404-0ubuntu1 
│     │                 │       ├ Name          : gcc-15-base 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/gcc-15-base@15-20250404-0ubuntu1?arch=a
│     │                 │       │                │       md64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : bdca96afe6e514c1 
│     │                 │       ├ Version       : 15-20250404 
│     │                 │       ├ Release       : 0ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : gcc-15 
│     │                 │       ├ SrcVersion    : 15-20250404 
│     │                 │       ├ SrcRelease    : 0ubuntu1 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: GPL-3.0-only 
│     │                 │       │                ├ [2]: GFDL-1.2-only 
│     │                 │       │                ├ [3]: Artistic-2.0 
│     │                 │       │                ╰ [4]: LGPL-2.0-or-later 
│     │                 │       ├ Maintainer    : Ubuntu Core developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:5bad638f6288ab3fee0c7d11f37d47946c7b0d806dae257aeea968
│     │                 │       │                 e2507deb1d 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/share/doc/gcc-15-base/README.Debian.amd64.gz 
│     │                 │                        ├ [1]: /usr/share/doc/gcc-15-base/TODO.Debian 
│     │                 │                        ├ [2]: /usr/share/doc/gcc-15-base/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/gcc-15-base/copyright 
│     │                 ├ [18]  ╭ ID            : gpgv@2.4.4-2ubuntu23.1 
│     │                 │       ├ Name          : gpgv 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/gpgv@2.4.4-2ubuntu23.1?arch=amd64&distr
│     │                 │       │                │       o=ubuntu-25.04 
│     │                 │       │                ╰ UID : d2a702b753c09f0f 
│     │                 │       ├ Version       : 2.4.4 
│     │                 │       ├ Release       : 2ubuntu23.1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : gnupg2 
│     │                 │       ├ SrcVersion    : 2.4.4 
│     │                 │       ├ SrcRelease    : 2ubuntu23.1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-3.0-or-later 
│     │                 │       │                ├ [1] : permissive 
│     │                 │       │                ├ [2] : LGPL-2.1-or-later 
│     │                 │       │                ├ [3] : LGPL-3.0-or-later 
│     │                 │       │                ├ [4] : GPL-2.0-or-later 
│     │                 │       │                ├ [5] : MIT 
│     │                 │       │                ├ [6] : BSD-3-Clause 
│     │                 │       │                ├ [7] : RFC-Reference 
│     │                 │       │                ├ [8] : TinySCHEME 
│     │                 │       │                ├ [9] : CC0-1.0 
│     │                 │       │                ├ [10]: GPL-3.0-only 
│     │                 │       │                ├ [11]: LGPL-3.0-only 
│     │                 │       │                ├ [12]: LGPL-2.1-only 
│     │                 │       │                ╰ [13]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libassuan9@3.0.2-2 
│     │                 │       │                ├ [1]: libbz2-1.0@1.0.8-6 
│     │                 │       │                ├ [2]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [3]: libgcrypt20@1.11.0-6ubuntu1 
│     │                 │       │                ├ [4]: libgpg-error0@1.51-3 
│     │                 │       │                ├ [5]: libnpth0t64@1.8-2 
│     │                 │       │                ╰ [6]: zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/bin/gpgv 
│     │                 │                        ├ [1]: /usr/share/doc/gpgv/NEWS.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/gpgv/changelog.Debian.gz 
│     │                 │                        ├ [3]: /usr/share/doc/gpgv/copyright 
│     │                 │                        ╰ [4]: /usr/share/man/man1/gpgv.1.gz 
│     │                 ├ [19]  ╭ ID            : grep@3.11-4build1 
│     │                 │       ├ Name          : grep 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/grep@3.11-4build1?arch=amd64&distro=ubu
│     │                 │       │                │       ntu-25.04 
│     │                 │       │                ╰ UID : 52f654ece808dae2 
│     │                 │       ├ Version       : 3.11 
│     │                 │       ├ Release       : 4build1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : grep 
│     │                 │       ├ SrcVersion    : 3.11 
│     │                 │       ├ SrcRelease    : 4build1 
│     │                 │       ├ Licenses       ╭ [0]: GPL-3.0-or-later 
│     │                 │       │                ╰ [1]: GPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:fc0fdc5983ea3d3579ccf335e51dec69684a0dd9bb915734999c57
│     │                 │       │                 33add9507a 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/egrep 
│     │                 │                        ├ [1] : /usr/bin/fgrep 
│     │                 │                        ├ [2] : /usr/bin/grep 
│     │                 │                        ├ [3] : /usr/bin/rgrep 
│     │                 │                        ├ [4] : /usr/share/doc/grep/AUTHORS 
│     │                 │                        ├ [5] : /usr/share/doc/grep/NEWS.Debian.gz 
│     │                 │                        ├ [6] : /usr/share/doc/grep/NEWS.gz 
│     │                 │                        ├ [7] : /usr/share/doc/grep/README 
│     │                 │                        ├ [8] : /usr/share/doc/grep/THANKS.gz 
│     │                 │                        ├ [9] : /usr/share/doc/grep/TODO.gz 
│     │                 │                        ├ [10]: /usr/share/doc/grep/changelog.Debian.gz 
│     │                 │                        ├ [11]: /usr/share/doc/grep/copyright 
│     │                 │                        ├ [12]: /usr/share/info/grep.info.gz 
│     │                 │                        ╰ [13]: /usr/share/man/man1/grep.1.gz 
│     │                 ├ [20]  ╭ ID            : gzip@1.13-1ubuntu3 
│     │                 │       ├ Name          : gzip 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/gzip@1.13-1ubuntu3?arch=amd64&distro=ub
│     │                 │       │                │       untu-25.04 
│     │                 │       │                ╰ UID : 42579ec8652fd92c 
│     │                 │       ├ Version       : 1.13 
│     │                 │       ├ Release       : 1ubuntu3 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : gzip 
│     │                 │       ├ SrcVersion    : 1.13 
│     │                 │       ├ SrcRelease    : 1ubuntu3 
│     │                 │       ├ Licenses       ╭ [0]: GPL-3.0-or-later 
│     │                 │       │                ├ [1]: GFDL-1.3+-no-invariant 
│     │                 │       │                ├ [2]: FSF-manpages 
│     │                 │       │                ├ [3]: GPL-3.0-only 
│     │                 │       │                ╰ [4]: GFDL-3 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:acaeab19e4cbb8081e18f8f40228ec5ab3831fd8c25b81624c7011
│     │                 │       │                 6ddbc9e89e 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/gunzip 
│     │                 │                        ├ [1] : /usr/bin/gzexe 
│     │                 │                        ├ [2] : /usr/bin/gzip 
│     │                 │                        ├ [3] : /usr/bin/zcat 
│     │                 │                        ├ [4] : /usr/bin/zcmp 
│     │                 │                        ├ [5] : /usr/bin/zdiff 
│     │                 │                        ├ [6] : /usr/bin/zegrep 
│     │                 │                        ├ [7] : /usr/bin/zfgrep 
│     │                 │                        ├ [8] : /usr/bin/zforce 
│     │                 │                        ├ [9] : /usr/bin/zgrep 
│     │                 │                        ├ [10]: /usr/bin/zless 
│     │                 │                        ├ [11]: /usr/bin/zmore 
│     │                 │                        ├ [12]: /usr/bin/znew 
│     │                 │                        ├ [13]: /usr/share/doc/gzip/NEWS.gz 
│     │                 │                        ├ [14]: /usr/share/doc/gzip/README.gz 
│     │                 │                        ├ [15]: /usr/share/doc/gzip/TODO 
│     │                 │                        ├ [16]: /usr/share/doc/gzip/changelog.Debian.gz 
│     │                 │                        ├ [17]: /usr/share/doc/gzip/copyright 
│     │                 │                        ├ [18]: /usr/share/info/gzip.info.gz 
│     │                 │                        ├ [19]: /usr/share/man/man1/gzexe.1.gz 
│     │                 │                        ├ [20]: /usr/share/man/man1/gzip.1.gz 
│     │                 │                        ├ [21]: /usr/share/man/man1/zdiff.1.gz 
│     │                 │                        ├ [22]: /usr/share/man/man1/zforce.1.gz 
│     │                 │                        ├ [23]: /usr/share/man/man1/zgrep.1.gz 
│     │                 │                        ├ [24]: /usr/share/man/man1/zless.1.gz 
│     │                 │                        ├ [25]: /usr/share/man/man1/zmore.1.gz 
│     │                 │                        ╰ [26]: /usr/share/man/man1/znew.1.gz 
│     │                 ├ [21]  ╭ ID            : hostname@3.25 
│     │                 │       ├ Name          : hostname 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/hostname@3.25?arch=amd64&distro=ubuntu-
│     │                 │       │                │       25.04 
│     │                 │       │                ╰ UID : b9dae67c3872a8e8 
│     │                 │       ├ Version       : 3.25 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : hostname 
│     │                 │       ├ SrcVersion    : 3.25 
│     │                 │       ├ Licenses       ─ [0]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:41e8679f87db3937458d27e3d1c892e59e440ad636eb2298cf322f
│     │                 │       │                 8be6f3e3e3 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/bin/hostname 
│     │                 │                        ├ [1]: /usr/share/doc/hostname/changelog.gz 
│     │                 │                        ├ [2]: /usr/share/doc/hostname/copyright 
│     │                 │                        ╰ [3]: /usr/share/man/man1/hostname.1.gz 
│     │                 ├ [22]  ╭ ID            : init-system-helpers@1.68 
│     │                 │       ├ Name          : init-system-helpers 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/init-system-helpers@1.68?arch=all&distr
│     │                 │       │                │       o=ubuntu-25.04 
│     │                 │       │                ╰ UID : 7d8e14fcf1360392 
│     │                 │       ├ Version       : 1.68 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : init-system-helpers 
│     │                 │       ├ SrcVersion    : 1.68 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ├ [1]: GPL-2.0-or-later 
│     │                 │       │                ╰ [2]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:24a27aafc1e036fc26c053b9785807003203360e2734ac94dac5b5
│     │                 │       │                 2b447f84f0 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/deb-systemd-helper 
│     │                 │                        ├ [1] : /usr/bin/deb-systemd-invoke 
│     │                 │                        ├ [2] : /usr/sbin/invoke-rc.d 
│     │                 │                        ├ [3] : /usr/sbin/service 
│     │                 │                        ├ [4] : /usr/sbin/update-rc.d 
│     │                 │                        ├ [5] : /usr/share/bug/init-system-helpers/control 
│     │                 │                        ├ [6] : /usr/share/doc/init-system-helpers/README.invoke-rc.d.gz 
│     │                 │                        ├ [7] : /usr/share/doc/init-system-helpers/README.policy-rc.d.gz 
│     │                 │                        ├ [8] : /usr/share/doc/init-system-helpers/changelog.gz 
│     │                 │                        ├ [9] : /usr/share/doc/init-system-helpers/copyright 
│     │                 │                        ├ [10]: /usr/share/man/man1/deb-systemd-helper.1p.gz 
│     │                 │                        ├ [11]: /usr/share/man/man1/deb-systemd-invoke.1p.gz 
│     │                 │                        ├ [12]: /usr/share/man/man8/invoke-rc.d.8.gz 
│     │                 │                        ├ [13]: /usr/share/man/man8/service.8.gz 
│     │                 │                        ╰ [14]: /usr/share/man/man8/update-rc.d.8.gz 
│     │                 ├ [23]  ╭ ID            : krb5-locales@1.21.3-4ubuntu2 
│     │                 │       ├ Name          : krb5-locales 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/krb5-locales@1.21.3-4ubuntu2?arch=all&d
│     │                 │       │                │       istro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 675c601436d4b197 
│     │                 │       ├ Version       : 1.21.3 
│     │                 │       ├ Release       : 4ubuntu2 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : krb5 
│     │                 │       ├ SrcVersion    : 1.21.3 
│     │                 │       ├ SrcRelease    : 4ubuntu2 
│     │                 │       ├ Licenses       ─ [0]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/share/doc/krb5-locales/changelog.Debian.gz 
│     │                 │                        ╰ [1]: /usr/share/doc/krb5-locales/copyright 
│     │                 ├ [24]  ╭ ID            : libacl1@2.3.2-2 
│     │                 │       ├ Name          : libacl1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libacl1@2.3.2-2?arch=amd64&distro=ubunt
│     │                 │       │                │       u-25.04 
│     │                 │       │                ╰ UID : 82479c1cdb2f12a6 
│     │                 │       ├ Version       : 2.3.2 
│     │                 │       ├ Release       : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : acl 
│     │                 │       ├ SrcVersion    : 2.3.2 
│     │                 │       ├ SrcRelease    : 2 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: GPL-2.0-only 
│     │                 │       │                ├ [2]: LGPL-2.0-or-later 
│     │                 │       │                ╰ [3]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:77f8d49c031182bbd6c4fe4ec9ad49edb5d4607f2dac795fc6932d
│     │                 │       │                 ce0e8f541e 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libacl.so.1.1.2302 
│     │                 │                        ├ [1]: /usr/share/doc/libacl1/changelog.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libacl1/copyright 
│     │                 │                        ╰ [3]: /usr/share/lintian/overrides/libacl1 
│     │                 ├ [25]  ╭ ID            : libapparmor1@4.1.0~beta5-0ubuntu14.2 
│     │                 │       ├ Name          : libapparmor1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libapparmor1@4.1.0~beta5-0ubuntu14.2?ar
│     │                 │       │                │       ch=amd64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 115b49df0ad9adc0 
│     │                 │       ├ Version       : 4.1.0~beta5 
│     │                 │       ├ Release       : 0ubuntu14.2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : apparmor 
│     │                 │       ├ SrcVersion    : 4.1.0~beta5 
│     │                 │       ├ SrcRelease    : 0ubuntu14.2 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: BSD-3-Clause 
│     │                 │       │                ├ [2]: LGPL-2.1-or-later 
│     │                 │       │                ├ [3]: GPL-2.0-only 
│     │                 │       │                ╰ [4]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libapparmor.so.1.24.2 
│     │                 │                        ├ [1]: /usr/share/doc/libapparmor1/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libapparmor1/copyright 
│     │                 ├ [26]  ╭ ID            : libapt-pkg7.0@3.0.0 
│     │                 │       ├ Name          : libapt-pkg7.0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libapt-pkg7.0@3.0.0?arch=amd64&distro=u
│     │                 │       │                │       buntu-25.04 
│     │                 │       │                ╰ UID : 9129130df57f4f1a 
│     │                 │       ├ Version       : 3.0.0 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : apt 
│     │                 │       ├ SrcVersion    : 3.0.0 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: curl 
│     │                 │       │                ├ [2]: BSD-3-Clause 
│     │                 │       │                ├ [3]: MIT 
│     │                 │       │                ╰ [4]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0] : libbz2-1.0@1.0.8-6 
│     │                 │       │                ├ [1] : libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [2] : libgcc-s1@15-20250404-0ubuntu1 
│     │                 │       │                ├ [3] : liblz4-1@1.10.0-4 
│     │                 │       │                ├ [4] : liblzma5@5.6.4-1ubuntu1 
│     │                 │       │                ├ [5] : libssl3t64@3.4.1-1ubuntu4 
│     │                 │       │                ├ [6] : libstdc++6@15-20250404-0ubuntu1 
│     │                 │       │                ├ [7] : libsystemd0@257.4-1ubuntu3.2 
│     │                 │       │                ├ [8] : libudev1@257.4-1ubuntu3.2 
│     │                 │       │                ├ [9] : libxxhash0@0.8.3-2 
│     │                 │       │                ├ [10]: libzstd1@1.5.6+dfsg-2 
│     │                 │       │                ╰ [11]: zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:75b36757f4777afa2a660b72c70a18335f993d119c26232018036c
│     │                 │       │                 01faecea8c 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/lib/x86_64-linux-gnu/libapt-pkg.so.7.0.0 
│     │                 │                        ├ [1] : /usr/share/doc/libapt-pkg7.0/NEWS.Debian.gz 
│     │                 │                        ├ [2] : /usr/share/doc/libapt-pkg7.0/changelog.gz 
│     │                 │                        ├ [3] : /usr/share/doc/libapt-pkg7.0/copyright 
│     │                 │                        ├ [4] : /usr/share/locale/ar/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [5] : /usr/share/locale/ast/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [6] : /usr/share/locale/bg/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [7] : /usr/share/locale/bs/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [8] : /usr/share/locale/ca/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [9] : /usr/share/locale/cs/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [10]: /usr/share/locale/cy/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [11]: /usr/share/locale/da/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [12]: /usr/share/locale/de/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [13]: /usr/share/locale/dz/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [14]: /usr/share/locale/el/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [15]: /usr/share/locale/es/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [16]: /usr/share/locale/eu/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [17]: /usr/share/locale/fi/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [18]: /usr/share/locale/fr/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [19]: /usr/share/locale/gl/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [20]: /usr/share/locale/hu/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [21]: /usr/share/locale/it/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [22]: /usr/share/locale/ja/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [23]: /usr/share/locale/km/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [24]: /usr/share/locale/ko/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [25]: /usr/share/locale/ku/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [26]: /usr/share/locale/lt/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [27]: /usr/share/locale/mr/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [28]: /usr/share/locale/nb/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [29]: /usr/share/locale/ne/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [30]: /usr/share/locale/nl/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [31]: /usr/share/locale/nn/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [32]: /usr/share/locale/pl/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [33]: /usr/share/locale/pt/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [34]: /usr/share/locale/pt_BR/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [35]: /usr/share/locale/ro/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [36]: /usr/share/locale/ru/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [37]: /usr/share/locale/sk/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [38]: /usr/share/locale/sl/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [39]: /usr/share/locale/sv/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [40]: /usr/share/locale/th/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [41]: /usr/share/locale/tl/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [42]: /usr/share/locale/tr/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [43]: /usr/share/locale/uk/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [44]: /usr/share/locale/vi/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ├ [45]: /usr/share/locale/zh_CN/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 │                        ╰ [46]: /usr/share/locale/zh_TW/LC_MESSAGES/libapt-pkg7.0.mo 
│     │                 ├ [27]  ╭ ID            : libassuan9@3.0.2-2 
│     │                 │       ├ Name          : libassuan9 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libassuan9@3.0.2-2?arch=amd64&distro=ub
│     │                 │       │                │       untu-25.04 
│     │                 │       │                ╰ UID : 419b93ca50a20e28 
│     │                 │       ├ Version       : 3.0.2 
│     │                 │       ├ Release       : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libassuan 
│     │                 │       ├ SrcVersion    : 3.0.2 
│     │                 │       ├ SrcRelease    : 2 
│     │                 │       ├ Licenses       ╭ [0] : LGPL-2.1-or-later 
│     │                 │       │                ├ [1] : FSFULLR 
│     │                 │       │                ├ [2] : FSFULLRWD 
│     │                 │       │                ├ [3] : GPL-2+ with Autoconf-data exception 
│     │                 │       │                ├ [4] : GPL-3+ with Autoconf-data exception 
│     │                 │       │                ├ [5] : X11 
│     │                 │       │                ├ [6] : GPL-2+ with Libtool exception 
│     │                 │       │                ├ [7] : GPL-3.0-or-later 
│     │                 │       │                ├ [8] : LGPL-3.0-or-later 
│     │                 │       │                ├ [9] : LGPL-2.1-only 
│     │                 │       │                ├ [10]: GPL-2.with.nonstandard.Autoconf-data.exception 
│     │                 │       │                ├ [11]: GPL-3+ with Autoconf-2.0~Archive exception 
│     │                 │       │                ├ [12]: GPL-2.0-only 
│     │                 │       │                ├ [13]: GPL-3.0-only 
│     │                 │       │                ╰ [14]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libgpg-error0@1.51-3 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:acfa524ca0e7cd2c6f38ea97e93a206e81e611429cb96ff8a2449d
│     │                 │       │                 8d01bdab11 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libassuan.so.9.0.2 
│     │                 │                        ├ [1]: /usr/share/doc/libassuan9/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libassuan9/copyright 
│     │                 ├ [28]  ╭ ID            : libattr1@1:2.5.2-3 
│     │                 │       ├ Name          : libattr1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libattr1@2.5.2-3?arch=amd64&distro=ubun
│     │                 │       │                │       tu-25.04&epoch=1 
│     │                 │       │                ╰ UID : 328c227186e85837 
│     │                 │       ├ Version       : 2.5.2 
│     │                 │       ├ Release       : 3 
│     │                 │       ├ Epoch         : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : attr 
│     │                 │       ├ SrcVersion    : 2.5.2 
│     │                 │       ├ SrcRelease    : 3 
│     │                 │       ├ SrcEpoch      : 1 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: GPL-2.0-only 
│     │                 │       │                ├ [2]: LGPL-2.0-or-later 
│     │                 │       │                ╰ [3]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:d0a08f7d6089dd2116e211cb8986f6e0979b4503c5208cc7e40a68
│     │                 │       │                 f68e1eb68e 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libattr.so.1.1.2502 
│     │                 │                        ├ [1]: /usr/share/doc/libattr1/changelog.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libattr1/copyright 
│     │                 │                        ╰ [3]: /usr/share/lintian/overrides/libattr1 
│     │                 ├ [29]  ╭ ID            : libaudit-common@1:4.0.2-2ubuntu2 
│     │                 │       ├ Name          : libaudit-common 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libaudit-common@4.0.2-2ubuntu2?arch=all
│     │                 │       │                │       &distro=ubuntu-25.04&epoch=1 
│     │                 │       │                ╰ UID : 1f712253a9ff239 
│     │                 │       ├ Version       : 4.0.2 
│     │                 │       ├ Release       : 2ubuntu2 
│     │                 │       ├ Epoch         : 1 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : audit 
│     │                 │       ├ SrcVersion    : 4.0.2 
│     │                 │       ├ SrcRelease    : 2ubuntu2 
│     │                 │       ├ SrcEpoch      : 1 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-only 
│     │                 │       │                ├ [1]: LGPL-2.1-only 
│     │                 │       │                ╰ [2]: GPL-1.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:5d34cc08269b83937b8eea64439cdba2a14a9f093ac8447bbc54eb
│     │                 │       │                 acc2b2095d 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/share/doc/libaudit-common/changelog.Debian.gz 
│     │                 │                        ├ [1]: /usr/share/doc/libaudit-common/copyright 
│     │                 │                        ╰ [2]: /usr/share/man/man5/libaudit.conf.5.gz 
│     │                 ├ [30]  ╭ ID            : libaudit1@1:4.0.2-2ubuntu2 
│     │                 │       ├ Name          : libaudit1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libaudit1@4.0.2-2ubuntu2?arch=amd64&dis
│     │                 │       │                │       tro=ubuntu-25.04&epoch=1 
│     │                 │       │                ╰ UID : ccb2c6b54f246ee6 
│     │                 │       ├ Version       : 4.0.2 
│     │                 │       ├ Release       : 2ubuntu2 
│     │                 │       ├ Epoch         : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : audit 
│     │                 │       ├ SrcVersion    : 4.0.2 
│     │                 │       ├ SrcRelease    : 2ubuntu2 
│     │                 │       ├ SrcEpoch      : 1 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-only 
│     │                 │       │                ├ [1]: LGPL-2.1-only 
│     │                 │       │                ╰ [2]: GPL-1.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libaudit-common@1:4.0.2-2ubuntu2 
│     │                 │       │                ├ [1]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [2]: libcap-ng0@0.8.5-4build1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:83ab1553a8cfacc4327dd449df1e5b893a74e6bcaf3cd52f61d01a
│     │                 │       │                 1681981f22 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libaudit.so.1.0.0 
│     │                 │                        ├ [1]: /usr/share/doc/libaudit1/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libaudit1/copyright 
│     │                 ├ [31]  ╭ ID            : libblkid1@2.40.2-14ubuntu1.1 
│     │                 │       ├ Name          : libblkid1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libblkid1@2.40.2-14ubuntu1.1?arch=amd64
│     │                 │       │                │       &distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 59cb6f3773eaeddc 
│     │                 │       ├ Version       : 2.40.2 
│     │                 │       ├ Release       : 14ubuntu1.1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : util-linux 
│     │                 │       ├ SrcVersion    : 2.40.2 
│     │                 │       ├ SrcRelease    : 14ubuntu1.1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-or-later 
│     │                 │       │                ├ [1] : GPL-2.0-only 
│     │                 │       │                ├ [2] : GPL-3.0-or-later 
│     │                 │       │                ├ [3] : LGPL-2.1-or-later 
│     │                 │       │                ├ [4] : public-domain 
│     │                 │       │                ├ [5] : BSD-4-Clause 
│     │                 │       │                ├ [6] : MIT 
│     │                 │       │                ├ [7] : ISC 
│     │                 │       │                ├ [8] : BSD-3-Clause 
│     │                 │       │                ├ [9] : BSLA 
│     │                 │       │                ├ [10]: LGPL-2.0-or-later 
│     │                 │       │                ├ [11]: BSD-2-Clause 
│     │                 │       │                ├ [12]: LGPL-3.0-or-later 
│     │                 │       │                ├ [13]: GPL-3.0-only 
│     │                 │       │                ├ [14]: LGPL-2.0-only 
│     │                 │       │                ├ [15]: LGPL-2.1-only 
│     │                 │       │                ╰ [16]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libblkid.so.1.1.0 
│     │                 │                        ├ [1]: /usr/share/doc/libblkid1/NEWS.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libblkid1/changelog.Debian.gz 
│     │                 │                        ├ [3]: /usr/share/doc/libblkid1/copyright 
│     │                 │                        ╰ [4]: /usr/share/lintian/overrides/libblkid1 
│     │                 ├ [32]  ╭ ID            : libbrotli1@1.1.0-2build4 
│     │                 │       ├ Name          : libbrotli1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libbrotli1@1.1.0-2build4?arch=amd64&dis
│     │                 │       │                │       tro=ubuntu-25.04 
│     │                 │       │                ╰ UID : e9b3a591a1fa782c 
│     │                 │       ├ Version       : 1.1.0 
│     │                 │       ├ Release       : 2build4 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : brotli 
│     │                 │       ├ SrcVersion    : 1.1.0 
│     │                 │       ├ SrcRelease    : 2build4 
│     │                 │       ├ Licenses       ─ [0]: MIT 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libbrotlicommon.so.1.1.0 
│     │                 │                        ├ [1]: /usr/lib/x86_64-linux-gnu/libbrotlidec.so.1.1.0 
│     │                 │                        ├ [2]: /usr/lib/x86_64-linux-gnu/libbrotlienc.so.1.1.0 
│     │                 │                        ├ [3]: /usr/share/doc/libbrotli1/changelog.Debian.gz 
│     │                 │                        ├ [4]: /usr/share/doc/libbrotli1/copyright 
│     │                 │                        ╰ [5]: /usr/share/lintian/overrides/libbrotli1 
│     │                 ├ [33]  ╭ ID            : libbsd0@0.12.2-2 
│     │                 │       ├ Name          : libbsd0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libbsd0@0.12.2-2?arch=amd64&distro=ubun
│     │                 │       │                │       tu-25.04 
│     │                 │       │                ╰ UID : 95df8338644dd569 
│     │                 │       ├ Version       : 0.12.2 
│     │                 │       ├ Release       : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libbsd 
│     │                 │       ├ SrcVersion    : 0.12.2 
│     │                 │       ├ SrcRelease    : 2 
│     │                 │       ├ Licenses       ╭ [0] : BSD-3-Clause 
│     │                 │       │                ├ [1] : BSD-3-clause-Regents 
│     │                 │       │                ├ [2] : BSD-2-Clause-NetBSD 
│     │                 │       │                ├ [3] : BSD-3-clause-author 
│     │                 │       │                ├ [4] : BSD-3-clause-John-Birrell 
│     │                 │       │                ├ [5] : BSD-5-clause-Peter-Wemm 
│     │                 │       │                ├ [6] : BSD-2-Clause 
│     │                 │       │                ├ [7] : BSD-2-clause-verbatim 
│     │                 │       │                ├ [8] : BSD-2-clause-author 
│     │                 │       │                ├ [9] : ISC 
│     │                 │       │                ├ [10]: ISC-Original 
│     │                 │       │                ├ [11]: MIT 
│     │                 │       │                ├ [12]: public-domain 
│     │                 │       │                ╰ [13]: Beerware 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libmd0@1.1.0-2build2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:112aff776bd8c1ef04d622aad3d1333d997efba03589b04817f77f
│     │                 │       │                 52572c4271 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libbsd.so.0.12.2 
│     │                 │                        ├ [1]: /usr/share/doc/libbsd0/changelog.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libbsd0/copyright 
│     │                 │                        ╰ [3]: /usr/share/lintian/overrides/libbsd0 
│     │                 ├ [34]  ╭ ID            : libbz2-1.0@1.0.8-6 
│     │                 │       ├ Name          : libbz2-1.0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libbz2-1.0@1.0.8-6?arch=amd64&distro=ub
│     │                 │       │                │       untu-25.04 
│     │                 │       │                ╰ UID : 5f02cdad2308808b 
│     │                 │       ├ Version       : 1.0.8 
│     │                 │       ├ Release       : 6 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : bzip2 
│     │                 │       ├ SrcVersion    : 1.0.8 
│     │                 │       ├ SrcRelease    : 6 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ╰ [1]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:53b90eb1e37e0f51f28f2b77d29f7fd418e0df7e5dd2112d19526d
│     │                 │       │                 ad2d13fff2 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libbz2.so.1.0.4 
│     │                 │                        ├ [1]: /usr/share/doc/libbz2-1.0/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libbz2-1.0/copyright 
│     │                 ├ [35]  ╭ ID            : libc-bin@2.41-6ubuntu1.2 
│     │                 │       ├ Name          : libc-bin 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libc-bin@2.41-6ubuntu1.2?arch=amd64&dis
│     │                 │       │                │       tro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 700daf2199d66f10 
│     │                 │       ├ Version       : 2.41 
│     │                 │       ├ Release       : 6ubuntu1.2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : glibc 
│     │                 │       ├ SrcVersion    : 2.41 
│     │                 │       ├ SrcRelease    : 6ubuntu1.2 
│     │                 │       ├ Licenses       ╭ [0] : LGPL-2.1-or-later 
│     │                 │       │                ├ [1] : GFDL-1.3-only 
│     │                 │       │                ├ [2] : LGPL-2.0-or-later 
│     │                 │       │                ├ [3] : LGPL-2.1+-with-link-exception 
│     │                 │       │                ├ [4] : LGPL-3.0-or-later 
│     │                 │       │                ├ [5] : GPL-2.0-or-later 
│     │                 │       │                ├ [6] : GPL-2+-with-link-exception 
│     │                 │       │                ├ [7] : GPL-2.0-only 
│     │                 │       │                ├ [8] : GPL-3.0-or-later 
│     │                 │       │                ├ [9] : FSFAP 
│     │                 │       │                ├ [10]: Carnegie 
│     │                 │       │                ├ [11]: Inner-Net 
│     │                 │       │                ├ [12]: MIT-like-Lord 
│     │                 │       │                ├ [13]: BSD-like-Spencer 
│     │                 │       │                ├ [14]: PCRE 
│     │                 │       │                ├ [15]: BSD-3-clause-Carnegie 
│     │                 │       │                ├ [16]: Unicode-DFS-2016 
│     │                 │       │                ├ [17]: BSL-1.0 
│     │                 │       │                ├ [18]: SunPro 
│     │                 │       │                ├ [19]: CORE-MATH 
│     │                 │       │                ├ [20]: BSD-3-clause-Berkeley 
│     │                 │       │                ├ [21]: BSD-3-clause-WIDE 
│     │                 │       │                ├ [22]: BSD-2-Clause 
│     │                 │       │                ├ [23]: BSD-3-clause-Oracle 
│     │                 │       │                ├ [24]: DEC 
│     │                 │       │                ├ [25]: IBM 
│     │                 │       │                ├ [26]: ISC 
│     │                 │       │                ├ [27]: Univ-Coimbra 
│     │                 │       │                ├ [28]: public-domain 
│     │                 │       │                ├ [29]: GPL-3.0-only 
│     │                 │       │                ├ [30]: LGPL-2.0-only 
│     │                 │       │                ├ [31]: LGPL-2.1-only 
│     │                 │       │                ╰ [32]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/getconf 
│     │                 │                        ├ [1] : /usr/bin/getent 
│     │                 │                        ├ [2] : /usr/bin/iconv 
│     │                 │                        ├ [3] : /usr/bin/ldd 
│     │                 │                        ├ [4] : /usr/bin/locale 
│     │                 │                        ├ [5] : /usr/bin/localedef 
│     │                 │                        ├ [6] : /usr/bin/pldd 
│     │                 │                        ├ [7] : /usr/bin/tzselect 
│     │                 │                        ├ [8] : /usr/bin/zdump 
│     │                 │                        ├ [9] : /usr/lib/locale/C.utf8/LC_ADDRESS 
│     │                 │                        ├ [10]: /usr/lib/locale/C.utf8/LC_COLLATE 
│     │                 │                        ├ [11]: /usr/lib/locale/C.utf8/LC_CTYPE 
│     │                 │                        ├ [12]: /usr/lib/locale/C.utf8/LC_IDENTIFICATION 
│     │                 │                        ├ [13]: /usr/lib/locale/C.utf8/LC_MEASUREMENT 
│     │                 │                        ├ [14]: /usr/lib/locale/C.utf8/LC_MESSAGES/SYS_LC_MESSAGES 
│     │                 │                        ├ [15]: /usr/lib/locale/C.utf8/LC_MONETARY 
│     │                 │                        ├ [16]: /usr/lib/locale/C.utf8/LC_NAME 
│     │                 │                        ├ [17]: /usr/lib/locale/C.utf8/LC_NUMERIC 
│     │                 │                        ├ [18]: /usr/lib/locale/C.utf8/LC_PAPER 
│     │                 │                        ├ [19]: /usr/lib/locale/C.utf8/LC_TELEPHONE 
│     │                 │                        ├ [20]: /usr/lib/locale/C.utf8/LC_TIME 
│     │                 │                        ├ [21]: /usr/sbin/iconvconfig 
│     │                 │                        ├ [22]: /usr/sbin/ldconfig 
│     │                 │                        ├ [23]: /usr/sbin/ldconfig.real 
│     │                 │                        ├ [24]: /usr/sbin/zic 
│     │                 │                        ├ [25]: /usr/share/doc/libc-bin/copyright 
│     │                 │                        ├ [26]: /usr/share/libc-bin/nsswitch.conf 
│     │                 │                        ├ [27]: /usr/share/lintian/overrides/libc-bin 
│     │                 │                        ├ [28]: /usr/share/man/man1/getconf.1.gz 
│     │                 │                        ╰ [29]: /usr/share/man/man1/tzselect.1.gz 
│     │                 ├ [36]  ╭ ID            : libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Name          : libc6 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libc6@2.41-6ubuntu1.2?arch=amd64&distro
│     │                 │       │                │       =ubuntu-25.04 
│     │                 │       │                ╰ UID : 8771c155c7515825 
│     │                 │       ├ Version       : 2.41 
│     │                 │       ├ Release       : 6ubuntu1.2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : glibc 
│     │                 │       ├ SrcVersion    : 2.41 
│     │                 │       ├ SrcRelease    : 6ubuntu1.2 
│     │                 │       ├ Licenses       ╭ [0] : LGPL-2.1-or-later 
│     │                 │       │                ├ [1] : GFDL-1.3-only 
│     │                 │       │                ├ [2] : LGPL-2.0-or-later 
│     │                 │       │                ├ [3] : LGPL-2.1+-with-link-exception 
│     │                 │       │                ├ [4] : LGPL-3.0-or-later 
│     │                 │       │                ├ [5] : GPL-2.0-or-later 
│     │                 │       │                ├ [6] : GPL-2+-with-link-exception 
│     │                 │       │                ├ [7] : GPL-2.0-only 
│     │                 │       │                ├ [8] : GPL-3.0-or-later 
│     │                 │       │                ├ [9] : FSFAP 
│     │                 │       │                ├ [10]: Carnegie 
│     │                 │       │                ├ [11]: Inner-Net 
│     │                 │       │                ├ [12]: MIT-like-Lord 
│     │                 │       │                ├ [13]: BSD-like-Spencer 
│     │                 │       │                ├ [14]: PCRE 
│     │                 │       │                ├ [15]: BSD-3-clause-Carnegie 
│     │                 │       │                ├ [16]: Unicode-DFS-2016 
│     │                 │       │                ├ [17]: BSL-1.0 
│     │                 │       │                ├ [18]: SunPro 
│     │                 │       │                ├ [19]: CORE-MATH 
│     │                 │       │                ├ [20]: BSD-3-clause-Berkeley 
│     │                 │       │                ├ [21]: BSD-3-clause-WIDE 
│     │                 │       │                ├ [22]: BSD-2-Clause 
│     │                 │       │                ├ [23]: BSD-3-clause-Oracle 
│     │                 │       │                ├ [24]: DEC 
│     │                 │       │                ├ [25]: IBM 
│     │                 │       │                ├ [26]: ISC 
│     │                 │       │                ├ [27]: Univ-Coimbra 
│     │                 │       │                ├ [28]: public-domain 
│     │                 │       │                ├ [29]: GPL-3.0-only 
│     │                 │       │                ├ [30]: LGPL-2.0-only 
│     │                 │       │                ├ [31]: LGPL-2.1-only 
│     │                 │       │                ╰ [32]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libgcc-s1@15-20250404-0ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/lib/x86_64-linux-gnu/gconv/ANSI_X3.110.so 
│     │                 │                        ├ [1]  : /usr/lib/x86_64-linux-gnu/gconv/ARMSCII-8.so 
│     │                 │                        ├ [2]  : /usr/lib/x86_64-linux-gnu/gconv/ASMO_449.so 
│     │                 │                        ├ [3]  : /usr/lib/x86_64-linux-gnu/gconv/BIG5.so 
│     │                 │                        ├ [4]  : /usr/lib/x86_64-linux-gnu/gconv/BIG5HKSCS.so 
│     │                 │                        ├ [5]  : /usr/lib/x86_64-linux-gnu/gconv/BRF.so 
│     │                 │                        ├ [6]  : /usr/lib/x86_64-linux-gnu/gconv/CP10007.so 
│     │                 │                        ├ [7]  : /usr/lib/x86_64-linux-gnu/gconv/CP1125.so 
│     │                 │                        ├ [8]  : /usr/lib/x86_64-linux-gnu/gconv/CP1250.so 
│     │                 │                        ├ [9]  : /usr/lib/x86_64-linux-gnu/gconv/CP1251.so 
│     │                 │                        ├ [10] : /usr/lib/x86_64-linux-gnu/gconv/CP1252.so 
│     │                 │                        ├ [11] : /usr/lib/x86_64-linux-gnu/gconv/CP1253.so 
│     │                 │                        ├ [12] : /usr/lib/x86_64-linux-gnu/gconv/CP1254.so 
│     │                 │                        ├ [13] : /usr/lib/x86_64-linux-gnu/gconv/CP1255.so 
│     │                 │                        ├ [14] : /usr/lib/x86_64-linux-gnu/gconv/CP1256.so 
│     │                 │                        ├ [15] : /usr/lib/x86_64-linux-gnu/gconv/CP1257.so 
│     │                 │                        ├ [16] : /usr/lib/x86_64-linux-gnu/gconv/CP1258.so 
│     │                 │                        ├ [17] : /usr/lib/x86_64-linux-gnu/gconv/CP737.so 
│     │                 │                        ├ [18] : /usr/lib/x86_64-linux-gnu/gconv/CP770.so 
│     │                 │                        ├ [19] : /usr/lib/x86_64-linux-gnu/gconv/CP771.so 
│     │                 │                        ├ [20] : /usr/lib/x86_64-linux-gnu/gconv/CP772.so 
│     │                 │                        ├ [21] : /usr/lib/x86_64-linux-gnu/gconv/CP773.so 
│     │                 │                        ├ [22] : /usr/lib/x86_64-linux-gnu/gconv/CP774.so 
│     │                 │                        ├ [23] : /usr/lib/x86_64-linux-gnu/gconv/CP775.so 
│     │                 │                        ├ [24] : /usr/lib/x86_64-linux-gnu/gconv/CP932.so 
│     │                 │                        ├ [25] : /usr/lib/x86_64-linux-gnu/gconv/CSN_369103.so 
│     │                 │                        ├ [26] : /usr/lib/x86_64-linux-gnu/gconv/CWI.so 
│     │                 │                        ├ [27] : /usr/lib/x86_64-linux-gnu/gconv/DEC-MCS.so 
│     │                 │                        ├ [28] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-AT-DE-A.so 
│     │                 │                        ├ [29] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-AT-DE.so 
│     │                 │                        ├ [30] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-CA-FR.so 
│     │                 │                        ├ [31] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-DK-NO-A.so 
│     │                 │                        ├ [32] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-DK-NO.so 
│     │                 │                        ├ [33] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-ES-A.so 
│     │                 │                        ├ [34] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-ES-S.so 
│     │                 │                        ├ [35] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-ES.so 
│     │                 │                        ├ [36] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-FI-SE-A.so 
│     │                 │                        ├ [37] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-FI-SE.so 
│     │                 │                        ├ [38] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-FR.so 
│     │                 │                        ├ [39] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-IS-FRISS.so 
│     │                 │                        ├ [40] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-IT.so 
│     │                 │                        ├ [41] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-PT.so 
│     │                 │                        ├ [42] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-UK.so 
│     │                 │                        ├ [43] : /usr/lib/x86_64-linux-gnu/gconv/EBCDIC-US.so 
│     │                 │                        ├ [44] : /usr/lib/x86_64-linux-gnu/gconv/ECMA-CYRILLIC.so 
│     │                 │                        ├ [45] : /usr/lib/x86_64-linux-gnu/gconv/EUC-CN.so 
│     │                 │                        ├ [46] : /usr/lib/x86_64-linux-gnu/gconv/EUC-JISX0213.so 
│     │                 │                        ├ [47] : /usr/lib/x86_64-linux-gnu/gconv/EUC-JP-MS.so 
│     │                 │                        ├ [48] : /usr/lib/x86_64-linux-gnu/gconv/EUC-JP.so 
│     │                 │                        ├ [49] : /usr/lib/x86_64-linux-gnu/gconv/EUC-KR.so 
│     │                 │                        ├ [50] : /usr/lib/x86_64-linux-gnu/gconv/EUC-TW.so 
│     │                 │                        ├ [51] : /usr/lib/x86_64-linux-gnu/gconv/GB18030.so 
│     │                 │                        ├ [52] : /usr/lib/x86_64-linux-gnu/gconv/GBBIG5.so 
│     │                 │                        ├ [53] : /usr/lib/x86_64-linux-gnu/gconv/GBGBK.so 
│     │                 │                        ├ [54] : /usr/lib/x86_64-linux-gnu/gconv/GBK.so 
│     │                 │                        ├ [55] : /usr/lib/x86_64-linux-gnu/gconv/GEORGIAN-ACADEMY.so 
│     │                 │                        ├ [56] : /usr/lib/x86_64-linux-gnu/gconv/GEORGIAN-PS.so 
│     │                 │                        ├ [57] : /usr/lib/x86_64-linux-gnu/gconv/GOST_19768-74.so 
│     │                 │                        ├ [58] : /usr/lib/x86_64-linux-gnu/gconv/GREEK-CCITT.so 
│     │                 │                        ├ [59] : /usr/lib/x86_64-linux-gnu/gconv/GREEK7-OLD.so 
│     │                 │                        ├ [60] : /usr/lib/x86_64-linux-gnu/gconv/GREEK7.so 
│     │                 │                        ├ [61] : /usr/lib/x86_64-linux-gnu/gconv/HP-GREEK8.so 
│     │                 │                        ├ [62] : /usr/lib/x86_64-linux-gnu/gconv/HP-ROMAN8.so 
│     │                 │                        ├ [63] : /usr/lib/x86_64-linux-gnu/gconv/HP-ROMAN9.so 
│     │                 │                        ├ [64] : /usr/lib/x86_64-linux-gnu/gconv/HP-THAI8.so 
│     │                 │                        ├ [65] : /usr/lib/x86_64-linux-gnu/gconv/HP-TURKISH8.so 
│     │                 │                        ├ [66] : /usr/lib/x86_64-linux-gnu/gconv/IBM037.so 
│     │                 │                        ├ [67] : /usr/lib/x86_64-linux-gnu/gconv/IBM038.so 
│     │                 │                        ├ [68] : /usr/lib/x86_64-linux-gnu/gconv/IBM1004.so 
│     │                 │                        ├ [69] : /usr/lib/x86_64-linux-gnu/gconv/IBM1008.so 
│     │                 │                        ├ [70] : /usr/lib/x86_64-linux-gnu/gconv/IBM1008_420.so 
│     │                 │                        ├ [71] : /usr/lib/x86_64-linux-gnu/gconv/IBM1025.so 
│     │                 │                        ├ [72] : /usr/lib/x86_64-linux-gnu/gconv/IBM1026.so 
│     │                 │                        ├ [73] : /usr/lib/x86_64-linux-gnu/gconv/IBM1046.so 
│     │                 │                        ├ [74] : /usr/lib/x86_64-linux-gnu/gconv/IBM1047.so 
│     │                 │                        ├ [75] : /usr/lib/x86_64-linux-gnu/gconv/IBM1097.so 
│     │                 │                        ├ [76] : /usr/lib/x86_64-linux-gnu/gconv/IBM1112.so 
│     │                 │                        ├ [77] : /usr/lib/x86_64-linux-gnu/gconv/IBM1122.so 
│     │                 │                        ├ [78] : /usr/lib/x86_64-linux-gnu/gconv/IBM1123.so 
│     │                 │                        ├ [79] : /usr/lib/x86_64-linux-gnu/gconv/IBM1124.so 
│     │                 │                        ├ [80] : /usr/lib/x86_64-linux-gnu/gconv/IBM1129.so 
│     │                 │                        ├ [81] : /usr/lib/x86_64-linux-gnu/gconv/IBM1130.so 
│     │                 │                        ├ [82] : /usr/lib/x86_64-linux-gnu/gconv/IBM1132.so 
│     │                 │                        ├ [83] : /usr/lib/x86_64-linux-gnu/gconv/IBM1133.so 
│     │                 │                        ├ [84] : /usr/lib/x86_64-linux-gnu/gconv/IBM1137.so 
│     │                 │                        ├ [85] : /usr/lib/x86_64-linux-gnu/gconv/IBM1140.so 
│     │                 │                        ├ [86] : /usr/lib/x86_64-linux-gnu/gconv/IBM1141.so 
│     │                 │                        ├ [87] : /usr/lib/x86_64-linux-gnu/gconv/IBM1142.so 
│     │                 │                        ├ [88] : /usr/lib/x86_64-linux-gnu/gconv/IBM1143.so 
│     │                 │                        ├ [89] : /usr/lib/x86_64-linux-gnu/gconv/IBM1144.so 
│     │                 │                        ├ [90] : /usr/lib/x86_64-linux-gnu/gconv/IBM1145.so 
│     │                 │                        ├ [91] : /usr/lib/x86_64-linux-gnu/gconv/IBM1146.so 
│     │                 │                        ├ [92] : /usr/lib/x86_64-linux-gnu/gconv/IBM1147.so 
│     │                 │                        ├ [93] : /usr/lib/x86_64-linux-gnu/gconv/IBM1148.so 
│     │                 │                        ├ [94] : /usr/lib/x86_64-linux-gnu/gconv/IBM1149.so 
│     │                 │                        ├ [95] : /usr/lib/x86_64-linux-gnu/gconv/IBM1153.so 
│     │                 │                        ├ [96] : /usr/lib/x86_64-linux-gnu/gconv/IBM1154.so 
│     │                 │                        ├ [97] : /usr/lib/x86_64-linux-gnu/gconv/IBM1155.so 
│     │                 │                        ├ [98] : /usr/lib/x86_64-linux-gnu/gconv/IBM1156.so 
│     │                 │                        ├ [99] : /usr/lib/x86_64-linux-gnu/gconv/IBM1157.so 
│     │                 │                        ├ [100]: /usr/lib/x86_64-linux-gnu/gconv/IBM1158.so 
│     │                 │                        ├ [101]: /usr/lib/x86_64-linux-gnu/gconv/IBM1160.so 
│     │                 │                        ├ [102]: /usr/lib/x86_64-linux-gnu/gconv/IBM1161.so 
│     │                 │                        ├ [103]: /usr/lib/x86_64-linux-gnu/gconv/IBM1162.so 
│     │                 │                        ├ [104]: /usr/lib/x86_64-linux-gnu/gconv/IBM1163.so 
│     │                 │                        ├ [105]: /usr/lib/x86_64-linux-gnu/gconv/IBM1164.so 
│     │                 │                        ├ [106]: /usr/lib/x86_64-linux-gnu/gconv/IBM1166.so 
│     │                 │                        ├ [107]: /usr/lib/x86_64-linux-gnu/gconv/IBM1167.so 
│     │                 │                        ├ [108]: /usr/lib/x86_64-linux-gnu/gconv/IBM12712.so 
│     │                 │                        ├ [109]: /usr/lib/x86_64-linux-gnu/gconv/IBM1364.so 
│     │                 │                        ├ [110]: /usr/lib/x86_64-linux-gnu/gconv/IBM1371.so 
│     │                 │                        ├ [111]: /usr/lib/x86_64-linux-gnu/gconv/IBM1388.so 
│     │                 │                        ├ [112]: /usr/lib/x86_64-linux-gnu/gconv/IBM1390.so 
│     │                 │                        ├ [113]: /usr/lib/x86_64-linux-gnu/gconv/IBM1399.so 
│     │                 │                        ├ [114]: /usr/lib/x86_64-linux-gnu/gconv/IBM16804.so 
│     │                 │                        ├ [115]: /usr/lib/x86_64-linux-gnu/gconv/IBM256.so 
│     │                 │                        ├ [116]: /usr/lib/x86_64-linux-gnu/gconv/IBM273.so 
│     │                 │                        ├ [117]: /usr/lib/x86_64-linux-gnu/gconv/IBM274.so 
│     │                 │                        ├ [118]: /usr/lib/x86_64-linux-gnu/gconv/IBM275.so 
│     │                 │                        ├ [119]: /usr/lib/x86_64-linux-gnu/gconv/IBM277.so 
│     │                 │                        ├ [120]: /usr/lib/x86_64-linux-gnu/gconv/IBM278.so 
│     │                 │                        ├ [121]: /usr/lib/x86_64-linux-gnu/gconv/IBM280.so 
│     │                 │                        ├ [122]: /usr/lib/x86_64-linux-gnu/gconv/IBM281.so 
│     │                 │                        ├ [123]: /usr/lib/x86_64-linux-gnu/gconv/IBM284.so 
│     │                 │                        ├ [124]: /usr/lib/x86_64-linux-gnu/gconv/IBM285.so 
│     │                 │                        ├ [125]: /usr/lib/x86_64-linux-gnu/gconv/IBM290.so 
│     │                 │                        ├ [126]: /usr/lib/x86_64-linux-gnu/gconv/IBM297.so 
│     │                 │                        ├ [127]: /usr/lib/x86_64-linux-gnu/gconv/IBM420.so 
│     │                 │                        ├ [128]: /usr/lib/x86_64-linux-gnu/gconv/IBM423.so 
│     │                 │                        ├ [129]: /usr/lib/x86_64-linux-gnu/gconv/IBM424.so 
│     │                 │                        ├ [130]: /usr/lib/x86_64-linux-gnu/gconv/IBM437.so 
│     │                 │                        ├ [131]: /usr/lib/x86_64-linux-gnu/gconv/IBM4517.so 
│     │                 │                        ├ [132]: /usr/lib/x86_64-linux-gnu/gconv/IBM4899.so 
│     │                 │                        ├ [133]: /usr/lib/x86_64-linux-gnu/gconv/IBM4909.so 
│     │                 │                        ├ [134]: /usr/lib/x86_64-linux-gnu/gconv/IBM4971.so 
│     │                 │                        ├ [135]: /usr/lib/x86_64-linux-gnu/gconv/IBM500.so 
│     │                 │                        ├ [136]: /usr/lib/x86_64-linux-gnu/gconv/IBM5347.so 
│     │                 │                        ├ [137]: /usr/lib/x86_64-linux-gnu/gconv/IBM803.so 
│     │                 │                        ├ [138]: /usr/lib/x86_64-linux-gnu/gconv/IBM850.so 
│     │                 │                        ├ [139]: /usr/lib/x86_64-linux-gnu/gconv/IBM851.so 
│     │                 │                        ├ [140]: /usr/lib/x86_64-linux-gnu/gconv/IBM852.so 
│     │                 │                        ├ [141]: /usr/lib/x86_64-linux-gnu/gconv/IBM855.so 
│     │                 │                        ├ [142]: /usr/lib/x86_64-linux-gnu/gconv/IBM856.so 
│     │                 │                        ├ [143]: /usr/lib/x86_64-linux-gnu/gconv/IBM857.so 
│     │                 │                        ├ [144]: /usr/lib/x86_64-linux-gnu/gconv/IBM858.so 
│     │                 │                        ├ [145]: /usr/lib/x86_64-linux-gnu/gconv/IBM860.so 
│     │                 │                        ├ [146]: /usr/lib/x86_64-linux-gnu/gconv/IBM861.so 
│     │                 │                        ├ [147]: /usr/lib/x86_64-linux-gnu/gconv/IBM862.so 
│     │                 │                        ├ [148]: /usr/lib/x86_64-linux-gnu/gconv/IBM863.so 
│     │                 │                        ├ [149]: /usr/lib/x86_64-linux-gnu/gconv/IBM864.so 
│     │                 │                        ├ [150]: /usr/lib/x86_64-linux-gnu/gconv/IBM865.so 
│     │                 │                        ├ [151]: /usr/lib/x86_64-linux-gnu/gconv/IBM866.so 
│     │                 │                        ├ [152]: /usr/lib/x86_64-linux-gnu/gconv/IBM866NAV.so 
│     │                 │                        ├ [153]: /usr/lib/x86_64-linux-gnu/gconv/IBM868.so 
│     │                 │                        ├ [154]: /usr/lib/x86_64-linux-gnu/gconv/IBM869.so 
│     │                 │                        ├ [155]: /usr/lib/x86_64-linux-gnu/gconv/IBM870.so 
│     │                 │                        ├ [156]: /usr/lib/x86_64-linux-gnu/gconv/IBM871.so 
│     │                 │                        ├ [157]: /usr/lib/x86_64-linux-gnu/gconv/IBM874.so 
│     │                 │                        ├ [158]: /usr/lib/x86_64-linux-gnu/gconv/IBM875.so 
│     │                 │                        ├ [159]: /usr/lib/x86_64-linux-gnu/gconv/IBM880.so 
│     │                 │                        ├ [160]: /usr/lib/x86_64-linux-gnu/gconv/IBM891.so 
│     │                 │                        ├ [161]: /usr/lib/x86_64-linux-gnu/gconv/IBM901.so 
│     │                 │                        ├ [162]: /usr/lib/x86_64-linux-gnu/gconv/IBM902.so 
│     │                 │                        ├ [163]: /usr/lib/x86_64-linux-gnu/gconv/IBM903.so 
│     │                 │                        ├ [164]: /usr/lib/x86_64-linux-gnu/gconv/IBM9030.so 
│     │                 │                        ├ [165]: /usr/lib/x86_64-linux-gnu/gconv/IBM904.so 
│     │                 │                        ├ [166]: /usr/lib/x86_64-linux-gnu/gconv/IBM905.so 
│     │                 │                        ├ [167]: /usr/lib/x86_64-linux-gnu/gconv/IBM9066.so 
│     │                 │                        ├ [168]: /usr/lib/x86_64-linux-gnu/gconv/IBM918.so 
│     │                 │                        ├ [169]: /usr/lib/x86_64-linux-gnu/gconv/IBM921.so 
│     │                 │                        ├ [170]: /usr/lib/x86_64-linux-gnu/gconv/IBM922.so 
│     │                 │                        ├ [171]: /usr/lib/x86_64-linux-gnu/gconv/IBM930.so 
│     │                 │                        ├ [172]: /usr/lib/x86_64-linux-gnu/gconv/IBM932.so 
│     │                 │                        ├ [173]: /usr/lib/x86_64-linux-gnu/gconv/IBM933.so 
│     │                 │                        ├ [174]: /usr/lib/x86_64-linux-gnu/gconv/IBM935.so 
│     │                 │                        ├ [175]: /usr/lib/x86_64-linux-gnu/gconv/IBM937.so 
│     │                 │                        ├ [176]: /usr/lib/x86_64-linux-gnu/gconv/IBM939.so 
│     │                 │                        ├ [177]: /usr/lib/x86_64-linux-gnu/gconv/IBM943.so 
│     │                 │                        ├ [178]: /usr/lib/x86_64-linux-gnu/gconv/IBM9448.so 
│     │                 │                        ├ [179]: /usr/lib/x86_64-linux-gnu/gconv/IEC_P27-1.so 
│     │                 │                        ├ [180]: /usr/lib/x86_64-linux-gnu/gconv/INIS-8.so 
│     │                 │                        ├ [181]: /usr/lib/x86_64-linux-gnu/gconv/INIS-CYRILLIC.so 
│     │                 │                        ├ [182]: /usr/lib/x86_64-linux-gnu/gconv/INIS.so 
│     │                 │                        ├ [183]: /usr/lib/x86_64-linux-gnu/gconv/ISIRI-3342.so 
│     │                 │                        ├ [184]: /usr/lib/x86_64-linux-gnu/gconv/ISO-2022-CN-EXT.so 
│     │                 │                        ├ [185]: /usr/lib/x86_64-linux-gnu/gconv/ISO-2022-CN.so 
│     │                 │                        ├ [186]: /usr/lib/x86_64-linux-gnu/gconv/ISO-2022-JP-3.so 
│     │                 │                        ├ [187]: /usr/lib/x86_64-linux-gnu/gconv/ISO-2022-JP.so 
│     │                 │                        ├ [188]: /usr/lib/x86_64-linux-gnu/gconv/ISO-2022-KR.so 
│     │                 │                        ├ [189]: /usr/lib/x86_64-linux-gnu/gconv/ISO-IR-197.so 
│     │                 │                        ├ [190]: /usr/lib/x86_64-linux-gnu/gconv/ISO-IR-209.so 
│     │                 │                        ├ [191]: /usr/lib/x86_64-linux-gnu/gconv/ISO646.so 
│     │                 │                        ├ [192]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-1.so 
│     │                 │                        ├ [193]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-10.so 
│     │                 │                        ├ [194]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-11.so 
│     │                 │                        ├ [195]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-13.so 
│     │                 │                        ├ [196]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-14.so 
│     │                 │                        ├ [197]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-15.so 
│     │                 │                        ├ [198]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-16.so 
│     │                 │                        ├ [199]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-2.so 
│     │                 │                        ├ [200]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-3.so 
│     │                 │                        ├ [201]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-4.so 
│     │                 │                        ├ [202]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-5.so 
│     │                 │                        ├ [203]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-6.so 
│     │                 │                        ├ [204]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-7.so 
│     │                 │                        ├ [205]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-8.so 
│     │                 │                        ├ [206]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-9.so 
│     │                 │                        ├ [207]: /usr/lib/x86_64-linux-gnu/gconv/ISO8859-9E.so 
│     │                 │                        ├ [208]: /usr/lib/x86_64-linux-gnu/gconv/ISO_10367-BOX.so 
│     │                 │                        ├ [209]: /usr/lib/x86_64-linux-gnu/gconv/ISO_11548-1.so 
│     │                 │                        ├ [210]: /usr/lib/x86_64-linux-gnu/gconv/ISO_2033.so 
│     │                 │                        ├ [211]: /usr/lib/x86_64-linux-gnu/gconv/ISO_5427-EXT.so 
│     │                 │                        ├ [212]: /usr/lib/x86_64-linux-gnu/gconv/ISO_5427.so 
│     │                 │                        ├ [213]: /usr/lib/x86_64-linux-gnu/gconv/ISO_5428.so 
│     │                 │                        ├ [214]: /usr/lib/x86_64-linux-gnu/gconv/ISO_6937-2.so 
│     │                 │                        ├ [215]: /usr/lib/x86_64-linux-gnu/gconv/ISO_6937.so 
│     │                 │                        ├ [216]: /usr/lib/x86_64-linux-gnu/gconv/JOHAB.so 
│     │                 │                        ├ [217]: /usr/lib/x86_64-linux-gnu/gconv/KOI-8.so 
│     │                 │                        ├ [218]: /usr/lib/x86_64-linux-gnu/gconv/KOI8-R.so 
│     │                 │                        ├ [219]: /usr/lib/x86_64-linux-gnu/gconv/KOI8-RU.so 
│     │                 │                        ├ [220]: /usr/lib/x86_64-linux-gnu/gconv/KOI8-T.so 
│     │                 │                        ├ [221]: /usr/lib/x86_64-linux-gnu/gconv/KOI8-U.so 
│     │                 │                        ├ [222]: /usr/lib/x86_64-linux-gnu/gconv/LATIN-GREEK-1.so 
│     │                 │                        ├ [223]: /usr/lib/x86_64-linux-gnu/gconv/LATIN-GREEK.so 
│     │                 │                        ├ [224]: /usr/lib/x86_64-linux-gnu/gconv/MAC-CENTRALEUROPE.so 
│     │                 │                        ├ [225]: /usr/lib/x86_64-linux-gnu/gconv/MAC-IS.so 
│     │                 │                        ├ [226]: /usr/lib/x86_64-linux-gnu/gconv/MAC-SAMI.so 
│     │                 │                        ├ [227]: /usr/lib/x86_64-linux-gnu/gconv/MAC-UK.so 
│     │                 │                        ├ [228]: /usr/lib/x86_64-linux-gnu/gconv/MACINTOSH.so 
│     │                 │                        ├ [229]: /usr/lib/x86_64-linux-gnu/gconv/MIK.so 
│     │                 │                        ├ [230]: /usr/lib/x86_64-linux-gnu/gconv/NATS-DANO.so 
│     │                 │                        ├ [231]: /usr/lib/x86_64-linux-gnu/gconv/NATS-SEFI.so 
│     │                 │                        ├ [232]: /usr/lib/x86_64-linux-gnu/gconv/PT154.so 
│     │                 │                        ├ [233]: /usr/lib/x86_64-linux-gnu/gconv/RK1048.so 
│     │                 │                        ├ [234]: /usr/lib/x86_64-linux-gnu/gconv/SAMI-WS2.so 
│     │                 │                        ├ [235]: /usr/lib/x86_64-linux-gnu/gconv/SHIFT_JISX0213.so 
│     │                 │                        ├ [236]: /usr/lib/x86_64-linux-gnu/gconv/SJIS.so 
│     │                 │                        ├ [237]: /usr/lib/x86_64-linux-gnu/gconv/T.61.so 
│     │                 │                        ├ [238]: /usr/lib/x86_64-linux-gnu/gconv/TCVN5712-1.so 
│     │                 │                        ├ [239]: /usr/lib/x86_64-linux-gnu/gconv/TIS-620.so 
│     │                 │                        ├ [240]: /usr/lib/x86_64-linux-gnu/gconv/TSCII.so 
│     │                 │                        ├ [241]: /usr/lib/x86_64-linux-gnu/gconv/UHC.so 
│     │                 │                        ├ [242]: /usr/lib/x86_64-linux-gnu/gconv/UNICODE.so 
│     │                 │                        ├ [243]: /usr/lib/x86_64-linux-gnu/gconv/UTF-16.so 
│     │                 │                        ├ [244]: /usr/lib/x86_64-linux-gnu/gconv/UTF-32.so 
│     │                 │                        ├ [245]: /usr/lib/x86_64-linux-gnu/gconv/UTF-7.so 
│     │                 │                        ├ [246]: /usr/lib/x86_64-linux-gnu/gconv/VISCII.so 
│     │                 │                        ├ [247]: /usr/lib/x86_64-linux-gnu/gconv/gconv-modules 
│     │                 │                        ├ [248]: /usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache 
│     │                 │                        ├ [249]: /usr/lib/x86_64-linux-gnu/gconv/gconv-modules.d/gconv
│     │                 │                        │        -modules-extra.conf 
│     │                 │                        ├ [250]: /usr/lib/x86_64-linux-gnu/gconv/libCNS.so 
│     │                 │                        ├ [251]: /usr/lib/x86_64-linux-gnu/gconv/libGB.so 
│     │                 │                        ├ [252]: /usr/lib/x86_64-linux-gnu/gconv/libISOIR165.so 
│     │                 │                        ├ [253]: /usr/lib/x86_64-linux-gnu/gconv/libJIS.so 
│     │                 │                        ├ [254]: /usr/lib/x86_64-linux-gnu/gconv/libJISX0213.so 
│     │                 │                        ├ [255]: /usr/lib/x86_64-linux-gnu/gconv/libKSC.so 
│     │                 │                        ├ [256]: /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 
│     │                 │                        ├ [257]: /usr/lib/x86_64-linux-gnu/libBrokenLocale.so.1 
│     │                 │                        ├ [258]: /usr/lib/x86_64-linux-gnu/libanl.so.1 
│     │                 │                        ├ [259]: /usr/lib/x86_64-linux-gnu/libc.so.6 
│     │                 │                        ├ [260]: /usr/lib/x86_64-linux-gnu/libc_malloc_debug.so.0 
│     │                 │                        ├ [261]: /usr/lib/x86_64-linux-gnu/libdl.so.2 
│     │                 │                        ├ [262]: /usr/lib/x86_64-linux-gnu/libm.so.6 
│     │                 │                        ├ [263]: /usr/lib/x86_64-linux-gnu/libmemusage.so 
│     │                 │                        ├ [264]: /usr/lib/x86_64-linux-gnu/libmvec.so.1 
│     │                 │                        ├ [265]: /usr/lib/x86_64-linux-gnu/libnsl.so.1 
│     │                 │                        ├ [266]: /usr/lib/x86_64-linux-gnu/libnss_compat.so.2 
│     │                 │                        ├ [267]: /usr/lib/x86_64-linux-gnu/libnss_dns.so.2 
│     │                 │                        ├ [268]: /usr/lib/x86_64-linux-gnu/libnss_files.so.2 
│     │                 │                        ├ [269]: /usr/lib/x86_64-linux-gnu/libnss_hesiod.so.2 
│     │                 │                        ├ [270]: /usr/lib/x86_64-linux-gnu/libpcprofile.so 
│     │                 │                        ├ [271]: /usr/lib/x86_64-linux-gnu/libpthread.so.0 
│     │                 │                        ├ [272]: /usr/lib/x86_64-linux-gnu/libresolv.so.2 
│     │                 │                        ├ [273]: /usr/lib/x86_64-linux-gnu/librt.so.1 
│     │                 │                        ├ [274]: /usr/lib/x86_64-linux-gnu/libthread_db.so.1 
│     │                 │                        ├ [275]: /usr/lib/x86_64-linux-gnu/libutil.so.1 
│     │                 │                        ├ [276]: /usr/share/doc/libc6/NEWS.Debian.gz 
│     │                 │                        ├ [277]: /usr/share/doc/libc6/NEWS.gz 
│     │                 │                        ├ [278]: /usr/share/doc/libc6/README.Debian.gz 
│     │                 │                        ├ [279]: /usr/share/doc/libc6/README.hesiod.gz 
│     │                 │                        ├ [280]: /usr/share/doc/libc6/changelog.Debian.gz 
│     │                 │                        ├ [281]: /usr/share/doc/libc6/copyright 
│     │                 │                        ╰ [282]: /usr/share/lintian/overrides/libc6 
│     │                 ├ [37]  ╭ ID            : libcap-ng0@0.8.5-4build1 
│     │                 │       ├ Name          : libcap-ng0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libcap-ng0@0.8.5-4build1?arch=amd64&dis
│     │                 │       │                │       tro=ubuntu-25.04 
│     │                 │       │                ╰ UID : a21954ab3756b44f 
│     │                 │       ├ Version       : 0.8.5 
│     │                 │       ├ Release       : 4build1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libcap-ng 
│     │                 │       ├ SrcVersion    : 0.8.5 
│     │                 │       ├ SrcRelease    : 4build1 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-2.1-or-later 
│     │                 │       │                ├ [1]: GPL-2.0-or-later 
│     │                 │       │                ├ [2]: GPL-3.0-only 
│     │                 │       │                ├ [3]: LGPL-2.1-only 
│     │                 │       │                ╰ [4]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:c179df0468e663a0c62f3d1bc891b8595d5144de7e56f48bec8a60
│     │                 │       │                 0d2b7d7c9b 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libcap-ng.so.0.0.0 
│     │                 │                        ├ [1]: /usr/lib/x86_64-linux-gnu/libdrop_ambient.so.0.0.0 
│     │                 │                        ├ [2]: /usr/share/doc/libcap-ng0/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/libcap-ng0/copyright 
│     │                 ├ [38]  ╭ ID            : libcap2@1:2.73-4ubuntu1 
│     │                 │       ├ Name          : libcap2 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libcap2@2.73-4ubuntu1?arch=amd64&distro
│     │                 │       │                │       =ubuntu-25.04&epoch=1 
│     │                 │       │                ╰ UID : b8d30ba08d6741 
│     │                 │       ├ Version       : 2.73 
│     │                 │       ├ Release       : 4ubuntu1 
│     │                 │       ├ Epoch         : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libcap2 
│     │                 │       ├ SrcVersion    : 2.73 
│     │                 │       ├ SrcRelease    : 4ubuntu1 
│     │                 │       ├ SrcEpoch      : 1 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ├ [1]: GPL-2.0-only 
│     │                 │       │                ╰ [2]: GPL-2.0-or-later 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:e4bff5cdeb8b97b561ae2fc4b8a5037f7bb36f1751cda74eccfd47
│     │                 │       │                 b443cf3705 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libcap.so.2.73 
│     │                 │                        ├ [1]: /usr/lib/x86_64-linux-gnu/libpsx.so.2.73 
│     │                 │                        ├ [2]: /usr/share/doc/libcap2/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/libcap2/copyright 
│     │                 ├ [39]  ╭ ID            : libcom-err2@1.47.2-1ubuntu1 
│     │                 │       ├ Name          : libcom-err2 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libcom-err2@1.47.2-1ubuntu1?arch=amd64&
│     │                 │       │                │       distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 6b7fb54f11fa2aa 
│     │                 │       ├ Version       : 1.47.2 
│     │                 │       ├ Release       : 1ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : e2fsprogs 
│     │                 │       ├ SrcVersion    : 1.47.2 
│     │                 │       ├ SrcRelease    : 1ubuntu1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-only 
│     │                 │       │                ├ [1] : GPL-2.0-or-later 
│     │                 │       │                ├ [2] : 0BSD 
│     │                 │       │                ├ [3] : MIT 
│     │                 │       │                ├ [4] : BSD-3-Clause-Variant 
│     │                 │       │                ├ [5] : BSD-3-Clause 
│     │                 │       │                ├ [6] : BSD-4-Clause-CMU 
│     │                 │       │                ├ [7] : LGPL-2.0-only 
│     │                 │       │                ├ [8] : Apache-2.0 
│     │                 │       │                ├ [9] : ISC 
│     │                 │       │                ├ [10]: MIT-US-export 
│     │                 │       │                ├ [11]: Kazlib 
│     │                 │       │                ├ [12]: Latex2e 
│     │                 │       │                ╰ [13]: GPL-2+ with Texinfo exception 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:92c42b0b73a4ae5695d888ded29f5343bc283e01fd6477eb596f40
│     │                 │       │                 c22015d00c 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libcom_err.so.2.1 
│     │                 │                        ├ [1]: /usr/share/doc/libcom-err2/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libcom-err2/copyright 
│     │                 ├ [40]  ╭ ID            : libcrypt1@1:4.4.38-1 
│     │                 │       ├ Name          : libcrypt1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libcrypt1@4.4.38-1?arch=amd64&distro=ub
│     │                 │       │                │       untu-25.04&epoch=1 
│     │                 │       │                ╰ UID : 1c44c45d03c93381 
│     │                 │       ├ Version       : 4.4.38 
│     │                 │       ├ Release       : 1 
│     │                 │       ├ Epoch         : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libxcrypt 
│     │                 │       ├ SrcVersion    : 4.4.38 
│     │                 │       ├ SrcRelease    : 1 
│     │                 │       ├ SrcEpoch      : 1 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:8c5fe434149b1697f0f82b2092ebdafcb93d28c954dde6d3f73411
│     │                 │       │                 2f7f0ecaee 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libcrypt.so.1.1.0 
│     │                 │                        ├ [1]: /usr/share/doc/libcrypt1/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libcrypt1/copyright 
│     │                 ├ [41]  ╭ ID            : libcurl4t64@8.12.1-3ubuntu1 
│     │                 │       ├ Name          : libcurl4t64 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.12.1-3ubuntu1?arch=amd64&
│     │                 │       │                │       distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : e39d89d31b7d2391 
│     │                 │       ├ Version       : 8.12.1 
│     │                 │       ├ Release       : 3ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : curl 
│     │                 │       ├ SrcVersion    : 8.12.1 
│     │                 │       ├ SrcRelease    : 3ubuntu1 
│     │                 │       ├ Licenses       ╭ [0] : curl 
│     │                 │       │                ├ [1] : OLDAP-2.8 
│     │                 │       │                ├ [2] : ISC 
│     │                 │       │                ├ [3] : GPL-2+ with Autoconf-data exception 
│     │                 │       │                ├ [4] : GPL-3+ with Autoconf-data exception 
│     │                 │       │                ├ [5] : GPL-2+ with Libtool exception 
│     │                 │       │                ├ [6] : BSD-3-Clause 
│     │                 │       │                ├ [7] : BSD-4-Clause-UC 
│     │                 │       │                ├ [8] : FSFULLR 
│     │                 │       │                ├ [9] : X11 
│     │                 │       │                ╰ [10]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0] : libbrotli1@1.1.0-2build4 
│     │                 │       │                ├ [1] : libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [2] : libgssapi-krb5-2@1.21.3-4ubuntu2 
│     │                 │       │                ├ [3] : libidn2-0@2.3.8-2 
│     │                 │       │                ├ [4] : libldap2@2.6.9+dfsg-2ubuntu1 
│     │                 │       │                ├ [5] : libnghttp2-14@1.64.0-1ubuntu1 
│     │                 │       │                ├ [6] : libpsl5t64@0.21.2-1.1build1 
│     │                 │       │                ├ [7] : librtmp1@2.4+20151223.gitfa8646d.1-2build7 
│     │                 │       │                ├ [8] : libssh2-1t64@1.11.1-1 
│     │                 │       │                ├ [9] : libssl3t64@3.4.1-1ubuntu4 
│     │                 │       │                ├ [10]: libzstd1@1.5.6+dfsg-2 
│     │                 │       │                ╰ [11]: zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libcurl.so.4.8.0 
│     │                 │                        ├ [1]: /usr/share/doc/libcurl4t64/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libcurl4t64/copyright 
│     │                 ├ [42]  ╭ ID            : libdb5.3t64@5.3.28+dfsg2-9 
│     │                 │       ├ Name          : libdb5.3t64 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libdb5.3t64@5.3.28%2Bdfsg2-9?arch=amd64
│     │                 │       │                │       &distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 43a94a2df7a812e6 
│     │                 │       ├ Version       : 5.3.28+dfsg2 
│     │                 │       ├ Release       : 9 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : db5.3 
│     │                 │       ├ SrcVersion    : 5.3.28+dfsg2 
│     │                 │       ├ SrcRelease    : 9 
│     │                 │       ├ Licenses       ╭ [0] : Sleepycat 
│     │                 │       │                ├ [1] : BSD-3-Clause 
│     │                 │       │                ├ [2] : MS-PL 
│     │                 │       │                ├ [3] : GPL-2.0-or-later 
│     │                 │       │                ├ [4] : Artistic-2.0 
│     │                 │       │                ├ [5] : X11 
│     │                 │       │                ├ [6] : MIT-old 
│     │                 │       │                ├ [7] : TCL-like 
│     │                 │       │                ├ [8] : BSD-3-clause-fjord 
│     │                 │       │                ├ [9] : GPL-3.0-only 
│     │                 │       │                ╰ [10]: Zlib 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:e5c56e85ceca6693ab040db58d21f4cd0c140b725f2b1740dfeac3
│     │                 │       │                 e6b96f350f 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libdb-5.3.so 
│     │                 │                        ├ [1]: /usr/share/doc/libdb5.3t64/build_signature_amd64.txt 
│     │                 │                        ├ [2]: /usr/share/doc/libdb5.3t64/changelog.Debian.gz 
│     │                 │                        ├ [3]: /usr/share/doc/libdb5.3t64/copyright 
│     │                 │                        ╰ [4]: /usr/share/lintian/overrides/libdb5.3t64 
│     │                 ├ [43]  ╭ ID            : libdebconfclient0@0.277ubuntu1 
│     │                 │       ├ Name          : libdebconfclient0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libdebconfclient0@0.277ubuntu1?arch=amd
│     │                 │       │                │       64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 8a0a3daa8ce7b073 
│     │                 │       ├ Version       : 0.277ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : cdebconf 
│     │                 │       ├ SrcVersion    : 0.277ubuntu1 
│     │                 │       ├ Licenses       ╭ [0]: BSD-2-Clause 
│     │                 │       │                ├ [1]: GPL-2.0-or-later 
│     │                 │       │                ╰ [2]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:18de76d36abf6cec09c313f3f3ee96c80f9f452ef281ca3ef4ea4e
│     │                 │       │                 af69fbfbc9 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libdebconfclient.so.0.0.0 
│     │                 │                        ├ [1]: /usr/share/doc/libdebconfclient0/changelog.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libdebconfclient0/copyright 
│     │                 ├ [44]  ╭ ID            : libext2fs2t64@1.47.2-1ubuntu1 
│     │                 │       ├ Name          : libext2fs2t64 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libext2fs2t64@1.47.2-1ubuntu1?arch=amd6
│     │                 │       │                │       4&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 4cc962da5302c17b 
│     │                 │       ├ Version       : 1.47.2 
│     │                 │       ├ Release       : 1ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : e2fsprogs 
│     │                 │       ├ SrcVersion    : 1.47.2 
│     │                 │       ├ SrcRelease    : 1ubuntu1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-only 
│     │                 │       │                ├ [1] : GPL-2.0-or-later 
│     │                 │       │                ├ [2] : 0BSD 
│     │                 │       │                ├ [3] : MIT 
│     │                 │       │                ├ [4] : BSD-3-Clause-Variant 
│     │                 │       │                ├ [5] : BSD-3-Clause 
│     │                 │       │                ├ [6] : BSD-4-Clause-CMU 
│     │                 │       │                ├ [7] : LGPL-2.0-only 
│     │                 │       │                ├ [8] : Apache-2.0 
│     │                 │       │                ├ [9] : ISC 
│     │                 │       │                ├ [10]: MIT-US-export 
│     │                 │       │                ├ [11]: Kazlib 
│     │                 │       │                ├ [12]: Latex2e 
│     │                 │       │                ╰ [13]: GPL-2+ with Texinfo exception 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:40e6242b5bbd20b0d4589f256b804d508d07840b79b87399564577
│     │                 │       │                 075890a2da 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libe2p.so.2.3 
│     │                 │                        ├ [1]: /usr/lib/x86_64-linux-gnu/libext2fs.so.2.4 
│     │                 │                        ├ [2]: /usr/share/doc/libext2fs2t64/changelog.Debian.gz 
│     │                 │                        ├ [3]: /usr/share/doc/libext2fs2t64/copyright 
│     │                 │                        ╰ [4]: /usr/share/lintian/overrides/libext2fs2t64 
│     │                 ├ [45]  ╭ ID            : libffi8@3.4.7-1 
│     │                 │       ├ Name          : libffi8 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libffi8@3.4.7-1?arch=amd64&distro=ubunt
│     │                 │       │                │       u-25.04 
│     │                 │       │                ╰ UID : 56a1d61c41470928 
│     │                 │       ├ Version       : 3.4.7 
│     │                 │       ├ Release       : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libffi 
│     │                 │       ├ SrcVersion    : 3.4.7 
│     │                 │       ├ SrcRelease    : 1 
│     │                 │       ├ Licenses       ╭ [0]: MIT 
│     │                 │       │                ├ [1]: X11 
│     │                 │       │                ├ [2]: GPL-2.0-or-later 
│     │                 │       │                ├ [3]: GPL-3.0-or-later 
│     │                 │       │                ├ [4]: MPL-1.1 
│     │                 │       │                ├ [5]: LGPL-2.1-or-later 
│     │                 │       │                ╰ [6]: public-domain 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libffi.so.8.1.4 
│     │                 │                        ├ [1]: /usr/share/doc/libffi8/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libffi8/copyright 
│     │                 ├ [46]  ╭ ID            : libgcc-s1@15-20250404-0ubuntu1 
│     │                 │       ├ Name          : libgcc-s1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libgcc-s1@15-20250404-0ubuntu1?arch=amd
│     │                 │       │                │       64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : e90dae861654b35f 
│     │                 │       ├ Version       : 15-20250404 
│     │                 │       ├ Release       : 0ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : gcc-15 
│     │                 │       ├ SrcVersion    : 15-20250404 
│     │                 │       ├ SrcRelease    : 0ubuntu1 
│     │                 │       ├ Maintainer    : Ubuntu Core developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: gcc-15-base@15-20250404-0ubuntu1 
│     │                 │       │                ╰ [1]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:0befdca610af390f03e87c0e63eac717425f8d33d570f99bd6197e
│     │                 │       │                 cbe6f334a5 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libgcc_s.so.1 
│     │                 │                        ╰ [1]: /usr/share/lintian/overrides/libgcc-s1 
│     │                 ├ [47]  ╭ ID            : libgcrypt20@1.11.0-6ubuntu1 
│     │                 │       ├ Name          : libgcrypt20 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libgcrypt20@1.11.0-6ubuntu1?arch=amd64&
│     │                 │       │                │       distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 5a0c5e86aadb6057 
│     │                 │       ├ Version       : 1.11.0 
│     │                 │       ├ Release       : 6ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libgcrypt20 
│     │                 │       ├ SrcVersion    : 1.11.0 
│     │                 │       ├ SrcRelease    : 6ubuntu1 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-2.0-or-later 
│     │                 │       │                ╰ [1]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libgpg-error0@1.51-3 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:b87379549b166e52bcd3203466fcf6ab7fa8f2c0c4c97f8eda27c1
│     │                 │       │                 3a1859f135 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libgcrypt.so.20.5.0 
│     │                 │                        ├ [1]: /usr/share/doc/libgcrypt20/AUTHORS.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libgcrypt20/NEWS.gz 
│     │                 │                        ├ [3]: /usr/share/doc/libgcrypt20/README.gz 
│     │                 │                        ├ [4]: /usr/share/doc/libgcrypt20/THANKS.gz 
│     │                 │                        ├ [5]: /usr/share/doc/libgcrypt20/changelog.Debian.gz 
│     │                 │                        ├ [6]: /usr/share/doc/libgcrypt20/copyright 
│     │                 │                        ╰ [7]: /usr/share/libgcrypt20/clean-up-unmanaged-libraries 
│     │                 ├ [48]  ╭ ID            : libgmp10@2:6.3.0+dfsg-3ubuntu1 
│     │                 │       ├ Name          : libgmp10 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libgmp10@6.3.0%2Bdfsg-3ubuntu1?arch=amd
│     │                 │       │                │       64&distro=ubuntu-25.04&epoch=2 
│     │                 │       │                ╰ UID : fb0a9b0289289e50 
│     │                 │       ├ Version       : 6.3.0+dfsg 
│     │                 │       ├ Release       : 3ubuntu1 
│     │                 │       ├ Epoch         : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : gmp 
│     │                 │       ├ SrcVersion    : 6.3.0+dfsg 
│     │                 │       ├ SrcRelease    : 3ubuntu1 
│     │                 │       ├ SrcEpoch      : 2 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: LGPL-3.0-or-later 
│     │                 │       │                ├ [2]: GPL-3.0-or-later 
│     │                 │       │                ├ [3]: GPL-3+ with Bison exception 
│     │                 │       │                ├ [4]: GPL-2.0-only 
│     │                 │       │                ├ [5]: GPL-3.0-only 
│     │                 │       │                ╰ [6]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:57327604cf9d01052c467d2a2fa64ec9f8208324a9044db09cb478
│     │                 │       │                 acc1f061d0 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libgmp.so.10.5.0 
│     │                 │                        ├ [1]: /usr/share/doc/libgmp10/README.Debian 
│     │                 │                        ├ [2]: /usr/share/doc/libgmp10/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/libgmp10/copyright 
│     │                 ├ [49]  ╭ ID            : libgnutls30t64@3.8.9-2ubuntu3.1 
│     │                 │       ├ Name          : libgnutls30t64 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libgnutls30t64@3.8.9-2ubuntu3.1?arch=am
│     │                 │       │                │       d64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 980d0b094651bf74 
│     │                 │       ├ Version       : 3.8.9 
│     │                 │       ├ Release       : 2ubuntu3.1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : gnutls28 
│     │                 │       ├ SrcVersion    : 3.8.9 
│     │                 │       ├ SrcRelease    : 2ubuntu3.1 
│     │                 │       ├ Licenses       ╭ [0] : LGPL-2.1-only 
│     │                 │       │                ├ [1] : LGPL-2.0-or-later 
│     │                 │       │                ├ [2] : LGPL-3.0-only 
│     │                 │       │                ├ [3] : GPL-2.0-or-later 
│     │                 │       │                ├ [4] : GPL-3.0-only 
│     │                 │       │                ├ [5] : GFDL-1.3-only 
│     │                 │       │                ├ [6] : CC0-1.0 
│     │                 │       │                ├ [7] : MIT 
│     │                 │       │                ├ [8] : Apache-2.0 
│     │                 │       │                ├ [9] : LGPL-3.0-or-later 
│     │                 │       │                ├ [10]: LGPL-2.1-or-later 
│     │                 │       │                ├ [11]: GPL-3.0-or-later 
│     │                 │       │                ├ [12]: BSD-3-Clause 
│     │                 │       │                ╰ [13]: FSFAP 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [1]: libgmp10@2:6.3.0+dfsg-3ubuntu1 
│     │                 │       │                ├ [2]: libhogweed6t64@3.10.1-1 
│     │                 │       │                ├ [3]: libidn2-0@2.3.8-2 
│     │                 │       │                ├ [4]: libnettle8t64@3.10.1-1 
│     │                 │       │                ├ [5]: libp11-kit0@0.25.5-2ubuntu3 
│     │                 │       │                ├ [6]: libtasn1-6@4.20.0-2 
│     │                 │       │                ╰ [7]: libunistring5@1.3-1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libgnutls.so.30.40.3 
│     │                 │                        ├ [1]: /usr/share/doc/libgnutls30t64/AUTHORS.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libgnutls30t64/NEWS.gz 
│     │                 │                        ├ [3]: /usr/share/doc/libgnutls30t64/README.md.gz 
│     │                 │                        ├ [4]: /usr/share/doc/libgnutls30t64/THANKS.gz 
│     │                 │                        ├ [5]: /usr/share/doc/libgnutls30t64/changelog.Debian.gz 
│     │                 │                        ├ [6]: /usr/share/doc/libgnutls30t64/copyright 
│     │                 │                        ╰ [7]: /usr/share/lintian/overrides/libgnutls30t64 
│     │                 ├ [50]  ╭ ID            : libgpg-error0@1.51-3 
│     │                 │       ├ Name          : libgpg-error0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libgpg-error0@1.51-3?arch=amd64&distro=
│     │                 │       │                │       ubuntu-25.04 
│     │                 │       │                ╰ UID : 29fc3f48ce9425a7 
│     │                 │       ├ Version       : 1.51 
│     │                 │       ├ Release       : 3 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libgpg-error 
│     │                 │       ├ SrcVersion    : 1.51 
│     │                 │       ├ SrcRelease    : 3 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-2.1-or-later 
│     │                 │       │                ├ [1]: BSD-3-Clause 
│     │                 │       │                ├ [2]: g10-permissive 
│     │                 │       │                ├ [3]: GPL-3.0-or-later 
│     │                 │       │                ├ [4]: LGPL-2.1-only 
│     │                 │       │                ╰ [5]: GPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:8d772e643a7d0855c18e5620a46c0124d88008b7759a7112f28960
│     │                 │       │                 f7dc69af8c 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.38.0 
│     │                 │                        ├ [1]: /usr/share/doc/libgpg-error0/README.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libgpg-error0/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/libgpg-error0/copyright 
│     │                 ├ [51]  ╭ ID            : libgssapi-krb5-2@1.21.3-4ubuntu2 
│     │                 │       ├ Name          : libgssapi-krb5-2 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libgssapi-krb5-2@1.21.3-4ubuntu2?arch=a
│     │                 │       │                │       md64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : cfa408fe08bf9427 
│     │                 │       ├ Version       : 1.21.3 
│     │                 │       ├ Release       : 4ubuntu2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : krb5 
│     │                 │       ├ SrcVersion    : 1.21.3 
│     │                 │       ├ SrcRelease    : 4ubuntu2 
│     │                 │       ├ Licenses       ─ [0]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [1]: libcom-err2@1.47.2-1ubuntu1 
│     │                 │       │                ├ [2]: libk5crypto3@1.21.3-4ubuntu2 
│     │                 │       │                ├ [3]: libkrb5-3@1.21.3-4ubuntu2 
│     │                 │       │                ╰ [4]: libkrb5support0@1.21.3-4ubuntu2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libgssapi_krb5.so.2.2 
│     │                 │                        ├ [1]: /usr/share/doc/libgssapi-krb5-2/copyright 
│     │                 │                        ╰ [2]: /usr/share/lintian/overrides/libgssapi-krb5-2 
│     │                 ├ [52]  ╭ ID            : libhogweed6t64@3.10.1-1 
│     │                 │       ├ Name          : libhogweed6t64 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libhogweed6t64@3.10.1-1?arch=amd64&dist
│     │                 │       │                │       ro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 986ade9f6c90477e 
│     │                 │       ├ Version       : 3.10.1 
│     │                 │       ├ Release       : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : nettle 
│     │                 │       ├ SrcVersion    : 3.10.1 
│     │                 │       ├ SrcRelease    : 1 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-3.0-or-later 
│     │                 │       │                ├ [1]: GPL-2.0-or-later 
│     │                 │       │                ├ [2]: LGPL-2.0-or-later 
│     │                 │       │                ├ [3]: LGPL-2.0-only 
│     │                 │       │                ├ [4]: MIT 
│     │                 │       │                ├ [5]: GPL-3.0-with-autoconf-exception+ 
│     │                 │       │                ├ [6]: public-domain 
│     │                 │       │                ├ [7]: GPL-2.0-only 
│     │                 │       │                ╰ [8]: GAP 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [1]: libgmp10@2:6.3.0+dfsg-3ubuntu1 
│     │                 │       │                ╰ [2]: libnettle8t64@3.10.1-1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libhogweed.so.6.10 
│     │                 │                        ├ [1]: /usr/share/doc/libhogweed6t64/copyright 
│     │                 │                        ╰ [2]: /usr/share/lintian/overrides/libhogweed6t64 
│     │                 ├ [53]  ╭ ID            : libidn2-0@2.3.8-2 
│     │                 │       ├ Name          : libidn2-0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libidn2-0@2.3.8-2?arch=amd64&distro=ubu
│     │                 │       │                │       ntu-25.04 
│     │                 │       │                ╰ UID : c11deacfe92e6d17 
│     │                 │       ├ Version       : 2.3.8 
│     │                 │       ├ Release       : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libidn2 
│     │                 │       ├ SrcVersion    : 2.3.8 
│     │                 │       ├ SrcRelease    : 2 
│     │                 │       ├ Licenses       ╭ [0]: GPL-3.0-or-later 
│     │                 │       │                ├ [1]: LGPL-3.0-or-later 
│     │                 │       │                ├ [2]: GPL-2.0-or-later 
│     │                 │       │                ├ [3]: MIT 
│     │                 │       │                ├ [4]: Unicode 
│     │                 │       │                ├ [5]: GPL-3.0-only 
│     │                 │       │                ├ [6]: GPL-2.0-only 
│     │                 │       │                ╰ [7]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libunistring5@1.3-1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libidn2.so.0.4.0 
│     │                 │                        ├ [1]: /usr/share/doc/libidn2-0/AUTHORS 
│     │                 │                        ├ [2]: /usr/share/doc/libidn2-0/NEWS.gz 
│     │                 │                        ├ [3]: /usr/share/doc/libidn2-0/README.md.gz 
│     │                 │                        ├ [4]: /usr/share/doc/libidn2-0/changelog.Debian.gz 
│     │                 │                        ├ [5]: /usr/share/doc/libidn2-0/copyright 
│     │                 │                        ╰ [6]: /usr/share/lintian/overrides/libidn2-0 
│     │                 ├ [54]  ╭ ID            : libk5crypto3@1.21.3-4ubuntu2 
│     │                 │       ├ Name          : libk5crypto3 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libk5crypto3@1.21.3-4ubuntu2?arch=amd64
│     │                 │       │                │       &distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : ea12349346510310 
│     │                 │       ├ Version       : 1.21.3 
│     │                 │       ├ Release       : 4ubuntu2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : krb5 
│     │                 │       ├ SrcVersion    : 1.21.3 
│     │                 │       ├ SrcRelease    : 4ubuntu2 
│     │                 │       ├ Licenses       ─ [0]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libkrb5support0@1.21.3-4ubuntu2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libk5crypto.so.3.1 
│     │                 │                        ╰ [1]: /usr/share/doc/libk5crypto3/copyright 
│     │                 ├ [55]  ╭ ID            : libkeyutils1@1.6.3-4ubuntu2 
│     │                 │       ├ Name          : libkeyutils1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libkeyutils1@1.6.3-4ubuntu2?arch=amd64&
│     │                 │       │                │       distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 20456e511e1f6f9b 
│     │                 │       ├ Version       : 1.6.3 
│     │                 │       ├ Release       : 4ubuntu2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : keyutils 
│     │                 │       ├ SrcVersion    : 1.6.3 
│     │                 │       ├ SrcRelease    : 4ubuntu2 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: LGPL-2.0-or-later 
│     │                 │       │                ├ [2]: GPL-2.0-only 
│     │                 │       │                ╰ [3]: LGPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libkeyutils.so.1.10 
│     │                 │                        ├ [1]: /usr/share/doc/libkeyutils1/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libkeyutils1/copyright 
│     │                 ├ [56]  ╭ ID            : libkrb5-3@1.21.3-4ubuntu2 
│     │                 │       ├ Name          : libkrb5-3 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libkrb5-3@1.21.3-4ubuntu2?arch=amd64&di
│     │                 │       │                │       stro=ubuntu-25.04 
│     │                 │       │                ╰ UID : c11c95553c484a6c 
│     │                 │       ├ Version       : 1.21.3 
│     │                 │       ├ Release       : 4ubuntu2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : krb5 
│     │                 │       ├ SrcVersion    : 1.21.3 
│     │                 │       ├ SrcRelease    : 4ubuntu2 
│     │                 │       ├ Licenses       ─ [0]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [1]: libcom-err2@1.47.2-1ubuntu1 
│     │                 │       │                ├ [2]: libk5crypto3@1.21.3-4ubuntu2 
│     │                 │       │                ├ [3]: libkeyutils1@1.6.3-4ubuntu2 
│     │                 │       │                ├ [4]: libkrb5support0@1.21.3-4ubuntu2 
│     │                 │       │                ╰ [5]: libssl3t64@3.4.1-1ubuntu4 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/krb5/plugins/preauth/spake.so 
│     │                 │                        ├ [1]: /usr/lib/x86_64-linux-gnu/libkrb5.so.3.3 
│     │                 │                        ├ [2]: /usr/share/doc/libkrb5-3/README.Debian 
│     │                 │                        ├ [3]: /usr/share/doc/libkrb5-3/README.gz 
│     │                 │                        ├ [4]: /usr/share/doc/libkrb5-3/copyright 
│     │                 │                        ╰ [5]: /usr/share/lintian/overrides/libkrb5-3 
│     │                 ├ [57]  ╭ ID            : libkrb5support0@1.21.3-4ubuntu2 
│     │                 │       ├ Name          : libkrb5support0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libkrb5support0@1.21.3-4ubuntu2?arch=am
│     │                 │       │                │       d64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 1a8079cf0998349d 
│     │                 │       ├ Version       : 1.21.3 
│     │                 │       ├ Release       : 4ubuntu2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : krb5 
│     │                 │       ├ SrcVersion    : 1.21.3 
│     │                 │       ├ SrcRelease    : 4ubuntu2 
│     │                 │       ├ Licenses       ─ [0]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libkrb5support.so.0.1 
│     │                 │                        ├ [1]: /usr/share/doc/libkrb5support0/changelog.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libkrb5support0/copyright 
│     │                 │                        ╰ [3]: /usr/share/lintian/overrides/libkrb5support0 
│     │                 ├ [58]  ╭ ID            : libldap-common@2.6.9+dfsg-2ubuntu1 
│     │                 │       ├ Name          : libldap-common 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libldap-common@2.6.9%2Bdfsg-2ubuntu1?ar
│     │                 │       │                │       ch=all&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : fd9a91bc2b6ec9ce 
│     │                 │       ├ Version       : 2.6.9+dfsg 
│     │                 │       ├ Release       : 2ubuntu1 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : openldap 
│     │                 │       ├ SrcVersion    : 2.6.9+dfsg 
│     │                 │       ├ SrcRelease    : 2ubuntu1 
│     │                 │       ├ Licenses       ╭ [0] : OpenLDAP-2.8 
│     │                 │       │                ├ [1] : FSF-unlimited 
│     │                 │       │                ├ [2] : GPL-2.0-with-autoconf-exception+ 
│     │                 │       │                ├ [3] : GPL-3.0-with-autoconf-exception+ 
│     │                 │       │                ├ [4] : GPL-2+ with Libtool exception 
│     │                 │       │                ├ [5] : GPL-3+ with Libtool exception 
│     │                 │       │                ├ [6] : GPL-3.0-or-later 
│     │                 │       │                ├ [7] : GPL-2.0-or-later 
│     │                 │       │                ├ [8] : UMich 
│     │                 │       │                ├ [9] : F5 
│     │                 │       │                ├ [10]: JCG 
│     │                 │       │                ├ [11]: MIT-XC 
│     │                 │       │                ├ [12]: NeoSoft-permissive 
│     │                 │       │                ├ [13]: BSD-3-Clause 
│     │                 │       │                ├ [14]: Beerware 
│     │                 │       │                ├ [15]: public-domain 
│     │                 │       │                ├ [16]: BSD-4-clause-California 
│     │                 │       │                ├ [17]: BSD-3-clause-variant 
│     │                 │       │                ├ [18]: Expat-ISC 
│     │                 │       │                ├ [19]: Expat-UNM 
│     │                 │       │                ├ [20]: MIT 
│     │                 │       │                ├ [21]: BSD-3-clause-California 
│     │                 │       │                ├ [22]: GPL-2.0-only 
│     │                 │       │                ╰ [23]: GPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/share/doc/libldap-common/NEWS.Debian.gz 
│     │                 │                        ├ [1]: /usr/share/doc/libldap-common/changelog.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libldap-common/copyright 
│     │                 │                        ╰ [3]: /usr/share/man/man5/ldap.conf.5.gz 
│     │                 ├ [59]  ╭ ID            : libldap2@2.6.9+dfsg-2ubuntu1 
│     │                 │       ├ Name          : libldap2 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libldap2@2.6.9%2Bdfsg-2ubuntu1?arch=amd
│     │                 │       │                │       64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : d71c2d3214699383 
│     │                 │       ├ Version       : 2.6.9+dfsg 
│     │                 │       ├ Release       : 2ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : openldap 
│     │                 │       ├ SrcVersion    : 2.6.9+dfsg 
│     │                 │       ├ SrcRelease    : 2ubuntu1 
│     │                 │       ├ Licenses       ╭ [0] : OpenLDAP-2.8 
│     │                 │       │                ├ [1] : FSF-unlimited 
│     │                 │       │                ├ [2] : GPL-2.0-with-autoconf-exception+ 
│     │                 │       │                ├ [3] : GPL-3.0-with-autoconf-exception+ 
│     │                 │       │                ├ [4] : GPL-2+ with Libtool exception 
│     │                 │       │                ├ [5] : GPL-3+ with Libtool exception 
│     │                 │       │                ├ [6] : GPL-3.0-or-later 
│     │                 │       │                ├ [7] : GPL-2.0-or-later 
│     │                 │       │                ├ [8] : UMich 
│     │                 │       │                ├ [9] : F5 
│     │                 │       │                ├ [10]: JCG 
│     │                 │       │                ├ [11]: MIT-XC 
│     │                 │       │                ├ [12]: NeoSoft-permissive 
│     │                 │       │                ├ [13]: BSD-3-Clause 
│     │                 │       │                ├ [14]: Beerware 
│     │                 │       │                ├ [15]: public-domain 
│     │                 │       │                ├ [16]: BSD-4-clause-California 
│     │                 │       │                ├ [17]: BSD-3-clause-variant 
│     │                 │       │                ├ [18]: Expat-ISC 
│     │                 │       │                ├ [19]: Expat-UNM 
│     │                 │       │                ├ [20]: MIT 
│     │                 │       │                ├ [21]: BSD-3-clause-California 
│     │                 │       │                ├ [22]: GPL-2.0-only 
│     │                 │       │                ╰ [23]: GPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [1]: libldap-common@2.6.9+dfsg-2ubuntu1 
│     │                 │       │                ├ [2]: libsasl2-2@2.1.28+dfsg1-9 
│     │                 │       │                ╰ [3]: libssl3t64@3.4.1-1ubuntu4 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/liblber.so.2.0.200 
│     │                 │                        ├ [1]: /usr/lib/x86_64-linux-gnu/libldap.so.2.0.200 
│     │                 │                        ├ [2]: /usr/share/doc/libldap2/NEWS.Debian.gz 
│     │                 │                        ├ [3]: /usr/share/doc/libldap2/changelog.Debian.gz 
│     │                 │                        ╰ [4]: /usr/share/doc/libldap2/copyright 
│     │                 ├ [60]  ╭ ID            : liblz4-1@1.10.0-4 
│     │                 │       ├ Name          : liblz4-1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/liblz4-1@1.10.0-4?arch=amd64&distro=ubu
│     │                 │       │                │       ntu-25.04 
│     │                 │       │                ╰ UID : af517a686fef85f0 
│     │                 │       ├ Version       : 1.10.0 
│     │                 │       ├ Release       : 4 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : lz4 
│     │                 │       ├ SrcVersion    : 1.10.0 
│     │                 │       ├ SrcRelease    : 4 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: BSD-2-Clause 
│     │                 │       │                ╰ [2]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libxxhash0@0.8.3-2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:5826ab42d1dd199dd0aceaf06bb175a93a83c9c9ce43e57376001f
│     │                 │       │                 58f045a670 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/liblz4.so.1.10.0 
│     │                 │                        ├ [1]: /usr/share/doc/liblz4-1/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/liblz4-1/copyright 
│     │                 ├ [61]  ╭ ID            : liblzma5@5.6.4-1ubuntu1 
│     │                 │       ├ Name          : liblzma5 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/liblzma5@5.6.4-1ubuntu1?arch=amd64&dist
│     │                 │       │                │       ro=ubuntu-25.04 
│     │                 │       │                ╰ UID : d23f8de3fb57473 
│     │                 │       ├ Version       : 5.6.4 
│     │                 │       ├ Release       : 1ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : xz-utils 
│     │                 │       ├ SrcVersion    : 5.6.4 
│     │                 │       ├ SrcRelease    : 1ubuntu1 
│     │                 │       ├ Licenses       ╭ [0] : 0BSD 
│     │                 │       │                ├ [1] : GPL-2.0-or-later 
│     │                 │       │                ├ [2] : LGPL-2.1-or-later 
│     │                 │       │                ├ [3] : FSFULLR 
│     │                 │       │                ├ [4] : GPL-3.0-or-later-WITH-Autoconf-exception-macro 
│     │                 │       │                ├ [5] : none 
│     │                 │       │                ├ [6] : PD 
│     │                 │       │                ├ [7] : permissive-nowarranty 
│     │                 │       │                ├ [8] : FSFUL 
│     │                 │       │                ├ [9] : noderivs 
│     │                 │       │                ├ [10]: PD-debian 
│     │                 │       │                ├ [11]: LGPL-2.1-only 
│     │                 │       │                ├ [12]: GPL-2.0-only 
│     │                 │       │                ╰ [13]: GPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:fa7e99a632c7ac55a3cb5f2d4fdf2252331cf9eaeba5138524a84f
│     │                 │       │                 b696babc14 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/liblzma.so.5.6.4 
│     │                 │                        ├ [1]: /usr/share/doc/liblzma5/AUTHORS 
│     │                 │                        ├ [2]: /usr/share/doc/liblzma5/NEWS.gz 
│     │                 │                        ├ [3]: /usr/share/doc/liblzma5/THANKS 
│     │                 │                        ├ [4]: /usr/share/doc/liblzma5/changelog.Debian.gz 
│     │                 │                        ╰ [5]: /usr/share/doc/liblzma5/copyright 
│     │                 ├ [62]  ╭ ID            : libmd0@1.1.0-2build2 
│     │                 │       ├ Name          : libmd0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libmd0@1.1.0-2build2?arch=amd64&distro=
│     │                 │       │                │       ubuntu-25.04 
│     │                 │       │                ╰ UID : 48f26379a8409df2 
│     │                 │       ├ Version       : 1.1.0 
│     │                 │       ├ Release       : 2build2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libmd 
│     │                 │       ├ SrcVersion    : 1.1.0 
│     │                 │       ├ SrcRelease    : 2build2 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ├ [1]: BSD-3-clause-Aaron-D-Gifford 
│     │                 │       │                ├ [2]: BSD-2-Clause 
│     │                 │       │                ├ [3]: BSD-2-Clause-NetBSD 
│     │                 │       │                ├ [4]: ISC 
│     │                 │       │                ├ [5]: Beerware 
│     │                 │       │                ├ [6]: public-domain-md4 
│     │                 │       │                ├ [7]: public-domain-md5 
│     │                 │       │                ╰ [8]: public-domain-sha1 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:34c52d5ed312415f5ec9f9450f3a58cf78096074631113a3e886ed
│     │                 │       │                 a163a3e99d 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libmd.so.0.1.0 
│     │                 │                        ├ [1]: /usr/share/doc/libmd0/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libmd0/copyright 
│     │                 ├ [63]  ╭ ID            : libmount1@2.40.2-14ubuntu1.1 
│     │                 │       ├ Name          : libmount1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libmount1@2.40.2-14ubuntu1.1?arch=amd64
│     │                 │       │                │       &distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 19ac325975df0d0f 
│     │                 │       ├ Version       : 2.40.2 
│     │                 │       ├ Release       : 14ubuntu1.1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : util-linux 
│     │                 │       ├ SrcVersion    : 2.40.2 
│     │                 │       ├ SrcRelease    : 14ubuntu1.1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-or-later 
│     │                 │       │                ├ [1] : GPL-2.0-only 
│     │                 │       │                ├ [2] : GPL-3.0-or-later 
│     │                 │       │                ├ [3] : LGPL-2.1-or-later 
│     │                 │       │                ├ [4] : public-domain 
│     │                 │       │                ├ [5] : BSD-4-Clause 
│     │                 │       │                ├ [6] : MIT 
│     │                 │       │                ├ [7] : ISC 
│     │                 │       │                ├ [8] : BSD-3-Clause 
│     │                 │       │                ├ [9] : BSLA 
│     │                 │       │                ├ [10]: LGPL-2.0-or-later 
│     │                 │       │                ├ [11]: BSD-2-Clause 
│     │                 │       │                ├ [12]: LGPL-3.0-or-later 
│     │                 │       │                ├ [13]: GPL-3.0-only 
│     │                 │       │                ├ [14]: LGPL-2.0-only 
│     │                 │       │                ├ [15]: LGPL-2.1-only 
│     │                 │       │                ╰ [16]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libblkid1@2.40.2-14ubuntu1.1 
│     │                 │       │                ├ [1]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [2]: libselinux1@3.7-3ubuntu3 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libmount.so.1.1.0 
│     │                 │                        ├ [1]: /usr/share/doc/libmount1/NEWS.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libmount1/changelog.Debian.gz 
│     │                 │                        ├ [3]: /usr/share/doc/libmount1/copyright 
│     │                 │                        ╰ [4]: /usr/share/lintian/overrides/libmount1 
│     │                 ├ [64]  ╭ ID            : libncursesw6@6.5+20250216-2 
│     │                 │       ├ Name          : libncursesw6 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libncursesw6@6.5%2B20250216-2?arch=amd6
│     │                 │       │                │       4&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : b875a9ab2eb98ce5 
│     │                 │       ├ Version       : 6.5+20250216 
│     │                 │       ├ Release       : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : ncurses 
│     │                 │       ├ SrcVersion    : 6.5+20250216 
│     │                 │       ├ SrcRelease    : 2 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libtinfo6@6.5+20250216-2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:ffdb4cd253e54c46e69ae39b24974cf45169d7dc377f5d78f911b7
│     │                 │       │                 bc67ef621f 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libformw.so.6.5 
│     │                 │                        ├ [1]: /usr/lib/x86_64-linux-gnu/libmenuw.so.6.5 
│     │                 │                        ├ [2]: /usr/lib/x86_64-linux-gnu/libncursesw.so.6.5 
│     │                 │                        ╰ [3]: /usr/lib/x86_64-linux-gnu/libpanelw.so.6.5 
│     │                 ├ [65]  ╭ ID            : libnettle8t64@3.10.1-1 
│     │                 │       ├ Name          : libnettle8t64 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libnettle8t64@3.10.1-1?arch=amd64&distr
│     │                 │       │                │       o=ubuntu-25.04 
│     │                 │       │                ╰ UID : 7222a4110219bbc1 
│     │                 │       ├ Version       : 3.10.1 
│     │                 │       ├ Release       : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : nettle 
│     │                 │       ├ SrcVersion    : 3.10.1 
│     │                 │       ├ SrcRelease    : 1 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-3.0-or-later 
│     │                 │       │                ├ [1]: GPL-2.0-or-later 
│     │                 │       │                ├ [2]: LGPL-2.0-or-later 
│     │                 │       │                ├ [3]: LGPL-2.0-only 
│     │                 │       │                ├ [4]: MIT 
│     │                 │       │                ├ [5]: GPL-3.0-with-autoconf-exception+ 
│     │                 │       │                ├ [6]: public-domain 
│     │                 │       │                ├ [7]: GPL-2.0-only 
│     │                 │       │                ╰ [8]: GAP 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libnettle.so.8.10 
│     │                 │                        ├ [1]: /usr/share/doc/libnettle8t64/NEWS.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libnettle8t64/README 
│     │                 │                        ├ [3]: /usr/share/doc/libnettle8t64/changelog.Debian.gz 
│     │                 │                        ├ [4]: /usr/share/doc/libnettle8t64/copyright 
│     │                 │                        ╰ [5]: /usr/share/lintian/overrides/libnettle8t64 
│     │                 ├ [66]  ╭ ID            : libnghttp2-14@1.64.0-1ubuntu1 
│     │                 │       ├ Name          : libnghttp2-14 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libnghttp2-14@1.64.0-1ubuntu1?arch=amd6
│     │                 │       │                │       4&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : ba14db7e848028cf 
│     │                 │       ├ Version       : 1.64.0 
│     │                 │       ├ Release       : 1ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : nghttp2 
│     │                 │       ├ SrcVersion    : 1.64.0 
│     │                 │       ├ SrcRelease    : 1ubuntu1 
│     │                 │       ├ Licenses       ╭ [0]: MIT 
│     │                 │       │                ├ [1]: all-permissive 
│     │                 │       │                ├ [2]: GPL-3.0-with-autoconf-exception+ 
│     │                 │       │                ├ [3]: BSD-2-Clause 
│     │                 │       │                ╰ [4]: GPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libnghttp2.so.14.28.3 
│     │                 │                        ├ [1]: /usr/share/doc/libnghttp2-14/AUTHORS 
│     │                 │                        ├ [2]: /usr/share/doc/libnghttp2-14/README.rst.gz 
│     │                 │                        ├ [3]: /usr/share/doc/libnghttp2-14/changelog.Debian.gz 
│     │                 │                        ╰ [4]: /usr/share/doc/libnghttp2-14/copyright 
│     │                 ├ [67]  ╭ ID            : libnpth0t64@1.8-2 
│     │                 │       ├ Name          : libnpth0t64 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libnpth0t64@1.8-2?arch=amd64&distro=ubu
│     │                 │       │                │       ntu-25.04 
│     │                 │       │                ╰ UID : 8fad15e1600a30e4 
│     │                 │       ├ Version       : 1.8 
│     │                 │       ├ Release       : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : npth 
│     │                 │       ├ SrcVersion    : 1.8 
│     │                 │       ├ SrcRelease    : 2 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-2.1-or-later 
│     │                 │       │                ╰ [1]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:fb56d7fda9ec4607560537a42a5bd8835ad9eae1e2c67568315503
│     │                 │       │                 442917a1ed 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libnpth.so.0.3.0 
│     │                 │                        ├ [1]: /usr/share/doc/libnpth0t64/changelog.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libnpth0t64/copyright 
│     │                 │                        ╰ [3]: /usr/share/lintian/overrides/libnpth0t64 
│     │                 ├ [68]  ╭ ID            : libp11-kit0@0.25.5-2ubuntu3 
│     │                 │       ├ Name          : libp11-kit0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libp11-kit0@0.25.5-2ubuntu3?arch=amd64&
│     │                 │       │                │       distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : c0866e91aa9b3423 
│     │                 │       ├ Version       : 0.25.5 
│     │                 │       ├ Release       : 2ubuntu3 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : p11-kit 
│     │                 │       ├ SrcVersion    : 0.25.5 
│     │                 │       ├ SrcRelease    : 2ubuntu3 
│     │                 │       ├ Licenses       ╭ [0] : BSD-3-Clause 
│     │                 │       │                ├ [1] : FSFULLR 
│     │                 │       │                ├ [2] : GPL-2+ with Autoconf-data exception 
│     │                 │       │                ├ [3] : GPL-3+ with Autoconf-data exception 
│     │                 │       │                ├ [4] : X11 
│     │                 │       │                ├ [5] : ISC 
│     │                 │       │                ├ [6] : customFSFULLRWD 
│     │                 │       │                ├ [7] : LGPL-2.1-or-later 
│     │                 │       │                ├ [8] : Apache-2.0 
│     │                 │       │                ├ [9] : customFSFUL 
│     │                 │       │                ├ [10]: FSFAP 
│     │                 │       │                ╰ [11]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libffi8@3.4.7-1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libp11-kit.so.0.4.1 
│     │                 │                        ├ [1]: /usr/share/doc/libp11-kit0/changelog.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libp11-kit0/copyright 
│     │                 │                        ╰ [3]: /usr/share/doc/libp11-kit0/examples/pkcs11.conf.example 
│     │                 ├ [69]  ╭ ID            : libpam-modules@1.5.3-7ubuntu4.4 
│     │                 │       ├ Name          : libpam-modules 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libpam-modules@1.5.3-7ubuntu4.4?arch=am
│     │                 │       │                │       d64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : c49554b6d433bfcd 
│     │                 │       ├ Version       : 1.5.3 
│     │                 │       ├ Release       : 7ubuntu4.4 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : pam 
│     │                 │       ├ SrcVersion    : 1.5.3 
│     │                 │       ├ SrcRelease    : 7ubuntu4.4 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ├ [1]: GPL-2.0-or-later 
│     │                 │       │                ├ [2]: GPL-2.0-only 
│     │                 │       │                ├ [3]: GPL-3.0-only 
│     │                 │       │                ├ [4]: GPL-3+ with Bison exception 
│     │                 │       │                ├ [5]: BSD-tcp_wrappers 
│     │                 │       │                ├ [6]: LGPL-2.0-or-later 
│     │                 │       │                ├ [7]: LGPL-2.0-only 
│     │                 │       │                ├ [8]: public-domain 
│     │                 │       │                ╰ [9]: Beerware 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/lib/x86_64-linux-gnu/security/pam_access.so 
│     │                 │                        ├ [1]  : /usr/lib/x86_64-linux-gnu/security/pam_debug.so 
│     │                 │                        ├ [2]  : /usr/lib/x86_64-linux-gnu/security/pam_deny.so 
│     │                 │                        ├ [3]  : /usr/lib/x86_64-linux-gnu/security/pam_echo.so 
│     │                 │                        ├ [4]  : /usr/lib/x86_64-linux-gnu/security/pam_env.so 
│     │                 │                        ├ [5]  : /usr/lib/x86_64-linux-gnu/security/pam_exec.so 
│     │                 │                        ├ [6]  : /usr/lib/x86_64-linux-gnu/security/pam_extrausers.so 
│     │                 │                        ├ [7]  : /usr/lib/x86_64-linux-gnu/security/pam_faildelay.so 
│     │                 │                        ├ [8]  : /usr/lib/x86_64-linux-gnu/security/pam_faillock.so 
│     │                 │                        ├ [9]  : /usr/lib/x86_64-linux-gnu/security/pam_filter.so 
│     │                 │                        ├ [10] : /usr/lib/x86_64-linux-gnu/security/pam_ftp.so 
│     │                 │                        ├ [11] : /usr/lib/x86_64-linux-gnu/security/pam_group.so 
│     │                 │                        ├ [12] : /usr/lib/x86_64-linux-gnu/security/pam_issue.so 
│     │                 │                        ├ [13] : /usr/lib/x86_64-linux-gnu/security/pam_keyinit.so 
│     │                 │                        ├ [14] : /usr/lib/x86_64-linux-gnu/security/pam_limits.so 
│     │                 │                        ├ [15] : /usr/lib/x86_64-linux-gnu/security/pam_listfile.so 
│     │                 │                        ├ [16] : /usr/lib/x86_64-linux-gnu/security/pam_localuser.so 
│     │                 │                        ├ [17] : /usr/lib/x86_64-linux-gnu/security/pam_loginuid.so 
│     │                 │                        ├ [18] : /usr/lib/x86_64-linux-gnu/security/pam_mail.so 
│     │                 │                        ├ [19] : /usr/lib/x86_64-linux-gnu/security/pam_mkhomedir.so 
│     │                 │                        ├ [20] : /usr/lib/x86_64-linux-gnu/security/pam_motd.so 
│     │                 │                        ├ [21] : /usr/lib/x86_64-linux-gnu/security/pam_namespace.so 
│     │                 │                        ├ [22] : /usr/lib/x86_64-linux-gnu/security/pam_nologin.so 
│     │                 │                        ├ [23] : /usr/lib/x86_64-linux-gnu/security/pam_permit.so 
│     │                 │                        ├ [24] : /usr/lib/x86_64-linux-gnu/security/pam_pwhistory.so 
│     │                 │                        ├ [25] : /usr/lib/x86_64-linux-gnu/security/pam_rhosts.so 
│     │                 │                        ├ [26] : /usr/lib/x86_64-linux-gnu/security/pam_rootok.so 
│     │                 │                        ├ [27] : /usr/lib/x86_64-linux-gnu/security/pam_securetty.so 
│     │                 │                        ├ [28] : /usr/lib/x86_64-linux-gnu/security/pam_selinux.so 
│     │                 │                        ├ [29] : /usr/lib/x86_64-linux-gnu/security/pam_sepermit.so 
│     │                 │                        ├ [30] : /usr/lib/x86_64-linux-gnu/security/pam_setquota.so 
│     │                 │                        ├ [31] : /usr/lib/x86_64-linux-gnu/security/pam_shells.so 
│     │                 │                        ├ [32] : /usr/lib/x86_64-linux-gnu/security/pam_stress.so 
│     │                 │                        ├ [33] : /usr/lib/x86_64-linux-gnu/security/pam_succeed_if.so 
│     │                 │                        ├ [34] : /usr/lib/x86_64-linux-gnu/security/pam_time.so 
│     │                 │                        ├ [35] : /usr/lib/x86_64-linux-gnu/security/pam_timestamp.so 
│     │                 │                        ├ [36] : /usr/lib/x86_64-linux-gnu/security/pam_tty_audit.so 
│     │                 │                        ├ [37] : /usr/lib/x86_64-linux-gnu/security/pam_umask.so 
│     │                 │                        ├ [38] : /usr/lib/x86_64-linux-gnu/security/pam_unix.so 
│     │                 │                        ├ [39] : /usr/lib/x86_64-linux-gnu/security/pam_userdb.so 
│     │                 │                        ├ [40] : /usr/lib/x86_64-linux-gnu/security/pam_usertype.so 
│     │                 │                        ├ [41] : /usr/lib/x86_64-linux-gnu/security/pam_warn.so 
│     │                 │                        ├ [42] : /usr/lib/x86_64-linux-gnu/security/pam_wheel.so 
│     │                 │                        ├ [43] : /usr/lib/x86_64-linux-gnu/security/pam_xauth.so 
│     │                 │                        ├ [44] : /usr/share/doc/libpam-modules/NEWS.Debian.gz 
│     │                 │                        ├ [45] : /usr/share/doc/libpam-modules/copyright 
│     │                 │                        ├ [46] : /usr/share/doc/libpam-modules/examples/upperLOWER.c 
│     │                 │                        ├ [47] : /usr/share/lintian/overrides/libpam-modules 
│     │                 │                        ├ [48] : /usr/share/man/man5/access.conf.5.gz 
│     │                 │                        ├ [49] : /usr/share/man/man5/faillock.conf.5.gz 
│     │                 │                        ├ [50] : /usr/share/man/man5/group.conf.5.gz 
│     │                 │                        ├ [51] : /usr/share/man/man5/limits.conf.5.gz 
│     │                 │                        ├ [52] : /usr/share/man/man5/namespace.conf.5.gz 
│     │                 │                        ├ [53] : /usr/share/man/man5/pam_env.conf.5.gz 
│     │                 │                        ├ [54] : /usr/share/man/man5/pwhistory.conf.5.gz 
│     │                 │                        ├ [55] : /usr/share/man/man5/sepermit.conf.5.gz 
│     │                 │                        ├ [56] : /usr/share/man/man5/time.conf.5.gz 
│     │                 │                        ├ [57] : /usr/share/man/man5/update-motd.5.gz 
│     │                 │                        ├ [58] : /usr/share/man/man8/pam_access.8.gz 
│     │                 │                        ├ [59] : /usr/share/man/man8/pam_debug.8.gz 
│     │                 │                        ├ [60] : /usr/share/man/man8/pam_deny.8.gz 
│     │                 │                        ├ [61] : /usr/share/man/man8/pam_echo.8.gz 
│     │                 │                        ├ [62] : /usr/share/man/man8/pam_env.8.gz 
│     │                 │                        ├ [63] : /usr/share/man/man8/pam_exec.8.gz 
│     │                 │                        ├ [64] : /usr/share/man/man8/pam_extrausers.8.gz 
│     │                 │                        ├ [65] : /usr/share/man/man8/pam_faildelay.8.gz 
│     │                 │                        ├ [66] : /usr/share/man/man8/pam_faillock.8.gz 
│     │                 │                        ├ [67] : /usr/share/man/man8/pam_filter.8.gz 
│     │                 │                        ├ [68] : /usr/share/man/man8/pam_ftp.8.gz 
│     │                 │                        ├ [69] : /usr/share/man/man8/pam_group.8.gz 
│     │                 │                        ├ [70] : /usr/share/man/man8/pam_issue.8.gz 
│     │                 │                        ├ [71] : /usr/share/man/man8/pam_keyinit.8.gz 
│     │                 │                        ├ [72] : /usr/share/man/man8/pam_limits.8.gz 
│     │                 │                        ├ [73] : /usr/share/man/man8/pam_listfile.8.gz 
│     │                 │                        ├ [74] : /usr/share/man/man8/pam_localuser.8.gz 
│     │                 │                        ├ [75] : /usr/share/man/man8/pam_loginuid.8.gz 
│     │                 │                        ├ [76] : /usr/share/man/man8/pam_mail.8.gz 
│     │                 │                        ├ [77] : /usr/share/man/man8/pam_mkhomedir.8.gz 
│     │                 │                        ├ [78] : /usr/share/man/man8/pam_motd.8.gz 
│     │                 │                        ├ [79] : /usr/share/man/man8/pam_namespace.8.gz 
│     │                 │                        ├ [80] : /usr/share/man/man8/pam_nologin.8.gz 
│     │                 │                        ├ [81] : /usr/share/man/man8/pam_permit.8.gz 
│     │                 │                        ├ [82] : /usr/share/man/man8/pam_pwhistory.8.gz 
│     │                 │                        ├ [83] : /usr/share/man/man8/pam_rhosts.8.gz 
│     │                 │                        ├ [84] : /usr/share/man/man8/pam_rootok.8.gz 
│     │                 │                        ├ [85] : /usr/share/man/man8/pam_securetty.8.gz 
│     │                 │                        ├ [86] : /usr/share/man/man8/pam_selinux.8.gz 
│     │                 │                        ├ [87] : /usr/share/man/man8/pam_sepermit.8.gz 
│     │                 │                        ├ [88] : /usr/share/man/man8/pam_setquota.8.gz 
│     │                 │                        ├ [89] : /usr/share/man/man8/pam_shells.8.gz 
│     │                 │                        ├ [90] : /usr/share/man/man8/pam_stress.8.gz 
│     │                 │                        ├ [91] : /usr/share/man/man8/pam_succeed_if.8.gz 
│     │                 │                        ├ [92] : /usr/share/man/man8/pam_time.8.gz 
│     │                 │                        ├ [93] : /usr/share/man/man8/pam_timestamp.8.gz 
│     │                 │                        ├ [94] : /usr/share/man/man8/pam_tty_audit.8.gz 
│     │                 │                        ├ [95] : /usr/share/man/man8/pam_umask.8.gz 
│     │                 │                        ├ [96] : /usr/share/man/man8/pam_unix.8.gz 
│     │                 │                        ├ [97] : /usr/share/man/man8/pam_userdb.8.gz 
│     │                 │                        ├ [98] : /usr/share/man/man8/pam_usertype.8.gz 
│     │                 │                        ├ [99] : /usr/share/man/man8/pam_warn.8.gz 
│     │                 │                        ├ [100]: /usr/share/man/man8/pam_wheel.8.gz 
│     │                 │                        ├ [101]: /usr/share/man/man8/pam_xauth.8.gz 
│     │                 │                        ╰ [102]: /usr/share/pam-configs/mkhomedir 
│     │                 ├ [70]  ╭ ID            : libpam-modules-bin@1.5.3-7ubuntu4.4 
│     │                 │       ├ Name          : libpam-modules-bin 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libpam-modules-bin@1.5.3-7ubuntu4.4?arc
│     │                 │       │                │       h=amd64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 5357e0bb8a1ff079 
│     │                 │       ├ Version       : 1.5.3 
│     │                 │       ├ Release       : 7ubuntu4.4 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : pam 
│     │                 │       ├ SrcVersion    : 1.5.3 
│     │                 │       ├ SrcRelease    : 7ubuntu4.4 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ├ [1]: GPL-2.0-or-later 
│     │                 │       │                ├ [2]: GPL-2.0-only 
│     │                 │       │                ├ [3]: GPL-3.0-only 
│     │                 │       │                ├ [4]: GPL-3+ with Bison exception 
│     │                 │       │                ├ [5]: BSD-tcp_wrappers 
│     │                 │       │                ├ [6]: LGPL-2.0-or-later 
│     │                 │       │                ├ [7]: LGPL-2.0-only 
│     │                 │       │                ├ [8]: public-domain 
│     │                 │       │                ╰ [9]: Beerware 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libaudit1@1:4.0.2-2ubuntu2 
│     │                 │       │                ├ [1]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [2]: libcrypt1@1:4.4.38-1 
│     │                 │       │                ├ [3]: libpam0g@1.5.3-7ubuntu4.4 
│     │                 │       │                ├ [4]: libselinux1@3.7-3ubuntu3 
│     │                 │       │                ╰ [5]: libsystemd0@257.4-1ubuntu3.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/lib/systemd/system/pam_namespace.service 
│     │                 │                        ├ [1] : /usr/sbin/faillock 
│     │                 │                        ├ [2] : /usr/sbin/mkhomedir_helper 
│     │                 │                        ├ [3] : /usr/sbin/pam_extrausers_chkpwd 
│     │                 │                        ├ [4] : /usr/sbin/pam_extrausers_update 
│     │                 │                        ├ [5] : /usr/sbin/pam_namespace_helper 
│     │                 │                        ├ [6] : /usr/sbin/pam_timestamp_check 
│     │                 │                        ├ [7] : /usr/sbin/pwhistory_helper 
│     │                 │                        ├ [8] : /usr/sbin/unix_chkpwd 
│     │                 │                        ├ [9] : /usr/sbin/unix_update 
│     │                 │                        ├ [10]: /usr/share/doc/libpam-modules-bin/copyright 
│     │                 │                        ├ [11]: /usr/share/lintian/overrides/libpam-modules-bin 
│     │                 │                        ├ [12]: /usr/share/man/man5/environment.5.gz 
│     │                 │                        ├ [13]: /usr/share/man/man8/faillock.8.gz 
│     │                 │                        ├ [14]: /usr/share/man/man8/mkhomedir_helper.8.gz 
│     │                 │                        ├ [15]: /usr/share/man/man8/pam_namespace_helper.8.gz 
│     │                 │                        ├ [16]: /usr/share/man/man8/pam_timestamp_check.8.gz 
│     │                 │                        ├ [17]: /usr/share/man/man8/pwhistory_helper.8.gz 
│     │                 │                        ├ [18]: /usr/share/man/man8/unix_chkpwd.8.gz 
│     │                 │                        ╰ [19]: /usr/share/man/man8/unix_update.8.gz 
│     │                 ├ [71]  ╭ ID            : libpam-runtime@1.5.3-7ubuntu4.4 
│     │                 │       ├ Name          : libpam-runtime 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libpam-runtime@1.5.3-7ubuntu4.4?arch=al
│     │                 │       │                │       l&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : ff7c6fc616e7055b 
│     │                 │       ├ Version       : 1.5.3 
│     │                 │       ├ Release       : 7ubuntu4.4 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : pam 
│     │                 │       ├ SrcVersion    : 1.5.3 
│     │                 │       ├ SrcRelease    : 7ubuntu4.4 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ├ [1]: GPL-2.0-or-later 
│     │                 │       │                ├ [2]: GPL-2.0-only 
│     │                 │       │                ├ [3]: GPL-3.0-only 
│     │                 │       │                ├ [4]: GPL-3+ with Bison exception 
│     │                 │       │                ├ [5]: BSD-tcp_wrappers 
│     │                 │       │                ├ [6]: LGPL-2.0-or-later 
│     │                 │       │                ├ [7]: LGPL-2.0-only 
│     │                 │       │                ├ [8]: public-domain 
│     │                 │       │                ╰ [9]: Beerware 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: debconf@1.5.87ubuntu1 
│     │                 │       │                ╰ [1]: libpam-modules@1.5.3-7ubuntu4.4 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/sbin/pam-auth-update 
│     │                 │                        ├ [1] : /usr/sbin/pam_getenv 
│     │                 │                        ├ [2] : /usr/share/doc/libpam-runtime/copyright 
│     │                 │                        ├ [3] : /usr/share/lintian/overrides/libpam-runtime 
│     │                 │                        ├ [4] : /usr/share/man/man5/pam.conf.5.gz 
│     │                 │                        ├ [5] : /usr/share/man/man7/PAM.7.gz 
│     │                 │                        ├ [6] : /usr/share/man/man8/pam-auth-update.8.gz 
│     │                 │                        ├ [7] : /usr/share/man/man8/pam_getenv.8.gz 
│     │                 │                        ├ [8] : /usr/share/pam-configs/unix 
│     │                 │                        ├ [9] : /usr/share/pam/common-account 
│     │                 │                        ├ [10]: /usr/share/pam/common-account.md5sums 
│     │                 │                        ├ [11]: /usr/share/pam/common-auth 
│     │                 │                        ├ [12]: /usr/share/pam/common-auth.md5sums 
│     │                 │                        ├ [13]: /usr/share/pam/common-password 
│     │                 │                        ├ [14]: /usr/share/pam/common-password.md5sums 
│     │                 │                        ├ [15]: /usr/share/pam/common-session 
│     │                 │                        ├ [16]: /usr/share/pam/common-session-noninteractive 
│     │                 │                        ├ [17]: /usr/share/pam/common-session-noninteractive.md5sums 
│     │                 │                        ╰ [18]: /usr/share/pam/common-session.md5sums 
│     │                 ├ [72]  ╭ ID            : libpam0g@1.5.3-7ubuntu4.4 
│     │                 │       ├ Name          : libpam0g 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libpam0g@1.5.3-7ubuntu4.4?arch=amd64&di
│     │                 │       │                │       stro=ubuntu-25.04 
│     │                 │       │                ╰ UID : e7da9492a7d7e6e9 
│     │                 │       ├ Version       : 1.5.3 
│     │                 │       ├ Release       : 7ubuntu4.4 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : pam 
│     │                 │       ├ SrcVersion    : 1.5.3 
│     │                 │       ├ SrcRelease    : 7ubuntu4.4 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ├ [1]: GPL-2.0-or-later 
│     │                 │       │                ├ [2]: GPL-2.0-only 
│     │                 │       │                ├ [3]: GPL-3.0-only 
│     │                 │       │                ├ [4]: GPL-3+ with Bison exception 
│     │                 │       │                ├ [5]: BSD-tcp_wrappers 
│     │                 │       │                ├ [6]: LGPL-2.0-or-later 
│     │                 │       │                ├ [7]: LGPL-2.0-only 
│     │                 │       │                ├ [8]: public-domain 
│     │                 │       │                ╰ [9]: Beerware 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: debconf@1.5.87ubuntu1 
│     │                 │       │                ├ [1]: libaudit1@1:4.0.2-2ubuntu2 
│     │                 │       │                ╰ [2]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libpam.so.0.85.1 
│     │                 │                        ├ [1]: /usr/lib/x86_64-linux-gnu/libpam_misc.so.0.82.1 
│     │                 │                        ├ [2]: /usr/lib/x86_64-linux-gnu/libpamc.so.0.82.1 
│     │                 │                        ├ [3]: /usr/share/doc/libpam0g/Debian-PAM-MiniPolicy.gz 
│     │                 │                        ├ [4]: /usr/share/doc/libpam0g/README 
│     │                 │                        ├ [5]: /usr/share/doc/libpam0g/README.Debian 
│     │                 │                        ├ [6]: /usr/share/doc/libpam0g/TODO.Debian 
│     │                 │                        ├ [7]: /usr/share/doc/libpam0g/changelog.Debian.gz 
│     │                 │                        ├ [8]: /usr/share/doc/libpam0g/copyright 
│     │                 │                        ╰ [9]: /usr/share/lintian/overrides/libpam0g 
│     │                 ├ [73]  ╭ ID            : libpcre2-8-0@10.45-1ubuntu0.1 
│     │                 │       ├ Name          : libpcre2-8-0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libpcre2-8-0@10.45-1ubuntu0.1?arch=amd6
│     │                 │       │                │       4&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 5f702b23e1c9e833 
│     │                 │       ├ Version       : 10.45 
│     │                 │       ├ Release       : 1ubuntu0.1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : pcre2 
│     │                 │       ├ SrcVersion    : 10.45 
│     │                 │       ├ SrcRelease    : 1ubuntu0.1 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-clause-Cambridge with BINARY LIBRARY-LIKE
│     │                 │       │                │      PACKAGES exception 
│     │                 │       │                ├ [1]: BSD-3-Clause 
│     │                 │       │                ├ [2]: X11 
│     │                 │       │                ├ [3]: BSD-2-Clause 
│     │                 │       │                ╰ [4]: public-domain 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libpcre2-8.so.0.14.0 
│     │                 │                        ├ [1]: /usr/share/doc/libpcre2-8-0/README.Debian 
│     │                 │                        ├ [2]: /usr/share/doc/libpcre2-8-0/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/libpcre2-8-0/copyright 
│     │                 ├ [74]  ╭ ID            : libproc2-0@2:4.0.4-7ubuntu1 
│     │                 │       ├ Name          : libproc2-0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libproc2-0@4.0.4-7ubuntu1?arch=amd64&di
│     │                 │       │                │       stro=ubuntu-25.04&epoch=2 
│     │                 │       │                ╰ UID : 625a043de7cedfa3 
│     │                 │       ├ Version       : 4.0.4 
│     │                 │       ├ Release       : 7ubuntu1 
│     │                 │       ├ Epoch         : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : procps 
│     │                 │       ├ SrcVersion    : 4.0.4 
│     │                 │       ├ SrcRelease    : 7ubuntu1 
│     │                 │       ├ SrcEpoch      : 2 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-2.1-or-later 
│     │                 │       │                ├ [1]: LGPL-2.0-or-later 
│     │                 │       │                ├ [2]: GPL-2.0-or-later 
│     │                 │       │                ├ [3]: GPL-2.0-only 
│     │                 │       │                ├ [4]: LGPL-2.0-only 
│     │                 │       │                ╰ [5]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libsystemd0@257.4-1ubuntu3.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:bea02cf36d107f9ee39a7752ea55b5aed19443652dd34864f18714
│     │                 │       │                 f75dcf1b37 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libproc2.so.0.0.2 
│     │                 │                        ├ [1]: /usr/share/doc/libproc2-0/NEWS.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libproc2-0/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/libproc2-0/copyright 
│     │                 ├ [75]  ╭ ID            : libpsl5t64@0.21.2-1.1build1 
│     │                 │       ├ Name          : libpsl5t64 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libpsl5t64@0.21.2-1.1build1?arch=amd64&
│     │                 │       │                │       distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : bbca01e905467da9 
│     │                 │       ├ Version       : 0.21.2 
│     │                 │       ├ Release       : 1.1build1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libpsl 
│     │                 │       ├ SrcVersion    : 0.21.2 
│     │                 │       ├ SrcRelease    : 1.1build1 
│     │                 │       ├ Licenses       ╭ [0]: MIT 
│     │                 │       │                ├ [1]: gnulib 
│     │                 │       │                ╰ [2]: Chromium 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [1]: libidn2-0@2.3.8-2 
│     │                 │       │                ╰ [2]: libunistring5@1.3-1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libpsl.so.5.3.4 
│     │                 │                        ├ [1]: /usr/share/doc/libpsl5t64/changelog.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libpsl5t64/copyright 
│     │                 │                        ╰ [3]: /usr/share/lintian/overrides/libpsl5t64 
│     │                 ├ [76]  ╭ ID            : librtmp1@2.4+20151223.gitfa8646d.1-2build7 
│     │                 │       ├ Name          : librtmp1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/librtmp1@2.4%2B20151223.gitfa8646d.1-2b
│     │                 │       │                │       uild7?arch=amd64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 3eaa4c312c598b1b 
│     │                 │       ├ Version       : 2.4+20151223.gitfa8646d.1 
│     │                 │       ├ Release       : 2build7 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : rtmpdump 
│     │                 │       ├ SrcVersion    : 2.4+20151223.gitfa8646d.1 
│     │                 │       ├ SrcRelease    : 2build7 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-only 
│     │                 │       │                ╰ [1]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [1]: libgmp10@2:6.3.0+dfsg-3ubuntu1 
│     │                 │       │                ╰ [2]: zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/librtmp.so.1 
│     │                 │                        ├ [1]: /usr/share/doc/librtmp1/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/librtmp1/copyright 
│     │                 ├ [77]  ╭ ID            : libsasl2-2@2.1.28+dfsg1-9 
│     │                 │       ├ Name          : libsasl2-2 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libsasl2-2@2.1.28%2Bdfsg1-9?arch=amd64&
│     │                 │       │                │       distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 3cc26aeeb7a28ca9 
│     │                 │       ├ Version       : 2.1.28+dfsg1 
│     │                 │       ├ Release       : 9 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : cyrus-sasl2 
│     │                 │       ├ SrcVersion    : 2.1.28+dfsg1 
│     │                 │       ├ SrcRelease    : 9 
│     │                 │       ├ Licenses       ╭ [0] : BSD-3-Clause-Attribution 
│     │                 │       │                ├ [1] : BSD-3-Clause 
│     │                 │       │                ├ [2] : BSD-2-Clause 
│     │                 │       │                ├ [3] : GPL-3.0-or-later 
│     │                 │       │                ├ [4] : GPL-3.0-only 
│     │                 │       │                ├ [5] : BSD-4-Clause-UC 
│     │                 │       │                ├ [6] : RSA-MD 
│     │                 │       │                ├ [7] : text://BSD-3-Clause-Attribution and IBM-as-is 
│     │                 │       │                ├ [8] : BSD-3-clause-JANET 
│     │                 │       │                ├ [9] : BSD-3-clause-PADL 
│     │                 │       │                ├ [10]: MIT-OpenVision 
│     │                 │       │                ├ [11]: OpenLDAP 
│     │                 │       │                ├ [12]: FSFULLR 
│     │                 │       │                ├ [13]: MIT-CMU 
│     │                 │       │                ├ [14]: MIT-Export 
│     │                 │       │                ├ [15]: BSD-2.2-clause 
│     │                 │       │                ╰ [16]: text://IBM-as-is 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [1]: libsasl2-modules-db@2.1.28+dfsg1-9 
│     │                 │       │                ╰ [2]: libssl3t64@3.4.1-1ubuntu4 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libsasl2.so.2.0.25 
│     │                 │                        ├ [1]: /usr/share/doc/libsasl2-2/README.Debian 
│     │                 │                        ├ [2]: /usr/share/doc/libsasl2-2/copyright 
│     │                 │                        ╰ [3]: /usr/share/man/man5/libsasl.5.gz 
│     │                 ├ [78]  ╭ ID            : libsasl2-modules@2.1.28+dfsg1-9 
│     │                 │       ├ Name          : libsasl2-modules 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libsasl2-modules@2.1.28%2Bdfsg1-9?arch=
│     │                 │       │                │       amd64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : ae58d504bfc5a3fe 
│     │                 │       ├ Version       : 2.1.28+dfsg1 
│     │                 │       ├ Release       : 9 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : cyrus-sasl2 
│     │                 │       ├ SrcVersion    : 2.1.28+dfsg1 
│     │                 │       ├ SrcRelease    : 9 
│     │                 │       ├ Licenses       ╭ [0] : BSD-3-Clause-Attribution 
│     │                 │       │                ├ [1] : BSD-3-Clause 
│     │                 │       │                ├ [2] : BSD-2-Clause 
│     │                 │       │                ├ [3] : GPL-3.0-or-later 
│     │                 │       │                ├ [4] : GPL-3.0-only 
│     │                 │       │                ├ [5] : BSD-4-Clause-UC 
│     │                 │       │                ├ [6] : RSA-MD 
│     │                 │       │                ├ [7] : text://BSD-3-Clause-Attribution and IBM-as-is 
│     │                 │       │                ├ [8] : BSD-3-clause-JANET 
│     │                 │       │                ├ [9] : BSD-3-clause-PADL 
│     │                 │       │                ├ [10]: MIT-OpenVision 
│     │                 │       │                ├ [11]: OpenLDAP 
│     │                 │       │                ├ [12]: FSFULLR 
│     │                 │       │                ├ [13]: MIT-CMU 
│     │                 │       │                ├ [14]: MIT-Export 
│     │                 │       │                ├ [15]: BSD-2.2-clause 
│     │                 │       │                ╰ [16]: text://IBM-as-is 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libssl3t64@3.4.1-1ubuntu4 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/sasl2/libanonymous.so.2.0.25 
│     │                 │                        ├ [1]: /usr/lib/x86_64-linux-gnu/sasl2/libcrammd5.so.2.0.25 
│     │                 │                        ├ [2]: /usr/lib/x86_64-linux-gnu/sasl2/libdigestmd5.so.2.0.25 
│     │                 │                        ├ [3]: /usr/lib/x86_64-linux-gnu/sasl2/liblogin.so.2.0.25 
│     │                 │                        ├ [4]: /usr/lib/x86_64-linux-gnu/sasl2/libntlm.so.2.0.25 
│     │                 │                        ├ [5]: /usr/lib/x86_64-linux-gnu/sasl2/libplain.so.2.0.25 
│     │                 │                        ├ [6]: /usr/lib/x86_64-linux-gnu/sasl2/libscram.so.2.0.25 
│     │                 │                        ├ [7]: /usr/share/doc/libsasl2-modules/changelog.Debian.gz 
│     │                 │                        ╰ [8]: /usr/share/doc/libsasl2-modules/copyright 
│     │                 ├ [79]  ╭ ID            : libsasl2-modules-db@2.1.28+dfsg1-9 
│     │                 │       ├ Name          : libsasl2-modules-db 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libsasl2-modules-db@2.1.28%2Bdfsg1-9?ar
│     │                 │       │                │       ch=amd64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 335fd847927b84b1 
│     │                 │       ├ Version       : 2.1.28+dfsg1 
│     │                 │       ├ Release       : 9 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : cyrus-sasl2 
│     │                 │       ├ SrcVersion    : 2.1.28+dfsg1 
│     │                 │       ├ SrcRelease    : 9 
│     │                 │       ├ Licenses       ╭ [0] : BSD-3-Clause-Attribution 
│     │                 │       │                ├ [1] : BSD-3-Clause 
│     │                 │       │                ├ [2] : BSD-2-Clause 
│     │                 │       │                ├ [3] : GPL-3.0-or-later 
│     │                 │       │                ├ [4] : GPL-3.0-only 
│     │                 │       │                ├ [5] : BSD-4-Clause-UC 
│     │                 │       │                ├ [6] : RSA-MD 
│     │                 │       │                ├ [7] : text://BSD-3-Clause-Attribution and IBM-as-is 
│     │                 │       │                ├ [8] : BSD-3-clause-JANET 
│     │                 │       │                ├ [9] : BSD-3-clause-PADL 
│     │                 │       │                ├ [10]: MIT-OpenVision 
│     │                 │       │                ├ [11]: OpenLDAP 
│     │                 │       │                ├ [12]: FSFULLR 
│     │                 │       │                ├ [13]: MIT-CMU 
│     │                 │       │                ├ [14]: MIT-Export 
│     │                 │       │                ├ [15]: BSD-2.2-clause 
│     │                 │       │                ╰ [16]: text://IBM-as-is 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libdb5.3t64@5.3.28+dfsg2-9 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/sasl2/libsasldb.so.2.0.25 
│     │                 │                        ├ [1]: /usr/share/doc/libsasl2-modules-db/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libsasl2-modules-db/copyright 
│     │                 ├ [80]  ╭ ID            : libseccomp2@2.5.5-1ubuntu6 
│     │                 │       ├ Name          : libseccomp2 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libseccomp2@2.5.5-1ubuntu6?arch=amd64&d
│     │                 │       │                │       istro=ubuntu-25.04 
│     │                 │       │                ╰ UID : c3e4836a2283c77e 
│     │                 │       ├ Version       : 2.5.5 
│     │                 │       ├ Release       : 1ubuntu6 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libseccomp 
│     │                 │       ├ SrcVersion    : 2.5.5 
│     │                 │       ├ SrcRelease    : 1ubuntu6 
│     │                 │       ├ Licenses       ─ [0]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:b45d1790efbb416a4e9a81705937477c3fdcc61f104e66ca7c9b8e
│     │                 │       │                 beaf3d2646 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libseccomp.so.2.5.5 
│     │                 │                        ├ [1]: /usr/share/doc/libseccomp2/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libseccomp2/copyright 
│     │                 ├ [81]  ╭ ID            : libselinux1@3.7-3ubuntu3 
│     │                 │       ├ Name          : libselinux1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libselinux1@3.7-3ubuntu3?arch=amd64&dis
│     │                 │       │                │       tro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 3677fb0a207d595e 
│     │                 │       ├ Version       : 3.7 
│     │                 │       ├ Release       : 3ubuntu3 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libselinux 
│     │                 │       ├ SrcVersion    : 3.7 
│     │                 │       ├ SrcRelease    : 3ubuntu3 
│     │                 │       ├ Licenses       ╭ [0]: public-domain 
│     │                 │       │                ╰ [1]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libpcre2-8-0@10.45-1ubuntu0.1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:b483c61b534ec5aec6ad338a4cdf1c4727f561833033e8aebee644
│     │                 │       │                 2f2127c57b 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/tmpfiles.d/libselinux1.conf 
│     │                 │                        ├ [1]: /usr/lib/x86_64-linux-gnu/libselinux.so.1 
│     │                 │                        ├ [2]: /usr/share/doc/libselinux1/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/libselinux1/copyright 
│     │                 ├ [82]  ╭ ID            : libsemanage-common@3.7-2.1build1 
│     │                 │       ├ Name          : libsemanage-common 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libsemanage-common@3.7-2.1build1?arch=a
│     │                 │       │                │       ll&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 841923b6fc294ad3 
│     │                 │       ├ Version       : 3.7 
│     │                 │       ├ Release       : 2.1build1 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : libsemanage 
│     │                 │       ├ SrcVersion    : 3.7 
│     │                 │       ├ SrcRelease    : 2.1build1 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-2.1-or-later 
│     │                 │       │                ├ [1]: LGPL-2.1-only 
│     │                 │       │                ╰ [2]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:bea8cc2210a943dcbfd66ca4fe94356b413ab2f238a91b7f2c51e0
│     │                 │       │                 c91df99d7e 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/share/doc/libsemanage-common/changelog.Debian.gz 
│     │                 │                        ├ [1]: /usr/share/doc/libsemanage-common/copyright 
│     │                 │                        ╰ [2]: /usr/share/man/man5/semanage.conf.5.gz 
│     │                 ├ [83]  ╭ ID            : libsemanage2@3.7-2.1build1 
│     │                 │       ├ Name          : libsemanage2 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libsemanage2@3.7-2.1build1?arch=amd64&d
│     │                 │       │                │       istro=ubuntu-25.04 
│     │                 │       │                ╰ UID : a33f0dffb5dbac06 
│     │                 │       ├ Version       : 3.7 
│     │                 │       ├ Release       : 2.1build1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libsemanage 
│     │                 │       ├ SrcVersion    : 3.7 
│     │                 │       ├ SrcRelease    : 2.1build1 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-2.1-or-later 
│     │                 │       │                ├ [1]: LGPL-2.1-only 
│     │                 │       │                ╰ [2]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libaudit1@1:4.0.2-2ubuntu2 
│     │                 │       │                ├ [1]: libbz2-1.0@1.0.8-6 
│     │                 │       │                ├ [2]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [3]: libselinux1@3.7-3ubuntu3 
│     │                 │       │                ├ [4]: libsemanage-common@3.7-2.1build1 
│     │                 │       │                ╰ [5]: libsepol2@3.7-1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:426b3aad6a9e3766030683077d921d34a57f0edd33a0ef0fc1fcdd
│     │                 │       │                 928f845852 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libsemanage.so.2 
│     │                 │                        ├ [1]: /usr/share/doc/libsemanage2/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libsemanage2/copyright 
│     │                 ├ [84]  ╭ ID            : libsepol2@3.7-1 
│     │                 │       ├ Name          : libsepol2 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libsepol2@3.7-1?arch=amd64&distro=ubunt
│     │                 │       │                │       u-25.04 
│     │                 │       │                ╰ UID : 93b67d3f42dddfe6 
│     │                 │       ├ Version       : 3.7 
│     │                 │       ├ Release       : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libsepol 
│     │                 │       ├ SrcVersion    : 3.7 
│     │                 │       ├ SrcRelease    : 1 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-2.1-or-later 
│     │                 │       │                ├ [1]: LGPL-2.1-only 
│     │                 │       │                ├ [2]: Zlib 
│     │                 │       │                ├ [3]: GPL-2.0-only 
│     │                 │       │                ╰ [4]: GPL-2.0-or-later 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:c56fdae46ae47f698e7d4f15a4bcf2e2dcffa2409657f7d99f974c
│     │                 │       │                 82511ea6ba 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libsepol.so.2 
│     │                 │                        ├ [1]: /usr/share/doc/libsepol2/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libsepol2/copyright 
│     │                 ├ [85]  ╭ ID            : libsmartcols1@2.40.2-14ubuntu1.1 
│     │                 │       ├ Name          : libsmartcols1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libsmartcols1@2.40.2-14ubuntu1.1?arch=a
│     │                 │       │                │       md64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 297c2f35a46e43ef 
│     │                 │       ├ Version       : 2.40.2 
│     │                 │       ├ Release       : 14ubuntu1.1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : util-linux 
│     │                 │       ├ SrcVersion    : 2.40.2 
│     │                 │       ├ SrcRelease    : 14ubuntu1.1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-or-later 
│     │                 │       │                ├ [1] : GPL-2.0-only 
│     │                 │       │                ├ [2] : GPL-3.0-or-later 
│     │                 │       │                ├ [3] : LGPL-2.1-or-later 
│     │                 │       │                ├ [4] : public-domain 
│     │                 │       │                ├ [5] : BSD-4-Clause 
│     │                 │       │                ├ [6] : MIT 
│     │                 │       │                ├ [7] : ISC 
│     │                 │       │                ├ [8] : BSD-3-Clause 
│     │                 │       │                ├ [9] : BSLA 
│     │                 │       │                ├ [10]: LGPL-2.0-or-later 
│     │                 │       │                ├ [11]: BSD-2-Clause 
│     │                 │       │                ├ [12]: LGPL-3.0-or-later 
│     │                 │       │                ├ [13]: GPL-3.0-only 
│     │                 │       │                ├ [14]: LGPL-2.0-only 
│     │                 │       │                ├ [15]: LGPL-2.1-only 
│     │                 │       │                ╰ [16]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libsmartcols.so.1.1.0 
│     │                 │                        ├ [1]: /usr/share/doc/libsmartcols1/NEWS.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libsmartcols1/changelog.Debian.gz 
│     │                 │                        ├ [3]: /usr/share/doc/libsmartcols1/copyright 
│     │                 │                        ╰ [4]: /usr/share/lintian/overrides/libsmartcols1 
│     │                 ├ [86]  ╭ ID            : libss2@1.47.2-1ubuntu1 
│     │                 │       ├ Name          : libss2 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libss2@1.47.2-1ubuntu1?arch=amd64&distr
│     │                 │       │                │       o=ubuntu-25.04 
│     │                 │       │                ╰ UID : 80c5b986bc4c1ff9 
│     │                 │       ├ Version       : 1.47.2 
│     │                 │       ├ Release       : 1ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : e2fsprogs 
│     │                 │       ├ SrcVersion    : 1.47.2 
│     │                 │       ├ SrcRelease    : 1ubuntu1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-only 
│     │                 │       │                ├ [1] : GPL-2.0-or-later 
│     │                 │       │                ├ [2] : 0BSD 
│     │                 │       │                ├ [3] : MIT 
│     │                 │       │                ├ [4] : BSD-3-Clause-Variant 
│     │                 │       │                ├ [5] : BSD-3-Clause 
│     │                 │       │                ├ [6] : BSD-4-Clause-CMU 
│     │                 │       │                ├ [7] : LGPL-2.0-only 
│     │                 │       │                ├ [8] : Apache-2.0 
│     │                 │       │                ├ [9] : ISC 
│     │                 │       │                ├ [10]: MIT-US-export 
│     │                 │       │                ├ [11]: Kazlib 
│     │                 │       │                ├ [12]: Latex2e 
│     │                 │       │                ╰ [13]: GPL-2+ with Texinfo exception 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libcom-err2@1.47.2-1ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:1a6dbb95cd07924b61cbdf87a40b4ab1025799c29f15adaf5c1eda
│     │                 │       │                 db0c0003fa 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libss.so.2.0 
│     │                 │                        ╰ [1]: /usr/share/doc/libss2/copyright 
│     │                 ├ [87]  ╭ ID            : libssh2-1t64@1.11.1-1 
│     │                 │       ├ Name          : libssh2-1t64 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libssh2-1t64@1.11.1-1?arch=amd64&distro
│     │                 │       │                │       =ubuntu-25.04 
│     │                 │       │                ╰ UID : 55e10a431751f336 
│     │                 │       ├ Version       : 1.11.1 
│     │                 │       ├ Release       : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libssh2 
│     │                 │       ├ SrcVersion    : 1.11.1 
│     │                 │       ├ SrcRelease    : 1 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ╰ [1]: ISC 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [1]: libssl3t64@3.4.1-1ubuntu4 
│     │                 │       │                ╰ [2]: zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libssh2.so.1.0.1 
│     │                 │                        ├ [1]: /usr/share/doc/libssh2-1t64/AUTHORS 
│     │                 │                        ├ [2]: /usr/share/doc/libssh2-1t64/RELEASE-NOTES.gz 
│     │                 │                        ├ [3]: /usr/share/doc/libssh2-1t64/changelog.Debian.gz 
│     │                 │                        ╰ [4]: /usr/share/doc/libssh2-1t64/copyright 
│     │                 ├ [88]  ╭ ID            : libssl3t64@3.4.1-1ubuntu4 
│     │                 │       ├ Name          : libssl3t64 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libssl3t64@3.4.1-1ubuntu4?arch=amd64&di
│     │                 │       │                │       stro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 801d2ce5599545e5 
│     │                 │       ├ Version       : 3.4.1 
│     │                 │       ├ Release       : 1ubuntu4 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : openssl 
│     │                 │       ├ SrcVersion    : 3.4.1 
│     │                 │       ├ SrcRelease    : 1ubuntu4 
│     │                 │       ├ Licenses       ╭ [0]: Apache-2.0 
│     │                 │       │                ├ [1]: Artistic-2.0 
│     │                 │       │                ├ [2]: GPL-1.0-or-later 
│     │                 │       │                ╰ [3]: GPL-1.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [1]: libzstd1@1.5.6+dfsg-2 
│     │                 │       │                ├ [2]: openssl-provider-legacy@3.4.1-1ubuntu4 
│     │                 │       │                ╰ [3]: zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/engines-3/afalg.so 
│     │                 │                        ├ [1]: /usr/lib/x86_64-linux-gnu/engines-3/loader_attic.so 
│     │                 │                        ├ [2]: /usr/lib/x86_64-linux-gnu/engines-3/padlock.so 
│     │                 │                        ├ [3]: /usr/lib/x86_64-linux-gnu/libcrypto.so.3 
│     │                 │                        ├ [4]: /usr/lib/x86_64-linux-gnu/libssl.so.3 
│     │                 │                        ├ [5]: /usr/share/doc/libssl3t64/NEWS.Debian.gz 
│     │                 │                        ├ [6]: /usr/share/doc/libssl3t64/changelog.Debian.gz 
│     │                 │                        ├ [7]: /usr/share/doc/libssl3t64/copyright 
│     │                 │                        ╰ [8]: /usr/share/lintian/overrides/libssl3t64 
│     │                 ├ [89]  ╭ ID            : libstdc++6@15-20250404-0ubuntu1 
│     │                 │       ├ Name          : libstdc++6 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libstdc%2B%2B6@15-20250404-0ubuntu1?arc
│     │                 │       │                │       h=amd64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 3355251cc58bda9 
│     │                 │       ├ Version       : 15-20250404 
│     │                 │       ├ Release       : 0ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : gcc-15 
│     │                 │       ├ SrcVersion    : 15-20250404 
│     │                 │       ├ SrcRelease    : 0ubuntu1 
│     │                 │       ├ Maintainer    : Ubuntu Core developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: gcc-15-base@15-20250404-0ubuntu1 
│     │                 │       │                ├ [1]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [2]: libgcc-s1@15-20250404-0ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:c7f0149d8cb0ff366fb9529c9b49adca8ce758dbe3ba472b572b3d
│     │                 │       │                 8949617090 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.34 
│     │                 │                        ├ [1]: /usr/share/gcc/python/libstdcxx/__init__.py 
│     │                 │                        ├ [2]: /usr/share/gcc/python/libstdcxx/v6/__init__.py 
│     │                 │                        ├ [3]: /usr/share/gcc/python/libstdcxx/v6/printers.py 
│     │                 │                        ├ [4]: /usr/share/gcc/python/libstdcxx/v6/xmethods.py 
│     │                 │                        ╰ [5]: /usr/share/gdb/auto-load/usr/lib/x86_64-linux-gnu/libst
│     │                 │                               dc++.so.6.0.34-gdb.py 
│     │                 ├ [90]  ╭ ID            : libsystemd0@257.4-1ubuntu3.2 
│     │                 │       ├ Name          : libsystemd0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libsystemd0@257.4-1ubuntu3.2?arch=amd64
│     │                 │       │                │       &distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 94a922d04b7fe3d4 
│     │                 │       ├ Version       : 257.4 
│     │                 │       ├ Release       : 1ubuntu3.2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : systemd 
│     │                 │       ├ SrcVersion    : 257.4 
│     │                 │       ├ SrcRelease    : 1ubuntu3.2 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-2.1-or-later 
│     │                 │       │                ├ [1]: CC0-1.0 
│     │                 │       │                ├ [2]: GPL-2 with Linux-syscall-note exception 
│     │                 │       │                ├ [3]: MIT 
│     │                 │       │                ├ [4]: public-domain 
│     │                 │       │                ├ [5]: GPL-2.0-or-later 
│     │                 │       │                ├ [6]: GPL-2.0-only 
│     │                 │       │                ╰ [7]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libcap2@1:2.73-4ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libsystemd.so.0.40.0 
│     │                 │                        ├ [1]: /usr/share/doc/libsystemd0/NEWS.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libsystemd0/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/libsystemd0/copyright 
│     │                 ├ [91]  ╭ ID            : libtasn1-6@4.20.0-2 
│     │                 │       ├ Name          : libtasn1-6 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libtasn1-6@4.20.0-2?arch=amd64&distro=u
│     │                 │       │                │       buntu-25.04 
│     │                 │       │                ╰ UID : 71c2bdacc54486b3 
│     │                 │       ├ Version       : 4.20.0 
│     │                 │       ├ Release       : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libtasn1-6 
│     │                 │       ├ SrcVersion    : 4.20.0 
│     │                 │       ├ SrcRelease    : 2 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-2.0-or-later 
│     │                 │       │                ├ [1]: LGPL-2.1-only 
│     │                 │       │                ├ [2]: GPL-3.0-only 
│     │                 │       │                ╰ [3]: GFDL-1.3-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libtasn1.so.6.6.4 
│     │                 │                        ├ [1]: /usr/share/doc/libtasn1-6/AUTHORS 
│     │                 │                        ├ [2]: /usr/share/doc/libtasn1-6/README.md 
│     │                 │                        ├ [3]: /usr/share/doc/libtasn1-6/THANKS 
│     │                 │                        ├ [4]: /usr/share/doc/libtasn1-6/changelog.Debian.gz 
│     │                 │                        ╰ [5]: /usr/share/doc/libtasn1-6/copyright 
│     │                 ├ [92]  ╭ ID            : libtinfo6@6.5+20250216-2 
│     │                 │       ├ Name          : libtinfo6 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libtinfo6@6.5%2B20250216-2?arch=amd64&d
│     │                 │       │                │       istro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 7a6f8e171781bbd9 
│     │                 │       ├ Version       : 6.5+20250216 
│     │                 │       ├ Release       : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : ncurses 
│     │                 │       ├ SrcVersion    : 6.5+20250216 
│     │                 │       ├ SrcRelease    : 2 
│     │                 │       ├ Licenses       ╭ [0]: MIT/X11 
│     │                 │       │                ├ [1]: X11 
│     │                 │       │                ╰ [2]: BSD-3-Clause 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:74a7f112d19374c9cc45989df018c4b160fe035d2f5df31cd9b5ac
│     │                 │       │                 491535c041 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libtic.so.6.5 
│     │                 │                        ├ [1]: /usr/lib/x86_64-linux-gnu/libtinfo.so.6.5 
│     │                 │                        ├ [2]: /usr/share/doc/libtinfo6/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/libtinfo6/copyright 
│     │                 ├ [93]  ╭ ID            : libudev1@257.4-1ubuntu3.2 
│     │                 │       ├ Name          : libudev1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libudev1@257.4-1ubuntu3.2?arch=amd64&di
│     │                 │       │                │       stro=ubuntu-25.04 
│     │                 │       │                ╰ UID : ef2e84cf7bb3c47c 
│     │                 │       ├ Version       : 257.4 
│     │                 │       ├ Release       : 1ubuntu3.2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : systemd 
│     │                 │       ├ SrcVersion    : 257.4 
│     │                 │       ├ SrcRelease    : 1ubuntu3.2 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-2.1-or-later 
│     │                 │       │                ├ [1]: CC0-1.0 
│     │                 │       │                ├ [2]: GPL-2 with Linux-syscall-note exception 
│     │                 │       │                ├ [3]: MIT 
│     │                 │       │                ├ [4]: public-domain 
│     │                 │       │                ├ [5]: GPL-2.0-or-later 
│     │                 │       │                ├ [6]: GPL-2.0-only 
│     │                 │       │                ╰ [7]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libcap2@1:2.73-4ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libudev.so.1.7.10 
│     │                 │                        ├ [1]: /usr/share/doc/libudev1/NEWS.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libudev1/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/libudev1/copyright 
│     │                 ├ [94]  ╭ ID            : libunistring5@1.3-1 
│     │                 │       ├ Name          : libunistring5 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libunistring5@1.3-1?arch=amd64&distro=u
│     │                 │       │                │       buntu-25.04 
│     │                 │       │                ╰ UID : 90f79315507859be 
│     │                 │       ├ Version       : 1.3 
│     │                 │       ├ Release       : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libunistring 
│     │                 │       ├ SrcVersion    : 1.3 
│     │                 │       ├ SrcRelease    : 1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-3.0-or-later 
│     │                 │       │                ├ [1] : LGPL-3.0-or-later 
│     │                 │       │                ├ [2] : LGPL-2.0-or-later 
│     │                 │       │                ├ [3] : GFDL-1.3-or-later 
│     │                 │       │                ├ [4] : GFDL-1.2-or-later 
│     │                 │       │                ├ [5] : LGPL-3.0-only 
│     │                 │       │                ├ [6] : LGPL-2.1-or-later 
│     │                 │       │                ├ [7] : BSD-3-Clause 
│     │                 │       │                ├ [8] : ISC 
│     │                 │       │                ├ [9] : Unicode-DFS-2016 
│     │                 │       │                ├ [10]: public-domain 
│     │                 │       │                ├ [11]: FreeSoftware 
│     │                 │       │                ├ [12]: GPL-2.0-or-later 
│     │                 │       │                ├ [13]: GPL-2+ with distribution exception 
│     │                 │       │                ├ [14]: MIT 
│     │                 │       │                ├ [15]: X11 
│     │                 │       │                ├ [16]: GPL-3.0-only 
│     │                 │       │                ├ [17]: GPL-2.0-only 
│     │                 │       │                ├ [18]: LGPL-2.0-only 
│     │                 │       │                ╰ [19]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libunistring.so.5.2.0 
│     │                 │                        ├ [1]: /usr/share/doc/libunistring5/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libunistring5/copyright 
│     │                 ├ [95]  ╭ ID            : libuuid1@2.40.2-14ubuntu1.1 
│     │                 │       ├ Name          : libuuid1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libuuid1@2.40.2-14ubuntu1.1?arch=amd64&
│     │                 │       │                │       distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 53b20be971b134b9 
│     │                 │       ├ Version       : 2.40.2 
│     │                 │       ├ Release       : 14ubuntu1.1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : util-linux 
│     │                 │       ├ SrcVersion    : 2.40.2 
│     │                 │       ├ SrcRelease    : 14ubuntu1.1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-or-later 
│     │                 │       │                ├ [1] : GPL-2.0-only 
│     │                 │       │                ├ [2] : GPL-3.0-or-later 
│     │                 │       │                ├ [3] : LGPL-2.1-or-later 
│     │                 │       │                ├ [4] : public-domain 
│     │                 │       │                ├ [5] : BSD-4-Clause 
│     │                 │       │                ├ [6] : MIT 
│     │                 │       │                ├ [7] : ISC 
│     │                 │       │                ├ [8] : BSD-3-Clause 
│     │                 │       │                ├ [9] : BSLA 
│     │                 │       │                ├ [10]: LGPL-2.0-or-later 
│     │                 │       │                ├ [11]: BSD-2-Clause 
│     │                 │       │                ├ [12]: LGPL-3.0-or-later 
│     │                 │       │                ├ [13]: GPL-3.0-only 
│     │                 │       │                ├ [14]: LGPL-2.0-only 
│     │                 │       │                ├ [15]: LGPL-2.1-only 
│     │                 │       │                ╰ [16]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libuuid.so.1.3.0 
│     │                 │                        ├ [1]: /usr/share/doc/libuuid1/NEWS.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/libuuid1/changelog.Debian.gz 
│     │                 │                        ╰ [3]: /usr/share/doc/libuuid1/copyright 
│     │                 ├ [96]  ╭ ID            : libxxhash0@0.8.3-2 
│     │                 │       ├ Name          : libxxhash0 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libxxhash0@0.8.3-2?arch=amd64&distro=ub
│     │                 │       │                │       untu-25.04 
│     │                 │       │                ╰ UID : 7d7b834046c1b68d 
│     │                 │       ├ Version       : 0.8.3 
│     │                 │       ├ Release       : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : xxhash 
│     │                 │       ├ SrcVersion    : 0.8.3 
│     │                 │       ├ SrcRelease    : 2 
│     │                 │       ├ Licenses       ╭ [0]: BSD-2-Clause 
│     │                 │       │                ├ [1]: GPL-2.0-or-later 
│     │                 │       │                ╰ [2]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:6d8286d995aeef1ffc85790ff7d8bef957a214d94bc1277d716b6b
│     │                 │       │                 2f5b8cbe51 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libxxhash.so.0.8.3 
│     │                 │                        ├ [1]: /usr/share/doc/libxxhash0/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libxxhash0/copyright 
│     │                 ├ [97]  ╭ ID            : libzstd1@1.5.6+dfsg-2 
│     │                 │       ├ Name          : libzstd1 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/libzstd1@1.5.6%2Bdfsg-2?arch=amd64&dist
│     │                 │       │                │       ro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 9449b476a670c9ff 
│     │                 │       ├ Version       : 1.5.6+dfsg 
│     │                 │       ├ Release       : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : libzstd 
│     │                 │       ├ SrcVersion    : 1.5.6+dfsg 
│     │                 │       ├ SrcRelease    : 2 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ├ [1]: GPL-2.0-only 
│     │                 │       │                ├ [2]: Zlib 
│     │                 │       │                ╰ [3]: MIT 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:53e48dd3634eb5e66ddd8fabd034e3760b93b816584d1d55a8966f
│     │                 │       │                 0b12e145b9 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libzstd.so.1.5.6 
│     │                 │                        ├ [1]: /usr/share/doc/libzstd1/changelog.Debian.gz 
│     │                 │                        ╰ [2]: /usr/share/doc/libzstd1/copyright 
│     │                 ├ [98]  ╭ ID            : login@1:4.16.0-2+really2.40.2-14ubuntu1.1 
│     │                 │       ├ Name          : login 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/login@4.16.0-2%2Breally2.40.2-14ubuntu1
│     │                 │       │                │       .1?arch=amd64&distro=ubuntu-25.04&epoch=1 
│     │                 │       │                ╰ UID : 99a9307f9536955d 
│     │                 │       ├ Version       : 4.16.0-2+really2.40.2 
│     │                 │       ├ Release       : 14ubuntu1.1 
│     │                 │       ├ Epoch         : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : util-linux 
│     │                 │       ├ SrcVersion    : 2.40.2 
│     │                 │       ├ SrcRelease    : 14ubuntu1.1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-or-later 
│     │                 │       │                ├ [1] : GPL-2.0-only 
│     │                 │       │                ├ [2] : GPL-3.0-or-later 
│     │                 │       │                ├ [3] : LGPL-2.1-or-later 
│     │                 │       │                ├ [4] : public-domain 
│     │                 │       │                ├ [5] : BSD-4-Clause 
│     │                 │       │                ├ [6] : MIT 
│     │                 │       │                ├ [7] : ISC 
│     │                 │       │                ├ [8] : BSD-3-Clause 
│     │                 │       │                ├ [9] : BSLA 
│     │                 │       │                ├ [10]: LGPL-2.0-or-later 
│     │                 │       │                ├ [11]: BSD-2-Clause 
│     │                 │       │                ├ [12]: LGPL-3.0-or-later 
│     │                 │       │                ├ [13]: GPL-3.0-only 
│     │                 │       │                ├ [14]: LGPL-2.0-only 
│     │                 │       │                ├ [15]: LGPL-2.1-only 
│     │                 │       │                ╰ [16]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libaudit1@1:4.0.2-2ubuntu2 
│     │                 │       │                ├ [1]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [2]: libcrypt1@1:4.4.38-1 
│     │                 │       │                ├ [3]: libpam-modules@1.5.3-7ubuntu4.4 
│     │                 │       │                ├ [4]: libpam-runtime@1.5.3-7ubuntu4.4 
│     │                 │       │                ╰ [5]: libpam0g@1.5.3-7ubuntu4.4 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/login 
│     │                 │                        ├ [1] : /usr/bin/newgrp 
│     │                 │                        ├ [2] : /usr/sbin/nologin 
│     │                 │                        ├ [3] : /usr/share/bash-completion/completions/newgrp 
│     │                 │                        ├ [4] : /usr/share/doc/login/NEWS.Debian.gz 
│     │                 │                        ├ [5] : /usr/share/doc/login/changelog.Debian.gz 
│     │                 │                        ├ [6] : /usr/share/doc/login/copyright 
│     │                 │                        ├ [7] : /usr/share/lintian/overrides/login 
│     │                 │                        ├ [8] : /usr/share/man/de/man1/login.1.gz 
│     │                 │                        ├ [9] : /usr/share/man/de/man8/nologin.8.gz 
│     │                 │                        ├ [10]: /usr/share/man/fr/man1/login.1.gz 
│     │                 │                        ├ [11]: /usr/share/man/man1/login.1.gz 
│     │                 │                        ├ [12]: /usr/share/man/man1/newgrp.1.gz 
│     │                 │                        ├ [13]: /usr/share/man/man8/nologin.8.gz 
│     │                 │                        ├ [14]: /usr/share/man/sr/man1/login.1.gz 
│     │                 │                        ╰ [15]: /usr/share/man/uk/man1/login.1.gz 
│     │                 ├ [99]  ╭ ID            : login.defs@1:4.16.0-7ubuntu1 
│     │                 │       ├ Name          : login.defs 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/login.defs@4.16.0-7ubuntu1?arch=all&dis
│     │                 │       │                │       tro=ubuntu-25.04&epoch=1 
│     │                 │       │                ╰ UID : 4016d70dedce9ad0 
│     │                 │       ├ Version       : 4.16.0 
│     │                 │       ├ Release       : 7ubuntu1 
│     │                 │       ├ Epoch         : 1 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : shadow 
│     │                 │       ├ SrcVersion    : 4.16.0 
│     │                 │       ├ SrcRelease    : 7ubuntu1 
│     │                 │       ├ SrcEpoch      : 1 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ├ [1]: GPL-1.0-only 
│     │                 │       │                ├ [2]: GPL-2.0-or-later 
│     │                 │       │                ╰ [3]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:3d394aa07fc4e580dfca7725ca24b4e529b0d8703b8d6a957217f9
│     │                 │       │                 45e4b61af6 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/share/apport/package-hooks/source_shadow.py 
│     │                 │                        ├ [1] : /usr/share/doc/login.defs/NEWS.Debian.gz 
│     │                 │                        ├ [2] : /usr/share/doc/login.defs/changelog.Debian.gz 
│     │                 │                        ├ [3] : /usr/share/doc/login.defs/copyright 
│     │                 │                        ├ [4] : /usr/share/man/de/man5/login.defs.5.gz 
│     │                 │                        ├ [5] : /usr/share/man/fr/man5/login.defs.5.gz 
│     │                 │                        ├ [6] : /usr/share/man/it/man5/login.defs.5.gz 
│     │                 │                        ├ [7] : /usr/share/man/ja/man5/login.defs.5.gz 
│     │                 │                        ├ [8] : /usr/share/man/man5/login.defs.5.gz 
│     │                 │                        ├ [9] : /usr/share/man/ru/man5/login.defs.5.gz 
│     │                 │                        ├ [10]: /usr/share/man/uk/man5/login.defs.5.gz 
│     │                 │                        ╰ [11]: /usr/share/man/zh_CN/man5/login.defs.5.gz 
│     │                 ├ [100] ╭ ID            : logsave@1.47.2-1ubuntu1 
│     │                 │       ├ Name          : logsave 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/logsave@1.47.2-1ubuntu1?arch=amd64&dist
│     │                 │       │                │       ro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 917dc52edb3d36a9 
│     │                 │       ├ Version       : 1.47.2 
│     │                 │       ├ Release       : 1ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : e2fsprogs 
│     │                 │       ├ SrcVersion    : 1.47.2 
│     │                 │       ├ SrcRelease    : 1ubuntu1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-only 
│     │                 │       │                ├ [1] : GPL-2.0-or-later 
│     │                 │       │                ├ [2] : 0BSD 
│     │                 │       │                ├ [3] : MIT 
│     │                 │       │                ├ [4] : BSD-3-Clause-Variant 
│     │                 │       │                ├ [5] : BSD-3-Clause 
│     │                 │       │                ├ [6] : BSD-4-Clause-CMU 
│     │                 │       │                ├ [7] : LGPL-2.0-only 
│     │                 │       │                ├ [8] : Apache-2.0 
│     │                 │       │                ├ [9] : ISC 
│     │                 │       │                ├ [10]: MIT-US-export 
│     │                 │       │                ├ [11]: Kazlib 
│     │                 │       │                ├ [12]: Latex2e 
│     │                 │       │                ╰ [13]: GPL-2+ with Texinfo exception 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:21e91dee4677d67324ef0e068816d02b197b7ec4537f624613213c
│     │                 │       │                 6fb47dc764 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/sbin/logsave 
│     │                 │                        ├ [1]: /usr/share/doc/logsave/changelog.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/logsave/copyright 
│     │                 │                        ╰ [3]: /usr/share/man/man8/logsave.8.gz 
│     │                 ├ [101] ╭ ID            : mawk@1.3.4.20250131-1 
│     │                 │       ├ Name          : mawk 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/mawk@1.3.4.20250131-1?arch=amd64&distro
│     │                 │       │                │       =ubuntu-25.04 
│     │                 │       │                ╰ UID : d83d0bb47779994b 
│     │                 │       ├ Version       : 1.3.4.20250131 
│     │                 │       ├ Release       : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : mawk 
│     │                 │       ├ SrcVersion    : 1.3.4.20250131 
│     │                 │       ├ SrcRelease    : 1 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-only 
│     │                 │       │                ├ [1]: X11 
│     │                 │       │                ╰ [2]: CC-BY-3.0 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:8ccec85e069f802a586a8a4c388764571950d823596624585f0cc6
│     │                 │       │                 9510abf690 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/mawk 
│     │                 │                        ├ [1] : /usr/share/doc/mawk/ACKNOWLEDGMENT 
│     │                 │                        ├ [2] : /usr/share/doc/mawk/README 
│     │                 │                        ├ [3] : /usr/share/doc/mawk/changelog.Debian.gz 
│     │                 │                        ├ [4] : /usr/share/doc/mawk/copyright 
│     │                 │                        ├ [5] : /usr/share/doc/mawk/examples/ct_length.awk 
│     │                 │                        ├ [6] : /usr/share/doc/mawk/examples/decl.awk 
│     │                 │                        ├ [7] : /usr/share/doc/mawk/examples/deps.awk 
│     │                 │                        ├ [8] : /usr/share/doc/mawk/examples/eatc.awk 
│     │                 │                        ├ [9] : /usr/share/doc/mawk/examples/gdecl.awk 
│     │                 │                        ├ [10]: /usr/share/doc/mawk/examples/hcal 
│     │                 │                        ├ [11]: /usr/share/doc/mawk/examples/hical 
│     │                 │                        ├ [12]: /usr/share/doc/mawk/examples/nocomment.awk 
│     │                 │                        ├ [13]: /usr/share/doc/mawk/examples/primes.awk 
│     │                 │                        ├ [14]: /usr/share/doc/mawk/examples/qsort.awk 
│     │                 │                        ├ [15]: /usr/share/man/man1/mawk.1.gz 
│     │                 │                        ├ [16]: /usr/share/man/man7/mawk-arrays.7.gz 
│     │                 │                        ╰ [17]: /usr/share/man/man7/mawk-code.7.gz 
│     │                 ├ [102] ╭ ID            : mount@2.40.2-14ubuntu1.1 
│     │                 │       ├ Name          : mount 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/mount@2.40.2-14ubuntu1.1?arch=amd64&dis
│     │                 │       │                │       tro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 7528b3347afde2a1 
│     │                 │       ├ Version       : 2.40.2 
│     │                 │       ├ Release       : 14ubuntu1.1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : util-linux 
│     │                 │       ├ SrcVersion    : 2.40.2 
│     │                 │       ├ SrcRelease    : 14ubuntu1.1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-or-later 
│     │                 │       │                ├ [1] : GPL-2.0-only 
│     │                 │       │                ├ [2] : GPL-3.0-or-later 
│     │                 │       │                ├ [3] : LGPL-2.1-or-later 
│     │                 │       │                ├ [4] : public-domain 
│     │                 │       │                ├ [5] : BSD-4-Clause 
│     │                 │       │                ├ [6] : MIT 
│     │                 │       │                ├ [7] : ISC 
│     │                 │       │                ├ [8] : BSD-3-Clause 
│     │                 │       │                ├ [9] : BSLA 
│     │                 │       │                ├ [10]: LGPL-2.0-or-later 
│     │                 │       │                ├ [11]: BSD-2-Clause 
│     │                 │       │                ├ [12]: LGPL-3.0-or-later 
│     │                 │       │                ├ [13]: GPL-3.0-only 
│     │                 │       │                ├ [14]: LGPL-2.0-only 
│     │                 │       │                ├ [15]: LGPL-2.1-only 
│     │                 │       │                ╰ [16]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/mount 
│     │                 │                        ├ [1] : /usr/bin/umount 
│     │                 │                        ├ [2] : /usr/sbin/losetup 
│     │                 │                        ├ [3] : /usr/sbin/swapoff 
│     │                 │                        ├ [4] : /usr/sbin/swapon 
│     │                 │                        ├ [5] : /usr/share/bash-completion/completions/losetup 
│     │                 │                        ├ [6] : /usr/share/bash-completion/completions/mount 
│     │                 │                        ├ [7] : /usr/share/bash-completion/completions/swapoff 
│     │                 │                        ├ [8] : /usr/share/bash-completion/completions/swapon 
│     │                 │                        ├ [9] : /usr/share/bash-completion/completions/umount 
│     │                 │                        ├ [10]: /usr/share/doc/mount/NEWS.Debian.gz 
│     │                 │                        ├ [11]: /usr/share/doc/mount/changelog.Debian.gz 
│     │                 │                        ├ [12]: /usr/share/doc/mount/copyright 
│     │                 │                        ├ [13]: /usr/share/doc/mount/examples/filesystems 
│     │                 │                        ├ [14]: /usr/share/doc/mount/examples/fstab 
│     │                 │                        ├ [15]: /usr/share/doc/mount/examples/mount.fstab 
│     │                 │                        ├ [16]: /usr/share/doc/mount/mount.txt 
│     │                 │                        ├ [17]: /usr/share/lintian/overrides/mount 
│     │                 │                        ├ [18]: /usr/share/man/man5/fstab.5.gz 
│     │                 │                        ├ [19]: /usr/share/man/man8/losetup.8.gz 
│     │                 │                        ├ [20]: /usr/share/man/man8/mount.8.gz 
│     │                 │                        ├ [21]: /usr/share/man/man8/swapon.8.gz 
│     │                 │                        ╰ [22]: /usr/share/man/man8/umount.8.gz 
│     │                 ├ [103] ╭ ID            : ncurses-base@6.5+20250216-2 
│     │                 │       ├ Name          : ncurses-base 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/ncurses-base@6.5%2B20250216-2?arch=all&
│     │                 │       │                │       distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 9b9008fe39f45d9f 
│     │                 │       ├ Version       : 6.5+20250216 
│     │                 │       ├ Release       : 2 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : ncurses 
│     │                 │       ├ SrcVersion    : 6.5+20250216 
│     │                 │       ├ SrcRelease    : 2 
│     │                 │       ├ Licenses       ╭ [0]: MIT/X11 
│     │                 │       │                ├ [1]: X11 
│     │                 │       │                ╰ [2]: BSD-3-Clause 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:7ee3e9cd1cbc2e7f9839c0a00b97cce14f66a8b6faf68d9c6b34d1
│     │                 │       │                 43a2d3dfda 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/share/doc/ncurses-base/FAQ 
│     │                 │                        ├ [1] : /usr/share/doc/ncurses-base/TODO.Debian 
│     │                 │                        ├ [2] : /usr/share/doc/ncurses-base/changelog.Debian.gz 
│     │                 │                        ├ [3] : /usr/share/doc/ncurses-base/copyright 
│     │                 │                        ├ [4] : /usr/share/lintian/overrides/ncurses-base 
│     │                 │                        ├ [5] : /usr/share/tabset/std 
│     │                 │                        ├ [6] : /usr/share/tabset/stdcrt 
│     │                 │                        ├ [7] : /usr/share/tabset/vt100 
│     │                 │                        ├ [8] : /usr/share/tabset/vt300 
│     │                 │                        ├ [9] : /usr/share/terminfo/E/Eterm 
│     │                 │                        ├ [10]: /usr/share/terminfo/a/ansi 
│     │                 │                        ├ [11]: /usr/share/terminfo/c/cons25 
│     │                 │                        ├ [12]: /usr/share/terminfo/c/cygwin 
│     │                 │                        ├ [13]: /usr/share/terminfo/d/dumb 
│     │                 │                        ├ [14]: /usr/share/terminfo/h/hurd 
│     │                 │                        ├ [15]: /usr/share/terminfo/l/linux 
│     │                 │                        ├ [16]: /usr/share/terminfo/m/mach 
│     │                 │                        ├ [17]: /usr/share/terminfo/m/mach-bold 
│     │                 │                        ├ [18]: /usr/share/terminfo/m/mach-color 
│     │                 │                        ├ [19]: /usr/share/terminfo/m/mach-gnu 
│     │                 │                        ├ [20]: /usr/share/terminfo/m/mach-gnu-color 
│     │                 │                        ├ [21]: /usr/share/terminfo/p/pcansi 
│     │                 │                        ├ [22]: /usr/share/terminfo/r/rxvt 
│     │                 │                        ├ [23]: /usr/share/terminfo/r/rxvt-basic 
│     │                 │                        ├ [24]: /usr/share/terminfo/r/rxvt-unicode 
│     │                 │                        ├ [25]: /usr/share/terminfo/r/rxvt-unicode-256color 
│     │                 │                        ├ [26]: /usr/share/terminfo/s/screen 
│     │                 │                        ├ [27]: /usr/share/terminfo/s/screen-256color 
│     │                 │                        ├ [28]: /usr/share/terminfo/s/screen-256color-bce 
│     │                 │                        ├ [29]: /usr/share/terminfo/s/screen-bce 
│     │                 │                        ├ [30]: /usr/share/terminfo/s/screen-s 
│     │                 │                        ├ [31]: /usr/share/terminfo/s/screen-w 
│     │                 │                        ├ [32]: /usr/share/terminfo/s/screen.xterm-256color 
│     │                 │                        ├ [33]: /usr/share/terminfo/s/sun 
│     │                 │                        ├ [34]: /usr/share/terminfo/t/tmux 
│     │                 │                        ├ [35]: /usr/share/terminfo/t/tmux-256color 
│     │                 │                        ├ [36]: /usr/share/terminfo/v/vt100 
│     │                 │                        ├ [37]: /usr/share/terminfo/v/vt102 
│     │                 │                        ├ [38]: /usr/share/terminfo/v/vt220 
│     │                 │                        ├ [39]: /usr/share/terminfo/v/vt52 
│     │                 │                        ├ [40]: /usr/share/terminfo/w/wsvt25 
│     │                 │                        ├ [41]: /usr/share/terminfo/w/wsvt25m 
│     │                 │                        ├ [42]: /usr/share/terminfo/x/xterm 
│     │                 │                        ├ [43]: /usr/share/terminfo/x/xterm-256color 
│     │                 │                        ├ [44]: /usr/share/terminfo/x/xterm-color 
│     │                 │                        ├ [45]: /usr/share/terminfo/x/xterm-mono 
│     │                 │                        ├ [46]: /usr/share/terminfo/x/xterm-r5 
│     │                 │                        ├ [47]: /usr/share/terminfo/x/xterm-r6 
│     │                 │                        ├ [48]: /usr/share/terminfo/x/xterm-vt220 
│     │                 │                        ╰ [49]: /usr/share/terminfo/x/xterm-xfree86 
│     │                 ├ [104] ╭ ID            : ncurses-bin@6.5+20250216-2 
│     │                 │       ├ Name          : ncurses-bin 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/ncurses-bin@6.5%2B20250216-2?arch=amd64
│     │                 │       │                │       &distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 18ff95b419c7a965 
│     │                 │       ├ Version       : 6.5+20250216 
│     │                 │       ├ Release       : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : ncurses 
│     │                 │       ├ SrcVersion    : 6.5+20250216 
│     │                 │       ├ SrcRelease    : 2 
│     │                 │       ├ Licenses       ╭ [0]: MIT/X11 
│     │                 │       │                ├ [1]: X11 
│     │                 │       │                ╰ [2]: BSD-3-Clause 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:e6fad6cfbf2298d3e04834194897b0d6715332adc5927b27395f5e
│     │                 │       │                 5b1e23c3e3 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/clear 
│     │                 │                        ├ [1] : /usr/bin/infocmp 
│     │                 │                        ├ [2] : /usr/bin/tabs 
│     │                 │                        ├ [3] : /usr/bin/tic 
│     │                 │                        ├ [4] : /usr/bin/toe 
│     │                 │                        ├ [5] : /usr/bin/tput 
│     │                 │                        ├ [6] : /usr/bin/tset 
│     │                 │                        ├ [7] : /usr/share/doc/ncurses-bin/copyright 
│     │                 │                        ├ [8] : /usr/share/man/man1/captoinfo.1.gz 
│     │                 │                        ├ [9] : /usr/share/man/man1/clear.1.gz 
│     │                 │                        ├ [10]: /usr/share/man/man1/infocmp.1.gz 
│     │                 │                        ├ [11]: /usr/share/man/man1/infotocap.1.gz 
│     │                 │                        ├ [12]: /usr/share/man/man1/tabs.1.gz 
│     │                 │                        ├ [13]: /usr/share/man/man1/tic.1.gz 
│     │                 │                        ├ [14]: /usr/share/man/man1/toe.1.gz 
│     │                 │                        ├ [15]: /usr/share/man/man1/tput.1.gz 
│     │                 │                        ├ [16]: /usr/share/man/man1/tset.1.gz 
│     │                 │                        ├ [17]: /usr/share/man/man5/scr_dump.5.gz 
│     │                 │                        ├ [18]: /usr/share/man/man5/term.5.gz 
│     │                 │                        ├ [19]: /usr/share/man/man5/terminfo.5.gz 
│     │                 │                        ├ [20]: /usr/share/man/man5/user_caps.5.gz 
│     │                 │                        ╰ [21]: /usr/share/man/man7/term.7.gz 
│     │                 ├ [105] ╭ ID            : openssl@3.4.1-1ubuntu4 
│     │                 │       ├ Name          : openssl 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/openssl@3.4.1-1ubuntu4?arch=amd64&distr
│     │                 │       │                │       o=ubuntu-25.04 
│     │                 │       │                ╰ UID : b89cffbf8d18d9da 
│     │                 │       ├ Version       : 3.4.1 
│     │                 │       ├ Release       : 1ubuntu4 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : openssl 
│     │                 │       ├ SrcVersion    : 3.4.1 
│     │                 │       ├ SrcRelease    : 1ubuntu4 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libssl3t64@3.4.1-1ubuntu4 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/bin/c_rehash 
│     │                 │                        ├ [1]  : /usr/bin/openssl 
│     │                 │                        ├ [2]  : /usr/lib/ssl/misc/CA.pl 
│     │                 │                        ├ [3]  : /usr/lib/ssl/misc/tsget.pl 
│     │                 │                        ├ [4]  : /usr/share/doc/openssl/HOWTO/certificates.txt.gz 
│     │                 │                        ├ [5]  : /usr/share/doc/openssl/HOWTO/documenting-functions-an
│     │                 │                        │        d-macros.md.gz 
│     │                 │                        ├ [6]  : /usr/share/doc/openssl/HOWTO/keys.txt 
│     │                 │                        ├ [7]  : /usr/share/doc/openssl/NEWS.md.gz 
│     │                 │                        ├ [8]  : /usr/share/doc/openssl/README-ENGINES.md.gz 
│     │                 │                        ├ [9]  : /usr/share/doc/openssl/README-PROVIDERS.md.gz 
│     │                 │                        ├ [10] : /usr/share/doc/openssl/README-QUIC.md 
│     │                 │                        ├ [11] : /usr/share/doc/openssl/README.Debian 
│     │                 │                        ├ [12] : /usr/share/doc/openssl/README.md.gz 
│     │                 │                        ├ [13] : /usr/share/doc/openssl/fingerprints.txt 
│     │                 │                        ├ [14] : /usr/share/lintian/overrides/openssl 
│     │                 │                        ├ [15] : /usr/share/man/man1/CA.pl.1ssl.gz 
│     │                 │                        ├ [16] : /usr/share/man/man1/openssl-asn1parse.1ssl.gz 
│     │                 │                        ├ [17] : /usr/share/man/man1/openssl-ca.1ssl.gz 
│     │                 │                        ├ [18] : /usr/share/man/man1/openssl-ciphers.1ssl.gz 
│     │                 │                        ├ [19] : /usr/share/man/man1/openssl-cmds.1ssl.gz 
│     │                 │                        ├ [20] : /usr/share/man/man1/openssl-cmp.1ssl.gz 
│     │                 │                        ├ [21] : /usr/share/man/man1/openssl-cms.1ssl.gz 
│     │                 │                        ├ [22] : /usr/share/man/man1/openssl-crl.1ssl.gz 
│     │                 │                        ├ [23] : /usr/share/man/man1/openssl-crl2pkcs7.1ssl.gz 
│     │                 │                        ├ [24] : /usr/share/man/man1/openssl-dgst.1ssl.gz 
│     │                 │                        ├ [25] : /usr/share/man/man1/openssl-dhparam.1ssl.gz 
│     │                 │                        ├ [26] : /usr/share/man/man1/openssl-dsa.1ssl.gz 
│     │                 │                        ├ [27] : /usr/share/man/man1/openssl-dsaparam.1ssl.gz 
│     │                 │                        ├ [28] : /usr/share/man/man1/openssl-ec.1ssl.gz 
│     │                 │                        ├ [29] : /usr/share/man/man1/openssl-ecparam.1ssl.gz 
│     │                 │                        ├ [30] : /usr/share/man/man1/openssl-enc.1ssl.gz 
│     │                 │                        ├ [31] : /usr/share/man/man1/openssl-engine.1ssl.gz 
│     │                 │                        ├ [32] : /usr/share/man/man1/openssl-errstr.1ssl.gz 
│     │                 │                        ├ [33] : /usr/share/man/man1/openssl-fipsinstall.1ssl.gz 
│     │                 │                        ├ [34] : /usr/share/man/man1/openssl-format-options.1ssl.gz 
│     │                 │                        ├ [35] : /usr/share/man/man1/openssl-gendsa.1ssl.gz 
│     │                 │                        ├ [36] : /usr/share/man/man1/openssl-genpkey.1ssl.gz 
│     │                 │                        ├ [37] : /usr/share/man/man1/openssl-genrsa.1ssl.gz 
│     │                 │                        ├ [38] : /usr/share/man/man1/openssl-info.1ssl.gz 
│     │                 │                        ├ [39] : /usr/share/man/man1/openssl-kdf.1ssl.gz 
│     │                 │                        ├ [40] : /usr/share/man/man1/openssl-list.1ssl.gz 
│     │                 │                        ├ [41] : /usr/share/man/man1/openssl-mac.1ssl.gz 
│     │                 │                        ├ [42] : /usr/share/man/man1/openssl-namedisplay-options.1ssl.gz 
│     │                 │                        ├ [43] : /usr/share/man/man1/openssl-nseq.1ssl.gz 
│     │                 │                        ├ [44] : /usr/share/man/man1/openssl-ocsp.1ssl.gz 
│     │                 │                        ├ [45] : /usr/share/man/man1/openssl-passphrase-options.1ssl.gz 
│     │                 │                        ├ [46] : /usr/share/man/man1/openssl-passwd.1ssl.gz 
│     │                 │                        ├ [47] : /usr/share/man/man1/openssl-pkcs12.1ssl.gz 
│     │                 │                        ├ [48] : /usr/share/man/man1/openssl-pkcs7.1ssl.gz 
│     │                 │                        ├ [49] : /usr/share/man/man1/openssl-pkcs8.1ssl.gz 
│     │                 │                        ├ [50] : /usr/share/man/man1/openssl-pkey.1ssl.gz 
│     │                 │                        ├ [51] : /usr/share/man/man1/openssl-pkeyparam.1ssl.gz 
│     │                 │                        ├ [52] : /usr/share/man/man1/openssl-pkeyutl.1ssl.gz 
│     │                 │                        ├ [53] : /usr/share/man/man1/openssl-prime.1ssl.gz 
│     │                 │                        ├ [54] : /usr/share/man/man1/openssl-rand.1ssl.gz 
│     │                 │                        ├ [55] : /usr/share/man/man1/openssl-rehash.1ssl.gz 
│     │                 │                        ├ [56] : /usr/share/man/man1/openssl-req.1ssl.gz 
│     │                 │                        ├ [57] : /usr/share/man/man1/openssl-rsa.1ssl.gz 
│     │                 │                        ├ [58] : /usr/share/man/man1/openssl-rsautl.1ssl.gz 
│     │                 │                        ├ [59] : /usr/share/man/man1/openssl-s_client.1ssl.gz 
│     │                 │                        ├ [60] : /usr/share/man/man1/openssl-s_server.1ssl.gz 
│     │                 │                        ├ [61] : /usr/share/man/man1/openssl-s_time.1ssl.gz 
│     │                 │                        ├ [62] : /usr/share/man/man1/openssl-sess_id.1ssl.gz 
│     │                 │                        ├ [63] : /usr/share/man/man1/openssl-smime.1ssl.gz 
│     │                 │                        ├ [64] : /usr/share/man/man1/openssl-speed.1ssl.gz 
│     │                 │                        ├ [65] : /usr/share/man/man1/openssl-spkac.1ssl.gz 
│     │                 │                        ├ [66] : /usr/share/man/man1/openssl-srp.1ssl.gz 
│     │                 │                        ├ [67] : /usr/share/man/man1/openssl-storeutl.1ssl.gz 
│     │                 │                        ├ [68] : /usr/share/man/man1/openssl-ts.1ssl.gz 
│     │                 │                        ├ [69] : /usr/share/man/man1/openssl-verification-options.1ssl
│     │                 │                        │        .gz 
│     │                 │                        ├ [70] : /usr/share/man/man1/openssl-verify.1ssl.gz 
│     │                 │                        ├ [71] : /usr/share/man/man1/openssl-version.1ssl.gz 
│     │                 │                        ├ [72] : /usr/share/man/man1/openssl-x509.1ssl.gz 
│     │                 │                        ├ [73] : /usr/share/man/man1/openssl.1ssl.gz 
│     │                 │                        ├ [74] : /usr/share/man/man1/tsget.1ssl.gz 
│     │                 │                        ├ [75] : /usr/share/man/man5/config.5ssl.gz 
│     │                 │                        ├ [76] : /usr/share/man/man5/fips_config.5ssl.gz 
│     │                 │                        ├ [77] : /usr/share/man/man5/x509v3_config.5ssl.gz 
│     │                 │                        ├ [78] : /usr/share/man/man7/EVP_ASYM_CIPHER-RSA.7ssl.gz 
│     │                 │                        ├ [79] : /usr/share/man/man7/EVP_ASYM_CIPHER-SM2.7ssl.gz 
│     │                 │                        ├ [80] : /usr/share/man/man7/EVP_CIPHER-AES.7ssl.gz 
│     │                 │                        ├ [81] : /usr/share/man/man7/EVP_CIPHER-ARIA.7ssl.gz 
│     │                 │                        ├ [82] : /usr/share/man/man7/EVP_CIPHER-BLOWFISH.7ssl.gz 
│     │                 │                        ├ [83] : /usr/share/man/man7/EVP_CIPHER-CAMELLIA.7ssl.gz 
│     │                 │                        ├ [84] : /usr/share/man/man7/EVP_CIPHER-CAST.7ssl.gz 
│     │                 │                        ├ [85] : /usr/share/man/man7/EVP_CIPHER-CHACHA.7ssl.gz 
│     │                 │                        ├ [86] : /usr/share/man/man7/EVP_CIPHER-DES.7ssl.gz 
│     │                 │                        ├ [87] : /usr/share/man/man7/EVP_CIPHER-IDEA.7ssl.gz 
│     │                 │                        ├ [88] : /usr/share/man/man7/EVP_CIPHER-NULL.7ssl.gz 
│     │                 │                        ├ [89] : /usr/share/man/man7/EVP_CIPHER-RC2.7ssl.gz 
│     │                 │                        ├ [90] : /usr/share/man/man7/EVP_CIPHER-RC4.7ssl.gz 
│     │                 │                        ├ [91] : /usr/share/man/man7/EVP_CIPHER-RC5.7ssl.gz 
│     │                 │                        ├ [92] : /usr/share/man/man7/EVP_CIPHER-SEED.7ssl.gz 
│     │                 │                        ├ [93] : /usr/share/man/man7/EVP_CIPHER-SM4.7ssl.gz 
│     │                 │                        ├ [94] : /usr/share/man/man7/EVP_KDF-ARGON2.7ssl.gz 
│     │                 │                        ├ [95] : /usr/share/man/man7/EVP_KDF-HKDF.7ssl.gz 
│     │                 │                        ├ [96] : /usr/share/man/man7/EVP_KDF-HMAC-DRBG.7ssl.gz 
│     │                 │                        ├ [97] : /usr/share/man/man7/EVP_KDF-KB.7ssl.gz 
│     │                 │                        ├ [98] : /usr/share/man/man7/EVP_KDF-KRB5KDF.7ssl.gz 
│     │                 │                        ├ [99] : /usr/share/man/man7/EVP_KDF-PBKDF1.7ssl.gz 
│     │                 │                        ├ [100]: /usr/share/man/man7/EVP_KDF-PBKDF2.7ssl.gz 
│     │                 │                        ├ [101]: /usr/share/man/man7/EVP_KDF-PKCS12KDF.7ssl.gz 
│     │                 │                        ├ [102]: /usr/share/man/man7/EVP_KDF-PVKKDF.7ssl.gz 
│     │                 │                        ├ [103]: /usr/share/man/man7/EVP_KDF-SCRYPT.7ssl.gz 
│     │                 │                        ├ [104]: /usr/share/man/man7/EVP_KDF-SS.7ssl.gz 
│     │                 │                        ├ [105]: /usr/share/man/man7/EVP_KDF-SSHKDF.7ssl.gz 
│     │                 │                        ├ [106]: /usr/share/man/man7/EVP_KDF-TLS13_KDF.7ssl.gz 
│     │                 │                        ├ [107]: /usr/share/man/man7/EVP_KDF-TLS1_PRF.7ssl.gz 
│     │                 │                        ├ [108]: /usr/share/man/man7/EVP_KDF-X942-ASN1.7ssl.gz 
│     │                 │                        ├ [109]: /usr/share/man/man7/EVP_KDF-X942-CONCAT.7ssl.gz 
│     │                 │                        ├ [110]: /usr/share/man/man7/EVP_KDF-X963.7ssl.gz 
│     │                 │                        ├ [111]: /usr/share/man/man7/EVP_KEM-EC.7ssl.gz 
│     │                 │                        ├ [112]: /usr/share/man/man7/EVP_KEM-RSA.7ssl.gz 
│     │                 │                        ├ [113]: /usr/share/man/man7/EVP_KEM-X25519.7ssl.gz 
│     │                 │                        ├ [114]: /usr/share/man/man7/EVP_KEYEXCH-DH.7ssl.gz 
│     │                 │                        ├ [115]: /usr/share/man/man7/EVP_KEYEXCH-ECDH.7ssl.gz 
│     │                 │                        ├ [116]: /usr/share/man/man7/EVP_KEYEXCH-X25519.7ssl.gz 
│     │                 │                        ├ [117]: /usr/share/man/man7/EVP_MAC-BLAKE2.7ssl.gz 
│     │                 │                        ├ [118]: /usr/share/man/man7/EVP_MAC-CMAC.7ssl.gz 
│     │                 │                        ├ [119]: /usr/share/man/man7/EVP_MAC-GMAC.7ssl.gz 
│     │                 │                        ├ [120]: /usr/share/man/man7/EVP_MAC-HMAC.7ssl.gz 
│     │                 │                        ├ [121]: /usr/share/man/man7/EVP_MAC-KMAC.7ssl.gz 
│     │                 │                        ├ [122]: /usr/share/man/man7/EVP_MAC-Poly1305.7ssl.gz 
│     │                 │                        ├ [123]: /usr/share/man/man7/EVP_MAC-Siphash.7ssl.gz 
│     │                 │                        ├ [124]: /usr/share/man/man7/EVP_MD-BLAKE2.7ssl.gz 
│     │                 │                        ├ [125]: /usr/share/man/man7/EVP_MD-KECCAK.7ssl.gz 
│     │                 │                        ├ [126]: /usr/share/man/man7/EVP_MD-MD2.7ssl.gz 
│     │                 │                        ├ [127]: /usr/share/man/man7/EVP_MD-MD4.7ssl.gz 
│     │                 │                        ├ [128]: /usr/share/man/man7/EVP_MD-MD5-SHA1.7ssl.gz 
│     │                 │                        ├ [129]: /usr/share/man/man7/EVP_MD-MD5.7ssl.gz 
│     │                 │                        ├ [130]: /usr/share/man/man7/EVP_MD-MDC2.7ssl.gz 
│     │                 │                        ├ [131]: /usr/share/man/man7/EVP_MD-NULL.7ssl.gz 
│     │                 │                        ├ [132]: /usr/share/man/man7/EVP_MD-RIPEMD160.7ssl.gz 
│     │                 │                        ├ [133]: /usr/share/man/man7/EVP_MD-SHA1.7ssl.gz 
│     │                 │                        ├ [134]: /usr/share/man/man7/EVP_MD-SHA2.7ssl.gz 
│     │                 │                        ├ [135]: /usr/share/man/man7/EVP_MD-SHA3.7ssl.gz 
│     │                 │                        ├ [136]: /usr/share/man/man7/EVP_MD-SHAKE.7ssl.gz 
│     │                 │                        ├ [137]: /usr/share/man/man7/EVP_MD-SM3.7ssl.gz 
│     │                 │                        ├ [138]: /usr/share/man/man7/EVP_MD-WHIRLPOOL.7ssl.gz 
│     │                 │                        ├ [139]: /usr/share/man/man7/EVP_MD-common.7ssl.gz 
│     │                 │                        ├ [140]: /usr/share/man/man7/EVP_PKEY-DH.7ssl.gz 
│     │                 │                        ├ [141]: /usr/share/man/man7/EVP_PKEY-DSA.7ssl.gz 
│     │                 │                        ├ [142]: /usr/share/man/man7/EVP_PKEY-EC.7ssl.gz 
│     │                 │                        ├ [143]: /usr/share/man/man7/EVP_PKEY-FFC.7ssl.gz 
│     │                 │                        ├ [144]: /usr/share/man/man7/EVP_PKEY-HMAC.7ssl.gz 
│     │                 │                        ├ [145]: /usr/share/man/man7/EVP_PKEY-RSA.7ssl.gz 
│     │                 │                        ├ [146]: /usr/share/man/man7/EVP_PKEY-SM2.7ssl.gz 
│     │                 │                        ├ [147]: /usr/share/man/man7/EVP_PKEY-X25519.7ssl.gz 
│     │                 │                        ├ [148]: /usr/share/man/man7/EVP_RAND-CRNG-TEST.7ssl.gz 
│     │                 │                        ├ [149]: /usr/share/man/man7/EVP_RAND-CTR-DRBG.7ssl.gz 
│     │                 │                        ├ [150]: /usr/share/man/man7/EVP_RAND-HASH-DRBG.7ssl.gz 
│     │                 │                        ├ [151]: /usr/share/man/man7/EVP_RAND-HMAC-DRBG.7ssl.gz 
│     │                 │                        ├ [152]: /usr/share/man/man7/EVP_RAND-JITTER.7ssl.gz 
│     │                 │                        ├ [153]: /usr/share/man/man7/EVP_RAND-SEED-SRC.7ssl.gz 
│     │                 │                        ├ [154]: /usr/share/man/man7/EVP_RAND-TEST-RAND.7ssl.gz 
│     │                 │                        ├ [155]: /usr/share/man/man7/EVP_RAND.7ssl.gz 
│     │                 │                        ├ [156]: /usr/share/man/man7/EVP_SIGNATURE-DSA.7ssl.gz 
│     │                 │                        ├ [157]: /usr/share/man/man7/EVP_SIGNATURE-ECDSA.7ssl.gz 
│     │                 │                        ├ [158]: /usr/share/man/man7/EVP_SIGNATURE-ED25519.7ssl.gz 
│     │                 │                        ├ [159]: /usr/share/man/man7/EVP_SIGNATURE-HMAC.7ssl.gz 
│     │                 │                        ├ [160]: /usr/share/man/man7/EVP_SIGNATURE-RSA.7ssl.gz 
│     │                 │                        ├ [161]: /usr/share/man/man7/OSSL_PROVIDER-FIPS.7ssl.gz 
│     │                 │                        ├ [162]: /usr/share/man/man7/OSSL_PROVIDER-base.7ssl.gz 
│     │                 │                        ├ [163]: /usr/share/man/man7/OSSL_PROVIDER-default.7ssl.gz 
│     │                 │                        ├ [164]: /usr/share/man/man7/OSSL_PROVIDER-legacy.7ssl.gz 
│     │                 │                        ├ [165]: /usr/share/man/man7/OSSL_PROVIDER-null.7ssl.gz 
│     │                 │                        ├ [166]: /usr/share/man/man7/OSSL_STORE-winstore.7ssl.gz 
│     │                 │                        ├ [167]: /usr/share/man/man7/RAND.7ssl.gz 
│     │                 │                        ├ [168]: /usr/share/man/man7/RSA-PSS.7ssl.gz 
│     │                 │                        ├ [169]: /usr/share/man/man7/X25519.7ssl.gz 
│     │                 │                        ├ [170]: /usr/share/man/man7/bio.7ssl.gz 
│     │                 │                        ├ [171]: /usr/share/man/man7/ct.7ssl.gz 
│     │                 │                        ├ [172]: /usr/share/man/man7/des_modes.7ssl.gz 
│     │                 │                        ├ [173]: /usr/share/man/man7/evp.7ssl.gz 
│     │                 │                        ├ [174]: /usr/share/man/man7/fips_module.7ssl.gz 
│     │                 │                        ├ [175]: /usr/share/man/man7/life_cycle-cipher.7ssl.gz 
│     │                 │                        ├ [176]: /usr/share/man/man7/life_cycle-digest.7ssl.gz 
│     │                 │                        ├ [177]: /usr/share/man/man7/life_cycle-kdf.7ssl.gz 
│     │                 │                        ├ [178]: /usr/share/man/man7/life_cycle-mac.7ssl.gz 
│     │                 │                        ├ [179]: /usr/share/man/man7/life_cycle-pkey.7ssl.gz 
│     │                 │                        ├ [180]: /usr/share/man/man7/life_cycle-rand.7ssl.gz 
│     │                 │                        ├ [181]: /usr/share/man/man7/openssl-core.h.7ssl.gz 
│     │                 │                        ├ [182]: /usr/share/man/man7/openssl-core_dispatch.h.7ssl.gz 
│     │                 │                        ├ [183]: /usr/share/man/man7/openssl-core_names.h.7ssl.gz 
│     │                 │                        ├ [184]: /usr/share/man/man7/openssl-env.7ssl.gz 
│     │                 │                        ├ [185]: /usr/share/man/man7/openssl-glossary.7ssl.gz 
│     │                 │                        ├ [186]: /usr/share/man/man7/openssl-qlog.7ssl.gz 
│     │                 │                        ├ [187]: /usr/share/man/man7/openssl-quic.7ssl.gz 
│     │                 │                        ├ [188]: /usr/share/man/man7/openssl-threads.7ssl.gz 
│     │                 │                        ├ [189]: /usr/share/man/man7/openssl_user_macros.7ssl.gz 
│     │                 │                        ├ [190]: /usr/share/man/man7/ossl-guide-introduction.7ssl.gz 
│     │                 │                        ├ [191]: /usr/share/man/man7/ossl-guide-libcrypto-introduction
│     │                 │                        │        .7ssl.gz 
│     │                 │                        ├ [192]: /usr/share/man/man7/ossl-guide-libraries-introduction
│     │                 │                        │        .7ssl.gz 
│     │                 │                        ├ [193]: /usr/share/man/man7/ossl-guide-libssl-introduction.7s
│     │                 │                        │        sl.gz 
│     │                 │                        ├ [194]: /usr/share/man/man7/ossl-guide-migration.7ssl.gz 
│     │                 │                        ├ [195]: /usr/share/man/man7/ossl-guide-quic-client-block.7ssl
│     │                 │                        │        .gz 
│     │                 │                        ├ [196]: /usr/share/man/man7/ossl-guide-quic-client-non-block.
│     │                 │                        │        7ssl.gz 
│     │                 │                        ├ [197]: /usr/share/man/man7/ossl-guide-quic-introduction.7ssl
│     │                 │                        │        .gz 
│     │                 │                        ├ [198]: /usr/share/man/man7/ossl-guide-quic-multi-stream.7ssl
│     │                 │                        │        .gz 
│     │                 │                        ├ [199]: /usr/share/man/man7/ossl-guide-tls-client-block.7ssl.gz 
│     │                 │                        ├ [200]: /usr/share/man/man7/ossl-guide-tls-client-non-block.7
│     │                 │                        │        ssl.gz 
│     │                 │                        ├ [201]: /usr/share/man/man7/ossl-guide-tls-introduction.7ssl.gz 
│     │                 │                        ├ [202]: /usr/share/man/man7/ossl-guide-tls-server-block.7ssl.gz 
│     │                 │                        ├ [203]: /usr/share/man/man7/ossl_store-file.7ssl.gz 
│     │                 │                        ├ [204]: /usr/share/man/man7/ossl_store.7ssl.gz 
│     │                 │                        ├ [205]: /usr/share/man/man7/passphrase-encoding.7ssl.gz 
│     │                 │                        ├ [206]: /usr/share/man/man7/property.7ssl.gz 
│     │                 │                        ├ [207]: /usr/share/man/man7/provider-asym_cipher.7ssl.gz 
│     │                 │                        ├ [208]: /usr/share/man/man7/provider-base.7ssl.gz 
│     │                 │                        ├ [209]: /usr/share/man/man7/provider-cipher.7ssl.gz 
│     │                 │                        ├ [210]: /usr/share/man/man7/provider-decoder.7ssl.gz 
│     │                 │                        ├ [211]: /usr/share/man/man7/provider-digest.7ssl.gz 
│     │                 │                        ├ [212]: /usr/share/man/man7/provider-encoder.7ssl.gz 
│     │                 │                        ├ [213]: /usr/share/man/man7/provider-kdf.7ssl.gz 
│     │                 │                        ├ [214]: /usr/share/man/man7/provider-kem.7ssl.gz 
│     │                 │                        ├ [215]: /usr/share/man/man7/provider-keyexch.7ssl.gz 
│     │                 │                        ├ [216]: /usr/share/man/man7/provider-keymgmt.7ssl.gz 
│     │                 │                        ├ [217]: /usr/share/man/man7/provider-mac.7ssl.gz 
│     │                 │                        ├ [218]: /usr/share/man/man7/provider-object.7ssl.gz 
│     │                 │                        ├ [219]: /usr/share/man/man7/provider-rand.7ssl.gz 
│     │                 │                        ├ [220]: /usr/share/man/man7/provider-signature.7ssl.gz 
│     │                 │                        ├ [221]: /usr/share/man/man7/provider-storemgmt.7ssl.gz 
│     │                 │                        ├ [222]: /usr/share/man/man7/provider.7ssl.gz 
│     │                 │                        ├ [223]: /usr/share/man/man7/proxy-certificates.7ssl.gz 
│     │                 │                        ╰ [224]: /usr/share/man/man7/x509.7ssl.gz 
│     │                 ├ [106] ╭ ID            : openssl-provider-legacy@3.4.1-1ubuntu4 
│     │                 │       ├ Name          : openssl-provider-legacy 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/openssl-provider-legacy@3.4.1-1ubuntu4?
│     │                 │       │                │       arch=amd64&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 39fe25021bab1c6e 
│     │                 │       ├ Version       : 3.4.1 
│     │                 │       ├ Release       : 1ubuntu4 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : openssl 
│     │                 │       ├ SrcVersion    : 3.4.1 
│     │                 │       ├ SrcRelease    : 1ubuntu4 
│     │                 │       ├ Licenses       ╭ [0]: Apache-2.0 
│     │                 │       │                ├ [1]: Artistic-2.0 
│     │                 │       │                ├ [2]: GPL-1.0-or-later 
│     │                 │       │                ╰ [3]: GPL-1.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ╰ [1]: libssl3t64@3.4.1-1ubuntu4 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/ossl-modules/legacy.so 
│     │                 │                        ╰ [1]: /usr/share/doc/openssl-provider-legacy/copyright 
│     │                 ├ [107] ╭ ID            : passwd@1:4.16.0-7ubuntu1 
│     │                 │       ├ Name          : passwd 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/passwd@4.16.0-7ubuntu1?arch=amd64&distr
│     │                 │       │                │       o=ubuntu-25.04&epoch=1 
│     │                 │       │                ╰ UID : 3bc9adb4bf916fa 
│     │                 │       ├ Version       : 4.16.0 
│     │                 │       ├ Release       : 7ubuntu1 
│     │                 │       ├ Epoch         : 1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : shadow 
│     │                 │       ├ SrcVersion    : 4.16.0 
│     │                 │       ├ SrcRelease    : 7ubuntu1 
│     │                 │       ├ SrcEpoch      : 1 
│     │                 │       ├ Licenses       ╭ [0]: BSD-3-Clause 
│     │                 │       │                ├ [1]: GPL-1.0-only 
│     │                 │       │                ├ [2]: GPL-2.0-or-later 
│     │                 │       │                ╰ [3]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0] : base-passwd@3.6.6 
│     │                 │       │                ├ [1] : libacl1@2.3.2-2 
│     │                 │       │                ├ [2] : libattr1@1:2.5.2-3 
│     │                 │       │                ├ [3] : libaudit1@1:4.0.2-2ubuntu2 
│     │                 │       │                ├ [4] : libbsd0@0.12.2-2 
│     │                 │       │                ├ [5] : libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [6] : libcrypt1@1:4.4.38-1 
│     │                 │       │                ├ [7] : libpam-modules@1.5.3-7ubuntu4.4 
│     │                 │       │                ├ [8] : libpam0g@1.5.3-7ubuntu4.4 
│     │                 │       │                ├ [9] : libselinux1@3.7-3ubuntu3 
│     │                 │       │                ├ [10]: libsemanage2@3.7-2.1build1 
│     │                 │       │                ╰ [11]: login.defs@1:4.16.0-7ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:7d99dab2371e2876669fc03ce11899d1028d8ce56a996fb8ce6d63
│     │                 │       │                 765d29135d 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/bin/chage 
│     │                 │                        ├ [1]  : /usr/bin/chfn 
│     │                 │                        ├ [2]  : /usr/bin/chsh 
│     │                 │                        ├ [3]  : /usr/bin/expiry 
│     │                 │                        ├ [4]  : /usr/bin/gpasswd 
│     │                 │                        ├ [5]  : /usr/bin/passwd 
│     │                 │                        ├ [6]  : /usr/lib/tmpfiles.d/passwd.conf 
│     │                 │                        ├ [7]  : /usr/sbin/chgpasswd 
│     │                 │                        ├ [8]  : /usr/sbin/chpasswd 
│     │                 │                        ├ [9]  : /usr/sbin/groupadd 
│     │                 │                        ├ [10] : /usr/sbin/groupdel 
│     │                 │                        ├ [11] : /usr/sbin/groupmod 
│     │                 │                        ├ [12] : /usr/sbin/grpck 
│     │                 │                        ├ [13] : /usr/sbin/grpconv 
│     │                 │                        ├ [14] : /usr/sbin/grpunconv 
│     │                 │                        ├ [15] : /usr/sbin/newusers 
│     │                 │                        ├ [16] : /usr/sbin/pwck 
│     │                 │                        ├ [17] : /usr/sbin/pwconv 
│     │                 │                        ├ [18] : /usr/sbin/pwunconv 
│     │                 │                        ├ [19] : /usr/sbin/shadowconfig 
│     │                 │                        ├ [20] : /usr/sbin/useradd 
│     │                 │                        ├ [21] : /usr/sbin/userdel 
│     │                 │                        ├ [22] : /usr/sbin/usermod 
│     │                 │                        ├ [23] : /usr/sbin/vipw 
│     │                 │                        ├ [24] : /usr/share/doc/passwd/NEWS.Debian.gz 
│     │                 │                        ├ [25] : /usr/share/doc/passwd/README.Debian 
│     │                 │                        ├ [26] : /usr/share/doc/passwd/TODO.Debian 
│     │                 │                        ├ [27] : /usr/share/doc/passwd/changelog.Debian.gz 
│     │                 │                        ├ [28] : /usr/share/doc/passwd/copyright 
│     │                 │                        ├ [29] : /usr/share/doc/passwd/examples/passwd.expire.cron 
│     │                 │                        ├ [30] : /usr/share/lintian/overrides/passwd 
│     │                 │                        ├ [31] : /usr/share/locale/bs/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [32] : /usr/share/locale/ca/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [33] : /usr/share/locale/cs/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [34] : /usr/share/locale/da/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [35] : /usr/share/locale/de/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [36] : /usr/share/locale/dz/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [37] : /usr/share/locale/el/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [38] : /usr/share/locale/es/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [39] : /usr/share/locale/eu/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [40] : /usr/share/locale/fi/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [41] : /usr/share/locale/fr/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [42] : /usr/share/locale/gl/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [43] : /usr/share/locale/he/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [44] : /usr/share/locale/hu/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [45] : /usr/share/locale/id/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [46] : /usr/share/locale/it/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [47] : /usr/share/locale/ja/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [48] : /usr/share/locale/ka/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [49] : /usr/share/locale/kk/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [50] : /usr/share/locale/km/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [51] : /usr/share/locale/ko/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [52] : /usr/share/locale/nb/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [53] : /usr/share/locale/ne/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [54] : /usr/share/locale/nl/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [55] : /usr/share/locale/nn/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [56] : /usr/share/locale/pl/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [57] : /usr/share/locale/pt/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [58] : /usr/share/locale/pt_BR/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [59] : /usr/share/locale/ro/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [60] : /usr/share/locale/ru/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [61] : /usr/share/locale/sk/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [62] : /usr/share/locale/sq/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [63] : /usr/share/locale/sv/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [64] : /usr/share/locale/tl/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [65] : /usr/share/locale/tr/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [66] : /usr/share/locale/uk/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [67] : /usr/share/locale/vi/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [68] : /usr/share/locale/zh_CN/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [69] : /usr/share/locale/zh_TW/LC_MESSAGES/shadow.mo 
│     │                 │                        ├ [70] : /usr/share/man/cs/man1/expiry.1.gz 
│     │                 │                        ├ [71] : /usr/share/man/cs/man1/gpasswd.1.gz 
│     │                 │                        ├ [72] : /usr/share/man/cs/man5/gshadow.5.gz 
│     │                 │                        ├ [73] : /usr/share/man/cs/man5/passwd.5.gz 
│     │                 │                        ├ [74] : /usr/share/man/cs/man5/shadow.5.gz 
│     │                 │                        ├ [75] : /usr/share/man/cs/man8/groupadd.8.gz 
│     │                 │                        ├ [76] : /usr/share/man/cs/man8/groupdel.8.gz 
│     │                 │                        ├ [77] : /usr/share/man/cs/man8/groupmod.8.gz 
│     │                 │                        ├ [78] : /usr/share/man/cs/man8/grpck.8.gz 
│     │                 │                        ├ [79] : /usr/share/man/cs/man8/vipw.8.gz 
│     │                 │                        ├ [80] : /usr/share/man/da/man1/chfn.1.gz 
│     │                 │                        ├ [81] : /usr/share/man/da/man5/gshadow.5.gz 
│     │                 │                        ├ [82] : /usr/share/man/da/man8/groupdel.8.gz 
│     │                 │                        ├ [83] : /usr/share/man/da/man8/vipw.8.gz 
│     │                 │                        ├ [84] : /usr/share/man/de/man1/chage.1.gz 
│     │                 │                        ├ [85] : /usr/share/man/de/man1/chfn.1.gz 
│     │                 │                        ├ [86] : /usr/share/man/de/man1/chsh.1.gz 
│     │                 │                        ├ [87] : /usr/share/man/de/man1/expiry.1.gz 
│     │                 │                        ├ [88] : /usr/share/man/de/man1/gpasswd.1.gz 
│     │                 │                        ├ [89] : /usr/share/man/de/man1/passwd.1.gz 
│     │                 │                        ├ [90] : /usr/share/man/de/man5/gshadow.5.gz 
│     │                 │                        ├ [91] : /usr/share/man/de/man5/passwd.5.gz 
│     │                 │                        ├ [92] : /usr/share/man/de/man5/shadow.5.gz 
│     │                 │                        ├ [93] : /usr/share/man/de/man8/chgpasswd.8.gz 
│     │                 │                        ├ [94] : /usr/share/man/de/man8/chpasswd.8.gz 
│     │                 │                        ├ [95] : /usr/share/man/de/man8/groupadd.8.gz 
│     │                 │                        ├ [96] : /usr/share/man/de/man8/groupdel.8.gz 
│     │                 │                        ├ [97] : /usr/share/man/de/man8/groupmod.8.gz 
│     │                 │                        ├ [98] : /usr/share/man/de/man8/grpck.8.gz 
│     │                 │                        ├ [99] : /usr/share/man/de/man8/newusers.8.gz 
│     │                 │                        ├ [100]: /usr/share/man/de/man8/pwck.8.gz 
│     │                 │                        ├ [101]: /usr/share/man/de/man8/pwconv.8.gz 
│     │                 │                        ├ [102]: /usr/share/man/de/man8/useradd.8.gz 
│     │                 │                        ├ [103]: /usr/share/man/de/man8/userdel.8.gz 
│     │                 │                        ├ [104]: /usr/share/man/de/man8/usermod.8.gz 
│     │                 │                        ├ [105]: /usr/share/man/de/man8/vipw.8.gz 
│     │                 │                        ├ [106]: /usr/share/man/fi/man1/chfn.1.gz 
│     │                 │                        ├ [107]: /usr/share/man/fi/man1/chsh.1.gz 
│     │                 │                        ├ [108]: /usr/share/man/fr/man1/chage.1.gz 
│     │                 │                        ├ [109]: /usr/share/man/fr/man1/chfn.1.gz 
│     │                 │                        ├ [110]: /usr/share/man/fr/man1/chsh.1.gz 
│     │                 │                        ├ [111]: /usr/share/man/fr/man1/expiry.1.gz 
│     │                 │                        ├ [112]: /usr/share/man/fr/man1/gpasswd.1.gz 
│     │                 │                        ├ [113]: /usr/share/man/fr/man1/passwd.1.gz 
│     │                 │                        ├ [114]: /usr/share/man/fr/man5/gshadow.5.gz 
│     │                 │                        ├ [115]: /usr/share/man/fr/man5/passwd.5.gz 
│     │                 │                        ├ [116]: /usr/share/man/fr/man5/shadow.5.gz 
│     │                 │                        ├ [117]: /usr/share/man/fr/man5/subgid.5.gz 
│     │                 │                        ├ [118]: /usr/share/man/fr/man5/subuid.5.gz 
│     │                 │                        ├ [119]: /usr/share/man/fr/man8/chgpasswd.8.gz 
│     │                 │                        ├ [120]: /usr/share/man/fr/man8/chpasswd.8.gz 
│     │                 │                        ├ [121]: /usr/share/man/fr/man8/groupadd.8.gz 
│     │                 │                        ├ [122]: /usr/share/man/fr/man8/groupdel.8.gz 
│     │                 │                        ├ [123]: /usr/share/man/fr/man8/groupmod.8.gz 
│     │                 │                        ├ [124]: /usr/share/man/fr/man8/grpck.8.gz 
│     │                 │                        ├ [125]: /usr/share/man/fr/man8/newusers.8.gz 
│     │                 │                        ├ [126]: /usr/share/man/fr/man8/pwck.8.gz 
│     │                 │                        ├ [127]: /usr/share/man/fr/man8/pwconv.8.gz 
│     │                 │                        ├ [128]: /usr/share/man/fr/man8/shadowconfig.8.gz 
│     │                 │                        ├ [129]: /usr/share/man/fr/man8/useradd.8.gz 
│     │                 │                        ├ [130]: /usr/share/man/fr/man8/userdel.8.gz 
│     │                 │                        ├ [131]: /usr/share/man/fr/man8/usermod.8.gz 
│     │                 │                        ├ [132]: /usr/share/man/fr/man8/vipw.8.gz 
│     │                 │                        ├ [133]: /usr/share/man/hu/man1/chsh.1.gz 
│     │                 │                        ├ [134]: /usr/share/man/hu/man1/gpasswd.1.gz 
│     │                 │                        ├ [135]: /usr/share/man/hu/man1/passwd.1.gz 
│     │                 │                        ├ [136]: /usr/share/man/hu/man5/passwd.5.gz 
│     │                 │                        ├ [137]: /usr/share/man/id/man1/chsh.1.gz 
│     │                 │                        ├ [138]: /usr/share/man/id/man8/useradd.8.gz 
│     │                 │                        ├ [139]: /usr/share/man/it/man1/chage.1.gz 
│     │                 │                        ├ [140]: /usr/share/man/it/man1/chfn.1.gz 
│     │                 │                        ├ [141]: /usr/share/man/it/man1/chsh.1.gz 
│     │                 │                        ├ [142]: /usr/share/man/it/man1/expiry.1.gz 
│     │                 │                        ├ [143]: /usr/share/man/it/man1/gpasswd.1.gz 
│     │                 │                        ├ [144]: /usr/share/man/it/man1/passwd.1.gz 
│     │                 │                        ├ [145]: /usr/share/man/it/man5/gshadow.5.gz 
│     │                 │                        ├ [146]: /usr/share/man/it/man5/passwd.5.gz 
│     │                 │                        ├ [147]: /usr/share/man/it/man5/shadow.5.gz 
│     │                 │                        ├ [148]: /usr/share/man/it/man8/chgpasswd.8.gz 
│     │                 │                        ├ [149]: /usr/share/man/it/man8/chpasswd.8.gz 
│     │                 │                        ├ [150]: /usr/share/man/it/man8/groupadd.8.gz 
│     │                 │                        ├ [151]: /usr/share/man/it/man8/groupdel.8.gz 
│     │                 │                        ├ [152]: /usr/share/man/it/man8/groupmod.8.gz 
│     │                 │                        ├ [153]: /usr/share/man/it/man8/grpck.8.gz 
│     │                 │                        ├ [154]: /usr/share/man/it/man8/newusers.8.gz 
│     │                 │                        ├ [155]: /usr/share/man/it/man8/pwck.8.gz 
│     │                 │                        ├ [156]: /usr/share/man/it/man8/pwconv.8.gz 
│     │                 │                        ├ [157]: /usr/share/man/it/man8/useradd.8.gz 
│     │                 │                        ├ [158]: /usr/share/man/it/man8/userdel.8.gz 
│     │                 │                        ├ [159]: /usr/share/man/it/man8/usermod.8.gz 
│     │                 │                        ├ [160]: /usr/share/man/it/man8/vipw.8.gz 
│     │                 │                        ├ [161]: /usr/share/man/ja/man1/chage.1.gz 
│     │                 │                        ├ [162]: /usr/share/man/ja/man1/chfn.1.gz 
│     │                 │                        ├ [163]: /usr/share/man/ja/man1/chsh.1.gz 
│     │                 │                        ├ [164]: /usr/share/man/ja/man1/expiry.1.gz 
│     │                 │                        ├ [165]: /usr/share/man/ja/man1/gpasswd.1.gz 
│     │                 │                        ├ [166]: /usr/share/man/ja/man1/passwd.1.gz 
│     │                 │                        ├ [167]: /usr/share/man/ja/man5/passwd.5.gz 
│     │                 │                        ├ [168]: /usr/share/man/ja/man5/shadow.5.gz 
│     │                 │                        ├ [169]: /usr/share/man/ja/man8/chpasswd.8.gz 
│     │                 │                        ├ [170]: /usr/share/man/ja/man8/groupadd.8.gz 
│     │                 │                        ├ [171]: /usr/share/man/ja/man8/groupdel.8.gz 
│     │                 │                        ├ [172]: /usr/share/man/ja/man8/groupmod.8.gz 
│     │                 │                        ├ [173]: /usr/share/man/ja/man8/grpck.8.gz 
│     │                 │                        ├ [174]: /usr/share/man/ja/man8/newusers.8.gz 
│     │                 │                        ├ [175]: /usr/share/man/ja/man8/pwck.8.gz 
│     │                 │                        ├ [176]: /usr/share/man/ja/man8/pwconv.8.gz 
│     │                 │                        ├ [177]: /usr/share/man/ja/man8/shadowconfig.8.gz 
│     │                 │                        ├ [178]: /usr/share/man/ja/man8/useradd.8.gz 
│     │                 │                        ├ [179]: /usr/share/man/ja/man8/userdel.8.gz 
│     │                 │                        ├ [180]: /usr/share/man/ja/man8/usermod.8.gz 
│     │                 │                        ├ [181]: /usr/share/man/ja/man8/vipw.8.gz 
│     │                 │                        ├ [182]: /usr/share/man/ko/man1/chfn.1.gz 
│     │                 │                        ├ [183]: /usr/share/man/ko/man1/chsh.1.gz 
│     │                 │                        ├ [184]: /usr/share/man/ko/man5/passwd.5.gz 
│     │                 │                        ├ [185]: /usr/share/man/ko/man8/vipw.8.gz 
│     │                 │                        ├ [186]: /usr/share/man/man1/chage.1.gz 
│     │                 │                        ├ [187]: /usr/share/man/man1/chfn.1.gz 
│     │                 │                        ├ [188]: /usr/share/man/man1/chsh.1.gz 
│     │                 │                        ├ [189]: /usr/share/man/man1/expiry.1.gz 
│     │                 │                        ├ [190]: /usr/share/man/man1/gpasswd.1.gz 
│     │                 │                        ├ [191]: /usr/share/man/man1/passwd.1.gz 
│     │                 │                        ├ [192]: /usr/share/man/man5/gshadow.5.gz 
│     │                 │                        ├ [193]: /usr/share/man/man5/passwd.5.gz 
│     │                 │                        ├ [194]: /usr/share/man/man5/shadow.5.gz 
│     │                 │                        ├ [195]: /usr/share/man/man5/subgid.5.gz 
│     │                 │                        ├ [196]: /usr/share/man/man5/subuid.5.gz 
│     │                 │                        ├ [197]: /usr/share/man/man8/chgpasswd.8.gz 
│     │                 │                        ├ [198]: /usr/share/man/man8/chpasswd.8.gz 
│     │                 │                        ├ [199]: /usr/share/man/man8/groupadd.8.gz 
│     │                 │                        ├ [200]: /usr/share/man/man8/groupdel.8.gz 
│     │                 │                        ├ [201]: /usr/share/man/man8/groupmod.8.gz 
│     │                 │                        ├ [202]: /usr/share/man/man8/grpck.8.gz 
│     │                 │                        ├ [203]: /usr/share/man/man8/newusers.8.gz 
│     │                 │                        ├ [204]: /usr/share/man/man8/pwck.8.gz 
│     │                 │                        ├ [205]: /usr/share/man/man8/pwconv.8.gz 
│     │                 │                        ├ [206]: /usr/share/man/man8/shadowconfig.8.gz 
│     │                 │                        ├ [207]: /usr/share/man/man8/useradd.8.gz 
│     │                 │                        ├ [208]: /usr/share/man/man8/userdel.8.gz 
│     │                 │                        ├ [209]: /usr/share/man/man8/usermod.8.gz 
│     │                 │                        ├ [210]: /usr/share/man/man8/vipw.8.gz 
│     │                 │                        ├ [211]: /usr/share/man/pl/man1/chage.1.gz 
│     │                 │                        ├ [212]: /usr/share/man/pl/man1/chsh.1.gz 
│     │                 │                        ├ [213]: /usr/share/man/pl/man1/expiry.1.gz 
│     │                 │                        ├ [214]: /usr/share/man/pl/man8/groupadd.8.gz 
│     │                 │                        ├ [215]: /usr/share/man/pl/man8/groupdel.8.gz 
│     │                 │                        ├ [216]: /usr/share/man/pl/man8/groupmod.8.gz 
│     │                 │                        ├ [217]: /usr/share/man/pl/man8/grpck.8.gz 
│     │                 │                        ├ [218]: /usr/share/man/pl/man8/shadowconfig.8.gz 
│     │                 │                        ├ [219]: /usr/share/man/pl/man8/userdel.8.gz 
│     │                 │                        ├ [220]: /usr/share/man/pl/man8/usermod.8.gz 
│     │                 │                        ├ [221]: /usr/share/man/pl/man8/vipw.8.gz 
│     │                 │                        ├ [222]: /usr/share/man/pt_BR/man1/gpasswd.1.gz 
│     │                 │                        ├ [223]: /usr/share/man/pt_BR/man5/passwd.5.gz 
│     │                 │                        ├ [224]: /usr/share/man/pt_BR/man5/shadow.5.gz 
│     │                 │                        ├ [225]: /usr/share/man/pt_BR/man8/groupadd.8.gz 
│     │                 │                        ├ [226]: /usr/share/man/pt_BR/man8/groupdel.8.gz 
│     │                 │                        ├ [227]: /usr/share/man/pt_BR/man8/groupmod.8.gz 
│     │                 │                        ├ [228]: /usr/share/man/ru/man1/chage.1.gz 
│     │                 │                        ├ [229]: /usr/share/man/ru/man1/chfn.1.gz 
│     │                 │                        ├ [230]: /usr/share/man/ru/man1/chsh.1.gz 
│     │                 │                        ├ [231]: /usr/share/man/ru/man1/expiry.1.gz 
│     │                 │                        ├ [232]: /usr/share/man/ru/man1/gpasswd.1.gz 
│     │                 │                        ├ [233]: /usr/share/man/ru/man1/passwd.1.gz 
│     │                 │                        ├ [234]: /usr/share/man/ru/man5/gshadow.5.gz 
│     │                 │                        ├ [235]: /usr/share/man/ru/man5/passwd.5.gz 
│     │                 │                        ├ [236]: /usr/share/man/ru/man5/shadow.5.gz 
│     │                 │                        ├ [237]: /usr/share/man/ru/man8/chgpasswd.8.gz 
│     │                 │                        ├ [238]: /usr/share/man/ru/man8/chpasswd.8.gz 
│     │                 │                        ├ [239]: /usr/share/man/ru/man8/groupadd.8.gz 
│     │                 │                        ├ [240]: /usr/share/man/ru/man8/groupdel.8.gz 
│     │                 │                        ├ [241]: /usr/share/man/ru/man8/groupmod.8.gz 
│     │                 │                        ├ [242]: /usr/share/man/ru/man8/grpck.8.gz 
│     │                 │                        ├ [243]: /usr/share/man/ru/man8/newusers.8.gz 
│     │                 │                        ├ [244]: /usr/share/man/ru/man8/pwck.8.gz 
│     │                 │                        ├ [245]: /usr/share/man/ru/man8/pwconv.8.gz 
│     │                 │                        ├ [246]: /usr/share/man/ru/man8/useradd.8.gz 
│     │                 │                        ├ [247]: /usr/share/man/ru/man8/userdel.8.gz 
│     │                 │                        ├ [248]: /usr/share/man/ru/man8/usermod.8.gz 
│     │                 │                        ├ [249]: /usr/share/man/ru/man8/vipw.8.gz 
│     │                 │                        ├ [250]: /usr/share/man/sv/man1/chage.1.gz 
│     │                 │                        ├ [251]: /usr/share/man/sv/man1/chsh.1.gz 
│     │                 │                        ├ [252]: /usr/share/man/sv/man1/expiry.1.gz 
│     │                 │                        ├ [253]: /usr/share/man/sv/man1/passwd.1.gz 
│     │                 │                        ├ [254]: /usr/share/man/sv/man5/gshadow.5.gz 
│     │                 │                        ├ [255]: /usr/share/man/sv/man5/passwd.5.gz 
│     │                 │                        ├ [256]: /usr/share/man/sv/man8/groupadd.8.gz 
│     │                 │                        ├ [257]: /usr/share/man/sv/man8/groupdel.8.gz 
│     │                 │                        ├ [258]: /usr/share/man/sv/man8/groupmod.8.gz 
│     │                 │                        ├ [259]: /usr/share/man/sv/man8/grpck.8.gz 
│     │                 │                        ├ [260]: /usr/share/man/sv/man8/pwck.8.gz 
│     │                 │                        ├ [261]: /usr/share/man/sv/man8/userdel.8.gz 
│     │                 │                        ├ [262]: /usr/share/man/sv/man8/vipw.8.gz 
│     │                 │                        ├ [263]: /usr/share/man/tr/man1/chage.1.gz 
│     │                 │                        ├ [264]: /usr/share/man/tr/man1/chfn.1.gz 
│     │                 │                        ├ [265]: /usr/share/man/tr/man1/passwd.1.gz 
│     │                 │                        ├ [266]: /usr/share/man/tr/man5/passwd.5.gz 
│     │                 │                        ├ [267]: /usr/share/man/tr/man5/shadow.5.gz 
│     │                 │                        ├ [268]: /usr/share/man/tr/man8/groupadd.8.gz 
│     │                 │                        ├ [269]: /usr/share/man/tr/man8/groupdel.8.gz 
│     │                 │                        ├ [270]: /usr/share/man/tr/man8/groupmod.8.gz 
│     │                 │                        ├ [271]: /usr/share/man/tr/man8/useradd.8.gz 
│     │                 │                        ├ [272]: /usr/share/man/tr/man8/userdel.8.gz 
│     │                 │                        ├ [273]: /usr/share/man/tr/man8/usermod.8.gz 
│     │                 │                        ├ [274]: /usr/share/man/uk/man1/chage.1.gz 
│     │                 │                        ├ [275]: /usr/share/man/uk/man1/chfn.1.gz 
│     │                 │                        ├ [276]: /usr/share/man/uk/man1/chsh.1.gz 
│     │                 │                        ├ [277]: /usr/share/man/uk/man1/expiry.1.gz 
│     │                 │                        ├ [278]: /usr/share/man/uk/man1/gpasswd.1.gz 
│     │                 │                        ├ [279]: /usr/share/man/uk/man1/passwd.1.gz 
│     │                 │                        ├ [280]: /usr/share/man/uk/man5/gshadow.5.gz 
│     │                 │                        ├ [281]: /usr/share/man/uk/man5/passwd.5.gz 
│     │                 │                        ├ [282]: /usr/share/man/uk/man5/shadow.5.gz 
│     │                 │                        ├ [283]: /usr/share/man/uk/man8/chgpasswd.8.gz 
│     │                 │                        ├ [284]: /usr/share/man/uk/man8/chpasswd.8.gz 
│     │                 │                        ├ [285]: /usr/share/man/uk/man8/groupadd.8.gz 
│     │                 │                        ├ [286]: /usr/share/man/uk/man8/groupdel.8.gz 
│     │                 │                        ├ [287]: /usr/share/man/uk/man8/groupmod.8.gz 
│     │                 │                        ├ [288]: /usr/share/man/uk/man8/grpck.8.gz 
│     │                 │                        ├ [289]: /usr/share/man/uk/man8/newusers.8.gz 
│     │                 │                        ├ [290]: /usr/share/man/uk/man8/pwck.8.gz 
│     │                 │                        ├ [291]: /usr/share/man/uk/man8/pwconv.8.gz 
│     │                 │                        ├ [292]: /usr/share/man/uk/man8/useradd.8.gz 
│     │                 │                        ├ [293]: /usr/share/man/uk/man8/userdel.8.gz 
│     │                 │                        ├ [294]: /usr/share/man/uk/man8/usermod.8.gz 
│     │                 │                        ├ [295]: /usr/share/man/uk/man8/vipw.8.gz 
│     │                 │                        ├ [296]: /usr/share/man/zh_CN/man1/chage.1.gz 
│     │                 │                        ├ [297]: /usr/share/man/zh_CN/man1/chfn.1.gz 
│     │                 │                        ├ [298]: /usr/share/man/zh_CN/man1/chsh.1.gz 
│     │                 │                        ├ [299]: /usr/share/man/zh_CN/man1/expiry.1.gz 
│     │                 │                        ├ [300]: /usr/share/man/zh_CN/man1/gpasswd.1.gz 
│     │                 │                        ├ [301]: /usr/share/man/zh_CN/man1/passwd.1.gz 
│     │                 │                        ├ [302]: /usr/share/man/zh_CN/man5/gshadow.5.gz 
│     │                 │                        ├ [303]: /usr/share/man/zh_CN/man5/passwd.5.gz 
│     │                 │                        ├ [304]: /usr/share/man/zh_CN/man5/shadow.5.gz 
│     │                 │                        ├ [305]: /usr/share/man/zh_CN/man8/chgpasswd.8.gz 
│     │                 │                        ├ [306]: /usr/share/man/zh_CN/man8/chpasswd.8.gz 
│     │                 │                        ├ [307]: /usr/share/man/zh_CN/man8/groupadd.8.gz 
│     │                 │                        ├ [308]: /usr/share/man/zh_CN/man8/groupdel.8.gz 
│     │                 │                        ├ [309]: /usr/share/man/zh_CN/man8/groupmod.8.gz 
│     │                 │                        ├ [310]: /usr/share/man/zh_CN/man8/grpck.8.gz 
│     │                 │                        ├ [311]: /usr/share/man/zh_CN/man8/newusers.8.gz 
│     │                 │                        ├ [312]: /usr/share/man/zh_CN/man8/pwck.8.gz 
│     │                 │                        ├ [313]: /usr/share/man/zh_CN/man8/pwconv.8.gz 
│     │                 │                        ├ [314]: /usr/share/man/zh_CN/man8/useradd.8.gz 
│     │                 │                        ├ [315]: /usr/share/man/zh_CN/man8/userdel.8.gz 
│     │                 │                        ├ [316]: /usr/share/man/zh_CN/man8/usermod.8.gz 
│     │                 │                        ├ [317]: /usr/share/man/zh_CN/man8/vipw.8.gz 
│     │                 │                        ├ [318]: /usr/share/man/zh_TW/man1/chfn.1.gz 
│     │                 │                        ├ [319]: /usr/share/man/zh_TW/man1/chsh.1.gz 
│     │                 │                        ├ [320]: /usr/share/man/zh_TW/man5/passwd.5.gz 
│     │                 │                        ├ [321]: /usr/share/man/zh_TW/man8/chpasswd.8.gz 
│     │                 │                        ├ [322]: /usr/share/man/zh_TW/man8/groupadd.8.gz 
│     │                 │                        ├ [323]: /usr/share/man/zh_TW/man8/groupdel.8.gz 
│     │                 │                        ├ [324]: /usr/share/man/zh_TW/man8/groupmod.8.gz 
│     │                 │                        ├ [325]: /usr/share/man/zh_TW/man8/useradd.8.gz 
│     │                 │                        ├ [326]: /usr/share/man/zh_TW/man8/userdel.8.gz 
│     │                 │                        ╰ [327]: /usr/share/man/zh_TW/man8/usermod.8.gz 
│     │                 ├ [108] ╭ ID            : perl-base@5.40.1-2ubuntu0.2 
│     │                 │       ├ Name          : perl-base 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/perl-base@5.40.1-2ubuntu0.2?arch=amd64&
│     │                 │       │                │       distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 5f19e7d42ba79591 
│     │                 │       ├ Version       : 5.40.1 
│     │                 │       ├ Release       : 2ubuntu0.2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : perl 
│     │                 │       ├ SrcVersion    : 5.40.1 
│     │                 │       ├ SrcRelease    : 2ubuntu0.2 
│     │                 │       ├ Licenses       ╭ [0] : GPL-1.0-or-later 
│     │                 │       │                ├ [1] : Artistic-2.0 
│     │                 │       │                ├ [2] : MIT 
│     │                 │       │                ├ [3] : REGCOMP 
│     │                 │       │                ├ [4] : GPL-2.0-with-bison-exception+ 
│     │                 │       │                ├ [5] : Unicode 
│     │                 │       │                ├ [6] : BZIP 
│     │                 │       │                ├ [7] : Zlib 
│     │                 │       │                ├ [8] : GPL-2.0-or-later 
│     │                 │       │                ├ [9] : FSFAP 
│     │                 │       │                ├ [10]: BSD-3-clause-with-weird-numbering 
│     │                 │       │                ├ [11]: CC0-1.0 
│     │                 │       │                ├ [12]: TEXT-TABS 
│     │                 │       │                ├ [13]: BSD-4-clause-POWERDOG 
│     │                 │       │                ├ [14]: BSD-3-clause-GENERIC 
│     │                 │       │                ├ [15]: BSD-3-Clause 
│     │                 │       │                ├ [16]: SDBM-PUBLIC-DOMAIN 
│     │                 │       │                ├ [17]: DONT-CHANGE-THE-GPL 
│     │                 │       │                ├ [18]: Artistic-dist 
│     │                 │       │                ├ [19]: LGPL-2.1-only 
│     │                 │       │                ├ [20]: GPL-1.0-only 
│     │                 │       │                ├ [21]: GPL-2.0-only 
│     │                 │       │                ╰ [22]: Artistic-2 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/bin/perl 
│     │                 │                        ├ [1]  : /usr/bin/perl5.40.1 
│     │                 │                        ├ [2]  : /usr/lib/x86_64-linux-gnu/perl-base/AutoLoader.pm 
│     │                 │                        ├ [3]  : /usr/lib/x86_64-linux-gnu/perl-base/Carp.pm 
│     │                 │                        ├ [4]  : /usr/lib/x86_64-linux-gnu/perl-base/Carp/Heavy.pm 
│     │                 │                        ├ [5]  : /usr/lib/x86_64-linux-gnu/perl-base/Config.pm 
│     │                 │                        ├ [6]  : /usr/lib/x86_64-linux-gnu/perl-base/Config_git.pl 
│     │                 │                        ├ [7]  : /usr/lib/x86_64-linux-gnu/perl-base/Config_heavy.pl 
│     │                 │                        ├ [8]  : /usr/lib/x86_64-linux-gnu/perl-base/Cwd.pm 
│     │                 │                        ├ [9]  : /usr/lib/x86_64-linux-gnu/perl-base/DynaLoader.pm 
│     │                 │                        ├ [10] : /usr/lib/x86_64-linux-gnu/perl-base/Errno.pm 
│     │                 │                        ├ [11] : /usr/lib/x86_64-linux-gnu/perl-base/Exporter.pm 
│     │                 │                        ├ [12] : /usr/lib/x86_64-linux-gnu/perl-base/Exporter/Heavy.pm 
│     │                 │                        ├ [13] : /usr/lib/x86_64-linux-gnu/perl-base/Fcntl.pm 
│     │                 │                        ├ [14] : /usr/lib/x86_64-linux-gnu/perl-base/File/Basename.pm 
│     │                 │                        ├ [15] : /usr/lib/x86_64-linux-gnu/perl-base/File/Glob.pm 
│     │                 │                        ├ [16] : /usr/lib/x86_64-linux-gnu/perl-base/File/Path.pm 
│     │                 │                        ├ [17] : /usr/lib/x86_64-linux-gnu/perl-base/File/Spec.pm 
│     │                 │                        ├ [18] : /usr/lib/x86_64-linux-gnu/perl-base/File/Spec/Unix.pm 
│     │                 │                        ├ [19] : /usr/lib/x86_64-linux-gnu/perl-base/File/Temp.pm 
│     │                 │                        ├ [20] : /usr/lib/x86_64-linux-gnu/perl-base/FileHandle.pm 
│     │                 │                        ├ [21] : /usr/lib/x86_64-linux-gnu/perl-base/Getopt/Long.pm 
│     │                 │                        ├ [22] : /usr/lib/x86_64-linux-gnu/perl-base/Getopt/Long/Parse
│     │                 │                        │        r.pm 
│     │                 │                        ├ [23] : /usr/lib/x86_64-linux-gnu/perl-base/Hash/Util.pm 
│     │                 │                        ├ [24] : /usr/lib/x86_64-linux-gnu/perl-base/IO.pm 
│     │                 │                        ├ [25] : /usr/lib/x86_64-linux-gnu/perl-base/IO/File.pm 
│     │                 │                        ├ [26] : /usr/lib/x86_64-linux-gnu/perl-base/IO/Handle.pm 
│     │                 │                        ├ [27] : /usr/lib/x86_64-linux-gnu/perl-base/IO/Pipe.pm 
│     │                 │                        ├ [28] : /usr/lib/x86_64-linux-gnu/perl-base/IO/Seekable.pm 
│     │                 │                        ├ [29] : /usr/lib/x86_64-linux-gnu/perl-base/IO/Select.pm 
│     │                 │                        ├ [30] : /usr/lib/x86_64-linux-gnu/perl-base/IO/Socket.pm 
│     │                 │                        ├ [31] : /usr/lib/x86_64-linux-gnu/perl-base/IO/Socket/INET.pm 
│     │                 │                        ├ [32] : /usr/lib/x86_64-linux-gnu/perl-base/IO/Socket/IP.pm 
│     │                 │                        ├ [33] : /usr/lib/x86_64-linux-gnu/perl-base/IO/Socket/UNIX.pm 
│     │                 │                        ├ [34] : /usr/lib/x86_64-linux-gnu/perl-base/IPC/Open2.pm 
│     │                 │                        ├ [35] : /usr/lib/x86_64-linux-gnu/perl-base/IPC/Open3.pm 
│     │                 │                        ├ [36] : /usr/lib/x86_64-linux-gnu/perl-base/List/Util.pm 
│     │                 │                        ├ [37] : /usr/lib/x86_64-linux-gnu/perl-base/POSIX.pm 
│     │                 │                        ├ [38] : /usr/lib/x86_64-linux-gnu/perl-base/Scalar/Util.pm 
│     │                 │                        ├ [39] : /usr/lib/x86_64-linux-gnu/perl-base/SelectSaver.pm 
│     │                 │                        ├ [40] : /usr/lib/x86_64-linux-gnu/perl-base/Socket.pm 
│     │                 │                        ├ [41] : /usr/lib/x86_64-linux-gnu/perl-base/Symbol.pm 
│     │                 │                        ├ [42] : /usr/lib/x86_64-linux-gnu/perl-base/Text/ParseWords.pm 
│     │                 │                        ├ [43] : /usr/lib/x86_64-linux-gnu/perl-base/Text/Tabs.pm 
│     │                 │                        ├ [44] : /usr/lib/x86_64-linux-gnu/perl-base/Text/Wrap.pm 
│     │                 │                        ├ [45] : /usr/lib/x86_64-linux-gnu/perl-base/Tie/Hash.pm 
│     │                 │                        ├ [46] : /usr/lib/x86_64-linux-gnu/perl-base/XSLoader.pm 
│     │                 │                        ├ [47] : /usr/lib/x86_64-linux-gnu/perl-base/attributes.pm 
│     │                 │                        ├ [48] : /usr/lib/x86_64-linux-gnu/perl-base/auto/Cwd/Cwd.so 
│     │                 │                        ├ [49] : /usr/lib/x86_64-linux-gnu/perl-base/auto/Fcntl/Fcntl.so 
│     │                 │                        ├ [50] : /usr/lib/x86_64-linux-gnu/perl-base/auto/File/Glob/Gl
│     │                 │                        │        ob.so 
│     │                 │                        ├ [51] : /usr/lib/x86_64-linux-gnu/perl-base/auto/Hash/Util/Ut
│     │                 │                        │        il.so 
│     │                 │                        ├ [52] : /usr/lib/x86_64-linux-gnu/perl-base/auto/IO/IO.so 
│     │                 │                        ├ [53] : /usr/lib/x86_64-linux-gnu/perl-base/auto/List/Util/Ut
│     │                 │                        │        il.so 
│     │                 │                        ├ [54] : /usr/lib/x86_64-linux-gnu/perl-base/auto/POSIX/POSIX.so 
│     │                 │                        ├ [55] : /usr/lib/x86_64-linux-gnu/perl-base/auto/Socket/Socke
│     │                 │                        │        t.so 
│     │                 │                        ├ [56] : /usr/lib/x86_64-linux-gnu/perl-base/auto/attributes/a
│     │                 │                        │        ttributes.so 
│     │                 │                        ├ [57] : /usr/lib/x86_64-linux-gnu/perl-base/auto/re/re.so 
│     │                 │                        ├ [58] : /usr/lib/x86_64-linux-gnu/perl-base/base.pm 
│     │                 │                        ├ [59] : /usr/lib/x86_64-linux-gnu/perl-base/builtin.pm 
│     │                 │                        ├ [60] : /usr/lib/x86_64-linux-gnu/perl-base/bytes.pm 
│     │                 │                        ├ [61] : /usr/lib/x86_64-linux-gnu/perl-base/constant.pm 
│     │                 │                        ├ [62] : /usr/lib/x86_64-linux-gnu/perl-base/feature.pm 
│     │                 │                        ├ [63] : /usr/lib/x86_64-linux-gnu/perl-base/fields.pm 
│     │                 │                        ├ [64] : /usr/lib/x86_64-linux-gnu/perl-base/integer.pm 
│     │                 │                        ├ [65] : /usr/lib/x86_64-linux-gnu/perl-base/lib.pm 
│     │                 │                        ├ [66] : /usr/lib/x86_64-linux-gnu/perl-base/locale.pm 
│     │                 │                        ├ [67] : /usr/lib/x86_64-linux-gnu/perl-base/overload.pm 
│     │                 │                        ├ [68] : /usr/lib/x86_64-linux-gnu/perl-base/overloading.pm 
│     │                 │                        ├ [69] : /usr/lib/x86_64-linux-gnu/perl-base/parent.pm 
│     │                 │                        ├ [70] : /usr/lib/x86_64-linux-gnu/perl-base/re.pm 
│     │                 │                        ├ [71] : /usr/lib/x86_64-linux-gnu/perl-base/strict.pm 
│     │                 │                        ├ [72] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Age.pl 
│     │                 │                        ├ [73] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Bc.pl 
│     │                 │                        ├ [74] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Bmg.pl 
│     │                 │                        ├ [75] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Bpb.pl 
│     │                 │                        ├ [76] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Bpt.pl 
│     │                 │                        ├ [77] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Cf.pl 
│     │                 │                        ├ [78] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Ea.pl 
│     │                 │                        ├ [79] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/EqUIde
│     │                 │                        │        o.pl 
│     │                 │                        ├ [80] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/GCB.pl 
│     │                 │                        ├ [81] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Gc.pl 
│     │                 │                        ├ [82] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Hst.pl 
│     │                 │                        ├ [83] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Identi
│     │                 │                        │        f2.pl 
│     │                 │                        ├ [84] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Identi
│     │                 │                        │        fi.pl 
│     │                 │                        ├ [85] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/InPC.pl 
│     │                 │                        ├ [86] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/InSC.pl 
│     │                 │                        ├ [87] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Isc.pl 
│     │                 │                        ├ [88] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Jg.pl 
│     │                 │                        ├ [89] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Jt.pl 
│     │                 │                        ├ [90] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Lb.pl 
│     │                 │                        ├ [91] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Lc.pl 
│     │                 │                        ├ [92] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/NFCQC.pl 
│     │                 │                        ├ [93] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/NFDQC.pl 
│     │                 │                        ├ [94] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/NFKCCF
│     │                 │                        │        .pl 
│     │                 │                        ├ [95] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/NFKCQC
│     │                 │                        │        .pl 
│     │                 │                        ├ [96] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/NFKDQC
│     │                 │                        │        .pl 
│     │                 │                        ├ [97] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Na1.pl 
│     │                 │                        ├ [98] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/NameAl
│     │                 │                        │        ia.pl 
│     │                 │                        ├ [99] : /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Nt.pl 
│     │                 │                        ├ [100]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Nv.pl 
│     │                 │                        ├ [101]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/PerlDe
│     │                 │                        │        ci.pl 
│     │                 │                        ├ [102]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/SB.pl 
│     │                 │                        ├ [103]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Sc.pl 
│     │                 │                        ├ [104]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Scx.pl 
│     │                 │                        ├ [105]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Tc.pl 
│     │                 │                        ├ [106]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Uc.pl 
│     │                 │                        ├ [107]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/Vo.pl 
│     │                 │                        ├ [108]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/WB.pl 
│     │                 │                        ├ [109]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/_PerlL
│     │                 │                        │        B.pl 
│     │                 │                        ├ [110]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/To/_PerlS
│     │                 │                        │        CX.pl 
│     │                 │                        ├ [111]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/N
│     │                 │                        │        A.pl 
│     │                 │                        ├ [112]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        100.pl 
│     │                 │                        ├ [113]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        11.pl 
│     │                 │                        ├ [114]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        110.pl 
│     │                 │                        ├ [115]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        120.pl 
│     │                 │                        ├ [116]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        130.pl 
│     │                 │                        ├ [117]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        140.pl 
│     │                 │                        ├ [118]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        150.pl 
│     │                 │                        ├ [119]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        20.pl 
│     │                 │                        ├ [120]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        30.pl 
│     │                 │                        ├ [121]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        31.pl 
│     │                 │                        ├ [122]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        32.pl 
│     │                 │                        ├ [123]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        40.pl 
│     │                 │                        ├ [124]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        41.pl 
│     │                 │                        ├ [125]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        50.pl 
│     │                 │                        ├ [126]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        51.pl 
│     │                 │                        ├ [127]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        52.pl 
│     │                 │                        ├ [128]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        60.pl 
│     │                 │                        ├ [129]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        61.pl 
│     │                 │                        ├ [130]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        70.pl 
│     │                 │                        ├ [131]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        80.pl 
│     │                 │                        ├ [132]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Age/V
│     │                 │                        │        90.pl 
│     │                 │                        ├ [133]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Alpha
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [134]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/AL
│     │                 │                        │        .pl 
│     │                 │                        ├ [135]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/AN
│     │                 │                        │        .pl 
│     │                 │                        ├ [136]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/B.pl 
│     │                 │                        ├ [137]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/BN
│     │                 │                        │        .pl 
│     │                 │                        ├ [138]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/CS
│     │                 │                        │        .pl 
│     │                 │                        ├ [139]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/EN
│     │                 │                        │        .pl 
│     │                 │                        ├ [140]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/ES
│     │                 │                        │        .pl 
│     │                 │                        ├ [141]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/ET
│     │                 │                        │        .pl 
│     │                 │                        ├ [142]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/L.pl 
│     │                 │                        ├ [143]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/NS
│     │                 │                        │        M.pl 
│     │                 │                        ├ [144]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/ON
│     │                 │                        │        .pl 
│     │                 │                        ├ [145]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/R.pl 
│     │                 │                        ├ [146]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bc/WS
│     │                 │                        │        .pl 
│     │                 │                        ├ [147]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/BidiC
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [148]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/BidiM
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [149]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Blk/N
│     │                 │                        │        B.pl 
│     │                 │                        ├ [150]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bpt/C
│     │                 │                        │        .pl 
│     │                 │                        ├ [151]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bpt/N
│     │                 │                        │        .pl 
│     │                 │                        ├ [152]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Bpt/O
│     │                 │                        │        .pl 
│     │                 │                        ├ [153]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/CE/Y.pl 
│     │                 │                        ├ [154]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/CI/Y.pl 
│     │                 │                        ├ [155]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/CWCF/
│     │                 │                        │        Y.pl 
│     │                 │                        ├ [156]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/CWCM/
│     │                 │                        │        Y.pl 
│     │                 │                        ├ [157]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/CWKCF
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [158]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/CWL/Y
│     │                 │                        │        .pl 
│     │                 │                        ├ [159]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/CWT/Y
│     │                 │                        │        .pl 
│     │                 │                        ├ [160]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/CWU/Y
│     │                 │                        │        .pl 
│     │                 │                        ├ [161]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Cased
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [162]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ccc/A
│     │                 │                        │        .pl 
│     │                 │                        ├ [163]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ccc/A
│     │                 │                        │        L.pl 
│     │                 │                        ├ [164]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ccc/A
│     │                 │                        │        R.pl 
│     │                 │                        ├ [165]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ccc/A
│     │                 │                        │        TAR.pl 
│     │                 │                        ├ [166]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ccc/B
│     │                 │                        │        .pl 
│     │                 │                        ├ [167]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ccc/B
│     │                 │                        │        R.pl 
│     │                 │                        ├ [168]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ccc/D
│     │                 │                        │        B.pl 
│     │                 │                        ├ [169]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ccc/N
│     │                 │                        │        K.pl 
│     │                 │                        ├ [170]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ccc/N
│     │                 │                        │        R.pl 
│     │                 │                        ├ [171]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ccc/O
│     │                 │                        │        V.pl 
│     │                 │                        ├ [172]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ccc/V
│     │                 │                        │        R.pl 
│     │                 │                        ├ [173]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/CompE
│     │                 │                        │        x/Y.pl 
│     │                 │                        ├ [174]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/DI/Y.pl 
│     │                 │                        ├ [175]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dash/
│     │                 │                        │        Y.pl 
│     │                 │                        ├ [176]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dep/Y
│     │                 │                        │        .pl 
│     │                 │                        ├ [177]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dia/Y
│     │                 │                        │        .pl 
│     │                 │                        ├ [178]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/Co
│     │                 │                        │        m.pl 
│     │                 │                        ├ [179]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/En
│     │                 │                        │        c.pl 
│     │                 │                        ├ [180]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/Fi
│     │                 │                        │        n.pl 
│     │                 │                        ├ [181]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/Fo
│     │                 │                        │        nt.pl 
│     │                 │                        ├ [182]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/In
│     │                 │                        │        it.pl 
│     │                 │                        ├ [183]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/Is
│     │                 │                        │        o.pl 
│     │                 │                        ├ [184]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/Me
│     │                 │                        │        d.pl 
│     │                 │                        ├ [185]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/Na
│     │                 │                        │        r.pl 
│     │                 │                        ├ [186]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/Nb
│     │                 │                        │        .pl 
│     │                 │                        ├ [187]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/No
│     │                 │                        │        nCanon.pl 
│     │                 │                        ├ [188]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/Sq
│     │                 │                        │        r.pl 
│     │                 │                        ├ [189]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/Su
│     │                 │                        │        b.pl 
│     │                 │                        ├ [190]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/Su
│     │                 │                        │        p.pl 
│     │                 │                        ├ [191]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Dt/Ve
│     │                 │                        │        rt.pl 
│     │                 │                        ├ [192]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/EBase
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [193]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/EComp
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [194]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/EPres
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [195]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ea/A.pl 
│     │                 │                        ├ [196]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ea/H.pl 
│     │                 │                        ├ [197]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ea/N.pl 
│     │                 │                        ├ [198]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ea/Na
│     │                 │                        │        .pl 
│     │                 │                        ├ [199]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ea/W.pl 
│     │                 │                        ├ [200]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Emoji
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [201]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ext/Y
│     │                 │                        │        .pl 
│     │                 │                        ├ [202]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/ExtPi
│     │                 │                        │        ct/Y.pl 
│     │                 │                        ├ [203]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/GCB/C
│     │                 │                        │        N.pl 
│     │                 │                        ├ [204]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/GCB/E
│     │                 │                        │        X.pl 
│     │                 │                        ├ [205]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/GCB/L
│     │                 │                        │        V.pl 
│     │                 │                        ├ [206]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/GCB/L
│     │                 │                        │        VT.pl 
│     │                 │                        ├ [207]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/GCB/P
│     │                 │                        │        P.pl 
│     │                 │                        ├ [208]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/GCB/S
│     │                 │                        │        M.pl 
│     │                 │                        ├ [209]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/GCB/X
│     │                 │                        │        X.pl 
│     │                 │                        ├ [210]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/C.pl 
│     │                 │                        ├ [211]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Cf
│     │                 │                        │        .pl 
│     │                 │                        ├ [212]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Cn
│     │                 │                        │        .pl 
│     │                 │                        ├ [213]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/L.pl 
│     │                 │                        ├ [214]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/LC
│     │                 │                        │        .pl 
│     │                 │                        ├ [215]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Ll
│     │                 │                        │        .pl 
│     │                 │                        ├ [216]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Lm
│     │                 │                        │        .pl 
│     │                 │                        ├ [217]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Lo
│     │                 │                        │        .pl 
│     │                 │                        ├ [218]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Lu
│     │                 │                        │        .pl 
│     │                 │                        ├ [219]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/M.pl 
│     │                 │                        ├ [220]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Mc
│     │                 │                        │        .pl 
│     │                 │                        ├ [221]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Me
│     │                 │                        │        .pl 
│     │                 │                        ├ [222]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Mn
│     │                 │                        │        .pl 
│     │                 │                        ├ [223]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/N.pl 
│     │                 │                        ├ [224]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Nd
│     │                 │                        │        .pl 
│     │                 │                        ├ [225]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Nl
│     │                 │                        │        .pl 
│     │                 │                        ├ [226]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/No
│     │                 │                        │        .pl 
│     │                 │                        ├ [227]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/P.pl 
│     │                 │                        ├ [228]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Pc
│     │                 │                        │        .pl 
│     │                 │                        ├ [229]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Pd
│     │                 │                        │        .pl 
│     │                 │                        ├ [230]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Pe
│     │                 │                        │        .pl 
│     │                 │                        ├ [231]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Pf
│     │                 │                        │        .pl 
│     │                 │                        ├ [232]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Pi
│     │                 │                        │        .pl 
│     │                 │                        ├ [233]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Po
│     │                 │                        │        .pl 
│     │                 │                        ├ [234]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Ps
│     │                 │                        │        .pl 
│     │                 │                        ├ [235]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/S.pl 
│     │                 │                        ├ [236]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Sc
│     │                 │                        │        .pl 
│     │                 │                        ├ [237]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Sk
│     │                 │                        │        .pl 
│     │                 │                        ├ [238]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Sm
│     │                 │                        │        .pl 
│     │                 │                        ├ [239]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/So
│     │                 │                        │        .pl 
│     │                 │                        ├ [240]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Z.pl 
│     │                 │                        ├ [241]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Gc/Zs
│     │                 │                        │        .pl 
│     │                 │                        ├ [242]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/GrBas
│     │                 │                        │        e/Y.pl 
│     │                 │                        ├ [243]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/GrExt
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [244]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Hex/Y
│     │                 │                        │        .pl 
│     │                 │                        ├ [245]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Hst/N
│     │                 │                        │        A.pl 
│     │                 │                        ├ [246]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Hyphe
│     │                 │                        │        n/T.pl 
│     │                 │                        ├ [247]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IDC/Y
│     │                 │                        │        .pl 
│     │                 │                        ├ [248]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IDS/Y
│     │                 │                        │        .pl 
│     │                 │                        ├ [249]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdSta
│     │                 │                        │        tus/Allowed.pl 
│     │                 │                        ├ [250]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdSta
│     │                 │                        │        tus/Restrict.pl 
│     │                 │                        ├ [251]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdTyp
│     │                 │                        │        e/DefaultI.pl 
│     │                 │                        ├ [252]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdTyp
│     │                 │                        │        e/Exclusio.pl 
│     │                 │                        ├ [253]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdTyp
│     │                 │                        │        e/Inclusio.pl 
│     │                 │                        ├ [254]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdTyp
│     │                 │                        │        e/LimitedU.pl 
│     │                 │                        ├ [255]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdTyp
│     │                 │                        │        e/NotChara.pl 
│     │                 │                        ├ [256]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdTyp
│     │                 │                        │        e/NotNFKC.pl 
│     │                 │                        ├ [257]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdTyp
│     │                 │                        │        e/NotXID.pl 
│     │                 │                        ├ [258]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdTyp
│     │                 │                        │        e/Obsolete.pl 
│     │                 │                        ├ [259]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdTyp
│     │                 │                        │        e/Recommen.pl 
│     │                 │                        ├ [260]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdTyp
│     │                 │                        │        e/Technica.pl 
│     │                 │                        ├ [261]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/IdTyp
│     │                 │                        │        e/Uncommon.pl 
│     │                 │                        ├ [262]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Ideo/
│     │                 │                        │        Y.pl 
│     │                 │                        ├ [263]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/10
│     │                 │                        │        _0.pl 
│     │                 │                        ├ [264]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/11
│     │                 │                        │        _0.pl 
│     │                 │                        ├ [265]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/12
│     │                 │                        │        _0.pl 
│     │                 │                        ├ [266]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/12
│     │                 │                        │        _1.pl 
│     │                 │                        ├ [267]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/13
│     │                 │                        │        _0.pl 
│     │                 │                        ├ [268]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/14
│     │                 │                        │        _0.pl 
│     │                 │                        ├ [269]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/15
│     │                 │                        │        _0.pl 
│     │                 │                        ├ [270]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/2_
│     │                 │                        │        0.pl 
│     │                 │                        ├ [271]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/2_
│     │                 │                        │        1.pl 
│     │                 │                        ├ [272]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/3_
│     │                 │                        │        0.pl 
│     │                 │                        ├ [273]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/3_
│     │                 │                        │        1.pl 
│     │                 │                        ├ [274]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/3_
│     │                 │                        │        2.pl 
│     │                 │                        ├ [275]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/4_
│     │                 │                        │        0.pl 
│     │                 │                        ├ [276]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/4_
│     │                 │                        │        1.pl 
│     │                 │                        ├ [277]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/5_
│     │                 │                        │        0.pl 
│     │                 │                        ├ [278]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/5_
│     │                 │                        │        1.pl 
│     │                 │                        ├ [279]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/5_
│     │                 │                        │        2.pl 
│     │                 │                        ├ [280]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/6_
│     │                 │                        │        0.pl 
│     │                 │                        ├ [281]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/6_
│     │                 │                        │        1.pl 
│     │                 │                        ├ [282]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/6_
│     │                 │                        │        2.pl 
│     │                 │                        ├ [283]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/6_
│     │                 │                        │        3.pl 
│     │                 │                        ├ [284]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/7_
│     │                 │                        │        0.pl 
│     │                 │                        ├ [285]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/8_
│     │                 │                        │        0.pl 
│     │                 │                        ├ [286]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/In/9_
│     │                 │                        │        0.pl 
│     │                 │                        ├ [287]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        Bottom.pl 
│     │                 │                        ├ [288]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        BottomAn.pl 
│     │                 │                        ├ [289]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        Left.pl 
│     │                 │                        ├ [290]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        LeftAndR.pl 
│     │                 │                        ├ [291]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        NA.pl 
│     │                 │                        ├ [292]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        Overstru.pl 
│     │                 │                        ├ [293]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        Right.pl 
│     │                 │                        ├ [294]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        Top.pl 
│     │                 │                        ├ [295]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        TopAndBo.pl 
│     │                 │                        ├ [296]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        TopAndL2.pl 
│     │                 │                        ├ [297]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        TopAndLe.pl 
│     │                 │                        ├ [298]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        TopAndRi.pl 
│     │                 │                        ├ [299]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InPC/
│     │                 │                        │        VisualOr.pl 
│     │                 │                        ├ [300]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Avagraha.pl 
│     │                 │                        ├ [301]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Bindu.pl 
│     │                 │                        ├ [302]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Cantilla.pl 
│     │                 │                        ├ [303]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Consona2.pl 
│     │                 │                        ├ [304]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Consona3.pl 
│     │                 │                        ├ [305]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Consona4.pl 
│     │                 │                        ├ [306]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Consona5.pl 
│     │                 │                        ├ [307]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Consona6.pl 
│     │                 │                        ├ [308]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Consona7.pl 
│     │                 │                        ├ [309]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Consona8.pl 
│     │                 │                        ├ [310]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Consona9.pl 
│     │                 │                        ├ [311]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Consonan.pl 
│     │                 │                        ├ [312]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Geminati.pl 
│     │                 │                        ├ [313]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Invisibl.pl 
│     │                 │                        ├ [314]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Nukta.pl 
│     │                 │                        ├ [315]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Number.pl 
│     │                 │                        ├ [316]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Other.pl 
│     │                 │                        ├ [317]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        PureKill.pl 
│     │                 │                        ├ [318]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Syllable.pl 
│     │                 │                        ├ [319]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        ToneMark.pl 
│     │                 │                        ├ [320]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Virama.pl 
│     │                 │                        ├ [321]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Visarga.pl 
│     │                 │                        ├ [322]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        Vowel.pl 
│     │                 │                        ├ [323]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        VowelDep.pl 
│     │                 │                        ├ [324]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/InSC/
│     │                 │                        │        VowelInd.pl 
│     │                 │                        ├ [325]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Ai
│     │                 │                        │        n.pl 
│     │                 │                        ├ [326]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Al
│     │                 │                        │        ef.pl 
│     │                 │                        ├ [327]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Be
│     │                 │                        │        h.pl 
│     │                 │                        ├ [328]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Da
│     │                 │                        │        l.pl 
│     │                 │                        ├ [329]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Fa
│     │                 │                        │        rsiYeh.pl 
│     │                 │                        ├ [330]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Fe
│     │                 │                        │        h.pl 
│     │                 │                        ├ [331]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Ga
│     │                 │                        │        f.pl 
│     │                 │                        ├ [332]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Ha
│     │                 │                        │        h.pl 
│     │                 │                        ├ [333]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Ha
│     │                 │                        │        nifiRo.pl 
│     │                 │                        ├ [334]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Ka
│     │                 │                        │        f.pl 
│     │                 │                        ├ [335]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/La
│     │                 │                        │        m.pl 
│     │                 │                        ├ [336]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/No
│     │                 │                        │        Joinin.pl 
│     │                 │                        ├ [337]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/No
│     │                 │                        │        on.pl 
│     │                 │                        ├ [338]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Qa
│     │                 │                        │        f.pl 
│     │                 │                        ├ [339]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Re
│     │                 │                        │        h.pl 
│     │                 │                        ├ [340]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Sa
│     │                 │                        │        d.pl 
│     │                 │                        ├ [341]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Se
│     │                 │                        │        en.pl 
│     │                 │                        ├ [342]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Ta
│     │                 │                        │        h.pl 
│     │                 │                        ├ [343]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Wa
│     │                 │                        │        w.pl 
│     │                 │                        ├ [344]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jg/Ye
│     │                 │                        │        h.pl 
│     │                 │                        ├ [345]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jt/C.pl 
│     │                 │                        ├ [346]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jt/D.pl 
│     │                 │                        ├ [347]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jt/L.pl 
│     │                 │                        ├ [348]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jt/R.pl 
│     │                 │                        ├ [349]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jt/T.pl 
│     │                 │                        ├ [350]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Jt/U.pl 
│     │                 │                        ├ [351]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/AI
│     │                 │                        │        .pl 
│     │                 │                        ├ [352]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/AL
│     │                 │                        │        .pl 
│     │                 │                        ├ [353]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/BA
│     │                 │                        │        .pl 
│     │                 │                        ├ [354]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/BB
│     │                 │                        │        .pl 
│     │                 │                        ├ [355]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/CJ
│     │                 │                        │        .pl 
│     │                 │                        ├ [356]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/CL
│     │                 │                        │        .pl 
│     │                 │                        ├ [357]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/CM
│     │                 │                        │        .pl 
│     │                 │                        ├ [358]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/EX
│     │                 │                        │        .pl 
│     │                 │                        ├ [359]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/GL
│     │                 │                        │        .pl 
│     │                 │                        ├ [360]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/ID
│     │                 │                        │        .pl 
│     │                 │                        ├ [361]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/IN
│     │                 │                        │        .pl 
│     │                 │                        ├ [362]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/IS
│     │                 │                        │        .pl 
│     │                 │                        ├ [363]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/NS
│     │                 │                        │        .pl 
│     │                 │                        ├ [364]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/NU
│     │                 │                        │        .pl 
│     │                 │                        ├ [365]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/OP
│     │                 │                        │        .pl 
│     │                 │                        ├ [366]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/PO
│     │                 │                        │        .pl 
│     │                 │                        ├ [367]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/PR
│     │                 │                        │        .pl 
│     │                 │                        ├ [368]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/QU
│     │                 │                        │        .pl 
│     │                 │                        ├ [369]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/SA
│     │                 │                        │        .pl 
│     │                 │                        ├ [370]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lb/XX
│     │                 │                        │        .pl 
│     │                 │                        ├ [371]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Lower
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [372]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Math/
│     │                 │                        │        Y.pl 
│     │                 │                        ├ [373]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/NFCQC
│     │                 │                        │        /M.pl 
│     │                 │                        ├ [374]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/NFCQC
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [375]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/NFDQC
│     │                 │                        │        /N.pl 
│     │                 │                        ├ [376]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/NFDQC
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [377]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/NFKCQ
│     │                 │                        │        C/N.pl 
│     │                 │                        ├ [378]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/NFKCQ
│     │                 │                        │        C/Y.pl 
│     │                 │                        ├ [379]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/NFKDQ
│     │                 │                        │        C/N.pl 
│     │                 │                        ├ [380]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/NFKDQ
│     │                 │                        │        C/Y.pl 
│     │                 │                        ├ [381]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nt/Di
│     │                 │                        │        .pl 
│     │                 │                        ├ [382]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nt/No
│     │                 │                        │        ne.pl 
│     │                 │                        ├ [383]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nt/Nu
│     │                 │                        │        .pl 
│     │                 │                        ├ [384]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/0.pl 
│     │                 │                        ├ [385]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/1.pl 
│     │                 │                        ├ [386]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/10
│     │                 │                        │        .pl 
│     │                 │                        ├ [387]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/10
│     │                 │                        │        0.pl 
│     │                 │                        ├ [388]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/10
│     │                 │                        │        00.pl 
│     │                 │                        ├ [389]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/10
│     │                 │                        │        000.pl 
│     │                 │                        ├ [390]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/10
│     │                 │                        │        0000.pl 
│     │                 │                        ├ [391]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/11
│     │                 │                        │        .pl 
│     │                 │                        ├ [392]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/12
│     │                 │                        │        .pl 
│     │                 │                        ├ [393]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/13
│     │                 │                        │        .pl 
│     │                 │                        ├ [394]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/14
│     │                 │                        │        .pl 
│     │                 │                        ├ [395]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/15
│     │                 │                        │        .pl 
│     │                 │                        ├ [396]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/16
│     │                 │                        │        .pl 
│     │                 │                        ├ [397]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/17
│     │                 │                        │        .pl 
│     │                 │                        ├ [398]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/18
│     │                 │                        │        .pl 
│     │                 │                        ├ [399]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/19
│     │                 │                        │        .pl 
│     │                 │                        ├ [400]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/1_
│     │                 │                        │        16.pl 
│     │                 │                        ├ [401]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/1_
│     │                 │                        │        2.pl 
│     │                 │                        ├ [402]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/1_
│     │                 │                        │        3.pl 
│     │                 │                        ├ [403]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/1_
│     │                 │                        │        4.pl 
│     │                 │                        ├ [404]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/1_
│     │                 │                        │        6.pl 
│     │                 │                        ├ [405]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/1_
│     │                 │                        │        8.pl 
│     │                 │                        ├ [406]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/2.pl 
│     │                 │                        ├ [407]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/20
│     │                 │                        │        .pl 
│     │                 │                        ├ [408]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/20
│     │                 │                        │        0.pl 
│     │                 │                        ├ [409]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/20
│     │                 │                        │        00.pl 
│     │                 │                        ├ [410]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/20
│     │                 │                        │        000.pl 
│     │                 │                        ├ [411]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/2_
│     │                 │                        │        3.pl 
│     │                 │                        ├ [412]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/3.pl 
│     │                 │                        ├ [413]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/30
│     │                 │                        │        .pl 
│     │                 │                        ├ [414]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/30
│     │                 │                        │        0.pl 
│     │                 │                        ├ [415]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/30
│     │                 │                        │        00.pl 
│     │                 │                        ├ [416]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/30
│     │                 │                        │        000.pl 
│     │                 │                        ├ [417]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/3_
│     │                 │                        │        16.pl 
│     │                 │                        ├ [418]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/3_
│     │                 │                        │        4.pl 
│     │                 │                        ├ [419]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/4.pl 
│     │                 │                        ├ [420]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/40
│     │                 │                        │        .pl 
│     │                 │                        ├ [421]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/40
│     │                 │                        │        0.pl 
│     │                 │                        ├ [422]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/40
│     │                 │                        │        00.pl 
│     │                 │                        ├ [423]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/40
│     │                 │                        │        000.pl 
│     │                 │                        ├ [424]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/5.pl 
│     │                 │                        ├ [425]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/50
│     │                 │                        │        .pl 
│     │                 │                        ├ [426]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/50
│     │                 │                        │        0.pl 
│     │                 │                        ├ [427]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/50
│     │                 │                        │        00.pl 
│     │                 │                        ├ [428]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/50
│     │                 │                        │        000.pl 
│     │                 │                        ├ [429]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/6.pl 
│     │                 │                        ├ [430]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/60
│     │                 │                        │        .pl 
│     │                 │                        ├ [431]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/60
│     │                 │                        │        0.pl 
│     │                 │                        ├ [432]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/60
│     │                 │                        │        00.pl 
│     │                 │                        ├ [433]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/60
│     │                 │                        │        000.pl 
│     │                 │                        ├ [434]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/7.pl 
│     │                 │                        ├ [435]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/70
│     │                 │                        │        .pl 
│     │                 │                        ├ [436]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/70
│     │                 │                        │        0.pl 
│     │                 │                        ├ [437]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/70
│     │                 │                        │        00.pl 
│     │                 │                        ├ [438]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/70
│     │                 │                        │        000.pl 
│     │                 │                        ├ [439]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/8.pl 
│     │                 │                        ├ [440]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/80
│     │                 │                        │        .pl 
│     │                 │                        ├ [441]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/80
│     │                 │                        │        0.pl 
│     │                 │                        ├ [442]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/80
│     │                 │                        │        00.pl 
│     │                 │                        ├ [443]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/80
│     │                 │                        │        000.pl 
│     │                 │                        ├ [444]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/9.pl 
│     │                 │                        ├ [445]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/90
│     │                 │                        │        .pl 
│     │                 │                        ├ [446]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/90
│     │                 │                        │        0.pl 
│     │                 │                        ├ [447]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/90
│     │                 │                        │        00.pl 
│     │                 │                        ├ [448]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Nv/90
│     │                 │                        │        000.pl 
│     │                 │                        ├ [449]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/PCM/Y
│     │                 │                        │        .pl 
│     │                 │                        ├ [450]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/PatSy
│     │                 │                        │        n/Y.pl 
│     │                 │                        ├ [451]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        Alnum.pl 
│     │                 │                        ├ [452]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        Assigned.pl 
│     │                 │                        ├ [453]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        Blank.pl 
│     │                 │                        ├ [454]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        Graph.pl 
│     │                 │                        ├ [455]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        PerlWord.pl 
│     │                 │                        ├ [456]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        PosixPun.pl 
│     │                 │                        ├ [457]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        Print.pl 
│     │                 │                        ├ [458]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        SpacePer.pl 
│     │                 │                        ├ [459]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        Title.pl 
│     │                 │                        ├ [460]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        Word.pl 
│     │                 │                        ├ [461]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        XPosixPu.pl 
│     │                 │                        ├ [462]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        _PerlAny.pl 
│     │                 │                        ├ [463]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        _PerlCh2.pl 
│     │                 │                        ├ [464]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        _PerlCha.pl 
│     │                 │                        ├ [465]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        _PerlFol.pl 
│     │                 │                        ├ [466]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        _PerlIDC.pl 
│     │                 │                        ├ [467]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        _PerlIDS.pl 
│     │                 │                        ├ [468]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        _PerlIsI.pl 
│     │                 │                        ├ [469]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        _PerlNch.pl 
│     │                 │                        ├ [470]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        _PerlPat.pl 
│     │                 │                        ├ [471]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        _PerlPr2.pl 
│     │                 │                        ├ [472]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        _PerlPro.pl 
│     │                 │                        ├ [473]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Perl/
│     │                 │                        │        _PerlQuo.pl 
│     │                 │                        ├ [474]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/QMark
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [475]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SB/AT
│     │                 │                        │        .pl 
│     │                 │                        ├ [476]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SB/CL
│     │                 │                        │        .pl 
│     │                 │                        ├ [477]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SB/EX
│     │                 │                        │        .pl 
│     │                 │                        ├ [478]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SB/FO
│     │                 │                        │        .pl 
│     │                 │                        ├ [479]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SB/LE
│     │                 │                        │        .pl 
│     │                 │                        ├ [480]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SB/LO
│     │                 │                        │        .pl 
│     │                 │                        ├ [481]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SB/NU
│     │                 │                        │        .pl 
│     │                 │                        ├ [482]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SB/SC
│     │                 │                        │        .pl 
│     │                 │                        ├ [483]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SB/ST
│     │                 │                        │        .pl 
│     │                 │                        ├ [484]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SB/Sp
│     │                 │                        │        .pl 
│     │                 │                        ├ [485]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SB/UP
│     │                 │                        │        .pl 
│     │                 │                        ├ [486]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SB/XX
│     │                 │                        │        .pl 
│     │                 │                        ├ [487]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/SD/Y.pl 
│     │                 │                        ├ [488]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/STerm
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [489]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Ar
│     │                 │                        │        ab.pl 
│     │                 │                        ├ [490]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Be
│     │                 │                        │        ng.pl 
│     │                 │                        ├ [491]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Cp
│     │                 │                        │        rt.pl 
│     │                 │                        ├ [492]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Cy
│     │                 │                        │        rl.pl 
│     │                 │                        ├ [493]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/De
│     │                 │                        │        va.pl 
│     │                 │                        ├ [494]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Du
│     │                 │                        │        pl.pl 
│     │                 │                        ├ [495]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Ge
│     │                 │                        │        or.pl 
│     │                 │                        ├ [496]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Gl
│     │                 │                        │        ag.pl 
│     │                 │                        ├ [497]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Go
│     │                 │                        │        ng.pl 
│     │                 │                        ├ [498]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Go
│     │                 │                        │        nm.pl 
│     │                 │                        ├ [499]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Gr
│     │                 │                        │        an.pl 
│     │                 │                        ├ [500]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Gr
│     │                 │                        │        ek.pl 
│     │                 │                        ├ [501]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Gu
│     │                 │                        │        jr.pl 
│     │                 │                        ├ [502]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Gu
│     │                 │                        │        ru.pl 
│     │                 │                        ├ [503]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Ha
│     │                 │                        │        n.pl 
│     │                 │                        ├ [504]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Ha
│     │                 │                        │        ng.pl 
│     │                 │                        ├ [505]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Hi
│     │                 │                        │        ra.pl 
│     │                 │                        ├ [506]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Ka
│     │                 │                        │        na.pl 
│     │                 │                        ├ [507]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Kn
│     │                 │                        │        da.pl 
│     │                 │                        ├ [508]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/La
│     │                 │                        │        tn.pl 
│     │                 │                        ├ [509]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Li
│     │                 │                        │        mb.pl 
│     │                 │                        ├ [510]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Li
│     │                 │                        │        nb.pl 
│     │                 │                        ├ [511]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Ml
│     │                 │                        │        ym.pl 
│     │                 │                        ├ [512]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Mo
│     │                 │                        │        ng.pl 
│     │                 │                        ├ [513]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Mu
│     │                 │                        │        lt.pl 
│     │                 │                        ├ [514]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Or
│     │                 │                        │        ya.pl 
│     │                 │                        ├ [515]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Si
│     │                 │                        │        nh.pl 
│     │                 │                        ├ [516]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Sy
│     │                 │                        │        rc.pl 
│     │                 │                        ├ [517]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Ta
│     │                 │                        │        ml.pl 
│     │                 │                        ├ [518]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Te
│     │                 │                        │        lu.pl 
│     │                 │                        ├ [519]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Zi
│     │                 │                        │        nh.pl 
│     │                 │                        ├ [520]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Sc/Zy
│     │                 │                        │        yy.pl 
│     │                 │                        ├ [521]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/A
│     │                 │                        │        dlm.pl 
│     │                 │                        ├ [522]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/A
│     │                 │                        │        rab.pl 
│     │                 │                        ├ [523]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/A
│     │                 │                        │        rmn.pl 
│     │                 │                        ├ [524]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/B
│     │                 │                        │        eng.pl 
│     │                 │                        ├ [525]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/B
│     │                 │                        │        hks.pl 
│     │                 │                        ├ [526]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/B
│     │                 │                        │        opo.pl 
│     │                 │                        ├ [527]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/C
│     │                 │                        │        akm.pl 
│     │                 │                        ├ [528]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/C
│     │                 │                        │        ham.pl 
│     │                 │                        ├ [529]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/C
│     │                 │                        │        opt.pl 
│     │                 │                        ├ [530]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/C
│     │                 │                        │        prt.pl 
│     │                 │                        ├ [531]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/C
│     │                 │                        │        yrl.pl 
│     │                 │                        ├ [532]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/D
│     │                 │                        │        eva.pl 
│     │                 │                        ├ [533]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/D
│     │                 │                        │        iak.pl 
│     │                 │                        ├ [534]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/D
│     │                 │                        │        upl.pl 
│     │                 │                        ├ [535]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/E
│     │                 │                        │        thi.pl 
│     │                 │                        ├ [536]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/G
│     │                 │                        │        eor.pl 
│     │                 │                        ├ [537]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/G
│     │                 │                        │        lag.pl 
│     │                 │                        ├ [538]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/G
│     │                 │                        │        ong.pl 
│     │                 │                        ├ [539]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/G
│     │                 │                        │        onm.pl 
│     │                 │                        ├ [540]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/G
│     │                 │                        │        ran.pl 
│     │                 │                        ├ [541]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/G
│     │                 │                        │        rek.pl 
│     │                 │                        ├ [542]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/G
│     │                 │                        │        ujr.pl 
│     │                 │                        ├ [543]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/G
│     │                 │                        │        uru.pl 
│     │                 │                        ├ [544]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/H
│     │                 │                        │        an.pl 
│     │                 │                        ├ [545]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/H
│     │                 │                        │        ang.pl 
│     │                 │                        ├ [546]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/H
│     │                 │                        │        ebr.pl 
│     │                 │                        ├ [547]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/H
│     │                 │                        │        ira.pl 
│     │                 │                        ├ [548]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/H
│     │                 │                        │        mng.pl 
│     │                 │                        ├ [549]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/H
│     │                 │                        │        mnp.pl 
│     │                 │                        ├ [550]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/K
│     │                 │                        │        ana.pl 
│     │                 │                        ├ [551]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/K
│     │                 │                        │        har.pl 
│     │                 │                        ├ [552]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/K
│     │                 │                        │        hmr.pl 
│     │                 │                        ├ [553]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/K
│     │                 │                        │        hoj.pl 
│     │                 │                        ├ [554]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/K
│     │                 │                        │        nda.pl 
│     │                 │                        ├ [555]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/K
│     │                 │                        │        thi.pl 
│     │                 │                        ├ [556]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/L
│     │                 │                        │        ana.pl 
│     │                 │                        ├ [557]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/L
│     │                 │                        │        ao.pl 
│     │                 │                        ├ [558]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/L
│     │                 │                        │        atn.pl 
│     │                 │                        ├ [559]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/L
│     │                 │                        │        imb.pl 
│     │                 │                        ├ [560]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/L
│     │                 │                        │        ina.pl 
│     │                 │                        ├ [561]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/L
│     │                 │                        │        inb.pl 
│     │                 │                        ├ [562]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/M
│     │                 │                        │        lym.pl 
│     │                 │                        ├ [563]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/M
│     │                 │                        │        ong.pl 
│     │                 │                        ├ [564]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/M
│     │                 │                        │        ult.pl 
│     │                 │                        ├ [565]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/M
│     │                 │                        │        ymr.pl 
│     │                 │                        ├ [566]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/N
│     │                 │                        │        and.pl 
│     │                 │                        ├ [567]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/N
│     │                 │                        │        ko.pl 
│     │                 │                        ├ [568]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/O
│     │                 │                        │        rya.pl 
│     │                 │                        ├ [569]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/P
│     │                 │                        │        hlp.pl 
│     │                 │                        ├ [570]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/R
│     │                 │                        │        ohg.pl 
│     │                 │                        ├ [571]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/S
│     │                 │                        │        hrd.pl 
│     │                 │                        ├ [572]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/S
│     │                 │                        │        ind.pl 
│     │                 │                        ├ [573]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/S
│     │                 │                        │        inh.pl 
│     │                 │                        ├ [574]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/S
│     │                 │                        │        yrc.pl 
│     │                 │                        ├ [575]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/T
│     │                 │                        │        agb.pl 
│     │                 │                        ├ [576]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/T
│     │                 │                        │        akr.pl 
│     │                 │                        ├ [577]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/T
│     │                 │                        │        alu.pl 
│     │                 │                        ├ [578]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/T
│     │                 │                        │        aml.pl 
│     │                 │                        ├ [579]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/T
│     │                 │                        │        ang.pl 
│     │                 │                        ├ [580]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/T
│     │                 │                        │        elu.pl 
│     │                 │                        ├ [581]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/T
│     │                 │                        │        haa.pl 
│     │                 │                        ├ [582]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/T
│     │                 │                        │        ibt.pl 
│     │                 │                        ├ [583]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/T
│     │                 │                        │        irh.pl 
│     │                 │                        ├ [584]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/V
│     │                 │                        │        ith.pl 
│     │                 │                        ├ [585]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/X
│     │                 │                        │        sux.pl 
│     │                 │                        ├ [586]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/Y
│     │                 │                        │        ezi.pl 
│     │                 │                        ├ [587]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/Y
│     │                 │                        │        i.pl 
│     │                 │                        ├ [588]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/Z
│     │                 │                        │        inh.pl 
│     │                 │                        ├ [589]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/Z
│     │                 │                        │        yyy.pl 
│     │                 │                        ├ [590]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Scx/Z
│     │                 │                        │        zzz.pl 
│     │                 │                        ├ [591]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Term/
│     │                 │                        │        Y.pl 
│     │                 │                        ├ [592]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/UIdeo
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [593]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Upper
│     │                 │                        │        /Y.pl 
│     │                 │                        ├ [594]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/VS/Y.pl 
│     │                 │                        ├ [595]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Vo/R.pl 
│     │                 │                        ├ [596]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Vo/Tr
│     │                 │                        │        .pl 
│     │                 │                        ├ [597]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Vo/Tu
│     │                 │                        │        .pl 
│     │                 │                        ├ [598]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/Vo/U.pl 
│     │                 │                        ├ [599]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/WB/EX
│     │                 │                        │        .pl 
│     │                 │                        ├ [600]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/WB/Ex
│     │                 │                        │        tend.pl 
│     │                 │                        ├ [601]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/WB/FO
│     │                 │                        │        .pl 
│     │                 │                        ├ [602]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/WB/HL
│     │                 │                        │        .pl 
│     │                 │                        ├ [603]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/WB/KA
│     │                 │                        │        .pl 
│     │                 │                        ├ [604]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/WB/LE
│     │                 │                        │        .pl 
│     │                 │                        ├ [605]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/WB/MB
│     │                 │                        │        .pl 
│     │                 │                        ├ [606]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/WB/ML
│     │                 │                        │        .pl 
│     │                 │                        ├ [607]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/WB/MN
│     │                 │                        │        .pl 
│     │                 │                        ├ [608]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/WB/NU
│     │                 │                        │        .pl 
│     │                 │                        ├ [609]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/WB/WS
│     │                 │                        │        egSpac.pl 
│     │                 │                        ├ [610]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/WB/XX
│     │                 │                        │        .pl 
│     │                 │                        ├ [611]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/XIDC/
│     │                 │                        │        Y.pl 
│     │                 │                        ├ [612]: /usr/lib/x86_64-linux-gnu/perl-base/unicore/lib/XIDS/
│     │                 │                        │        Y.pl 
│     │                 │                        ├ [613]: /usr/lib/x86_64-linux-gnu/perl-base/utf8.pm 
│     │                 │                        ├ [614]: /usr/lib/x86_64-linux-gnu/perl-base/vars.pm 
│     │                 │                        ├ [615]: /usr/lib/x86_64-linux-gnu/perl-base/warnings.pm 
│     │                 │                        ├ [616]: /usr/lib/x86_64-linux-gnu/perl-base/warnings/register
│     │                 │                        │        .pm 
│     │                 │                        ├ [617]: /usr/share/doc/perl-base/changelog.Debian.gz 
│     │                 │                        ├ [618]: /usr/share/doc/perl-base/copyright 
│     │                 │                        ├ [619]: /usr/share/doc/perl/AUTHORS.gz 
│     │                 │                        ├ [620]: /usr/share/doc/perl/Documentation 
│     │                 │                        ├ [621]: /usr/share/lintian/overrides/perl-base 
│     │                 │                        ╰ [622]: /usr/share/man/man1/perl.1.gz 
│     │                 ├ [109] ╭ ID            : procps@2:4.0.4-7ubuntu1 
│     │                 │       ├ Name          : procps 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/procps@4.0.4-7ubuntu1?arch=amd64&distro
│     │                 │       │                │       =ubuntu-25.04&epoch=2 
│     │                 │       │                ╰ UID : 2efadaa89038e979 
│     │                 │       ├ Version       : 4.0.4 
│     │                 │       ├ Release       : 7ubuntu1 
│     │                 │       ├ Epoch         : 2 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : procps 
│     │                 │       ├ SrcVersion    : 4.0.4 
│     │                 │       ├ SrcRelease    : 7ubuntu1 
│     │                 │       ├ SrcEpoch      : 2 
│     │                 │       ├ Licenses       ╭ [0]: LGPL-2.1-or-later 
│     │                 │       │                ├ [1]: LGPL-2.0-or-later 
│     │                 │       │                ├ [2]: GPL-2.0-or-later 
│     │                 │       │                ├ [3]: GPL-2.0-only 
│     │                 │       │                ├ [4]: LGPL-2.0-only 
│     │                 │       │                ╰ [5]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: init-system-helpers@1.68 
│     │                 │       │                ├ [1]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [2]: libncursesw6@6.5+20250216-2 
│     │                 │       │                ├ [3]: libproc2-0@2:4.0.4-7ubuntu1 
│     │                 │       │                ├ [4]: libsystemd0@257.4-1ubuntu3.2 
│     │                 │       │                ╰ [5]: libtinfo6@6.5+20250216-2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:6df185ec4703d8da0011a5247a87ec357cb3fa44dabfc9dd36ad41
│     │                 │       │                 1cfda27718 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/bin/free 
│     │                 │                        ├ [1]  : /usr/bin/kill 
│     │                 │                        ├ [2]  : /usr/bin/pgrep 
│     │                 │                        ├ [3]  : /usr/bin/pidwait 
│     │                 │                        ├ [4]  : /usr/bin/pmap 
│     │                 │                        ├ [5]  : /usr/bin/ps 
│     │                 │                        ├ [6]  : /usr/bin/pwdx 
│     │                 │                        ├ [7]  : /usr/bin/skill 
│     │                 │                        ├ [8]  : /usr/bin/slabtop 
│     │                 │                        ├ [9]  : /usr/bin/tload 
│     │                 │                        ├ [10] : /usr/bin/top 
│     │                 │                        ├ [11] : /usr/bin/uptime 
│     │                 │                        ├ [12] : /usr/bin/vmstat 
│     │                 │                        ├ [13] : /usr/bin/w 
│     │                 │                        ├ [14] : /usr/bin/watch 
│     │                 │                        ├ [15] : /usr/sbin/sysctl 
│     │                 │                        ├ [16] : /usr/share/bug/procps/presubj 
│     │                 │                        ├ [17] : /usr/share/doc/procps/FAQ.gz 
│     │                 │                        ├ [18] : /usr/share/doc/procps/README.Debian 
│     │                 │                        ├ [19] : /usr/share/doc/procps/bugs.md 
│     │                 │                        ├ [20] : /usr/share/doc/procps/copyright 
│     │                 │                        ├ [21] : /usr/share/lintian/overrides/procps 
│     │                 │                        ├ [22] : /usr/share/man/de/man1/free.1.gz 
│     │                 │                        ├ [23] : /usr/share/man/de/man1/kill.1.gz 
│     │                 │                        ├ [24] : /usr/share/man/de/man1/pgrep.1.gz 
│     │                 │                        ├ [25] : /usr/share/man/de/man1/pidof.1.gz 
│     │                 │                        ├ [26] : /usr/share/man/de/man1/pmap.1.gz 
│     │                 │                        ├ [27] : /usr/share/man/de/man1/ps.1.gz 
│     │                 │                        ├ [28] : /usr/share/man/de/man1/pwdx.1.gz 
│     │                 │                        ├ [29] : /usr/share/man/de/man1/skill.1.gz 
│     │                 │                        ├ [30] : /usr/share/man/de/man1/slabtop.1.gz 
│     │                 │                        ├ [31] : /usr/share/man/de/man1/tload.1.gz 
│     │                 │                        ├ [32] : /usr/share/man/de/man1/uptime.1.gz 
│     │                 │                        ├ [33] : /usr/share/man/de/man1/w.1.gz 
│     │                 │                        ├ [34] : /usr/share/man/de/man1/watch.1.gz 
│     │                 │                        ├ [35] : /usr/share/man/de/man5/sysctl.conf.5.gz 
│     │                 │                        ├ [36] : /usr/share/man/de/man8/sysctl.8.gz 
│     │                 │                        ├ [37] : /usr/share/man/de/man8/vmstat.8.gz 
│     │                 │                        ├ [38] : /usr/share/man/fr/man1/free.1.gz 
│     │                 │                        ├ [39] : /usr/share/man/fr/man1/kill.1.gz 
│     │                 │                        ├ [40] : /usr/share/man/fr/man1/pmap.1.gz 
│     │                 │                        ├ [41] : /usr/share/man/fr/man1/ps.1.gz 
│     │                 │                        ├ [42] : /usr/share/man/fr/man1/pwdx.1.gz 
│     │                 │                        ├ [43] : /usr/share/man/fr/man1/skill.1.gz 
│     │                 │                        ├ [44] : /usr/share/man/fr/man1/slabtop.1.gz 
│     │                 │                        ├ [45] : /usr/share/man/fr/man1/tload.1.gz 
│     │                 │                        ├ [46] : /usr/share/man/fr/man1/uptime.1.gz 
│     │                 │                        ├ [47] : /usr/share/man/fr/man1/w.1.gz 
│     │                 │                        ├ [48] : /usr/share/man/fr/man1/watch.1.gz 
│     │                 │                        ├ [49] : /usr/share/man/fr/man5/sysctl.conf.5.gz 
│     │                 │                        ├ [50] : /usr/share/man/fr/man8/sysctl.8.gz 
│     │                 │                        ├ [51] : /usr/share/man/fr/man8/vmstat.8.gz 
│     │                 │                        ├ [52] : /usr/share/man/man1/free.1.gz 
│     │                 │                        ├ [53] : /usr/share/man/man1/kill.1.gz 
│     │                 │                        ├ [54] : /usr/share/man/man1/pgrep.1.gz 
│     │                 │                        ├ [55] : /usr/share/man/man1/pmap.1.gz 
│     │                 │                        ├ [56] : /usr/share/man/man1/ps.1.gz 
│     │                 │                        ├ [57] : /usr/share/man/man1/pwdx.1.gz 
│     │                 │                        ├ [58] : /usr/share/man/man1/skill.1.gz 
│     │                 │                        ├ [59] : /usr/share/man/man1/slabtop.1.gz 
│     │                 │                        ├ [60] : /usr/share/man/man1/tload.1.gz 
│     │                 │                        ├ [61] : /usr/share/man/man1/top.1.gz 
│     │                 │                        ├ [62] : /usr/share/man/man1/uptime.1.gz 
│     │                 │                        ├ [63] : /usr/share/man/man1/w.1.gz 
│     │                 │                        ├ [64] : /usr/share/man/man1/watch.1.gz 
│     │                 │                        ├ [65] : /usr/share/man/man3/procps.3.gz 
│     │                 │                        ├ [66] : /usr/share/man/man3/procps_misc.3.gz 
│     │                 │                        ├ [67] : /usr/share/man/man3/procps_pids.3.gz 
│     │                 │                        ├ [68] : /usr/share/man/man5/sysctl.conf.5.gz 
│     │                 │                        ├ [69] : /usr/share/man/man8/sysctl.8.gz 
│     │                 │                        ├ [70] : /usr/share/man/man8/vmstat.8.gz 
│     │                 │                        ├ [71] : /usr/share/man/pl/man1/free.1.gz 
│     │                 │                        ├ [72] : /usr/share/man/pl/man1/pgrep.1.gz 
│     │                 │                        ├ [73] : /usr/share/man/pl/man1/pmap.1.gz 
│     │                 │                        ├ [74] : /usr/share/man/pl/man1/uptime.1.gz 
│     │                 │                        ├ [75] : /usr/share/man/pl/man3/procps.3.gz 
│     │                 │                        ├ [76] : /usr/share/man/pl/man3/procps_misc.3.gz 
│     │                 │                        ├ [77] : /usr/share/man/pl/man3/procps_pids.3.gz 
│     │                 │                        ├ [78] : /usr/share/man/pl/man8/vmstat.8.gz 
│     │                 │                        ├ [79] : /usr/share/man/pt_BR/man1/free.1.gz 
│     │                 │                        ├ [80] : /usr/share/man/pt_BR/man1/kill.1.gz 
│     │                 │                        ├ [81] : /usr/share/man/pt_BR/man1/pmap.1.gz 
│     │                 │                        ├ [82] : /usr/share/man/pt_BR/man1/pwdx.1.gz 
│     │                 │                        ├ [83] : /usr/share/man/pt_BR/man1/skill.1.gz 
│     │                 │                        ├ [84] : /usr/share/man/pt_BR/man1/slabtop.1.gz 
│     │                 │                        ├ [85] : /usr/share/man/pt_BR/man1/tload.1.gz 
│     │                 │                        ├ [86] : /usr/share/man/pt_BR/man1/uptime.1.gz 
│     │                 │                        ├ [87] : /usr/share/man/pt_BR/man1/w.1.gz 
│     │                 │                        ├ [88] : /usr/share/man/pt_BR/man1/watch.1.gz 
│     │                 │                        ├ [89] : /usr/share/man/pt_BR/man5/sysctl.conf.5.gz 
│     │                 │                        ├ [90] : /usr/share/man/pt_BR/man8/sysctl.8.gz 
│     │                 │                        ├ [91] : /usr/share/man/pt_BR/man8/vmstat.8.gz 
│     │                 │                        ├ [92] : /usr/share/man/ro/man1/free.1.gz 
│     │                 │                        ├ [93] : /usr/share/man/ro/man1/kill.1.gz 
│     │                 │                        ├ [94] : /usr/share/man/ro/man1/pgrep.1.gz 
│     │                 │                        ├ [95] : /usr/share/man/ro/man1/pidof.1.gz 
│     │                 │                        ├ [96] : /usr/share/man/ro/man1/pmap.1.gz 
│     │                 │                        ├ [97] : /usr/share/man/ro/man1/ps.1.gz 
│     │                 │                        ├ [98] : /usr/share/man/ro/man1/pwdx.1.gz 
│     │                 │                        ├ [99] : /usr/share/man/ro/man1/skill.1.gz 
│     │                 │                        ├ [100]: /usr/share/man/ro/man1/slabtop.1.gz 
│     │                 │                        ├ [101]: /usr/share/man/ro/man1/tload.1.gz 
│     │                 │                        ├ [102]: /usr/share/man/ro/man1/top.1.gz 
│     │                 │                        ├ [103]: /usr/share/man/ro/man1/uptime.1.gz 
│     │                 │                        ├ [104]: /usr/share/man/ro/man1/w.1.gz 
│     │                 │                        ├ [105]: /usr/share/man/ro/man1/watch.1.gz 
│     │                 │                        ├ [106]: /usr/share/man/ro/man3/procps.3.gz 
│     │                 │                        ├ [107]: /usr/share/man/ro/man3/procps_misc.3.gz 
│     │                 │                        ├ [108]: /usr/share/man/ro/man3/procps_pids.3.gz 
│     │                 │                        ├ [109]: /usr/share/man/ro/man5/sysctl.conf.5.gz 
│     │                 │                        ├ [110]: /usr/share/man/ro/man8/sysctl.8.gz 
│     │                 │                        ├ [111]: /usr/share/man/ro/man8/vmstat.8.gz 
│     │                 │                        ├ [112]: /usr/share/man/sv/man1/free.1.gz 
│     │                 │                        ├ [113]: /usr/share/man/sv/man1/kill.1.gz 
│     │                 │                        ├ [114]: /usr/share/man/sv/man1/pgrep.1.gz 
│     │                 │                        ├ [115]: /usr/share/man/sv/man1/pidof.1.gz 
│     │                 │                        ├ [116]: /usr/share/man/sv/man1/pmap.1.gz 
│     │                 │                        ├ [117]: /usr/share/man/sv/man1/ps.1.gz 
│     │                 │                        ├ [118]: /usr/share/man/sv/man1/pwdx.1.gz 
│     │                 │                        ├ [119]: /usr/share/man/sv/man1/skill.1.gz 
│     │                 │                        ├ [120]: /usr/share/man/sv/man1/slabtop.1.gz 
│     │                 │                        ├ [121]: /usr/share/man/sv/man1/tload.1.gz 
│     │                 │                        ├ [122]: /usr/share/man/sv/man1/top.1.gz 
│     │                 │                        ├ [123]: /usr/share/man/sv/man1/uptime.1.gz 
│     │                 │                        ├ [124]: /usr/share/man/sv/man1/w.1.gz 
│     │                 │                        ├ [125]: /usr/share/man/sv/man1/watch.1.gz 
│     │                 │                        ├ [126]: /usr/share/man/sv/man3/procps.3.gz 
│     │                 │                        ├ [127]: /usr/share/man/sv/man3/procps_misc.3.gz 
│     │                 │                        ├ [128]: /usr/share/man/sv/man3/procps_pids.3.gz 
│     │                 │                        ├ [129]: /usr/share/man/sv/man5/sysctl.conf.5.gz 
│     │                 │                        ├ [130]: /usr/share/man/sv/man8/sysctl.8.gz 
│     │                 │                        ├ [131]: /usr/share/man/sv/man8/vmstat.8.gz 
│     │                 │                        ├ [132]: /usr/share/man/uk/man1/free.1.gz 
│     │                 │                        ├ [133]: /usr/share/man/uk/man1/kill.1.gz 
│     │                 │                        ├ [134]: /usr/share/man/uk/man1/pgrep.1.gz 
│     │                 │                        ├ [135]: /usr/share/man/uk/man1/pidof.1.gz 
│     │                 │                        ├ [136]: /usr/share/man/uk/man1/pmap.1.gz 
│     │                 │                        ├ [137]: /usr/share/man/uk/man1/ps.1.gz 
│     │                 │                        ├ [138]: /usr/share/man/uk/man1/pwdx.1.gz 
│     │                 │                        ├ [139]: /usr/share/man/uk/man1/skill.1.gz 
│     │                 │                        ├ [140]: /usr/share/man/uk/man1/slabtop.1.gz 
│     │                 │                        ├ [141]: /usr/share/man/uk/man1/tload.1.gz 
│     │                 │                        ├ [142]: /usr/share/man/uk/man1/top.1.gz 
│     │                 │                        ├ [143]: /usr/share/man/uk/man1/uptime.1.gz 
│     │                 │                        ├ [144]: /usr/share/man/uk/man1/w.1.gz 
│     │                 │                        ├ [145]: /usr/share/man/uk/man1/watch.1.gz 
│     │                 │                        ├ [146]: /usr/share/man/uk/man3/procps.3.gz 
│     │                 │                        ├ [147]: /usr/share/man/uk/man3/procps_misc.3.gz 
│     │                 │                        ├ [148]: /usr/share/man/uk/man3/procps_pids.3.gz 
│     │                 │                        ├ [149]: /usr/share/man/uk/man5/sysctl.conf.5.gz 
│     │                 │                        ├ [150]: /usr/share/man/uk/man8/sysctl.8.gz 
│     │                 │                        ╰ [151]: /usr/share/man/uk/man8/vmstat.8.gz 
│     │                 ├ [110] ╭ ID            : publicsuffix@20250108.1153-0.1 
│     │                 │       ├ Name          : publicsuffix 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/publicsuffix@20250108.1153-0.1?arch=all
│     │                 │       │                │       &distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 6d122b4c09fb54c0 
│     │                 │       ├ Version       : 20250108.1153 
│     │                 │       ├ Release       : 0.1 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : publicsuffix 
│     │                 │       ├ SrcVersion    : 20250108.1153 
│     │                 │       ├ SrcRelease    : 0.1 
│     │                 │       ├ Licenses       ╭ [0]: MPL-2.0 
│     │                 │       │                ╰ [1]: CC0-1.0 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]: /usr/share/doc/publicsuffix/README.Debian 
│     │                 │                        ├ [1]: /usr/share/doc/publicsuffix/changelog.Debian.gz 
│     │                 │                        ├ [2]: /usr/share/doc/publicsuffix/copyright 
│     │                 │                        ├ [3]: /usr/share/doc/publicsuffix/examples/test_psl.txt 
│     │                 │                        ├ [4]: /usr/share/publicsuffix/public_suffix_list.dafsa 
│     │                 │                        ╰ [5]: /usr/share/publicsuffix/public_suffix_list.dat 
│     │                 ├ [111] ╭ ID            : sed@4.9-2build1 
│     │                 │       ├ Name          : sed 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/sed@4.9-2build1?arch=amd64&distro=ubunt
│     │                 │       │                │       u-25.04 
│     │                 │       │                ╰ UID : a3e97fece62a9cab 
│     │                 │       ├ Version       : 4.9 
│     │                 │       ├ Release       : 2build1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : sed 
│     │                 │       ├ SrcVersion    : 4.9 
│     │                 │       ├ SrcRelease    : 2build1 
│     │                 │       ├ Licenses       ╭ [0]: GPL-3.0-or-later 
│     │                 │       │                ├ [1]: GPL-3.0-only 
│     │                 │       │                ├ [2]: X11 
│     │                 │       │                ├ [3]: GFDL-1.3-no-invariants-or-later 
│     │                 │       │                ├ [4]: GFDL-1.3-only 
│     │                 │       │                ├ [5]: ISC 
│     │                 │       │                ├ [6]: BSD-4-Clause-UC 
│     │                 │       │                ├ [7]: BSL-1 
│     │                 │       │                ╰ [8]: pcre 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:a09b856849cf36190f8cd39da33486b14bcaf81b592530b2f3236d
│     │                 │       │                 a17daaad2f 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/sed 
│     │                 │                        ├ [1] : /usr/share/doc/sed/AUTHORS 
│     │                 │                        ├ [2] : /usr/share/doc/sed/BUGS.gz 
│     │                 │                        ├ [3] : /usr/share/doc/sed/NEWS.gz 
│     │                 │                        ├ [4] : /usr/share/doc/sed/README 
│     │                 │                        ├ [5] : /usr/share/doc/sed/THANKS.gz 
│     │                 │                        ├ [6] : /usr/share/doc/sed/changelog.Debian.gz 
│     │                 │                        ├ [7] : /usr/share/doc/sed/copyright 
│     │                 │                        ├ [8] : /usr/share/doc/sed/examples/dc.sed 
│     │                 │                        ├ [9] : /usr/share/doc/sed/sedfaq.txt.gz 
│     │                 │                        ├ [10]: /usr/share/info/sed.info.gz 
│     │                 │                        ╰ [11]: /usr/share/man/man1/sed.1.gz 
│     │                 ├ [112] ╭ ID            : sensible-utils@0.0.24 
│     │                 │       ├ Name          : sensible-utils 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/sensible-utils@0.0.24?arch=all&distro=u
│     │                 │       │                │       buntu-25.04 
│     │                 │       │                ╰ UID : 210e9c84470d573d 
│     │                 │       ├ Version       : 0.0.24 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : sensible-utils 
│     │                 │       ├ SrcVersion    : 0.0.24 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: All-permissive 
│     │                 │       │                ├ [2]: configure 
│     │                 │       │                ├ [3]: installsh 
│     │                 │       │                ╰ [4]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:aa27c575c649320b59609a5faa0fedc8aa7a6c412c74fc4a20e0d4
│     │                 │       │                 ff43c6a652 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/select-editor 
│     │                 │                        ├ [1] : /usr/bin/sensible-browser 
│     │                 │                        ├ [2] : /usr/bin/sensible-editor 
│     │                 │                        ├ [3] : /usr/bin/sensible-pager 
│     │                 │                        ├ [4] : /usr/bin/sensible-terminal 
│     │                 │                        ├ [5] : /usr/lib/mime/packages/sensible-utils 
│     │                 │                        ├ [6] : /usr/share/doc/sensible-utils/changelog.gz 
│     │                 │                        ├ [7] : /usr/share/doc/sensible-utils/copyright 
│     │                 │                        ├ [8] : /usr/share/man/de/man1/select-editor.1.gz 
│     │                 │                        ├ [9] : /usr/share/man/de/man1/sensible-browser.1.gz 
│     │                 │                        ├ [10]: /usr/share/man/de/man1/sensible-editor.1.gz 
│     │                 │                        ├ [11]: /usr/share/man/de/man1/sensible-pager.1.gz 
│     │                 │                        ├ [12]: /usr/share/man/de/man1/sensible-terminal.1.gz 
│     │                 │                        ├ [13]: /usr/share/man/fr/man1/select-editor.1.gz 
│     │                 │                        ├ [14]: /usr/share/man/fr/man1/sensible-browser.1.gz 
│     │                 │                        ├ [15]: /usr/share/man/fr/man1/sensible-editor.1.gz 
│     │                 │                        ├ [16]: /usr/share/man/fr/man1/sensible-pager.1.gz 
│     │                 │                        ├ [17]: /usr/share/man/fr/man1/sensible-terminal.1.gz 
│     │                 │                        ├ [18]: /usr/share/man/man1/select-editor.1.gz 
│     │                 │                        ├ [19]: /usr/share/man/man1/sensible-browser.1.gz 
│     │                 │                        ├ [20]: /usr/share/man/man1/sensible-editor.1.gz 
│     │                 │                        ├ [21]: /usr/share/man/man1/sensible-pager.1.gz 
│     │                 │                        ├ [22]: /usr/share/man/man1/sensible-terminal.1.gz 
│     │                 │                        ├ [23]: /usr/share/man/pl/man1/sensible-editor.1.gz 
│     │                 │                        ├ [24]: /usr/share/man/pt/man1/select-editor.1.gz 
│     │                 │                        ├ [25]: /usr/share/man/pt/man1/sensible-browser.1.gz 
│     │                 │                        ╰ [26]: /usr/share/man/pt/man1/sensible-pager.1.gz 
│     │                 ├ [113] ╭ ID            : sudo@1.9.16p2-1ubuntu1.1 
│     │                 │       ├ Name          : sudo 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/sudo@1.9.16p2-1ubuntu1.1?arch=amd64&dis
│     │                 │       │                │       tro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 62556afad0ac11b7 
│     │                 │       ├ Version       : 1.9.16p2 
│     │                 │       ├ Release       : 1ubuntu1.1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : sudo 
│     │                 │       ├ SrcVersion    : 1.9.16p2 
│     │                 │       ├ SrcRelease    : 1ubuntu1.1 
│     │                 │       ├ Licenses       ╭ [0]: ISC 
│     │                 │       │                ├ [1]: BSD-2-Clause 
│     │                 │       │                ├ [2]: BSD-3-Clause 
│     │                 │       │                ├ [3]: Zlib 
│     │                 │       │                ├ [4]: other 
│     │                 │       │                ├ [5]: public-domain 
│     │                 │       │                ├ [6]: GPL-2.0-or-later 
│     │                 │       │                ╰ [7]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ╭ [0]: libapparmor1@4.1.0~beta5-0ubuntu14.2 
│     │                 │       │                ├ [1]: libaudit1@1:4.0.2-2ubuntu2 
│     │                 │       │                ├ [2]: libc6@2.41-6ubuntu1.2 
│     │                 │       │                ├ [3]: libpam-modules@1.5.3-7ubuntu4.4 
│     │                 │       │                ├ [4]: libpam0g@1.5.3-7ubuntu4.4 
│     │                 │       │                ├ [5]: libselinux1@3.7-3ubuntu3 
│     │                 │       │                ├ [6]: libssl3t64@3.4.1-1ubuntu4 
│     │                 │       │                ╰ [7]: zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu1 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/cvtsudoers 
│     │                 │                        ├ [1] : /usr/bin/sudo 
│     │                 │                        ├ [2] : /usr/bin/sudoreplay 
│     │                 │                        ├ [3] : /usr/include/sudo_plugin.h 
│     │                 │                        ├ [4] : /usr/lib/tmpfiles.d/sudo.conf 
│     │                 │                        ├ [5] : /usr/libexec/sudo/audit_json.so 
│     │                 │                        ├ [6] : /usr/libexec/sudo/group_file.so 
│     │                 │                        ├ [7] : /usr/libexec/sudo/libsudo_util.so.0.0.0 
│     │                 │                        ├ [8] : /usr/libexec/sudo/sesh 
│     │                 │                        ├ [9] : /usr/libexec/sudo/sudo_intercept.so 
│     │                 │                        ├ [10]: /usr/libexec/sudo/sudo_noexec.so 
│     │                 │                        ├ [11]: /usr/libexec/sudo/sudoers.so 
│     │                 │                        ├ [12]: /usr/libexec/sudo/system_group.so 
│     │                 │                        ├ [13]: /usr/sbin/sudo_logsrvd 
│     │                 │                        ├ [14]: /usr/sbin/sudo_sendlog 
│     │                 │                        ├ [15]: /usr/sbin/visudo 
│     │                 │                        ├ [16]: /usr/share/apport/package-hooks/source_sudo.py 
│     │                 │                        ├ [17]: /usr/share/doc/sudo/CONTRIBUTING.md 
│     │                 │                        ├ [18]: /usr/share/doc/sudo/CONTRIBUTORS.md.gz 
│     │                 │                        ├ [19]: /usr/share/doc/sudo/HISTORY.md 
│     │                 │                        ├ [20]: /usr/share/doc/sudo/NEWS.Debian.gz 
│     │                 │                        ├ [21]: /usr/share/doc/sudo/NEWS.gz 
│     │                 │                        ├ [22]: /usr/share/doc/sudo/OPTIONS 
│     │                 │                        ├ [23]: /usr/share/doc/sudo/README.Debian 
│     │                 │                        ├ [24]: /usr/share/doc/sudo/README.md 
│     │                 │                        ├ [25]: /usr/share/doc/sudo/SECURITY.md 
│     │                 │                        ├ [26]: /usr/share/doc/sudo/TROUBLESHOOTING.md.gz 
│     │                 │                        ├ [27]: /usr/share/doc/sudo/UPGRADE.md.gz 
│     │                 │                        ├ [28]: /usr/share/doc/sudo/changelog.Debian.gz 
│     │                 │                        ├ [29]: /usr/share/doc/sudo/copyright 
│     │                 │                        ├ [30]: /usr/share/doc/sudo/examples/cvtsudoers.conf 
│     │                 │                        ├ [31]: /usr/share/doc/sudo/examples/pam.conf 
│     │                 │                        ├ [32]: /usr/share/doc/sudo/examples/sudo.conf 
│     │                 │                        ├ [33]: /usr/share/doc/sudo/examples/sudo_logsrvd.conf 
│     │                 │                        ├ [34]: /usr/share/doc/sudo/examples/sudoers 
│     │                 │                        ├ [35]: /usr/share/doc/sudo/examples/sudoers.dist 
│     │                 │                        ├ [36]: /usr/share/doc/sudo/examples/syslog.conf 
│     │                 │                        ├ [37]: /usr/share/lintian/overrides/sudo 
│     │                 │                        ├ [38]: /usr/share/man/man1/cvtsudoers.1.gz 
│     │                 │                        ├ [39]: /usr/share/man/man5/sudo.conf.5.gz 
│     │                 │                        ├ [40]: /usr/share/man/man5/sudo_logsrv.proto.5.gz 
│     │                 │                        ├ [41]: /usr/share/man/man5/sudo_logsrvd.conf.5.gz 
│     │                 │                        ├ [42]: /usr/share/man/man5/sudo_plugin.5.gz 
│     │                 │                        ├ [43]: /usr/share/man/man5/sudoers.5.gz 
│     │                 │                        ├ [44]: /usr/share/man/man5/sudoers_timestamp.5.gz 
│     │                 │                        ├ [45]: /usr/share/man/man8/sudo.8.gz 
│     │                 │                        ├ [46]: /usr/share/man/man8/sudo_logsrvd.8.gz 
│     │                 │                        ├ [47]: /usr/share/man/man8/sudo_root.8.gz 
│     │                 │                        ├ [48]: /usr/share/man/man8/sudo_sendlog.8.gz 
│     │                 │                        ├ [49]: /usr/share/man/man8/sudoreplay.8.gz 
│     │                 │                        ╰ [50]: /usr/share/man/man8/visudo.8.gz 
│     │                 ├ [114] ╭ ID            : sysvinit-utils@3.14-1ubuntu1 
│     │                 │       ├ Name          : sysvinit-utils 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/sysvinit-utils@3.14-1ubuntu1?arch=amd64
│     │                 │       │                │       &distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 912b5cf46b7c9447 
│     │                 │       ├ Version       : 3.14 
│     │                 │       ├ Release       : 1ubuntu1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : sysvinit 
│     │                 │       ├ SrcVersion    : 3.14 
│     │                 │       ├ SrcRelease    : 1ubuntu1 
│     │                 │       ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│     │                 │       │                ├ [1]: LGPL-2.1-or-later 
│     │                 │       │                ├ [2]: GPL-3.0-only 
│     │                 │       │                ├ [3]: GPL-2.0-only 
│     │                 │       │                ╰ [4]: LGPL-2.1-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:5db5a09eb1abd577087404f5f551b50d94cbb1cac84c808503dbd6
│     │                 │       │                 877f50297c 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/lib/init/init-d-script 
│     │                 │                        ├ [1] : /usr/lib/init/vars.sh 
│     │                 │                        ├ [2] : /usr/lib/lsb/init-functions 
│     │                 │                        ├ [3] : /usr/lib/lsb/init-functions.d/00-verbose 
│     │                 │                        ├ [4] : /usr/lib/lsb/init-functions.d/50-ubuntu-logging 
│     │                 │                        ├ [5] : /usr/sbin/fstab-decode 
│     │                 │                        ├ [6] : /usr/sbin/killall5 
│     │                 │                        ├ [7] : /usr/share/doc/sysvinit-utils/changelog.Debian.gz 
│     │                 │                        ├ [8] : /usr/share/doc/sysvinit-utils/copyright 
│     │                 │                        ├ [9] : /usr/share/man/man5/init-d-script.5.gz 
│     │                 │                        ├ [10]: /usr/share/man/man8/fstab-decode.8.gz 
│     │                 │                        ├ [11]: /usr/share/man/man8/killall5.8.gz 
│     │                 │                        ╰ [12]: /usr/share/man/man8/pidof.8.gz 
│     │                 ├ [115] ╭ ID            : tar@1.35+dfsg-3.1 
│     │                 │       ├ Name          : tar 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-3.1?arch=amd64&distro=u
│     │                 │       │                │       buntu-25.04 
│     │                 │       │                ╰ UID : a03ee9a61d584e89 
│     │                 │       ├ Version       : 1.35+dfsg 
│     │                 │       ├ Release       : 3.1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : tar 
│     │                 │       ├ SrcVersion    : 1.35+dfsg 
│     │                 │       ├ SrcRelease    : 3.1 
│     │                 │       ├ Licenses       ╭ [0]: GPL-3.0-or-later 
│     │                 │       │                ├ [1]: GPL-3.0-only 
│     │                 │       │                ├ [2]: GPL-3+ with Bison exception 
│     │                 │       │                ├ [3]: LGPL-2.1-or-later 
│     │                 │       │                ├ [4]: LGPL-2.1-only 
│     │                 │       │                ├ [5]: LGPL-3.0-or-later 
│     │                 │       │                ├ [6]: LGPL-3.0-only 
│     │                 │       │                ├ [7]: GPL-2.0-or-later 
│     │                 │       │                ╰ [8]: GPL-2.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:491c813c2b94230de3253c6e05b8f54d62279d7d1e2ace05d7e4ee
│     │                 │       │                 0ed09a6df0 
│     │                 │       ╰ InstalledFiles ╭ [0] : /usr/bin/tar 
│     │                 │                        ├ [1] : /usr/lib/mime/packages/tar 
│     │                 │                        ├ [2] : /usr/sbin/rmt-tar 
│     │                 │                        ├ [3] : /usr/sbin/tarcat 
│     │                 │                        ├ [4] : /usr/share/doc/tar/AUTHORS 
│     │                 │                        ├ [5] : /usr/share/doc/tar/NEWS.gz 
│     │                 │                        ├ [6] : /usr/share/doc/tar/README.Debian 
│     │                 │                        ├ [7] : /usr/share/doc/tar/THANKS.gz 
│     │                 │                        ├ [8] : /usr/share/doc/tar/changelog.Debian.gz 
│     │                 │                        ├ [9] : /usr/share/doc/tar/copyright 
│     │                 │                        ├ [10]: /usr/share/man/man1/tar.1.gz 
│     │                 │                        ├ [11]: /usr/share/man/man1/tarcat.1.gz 
│     │                 │                        ╰ [12]: /usr/share/man/man8/rmt-tar.8.gz 
│     │                 ├ [116] ╭ ID            : ubuntu-keyring@2023.11.28.1 
│     │                 │       ├ Name          : ubuntu-keyring 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/ubuntu-keyring@2023.11.28.1?arch=all&di
│     │                 │       │                │       stro=ubuntu-25.04 
│     │                 │       │                ╰ UID : a1d74f9aa35f670c 
│     │                 │       ├ Version       : 2023.11.28.1 
│     │                 │       ├ Arch          : all 
│     │                 │       ├ SrcName       : ubuntu-keyring 
│     │                 │       ├ SrcVersion    : 2023.11.28.1 
│     │                 │       ├ Licenses       ─ [0]: GPL-2.0-or-later 
│     │                 │       ├ Maintainer    : Dimitri John Ledkov <dimitri.ledkov@canonical.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ├ Digest        : sha256:36de43b15853ccae0028e9a767613770c704833f82586f28eb262f
│     │                 │       │                 0311adb8a8 
│     │                 │       ╰ InstalledFiles ╭ [0]: /etc/apt/trusted.gpg.d/ubuntu-keyring-2012-cdimage.gpg 
│     │                 │                        ├ [1]: /etc/apt/trusted.gpg.d/ubuntu-keyring-2018-archive.gpg 
│     │                 │                        ├ [2]: /usr/share/doc/ubuntu-keyring/changelog.gz 
│     │                 │                        ├ [3]: /usr/share/doc/ubuntu-keyring/copyright 
│     │                 │                        ├ [4]: /usr/share/keyrings/ubuntu-archive-keyring.gpg 
│     │                 │                        ├ [5]: /usr/share/keyrings/ubuntu-archive-removed-keys.gpg 
│     │                 │                        ├ [6]: /usr/share/keyrings/ubuntu-cloudimage-keyring.gpg 
│     │                 │                        ├ [7]: /usr/share/keyrings/ubuntu-cloudimage-removed-keys.gpg 
│     │                 │                        ╰ [8]: /usr/share/keyrings/ubuntu-master-keyring.gpg 
│     │                 ├ [117] ╭ ID            : util-linux@2.40.2-14ubuntu1.1 
│     │                 │       ├ Name          : util-linux 
│     │                 │       ├ Identifier     ╭ PURL: pkg:deb/ubuntu/util-linux@2.40.2-14ubuntu1.1?arch=amd6
│     │                 │       │                │       4&distro=ubuntu-25.04 
│     │                 │       │                ╰ UID : 1492085ce715e7c5 
│     │                 │       ├ Version       : 2.40.2 
│     │                 │       ├ Release       : 14ubuntu1.1 
│     │                 │       ├ Arch          : amd64 
│     │                 │       ├ SrcName       : util-linux 
│     │                 │       ├ SrcVersion    : 2.40.2 
│     │                 │       ├ SrcRelease    : 14ubuntu1.1 
│     │                 │       ├ Licenses       ╭ [0] : GPL-2.0-or-later 
│     │                 │       │                ├ [1] : GPL-2.0-only 
│     │                 │       │                ├ [2] : GPL-3.0-or-later 
│     │                 │       │                ├ [3] : LGPL-2.1-or-later 
│     │                 │       │                ├ [4] : public-domain 
│     │                 │       │                ├ [5] : BSD-4-Clause 
│     │                 │       │                ├ [6] : MIT 
│     │                 │       │                ├ [7] : ISC 
│     │                 │       │                ├ [8] : BSD-3-Clause 
│     │                 │       │                ├ [9] : BSLA 
│     │                 │       │                ├ [10]: LGPL-2.0-or-later 
│     │                 │       │                ├ [11]: BSD-2-Clause 
│     │                 │       │                ├ [12]: LGPL-3.0-or-later 
│     │                 │       │                ├ [13]: GPL-3.0-only 
│     │                 │       │                ├ [14]: LGPL-2.0-only 
│     │                 │       │                ├ [15]: LGPL-2.1-only 
│     │                 │       │                ╰ [16]: LGPL-3.0-only 
│     │                 │       ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                 │       ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                 │       │                │         6ba98c37923562c6ba4 
│     │                 │       │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                 │       │                          a60c40f64c3148c1317 
│     │                 │       ╰ InstalledFiles ╭ [0]  : /usr/bin/choom 
│     │                 │                        ├ [1]  : /usr/bin/chrt 
│     │                 │                        ├ [2]  : /usr/bin/dmesg 
│     │                 │                        ├ [3]  : /usr/bin/fallocate 
│     │                 │                        ├ [4]  : /usr/bin/findmnt 
│     │                 │                        ├ [5]  : /usr/bin/flock 
│     │                 │                        ├ [6]  : /usr/bin/getopt 
│     │                 │                        ├ [7]  : /usr/bin/hardlink 
│     │                 │                        ├ [8]  : /usr/bin/ionice 
│     │                 │                        ├ [9]  : /usr/bin/ipcmk 
│     │                 │                        ├ [10] : /usr/bin/ipcrm 
│     │                 │                        ├ [11] : /usr/bin/ipcs 
│     │                 │                        ├ [12] : /usr/bin/lsblk 
│     │                 │                        ├ [13] : /usr/bin/lscpu 
│     │                 │                        ├ [14] : /usr/bin/lsipc 
│     │                 │                        ├ [15] : /usr/bin/lslocks 
│     │                 │                        ├ [16] : /usr/bin/lslogins 
│     │                 │                        ├ [17] : /usr/bin/lsmem 
│     │                 │                        ├ [18] : /usr/bin/lsns 
│     │                 │                        ├ [19] : /usr/bin/mcookie 
│     │                 │                        ├ [20] : /usr/bin/more 
│     │                 │                        ├ [21] : /usr/bin/mountpoint 
│     │                 │                        ├ [22] : /usr/bin/namei 
│     │                 │                        ├ [23] : /usr/bin/nsenter 
│     │                 │                        ├ [24] : /usr/bin/partx 
│     │                 │                        ├ [25] : /usr/bin/prlimit 
│     │                 │                        ├ [26] : /usr/bin/rename.ul 
│     │                 │                        ├ [27] : /usr/bin/resizepart 
│     │                 │                        ├ [28] : /usr/bin/rev 
│     │                 │                        ├ [29] : /usr/bin/setarch 
│     │                 │                        ├ [30] : /usr/bin/setpriv 
│     │                 │                        ├ [31] : /usr/bin/setsid 
│     │                 │                        ├ [32] : /usr/bin/setterm 
│     │                 │                        ├ [33] : /usr/bin/su 
│     │                 │                        ├ [34] : /usr/bin/taskset 
│     │                 │                        ├ [35] : /usr/bin/uclampset 
│     │                 │                        ├ [36] : /usr/bin/unshare 
│     │                 │                        ├ [37] : /usr/bin/wdctl 
│     │                 │                        ├ [38] : /usr/bin/whereis 
│     │                 │                        ├ [39] : /usr/lib/mime/packages/util-linux 
│     │                 │                        ├ [40] : /usr/lib/systemd/system/fstrim.service 
│     │                 │                        ├ [41] : /usr/lib/systemd/system/fstrim.timer 
│     │                 │                        ├ [42] : /usr/sbin/agetty 
│     │                 │                        ├ [43] : /usr/sbin/blkdiscard 
│     │                 │                        ├ [44] : /usr/sbin/blkid 
│     │                 │                        ├ [45] : /usr/sbin/blkzone 
│     │                 │                        ├ [46] : /usr/sbin/blockdev 
│     │                 │                        ├ [47] : /usr/sbin/chcpu 
│     │                 │                        ├ [48] : /usr/sbin/chmem 
│     │                 │                        ├ [49] : /usr/sbin/findfs 
│     │                 │                        ├ [50] : /usr/sbin/fsck 
│     │                 │                        ├ [51] : /usr/sbin/fsfreeze 
│     │                 │                        ├ [52] : /usr/sbin/fstrim 
│     │                 │                        ├ [53] : /usr/sbin/isosize 
│     │                 │                        ├ [54] : /usr/sbin/ldattach 
│     │                 │                        ├ [55] : /usr/sbin/mkfs 
│     │                 │                        ├ [56] : /usr/sbin/mkswap 
│     │                 │                        ├ [57] : /usr/sbin/pivot_root 
│     │                 │                        ├ [58] : /usr/sbin/readprofile 
│     │                 │                        ├ [59] : /usr/sbin/rtcwake 
│     │                 │                        ├ [60] : /usr/sbin/runuser 
│     │                 │                        ├ [61] : /usr/sbin/sulogin 
│     │                 │                        ├ [62] : /usr/sbin/swaplabel 
│     │                 │                        ├ [63] : /usr/sbin/switch_root 
│     │                 │                        ├ [64] : /usr/sbin/wipefs 
│     │                 │                        ├ [65] : /usr/sbin/zramctl 
│     │                 │                        ├ [66] : /usr/share/bash-completion/completions/blkdiscard 
│     │                 │                        ├ [67] : /usr/share/bash-completion/completions/blkid 
│     │                 │                        ├ [68] : /usr/share/bash-completion/completions/blkzone 
│     │                 │                        ├ [69] : /usr/share/bash-completion/completions/blockdev 
│     │                 │                        ├ [70] : /usr/share/bash-completion/completions/chcpu 
│     │                 │                        ├ [71] : /usr/share/bash-completion/completions/chmem 
│     │                 │                        ├ [72] : /usr/share/bash-completion/completions/chrt 
│     │                 │                        ├ [73] : /usr/share/bash-completion/completions/dmesg 
│     │                 │                        ├ [74] : /usr/share/bash-completion/completions/fallocate 
│     │                 │                        ├ [75] : /usr/share/bash-completion/completions/findfs 
│     │                 │                        ├ [76] : /usr/share/bash-completion/completions/findmnt 
│     │                 │                        ├ [77] : /usr/share/bash-completion/completions/flock 
│     │                 │                        ├ [78] : /usr/share/bash-completion/completions/fsck 
│     │                 │                        ├ [79] : /usr/share/bash-completion/completions/fsfreeze 
│     │                 │                        ├ [80] : /usr/share/bash-completion/completions/fstrim 
│     │                 │                        ├ [81] : /usr/share/bash-completion/completions/getopt 
│     │                 │                        ├ [82] : /usr/share/bash-completion/completions/hardlink 
│     │                 │                        ├ [83] : /usr/share/bash-completion/completions/ionice 
│     │                 │                        ├ [84] : /usr/share/bash-completion/completions/ipcmk 
│     │                 │                        ├ [85] : /usr/share/bash-completion/completions/ipcrm 
│     │                 │                        ├ [86] : /usr/share/bash-completion/completions/ipcs 
│     │                 │                        ├ [87] : /usr/share/bash-completion/completions/isosize 
│     │                 │                        ├ [88] : /usr/share/bash-completion/completions/ldattach 
│     │                 │                        ├ [89] : /usr/share/bash-completion/completions/lsblk 
│     │                 │                        ├ [90] : /usr/share/bash-completion/completions/lscpu 
│     │                 │                        ├ [91] : /usr/share/bash-completion/completions/lsipc 
│     │                 │                        ├ [92] : /usr/share/bash-completion/completions/lslocks 
│     │                 │                        ├ [93] : /usr/share/bash-completion/completions/lslogins 
│     │                 │                        ├ [94] : /usr/share/bash-completion/completions/lsmem 
│     │                 │                        ├ [95] : /usr/share/bash-completion/completions/lsns 
│     │                 │                        ├ [96] : /usr/share/bash-completion/completions/mcookie 
│     │                 │                        ├ [97] : /usr/share/bash-completion/completions/mkfs 
│     │                 │                        ├ [98] : /usr/share/bash-completion/completions/mkswap 
│     │                 │                        ├ [99] : /usr/share/bash-completion/completions/more 
│     │                 │                        ├ [100]: /usr/share/bash-completion/completions/mountpoint 
│     │                 │                        ├ [101]: /usr/share/bash-completion/completions/namei 
│     │                 │                        ├ [102]: /usr/share/bash-completion/completions/nsenter 
│     │                 │                        ├ [103]: /usr/share/bash-completion/completions/partx 
│     │                 │                        ├ [104]: /usr/share/bash-completion/completions/pivot_root 
│     │                 │                        ├ [105]: /usr/share/bash-completion/completions/prlimit 
│     │                 │                        ├ [106]: /usr/share/bash-completion/completions/readprofile 
│     │                 │                        ├ [107]: /usr/share/bash-completion/completions/resizepart 
│     │                 │                        ├ [108]: /usr/share/bash-completion/completions/rev 
│     │                 │                        ├ [109]: /usr/share/bash-completion/completions/rtcwake 
│     │                 │                        ├ [110]: /usr/share/bash-completion/completions/setarch 
│     │                 │                        ├ [111]: /usr/share/bash-completion/completions/setpriv 
│     │                 │                        ├ [112]: /usr/share/bash-completion/completions/setsid 
│     │                 │                        ├ [113]: /usr/share/bash-completion/completions/setterm 
│     │                 │                        ├ [114]: /usr/share/bash-completion/completions/su 
│     │                 │                        ├ [115]: /usr/share/bash-completion/completions/swaplabel 
│     │                 │                        ├ [116]: /usr/share/bash-completion/completions/taskset 
│     │                 │                        ├ [117]: /usr/share/bash-completion/completions/uclampset 
│     │                 │                        ├ [118]: /usr/share/bash-completion/completions/unshare 
│     │                 │                        ├ [119]: /usr/share/bash-completion/completions/wdctl 
│     │                 │                        ├ [120]: /usr/share/bash-completion/completions/whereis 
│     │                 │                        ├ [121]: /usr/share/bash-completion/completions/wipefs 
│     │                 │                        ├ [122]: /usr/share/bash-completion/completions/zramctl 
│     │                 │                        ├ [123]: /usr/share/doc/util-linux/00-about-docs.txt 
│     │                 │                        ├ [124]: /usr/share/doc/util-linux/AUTHORS.gz 
│     │                 │                        ├ [125]: /usr/share/doc/util-linux/NEWS.Debian.gz 
│     │                 │                        ├ [126]: /usr/share/doc/util-linux/PAM-configuration.txt 
│     │                 │                        ├ [127]: /usr/share/doc/util-linux/README.Debian 
│     │                 │                        ├ [128]: /usr/share/doc/util-linux/blkid.txt 
│     │                 │                        ├ [129]: /usr/share/doc/util-linux/cal.txt 
│     │                 │                        ├ [130]: /usr/share/doc/util-linux/changelog.Debian.gz 
│     │                 │                        ├ [131]: /usr/share/doc/util-linux/col.txt 
│     │                 │                        ├ [132]: /usr/share/doc/util-linux/copyright 
│     │                 │                        ├ [133]: /usr/share/doc/util-linux/deprecated.txt 
│     │                 │                        ├ [134]: /usr/share/doc/util-linux/examples/getopt-example.bash 
│     │                 │                        ├ [135]: /usr/share/doc/util-linux/getopt.txt 
│     │                 │                        ├ [136]: /usr/share/doc/util-linux/getopt_changelog.txt 
│     │                 │                        ├ [137]: /usr/share/doc/util-linux/howto-build-sys.txt 
│     │                 │                        ├ [138]: /usr/share/doc/util-linux/howto-compilation.txt 
│     │                 │                        ├ [139]: /usr/share/doc/util-linux/howto-contribute.txt.gz 
│     │                 │                        ├ [140]: /usr/share/doc/util-linux/howto-debug.txt 
│     │                 │                        ├ [141]: /usr/share/doc/util-linux/howto-man-page.txt 
│     │                 │                        ├ [142]: /usr/share/doc/util-linux/howto-pull-request.txt.gz 
│     │                 │                        ├ [143]: /usr/share/doc/util-linux/howto-tests.txt 
│     │                 │                        ├ [144]: /usr/share/doc/util-linux/howto-usage-function.txt.gz 
│     │                 │                        ├ [145]: /usr/share/doc/util-linux/hwclock.txt 
│     │                 │                        ├ [146]: /usr/share/doc/util-linux/modems-with-agetty.txt 
│     │                 │                        ├ [147]: /usr/share/doc/util-linux/mount.txt 
│     │                 │                        ├ [148]: /usr/share/doc/util-linux/parse-date.txt.gz 
│     │                 │                        ├ [149]: /usr/share/doc/util-linux/pg.txt 
│     │                 │                        ├ [150]: /usr/share/doc/util-linux/poeigl.txt.gz 
│     │                 │                        ├ [151]: /usr/share/doc/util-linux/release-schedule.txt 
│     │                 │                        ├ [152]: /usr/share/doc/util-linux/releases/v2.13-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [153]: /usr/share/doc/util-linux/releases/v2.14-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [154]: /usr/share/doc/util-linux/releases/v2.15-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [155]: /usr/share/doc/util-linux/releases/v2.16-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [156]: /usr/share/doc/util-linux/releases/v2.17-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [157]: /usr/share/doc/util-linux/releases/v2.18-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [158]: /usr/share/doc/util-linux/releases/v2.19-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [159]: /usr/share/doc/util-linux/releases/v2.20-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [160]: /usr/share/doc/util-linux/releases/v2.21-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [161]: /usr/share/doc/util-linux/releases/v2.22-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [162]: /usr/share/doc/util-linux/releases/v2.23-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [163]: /usr/share/doc/util-linux/releases/v2.24-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [164]: /usr/share/doc/util-linux/releases/v2.25-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [165]: /usr/share/doc/util-linux/releases/v2.26-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [166]: /usr/share/doc/util-linux/releases/v2.27-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [167]: /usr/share/doc/util-linux/releases/v2.28-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [168]: /usr/share/doc/util-linux/releases/v2.29-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [169]: /usr/share/doc/util-linux/releases/v2.30-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [170]: /usr/share/doc/util-linux/releases/v2.31-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [171]: /usr/share/doc/util-linux/releases/v2.32-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [172]: /usr/share/doc/util-linux/releases/v2.33-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [173]: /usr/share/doc/util-linux/releases/v2.34-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [174]: /usr/share/doc/util-linux/releases/v2.35-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [175]: /usr/share/doc/util-linux/releases/v2.36-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [176]: /usr/share/doc/util-linux/releases/v2.37-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [177]: /usr/share/doc/util-linux/releases/v2.38-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [178]: /usr/share/doc/util-linux/releases/v2.39-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [179]: /usr/share/doc/util-linux/releases/v2.40-ReleaseNotes
│     │                 │                        │        .gz 
│     │                 │                        ├ [180]: /usr/share/doc/util-linux/releases/v2.40.1-ReleaseNot
│     │                 │                        │        es.gz 
│     │                 │                        ├ [181]: /usr/share/doc/util-linux/releases/v2.40.2-ReleaseNotes 
│     │                 │                        ├ [182]: /usr/share/lintian/overrides/util-linux 
│     │                 │                        ├ [183]: /usr/share/man/man1/choom.1.gz 
│     │                 │                        ├ [184]: /usr/share/man/man1/chrt.1.gz 
│     │                 │                        ├ [185]: /usr/share/man/man1/dmesg.1.gz 
│     │                 │                        ├ [186]: /usr/share/man/man1/fallocate.1.gz 
│     │                 │                        ├ [187]: /usr/share/man/man1/flock.1.gz 
│     │                 │                        ├ [188]: /usr/share/man/man1/getopt.1.gz 
│     │                 │                        ├ [189]: /usr/share/man/man1/hardlink.1.gz 
│     │                 │                        ├ [190]: /usr/share/man/man1/ionice.1.gz 
│     │                 │                        ├ [191]: /usr/share/man/man1/ipcmk.1.gz 
│     │                 │                        ├ [192]: /usr/share/man/man1/ipcrm.1.gz 
│     │                 │                        ├ [193]: /usr/share/man/man1/ipcs.1.gz 
│     │                 │                        ├ [194]: /usr/share/man/man1/lscpu.1.gz 
│     │                 │                        ├ [195]: /usr/share/man/man1/lsipc.1.gz 
│     │                 │                        ├ [196]: /usr/share/man/man1/lslogins.1.gz 
│     │                 │                        ├ [197]: /usr/share/man/man1/lsmem.1.gz 
│     │                 │                        ├ [198]: /usr/share/man/man1/mcookie.1.gz 
│     │                 │                        ├ [199]: /usr/share/man/man1/more.1.gz 
│     │                 │                        ├ [200]: /usr/share/man/man1/mountpoint.1.gz 
│     │                 │                        ├ [201]: /usr/share/man/man1/namei.1.gz 
│     │                 │                        ├ [202]: /usr/share/man/man1/nsenter.1.gz 
│     │                 │                        ├ [203]: /usr/share/man/man1/prlimit.1.gz 
│     │                 │                        ├ [204]: /usr/share/man/man1/rename.ul.1.gz 
│     │                 │                        ├ [205]: /usr/share/man/man1/rev.1.gz 
│     │                 │                        ├ [206]: /usr/share/man/man1/runuser.1.gz 
│     │                 │                        ├ [207]: /usr/share/man/man1/setpriv.1.gz 
│     │                 │                        ├ [208]: /usr/share/man/man1/setsid.1.gz 
│     │                 │                        ├ [209]: /usr/share/man/man1/setterm.1.gz 
│     │                 │                        ├ [210]: /usr/share/man/man1/su.1.gz 
│     │                 │                        ├ [211]: /usr/share/man/man1/taskset.1.gz 
│     │                 │                        ├ [212]: /usr/share/man/man1/uclampset.1.gz 
│     │                 │                        ├ [213]: /usr/share/man/man1/unshare.1.gz 
│     │                 │                        ├ [214]: /usr/share/man/man1/whereis.1.gz 
│     │                 │                        ├ [215]: /usr/share/man/man5/adjtime_config.5.gz 
│     │                 │                        ├ [216]: /usr/share/man/man5/terminal-colors.d.5.gz 
│     │                 │                        ├ [217]: /usr/share/man/man8/agetty.8.gz 
│     │                 │                        ├ [218]: /usr/share/man/man8/blkdiscard.8.gz 
│     │                 │                        ├ [219]: /usr/share/man/man8/blkid.8.gz 
│     │                 │                        ├ [220]: /usr/share/man/man8/blkzone.8.gz 
│     │                 │                        ├ [221]: /usr/share/man/man8/blockdev.8.gz 
│     │                 │                        ├ [222]: /usr/share/man/man8/chcpu.8.gz 
│     │                 │                        ├ [223]: /usr/share/man/man8/chmem.8.gz 
│     │                 │                        ├ [224]: /usr/share/man/man8/findfs.8.gz 
│     │                 │                        ├ [225]: /usr/share/man/man8/findmnt.8.gz 
│     │                 │                        ├ [226]: /usr/share/man/man8/fsck.8.gz 
│     │                 │                        ├ [227]: /usr/share/man/man8/fsfreeze.8.gz 
│     │                 │                        ├ [228]: /usr/share/man/man8/fstrim.8.gz 
│     │                 │                        ├ [229]: /usr/share/man/man8/isosize.8.gz 
│     │                 │                        ├ [230]: /usr/share/man/man8/ldattach.8.gz 
│     │                 │                        ├ [231]: /usr/share/man/man8/lsblk.8.gz 
│     │                 │                        ├ [232]: /usr/share/man/man8/lslocks.8.gz 
│     │                 │                        ├ [233]: /usr/share/man/man8/lsns.8.gz 
│     │                 │                        ├ [234]: /usr/share/man/man8/mkfs.8.gz 
│     │                 │                        ├ [235]: /usr/share/man/man8/mkswap.8.gz 
│     │                 │                        ├ [236]: /usr/share/man/man8/partx.8.gz 
│     │                 │                        ├ [237]: /usr/share/man/man8/pivot_root.8.gz 
│     │                 │                        ├ [238]: /usr/share/man/man8/readprofile.8.gz 
│     │                 │                        ├ [239]: /usr/share/man/man8/resizepart.8.gz 
│     │                 │                        ├ [240]: /usr/share/man/man8/rtcwake.8.gz 
│     │                 │                        ├ [241]: /usr/share/man/man8/setarch.8.gz 
│     │                 │                        ├ [242]: /usr/share/man/man8/sulogin.8.gz 
│     │                 │                        ├ [243]: /usr/share/man/man8/swaplabel.8.gz 
│     │                 │                        ├ [244]: /usr/share/man/man8/switch_root.8.gz 
│     │                 │                        ├ [245]: /usr/share/man/man8/wdctl.8.gz 
│     │                 │                        ├ [246]: /usr/share/man/man8/wipefs.8.gz 
│     │                 │                        ├ [247]: /usr/share/man/man8/zramctl.8.gz 
│     │                 │                        ╰ [248]: /usr/share/util-linux/logcheck/ignore.d.server/util-l
│     │                 │                                 inux 
│     │                 ╰ [118] ╭ ID            : zlib1g@1:1.3.dfsg+really1.3.1-1ubuntu1 
│     │                         ├ Name          : zlib1g 
│     │                         ├ Identifier     ╭ PURL: pkg:deb/ubuntu/zlib1g@1.3.dfsg%2Breally1.3.1-1ubuntu1?
│     │                         │                │       arch=amd64&distro=ubuntu-25.04&epoch=1 
│     │                         │                ╰ UID : b037afce5c0cbe60 
│     │                         ├ Version       : 1.3.dfsg+really1.3.1 
│     │                         ├ Release       : 1ubuntu1 
│     │                         ├ Epoch         : 1 
│     │                         ├ Arch          : amd64 
│     │                         ├ SrcName       : zlib 
│     │                         ├ SrcVersion    : 1.3.dfsg+really1.3.1 
│     │                         ├ SrcRelease    : 1ubuntu1 
│     │                         ├ SrcEpoch      : 1 
│     │                         ├ Licenses       ─ [0]: Zlib 
│     │                         ├ Maintainer    : Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com> 
│     │                         ├ DependsOn      ─ [0]: libc6@2.41-6ubuntu1.2 
│     │                         ├ Layer          ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb
│     │                         │                │         6ba98c37923562c6ba4 
│     │                         │                ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1
│     │                         │                          a60c40f64c3148c1317 
│     │                         ├ Digest        : sha256:bf8e492a5ee29396802e0c8f1608a9926df9fac0174388d174f1e2
│     │                         │                 b919f79bfa 
│     │                         ╰ InstalledFiles ╭ [0]: /usr/lib/x86_64-linux-gnu/libz.so.1.3.1 
│     │                                          ├ [1]: /usr/share/doc/zlib1g/changelog.Debian.gz 
│     │                                          ╰ [2]: /usr/share/doc/zlib1g/copyright 
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2016-2781 
│                       │      ├ PkgID           : coreutils@9.5-1ubuntu1.25.04.2 
│                       │      ├ PkgName         : coreutils 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/coreutils@9.5-1ubuntu1.25.04.2?arch=am
│                       │      │                  │       d64&distro=ubuntu-25.04 
│                       │      │                  ╰ UID : fb90d22e49e1fb47 
│                       │      ├ InstalledVersion: 9.5-1ubuntu1.25.04.2 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
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
│                       │      ╰ LastModifiedDate: 2025-06-09T16:15:25.013Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2025-10148 
│                       │      ├ PkgID           : curl@8.12.1-3ubuntu1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.12.1-3ubuntu1?arch=amd64&distro
│                       │      │                  │       =ubuntu-25.04 
│                       │      │                  ╰ UID : 6ea7a92c5821dca8 
│                       │      ├ InstalledVersion: 8.12.1-3ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-10148 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : curl: predictable WebSocket mask 
│                       │      ├ Description     : curl's websocket code did not update the 32 bit mask pattern
│                       │      │                    for each new
│                       │      │                    outgoing frame as the specification says. Instead it used a
│                       │      │                    fixed mask that
│                       │      │                   persisted and was used throughout the entire connection.
│                       │      │                   
│                       │      │                   A predictable mask pattern allows for a malicious server to
│                       │      │                   induce traffic
│                       │      │                   between the two communicating parties that could be
│                       │      │                   interpreted by an involved
│                       │      │                   proxy (configured or transparent) as genuine, real, HTTP
│                       │      │                   traffic with content
│                       │      │                   and thereby poison its cache. That cached poisoned content
│                       │      │                   could then be
│                       │      │                   served to all users of that proxy. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-10148 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2025-10148.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-10148.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3330839 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2025-10148 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2025-10148 
│                       │      ├ PublishedDate   : 2025-09-12T06:15:40.02Z 
│                       │      ╰ LastModifiedDate: 2025-09-15T15:21:42.937Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2025-9086 
│                       │      ├ PkgID           : curl@8.12.1-3ubuntu1 
│                       │      ├ PkgName         : curl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/curl@8.12.1-3ubuntu1?arch=amd64&distro
│                       │      │                  │       =ubuntu-25.04 
│                       │      │                  ╰ UID : 6ea7a92c5821dca8 
│                       │      ├ InstalledVersion: 8.12.1-3ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-9086 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : curl: libcurl: Curl out of bounds read for cookie path 
│                       │      ├ Description     : 1. A cookie is set using the `secure` keyword for
│                       │      │                   `https://target`
│                       │      │                   2. curl is redirected to or otherwise made to speak with
│                       │      │                   `http://target` (same
│                       │      │                      hostname, but using clear text HTTP) using the same
│                       │      │                   cookie set
│                       │      │                   3. The same cookie name is set - but with just a slash as
│                       │      │                   path (`path='/'`).
│                       │      │                      Since this site is not secure, the cookie *should* just
│                       │      │                   be ignored.
│                       │      │                   4. A bug in the path comparison logic makes curl read
│                       │      │                   outside a heap buffer
│                       │      │                      boundary
│                       │      │                   
│                       │      │                   The bug either causes a crash or it potentially makes the
│                       │      │                   comparison come to
│                       │      │                   the wrong conclusion and lets the clear-text site override
│                       │      │                   the contents of the
│                       │      │                   secure cookie, contrary to expectations and depending on the
│                       │      │                    memory contents
│                       │      │                   immediately following the single-byte allocation that holds
│                       │      │                   the path.
│                       │      │                   The presumed and correct behavior would be to plainly ignore
│                       │      │                    the second set of
│                       │      │                   the cookie since it was already set as secure on a secure
│                       │      │                   host so overriding
│                       │      │                   it on an insecure host should not be okay. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-9086 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2025-9086.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-9086.json 
│                       │      │                  ├ [3]: https://github.com/curl/curl/commit/c6ae07c6a541e0e96d
│                       │      │                  │      0040afb6 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3294999 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2025-9086 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2025-9086 
│                       │      ├ PublishedDate   : 2025-09-12T06:15:44.1Z 
│                       │      ╰ LastModifiedDate: 2025-09-15T15:21:42.937Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2022-3219 
│                       │      ├ PkgID           : gpgv@2.4.4-2ubuntu23.1 
│                       │      ├ PkgName         : gpgv 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/gpgv@2.4.4-2ubuntu23.1?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-25.04 
│                       │      │                  ╰ UID : d2a702b753c09f0f 
│                       │      ├ InstalledVersion: 2.4.4-2ubuntu23.1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
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
│                       │      ╰ LastModifiedDate: 2025-03-12T21:15:38.207Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2025-10148 
│                       │      ├ PkgID           : libcurl4t64@8.12.1-3ubuntu1 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.12.1-3ubuntu1?arch=amd64
│                       │      │                  │       &distro=ubuntu-25.04 
│                       │      │                  ╰ UID : e39d89d31b7d2391 
│                       │      ├ InstalledVersion: 8.12.1-3ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-10148 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : curl: predictable WebSocket mask 
│                       │      ├ Description     : curl's websocket code did not update the 32 bit mask pattern
│                       │      │                    for each new
│                       │      │                    outgoing frame as the specification says. Instead it used a
│                       │      │                    fixed mask that
│                       │      │                   persisted and was used throughout the entire connection.
│                       │      │                   
│                       │      │                   A predictable mask pattern allows for a malicious server to
│                       │      │                   induce traffic
│                       │      │                   between the two communicating parties that could be
│                       │      │                   interpreted by an involved
│                       │      │                   proxy (configured or transparent) as genuine, real, HTTP
│                       │      │                   traffic with content
│                       │      │                   and thereby poison its cache. That cached poisoned content
│                       │      │                   could then be
│                       │      │                   served to all users of that proxy. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-10148 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2025-10148.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-10148.json 
│                       │      │                  ├ [3]: https://hackerone.com/reports/3330839 
│                       │      │                  ├ [4]: https://nvd.nist.gov/vuln/detail/CVE-2025-10148 
│                       │      │                  ╰ [5]: https://www.cve.org/CVERecord?id=CVE-2025-10148 
│                       │      ├ PublishedDate   : 2025-09-12T06:15:40.02Z 
│                       │      ╰ LastModifiedDate: 2025-09-15T15:21:42.937Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2025-9086 
│                       │      ├ PkgID           : libcurl4t64@8.12.1-3ubuntu1 
│                       │      ├ PkgName         : libcurl4t64 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libcurl4t64@8.12.1-3ubuntu1?arch=amd64
│                       │      │                  │       &distro=ubuntu-25.04 
│                       │      │                  ╰ UID : e39d89d31b7d2391 
│                       │      ├ InstalledVersion: 8.12.1-3ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-9086 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : curl: libcurl: Curl out of bounds read for cookie path 
│                       │      ├ Description     : 1. A cookie is set using the `secure` keyword for
│                       │      │                   `https://target`
│                       │      │                   2. curl is redirected to or otherwise made to speak with
│                       │      │                   `http://target` (same
│                       │      │                      hostname, but using clear text HTTP) using the same
│                       │      │                   cookie set
│                       │      │                   3. The same cookie name is set - but with just a slash as
│                       │      │                   path (`path='/'`).
│                       │      │                      Since this site is not secure, the cookie *should* just
│                       │      │                   be ignored.
│                       │      │                   4. A bug in the path comparison logic makes curl read
│                       │      │                   outside a heap buffer
│                       │      │                      boundary
│                       │      │                   
│                       │      │                   The bug either causes a crash or it potentially makes the
│                       │      │                   comparison come to
│                       │      │                   the wrong conclusion and lets the clear-text site override
│                       │      │                   the contents of the
│                       │      │                   secure cookie, contrary to expectations and depending on the
│                       │      │                    memory contents
│                       │      │                   immediately following the single-byte allocation that holds
│                       │      │                   the path.
│                       │      │                   The presumed and correct behavior would be to plainly ignore
│                       │      │                    the second set of
│                       │      │                   the cookie since it was already set as secure on a secure
│                       │      │                   host so overriding
│                       │      │                   it on an insecure host should not be okay. 
│                       │      ├ Severity        : LOW 
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 1 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.3 
│                       │      ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-9086 
│                       │      │                  ├ [1]: https://curl.se/docs/CVE-2025-9086.html 
│                       │      │                  ├ [2]: https://curl.se/docs/CVE-2025-9086.json 
│                       │      │                  ├ [3]: https://github.com/curl/curl/commit/c6ae07c6a541e0e96d
│                       │      │                  │      0040afb6 
│                       │      │                  ├ [4]: https://hackerone.com/reports/3294999 
│                       │      │                  ├ [5]: https://nvd.nist.gov/vuln/detail/CVE-2025-9086 
│                       │      │                  ╰ [6]: https://www.cve.org/CVERecord?id=CVE-2025-9086 
│                       │      ├ PublishedDate   : 2025-09-12T06:15:44.1Z 
│                       │      ╰ LastModifiedDate: 2025-09-15T15:21:42.937Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2024-2236 
│                       │      ├ PkgID           : libgcrypt20@1.11.0-6ubuntu1 
│                       │      ├ PkgName         : libgcrypt20 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libgcrypt20@1.11.0-6ubuntu1?arch=amd64
│                       │      │                  │       &distro=ubuntu-25.04 
│                       │      │                  ╰ UID : 5a0c5e86aadb6057 
│                       │      ├ InstalledVersion: 1.11.0-6ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
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
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2025:3530 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2025:3534 
│                       │      │                  ├ [3] : https://access.redhat.com/security/cve/CVE-2024-2236 
│                       │      │                  ├ [4] : https://bugzilla.redhat.com/2245218 
│                       │      │                  ├ [5] : https://bugzilla.redhat.com/show_bug.cgi?id=2245218 
│                       │      │                  ├ [6] : https://bugzilla.redhat.com/show_bug.cgi?id=2268268 
│                       │      │                  ├ [7] : https://dev.gnupg.org/T7136 
│                       │      │                  ├ [8] : https://errata.almalinux.org/9/ALSA-2024-9404.html 
│                       │      │                  ├ [9] : https://github.com/tomato42/marvin-toolkit/tree/maste
│                       │      │                  │       r/example/libgcrypt 
│                       │      │                  ├ [10]: https://gitlab.com/redhat-crypto/libgcrypt/libgcrypt-
│                       │      │                  │       mirror/-/merge_requests/17 
│                       │      │                  ├ [11]: https://linux.oracle.com/cve/CVE-2024-2236.html 
│                       │      │                  ├ [12]: https://linux.oracle.com/errata/ELSA-2024-9404.html 
│                       │      │                  ├ [13]: https://lists.gnupg.org/pipermail/gcrypt-devel/2024-M
│                       │      │                  │       arch/005607.html 
│                       │      │                  ├ [14]: https://nvd.nist.gov/vuln/detail/CVE-2024-2236 
│                       │      │                  ╰ [15]: https://www.cve.org/CVERecord?id=CVE-2024-2236 
│                       │      ├ PublishedDate   : 2024-03-06T22:15:57.977Z 
│                       │      ╰ LastModifiedDate: 2025-04-02T17:15:37.79Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2025-8941 
│                       │      ├ PkgID           : libpam-modules@1.5.3-7ubuntu4.4 
│                       │      ├ PkgName         : libpam-modules 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam-modules@1.5.3-7ubuntu4.4?arch=a
│                       │      │                  │       md64&distro=ubuntu-25.04 
│                       │      │                  ╰ UID : c49554b6d433bfcd 
│                       │      ├ InstalledVersion: 1.5.3-7ubuntu4.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-8941 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : linux-pam: Incomplete fix for CVE-2025-6020 
│                       │      ├ Description     : A flaw was found in linux-pam. The pam_namespace module may
│                       │      │                   improperly handle user-controlled paths, allowing local
│                       │      │                   users to exploit symlink attacks and race conditions to
│                       │      │                   elevate their privileges to root. This CVE provides a
│                       │      │                   "complete" fix for CVE-2025-6020. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:14557 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2025:15099 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2025:15100 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2025:15101 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2025:15102 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2025:15103 
│                       │      │                  ├ [6] : https://access.redhat.com/errata/RHSA-2025:15104 
│                       │      │                  ├ [7] : https://access.redhat.com/errata/RHSA-2025:15105 
│                       │      │                  ├ [8] : https://access.redhat.com/errata/RHSA-2025:15106 
│                       │      │                  ├ [9] : https://access.redhat.com/errata/RHSA-2025:15107 
│                       │      │                  ├ [10]: https://access.redhat.com/errata/RHSA-2025:15709 
│                       │      │                  ├ [11]: https://access.redhat.com/errata/RHSA-2025:15827 
│                       │      │                  ├ [12]: https://access.redhat.com/errata/RHSA-2025:15828 
│                       │      │                  ├ [13]: https://access.redhat.com/errata/RHSA-2025:16524 
│                       │      │                  ├ [14]: https://access.redhat.com/security/cve/CVE-2025-8941 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/2372512 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/2388220 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2372512 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2388220 
│                       │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-6020 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-8941 
│                       │      │                  ├ [21]: https://errata.almalinux.org/9/ALSA-2025-15099.html 
│                       │      │                  ├ [22]: https://errata.rockylinux.org/RLSA-2025:14557 
│                       │      │                  ├ [23]: https://linux.oracle.com/cve/CVE-2025-8941.html 
│                       │      │                  ├ [24]: https://linux.oracle.com/errata/ELSA-2025-15099.html 
│                       │      │                  ├ [25]: https://nvd.nist.gov/vuln/detail/CVE-2025-8941 
│                       │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2025-8941 
│                       │      ├ PublishedDate   : 2025-08-13T15:15:41.873Z 
│                       │      ╰ LastModifiedDate: 2025-09-23T20:15:33.927Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2025-8941 
│                       │      ├ PkgID           : libpam-modules-bin@1.5.3-7ubuntu4.4 
│                       │      ├ PkgName         : libpam-modules-bin 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam-modules-bin@1.5.3-7ubuntu4.4?ar
│                       │      │                  │       ch=amd64&distro=ubuntu-25.04 
│                       │      │                  ╰ UID : 5357e0bb8a1ff079 
│                       │      ├ InstalledVersion: 1.5.3-7ubuntu4.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-8941 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : linux-pam: Incomplete fix for CVE-2025-6020 
│                       │      ├ Description     : A flaw was found in linux-pam. The pam_namespace module may
│                       │      │                   improperly handle user-controlled paths, allowing local
│                       │      │                   users to exploit symlink attacks and race conditions to
│                       │      │                   elevate their privileges to root. This CVE provides a
│                       │      │                   "complete" fix for CVE-2025-6020. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:14557 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2025:15099 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2025:15100 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2025:15101 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2025:15102 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2025:15103 
│                       │      │                  ├ [6] : https://access.redhat.com/errata/RHSA-2025:15104 
│                       │      │                  ├ [7] : https://access.redhat.com/errata/RHSA-2025:15105 
│                       │      │                  ├ [8] : https://access.redhat.com/errata/RHSA-2025:15106 
│                       │      │                  ├ [9] : https://access.redhat.com/errata/RHSA-2025:15107 
│                       │      │                  ├ [10]: https://access.redhat.com/errata/RHSA-2025:15709 
│                       │      │                  ├ [11]: https://access.redhat.com/errata/RHSA-2025:15827 
│                       │      │                  ├ [12]: https://access.redhat.com/errata/RHSA-2025:15828 
│                       │      │                  ├ [13]: https://access.redhat.com/errata/RHSA-2025:16524 
│                       │      │                  ├ [14]: https://access.redhat.com/security/cve/CVE-2025-8941 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/2372512 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/2388220 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2372512 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2388220 
│                       │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-6020 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-8941 
│                       │      │                  ├ [21]: https://errata.almalinux.org/9/ALSA-2025-15099.html 
│                       │      │                  ├ [22]: https://errata.rockylinux.org/RLSA-2025:14557 
│                       │      │                  ├ [23]: https://linux.oracle.com/cve/CVE-2025-8941.html 
│                       │      │                  ├ [24]: https://linux.oracle.com/errata/ELSA-2025-15099.html 
│                       │      │                  ├ [25]: https://nvd.nist.gov/vuln/detail/CVE-2025-8941 
│                       │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2025-8941 
│                       │      ├ PublishedDate   : 2025-08-13T15:15:41.873Z 
│                       │      ╰ LastModifiedDate: 2025-09-23T20:15:33.927Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2025-8941 
│                       │      ├ PkgID           : libpam-runtime@1.5.3-7ubuntu4.4 
│                       │      ├ PkgName         : libpam-runtime 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam-runtime@1.5.3-7ubuntu4.4?arch=a
│                       │      │                  │       ll&distro=ubuntu-25.04 
│                       │      │                  ╰ UID : ff7c6fc616e7055b 
│                       │      ├ InstalledVersion: 1.5.3-7ubuntu4.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-8941 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : linux-pam: Incomplete fix for CVE-2025-6020 
│                       │      ├ Description     : A flaw was found in linux-pam. The pam_namespace module may
│                       │      │                   improperly handle user-controlled paths, allowing local
│                       │      │                   users to exploit symlink attacks and race conditions to
│                       │      │                   elevate their privileges to root. This CVE provides a
│                       │      │                   "complete" fix for CVE-2025-6020. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:14557 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2025:15099 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2025:15100 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2025:15101 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2025:15102 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2025:15103 
│                       │      │                  ├ [6] : https://access.redhat.com/errata/RHSA-2025:15104 
│                       │      │                  ├ [7] : https://access.redhat.com/errata/RHSA-2025:15105 
│                       │      │                  ├ [8] : https://access.redhat.com/errata/RHSA-2025:15106 
│                       │      │                  ├ [9] : https://access.redhat.com/errata/RHSA-2025:15107 
│                       │      │                  ├ [10]: https://access.redhat.com/errata/RHSA-2025:15709 
│                       │      │                  ├ [11]: https://access.redhat.com/errata/RHSA-2025:15827 
│                       │      │                  ├ [12]: https://access.redhat.com/errata/RHSA-2025:15828 
│                       │      │                  ├ [13]: https://access.redhat.com/errata/RHSA-2025:16524 
│                       │      │                  ├ [14]: https://access.redhat.com/security/cve/CVE-2025-8941 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/2372512 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/2388220 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2372512 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2388220 
│                       │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-6020 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-8941 
│                       │      │                  ├ [21]: https://errata.almalinux.org/9/ALSA-2025-15099.html 
│                       │      │                  ├ [22]: https://errata.rockylinux.org/RLSA-2025:14557 
│                       │      │                  ├ [23]: https://linux.oracle.com/cve/CVE-2025-8941.html 
│                       │      │                  ├ [24]: https://linux.oracle.com/errata/ELSA-2025-15099.html 
│                       │      │                  ├ [25]: https://nvd.nist.gov/vuln/detail/CVE-2025-8941 
│                       │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2025-8941 
│                       │      ├ PublishedDate   : 2025-08-13T15:15:41.873Z 
│                       │      ╰ LastModifiedDate: 2025-09-23T20:15:33.927Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2025-8941 
│                       │      ├ PkgID           : libpam0g@1.5.3-7ubuntu4.4 
│                       │      ├ PkgName         : libpam0g 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/libpam0g@1.5.3-7ubuntu4.4?arch=amd64&d
│                       │      │                  │       istro=ubuntu-25.04 
│                       │      │                  ╰ UID : e7da9492a7d7e6e9 
│                       │      ├ InstalledVersion: 1.5.3-7ubuntu4.4 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
│                       │      ├ SeveritySource  : ubuntu 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-8941 
│                       │      ├ DataSource       ╭ ID  : ubuntu 
│                       │      │                  ├ Name: Ubuntu CVE Tracker 
│                       │      │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                       │      ├ Title           : linux-pam: Incomplete fix for CVE-2025-6020 
│                       │      ├ Description     : A flaw was found in linux-pam. The pam_namespace module may
│                       │      │                   improperly handle user-controlled paths, allowing local
│                       │      │                   users to exploit symlink attacks and race conditions to
│                       │      │                   elevate their privileges to root. This CVE provides a
│                       │      │                   "complete" fix for CVE-2025-6020. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs           ─ [0]: CWE-22 
│                       │      ├ VendorSeverity   ╭ alma       : 3 
│                       │      │                  ├ oracle-oval: 3 
│                       │      │                  ├ redhat     : 3 
│                       │      │                  ├ rocky      : 3 
│                       │      │                  ╰ ubuntu     : 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 7.8 
│                       │      ├ References       ╭ [0] : https://access.redhat.com/errata/RHSA-2025:14557 
│                       │      │                  ├ [1] : https://access.redhat.com/errata/RHSA-2025:15099 
│                       │      │                  ├ [2] : https://access.redhat.com/errata/RHSA-2025:15100 
│                       │      │                  ├ [3] : https://access.redhat.com/errata/RHSA-2025:15101 
│                       │      │                  ├ [4] : https://access.redhat.com/errata/RHSA-2025:15102 
│                       │      │                  ├ [5] : https://access.redhat.com/errata/RHSA-2025:15103 
│                       │      │                  ├ [6] : https://access.redhat.com/errata/RHSA-2025:15104 
│                       │      │                  ├ [7] : https://access.redhat.com/errata/RHSA-2025:15105 
│                       │      │                  ├ [8] : https://access.redhat.com/errata/RHSA-2025:15106 
│                       │      │                  ├ [9] : https://access.redhat.com/errata/RHSA-2025:15107 
│                       │      │                  ├ [10]: https://access.redhat.com/errata/RHSA-2025:15709 
│                       │      │                  ├ [11]: https://access.redhat.com/errata/RHSA-2025:15827 
│                       │      │                  ├ [12]: https://access.redhat.com/errata/RHSA-2025:15828 
│                       │      │                  ├ [13]: https://access.redhat.com/errata/RHSA-2025:16524 
│                       │      │                  ├ [14]: https://access.redhat.com/security/cve/CVE-2025-8941 
│                       │      │                  ├ [15]: https://bugzilla.redhat.com/2372512 
│                       │      │                  ├ [16]: https://bugzilla.redhat.com/2388220 
│                       │      │                  ├ [17]: https://bugzilla.redhat.com/show_bug.cgi?id=2372512 
│                       │      │                  ├ [18]: https://bugzilla.redhat.com/show_bug.cgi?id=2388220 
│                       │      │                  ├ [19]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-6020 
│                       │      │                  ├ [20]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-20
│                       │      │                  │       25-8941 
│                       │      │                  ├ [21]: https://errata.almalinux.org/9/ALSA-2025-15099.html 
│                       │      │                  ├ [22]: https://errata.rockylinux.org/RLSA-2025:14557 
│                       │      │                  ├ [23]: https://linux.oracle.com/cve/CVE-2025-8941.html 
│                       │      │                  ├ [24]: https://linux.oracle.com/errata/ELSA-2025-15099.html 
│                       │      │                  ├ [25]: https://nvd.nist.gov/vuln/detail/CVE-2025-8941 
│                       │      │                  ╰ [26]: https://www.cve.org/CVERecord?id=CVE-2025-8941 
│                       │      ├ PublishedDate   : 2025-08-13T15:15:41.873Z 
│                       │      ╰ LastModifiedDate: 2025-09-23T20:15:33.927Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : login.defs@1:4.16.0-7ubuntu1 
│                       │      ├ PkgName         : login.defs 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/login.defs@4.16.0-7ubuntu1?arch=all&di
│                       │      │                  │       stro=ubuntu-25.04&epoch=1 
│                       │      │                  ╰ UID : 4016d70dedce9ad0 
│                       │      ├ InstalledVersion: 1:4.16.0-7ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
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
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-1188 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
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
│                       ├ [12] ╭ VulnerabilityID : CVE-2024-56433 
│                       │      ├ PkgID           : passwd@1:4.16.0-7ubuntu1 
│                       │      ├ PkgName         : passwd 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/passwd@4.16.0-7ubuntu1?arch=amd64&dist
│                       │      │                  │       ro=ubuntu-25.04&epoch=1 
│                       │      │                  ╰ UID : 3bc9adb4bf916fa 
│                       │      ├ InstalledVersion: 1:4.16.0-7ubuntu1 
│                       │      ├ Status          : affected 
│                       │      ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                       │      │                  │         b6ba98c37923562c6ba4 
│                       │      │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                       │      │                            1a60c40f64c3148c1317 
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
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs           ─ [0]: CWE-1188 
│                       │      ├ VendorSeverity   ╭ azure : 1 
│                       │      │                  ├ redhat: 1 
│                       │      │                  ╰ ubuntu: 1 
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
│                       ╰ [13] ╭ VulnerabilityID : CVE-2025-45582 
│                              ├ PkgID           : tar@1.35+dfsg-3.1 
│                              ├ PkgName         : tar 
│                              ├ PkgIdentifier    ╭ PURL: pkg:deb/ubuntu/tar@1.35%2Bdfsg-3.1?arch=amd64&distro=
│                              │                  │       ubuntu-25.04 
│                              │                  ╰ UID : a03ee9a61d584e89 
│                              ├ InstalledVersion: 1.35+dfsg-3.1 
│                              ├ Status          : affected 
│                              ├ Layer            ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168b
│                              │                  │         b6ba98c37923562c6ba4 
│                              │                  ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e
│                              │                            1a60c40f64c3148c1317 
│                              ├ SeveritySource  : ubuntu 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2025-45582 
│                              ├ DataSource       ╭ ID  : ubuntu 
│                              │                  ├ Name: Ubuntu CVE Tracker 
│                              │                  ╰ URL : https://git.launchpad.net/ubuntu-cve-tracker 
│                              ├ Title           : tar: Tar path traversal 
│                              ├ Description     : GNU Tar through 1.35 allows file overwrite via directory
│                              │                   traversal in crafted TAR archives, with a certain two-step
│                              │                   process. First, the victim must extract an archive that
│                              │                   contains a ../ symlink to a critical directory. Second, the
│                              │                   victim must extract an archive that contains a critical
│                              │                   file, specified via a relative pathname that begins with the
│                              │                    symlink name and ends with that critical file's name. Here,
│                              │                    the extraction follows the symlink and overwrites the
│                              │                   critical file. This bypasses the protection mechanism of
│                              │                   "Member name contains '..'" that would occur for a single
│                              │                   TAR archive that attempted to specify the critical file via
│                              │                   a ../ approach. For example, the first archive can contain
│                              │                   "x -> ../../../../../home/victim/.ssh" and the second
│                              │                   archive can contain x/authorized_keys. This can affect
│                              │                   server applications that automatically extract any number of
│                              │                    user-supplied TAR archives, and were relying on the
│                              │                   blocking of traversal. This can also affect software
│                              │                   installation processes in which "tar xf" is run more than
│                              │                   once (e.g., when installing a package can automatically
│                              │                   install two dependencies that are set up as untrusted
│                              │                   tarballs instead of official packages). NOTE: the official
│                              │                   GNU Tar manual has an otherwise-empty directory for each
│                              │                   "tar xf" in its Security Rules of Thumb; however,
│                              │                   third-party advice leads users to run "tar xf" more than
│                              │                   once into the same directory. 
│                              ├ Severity        : MEDIUM 
│                              ├ CweIDs           ─ [0]: CWE-24 
│                              ├ VendorSeverity   ╭ redhat: 2 
│                              │                  ╰ ubuntu: 2 
│                              ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L
│                              │                           │           /A:L 
│                              │                           ╰ V3Score : 5.6 
│                              ├ References       ╭ [0]: https://access.redhat.com/security/cve/CVE-2025-45582 
│                              │                  ├ [1]: https://github.com/i900008/vulndb/blob/main/Gnu_tar_vu
│                              │                  │      ln.md 
│                              │                  ├ [2]: https://lists.gnu.org/archive/html/bug-tar/2025-08/msg
│                              │                  │      00012.html 
│                              │                  ├ [3]: https://nvd.nist.gov/vuln/detail/CVE-2025-45582 
│                              │                  ├ [4]: https://www.cve.org/CVERecord?id=CVE-2025-45582 
│                              │                  ├ [5]: https://www.gnu.org/software/tar/ 
│                              │                  ├ [6]: https://www.gnu.org/software/tar/manual/html_node/Inte
│                              │                  │      grity.html 
│                              │                  ├ [7]: https://www.gnu.org/software/tar/manual/html_node/Inte
│                              │                  │      grity.html#Integrity 
│                              │                  ╰ [8]: https://www.gnu.org/software/tar/manual/html_node/Secu
│                              │                         rity-rules-of-thumb.html 
│                              ├ PublishedDate   : 2025-07-11T17:15:37.183Z 
│                              ╰ LastModifiedDate: 2025-08-18T04:15:36.743Z 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages ╭ [0]  ╭ Name      : com.fasterxml.jackson.core:jackson-annotations 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.19.2 
                 │      │            ╰ UID : 616b3ade15e2741b 
                 │      ├ Version   : 2.19.2 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [1]  ╭ Name      : com.fasterxml.jackson.core:jackson-core 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-core@2.19.2 
                 │      │            ╰ UID : eb0a1b87ceaebbe2 
                 │      ├ Version   : 2.19.2 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [2]  ╭ Name      : com.fasterxml.jackson.core:jackson-databind 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.19.2 
                 │      │            ╰ UID : 6027c5181a259e3 
                 │      ├ Version   : 2.19.2 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [3]  ╭ Name      : com.fasterxml.jackson.dataformat:jackson-dataformat-toml 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.fasterxml.jackson.dataformat/jackson-dataformat-toml
                 │      │            │       @2.19.2 
                 │      │            ╰ UID : f187132d4296b98 
                 │      ├ Version   : 2.19.2 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [4]  ╭ Name      : com.github.mwiede:jsch 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.github.mwiede/jsch@2.27.2 
                 │      │            ╰ UID : f0e4991223748277 
                 │      ├ Version   : 2.27.2 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [5]  ╭ Name      : com.github.vertical-blank:sql-formatter 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.github.vertical-blank/sql-formatter@2.0.5 
                 │      │            ╰ UID : 4aa6d74fa002054a 
                 │      ├ Version   : 2.0.5 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [6]  ╭ Name      : com.google.code.gson:gson 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.google.code.gson/gson@2.13.1 
                 │      │            ╰ UID : e51e4f5d991743b4 
                 │      ├ Version   : 2.13.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [7]  ╭ Name      : com.googlecode.juniversalchardet:juniversalchardet 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.googlecode.juniversalchardet/juniversalchardet@1.0.3 
                 │      │            ╰ UID : 59979d47f792d6c8 
                 │      ├ Version   : 1.0.3 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [8]  ╭ Name      : com.jcraft:jsch.agentproxy.connector-factory 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.connector-factory@0.0.9 
                 │      │            ╰ UID : c33f344564a099d2 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [9]  ╭ Name      : com.jcraft:jsch.agentproxy.core 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.core@0.0.9 
                 │      │            ╰ UID : 4be7fe5e595d9eb2 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [10] ╭ Name      : com.jcraft:jsch.agentproxy.jsch 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.jsch@0.0.9 
                 │      │            ╰ UID : 2c09ba989715b29 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [11] ╭ Name      : com.jcraft:jsch.agentproxy.pageant 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.pageant@0.0.9 
                 │      │            ╰ UID : 8affbecb98c67dc0 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [12] ╭ Name      : com.jcraft:jsch.agentproxy.sshagent 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.sshagent@0.0.9 
                 │      │            ╰ UID : 77f3ddb6f8158192 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [13] ╭ Name      : com.jcraft:jsch.agentproxy.svnkit-trilead-ssh2 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.svnkit-trilead-ssh2@0.0.9 
                 │      │            ╰ UID : dfc6f6319fc95cbe 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [14] ╭ Name      : com.jcraft:jsch.agentproxy.usocket-jna 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.usocket-jna@0.0.9 
                 │      │            ╰ UID : 80b49070dfd3f3a7 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [15] ╭ Name      : com.jcraft:jsch.agentproxy.usocket-nc 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.usocket-nc@0.0.9 
                 │      │            ╰ UID : 8ce583c9bcf3a507 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [16] ╭ Name      : com.sun.activation:javax.activation 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.sun.activation/javax.activation@1.2.0 
                 │      │            ╰ UID : 885b1754dac6edf 
                 │      ├ Version   : 1.2.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [17] ╭ Name      : com.sun.mail:javax.mail 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.sun.mail/javax.mail@1.6.2 
                 │      │            ╰ UID : eb67ca13361cdf7e 
                 │      ├ Version   : 1.6.2 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [18] ╭ Name      : com.warrenstrange:googleauth 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.warrenstrange/googleauth@1.5.0 
                 │      │            ╰ UID : abdfc1ca334283c7 
                 │      ├ Version   : 1.5.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [19] ╭ Name      : commons-cli:commons-cli 
                 │      ├ Identifier ╭ PURL: pkg:maven/commons-cli/commons-cli@1.10.0 
                 │      │            ╰ UID : ffefc9129580b7cf 
                 │      ├ Version   : 1.10.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [20] ╭ Name      : commons-codec:commons-codec 
                 │      ├ Identifier ╭ PURL: pkg:maven/commons-codec/commons-codec@1.19.0 
                 │      │            ╰ UID : 9a9278de888f0833 
                 │      ├ Version   : 1.19.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [21] ╭ Name      : commons-io:commons-io 
                 │      ├ Identifier ╭ PURL: pkg:maven/commons-io/commons-io@2.20.0 
                 │      │            ╰ UID : a80b795c06f99084 
                 │      ├ Version   : 2.20.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [22] ╭ Name      : commons-logging:commons-logging 
                 │      ├ Identifier ╭ PURL: pkg:maven/commons-logging/commons-logging@1.3.5 
                 │      │            ╰ UID : 78410c5141b86fa 
                 │      ├ Version   : 1.3.5 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [23] ╭ Name      : commons-net:commons-net 
                 │      ├ Identifier ╭ PURL: pkg:maven/commons-net/commons-net@3.11.1 
                 │      │            ╰ UID : 1af550b4580218d2 
                 │      ├ Version   : 3.11.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [24] ╭ Name      : de.vandermeer:asciilist-j7 
                 │      ├ Identifier ╭ PURL: pkg:maven/de.vandermeer/asciilist-j7@1.0.0 
                 │      │            ╰ UID : d4e586b2e07acda4 
                 │      ├ Version   : 1.0.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [25] ╭ Name      : de.vandermeer:asciitable-j7 
                 │      ├ Identifier ╭ PURL: pkg:maven/de.vandermeer/asciitable-j7@1.0.1 
                 │      │            ╰ UID : 272a590ba643367f 
                 │      ├ Version   : 1.0.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [26] ╭ Name      : dnsjava:dnsjava 
                 │      ├ Identifier ╭ PURL: pkg:maven/dnsjava/dnsjava@3.6.3 
                 │      │            ╰ UID : 4b5e6e63b1733dfa 
                 │      ├ Version   : 3.6.3 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [27] ╭ Name      : io.jsonwebtoken:jjwt-api 
                 │      ├ Identifier ╭ PURL: pkg:maven/io.jsonwebtoken/jjwt-api@0.12.6 
                 │      │            ╰ UID : d29f8391f035ed2d 
                 │      ├ Version   : 0.12.6 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [28] ╭ Name      : io.jsonwebtoken:jjwt-gson 
                 │      ├ Identifier ╭ PURL: pkg:maven/io.jsonwebtoken/jjwt-gson@0.12.6 
                 │      │            ╰ UID : d9f6af7ee5867b6f 
                 │      ├ Version   : 0.12.6 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [29] ╭ Name      : io.jsonwebtoken:jjwt-impl 
                 │      ├ Identifier ╭ PURL: pkg:maven/io.jsonwebtoken/jjwt-impl@0.12.6 
                 │      │            ╰ UID : d35dbad1bf5f0f67 
                 │      ├ Version   : 0.12.6 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [30] ╭ Name      : io.sigpipe:jbsdiff 
                 │      ├ Identifier ╭ PURL: pkg:maven/io.sigpipe/jbsdiff@1.0 
                 │      │            ╰ UID : 3ad9c9a90222e030 
                 │      ├ Version   : 1.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [31] ╭ Name      : jakarta.activation:jakarta.activation-api 
                 │      ├ Identifier ╭ PURL: pkg:maven/jakarta.activation/jakarta.activation-api@1.2.2 
                 │      │            ╰ UID : 84baa18824622446 
                 │      ├ Version   : 1.2.2 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [32] ╭ Name      : javax.xml.bind:jaxb-api 
                 │      ├ Identifier ╭ PURL: pkg:maven/javax.xml.bind/jaxb-api@2.3.1 
                 │      │            ╰ UID : 68f09018f4453b95 
                 │      ├ Version   : 2.3.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [33] ╭ Name      : jline:jline 
                 │      ├ Identifier ╭ PURL: pkg:maven/jline/jline@2.14.6 
                 │      │            ╰ UID : 6930774a112e73bc 
                 │      ├ Version   : 2.14.6 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [34] ╭ Name      : org.apache.commons:commons-collections4 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.apache.commons/commons-collections4@4.5.0 
                 │      │            ╰ UID : b6f26728bc972346 
                 │      ├ Version   : 4.5.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [35] ╭ Name      : org.apache.commons:commons-compress 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.apache.commons/commons-compress@1.28.0 
                 │      │            ╰ UID : 645d61b3c78fd14e 
                 │      ├ Version   : 1.28.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [36] ╭ Name      : org.apache.commons:commons-csv 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.apache.commons/commons-csv@1.14.0 
                 │      │            ╰ UID : 604b08d649d68838 
                 │      ├ Version   : 1.14.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [37] ╭ Name      : org.apache.commons:commons-email 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.apache.commons/commons-email@1.6.0 
                 │      │            ╰ UID : 1cdb7e2822178209 
                 │      ├ Version   : 1.6.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [38] ╭ Name      : org.apache.commons:commons-lang3 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.apache.commons/commons-lang3@3.18.0 
                 │      │            ╰ UID : 46de2531678b981 
                 │      ├ Version   : 3.18.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [39] ╭ Name      : org.apache.commons:commons-math3 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.apache.commons/commons-math3@3.6.1 
                 │      │            ╰ UID : 3992f1c5b6195e89 
                 │      ├ Version   : 3.6.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [40] ╭ Name      : org.eclipse.jetty.websocket:jetty-websocket-core-client 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty.websocket/jetty-websocket-core-client@
                 │      │            │       12.1.1 
                 │      │            ╰ UID : e1a5d577714445f3 
                 │      ├ Version   : 12.1.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [41] ╭ Name      : org.eclipse.jetty.websocket:jetty-websocket-core-common 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty.websocket/jetty-websocket-core-common@
                 │      │            │       12.1.1 
                 │      │            ╰ UID : 1f68f28f376545f0 
                 │      ├ Version   : 12.1.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [42] ╭ Name      : org.eclipse.jetty.websocket:jetty-websocket-jetty-api 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty.websocket/jetty-websocket-jetty-api@12
                 │      │            │       .1.1 
                 │      │            ╰ UID : f8f3c943251b09e4 
                 │      ├ Version   : 12.1.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [43] ╭ Name      : org.eclipse.jetty.websocket:jetty-websocket-jetty-client 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty.websocket/jetty-websocket-jetty-client
                 │      │            │       @12.1.1 
                 │      │            ╰ UID : adeeca375aa2e56 
                 │      ├ Version   : 12.1.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [44] ╭ Name      : org.eclipse.jetty.websocket:jetty-websocket-jetty-common 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty.websocket/jetty-websocket-jetty-common
                 │      │            │       @12.1.1 
                 │      │            ╰ UID : a47c5fec6d8d33c6 
                 │      ├ Version   : 12.1.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [45] ╭ Name      : org.eclipse.jetty:jetty-client 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty/jetty-client@12.1.1 
                 │      │            ╰ UID : 2a53b4854a5f4c26 
                 │      ├ Version   : 12.1.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [46] ╭ Name      : org.eclipse.jetty:jetty-http 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty/jetty-http@12.1.1 
                 │      │            ╰ UID : c4eaa9c6ed827c7f 
                 │      ├ Version   : 12.1.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [47] ╭ Name      : org.eclipse.jetty:jetty-io 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty/jetty-io@12.1.1 
                 │      │            ╰ UID : 59c1c0b60d065a06 
                 │      ├ Version   : 12.1.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [48] ╭ Name      : org.eclipse.jetty:jetty-util 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty/jetty-util@12.1.1 
                 │      │            ╰ UID : 609c496af4c9731e 
                 │      ├ Version   : 12.1.1 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [49] ╭ Name      : org.fusesource.hawtjni:hawtjni-runtime 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.hawtjni/hawtjni-runtime@1.17 
                 │      │            ╰ UID : 368c86360d5d2d6e 
                 │      ├ Version   : 1.17 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [50] ╭ Name      : org.fusesource.jansi:jansi 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi@1.18 
                 │      │            ╰ UID : 28003612621d63f7 
                 │      ├ Version   : 1.18 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [51] ╭ Name      : org.fusesource.jansi:jansi-freebsd32 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-freebsd32@1.8 
                 │      │            ╰ UID : 75689643540ac0cc 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [52] ╭ Name      : org.fusesource.jansi:jansi-freebsd64 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-freebsd64@1.8 
                 │      │            ╰ UID : cdf9cdca8706e16f 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [53] ╭ Name      : org.fusesource.jansi:jansi-linux32 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-linux32@1.8 
                 │      │            ╰ UID : 3d49c0eb4793e1f4 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [54] ╭ Name      : org.fusesource.jansi:jansi-linux64 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-linux64@1.8 
                 │      │            ╰ UID : 8b11f3d47b9658b2 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [55] ╭ Name      : org.fusesource.jansi:jansi-native 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-native@1.8 
                 │      │            ╰ UID : c89c538fba388aa2 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [56] ╭ Name      : org.fusesource.jansi:jansi-osx 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-osx@1.8 
                 │      │            ╰ UID : b0bc0de50b8059ad 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [57] ╭ Name      : org.fusesource.jansi:jansi-windows32 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-windows32@1.8 
                 │      │            ╰ UID : 7c1a51c801be878e 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [58] ╭ Name      : org.fusesource.jansi:jansi-windows64 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-windows64@1.8 
                 │      │            ╰ UID : 6c10b179e44aabcb 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [59] ╭ Name      : org.semver4j:semver4j 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.semver4j/semver4j@6.0.0 
                 │      │            ╰ UID : b4987f502c5eba1f 
                 │      ├ Version   : 6.0.0 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [60] ╭ Name      : org.slf4j:slf4j-api 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.slf4j/slf4j-api@2.0.17 
                 │      │            ╰ UID : 669ca5d81bb821ff 
                 │      ├ Version   : 2.0.17 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [61] ╭ Name      : org.slf4j:slf4j-nop 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.slf4j/slf4j-nop@2.0.17 
                 │      │            ╰ UID : 5e42b1280e39632b 
                 │      ├ Version   : 2.0.17 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [62] ╭ Name      : org.snmp4j:snmp4j 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.snmp4j/snmp4j@3.9.6 
                 │      │            ╰ UID : 9cf3d6b9898ef004 
                 │      ├ Version   : 3.9.6 
                 │      ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                 │      │            │         62c6ba4 
                 │      │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                 │      │                      48c1317 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ╰ [63] ╭ Name      : org.snmp4j:snmp4j-agent 
                        ├ Identifier ╭ PURL: pkg:maven/org.snmp4j/snmp4j-agent@3.8.2 
                        │            ╰ UID : 9ed630f1f75d1f9b 
                        ├ Version   : 3.8.2 
                        ├ Layer      ╭ Digest: sha256:6771e82896a3919929614a8b608bb300896fa92d168bb6ba98c379235
                        │            │         62c6ba4 
                        │            ╰ DiffID: sha256:c26e4e03d3068572d5bd18544e9b94b5affabda5c26e1a60c40f64c31
                        │                      48c1317 
                        ╰ FilePath  : openaf/openaf.jar 
````
